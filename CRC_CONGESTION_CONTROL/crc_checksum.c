#include <stdio.h>
#include <stdint.h>

// CRC-CCITT parameters
#define CRC_CCITT_POLY 0x1021
#define CRC_CCITT_INITIAL 0xFFFF

// Function to calculate CRC-CCITT checksum
uint16_t calculate_crc_ccitt(uint8_t *data, int length) {
    uint16_t crc = CRC_CCITT_INITIAL;
    for (int i = 0; i < length; i++) {
        crc ^= (uint16_t)data[i] << 8;
        for (int j = 0; j < 8; j++) {
            if (crc & 0x8000) {
                crc = (crc << 1) ^ CRC_CCITT_POLY;
            } else {
                crc <<= 1;
            }
        }
    }
    return crc;
}

int main() {
    uint8_t data[] = {0x12, 0x34, 0x56, 0x78}; // Replace with your data
    int data_length = sizeof(data) / sizeof(data[0]);

    uint16_t crc_ccitt = calculate_crc_ccitt(data, data_length);

    printf("Data: ");
    for (int i = 0; i < data_length; i++) {
        printf("%02X ", data[i]);
    }

    printf("\nCRC-CCITT Checksum: %04X\n", crc_ccitt);

    return 0;
}
