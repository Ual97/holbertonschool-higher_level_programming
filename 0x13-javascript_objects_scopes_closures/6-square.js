#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      for (let i = 0; i < this.width; i++) {
        console.log('X'.repeat(this.height));
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log('C'.repeat(this.height));
      }
    }
  }
};
