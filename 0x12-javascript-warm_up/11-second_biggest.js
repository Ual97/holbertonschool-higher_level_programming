#!/usr/bin/node

let i = 0;
if (process.argv.length <= 2) {
  console.log('0');
} else {
  const arr = process.argv;
  const sortedarr = arr.sort(function(a, b){return a - b});
  for (sortedarr[i]; sortedarr[null]; i++) {
    if (Number.isInteger(sortedarr[i])) {
      parseInt(sortedarr[i]);
    }
  } console.log(sortedarr[i - 1]);
}
