import random


class Rect:
    ''' 
    Rects will exist on the map in order to manage regions that
    represent rooms. They are also for checking to see if rooms
    intersect when being generated and placed on the map
    '''

    def __init__(self, coords, size):
        '''
        coords is a tuple containing the top left x, y coordinates
        of the rect. size is a tuple containing the height and width
        of the rect.
        '''
        self.x1, self.y1 = coords
        self.w, self.h = size
        self.x2 = self.x1 + self.w
        self.y2 = self.y1 + self.h

    @property
    def center(self):
        ''' 
        The coordinates of the center of the rectangle in order
        to create tunneling targets for connecting rects together.
        '''
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return (center_x, center_y)

    def intersects(self, target):
        '''
        Returns true if the rects intersect on both the x and y plane.
        '''
        intersect = self.x1 <= target.x2 and self.x2 >= target.x1 and self.y1 <= target.y2 and self.y2 <= target.y1

        return intersect


class Room:
    def __init__(self, sector_type, x, y):
        self.sector_type = sector_type
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"

    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)

    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")


class Map:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
        self.max_regions = 30
        self.max_region_size = 7
        self.min_region_size = 3

    def draw_region(self, region):
        for x in range(region.x1, region.x2):
            for y in range(region.y1, region.y2):
                self.grid[x][y] = Room('0', x, y)

    def draw_tunnel(self, a, b):
        x1, y1 = a
        x2, y2 = b

        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.grid[x][y1] = Room('0', x, y1)

        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.grid[x2][y] = Room('0', x1, y)

    def generate_rooms(self, size_x, size_y):

        self.grid = []
        self.width = size_x
        self.height = size_y
        for x in range(0, self.width):
            self.grid.append([])
            for y in range(0, self.height):
                self.grid[x].append(Room('1', x, y))

        region_list = []
        center_of_last_region = None

        for i in range(self.max_regions):

            w = random.randint(self.min_region_size, self.max_region_size)
            h = random.randint(self.min_region_size, self.max_region_size)
            x = random.randint(2, self.width-(w+2))
            y = random.randint(2, self.height-(h+2))

            region = Rect((x, y), (w, h))

            placement_failed = False

            for placed_region in region_list:
                if region.intersects(placed_region):
                    placement_failed = True
                    break

            if not placement_failed:
                region_list.append(region)
                self.draw_region(region)
                if center_of_last_region is not None:
                    self.draw_tunnel(region.center, center_of_last_region)

                center_of_last_region = region.center

    def print_rooms(self):
        '''
        Print out rooms in a series of 1, 0 based on sector.
        '''
        string = ""
        for i in range(0, self.width):
            string += "\n"
            for j in range(0, self.height):
                string += f"{self.grid[i][j].sector_type}"
        print(string)


m = Map()
width = 50
height = 50
m.generate_rooms(width, height)
m.print_rooms()
