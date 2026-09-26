CREATE TABLE IF NOT EXISTS content_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  collection TEXT NOT NULL,
  path TEXT NOT NULL,
  slug TEXT NOT NULL,
  title TEXT NOT NULL,
  status TEXT DEFAULT 'draft',
  body TEXT,
  metadata_json TEXT,
  cover_image TEXT,
  published_at TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(collection, path)
);
CREATE INDEX IF NOT EXISTS idx_content_items_collection_slug ON content_items(collection, slug);
CREATE INDEX IF NOT EXISTS idx_content_items_path ON content_items(path);

CREATE VIEW IF NOT EXISTS entries AS
SELECT * FROM content_items WHERE collection = 'entries';

CREATE VIEW IF NOT EXISTS articles AS
SELECT * FROM content_items WHERE collection = 'articles';

CREATE VIEW IF NOT EXISTS photoindexes AS
SELECT * FROM content_items WHERE collection = 'photoindexes';
