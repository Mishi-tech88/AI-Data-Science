# main.py
from config import initialize_gemini
from travel_planner import generate_itinerary


def get_int_input(prompt, min_value=1, max_value=None):
    """Prompt for an integer, re-asking until valid input is given."""
    while True:
        raw = input(prompt).strip()
        # Remove common currency formatting
        cleaned = raw.replace("$", "").replace(",", "").replace(" ", "")

        try:
            value = int(float(cleaned))  # float() first handles "44.00"
        except ValueError:
            print(f"  ⚠ Invalid input '{raw}'. Please enter a whole number (e.g., 200).")
            continue

        if value < min_value:
            print(f"  ⚠ Value must be at least {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"  ⚠ Value must be at most {max_value}.")
            continue

        return value


def get_user_input():
    print("\n===== AI TRAVEL PLANNER =====")
    name = input("Name: ").strip()

    while not name:
        print("  ⚠ Name cannot be empty.")
        name = input("Name: ").strip()

    destination = input("Destination: ").strip()
    while not destination:
        print("  ⚠ Destination cannot be empty.")
        destination = input("Destination: ").strip()

    days = get_int_input("Number of Days: ", min_value=1, max_value=365)
    budget = get_int_input("Budget (USD): ", min_value=1, max_value=1_000_000)

    interests_raw = input("Interests (comma-separated, e.g., Food, Beaches): ").strip()
    interests = [i.strip() for i in interests_raw.split(",") if i.strip()]
    if not interests:
        interests = ["General sightseeing"]

    travel_style = input("Travel Style (Solo/Family/Friends): ").strip().title()
    if travel_style not in ("Solo", "Family", "Friends"):
        print(f"  ⚠ Unrecognized style '{travel_style}'. Defaulting to 'Solo'.")
        travel_style = "Solo"

    return {
        "name": name,
        "destination": destination,
        "days": days,
        "budget": budget,
        "interests": interests,
        "travel_style": travel_style,
    }

# def get_user_input():
#     print("\n===== AI TRAVEL PLANNER =====")
#     name = input("Name: ").strip()
#     destination = input("Destination: ").strip()
#     days = int(input("Number of Days: ").strip())
#     budget = int(input("Budget (USD): ").strip())
#     interests = input("Interests (comma-separated, e.g., Food, Beaches): ").strip()
#     travel_style = input("Travel Style (Solo/Family/Friends): ").strip()

    # # return {
    # #     "name": name,
    # #     "destination": destination,
    # #     "days": days,
    # #     "budget": budget,
    # #     "interests": [i.strip() for i in interests.split(",") if i.strip()],
    # #     "travel_style": travel_style,
    # }


def choose_technique():
    print("\nChoose a prompting technique:")
    print("  1. Zero-Shot")
    print("  2. Few-Shot")
    print("  3. Structured Reasoning")
    
    choice = input("Enter 1, 2, or 3: ").strip()
    mapping = {"1": "zero-shot", "2": "few-shot", "3": "structured"}
    return mapping.get(choice, "zero-shot")

# In main.py
def main():
    client = initialize_gemini() # Changed variable name for clarity
    user_data = get_user_input()
    technique = choose_technique()

    print(f"\nGenerating itinerary using '{technique}' prompting...\n")
    print("=" * 60)

    # Pass the client to the generator function
    itinerary = generate_itinerary(client, user_data, technique)

    print(itinerary)
    print("=" * 60)
# def main():
#     model = initialize_gemini()
#     user_data = get_user_input()
#     technique = choose_technique()

#     print(f"\nGenerating itinerary using '{technique}' prompting...\n")
#     print("=" * 60)

#     itinerary = generate_itinerary(model, user_data, technique)

#     print(itinerary)
#     print("=" * 60)


if __name__ == "__main__":
    main()



