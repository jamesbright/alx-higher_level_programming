#!/usr/bin/node
const argv = process.argv;
if (argv.length < 4) {
  console.log(0);
} else {
  const secondBiggest = argv.slice(2).sort((a, b) => b - a)[1];
  console.log(secondBiggest);
}
