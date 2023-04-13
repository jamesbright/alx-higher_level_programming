#!/usr/bin/node
// returns elements * index of array
const list = require('./100-data').list;
const list2 = list.map((el, index) => el * index);
console.log(list);
console.log(list2);
