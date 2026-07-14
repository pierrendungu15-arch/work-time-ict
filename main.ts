let safe = 0
basic.forever(function () {
    safe = pins.digitalReadPin(DigitalPin.P0)
    if (safe == 1) {
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else if (false) {
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
})
