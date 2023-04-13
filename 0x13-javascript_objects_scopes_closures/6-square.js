#!/usr/bin/node
const Square5 = require('./5-square.js');
module.exports = class Square extends Square5 {
  charPrint (c = 'X') {
    let chars = '';
    let i = 0;
    let j = 0;

    while (i < this.width) {
      chars += c;
      i++;
    }
    while (j < this.height) {
      console.log(chars);
      j++;
    }
  }
};
