// Import the 'request' module
const request = require('request')

// Get the API URL from the command-line arguments
const url = process.argv[2]

// Send a GET request to the Star Wars API
request(url, function (error, response, body) {
  // If an error occurred, print it to the console
  if (error) {
    console.error('Error:', error)
  } else {
    // Parse the JSON response body into a JavaScript object
    const films = JSON.parse(body).results

    // Initialize a counter for the number of films
    let count = 0

    // Iterate over each film
    films.forEach(film => {
      // Iterate over each character in the film
      film.characters.forEach(character => {
        // If the character is Wedge Antilles (character ID 18), increment the counter
        if (character.endsWith('/18/')) {
          count++
        }
      })
    })

    // Print the number of films where Wedge Antilles is present
    console.log(count)
  }
})