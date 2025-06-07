# Simple data analysis without external dependencies

DATA = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [95, 85, 92]
}


def main():
    scores = DATA["Score"]
    avg = sum(scores) / len(scores)
    print(f"Average score: {avg:.1f}")
    highest = max(zip(DATA["Name"], scores), key=lambda x: x[1])
    print(f"Highest score: {highest[0]} with {highest[1]}")


if __name__ == "__main__":
    main()

