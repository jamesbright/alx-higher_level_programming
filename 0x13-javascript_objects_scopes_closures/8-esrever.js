#!/usr/bin/node
// returns a reversed list
exports.esrever = function (list) {
  let i = 0;
  const list2 = list.slice();
  while (i < list.length) {
    list[i] = list2[list.length - i - 1];
    i++;
  }
  return list;
};
