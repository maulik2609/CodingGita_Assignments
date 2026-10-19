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