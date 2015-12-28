from nose.tools import *
from exercise47.game import Room


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equals(gold.name, "GoldRoom")
    assert_equals(gold.paths, {})


def test_room_paths():
    center = Room("Center", "The room in the center.")
    north = Room("North", "The room in the north.")
    south = Room("South", "The room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equals(center.go('north'), north)
    assert_equals(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)