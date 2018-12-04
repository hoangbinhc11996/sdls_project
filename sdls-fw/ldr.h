#ifndef laser_control_h
#define laser_control_h 

#include <avr/io.h>
#include <stdlib.h>
#define F_CPU 16000000UL
#include <util/delay.h>
#define BAUDRATE 9600
#define BAUD_PRESCALLER (((F_CPU / (BAUDRATE * 16UL))) - 1)

void ldr_init(void);
uint16_t ldr_read(uint8_t channel);

#endif
