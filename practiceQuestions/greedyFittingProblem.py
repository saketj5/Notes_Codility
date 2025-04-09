### 5. Fill a Container (Greedy Fitting Problem)
# Task: Fit boxes into minimum number of containers of size W.
def min_containers(boxes, W):
    boxes.sort(reverse=True)
    containers = []
    for box in boxes:
        placed = False
        for i in range(len(containers)):
            if containers[i] + box <= W:
                containers[i] += box
                placed = True
                break
        if not placed:
            containers.append(box)
    return len(containers)

