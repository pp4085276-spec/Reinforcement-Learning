class GridWorld:
    """A simple grid world for a robot to navigate."""

    MOVES = {0: (0, -1), 1: (0, 1), 2: (-1, 0), 3: (1, 0)}  # up, down, left, right

    def __init__(self, width=6, height=6, walls=None, start=(0, 0), goal=(5, 5)):
        self.width = width
        self.height = height
        self.walls = set(walls or [(2, 1), (2, 2), (3, 4)])
        self.start = start
        self.goal = goal
        self.robot = start

    def reset(self):
        self.robot = self.start
        return self.robot

    def step(self, action):
        dx, dy = self.MOVES[action]
        x, y = self.robot[0] + dx, self.robot[1] + dy
        reward = -1
        if 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.walls:
            self.robot = (x, y)
        else:
            reward = -5  # hit a wall or the edge
        done = self.robot == self.goal
        if done:
            reward = 10
        return self.robot, reward, done

    def render(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) == self.robot:
                    row += "R "
                elif (x, y) == self.goal:
                    row += "G "
                elif (x, y) in self.walls:
                    row += "# "
                else:
                    row += ". "
            print(row)


if __name__ == "__main__":
    env = GridWorld()
    env.reset()
    env.render()
    