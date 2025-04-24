from machine import Pin, ADC, PWM
from time import sleep

# Set up the LDR sensor on ADC pin
ldr = ADC(26)  # ADC pin 26 for LDR

# PIR Motion Sensor connected to GPIO8
pir = Pin(8, Pin.IN)

# LEDs connected to GPIO pins 2-7 (6 LEDs in total)
led_pins = [2, 3, 4, 5, 6, 7]
leds = [PWM(Pin(pin)) for pin in led_pins]

# Set PWM frequency for all LEDs
for led in leds:
    led.freq(1000)

# Define brightness levels
LOW_BRIGHTNESS = 32768
HIGH_BRIGHTNESS = 65535
DARK_THRESHOLD = 30000

while True:
    # Read the LDR sensor value (light intensity)
    light_value = ldr.read_u16()

    # Read the PIR motion sensor status (0 or 1)
    motion_detected = pir.value()

    # Control LEDs based on light and motion detection
    if light_value < DARK_THRESHOLD:  # It’s dark
        if motion_detected:  # Motion detected
            for led in leds:
                led.duty_u16(HIGH_BRIGHTNESS)
        else:  # No motion
            for led in leds:
                led.duty_u16(LOW_BRIGHTNESS)
    else:  # It’s bright
        for led in leds:
            led.duty_u16(0)  # Turn off LEDs

    sleep(0.1)  # Wait for 100ms before checking again
