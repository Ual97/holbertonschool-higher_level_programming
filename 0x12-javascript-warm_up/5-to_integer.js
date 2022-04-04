#!/usr/bin/node

const var1 = (process.argv[2]);
if (Number.isInteger(parseInt(var1))) {
  console.log('My number: ' + parseInt(var1));
} else {
  console.log('Not a number');
}
