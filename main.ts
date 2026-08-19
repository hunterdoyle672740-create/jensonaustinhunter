scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairLarge, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    info.setScore(120 - 2 * coconut_2)
    game.gameOver(true)
})
let coconut_2 = 0
let Player_1 = sprites.create(img`
        . . . . . . . . . . . . . . . .
        . . . . c c c c . . . . . . . .
        . . c c 5 5 5 5 c c . . . . . .
        . c 5 5 5 5 5 5 5 5 c . . . . .
        c 5 5 5 5 5 1 f 5 5 5 c . . . .
        c 5 5 5 5 5 f f 5 5 5 5 c . . .
        c 5 5 5 5 5 5 5 5 5 5 5 c . . .
        c c b b 1 b 5 5 5 5 5 5 d c . .
        c 5 3 3 3 5 5 5 5 5 d d d c . .
        . b 5 5 5 5 5 5 5 5 d d d c . .
        . . c b b c 5 5 b d d d d c c .
        . c b b c 5 5 b b d d d d c d c
        . c c c c c c d d d d d d d d c
        . . . c c c c d 5 5 b d d d c .
        . . c c c c c b 5 5 b c c c . .
        . . c b b b c d 5 5 b c . . . .
        `, SpriteKind.Player)
Player_1.setScale(0.6, ScaleAnchor.Middle)
controller.moveSprite(Player_1)
tiles.setCurrentTilemap(tilemap`
    level1
    `)
tiles.placeOnRandomTile(Player_1, sprites.dungeon.stairNorth)
scene.cameraFollowSprite(Player_1)
coconut_2 = 0
forever(function on_forever() {
    
    info.changeScoreBy(1)
    coconut_2 += 1
    pause(1000)
})
