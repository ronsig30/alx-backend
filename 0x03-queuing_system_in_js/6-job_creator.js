import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Define job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a push notification message',
};

// Create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Event listeners for the job
job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
