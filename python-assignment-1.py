print("Ritik Tomar")
print("E22CSEU0712")
class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def list_matches_by_team(self, team_name):
        team_matches = []
        for match in self.matches:
            if team_name in (match.team1, match.team2):
                team_matches.append(match)
        return team_matches

    def list_matches_by_location(self, location):
        location_matches = []
        for match in self.matches:
            if match.location == location:
                location_matches.append(match)
        return location_matches

    def list_matches_by_timing(self, timing):
        timing_matches = []
        for match in self.matches:
            if match.timing == timing:
                timing_matches.append(match)
        return timing_matches

def main():
    flight_table = FlightTable()

    # Adding matches to the table
    flight_table.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    flight_table.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    flight_table.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    flight_table.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    flight_table.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    flight_table.add_match(Match("Delhi", "India", "Australia", "DAY"))

    print("Search options:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        team_name = input("Enter the team name: ")
        team_matches = flight_table.list_matches_by_team(team_name)
        print(f"Matches involving {team_name}:")
        for match in team_matches:
            print(f"{match.team1} vs {match.team2} at {match.location}, Timing: {match.timing}")

    elif choice == 2:
        location = input("Enter the location: ")
        location_matches = flight_table.list_matches_by_location(location)
        print(f"Matches at {location}:")
        for match in location_matches:
            print(f"{match.team1} vs {match.team2}, Timing: {match.timing}")

    elif choice == 3:
        timing = input("Enter the timing: ")
        timing_matches = flight_table.list_matches_by_timing(timing)
        print(f"Matches with timing {timing}:")
        for match in timing_matches:
            print(f"{match.team1} vs {match.team2} at {match.location}")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
