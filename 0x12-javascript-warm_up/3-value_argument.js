#!/usr/bin/node
const numargs = process.argv;
if (process.argv[2] === undefined) {
    console.log("No arguments");
} else {
    console.log("Argument(s) found");
}