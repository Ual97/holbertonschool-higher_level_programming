#!/usr/bin/node

exports.esrever = function (list) {
  const arrlen = list.length;
  const newlist = [];
  for (let i = arrlen - 1; i >= 0; i--) {
    newlist.push(list[i]);
  }
  return newlist;
};
