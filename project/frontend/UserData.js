// MongoDB Playground
// To disable this template go to Settings | MongoDB | Use Default Template For Playground.
// Make sure you are connected to enable completions and to be able to run a playground.
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.
// The result of the last command run in a playground is shown on the results panel.
// By default the first 20 documents will be returned with a cursor.
// Use 'console.log()' to print to the debug output.
// For more documentation on playgrounds please refer to
// https://www.mongodb.com/docs/mongodb-vscode/playgrounds/

// Select the database to use.
use('yourDatabaseName'); // Replace 'yourDatabaseName' with your actual database name

// Insert a few documents into the users collection.
db.getCollection('users').insertMany([
  { 'name': 'John Doe', 'email': 'john@example.com', 'password': 'password123', 'createdAt': new Date() },
  { 'name': 'Jane Smith', 'email': 'jane@example.com', 'password': 'password123', 'createdAt': new Date() },
  { 'name': 'Alice Johnson', 'email': 'alice@example.com', 'password': 'password123', 'createdAt': new Date() },
  { 'name': 'Bob Brown', 'email': 'bob@example.com', 'password': 'password123', 'createdAt': new Date() },
  { 'name': 'Charlie Green', 'email': 'charlie@example.com', 'password': 'password123', 'createdAt': new Date() }
]);

// Run a find command to view all users created today.
const usersCreatedToday = db.getCollection('users').find({
  createdAt: { $gte: new Date(new Date().setHours(0, 0, 0, 0)) }
}).count();

// Print a message to the output window.
console.log(`${usersCreatedToday} users were created today.`);

// Here we run an aggregation to count the number of users created.
db.getCollection('users').aggregate([
  // Group the users by day of creation.
  { $group: { _id: { $dateToString: { format: "%Y-%m-%d", date: "$createdAt" } }, totalUsers: { $sum: 1 } } }
]).toArray().forEach(result => console.log(result));
