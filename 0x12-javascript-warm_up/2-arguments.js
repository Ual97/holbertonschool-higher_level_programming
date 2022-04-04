#!/usr/bin/node

const var1 = 'No argument';
const var2 = 'Argument found';
const var3 = 'Arguments found';
console.log(process.argv.length);
if (process.argv.length === 2) {
  console.log(var1);
} else if (process.argv.length === 3) {
  console.log(var2);
} else if (process.argv.length > 3) {
  console.log(var3);
}
