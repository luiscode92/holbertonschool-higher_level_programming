#!/usr/bin/node

if (process.argv[2]) {
  const x = process.argv[2];
  for (var i = 1; i <= x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
