#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
const prop = 'value';
myObject[prop] = 89;
console.log(myObject);
