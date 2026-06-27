import heapq

def min_cost_to_connect_cables(cables):
    # Перетворюємо список у мінімальну купу
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Беремо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Вартість поточного з'єднання
        cost = first + second
        total_cost += cost

        # Новий кабель повертаємо в купу
        heapq.heappush(cables, cost)

    return total_cost


# Приклад
cables = [4, 3, 2, 6]

print("Мінімальні витрати:", min_cost_to_connect_cables(cables))
