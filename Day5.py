def calculate_sum_and_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers) if numbers else 0
    return total_sum, average

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]  # Example list of numbers
    total_sum, average = calculate_sum_and_average(numbers)
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")