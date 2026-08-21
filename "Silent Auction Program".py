import os

# Display welcome message
print("***** Welcome to the Silent Auction Program *****")


# Function to find the bidder who made the highest bid
def find_winner(bidder_details):

    # Store the highest bid value
    highest_bid = 0

    # Store the name of the winner
    winner = ""

    # Loop through all bidders
    for bidder in bidder_details:

        # Get the bid price of the current bidder
        bidding_price = bidder_details[bidder]

        # Check if the current bid is higher than the highest bid
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder

    # Display the winner
    print(f"Here is the list of all the bidders: {winner}")
    print(f"The winner is {winner} with a bid price of ${highest_bid}")


# Create an empty dictionary to store bidder names and bids
bidder_deta = {}

# Variable to control the bidding loop
end_of_bidding = False


# Continue taking bids until there are no more bidders
while not end_of_bidding:

    # Ask the bidder for their name
    name = input("What is your name?: ")

    # Ask the bidder for their bidding price
    price = int(input("What is your bidding price?: "))

    # Store the bidder's name and price in the dictionary
    bidder_deta[name] = price

    # Ask if there are more bidders
    more_bidders = input(
        "Are there more bidders? Type 'yes' or 'no': "
    ).lower()

    # If there are no more bidders
    if more_bidders == "no":
        end_of_bidding = True

        # Find and display the winner
        find_winner(bidder_deta)

    # If there are more bidders
    elif more_bidders == "yes":

        # Clear the screen before the next bidder enters
        os.system("cls")py
