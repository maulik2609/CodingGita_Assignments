//Question -no. 1 ------------

let temp = [28, 32, 25, 40, 18, 35];
let count = 0;

for (let i = 0; i < temp.length; i++) {
    if (temp[i] > 30) {
        count++;
    }
}
console.log(count);


//Question -no. 2 ------------

let num = 4729;
let sum = 0;

for (; num > 0; num = Math.floor(num / 10)) {
    sum += num % 10;
}
console.log(sum);


//Question -no. 3 ------------

for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0 && i % 7 !== 0) {
        console.log(i);
    }
}


//Question -no. 4 ------------

let str = "JavaScript";
let result = "";

for (let i = 0; i < str.length; i++) {
    let ch = str[i].toLowerCase();

    if (
        ch !== "a" &&
        ch !== "e" &&
        ch !== "i" &&
        ch !== "o" &&
        ch !== "u"
    ) {
        result += str[i];
    }
}
console.log(result);


//Question -no. 5 ------------

let arr = [12, 45, 23, 67, 34, 89, 10];
let largest = arr[0];

for (let i = 1; i < arr.length; i++) {
    if (arr[i] > largest) {
        largest = arr[i];
    }
}
console.log(largest);


//Question -no. 6 ------------

let number = 28;
let divisorSum = 0;

for (let i = 1; i < number; i++) {
    if (number % i === 0) {
        divisorSum += i;
    }
}

if (divisorSum === number) {
    console.log("Perfect Number");
} else {
    console.log("Not a Perfect Number");
}


//Question -no. 7 ------------

let value = 1;

for (let i = 1; i <= 8; i++) {
    console.log(value);
    value *= 2;
}

