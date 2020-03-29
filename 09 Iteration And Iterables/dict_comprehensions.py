country_to_capital = { 'United Kingdom': 'London',
                        'Brazil': 'Brasília',
                        'Morocco': 'Rabat',
                        'Sweden': 'Stockholm' }
capital_to_country = {capital: country for country, capital in country_to_capital.items()}
from pprint import pprint as pp
pp(capital_to_country)
