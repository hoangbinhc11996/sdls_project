#ifndef laser_control_h
#define laser_control_h 


void laser_init();
void laser_off(uint8_t laser_bit);
void laser_on(uint8_t laser_bit);
void laser_run(uint8_t mode, uint8_t value);

#endif
