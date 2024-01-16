import random

def simulate_coin_flips(num_flips):
    singlet_counts = {}

    for _ in range(num_flips):
        result = random.choice([0, 1])
        if result in singlet_counts:
            singlet_counts[result] += 1
        else:
            singlet_counts[result] = 1

    return singlet_counts

def calculate_percentage(singlet_counts, total_flips):
    percentage_dict = {}

    for outcome, count in singlet_counts.items():
        percentage = (count / total_flips) * 100
        percentage_dict[outcome] = percentage

    return percentage_dict
num_flips=int(input())
singlet_counts_result = simulate_coin_flips(num_flips)
percentage_result = calculate_percentage(singlet_counts_result, num_flips)
print("Singlet Counts:", singlet_counts_result)
print("Percentage of Singlet Combinations:", percentage_result)
