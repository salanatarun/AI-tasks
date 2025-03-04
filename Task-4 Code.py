print("Monkey banana -1")
class MonkeyBananaProblem:
    def __init__(self):
        self.initial_state = ('A', 'C', 'on_floor', 'empty_hands')  # Monkey at A, Box at C
        self.goal_state = ('B', 'B', 'on_box', 'has_banana')

    def is_goal(self, state):
        return state == self.goal_state

    def successors(self, state):
        monkey, box, monkey_state, hands = state
        actions = []

        if monkey_state == 'on_floor':
            if monkey != box:
                actions.append(('walk', box, (box, box, 'on_floor', hands)))
            if monkey == box:
                actions.append(('climb', monkey, (monkey, box, 'on_box', hands)))
        if monkey_state == 'on_box' and monkey == box == 'B':
            actions.append(('grab', 'banana', (monkey, box, 'on_box', 'has_banana')))
        return actions

    def solve(self):
        from collections import deque
        visited = set()
        queue = deque([(self.initial_state, [])])

        while queue:
            current_state, path = queue.popleft()
            if self.is_goal(current_state):
                return path + [current_state]
            if current_state in visited:
                continue
            visited.add(current_state)
            for action, _, next_state in self.successors(current_state):
                queue.append((next_state, path + [current_state]))
        return None


# Solve the problem
problem = MonkeyBananaProblem()
solution = problem.solve()
if solution:
    print("Solution Found:")
    for step in solution:
        print(step)
else:
    print("No Solution Found.")

print("Monkey banana-2")
class MonkeyBananaCompetition:
    def __init__(self):
        self.initial_state = (('A', 'C', 'on_floor', 'empty_hands'),
                              ('C', 'C', 'on_floor', 'empty_hands'))
        self.goal_state = ('has_banana')

    def is_goal(self, state):
        return state[0][3] == self.goal_state or state[1][3] == self.goal_state

    def successors(self, monkey_state):
        monkey, box, m_state, hands = monkey_state
        actions = []
        if m_state == 'on_floor':
            if monkey != box:
                actions.append(('walk', box, (box, box, 'on_floor', hands)))
            if monkey == box:
                actions.append(('climb', monkey, (monkey, box, 'on_box', hands)))
        if m_state == 'on_box' and monkey == box == 'B':
            actions.append(('grab', 'banana', (monkey, box, 'on_box', 'has_banana')))
        return actions

    def solve(self):
        from collections import deque
        visited = set()
        queue = deque([(self.initial_state, [])])

        while queue:
            (m1, m2), path = queue.popleft()
            if self.is_goal((m1, m2)):
                return path + [(m1, m2)]
            if (m1, m2) in visited:
                continue
            visited.add((m1, m2))

            for action1, _, next_m1 in self.successors(m1):
                for action2, _, next_m2 in self.successors(m2):
                    queue.append(((next_m1, next_m2), path + [(m1, m2)]))
        return None


# Solve the problem
competition = MonkeyBananaCompetition()
solution = competition.solve()
if solution:
    print("Solution Found in Competitive Environment:")
    for step in solution:
        print(step)
else:
    print("No Solution Found.")
