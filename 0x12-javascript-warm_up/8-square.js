#!/usr/bin/node

const var1 = parseInt(process.argv[2]);
const var2 = 'X';
if (Number.isInteger(var1)) {
  for (let i = 0; i < var1; i++) {
    console.log(var2.repeat(var1));
  }
} else {
  console.log('Missing size');
}
