"""
Created by: Alexander Haynes
Date: March 8, 2026
Package Sorting System for Smarter Technology's Robotic Automation Factory

This script dispatches packages to the correct stack based on their volume and mass.
"""

def sort(width, height, length, mass):
    REJECTED = "REJECTED"
    SPECIAL = "SPECIAL"
    STANDARD = "STANDARD"

    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        return REJECTED

    MAX_VOLUME = 1_000_000  # cubic centimeters
    MAX_DIMENSION = 150  # centimeters
    MAX_WEIGHT = 20  # kilograms

    volume = width * height * length
    is_bulky = volume >= MAX_VOLUME or width >= MAX_DIMENSION or height >= MAX_DIMENSION or length >= MAX_DIMENSION
    is_heavy = mass >= MAX_WEIGHT

    if is_bulky and is_heavy:
        return REJECTED
    elif is_bulky or is_heavy:
        return SPECIAL
    else:
        return STANDARD


def main():
    print("=" * 60)
    print("Package Sorting System - Test Cases")
    print("Created by: Alexander Haynes")
    print("Date: March 8, 2026")
    print("=" * 60)

    # Test case 1: STANDARD package (not bulky, not heavy)
    print("\nTest 1: STANDARD Package")
    print("Dimensions: 50cm x 50cm x 50cm, Mass: 10kg")
    result1 = sort(50, 50, 50, 10)
    print(f"Result: {result1}")
    print(f"Volume: {50*50*50:,} cm³, Mass: 10 kg")

    # Test case 2: SPECIAL package (bulky due to volume, not heavy)
    print("\nTest 2: SPECIAL Package (Bulky by volume)")
    print("Dimensions: 100cm x 100cm x 100cm, Mass: 15kg")
    result2 = sort(100, 100, 100, 15)
    print(f"Result: {result2}")
    print(f"Volume: {100*100*100:,} cm³, Mass: 15 kg")

    # Test case 3: SPECIAL package (bulky due to dimension, not heavy)
    print("\nTest 3: SPECIAL Package (Bulky by dimension)")
    print("Dimensions: 160cm x 50cm x 50cm, Mass: 10kg")
    result3 = sort(160, 50, 50, 10)
    print(f"Result: {result3}")
    print(f"Volume: {160*50*50:,} cm³, One dimension >= 150cm")

    # Test case 4: SPECIAL package (heavy but not bulky)
    print("\nTest 4: SPECIAL Package (Heavy)")
    print("Dimensions: 50cm x 50cm x 50cm, Mass: 25kg")
    result4 = sort(50, 50, 50, 25)
    print(f"Result: {result4}")
    print(f"Volume: {50*50*50:,} cm³, Mass: 25 kg")

    # Test case 5: REJECTED package (both bulky and heavy)
    print("\nTest 5: REJECTED Package (Bulky AND Heavy)")
    print("Dimensions: 150cm x 100cm x 100cm, Mass: 30kg")
    result5 = sort(150, 100, 100, 30)
    print(f"Result: {result5}")
    print(f"Volume: {150*100*100:,} cm³, Mass: 30 kg")

    # Test case 6: Another REJECTED package (bulky by volume and heavy)
    print("\nTest 6: REJECTED Package (Large volume AND Heavy)")
    print("Dimensions: 120cm x 120cm x 120cm, Mass: 40kg")
    result6 = sort(120, 120, 120, 40)
    print(f"Result: {result6}")
    print(f"Volume: {120*120*120:,} cm³, Mass: 40 kg")

    # Test case 7: Invalid input
    print("\nTest 7: REJECTED Package (Invalid input)")
    print("Dimensions: -10cm x 50cm x 50cm, Mass: 10kg")
    result7 = sort(-10, 50, 50, 10)
    print(f"Result: {result7}")
    print(f"Volume: {-10*50*50:,} cm³, Mass: 10 kg")


if __name__ == "__main__":
    main()
