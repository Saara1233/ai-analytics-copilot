"""
Types
"""

def main():
    p_name = 'xyz'
    p_age = 20
    p_wage = 200000000.10
    p_employed = True

    passenger_profile = {
        "name" : p_name,
        "age" : p_age,
        "wage" : p_wage,
        "employed" : p_employed   
    }

    print("=== PASSENGER DATA RECORD ===")
    print(f"passenger name {passenger_profile['name']}")
    print(f"passenger is rich {passenger_profile['wage']}")

    passenger_profile['fare'] = 8.50
    print(f"fare is {passenger_profile['fare']}")

if __name__ == "__main__":
    main()