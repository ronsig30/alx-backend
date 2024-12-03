import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Event Handler for successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

//Event handler for error
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});