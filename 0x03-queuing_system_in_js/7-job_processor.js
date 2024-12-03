import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

/**
 * Function to send notifications
 * @param {string} phoneNumber - The phone number to send the notification to
 * @param {string} message - The message to send
 * @param {object} job - The job object
 * @param {function} done - Callback function to indicate completion or failure
 */
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100); // Start tracking progress at 0%
  
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100); // Update progress to 50%
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done(); // Job completed successfully
}

// Create a queue
const queue = kue.createQueue();

// Process jobs in the 'push_notification_code_2' queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
