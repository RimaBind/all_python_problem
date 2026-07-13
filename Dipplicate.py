
nums = [1, 2, 3, 2, 4, 1]  # Input list
counts = {}  # Dictionary to count how many times each number appears
output = []  # List to store duplicate numbers

for n in nums:  # Visit each number in the list
    counts[n] = counts.get(n, 0) + 1  # Build frequency map using same logic as character count
   #print("counts :",counts)
    print("count  elements",counts)
for key, value in counts.items():  # Loop through dictionary key-value pairs
    if value > 1:  # If a number appears more than once, it is duplicated
        output.append(key)  
print("more than one time items appear in list :",output)  # Display [1, 2]