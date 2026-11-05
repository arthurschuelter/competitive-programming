# python3 main.py < input.txt
# source ./.env/bin/activate
# pytest test_main.py -v
import sys

def main():
    lines = GetInput()
    count_p1 = CountStepsP1(lines)
    count_p2 = CountStepsP2(lines)
        
    print(f"Password 1 is {red(str(count_p1))}")
    print(f"Password 2 is {green(str(count_p2))}")

def GetInput():
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())
    return lines

def CountStepsP1(lines: list):
    start, count = 50, 0
    for line in lines:
        direction, steps = line[:1], line[1:]
        # R++, L--
        steps = int(steps) if direction == "R" else (int(steps) * -1)

        start = (start + steps) % 100
        
        if start == 0:
            count += 1
    
    return count

def CountStepsP2(lines: list):
    start, count = 50, 0
    for line in lines:
        direction, steps = line[:1], line[1:]
        # R++, L--
        steps = int(steps) if direction == "R" else (int(steps) * -1)
        laps = abs(steps) // 100
        remaining_steps = (abs(steps)  - (laps*100))  * (-1 if direction == "L" else 1)

        for _ in range(laps):
            count += 1
        
        if remaining_steps == 0:
            continue
        
        if (start > 0 and start + remaining_steps < 0):
            count += 1
        
        if (start > 0 and start + remaining_steps > 100):
            count += 1 

        if (start + remaining_steps) % 100 == 0:
            count += 1
        start = (start + remaining_steps) % 100
    return count

def red(s: str) -> str:
    return f"\033[91m{s}\033[0m"

def green(s: str) -> str:
    return f"\033[92m{s}\033[0m"
    

if __name__ == "__main__":
    main()