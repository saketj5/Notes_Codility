### 9. Budget Allocation
# Task: Fund max number of projects within given budget.
def max_projects(costs, budget):
    costs.sort()
    count = 0
    for cost in costs:
        if budget >= cost:
            budget -= cost
            count += 1
        else:
            break
    return count
