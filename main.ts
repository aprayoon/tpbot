basic.showString("Hello!")
basic.showIcon(IconNames.Skull)
basic.forever(function () {
    TPBot.headlightColor(0xff0000)
    TPBot.setTravelSpeed(TPBot.DriveDirection.Forward, 50)
    TPBot.stopCar()
})
