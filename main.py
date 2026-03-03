numbers = input("Enter numbers separated by space: ").split()

numbers = [float(n) for n in numbers]

print("Count:", len(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
