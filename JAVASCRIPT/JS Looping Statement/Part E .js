//Question -1. ------------

let num = 1;
for (let i = 1; i <= 4; i++) {
    for (let j = 1; j <= i; j++) {
        process.stdout.write(num + " ");
        num++;
    }
    console.log();
}


//Question -2. ------------

for (let i = 1; i <= 4; i++) {
    for (let j = 1; j <= i; j++) {
        process.stdout.write(i + " ");
    }
    console.log();
}


//Question -3. ------------

let n = 1;
for (let i = 1; i <= 4; i++) {
    for (let j = 1; j <= i; j++) {
        process.stdout.write(n + " ");
        n++;
    }
    console.log();
}


//Question -4. ------------

for (let i = 1; i <= 4; i++) {
    let bag = "";
    for (let j = 1; j <= 4; j++) {
        if (i === 1 || i === 4 || j === 1 || j === 4) {
            bag += "* ";
        } else {
            bag += "  ";
        }
    }
    console.log(bag);
}


//Question -5. ------------

for (let i = 1; i <= 6; i++) {
    let bag = "";
    for (let j = 1; j <= i; j++) {
        if (i % 2 === 1) {
            bag += "# ";
        } else {
            bag += "$ ";
        }
    }
    console.log(bag);
}


//Question -6. ------------

for (let i = 1; i <= 5; i++) {
    let bag = "";
    for (let j = 1; j <= i; j++) {
        bag += String.fromCharCode(64 + j) + " ";
    }
    console.log(bag);
}


//Question -7. ------------

for (let i = 1; i <= 5; i++) {
    let bag = "";
    for (let j = 1; j <= i; j++) {
        if (j === 1 || j === i || i === 5) {
            bag += "* ";
        } else {
            bag += "  ";
        }
    }
    console.log(bag);
}


//Question -8. ------------

for (let i = 5; i >= 1; i--) {
    let bag = "";
    for (let j = 1; j <= i; j++) {
        bag += "*";
    }
    console.log(bag);
}


//Question -9. ------------

for (let i = 5; i >= 1; i--) {
    let bag = "";
    for (let j = 1; j <= i; j++) {
        bag += i + " ";
    }
    console.log(bag);
}


//Question -10. ------------

for (let i = 5; i >= 1; i--) {
    let bag = "";
    for (let j = 1; j <= i; j++) {
        bag += j + " ";
    }
    console.log(bag);
}


//Question -11. ------------

let value = 15;
for (let i = 5; i >= 1; i--) {
    let bag = "";
    for (let j = 1; j <= i; j++) {
        bag += value + " ";
        value--;
    }
    console.log(bag);
}


//Question -12. ------------

for (let i = 5; i >= 1; i--) {
    let bag = "";
    for (let j = 1; j <= i; j++) {
        if (i === 5 || j === 1 || j === i) {
            bag += "* ";
        } else {
            bag += "  ";
        }
    }
    console.log(bag);
}


//Question -13. ------------

for (let i = 1; i <= 5; i++) {
    let bag = "";
    for (let j = 1; j <= 5; j++) {
        if (i !== j) {
            bag += "* ";
        } else {
            bag += "  ";
        }
    }
    console.log(bag);
}


//Question -14. ------------

for (let i = 1; i <= 5; i++) {
    for (let j = 1; j <= 10; j++) {
        if ((i * j) % 2 === 0) {
            console.log(i + " x " + j + " = " + (i * j));
        }
    }
    console.log();
}


//Question -15. ------------

for (let i = 1; i <= 3; i++) {
    let bag = "";

    for (let j = 1; j <= 3 - i; j++) {
        bag += "  ";
    }

    for (let j = 1; j <= i; j++) {
        bag += j + " ";
    }

    for (let j = i - 1; j >= 1; j--) {
        bag += j + " ";
    }

    console.log(bag);
}