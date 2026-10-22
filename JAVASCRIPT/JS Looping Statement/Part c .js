//Part C-a] break inside a for Loop

//Question -no. 1 ------------

let arr1 = [2, 4, 6, 7, 9, 10];

for (let i = 0; i < arr1.length-1; i++) {
    if (arr1[i] === 7) {
        console.log("Index =", i);
        break;
    }
}


//Question -no. 2 ------------

let correctPassword = "1234";
let password = "";

for (let i = 1; i <= 5; i++) {
    password = "1111";

    if (password === correctPassword) {
        console.log("Access granted");
        break;
    }

    if (i === 5) {
        console.log("Account locked");
    }
}


//Question -no. 3 ------------

let sum = 0;

for (let i = 1; i++;){
    sum += i;

    if (sum > 100) {
        console.log("Last number added =", i);
        break;
    }
}



//Question -no. 4 ------------

let names = ["Rahul", "Amit", "Sahil", "Karan", "Suresh"];

for (let i = 0; i < names.length; i++) {
    if (names[i] === "S") {
        console.log(names[i]);
        break;
    }
}

//Part C-b] continue inside a for Loop

//Question -no. 1 ------------

for (let i = 1; i <= 30; i++) {
    if (i % 4 === 0) {
        continue;
    }

    console.log(i);
}


//Question -no. 2 ------------

let numbers = [10, -5, 20, -3, 15, -8];
let positiveSum = 0;

for (let i = 0; i < numbers.length-1; i++) {
    if (numbers[i] < 0) {
        continue;
    }

    positiveSum += numbers[i];
}

console.log("Positive Sum =", positiveSum);


//Question -no. 3 ------------

let str = "Hello World";

for (let i = 0; i < str.length; i++) {
    if (str[i] === " ") {
        continue;
    }
    console.log(str[i]);
}


//Question -no. 4 ------------

for (let i = 1; i <= 12; i++) {
    let product = 6 * i;

    if (product % 5 === 0) {
        continue;
    }

    console.log("6 x " + i + " = " + product);
}


//Question -no. 5 ------------

let ages = [12, 18, 25, 15, 30, 17, 22];

for (let i = 0; i < ages.length; i++) {
    if (ages[i] < 18) {
        continue;
    }

    console.log(ages[i]);
}
