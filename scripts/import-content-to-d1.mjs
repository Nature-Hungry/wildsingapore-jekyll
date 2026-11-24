import fs from 'node:fs';
import path from 'node:path';
import { parse as parseYAML } from 'yaml';

const root = process.cwd();
const collections = [
  { name: 'entries', dir: '_entries' },
  { name: 'articles', dir: '_articles' },
  { name: 'photoindexes', dir: '_photoindexes' }
];

const parseMarkdownFrontMatter = (fileText) => {
  if (!fileText.startsWith('---')) return { metadata: {}, body: fileText };
  const match = fileText.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!match) return { metadata: {}, body: fileText };

  const [, frontMatter, body] = match;
  let metadata = {};

  try {
    metadata = parseYAML(frontMatter) || {};
  } catch (error) {
    metadata = {};
  }

  return { metadata, body: body || '' };
};

const isContentFile = (filename) => /\.(md|markdown|html|htm)$/.test(filename);

const sanitizeForSql = (value) => {
  if (value === null || value === undefined) return '';
  if (typeof value === 'string') return value.replace(/'/g, "''");
  return String(value).replace(/'/g, "''");
};

const records = [];

for (const collection of collections) {
  const dir = path.join(root, collection.dir);
  if (!fs.existsSync(dir)) continue;

  const walk = (currentDir) => {
    const entries = fs.readdirSync(currentDir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(currentDir, entry.name);
      if (entry.isDirectory()) {
        walk(fullPath);
      } else if (entry.isFile() && isContentFile(entry.name)) {
        const fileText = fs.readFileSync(fullPath, 'utf8');
        const { metadata, body } = parseMarkdownFrontMatter(fileText);
        const relativePath = path.relative(root, fullPath).replace(/\\/g, '/');
        const slug = metadata.slug || path.basename(fullPath, path.extname(fullPath));
        const title = metadata.title || slug.replace(/[-_]/g, ' ');
        const collectionName = collection.name;
        const metadataJson = JSON.stringify(metadata, null, 2);
        const publishedAt = metadata.date || metadata.updated || metadata.published_at || new Date().toISOString();
        const status = metadata.status || 'published';
        const coverImage = metadata.coverimg || metadata.cover_image || '';

        records.push({
          collection: collectionName,
          path: relativePath,
          slug: slug,
          title: title,
          status,
          body: body || '',
          metadata_json: metadataJson,
          cover_image: coverImage,
          published_at: publishedAt.toString()
        });
      }
    }
  };

  walk(dir);
}

const sql = [
  'BEGIN TRANSACTION;',
  ...records.map((row) => `INSERT INTO content_items (collection, path, slug, title, status, body, metadata_json, cover_image, published_at) VALUES ('${sanitizeForSql(row.collection)}', '${sanitizeForSql(row.path)}', '${sanitizeForSql(row.slug)}', '${sanitizeForSql(row.title)}', '${sanitizeForSql(row.status)}', '${sanitizeForSql(row.body)}', '${sanitizeForSql(row.metadata_json)}', '${sanitizeForSql(row.cover_image)}', '${sanitizeForSql(row.published_at)}');`),
  'COMMIT;'
].join('\n');

fs.mkdirSync(path.join(root, 'db'), { recursive: true });
fs.writeFileSync(path.join(root, 'db', 'seed.sql'), sql, 'utf8');
console.log(`Prepared ${records.length} rows for Cloudflare D1 import.`);
console.log('SQL file written to db/seed.sql');
