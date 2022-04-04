#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv;
  const sortedarr = arr.sort(function (a, b) { return a - b; });
  const arrlen = sortedarr.length;
  console.log(sortedarr[arrlen - 2]);
}
