#!/usr/bin/env node
const fs = require('fs');
const { argv } = require('process');
fs.readFile(process.argv[2], process.argv[3], 'utf8', (err, data) => {
    if (err) {
        console.log(err);
        return;
    }
 });