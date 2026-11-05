# python3 main.py < input.txt
import sys
# 18893502033

invalid_ids = []

def main() -> None:
	print("Day 2")
	inputs = GetInput()
	invalid_sum = 0

	for input_pair in inputs:
		start = int(input_pair[0])
		end = int(input_pair[1])
		invalid_sum += ProcessRange(start, end)
	print(f"Invalid Ids: {invalid_ids}")
	print(f"Invalid sum: {invalid_sum}")

def ProcessRange(start: int, end: int) -> int:
	invalid_sum = 0
	for num in range(start, end + 1):
		if IsInvalid(num):
			invalid_ids.append(num)
			invalid_sum += num
	return invalid_sum

def IsInvalid(num: int) -> bool:
	item = str(num)
	for size in range(1, len(item)):
		compare = item[0:size]

		equals = True
		for i in range(len(item)):
			buffer = item[i * size:(i + 1) * size]
			if buffer == "":
				break
			if buffer != compare:
				equals =  False
		if equals:
			return True
	return False

def GetInput():
	line = ""
	for line in sys.stdin:
		line = line.strip().split(",")
	return [item.split("-") for item in line]

if __name__ == "__main__":
	main()