import itertools

values = ['a', 'b', 'c', 'd', 'e', 'f']

# Generate combinations
all_filter_combinations = []

                                        # Iterate over all possible lengths of combinations
for i in range(1, 4):
    all_filter_combinations.extend(itertools.combinations(values, i))
print(all_filter_combinations)

