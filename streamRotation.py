def getNextCampus(campusCount, totalCampuses):
    return (campusCount + 1) % totalCampuses

def initCampuses(numberOfCampuses):
    return list(range(numberOfCampuses))

def initConnections(numberOfCampuses):
    campusList = initCampuses(numberOfCampuses)
    connections = {}
    for campus in campusList:
        connections[campus] = getNextCampus(campus, numberOfCampuses)
    return connections

def printConnections(connections, totalCampuses):
    # Format connections, ensuring no self-pointing
    formatted_connections = ', '.join(
        f"{k}->{(v + 1) % totalCampuses if k == v else v}" for k, v in connections.items()
    )
    print(f"{{ {formatted_connections} }}")

# Main loop for campus rotation
def main():
    numberOfCampuses = 5
    connections = initConnections(numberOfCampuses)
    currentCampus = 0
    rounds = 0

    while True:
        if rounds == 0:
            print("Initial connections:")
        else:
            # Update connections based on the current campus
            for campus in list(connections.keys()):
                connections[campus] = getNextCampus(connections[campus], numberOfCampuses)

        printConnections(connections, numberOfCampuses)

        user_input = input("Type 'next' to go to the next campus or 'exit' to quit: ").strip().lower()

        if user_input == "next":
            currentCampus = connections[currentCampus]
            rounds += 1
        elif user_input == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid input. Please type 'next' or 'exit'.")

if __name__ == "__main__":
    main()
