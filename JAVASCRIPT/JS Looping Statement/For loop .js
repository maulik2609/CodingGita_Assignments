//Question -no. 1 -----------

for (let i = 1; i <= 15; i++) {
    console.log(i);
}

//Question -no. 2 ------------

for (let i = 2; i <= 40; i += 2) {
    console.log(i);
}

//Question -no. 3 ------------

for (let i = 1; i <= 35; i += 2) {
    console.log(i);
}

//Question -no. 4 ------------

let total = 0;

for (let i = 1; i <= 10; i++) {
    total = total + (i * 10);
}

console.log("Total savings after 10 days: ₹" + total);

//Question -no. 5 ------------

for (let i = 1; i <= 10; i++) {
    console.log("12 x " + i + " = " + (12 * i));
}

//Question -no. 6 ------------

let water = 0;

for (let i = 1; i <= 7; i++) {
    water = water + 3;
    console.log("Day " + i + ": " + water + " glasses");
}

//Question -no. 7 ------------

for (let i = 1; i <= 10; i++) {
    console.log(i + " chocolates = ₹" + (i * 15));
}

//Question -no. 8 ------------

let sum = 0;

for (let i = 2; i <= 30; i += 2) {
    sum = sum + i;
}

console.log("Sum of even numbers: " + sum);

//Question -no. 9 ------------

for (let i = 1; i <= 7; i++) {
    console.log("Day " + i + ": " + (i * 5) + " push-ups");
}

//Question -no. 10 ------------

for (let i = 1; i <= 8; i++) {
    if (i === 1) {
        console.log(i + " person: ₹" + (i * 150));
    } else {
        console.log(i + " people: ₹" + (i * 150));
    }
}


//PART -B 

//Question -no. 1 ------------

let temperatures = [28, 32, 25, 40, 18, 35];
let count = 0;

for (let i = 0; i < temperatures.length-1; i++) {
    if (temperatures[i] > 30) {
        count++;
    }
}

console.log(count);


//Question -no. 2 ------------

let num = 4729;
let summ = 0;

for (; num > 0; num =(num / 10)) {
    summ += num % 10;
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
    let ch = str[i];

    if (ch !== "a" && ch !== "e" && ch !== "i" &&
        ch !== "o" && ch !== "u") {
        result += str[i];
    }
}

console.log(result);


//Question -no. 5 ------------

let arr = [12, 45, 23, 67, 34, 89, 10];
let largest = arr[0];

for (let i = 1; i < arr.length-1; i++) {
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



//Question -no. 9 ------------

let scores = [45, 78, 90, 32, 56, 88];
let totals = 0;

for (let i = 0; i < scores.length; i++) {
    totals+= scores[i];
}

let average = total / scores.length;
let aboveAverage = 0;

for (let i = 0; i < scores.length; i++) {
    if (scores[i] > average) {
        aboveAverage++;
    }
}

console.log("Average =", average);
console.log("Above Average =", aboveAverage);



