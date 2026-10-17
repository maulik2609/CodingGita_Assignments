//Question -no. 1 ------------

let num = 14;

let result = num % 7 === 0
    ? "Divisible by 7"
    : "Not Divisible by 7";

console.log(result);


//Question -no. 2 ------------

let temperature = 32;

let weather = temperature >= 30
    ? "Hot Day"
    : "Pleasant Day";

console.log(weather);


//Question -no. 3 ------------

let str = "";

let answer = str === ""
    ? "Empty String"
    : "String has content";

console.log(answer);


//Question -no. 4 ------------

let age = 16;

let category = age < 13
    ? "Child"
    : age <= 19
        ? "Teenager"
        : "Adult";

console.log(category);


//Question -no. 5 ------------

let a = 25;
let b = 40;
let c = 15;

let greatest = a > b
    ? (a > c ? a : c)
    : (b > c ? b : c);

console.log("Greatest:", greatest);


//Question -no. 6 ------------

let marks = 68;

let grade = marks >= 75
    ? "Distinction"
    : marks >= 60
        ? "First Class"
        : marks >= 50
            ? "Second Class"
            : marks >= 35
                ? "Pass"
                : "Fail";

console.log(grade);


//Question -no. 7 ------------

let number = -7;

let type = number === 0
    ? "Zero"
    : number > 0
        ? (number % 2 === 0 ? "Positive Even" : "Positive Odd")
        : (number % 2 === 0 ? "Negative Even" : "Negative Odd");

console.log(type);


//Question -no. 8 ------------

let year = 2024;

let leap = year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)
    ? "Leap Year"
    : "Not a Leap Year";

console.log(leap);


//Question -no. 9 ------------

let role = "admin";
let action = "edit";

let message = role === "admin"
    ? (action === "delete"
        ? "Admin Delete"
        : action === "edit"
            ? "Admin Edit"
            : "Admin Other")
    : role === "user"
        ? (action === "view"
            ? "User View"
            : "User Restricted")
        : "Invalid Role";

console.log(message);


//Question -no. 10 ------------

let cartTotal = 6000;

let order = cartTotal >= 5000
    ? { discount: 20, payable: cartTotal * 0.80 }
    : cartTotal >= 2000
        ? { discount: 10, payable: cartTotal * 0.90 }
        : cartTotal >= 1000
            ? { discount: 5, payable: cartTotal * 0.95 }
            : { discount: 0, payable: cartTotal };

console.log("Discount:", order.discount + "%");
console.log("Final Amount: ₹" + order.payable);