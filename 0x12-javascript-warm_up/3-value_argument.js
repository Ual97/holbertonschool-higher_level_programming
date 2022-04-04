#!/usr/bin/node

const var1 = 'No argument';
const var2 = process.argv[3];
console.log(var2);
if (process.argv.length <= 2) {
  console.log(var1);
} else {
  console.log(process.argv[3])
}
