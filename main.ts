input.onGesture(Gesture.Shake, function () {
    for (let index = 0; index < 2; index++) {
        music.play(music.stringPlayable("C5 A B G E F C D ", 149), music.PlaybackMode.UntilDone)
    }
})
basic.showLeds(`
    # . # # #
    # . # . .
    # . # # #
    # . # . .
    # . # # #
    `)
basic.showLeds(`
    # . . . #
    # # . # #
    # # # # #
    . # # # .
    . . # . .
    `)
