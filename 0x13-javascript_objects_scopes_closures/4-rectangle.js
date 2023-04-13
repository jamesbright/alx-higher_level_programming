#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // method prints rectangle
  print () {
    let x = '';
    let i = 0;
    let j = 0;
    while (i < this.width) {
      x += 'X';
      i++;
    }
    while (j < this.height) {
      console.log(x);
      j++;
    }
  }

  // method rotates rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // method doubles rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
