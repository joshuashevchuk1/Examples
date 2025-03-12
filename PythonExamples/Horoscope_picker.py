
def get_zodiac_sign(month, day):
    zodiac_signs = [
        ("Capricorn", (1, 1), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21)),
        ("Capricorn", (12, 22), (12, 31)),  # Capricorn appears twice since it spans two years
    ]

    for sign, start, end in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign

    return "Invalid date"  # Fallback in case something goes wrong

# Get user input
birthdate = input("Enter your birthdate (MM-DD or YYYY-MM-DD): ").strip()

# Extract month and day
try:
    parts = birthdate.split("-")
    month, day = int(parts[-2]), int(parts[-1])  # Takes last two parts to support both formats

    # Get zodiac sign
    sign = get_zodiac_sign(month, day)
    print(f"Your zodiac sign is: {sign} 🔮")

except ValueError:
    print("Invalid date format. Please enter in MM-DD or YYYY-MM-DD format.")
