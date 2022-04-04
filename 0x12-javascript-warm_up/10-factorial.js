#!/usr/bin/node

const var1 = parseInt(process.argv[2]);
console.log(factorial(var1));
function factorial (var1) {
  if (!var1) {
    return 1;
  } else {
    return (var1 * factorial(var1 - 1));
  }
}
