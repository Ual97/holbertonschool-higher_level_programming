!/usr/bin/node

const var1 = 'No argument';
const var2 = process.argv[2];
if (!process.argv[2]) {
  console.log(var1);
} else {
  console.log(var2);
}
