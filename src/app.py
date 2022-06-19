import sys
import os



def prime(s):
    # your code goes here
    i = int(sys.argv[1])
    if i > 1:
        for n in range(2, int(i/2)+1):
            if (i % n) == 0:
                s = "%d is not a prime number" % (i)
            else:
                s = "%d is a prime number" % (i)
    return s
    
def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
