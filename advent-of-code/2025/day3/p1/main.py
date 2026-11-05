import sys

def main():
	print("Day 3")
	batteries = get_input()
	total_joltage = 0
	for i, battery in enumerate(batteries):
		total_joltage += max_joltage(battery)

	print(f"Total max joltage: {total_joltage}")

def max_joltage(battery: str) -> int:
	max_jolt = 0
	l, r = 0, 1

	while(r < len(battery)):
		jolt = joltage(battery[l], battery[r])
		if jolt > max_jolt:
			max_jolt = jolt

		if battery[l] < battery[r]:
			l = r
		
		r += 1

	return max_jolt
		

def joltage(a: str, b: str) -> int:
	return int(a)*10 + int(b)


def get_input() -> list[str]:
	batteries = []
	for line in sys.stdin:
		batteries.append(line.strip())
	return batteries

if __name__ == "__main__":
	main()