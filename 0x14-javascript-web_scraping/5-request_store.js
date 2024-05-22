#!/usr/bin/env node
// This script is meant to be run as a standalone Node.js script

// Import the 'request' module for making HTTP requests
const request = require('request')

// Get the movie ID from the command-line arguments
// The ID is expected to be the second argument when running this script
const id = process.argv[2]

// The URL is based on the Star Wars API and includes the movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${id}`

// Send a GET request to the Star Wars API

request(url, function (error, response, body) {
  // If an error occurred during the request, print it to the console
  if (error) {
    console.error('Error:', error)
  } else {
    // If the request was successful, parse the JSON response body into a JavaScript object
    const film = JSON.parse(body)

    // Print the title of the movie to the console
    
    console.log(film.title)
  }
})