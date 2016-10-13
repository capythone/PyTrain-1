smplextext = '''According to Land Rover’s design boss, Gerry McGovern,
“Design creates an emotional connection between our customers and our vehicles.
 Our clear design strategy means our vehicles are instantly recognisable and communicate
 the values of Land Rover that our customers love. New Discovery’s flawless volume and proportions,
 sophisticated surfaces and precise detailing beautifully combine with engineering integrity to create
 a premium SUV that will resonate with today’s customers.”
'''
words = smplextext.split(' ')
print(words)
freq_distribution = {}

for each in words:
    if each in freq_distribution :
        freq_distribution[each] += 1
    elif 'a' or 'b' in each:
        freq_distribution[each] = 1

print(freq_distribution)
number_of_words_with_a = 0
for k in freq_distribution:
    number_of_words_with_a += freq_distribution[k]

print("Number of words that contain letter 'a' ", number_of_words_with_a)

if 'a' in 'bbbbb' and 'b' in 'bbbbb':
    print("both a and b exits")
