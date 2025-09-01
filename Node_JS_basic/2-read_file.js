const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0);
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
    console.log(`Number of students: ${total}`);
    for (const field of order) {
      const count = groups[field].length;
      const list = groups[field].join(', ');
      console.log(`Number of students in ${field}: ${count}. List: ${list}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
