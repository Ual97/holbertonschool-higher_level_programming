#!/usr/bin/node

const var1 = 'No argument';
const var2 = 'Argument found';
const var3 = 'Arguments found';
if (process.argv) {
  console.log(var1);
} else if (process.argv === 1) {
  console.log(var2);
} else if (process.argv > 1) {
console.log(var3);
}
