#!/usr/bin/node

const var1 = parseInt(process.argv[2]);
const var2 = parseInt(process.argv[3]);
if (Number.isInteger(var1) && Number.isInteger(var2)) {
  console.log(var1 + var2);
} else {
    console.log('NaN');
}
