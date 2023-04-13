#!/usr/bin/node
/* converts from base ten to any base passed in */
exports.converter = function (base) {
  return function (arg) {
    return arg.toString(base);
  };
};
