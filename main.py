def on_overlap_tile(sprite, location):
    info.set_score(120 - 2 * coconut_2)
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_large,
    on_overlap_tile)

coconut_2 = 0
Player_1 = sprites.create(img("""
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
        """),
    SpriteKind.player)
Player_1.set_scale(0.6, ScaleAnchor.MIDDLE)
controller.move_sprite(Player_1)
tiles.set_current_tilemap(tilemap("""
    level1
    """))
tiles.place_on_random_tile(Player_1, sprites.dungeon.stair_north)
scene.camera_follow_sprite(Player_1)
coconut_2 = 0

def on_forever():
    global coconut_2
    info.change_score_by(1)
    coconut_2 += 1
    pause(1000)
forever(on_forever)
