#!/usr/bin/node
const var1 = parseInt(process.argv[2]);
function factorial(var1) {
  if (var1 === 0) {
    console.log('NaN');
  } else {
    console.log(var1 * factorial(var1 - 1));
  }
}
