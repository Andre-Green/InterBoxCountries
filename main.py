import requests
from prettytable import PrettyTable

class CountryInfo:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_country_data(self, country_name):
        response = requests.get(f"{self.api_url}/name/{country_name}")
        if response.status_code == 200:
            data = response.json()
            if data:
                country = data[0]
                name = country.get('name', {}).get('common', 'N/A')
                capital = country.get('capital', ['N/A'])[0]
                flag_url = country.get('flags', {}).get('png', 'N/A')
                return name, capital, flag_url
            else:
                return None
        else:
            return None

    def display_country_info(self, country_name):
        country_data = self.get_country_data(country_name)
        if country_data:
            table = PrettyTable()
            table.field_names = ["Country", "Capital", "Flag URL"]
            table.add_row(country_data)
            print(table)
        else:
            print(f"Could not find data for country: {country_name}")


def all_countries(api_url):
    response = requests.get(f"{api_url}/all")
    if response.status_code == 200:
        counries = response.json()
        for counrie in counries:
            counries_names = (counrie['name']['common'])
            print(counries_names)
    else:
        print(f"API don't work. Response status code: {response.status_code}")



if __name__ == "__main__":
    api_url = "https://restcountries.com/v3.1"
    country_info = CountryInfo(api_url)

    country_name = input("Enter the name of the country: ")
    country_info.display_country_info(country_name)
    # all_countries(api_url)