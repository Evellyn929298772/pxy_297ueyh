def on_gesture_shake():
    for index in range(2):
        music.play(music.string_playable("C5 A B G E F C D ", 149),
            music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_leds("""
    # . # # #
    # . # . .
    # . # # #
    # . # . .
    # . # # #
    """)
basic.show_leds("""
    # . . . #
    # # . # #
    # # # # #
    . # # # .
    . . # . .
    """)