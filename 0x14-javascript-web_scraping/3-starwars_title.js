#!/usr/bin/env node
// Import the 'request' module
const request = require('request')

// Get the movie ID from the command-line arguments
const id = process.argv[2]

// Construct the URL for the API request
const url = `https://swapi-api.alx-tools.com/api/films/${id}`

// Send a GET request to the Star Wars API
request(url, function (error, response, body) {
  // If an error occurred, print it to the console
  if (error) {
    console.error('Error:', error)
  } else {
    // Parse the JSON response body into a JavaScript object
    const film = JSON.parse(body)

    // Print the title of the movie
    console.log(film.title)
  }
})