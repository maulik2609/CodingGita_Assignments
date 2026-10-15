//Question -no. 1 ------------
let name = "Rahul";
console.log(typeof name);

//Question -no. 2 ------------
let age = 25;
console.log(typeof age);

//Question -no. 3 ------------
let isStudent = true;
console.log(typeof isStudent);

//Question -no. 4 ------------
let city;
console.log(typeof city);

//Question -no. 5 ------------
console.log(typeof null);

//Question -no. 6 ------------
console.log(typeof 42);       // number
console.log(typeof "Hello");  // string
console.log(typeof true);     // boolean
console.log(typeof undefined); // undefined

//Question -no. 7 ------------
console.log(typeof null); // object
console.log(typeof {});   // object
console.log(typeof []);   // object

//Question -no. 8 ------------
console.log(typeof NaN);          // number
console.log(typeof Infinity);     // number
console.log(typeof function(){}); // function

//Question -no. 9 ------------
let price = 99.99;
let message = "Welcome";
let isActive = false;

console.log("price:", typeof price);
console.log("message:", typeof message);
console.log("isActive:", typeof isActive);

//Question -no. 10 ------------
let value = null;
console.log(typeof value); // object
console.log(typeof value === "object"); // true

//Question -no. 11 ------------
console.log(typeof typeof 100);   // string
console.log(typeof typeof "Hi");  // string
console.log(typeof typeof true);  // string

//Question -no. 12 ------------
let a = 10;
let b = "10";
console.log(typeof a === typeof b); // false
console.log(typeof a == typeof b);  // false

//Question -no. 13 ------------
console.log(typeof null === "object"); // true
console.log(typeof [] === "object");   // true
console.log(typeof {} === "object");   // true

//Question -no. 14 ------------
let x;
console.log(typeof x); // undefined
x = null;
console.log(typeof x); // object
x = 0;
console.log(typeof x); // number

//Question -no. 15 ------------
console.log(typeof NaN === "number");      // true
console.log(typeof Infinity === "number"); // true
console.log(typeof (1 / 0));               // number