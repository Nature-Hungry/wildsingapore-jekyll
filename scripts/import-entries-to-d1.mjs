import fs from 'node:fs';
import path from 'node:path';

const repoRoot = process.cwd();
const filePath = path.join(repoRoot, 'scripts', 'entries-sample.json');
const sqlPath = path.join(repoRoot, 'db', 'schema.sql');

if (!fs.existsSync(filePath)) {
  console.error('Missing seed data at scripts/entries-sample.json. Run the extraction step first.');
  process.exit(1);
}

const entries = JSON.parse(fs.readFileSync(filePath, 'utf8'));
const schema = fs.readFileSync(sqlPath, 'utf8');

console.log('D1 seed script ready.');
console.log('Schema file:', sqlPath);
console.log('Records to import:', entries.length);
console.log('SQL setup to run:');
console.log(schema);
console.log('Sample insert example:');
console.log(`INSERT INTO entries (slug, title, category, status, summary, body, keywords, taxonomy_json, cover_image, published_at) VALUES ('${entries[0]?.slug || 'sample'}', '${entries[0]?.title || 'Sample'}', '${entries[0]?.category || ''}', 'published', '${(entries[0]?.summary || '').replace(/'/g, "''")}', '${(entries[0]?.body || '').replace(/'/g, "''").slice(0, 80)}', '${(entries[0]?.keywords || '').replace(/'/g, "''")}', '${(entries[0]?.taxonomy_json || '').replace(/'/g, "''")}', '${(entries[0]?.cover_image || '').replace(/'/g, "''")}', '${(entries[0]?.published_at || '').replace(/'/g, "''")}');`);
