#!/usr/bin/node

function factorial (num) {
  if (num === 1 || num === 0) {
    return 1;
  } else if (isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
