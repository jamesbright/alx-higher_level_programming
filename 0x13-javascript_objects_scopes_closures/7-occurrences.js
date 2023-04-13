#!/usr/bin/node
// find number of occurences of an element
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (el, index) {
    if (el === searchElement) {
      count++;
    }
  });
  return count;
};
