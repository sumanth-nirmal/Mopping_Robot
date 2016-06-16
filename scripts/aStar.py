class AStar:
    def __init__(self, _neighbor_test, minimums, maximums, steps, axis_connected=1, euclidian=True):
        self.neighbor_test = _neighbor_test
        self.minimums = minimums
        self.maximums = maximums
        self.steps = steps
        self.grid_size = [(_max - _min) / float(_step)
                          for _min, _max, _step
                          in zip(self.minimums, self.maximums, self.steps)]

        if euclidian:
            self._metric = self._euclidian
        else:
            self._metric = self._manhattan

        self.rpoints = zeros([product(self.steps)*1.2, 3])
        self.bpoints = zeros([product(self.steps)*1.22, 3])
        self.rhandle = None
        self.rid = 0
        self.ghandle = None
        self.gid = 0

        if axis_connected is 1:
            self.neighbor_offsets = list(OrderedDict.fromkeys([x for x in itertools.permutations([0, 0, 1])]))
            self.neighbor_offsets.extend(list(OrderedDict.fromkeys([x for x in itertools.permutations([0, 0, -1])])))
            self.neighbor_offsets.sort()
            self.neighbor_offsets = list(OrderedDict.fromkeys(self.neighbor_offsets))
        else:
            _tmp_offsets = list()
            for i in range(axis_connected):
                _tmp_offsets.extend([-1, 1, 0])
            self.neighbor_offsets = [x for x in itertools.permutations(_tmp_offsets, 3)]
            self.neighbor_offsets.sort(cmp=lambda a, b: sum([abs(i) for i in a]) - sum([abs(i) for i in b]))
            self.neighbor_offsets = list(OrderedDict.fromkeys(self.neighbor_offsets))
            if tuple([0 for x in range(axis_connected)]) in self.neighbor_offsets:
                self.neighbor_offsets.remove(tuple([0 for x in range(axis_connected)]))

    def grid_to_pos(self, cell):
        return tuple([_val * _size + _min
                      for _val, _size, _min
                      in zip(cell, self.grid_size, self.minimums)])

    def pos2Grid(self, pos):
        return tuple([round((_val - _min) * _steps / (_max - _min - .0))
                     for _val, _steps, _max, _min
                     in zip(pos, self.steps, self.maximums, self.minimums)])

    def limit_check(self, n):
        _pos = self.grid_to_pos(n)
        for _max, _min, _val in zip(self.maximums, self.minimums, _pos):
            if _min > _val or _max < _val:
                return False
        return True

    @staticmethod
    def _vec_sum(a, b):
        return tuple(map(operator.add, a, b))

    def fetchNeighbours(self, current_cell):
        neighbours = [self._vec_sum(current_cell, off) for off in self.neighbor_offsets]
        if False:
            return [n for n in neighbours if self.limit_check(n) and self.neighbor_test(self.grid_to_pos(n))]
        else:
            filt_neighbours = list()
            for n in neighbours:
                if self.limit_check(n) and self.neighbor_test(self.grid_to_pos(n)):
                    filt_neighbours.append(n)
                else:
                    rad = 0.4 * min(self.grid_size[:-1])
                    _pos = self.grid_to_pos(n)
                    self.rpoints[self.rid] = [_pos[0] + cos(_pos[2]) * rad,
                                                     _pos[1] + sin(_pos[2]) * rad,
                                                     0.028]
                    self.rid += 1
                    if self.rid % 100 is 0:
                        self.rhandle = env.plot3(points=self.rpoints, pointsize=2.0, colors=RED)
            return filt_neighbours

    def cost(self, a, b):
        return self._metric(self.grid_to_pos(a), self.grid_to_pos(b))

    def heuristic(self, a, b):
        return self._metric(self.grid_to_pos(a), self.grid_to_pos(b))

    @staticmethod
    def _manhattan(a, b):
        return linalg.norm([abs(b - a) for a, b in zip(a, b)], ord=1)

    @staticmethod
    def _euclidian(a, b):
        return linalg.norm([abs(b - a) for a, b in zip(a, b)], ord=2)

    def AStarSearch(self, start_pos, goal_pos):

        start = self.pos2Grid(start_pos)
        goal = self.pos2Grid(goal_pos)

        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = dict()
        cost_so_far = dict()
        came_from[start] = None
        cost_so_far[start] = 0

        ctr = 0
        while not frontier.empty():
            pri, current = frontier.get()

            ctr += 1
            rad = 0.4 * min(self.grid_size[:-1])
            _pos = self.grid_to_pos(current)

            self.bpoints[self.gid] = [_pos[0] + cos(_pos[2]) * rad,
                                                 _pos[1] + sin(_pos[2]) * rad,
                                                 0.025]
            self.gid += 1
            if self.gid % 100 is 0:
                self.ghandle = env.plot3(points=self.bpoints, pointsize=2.0, colors=BLUE)

            if current == goal:
                print "Path found!"
                path = [goal]
                cell = goal
                while cell in came_from.keys():
                    cell = came_from[cell]
                    path.append(cell)
                path.reverse()
                return map(self.grid_to_pos, path[1:])

            for next in self.fetchNeighbours(current):
                new_cost = cost_so_far[current] + self.cost(self.grid_to_pos(current), self.grid_to_pos(next))
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + self.heuristic(self.grid_to_pos(next), self.grid_to_pos(goal))
                    frontier.put((priority, next))
                    came_from[next] = current

        print "No path found!"
        return []
