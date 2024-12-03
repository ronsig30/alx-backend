import { createClient, print } from 'redis';

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

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, value) => {
        if (err) {
            console.log(`Error: ${err.message}`);
        } else {
            console.log(value);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');