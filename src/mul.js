// file: mul.js

// Import the native add-on module:
const addon = require( './build/Release/addon.node' );

// Compute the product of two integers:
const res = addon( 5, 10 );
console.log( 'The product of %d and %d is %d', 5, 10, res );
