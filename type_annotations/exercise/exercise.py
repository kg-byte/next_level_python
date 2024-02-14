# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Exercise: Add type annotations
# Add appropriate type annotations to the functions to specify the types of the parameters
# and return values.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def calculate_average(numbers: list[int]) -> float:
    length_of_numbers = len(numbers)
    if length_of_numbers > 0:
        return sum(numbers) / length_of_numbers
    return 0.0


def calculate_total_sales(sales: dict[str, int]):
    return sum(sales.values())


def main():
    data = [1, 2, 3, 4, 5]
    average = calculate_average(data)
    print("The average is:", average)

    sales_data = {"product_a": 100, "product_b": 250, "product_c": 80, "product_d": 150}
    print("Sales data for product C:", sales_data["product_c"])
    total_sales = calculate_total_sales(sales_data)
    print("Total sales:", total_sales)


if __name__ == "__main__":
    main()
