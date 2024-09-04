from collections import deque

class WarehouseState:
    def __init__(self, boxes, empty_spot):
        self.boxes = boxes
        self.empty_spot = empty_spot

    def is_goal(self, goal_state):
        return self.boxes == goal_state

    def get_possible_moves(self):
        moves = []
        for i in range(len(self.boxes)):
            if i != self.empty_spot:
                new_boxes = self.boxes[:]
                new_boxes[self.empty_spot], new_boxes[i] = new_boxes[i], new_boxes[self.empty_spot]
                moves.append(WarehouseState(new_boxes, i))
        return moves

    def __eq__(self, other):
        return self.boxes == other.boxes

    def __hash__(self):
        return hash(tuple(self.boxes))


def bfs_solve(start_state, goal_state):
    queue = deque([start_state])
    visited = set()
    parent_map = {start_state: None}

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal(goal_state):
            path = []
            while current_state:
                path.append(current_state.boxes)
                current_state = parent_map[current_state]
            return path[::-1]  # Повертаємо шлях від початкового до кінцевого стану

        visited.add(current_state)

        for next_state in current_state.get_possible_moves():
            if next_state not in visited and next_state not in queue:
                parent_map[next_state] = current_state
                queue.append(next_state)

    return None

    

start = WarehouseState([2, 3, 1, None], 3)
goal = [None, 1, 2, 3]

solution = bfs_solve(start, goal)

if solution:
    print("Рішення знайдено:")
    for step in solution:
        print(step)
else:
    print("Рішення не знайдено")
