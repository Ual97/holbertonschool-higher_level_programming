#!/usr/bin/node

const fname = process.argv[2];
const text = process.argv[3];
const fs = require('fs');
fs.writeFile(fname, text, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
