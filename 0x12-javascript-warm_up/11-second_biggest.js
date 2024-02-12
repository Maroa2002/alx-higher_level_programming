#!/usr/bin/node

function secLargest (args) {
  if (args.length <= 1) {
    return 0;
  } else {
    const nums = args.map(Number).filter((n, index, array) => array.indexOf(n) === index);
    nums.sort((a, b) => b - a);
    return nums[1];
  }
}

const numArgs = process.argv.slice(2);
console.log(secLargest(numArgs));
