from devLevel import LEVEL
# cell = str(input("Enter A Tile ID:"))

for cell, row in LEVEL:
    for cell, col in LEVEL:
        x=0
        y=0
        match cell:
            case'0':
                print("BreakableBlock")
                # tile = Tile((x,y),TILESIZE,GAMETILES["BreakableBlock"])
                # self.tiles.add(tile)
            case'1':
                print("GrassBlock")
                # tile = Tile((x,y),TILESIZE,GAMETILES["GrassBlock"])
                # self.tiles.add(tile)
            case'2':
                print("CastleHallBrickFloor")
                # tile = Tile((x,y),TILESIZE,GAMETILES["CastleHallBrickFloor"])
                # self.tiles.add(tile)
            case'3':
                print("CastleHallFloorPillar")
                # tile = Tile((x,y),TILESIZE,GAMETILES["CastleHallFloorPillar"])
                # self.tiles.add(tile)
            case'4':
                print("BrickBlock")
                # tile = Tile((x,y),TILESIZE,GAMETILES["BrickBlock"])
                # self.tiles.add(tile)
            case'5':
                print("CastleHallFloorSupport")
                # tile = Tile((x,y),TILESIZE,GAMETILES["CastleHallFloorSupport"])
                # self.tiles.add(tile)
            case'6':
                print("ChapelFloor")
                # tile = Tile((x,y),TILESIZE,GAMETILES["ChapelFloor"])
                # self.tiles.add(tile)
            case'7':
                print("ChapelSupport")
                # tile = Tile((x,y),TILESIZE,GAMETILES["ChapelSupport"])
                # self.tiles.add(tile)
            case'8':
                print("IceFloor")
                # tile = Tile((x,y),TILESIZE,GAMETILES["IceFloor"])
                # self.tiles.add(tile)
            case'9':
                print("IceyBlock")
                # tile = Tile((x,y),TILESIZE,GAMETILES["IceyBlock"])
                # self.tiles.add(tile)
            case'10':
                print("DrakeGround")
                # tile = Tile((x,y),TILESIZE,GAMETILES["DrakeGround"])
                # self.tiles.add(tile)
            case'11':
                print("MagmaPoolBlock")
                # tile = Tile((x,y),TILESIZE,GAMETILES["MagmaPoolBlock"])
                # self.tiles.add(tile)
            case'12':
                print("WonderBlockFloor")
                # tile = Tile((x,y),TILESIZE,GAMETILES["WonderBlockFloor"])
                # self.tiles.add(tile)
            case'13':
                print("WonderBlockSupport")
                # tile = Tile((x,y),TILESIZE,GAMETILES["WonderBlockSupport"])
                # self.tiles.add(tile)
            case'14':
                print("PillarBlock")
                # tile = Tile((x,y),TILESIZE,GAMETILES["PillarBlock"])
                # self.tiles.add(tile)
            case'15':
                print("PillarSupport")
                # tile = Tile((x,y),TILESIZE,GAMETILES["PillarSupport"])
                # self.tiles.add(tile)
            case'16':
                print("GhostTrainFloor")
                # tile = Tile((x,y),TILESIZE,GAMETILES["GhostTrainFloor"])
                # self.tiles.add(tile)
            case'17':
                print("HauntedPrisonFloor")
                # tile = Tile((x,y),TILESIZE,GAMETILES["HauntedPrisonFloor"])
                # self.tiles.add(tile)
            case'18':
                print("HauntedPrisonSupport")
                # tile = Tile((x,y),TILESIZE,GAMETILES["HauntedPrisonSupport"])
                # self.tiles.add(tile)
            case'19':
                print("MasterChamberFloor")
                # tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberFloor"])
                # self.tiles.add(tile)
            case'20':
                print("MasterChamberSigil")
                # tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberSigil"])
                # self.tiles.add(tile)
            case'21':
                print("MasterChamberPillarTop")
                # tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberPillarTop"])
                # self.tiles.add(tile)
            case'22':
                print("MasterChamberPillar")
                # tile = Tile((x,y),TILESIZE,GAMETILES["MasterChamberPillar"])
                # self.tiles.add(tile)
            case'23':
                print("ClassicBlock")
                # tile = Tile((x,y),TILESIZE,GAMETILES["ClassicBlock"])
                # self.tiles.add(tile)
            case'24':
                print("player")
            case'25':
                print("LevelEnd")
                # tile = Tile((x,y),TILESIZE,GAMETILES["LevelEnd"])
                # self.tiles.add(tile)
                pass