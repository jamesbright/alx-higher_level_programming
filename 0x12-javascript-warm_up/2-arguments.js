#!/usr/bin/node
const argv = process.argv;
if (argv.length > 3) {
  console.log('Arguments found');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
