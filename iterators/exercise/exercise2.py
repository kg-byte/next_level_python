# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Generate permutations and filter based on conditions
# Use itertools to generate all permutations of the data list. Filter the permutations
# to keep only those where the first element is prime. Use itertools to chain together the
# filtered permutations. The expected output of this program is 1080.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import itertools

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculate_chained_permutations(data: list[int]) -> list[int]:
    ...
    permutations = itertools.permutations(data)
    filtered_permutations =filter(lambda x: is_prime(x[0]), permutations)
    chained_permutations = itertools.chain.from_iterable(filtered_permutations)
    return list(chained_permutations)

def main() -> None:
    data = [1, 2, 3, 4, 5]

    # TODO: Use itertools to generate all permutations of the data list
    # TODO: Filter the permutations to keep only those where the first element is prime
    # TODO: Use itertools to chain together the filtered permutations
    # Use the calculate_chained_permutations function to get the result
    chained_permutations: list[int] = calculate_chained_permutations(data)
    # Print the sum of the chained permutations
    print("Sum of chained permutations:", sum(chained_permutations))


if __name__ == "__main__":
    main()
