#!/usr/bin/node

const var1 = 'No argument';
if (process.argv.length <= 2) {
  console.log(var1);
} else {
  console.log(process.argv[3])
}
