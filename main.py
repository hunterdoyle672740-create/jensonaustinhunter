def on_a_pressed():
    global lkfjadsflkj
    lkfjadsflkj = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . 2 2 . . . . . . .
            . . . . . . . f f . . . . . . .
            . . . . . . . 2 2 . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        Player_1,
        50,
        50)
    lkfjadsflkj.follow(myEnemy)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    info.set_score(120 - 2 * coconut_2)
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_large,
    on_overlap_tile)

def on_on_overlap(sprite2, otherSprite):
    game.game_over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

lkfjadsflkj: Sprite = None
coconut_2 = 0
myEnemy: Sprite = None
Player_1: Sprite = None
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
myEnemy = sprites.create(img("""
        ........................
        ........................
        ........................
        ........................
        ..........ffff..........
        ........ff1111ff........
        .......fb111111bf.......
        .......f11111111f.......
        ......fd11111111df......
        ......fd11111111df......
        ......fddd1111dddf......
        ......fbdbfddfbdbf......
        ......fcdcf11fcdcf......
        .......fb111111bf.......
        ......fffcdb1bdffff.....
        ....fc111cbfbfc111cf....
        ....f1b1b1ffff1b1b1f....
        ....fbfbffffffbfbfbf....
        .........ffffff.........
        ...........fff..........
        ........................
        ........................
        ........................
        ........................
        """),
    SpriteKind.enemy)
myEnemy.follow(Player_1, 30)
myEnemy.set_scale(0.4, ScaleAnchor.MIDDLE)
Player_1.set_scale(0.6, ScaleAnchor.MIDDLE)
controller.move_sprite(Player_1)
tiles.set_current_tilemap(tilemap("""
    level1
    """))
tiles.place_on_random_tile(Player_1, sprites.dungeon.stair_north)
scene.camera_follow_sprite(Player_1)
coconut_2 = 0
myEnemy.set_position(160, 0)

def on_forever():
    global coconut_2
    info.change_score_by(1)
    coconut_2 += 1
    pause(1000)
forever(on_forever)
