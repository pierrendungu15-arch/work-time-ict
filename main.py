safe = 0

def on_forever():
    global safe
    safe = pins.digital_read_pin(DigitalPin.P3)
    if safe == 1:
        pins.digital_write_pin(DigitalPin.P1, 1)
    elif False:
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)
