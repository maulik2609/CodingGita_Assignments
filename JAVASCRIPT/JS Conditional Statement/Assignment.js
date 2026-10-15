// A] if Statement

//Question -1 ------------

let n = 25;
if (n % 5 == 0) {
    console.log("Divisible by 5");
}

//Question -2 ------------

let age = 65;
if (age >= 60) {
    console.log("Senior Citizen");
}

//Question -3 ------------

let num = 150;
if (num > 100) {
    console.log("Big Number");
}

//Question -4 ------------

let temperature = 5;
if (temperature < 10) {
    console.log("Very Cold");
}

//Question -5 ------------

let marks = 100;
if (marks == 100) {
    console.log("Perfect Score");
}

//Question -6 ------------

let number = -10;
if (number < 0) {
    console.log("Negative Number");
}

//Question -7 ------------

let str = "";
if (str == "") {
    console.log("No input provided");
}

//Question -8 ------------

let year = 1900;
if (year % 100 == 0) {
    console.log("Century Year");
}

//Question -9 ------------

let value = 8;
if (value > 0 && value % 2 == 0) {
    console.log("Positive Even Number");
}

//Question -10 ------------

let marks1 = 75;
if (marks1 >= 35 && marks1 <= 100) {
    console.log("Valid Marks");
}


// B] if...else Statement

//Question -1 ------------

let n1 = 7;
if (n1 % 2 == 0) {
    console.log("Even");
} else {
    console.log("Odd");
}

//Question -2 ------------

let age1 = 20;
if (age1 >= 18) {
    console.log("Eligible");
} else {
    console.log("Not Eligible");
}

//Question -3 ------------

let n2 = -5;
if (n2 >= 0) {
    console.log("Positive");
} else {
    console.log("Negative");
}

//Question -4 ------------

let marks2 = 40;
if (marks2 >= 35) {
    console.log("Pass");
} else {
    console.log("Fail");
}

//Question -5 ------------

let ch = "A";
if (ch >= "A" && ch <= "Z") {
    console.log("Uppercase Letter");
} else {
    console.log("Not Uppercase Letter");
}

//Question -6 ------------

let n3 = 10;
if (n3 % 3 == 0) {
    console.log("Divisible by 3");
} else {
    console.log("Not Divisible by 3");
}

//Question -7 ------------

let password = "admin123";
if (password == "admin123") {
    console.log("Login Successful");
} else {
    console.log("Incorrect Password");
}

//Question -8 ------------

let year1 = 2024;
if (year1 % 4 == 0) {
    console.log("Leap Year");
} else {
    console.log("Not a Leap Year");
}

//Question -9 ------------

let a = 25;
let b = 30;
if (a > b) {
    console.log(a);
} else {
    console.log(b);
}

//Question -10 ------------

let n4 = 0;
if (n4 > 0) {
    console.log("Positive");
} else {
    if (n4 < 0) {
        console.log("Negative");
    } else {
        console.log("Zero");
    }
}