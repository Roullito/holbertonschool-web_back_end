console.log('Welcome to Holberton School, what is your name?');
process.stdin.setEncoding('utf8');

let inputReceived = false;

process.stdin.on('data', (chunk) => {
  if (!inputReceived) {
    const name = chunk.trim();
    console.log(`Your name is: ${name}`);
    inputReceived = true;
    if (process.stdin.isTTY) {
      process.stdin.resume();
    } else {
      process.stdin.emit('end');
    }
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
