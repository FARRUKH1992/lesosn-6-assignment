#Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 


def highlight_keywords(review, keywords):
    """
    Function to capitalize keywords in a review.
    
    Parameters:
    review (str): The review text.
    keywords (list): A list of keywords to be highlighted.
    
    Returns:
    str: The review with keywords capitalized.
    """
    for keyword in keywords:
        # Replace each keyword with its uppercase version
        review = review.replace(keyword, keyword.upper())
    return review

def main():
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
    
    keywords = ["good", "excellent", "bad", "poor", "average"]
    
    for review in reviews:
        highlighted_review = highlight_keywords(review, keywords)
        print(highlighted_review)

if __name__ == "__main__":
    main()



# highlight_keywords Function:
# Returns the updated review
# Defines a list of reviews and a list of keywords to highlight



# task 2
# positive and negative words.
# positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
#  negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

def tally_sentiment(reviews, positive_words, negative_words):
    """
    Function to tally positive and negative words in each review.
    
    Parameters:
    reviews (list): A list of review texts.
    positive_words (list): A list of positive words.
    negative_words (list): A list of negative words.
    
    Returns:
    dict: A dictionary with total counts of positive and negative words.
    """
    positive_count = 0
    negative_count = 0

    for review in reviews:
        words = review.lower().split()
        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1
    
    return {
        "positive": positive_count,
        "negative": negative_count
    }

def create_summary(review, length=30):
    """
    Function to create a summary of the review by truncating it to the specified length.
    
    Parameters:
    review (str): The review text.
    length (int): The maximum length of the summary including ellipsis.
    
    Returns:
    str: The review summary.
    """
    if len(review) <= length:
        return review
    
    # Find the last space within the limit to avoid cutting off a word
    summary = review[:length].rsplit(' ', 1)[0]
    return summary + "…"

def main():
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
    
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    
    # Task 2: Tally sentiment
    sentiment_counts = tally_sentiment(reviews, positive_words, negative_words)
    print("Sentiment Tally:")
    print(f"Total positive words: {sentiment_counts['positive']}")
    print(f"Total negative words: {sentiment_counts['negative']}")
    
    # Task 3: Review Summary
    print("\nReview Summaries:")
    for review in reviews:
        summary = create_summary(review)
        print(summary)

if __name__ == "__main__":
    main()


# User Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.
# Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message



def validate_name_length(name, name_type):
    """
    Function to validate the length of a name.
    
    Parameters:
    name (str): The name to be validated.
    name_type (str): A description of the name (e.g., 'first name' or 'last name').
    
    Returns:
    bool: True if the name is valid, False otherwise.
    """
    if len(name) < 2:
        print(f"Error: The {name_type} must be at least 2 characters long.")
        return False
    return True

def main():
    # Ask for user input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    # Validate the length of the names
    first_name_valid = validate_name_length(first_name, "first name")
    last_name_valid = validate_name_length(last_name, "last name")
    
    # Check if both names are valid
    if first_name_valid and last_name_valid:
        print(f"Welcome, {first_name} {last_name}!")
    else:
        print("Please provide valid names.")

if __name__ == "__main__":
    main()
