basic.show_string("Hello!")
basic.show_icon(IconNames.SKULL)

def on_forever():
    music.play(music.create_sound_expression(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    TPBot.set_travel_speed(TPBot.DriveDirection.FORWARD, 50)
basic.forever(on_forever)
