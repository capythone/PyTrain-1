#first we specify two lists of strings:
good_reads = ["The Hunger games", "A Clockwork Orange",
              "Pride and Prejudice", "Water for Elephants",
              "The Shadow of the Wind", "Bel Canto"]

bad_reads = ["Fifty Shades of Grey", "Twilight"]

all_reads = good_reads + bad_reads
print(all_reads)

good_reads.sort()
print(good_reads)
