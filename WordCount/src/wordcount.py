import sys

def parse(fname):
    file = open(fname, 'r')
    wordcount = {}
    for word in file.read().replace(',', ' ').replace('.', ' ').replace('"', ' ').replace('?', ' ').replace('!', ' ').replace(':', ' ').replace(';', ' ').replace('--', ' ').split():
        word = word.lower()
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount

def print_count(fname):
    '''
    Prints one per line '<word> <count>' sorted by word for the given file
    '''
    wordcount = parse(fname)
    
    for key in sorted(wordcount):
        print key, wordcount[key]


def print_top(fname):
    '''
    Prints the top count listing for the given file
    '''
    wordcount = parse(fname)
    count = 0
    for key in sorted(wordcount, key=wordcount.get, reverse=True):
        print key, wordcount[key]
        count = count + 1
        if count == 20:
            break


def main():
    if len(sys.argv) != 3:
        print 'Usage: ./wordcount.py {--count | --top} <file name>'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_count(filename)
    elif option == '--top':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
