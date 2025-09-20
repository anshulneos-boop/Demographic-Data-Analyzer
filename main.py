import demographic_data_analyzer as dda

if __name__ == "__main__":
    results = dda.calculate_demographics()

    # Print results
    for key, value in results.items():
        print(f"{key}: {value}")
