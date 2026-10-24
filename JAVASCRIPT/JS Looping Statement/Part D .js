
//Question - no. 1 ------------

for (let i = 50; i >= 1; i--) {
    if (i % 3 == 0 && i % 9 != 0) {
        console.log(i);
    }
}


//Question - no. 2 ------------

let num = 4729;
let product = 1;

for (; num > 0; num = Math.floor(num / 10)) {
    let digit = num % 10;

    if (digit % 2 != 0) {
        product = product * digit;
    }
}
console.log(product);


//Question - no. 3 ------------

let str = "Programming";
let result = "";

for (let i = str.length - 1; i >= 0; i--) {
    if (!"aeiouAEIOU".includes(str[i])) {
        result = result + str[i];
    }
}
console.log(result);


//Question - no. 4 ------------

let a = 0, b = 1;
let fib = [];

for (let i = 0; i < 15; i++) {
    fib[i] = a;
    let c = a + b;
    a = b;
    b = c;
}

for (let i = 14; i >= 0; i--) {
    console.log(fib[i]);
}


//Question - no. 5 ------------

let n = 1221;
let original = n;
let rev = 0;

for (; n > 0; n = Math.floor(n / 10)) {
    rev = rev * 10 + n % 10;
}

if (original == rev) {
    console.log("Palindrome");
} else {
    console.log("Not Palindrome");
}


//Question - no. 6 ------------

let arr = [12, 45, 7, 23, 56, 89, 34];
let max = 0;

for (let i = arr.length - 1; i >= 0; i--) {
    if (arr[i] < 50 && arr[i] > max) {
        max = arr[i];
    }
}
console.log(max);


//Question - no. 7 ------------

let temp = [32, 28, 41, 19, 35, 27, 38];
let count = 0;

for (let i = temp.length - 1; i >= 0; i--) {
    if (temp[i] < 30) {
        count++;
    }
}
console.log(count);


//Question - no. 8 ------------

let decimal = 13;
let binary = "";

for (; decimal > 0; decimal = Math.floor(decimal / 2)) {
    binary = binary + (decimal % 2);
}
console.log(binary);


//Question - no. 9 ------------

let scores = [90, 85, 70, 95, 60, 88, 75];

for (let i = scores.length - 1; i >= 0; i--) {
    if (scores[i] > 80) {
        console.log(scores[i], i);
        break;
    }
}


//Question - no. 10 ------------

for (let i = 40; i >= 1; i--) {
    if (Math.sqrt(i) % 1 == 0) {
        continue;
    }
    console.log(i);
}
