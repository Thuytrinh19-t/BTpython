def main():
    n = int(input())

    city_to_country = {}

    for _ in range(n):
        data = input().split()
        country = data[0]
        cities = data[1:]
        for city in cities:
            city_to_country[city] = country

    m = int(input())

    for _ in range(m):
        city_query = input()
        country = city_to_country.get(city_query, "Unknown")
        print(f"{city_query} {country}")

if __name__ == "__main__":
    main()
