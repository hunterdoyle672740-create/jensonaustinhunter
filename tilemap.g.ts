// Auto-generated code. Do not edit.
namespace myTiles {
    //% fixedInstance jres blockIdentity=images._tile
    export const transparency16 = image.ofBuffer(hex``);

    helpers._registerFactory("tilemap", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "level1":
            case "level1":return tiles.createTilemap(hex`10001000030a0501050505060606010106050505030105010105050606030106060505050301050401010501010101010105050503010105040105010404010401010105030302050101050107010106010501050303010701050501070404060105050503030105010501010701010201050505010301050101020707010404040505050101010504010407070105030305050503030208080101010702050101010105030301010801040107010501050401050303030101010501070101010501010501010301040405010704040405010505030103010303030101010103050105050301010103030304040401010501010103040404030303040404040105030309`, img`
2 . 2 . 2 2 2 2 2 2 . . 2 2 2 2 
2 . 2 . . 2 2 2 2 2 . 2 2 2 2 2 
2 . 2 2 . . 2 . . . . . . 2 2 2 
2 . . 2 2 . 2 . 2 2 . 2 . . . 2 
2 2 . 2 . . 2 . 2 . . 2 . 2 . 2 
2 2 . 2 . 2 2 . 2 2 2 2 . 2 2 2 
2 2 . 2 . 2 . . 2 . . . . 2 2 2 
. 2 . 2 . . . 2 2 . 2 2 2 2 2 2 
. . . 2 2 . 2 2 2 . 2 2 2 2 2 2 
2 2 . 2 2 . . . 2 . 2 . . . . 2 
2 2 . . 2 . 2 . 2 . 2 . 2 2 . 2 
2 2 2 . . . 2 . 2 . . . 2 . . 2 
. . 2 . 2 2 2 . 2 2 2 2 2 . 2 2 
2 . 2 . 2 2 2 . . . . 2 2 . 2 2 
2 . . . 2 2 2 2 2 2 . . 2 . . . 
2 2 2 2 2 2 2 2 2 2 2 . 2 2 2 . 
`, [myTiles.transparency16,sprites.dungeon.floorDark0,sprites.dungeon.floorDark1,sprites.dungeon.greenOuterWest0,sprites.dungeon.greenOuterSouth0,sprites.dungeon.greenOuterEast0,sprites.dungeon.greenOuterNorth0,sprites.dungeon.greenOuterWest1,sprites.dungeon.greenOuterEast1,sprites.dungeon.stairNorth,sprites.dungeon.stairLarge], TileScale.Sixteen);
        }
        return null;
    })

    helpers._registerFactory("tile", function(name: string) {
        switch(helpers.stringTrim(name)) {
            case "transparency16":return transparency16;
        }
        return null;
    })

}
// Auto-generated code. Do not edit.
