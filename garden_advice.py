# Gardening Advice Program


# Get user input for the season and type of plant (Add input)
'''
    Get user input and convert to lowercase to match
    all input types.
'''
season = input("Enter the season (summer/winter): ").lower()
plant_type = input("Enter the plant type (flower/vegetable): ").lower()

# Function to generate advice (Add function here)
def get_gardening_advice(season, plant_type):
    '''
        This function uses dictionaries to store advice for plants
        and seasons.

        The advice is then determined by entered season and plant type.
        For incorrect input, a no advice message will be displayed.
    '''

    # Dictionary for storing advice for seasons
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n"
    }

    # Dictionary storing advice for plants
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!"
    }

    # Determine advice based on the season
    advice = season_advice.get(season, "No advice for this season.\n")

    # Determine advice based on the plant type
    advice += plant_advice.get(
        plant_type,
        "No advice for this type of plant."
    )

    return advice


# Generate and display the advice
advice = get_gardening_advice(season, plant_type)

print("\nGardening Advice:")
print(advice)
