import sys

def main():
	batteries = get_input()
	total_joltage = 0
	for i, battery in enumerate(batteries):
		total_joltage += max_joltage(battery)

	print(f"Total max joltage: {total_joltage}")

def max_joltage(battery: str) -> int:
	pointers = []
	remaining = 12
	start = 0

	for position in range(12):
		remaining = 12 - position
		search_end = len(battery) - remaining + 1
		max_digit = '0'
		start_search = start

		for i in range(start_search, search_end):
			# print(i, battery[i])
			if battery[i] > max_digit:
				max_digit = battery[i]
				start_search = i
			
		pointers.append(start_search)
		start = start_search + 1
		# print(f"Pointers: {pointers}")
	return joltage(battery, pointers)
		

def joltage(battery: str, pointers: list[int]) -> int:
	# print(f"Pointers: {pointers}")
	# for p in pointers:
	# 	print(f"{battery[p]}", end="")
	# print()

	jolt = 0
	size = len(pointers)
	for i in range(len(pointers)):
		n = int(battery[pointers[i]])
		power = pow(10, size - i - 1)
		jolt += n * power
		# print(f"n: {n} | power: {power}")
	return jolt

def update_pointers(battery: str, pointers: list[int]) -> list[int]:
	size = len(pointers)
	for i in range(size-1, 0, -1):
		r = pointers[i]
		l = pointers[i-1]

		if battery[l] < battery[r]:
			pointers[i-1] = pointers[i]
		else:
			break
	
	pointers[11] += 1
	return pointers

def get_input() -> list[str]:
	batteries = []
	for line in sys.stdin:
		batteries.append(line.strip())
	return batteries

if __name__ == "__main__":
	main()