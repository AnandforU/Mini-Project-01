def flames_game(name1, name2):
    # Step 1: Normalize the names by removing spaces and converting to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    # Step 2: Remove common characters from both names
    list1 = list(name1)
    list2 = list(name2)

    for char in name1:
        if char in list2:
            list2.remove(char)
            list1.remove(char)

    # Remaining characters count
    remaining_count = len(list1) + len(list2)

    # FLAMES list
    flames = ['F', 'L', 'A', 'M', 'E', 'S']

    # Determine the result based on remaining_count
    index = 0
    while len(flames) > 1:
        index = (index + remaining_count - 1) % len(flames)
        flames.pop(index)

    # Final result
    result = flames[0]

    # Mapping result to status
    status_mapping = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    
    # Output format
    status = status_mapping[result]
    return f"status = {status}"

# Example usage:
player1 = input("Enter the first name: ")
player2 = input("Enter the second name: ")
print(flames_game(player1, player2))
