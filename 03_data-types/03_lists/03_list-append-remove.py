
# A list acts like a container where we can store all kinds of information.
# We can access a list using indexes and slices.

#start with an empty list
good_reads = []
print(good_reads)

good_reads.append("The Hunger games")
good_reads.append("Harry Potter")
print(good_reads)

# Now, if for some reason we don't like a particular book anymore, we can change it as follows:
# good_reads.remove("Harry Potter")
print(good_reads)

if "Harry Poter" not in good_reads:
    print("Harry Potter doesn't exist in the list")
#
# good_reads[0] = "Pride and Prejudice"
# print(good_reads)
#
#
#
# #TODO: Exercises
# #the title of the second book in our good reads collection
# # add aditional books
#
# good_reads = ["The Hunger games", "A Clockwork Orange",
#               "Pride and Prejudice", "Water for Elephants",
#               "The Shadow of the Wind", "Bel Canto"]
#
# good_reads.remove("Water for Elephants")
#
# print(good_reads)
#
# ### If we try to remove a book that is not in our collection, Python raises an error
#
# # good_reads.remove("White Oleander")
#
#
# ##### append two list with each other
# good_reads = ["The Hunger games", "A Clockwork Orange",
#               "Pride and Prejudice", "Water for Elephants",
#               "The Shadow of the Wind", "Bel Canto"]
#
# bad_reads = ["Fifty Shades of Grey", "Twilight"]
#
# all_reads = good_reads + bad_reads
# print(all_reads)