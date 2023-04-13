#!/usr/bin/node
// sorts dictionary of occurrences
const dict = require('./101-data').dict;
const dict2 = {};
Object.keys(dict).map(function (key, index) {
  if (dict2[dict[key]] === undefined) {
    dict2[dict[key]] = [];
  }
  return dict2[dict[key]].push(key);
});
console.log(dict2);
