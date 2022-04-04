#!/usr/bin/node

const var1 = 'C is fun';
const var2 = parseInt(var1);
if (Number.isInteger(parseInt(var1))) {
  for (let i = 0; i < var2; i++) {
    console.log(var1);
  }
}
else {
  console.log('Missing number of occurrences');
}
