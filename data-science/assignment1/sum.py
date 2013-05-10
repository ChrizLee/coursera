import sys


def main():
    count, total = 0.0, 0.0
    term_file = open(sys.argv[1], "r")
    for line in term_file:
        count += 1
        total += float(line.split("\t")[1])

    print total, count, total/count

if __name__ == '__main__':
    main()