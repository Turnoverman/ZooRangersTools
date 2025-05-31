#!/usr/bin/python3

import essence20

def roll_3d2():
    """
    Simulates rolling 3d2 by calling essence20.skilldieportion three times and summing the results.
    Each call represents rolling a single d2 die.
    
    Returns:
        int: The sum of three 1d2 rolls. Possible results are 3, 4, 5, or 6.
    """
    roll1 = essence20.skilldieportion(essence20.DiceLadder.d2, False, None)
    roll2 = essence20.skilldieportion(essence20.DiceLadder.d2, False, None)
    roll3 = essence20.skilldieportion(essence20.DiceLadder.d2, False, None)
    return roll1 + roll2 + roll3

def analyze_outliers(num_players, num_rolls):
    """
    Rolls 3d2 for multiple players a specified number of times and
    analyzes the frequency of "awkward" outlier scenarios.
    
    Args:
        num_players (int): The number of players participating in the simulation.
        num_rolls (int): The total number of times each player rolls 3d2.
    """
    # Initialize a dictionary to store results for each player
    player_results = {f'player_{i+1}': [] for i in range(num_players)}

    # Counters for different types of "awkward" scenarios
    range_3_count = 0  # e.g., one player gets 3, others get 6, or vice-versa
    range_2_count = 0  # e.g., one player gets 3, others get 5, or 4 vs 6

    print(f"Simulating {num_rolls} rolls for {num_players} players...")
    
    # Perform the dice rolls for all players for the specified number of times
    for _ in range(num_rolls):
        current_roll_set = []
        for player in player_results:
            roll_result = roll_3d2()
            player_results[player].append(roll_result)
            current_roll_set.append(roll_result)

        # Analyze the current set of rolls for outliers
        min_score = min(current_roll_set)
        max_score = max(current_roll_set)
        current_range = max_score - min_score

        if current_range == 3:
            range_3_count += 1
        elif current_range == 2:
            range_2_count += 1

    print("\n--- Outlier Analysis Results ---")
    print(f"Total simulations: {num_rolls}")

    # Calculate percentages
    percent_range_3 = (range_3_count / num_rolls) * 100
    percent_range_2 = (range_2_count / num_rolls) * 100
    
    print(f"Occurrences where range of scores was 3 (e.g., 3 vs 6): {range_3_count} ({percent_range_3:.4f}%)")
    print(f"Occurrences where range of scores was 2 (e.g., 3 vs 5, or 4 vs 6): {range_2_count} ({percent_range_2:.4f}%)")
    print(f"Total 'awkward' scenarios (range >= 2): {range_3_count + range_2_count} ({(percent_range_3 + percent_range_2):.4f}%)")

if __name__ == "__main__":
    # Define the number of players and the total number of rolls
    num_players = 5
    num_rolls = 1_000_000
    
    # Run the outlier analysis
    analyze_outliers(num_players, num_rolls)
