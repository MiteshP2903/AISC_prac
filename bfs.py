from collections import deque

def water_jug(cap1, cap2, target):
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        jug1, jug2, path = queue.popleft()

        if jug1 == target or jug2 == target:
            return path + [((jug1, jug2), "Target Reached")]

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        transitions = [
            (cap1, jug2, "Jug1 is full"),
            (jug1, cap2, "Jug2 is full"),
            (0, jug2, "Jug1 is empty"),
            (jug1, 0, "Jug2 is empty"),  # Fixed the '1' to '0' here
            (jug1 - min(jug1, cap2 - jug2), jug2 + min(jug1, cap2 - jug2), "Pour 1->2"),
            (jug1 + min(jug2, cap1 - jug1), jug2 - min(jug2, cap1 - jug1), "Pour 2->1")
        ]

        for next_jug1, next_jug2, actions in transitions:
            if (next_jug1, next_jug2) not in visited:
                next_path = path + [((jug1, jug2), actions)]
                # FIXED: Added extra parentheses so it's only ONE argument
                queue.append((next_jug1, next_jug2, next_path))

    # FIXED: Unindented so it only triggers if the whole loop finishes with no winner
    return "No solution found"


steps = water_jug(4, 3, 2)
print("Water jug steps:")
if isinstance(steps, list):
    for state, actions in steps:
        print(f"State: {state} -> Action: {actions}")
else:
    print(steps)