import numpy as np

def main():
    N = int(input())
    l = list(map(int, input().split()))

    l = np.argsort(l)
    print(f"{l[0] + 1} {l[1] + 1} {l[2] + 1}")

if __name__ == "__main__":
    main()