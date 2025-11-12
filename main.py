import sys

from stats import get_num_words

from stats import get_report

## printing explanation if more than 1 path entered
if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

print ("============ BOOKBOT ============")
print (f"Analyzing book found at {path}...")
print ("----------- Word Count ----------")
get_num_words(path)
print ("--------- Character Count -------")
get_report(path)
print ("============= END ===============")
