import subprocess
from math import floor

def main():
    subprocess_args = ["ssh", "alice@10.10.217.228", "-p", "9000"]
    ports = []

    for i in range(9000, 14000):
        if i < 9100 or i > 9107:
            ports.append(i)

    left_end = 0
    right_end = len(ports) - 1

    while left_end <= right_end:
        mid = floor((right_end - left_end) / 2) + left_end
        subprocess_args[3] = str(ports[mid])
        result = subprocess.run(subprocess_args, stdout=subprocess.PIPE)
        response = result.stdout.decode("utf-8").strip()
        print(f"Port {ports[mid]}: {response}")

        if response == "Lower":
            left_end = mid
        elif response == "Higher":
            right_end = mid
        else:
            print(f"Found at Port {ports[mid]}")
            break


    

if __name__ == "__main__":
    main()
