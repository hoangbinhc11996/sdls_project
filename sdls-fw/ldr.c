#include "ldr.h"

void ldr_init(void){
 ADCSRA |= ((1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0));    //16Mhz/128 = 125Khz the ADC reference clock
 ADMUX |= (1<<REFS0);                //Voltage reference from Avcc (5v)
 ADCSRA |= (1<<ADEN);                //Turn on ADC
 ADCSRA |= (1<<ADSC);                //Do an initial conversion because this one is the slowest and to ensure that everything is up and running
}
 
uint16_t ldr_read(uint8_t tool){
 ADMUX &= 0xF0;                    //Clear the older channel that was read
 ADMUX |= tool;                //Defines the new ADC channel to be read
 ADCSRA |= (1<<ADSC);                //Starts a new conversion
 while(ADCSRA & (1<<ADSC));            //Wait until the conversion is done
 return ADCW;                    //Returns the ADC value of the chosen channel
}

void print_ldr(uint8_t tool){
 if (tool >=0){
 char buffer[5];
 itoa(ldr_read(tool), buffer, 10);
 printString(buffer);
 printString("\r\n");
 }
}
