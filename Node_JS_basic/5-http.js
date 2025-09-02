const http = require('http');
const fs = require('fs');

const DB_PATH = process.argv[2];

function parseStudents(data) {
  const lines = data
    .split('\n')
    .map((l) => l.trim())
    .filter((l) => l.length > 0);

  if (lines.length <= 1) {
    return { total: 0, order: [], groups: {} };
  }

  const header = lines[0];
  const rows = lines.slice(1);
  const cols = header.split(',').map((c) => c.trim());
  const idxFirst = cols.indexOf('firstname');
  const idxField = cols.indexOf('field');
  const groups = Object.create(null);
  const order = [];
  let total = 0;
  for (const row of rows) {
    const cells = row.split(',').map((c) => c.trim());
    const firstname = cells[idxFirst];
    const field = cells[idxField];
    if (!groups[field]) {
      groups[field] = [];
      order.push(field);
    }
    groups[field].push(firstname);
    total += 1;
  }

  return { total, order, groups };
}

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
    return;
  }
  if (req.url === '/students') {
    let body = 'This is the list of our students\n';
    fs.readFile(DB_PATH, 'utf8', (err, data) => {
      if (err) {
        body += 'Cannot load the database';
        res.statusCode = 200;
        res.end(body);
        return;
      }
      const { total, order, groups } = parseStudents(data);
      body += `Number of students: ${total}\n`;
      for (const field of order) {
        const count = groups[field].length;
        const list = groups[field].join(', ');
        body += `Number of students in ${field}: ${count}. List: ${list}\n`;
      }
      res.statusCode = 200;
      res.end(body);
    });
  }
});

app.listen(1245, () => {
  console.log('Server running at http://localhost:1245/');
});
module.exports = app;
