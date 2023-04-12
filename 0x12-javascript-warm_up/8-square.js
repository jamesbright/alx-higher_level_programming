#!/usr/bin/node
const argv = process.argv;
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  let i = argv[2];
  while (i > 0) {
    console.log('X'.repeat(argv[2]));
    i--;
  }
}
