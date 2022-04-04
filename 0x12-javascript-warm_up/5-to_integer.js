#!/usr/bin/node

const var1 = (process.argv[2]);
if (Number.isInteger(var1) === true) {
  console.log('My number: ' + parseInt(var1));
} else {
  console.log('Not a number');
}
