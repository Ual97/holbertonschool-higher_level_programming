#!/usr/bin/node
const var1 = parseInt(process.argv[2]);
function factorial(var1) {
  if (!var1) {
    console.log('1');
  } else {
    console.log(var1 * factorial(var1 - 1));
  }
}
