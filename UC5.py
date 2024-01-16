import random

def simulate_coin_flips(num_flips):
    singlet_counts = {0: 0, 1: 0}
    doublet_counts = {'HH': 0, 'HT': 0, 'TH': 0, 'TT': 0}
    triplet_counts = {'HHH': 0, 'HHT': 0, 'HTH': 0, 'THH': 0, 'HTT': 0, 'THT': 0, 'TTH': 0, 'TTT': 0}

    for _ in range(num_flips - 2):
        result1 = random.choice([0, 1])
        result2 = random.choice([0, 1])
        result3 = random.choice([0, 1])
        singlet_counts[result1] += 1
        singlet_counts[result2] += 1
        singlet_counts[result3] += 1
        outcome_doublet = 'H' if result2 == 1 else 'T'
        outcome_doublet += 'H' if result3 == 1 else 'T'
        doublet_counts[outcome_doublet] += 1
        outcome_triplet = 'H' if result1 == 1 else 'T'
        outcome_triplet += 'H' if result2 == 1 else 'T'
        outcome_triplet += 'H' if result3 == 1 else 'T'
        triplet_counts[outcome_triplet] += 1

    return singlet_counts, doublet_counts, triplet_counts

def calculate_percentage(counts, total_flips):
    percentage_dict = {}
    for key, value in counts.items():
        percentage_dict[key] = (value / total_flips) * 100
    return percentage_dict

def main():
    num_flips = int(input("Enter the number of coin flips: "))
    singlet_counts_result, doublet_counts_result, triplet_counts_result = simulate_coin_flips(num_flips)

    singlet_percentage = calculate_percentage(singlet_counts_result, num_flips * 3)
    doublet_percentage = calculate_percentage(doublet_counts_result, num_flips * 2)
    triplet_percentage = calculate_percentage(triplet_counts_result, num_flips)

    print("Singlet Counts:", singlet_counts_result)
    print("Doublet Counts:", doublet_counts_result)
    print("Triplet Counts:", triplet_counts_result)

    print("\nSinglet Percentages:", singlet_percentage)
    print("Doublet Percentages:", doublet_percentage)
    print("Triplet Percentages:", triplet_percentage)

    winning_combination = max(singlet_percentage, doublet_percentage, triplet_percentage, key=singlet_percentage.get)
    print("\nWinning Combination:", winning_combination)

if __name__ == "__main__":
    main()
