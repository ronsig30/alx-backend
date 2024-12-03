import { createClient, print } from 'redis';
import { promisify } from 'util';

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
//promisify the `get` method of the Redis client.
const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.log(`Error: ${err.message}`);
    }
}


(async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();