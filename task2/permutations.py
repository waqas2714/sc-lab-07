from typing import List

def generate_permutations_recursive(s: str, current: str, used: List[bool], results: List[str], include_duplicates: bool):
    if len(current) == len(s):
        results.append(current)  # Append to the list for results
        return
    
    for i in range(len(s)):
        if used[i]:
            continue
        # Skip duplicates if not including them
        if not include_duplicates and i > 0 and s[i] == s[i - 1] and not used[i - 1]:
            continue
        used[i] = True
        generate_permutations_recursive(s, current + s[i], used, results, include_duplicates)
        used[i] = False

def generate_permutations(s: str, include_duplicates: bool) -> List[str]:
    if not s:
        raise ValueError("Input string cannot be empty")
    
    results: List[str] = []  # Always initialize as a list
    used = [False] * len(s)
    
    # Sort the string to handle duplicates
    generate_permutations_recursive(sorted(s), "", used, results, include_duplicates)
    
    return sorted(results)  # Always return sorted results

def generate_permutations_non_recursive(s: str) -> List[str]:
    from itertools import permutations
    return sorted(set([''.join(p) for p in permutations(s)]))

def main():
    input_str = input("Enter a string: ")
    include_duplicates = input("Include duplicate permutations? (yes/no): ").strip().lower() == 'yes'
    
    try:
        recursive_perms = generate_permutations(input_str, include_duplicates)
        print("Permutations (Recursive):", recursive_perms)

        non_recursive_perms = generate_permutations_non_recursive(input_str)
        print("Permutations (Non-Recursive):", non_recursive_perms)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
