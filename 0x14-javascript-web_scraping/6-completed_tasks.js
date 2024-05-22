// Import the 'request' module
const request = require('request')

// Get the API URL from the command-line arguments
const url = process.argv[2]

// Send a GET request to the API
request(url, function (error, response, body) {
  // If an error occurred, print it to the console
  if (error) {
    console.error('Error:', error)
  } else {
    // Parse the JSON response body into a JavaScript object
    const todos = JSON.parse(body)

    // Create an empty object to store the task counts
    const taskCounts = {}

    // Iterate over each todo
    todos.forEach(todo => {
      // If the todo is completed
      if (todo.completed) {
        // If the user's ID is not yet in the taskCounts object, add it with a count of 1
        if (!taskCounts[todo.userId]) {
          taskCounts[todo.userId] = 1
        } else {
          // Otherwise, increment the count for the user's ID
          taskCounts[todo.userId]++
        }
      }
    })

    // Print the number of completed tasks for each user ID
    for (const userId in taskCounts) {
      console.log(`User ${userId}: ${taskCounts[userId]}`)
    }
  }
})