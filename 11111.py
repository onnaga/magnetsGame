import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue, storing (cost, node, path)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))  # (التكلفة، العقدة، المسار)

    visited = set()  # لتجنب إعادة زيارة العقد

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        # إذا وصلنا إلى الهدف
        if current_node == goal:
            return cost, path

        # تخطي العقدة إذا كانت قد زارت سابقًا
        if current_node in visited:
            continue

        visited.add(current_node)

        # استكشاف الجيران
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                new_cost = cost + weight
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (new_cost, neighbor, new_path))

    return float('inf'), []  # إذا لم يتم العثور على المسار

# تمثيل الرسم البياني كقاموس
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start = 'A'
goal = 'D'
cost, path = uniform_cost_search(graph, start, goal)
print(f"Cost: {cost}, Path: {path}")