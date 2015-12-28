class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        """
            Get the correct path from the path dictionary based on direction
        :param direction:
        :return:
        """
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        """
            Add paths to the class variable path
        :param paths:
        :return:
        """
        self.paths.update(paths)
