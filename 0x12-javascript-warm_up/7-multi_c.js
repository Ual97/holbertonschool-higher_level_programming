#!/usr/bin/node

const var1 = 'C is fun';
const var2 = parseInt(process.argv[2]);
if (Number.isInteger(var2)) {
  for (let i = 0; i < var2; i++) {
    console.log(var1);
  }
} else {
  console.log('Missing number of occurrences');
}
