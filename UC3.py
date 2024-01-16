import random

def simulate_coin_flips(num_flips):
    doublet_counts = {'HH': 0, 'HT': 0, 'TH': 0, 'TT': 0}

    for _ in range(num_flips - 1):
        result1 = random.choice([0, 1])
        result2 = random.choice([0, 1])
        outcome = 'H' if result1 == 1 else 'T'
        outcome += 'H' if result2 == 1 else 'T'
        doublet_counts[outcome] += 1

    return doublet_counts

def calculate_percentage(doublet_counts, total_flips):
    percentage_dict = {outcome: (count / (total_flips - 1)) * 100 for outcome, count in doublet_counts.items()}
    return percentage_dict

def main():
    num_flips = int(input("Enter the number of coin flips: "))
    doublet_counts_result = simulate_coin_flips(num_flips)
    percentage_result = calculate_percentage(doublet_counts_result, num_flips)
    print("Doublet Counts:", doublet_counts_result)
    print("Percentage of Doublet Combinations:", percentage_result)

if __name__ == "__main__":
    main()
