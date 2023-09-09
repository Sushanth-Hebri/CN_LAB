#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define BUCKET_SIZE 10 // Bucket size (maximum number of tokens it can hold)
#define OUTPUT_RATE 2  // Output rate (tokens removed per second)

void leakyBucket(int input_rate) {
    int bucket = 0; // Initialize the bucket with no tokens

    for (int second = 1; second <= 10; second++) {
        printf("Second %d: ", second);

        // Add incoming tokens at the specified input rate
        bucket += input_rate;

        if (bucket > BUCKET_SIZE) {
            bucket = BUCKET_SIZE; // Limit the bucket size
        }

        printf("Incoming: %d, Bucket: %d, ", input_rate, bucket);

        // Determine how many tokens can be sent out (up to the output rate)
        int tokens_out = (bucket > OUTPUT_RATE) ? OUTPUT_RATE : bucket;

        printf("Outgoing: %d\n", tokens_out);

        // Remove the sent tokens from the bucket
        bucket -= tokens_out;

        sleep(1); // Sleep for 1 second to simulate real-time
    }
}

int main() {
    int input_rate;

    printf("Enter input rate (tokens per second): ");
    scanf("%d", &input_rate);

    printf("\nRunning the leaky bucket algorithm...\n\n");

    leakyBucket(input_rate);

    return 0;
}
