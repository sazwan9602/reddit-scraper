from src import reddit

if __name__ == "__main__":
    subreddit = input("Enter subreddit name (no spaces): ")
    if " " in subreddit or not subreddit:
        print("Invalid input. Please enter a string with no spaces.")
    else:
        reddit.run(subreddit)
