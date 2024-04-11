#!/usr/bin/node
const argument = process.argv[2];
if (!isNaN(argument)) {
    const num = parseInt(argument);
    if (!isNaN(num)) {
        console.log("My number:", num);
    } else {
        console.log("Not a number");
    }
} else {
    console.log("Not a number");
}
