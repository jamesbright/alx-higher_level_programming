#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
const argv = process.argv;
console.log(add(argv[2], argv[3]));
