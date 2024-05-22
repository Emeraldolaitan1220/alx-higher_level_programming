#!/usr/bin/env node
// Write a script that display the status code of a GET request.
const request = require('request');
// import request

const url = process.argv[2];
// get the url from the command line

request(url, function (error, response, body) {
  if (error) {
    console.log('Error:', error);
  } else {
    console.log('Status:', response.statusCode);
  }
});