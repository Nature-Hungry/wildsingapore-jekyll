const json = (body, status = 200) =>
  new Response(JSON.stringify(body), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    }
  });

const normalizeCollection = (collection) => {
  if (!collection) return 'entries';
  const normalized = String(collection).trim().toLowerCase();
  return ['entries', 'articles', 'photoindexes'].includes(normalized) ? normalized : 'entries';
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === 'OPTIONS') {
      return new Response(null, {
        status: 204,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        }
      });
    }

    if (url.pathname === '/api/content/health') {
      return json({ ok: true, database: env.ENTRIES_DB ? 'connected' : 'missing' });
    }

    if (url.pathname === '/api/content') {
      const { results } = await env.ENTRIES_DB.prepare(
        'SELECT * FROM content_items ORDER BY collection, title LIMIT 200'
      ).all();
      return json({ items: results });
    }

    if (url.pathname.startsWith('/api/content/')) {
      const parts = url.pathname.replace(/^\/api\/content\//, '').split('/');
      const collection = normalizeCollection(parts[0]);
      const slug = parts[1] ? decodeURIComponent(parts[1]) : null;

      if (request.method === 'GET') {
        if (!slug) {
          const { results } = await env.ENTRIES_DB.prepare(
            'SELECT * FROM content_items WHERE collection = ? ORDER BY title LIMIT 200'
          ).bind(collection).all();
          return json({ collection, items: results });
        }

        const row = await env.ENTRIES_DB.prepare(
          'SELECT * FROM content_items WHERE collection = ? AND slug = ?'
        ).bind(collection, slug).first();

        if (!row) return json({ error: 'not found' }, 404);
        return json({ collection, item: row });
      }

      if (request.method === 'POST' || request.method === 'PUT') {
        const payload = await request.json();
        const item = {
          collection,
          path: payload.path || `${collection}/${payload.slug || 'untitled'}`,
          slug: payload.slug || 'untitled',
          title: payload.title || 'Untitled',
          status: payload.status || 'draft',
          body: payload.body || '',
          metadata_json: JSON.stringify(payload.metadata || {}),
          cover_image: payload.cover_image || '',
          published_at: payload.published_at || new Date().toISOString()
        };

        if (request.method === 'POST') {
          await env.ENTRIES_DB.prepare(`
            INSERT INTO content_items (collection, path, slug, title, status, body, metadata_json, cover_image, published_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
          `).bind(
            item.collection,
            item.path,
            item.slug,
            item.title,
            item.status,
            item.body,
            item.metadata_json,
            item.cover_image,
            item.published_at
          ).run();
          return json({ ok: true, item }, 201);
        }

        await env.ENTRIES_DB.prepare(`
          UPDATE content_items
          SET path = ?, slug = ?, title = ?, status = ?, body = ?, metadata_json = ?, cover_image = ?, published_at = ?, updated_at = CURRENT_TIMESTAMP
          WHERE collection = ? AND slug = ?
        `).bind(
          item.path,
          item.slug,
          item.title,
          item.status,
          item.body,
          item.metadata_json,
          item.cover_image,
          item.published_at,
          collection,
          slug || item.slug
        ).run();

        return json({ ok: true, item });
      }

      if (request.method === 'DELETE') {
        await env.ENTRIES_DB.prepare('DELETE FROM content_items WHERE collection = ? AND slug = ?').bind(collection, slug).run();
        return json({ ok: true, collection, slug });
      }
    }

    return json({ error: 'not found' }, 404);
  }
};
