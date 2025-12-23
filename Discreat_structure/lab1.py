from typing import List, Set, Tuple


# --- Helper Functions ---

def print_crisp_set(name: str, crisp_set: Set) -> None:
    """Helper function to print a crisp set."""
    print(f"{name} = {{", end="")
    print(", ".join(map(str, crisp_set)), end="")
    print("}")


# --- CRISP SET OPERATIONS ---

def crisp_union(A: Set[int], B: Set[int]) -> Set[int]:
    """Calculates the Union of two crisp sets (A U B)."""
    return A | B  # Union using the | operator


def crisp_intersection(A: Set[int], B: Set[int]) -> Set[int]:
    """Calculates the Intersection of two crisp sets (A ∩ B)."""
    return A & B  # Intersection using the & operator


def crisp_difference(A: Set[int], B: Set[int]) -> Set[int]:
    """Calculates the Difference of two crisp sets (A - B)."""
    return A - B  # Difference using the - operator


def power_set(elements: List) -> List[List]:
    """Calculates the Power Set of a crisp set (all possible subsets)."""
    result = []
    num_subsets = 1 << len(elements)  # 2^n subsets

    for i in range(num_subsets):
        subset = [elements[j] for j in range(len(elements)) if (i & (1 << j)) > 0]
        result.append(subset)

    return result


def cartesian_product(setA: List[int], setB: List[int]) -> List[Tuple[int, int]]:
    """Calculates the Cartesian Product of two crisp sets (A x B)."""
    return [(a, b) for a in setA for b in setB]


# --- Main Demonstration ---

def main() -> None:
    print("=" * 54)
    print("           CRISP SET OPERATIONS DEMONSTRATION         ")
    print("=" * 54)

    # Define two crisp sets for basic operations
    setA: Set[int] = {10, 20, 30, 40, 50}
    setB: Set[int] = {30, 40, 60, 70}

    print_crisp_set("Set A", setA)
    print_crisp_set("Set B", setB)
    print()

    # 1. UNION (A U B)
    union_result = crisp_union(setA, setB)
    print_crisp_set("1. Union (A U B)", union_result)

    # 2. INTERSECTION (A ∩ B)
    intersection_result = crisp_intersection(setA, setB)
    print_crisp_set("2. Intersection (A ∩ B)", intersection_result)

    # 3. DIFFERENCE (A - B)
    difference_result = crisp_difference(setA, setB)
    print_crisp_set("3. Difference (A - B)", difference_result)

    print("\n" + "-" * 54)

    # 4. POWER SET P(X)
    setX_vec = ['a', 'b', 'c']
    print("4. Power Set P(X): Base Set X = {'a', 'b', 'c'}")
    p_set = power_set(setX_vec)
    print(f"   Total Subsets: {len(p_set)} (2^3)")

    for count, subset in enumerate(p_set, 1):
        print(f"     Subset {count}: {{", end="")
        print(", ".join(subset), end="")
        print("}")

    print("\n" + "-" * 54)

    # 5. CARTESIAN PRODUCT (Y x Z)
    setY_cart = ["Red", "Blue"]
    setZ_cart = [1, 2, 3]
    print("5. Cartesian Product (Y x Z):")
    print(f"   Set Y = {setY_cart}")
    print(f"   Set Z = {setZ_cart}")

    cart_prod = cartesian_product(setY_cart, setZ_cart)
    print(f"   Result (Total Pairs: {len(cart_prod)}):", end=" ")
    print("{", end="")
    print(", ".join(f"({x}, {y})" for x, y in cart_prod), end="")
    print("}")

    print("=" * 54)


if __name__ == "__main__":
    main()
