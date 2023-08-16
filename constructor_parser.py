from bs4 import BeautifulSoup
import requests


class ConstructorParser:
  def __init__(self, url):
    self.url = url
  
  def constructor_name_to_constructor_id(self, constructor_name):
    match constructor_name:
      case 'red_bull':
        constructor = 'red_bull'
      case 'mercedes':
        constructor = 'mercedes'
      case 'aston_martin':
        constructor = 'aston_martin'
      case 'ferrari':
        constructor = 'ferrari'
      case 'mclaren':
        constructor = 'mclaren'
      case 'alpine':
        constructor = 'alpine'
      case 'williams':
        constructor = 'williams'
      case 'haas':
        constructor = 'haas'
      case 'alfa_romeo':
        constructor = 'alfa'
      case 'alphatauri':
        constructor = 'alphatauri'
      case _:
        constructor = 'unknown'
    return constructor
  
  def constructor_name_to_constructor_twitter_handle(self, constructor_name):
    match constructor_name:
      case 'red_bull':
        constructor = 'redbullracing'
      case 'mercedes':
        constructor = 'MercedesAMGF1'
      case 'aston_martin':
        constructor = 'AstonMartinF1'
      case 'ferrari':
        constructor = 'ScuderiaFerrari'
      case 'mclaren':
        constructor = 'McLarenF1'
      case 'alpine':
        constructor = 'AlpineF1Team'
      case 'williams':
        constructor = 'WilliamsRacing'
      case 'haas':
        constructor = 'HaasF1Team'
      case 'alfa':
        constructor = 'alfaromeostake'
      case 'alphatauri':
        constructor = 'AlphaTauriF1'
      case _:
        constructor = 'unknown'
    return constructor

  def get_constructor_information_from_urls(self, urls):
    result = {}
    stats_needed = {
      'highest_race_finish': True,
      'pole_positions': True,
      'world_championships': True,
      'chassis': True,
    }

    for url in urls:
      page = requests.get(url)

      soup = BeautifulSoup(page.content, 'html.parser')
      constructor_name = soup.find('h1', class_='headline').text.strip().lower().replace(' ', '_')
      constructor = self.constructor_name_to_constructor_id(constructor_name)
      print(constructor)
      # Find the constructor's headers
      constructor_headers = soup.find_all('th', class_='stat-key')
      # print(constructor_headers)

      # Find the constructor's stats
      constructor_stats = soup.find_all('td', class_='stat-value')
      # print(constructor_stats)

      # Create a dictionary of the constructor's stats
      h = {}
      h["twitter_handle"] = self.constructor_name_to_constructor_twitter_handle(constructor)
      for index, constructorObj in enumerate(constructor_headers):
          key = constructorObj.text.strip().replace(' ', '_').lower()
          value = constructor_stats[index].text.strip()
          if stats_needed.get(key):
            h[key] = value
      result[constructor] = h
    print(result)
    return result

  def constructor_update(self, urls):
    # hard coded data to avoid scrappping while building
    # constructor_info = {'red_bull': {'twitter_handle': 'redbullracing', 'chassis': 'RB19', 'world_championships': '5', 'highest_race_finish': '1 (x104)', 'pole_positions': '92'}, 'mercedes': {'twitter_handle': 'MercedesAMGF1', 'chassis': 'W14', 'world_championships': '8', 'highest_race_finish': '1 (x116)', 'pole_positions': '129'}, 'alphatauri': {'twitter_handle': 'AlphaTauriF1', 'chassis': 'AT04', 'world_championships': 'N/A', 'highest_race_finish': '1 (x2)', 'pole_positions': '1'}, 'alfa': {'twitter_handle': 'unknown', 'chassis': 'C43', 'world_championships': 'N/A', 'highest_race_finish': '1 (x1)', 'pole_positions': '1'}, 'alpine': {'twitter_handle': 'AlpineF1Team', 'chassis': 'A523', 'world_championships': '2', 'highest_race_finish': '1 (x21)', 'pole_positions': '20'}, 'haas': {'twitter_handle': 'HaasF1Team', 'chassis': 'VF-23', 'world_championships': 'N/A', 'highest_race_finish': '4 (x1)', 'pole_positions': '1'}, 'williams': {'twitter_handle': 'WilliamsRacing', 'chassis': 'FW45', 'world_championships': '9', 'highest_race_finish': '1 (x114)', 'pole_positions': '128'}, 'mclaren': {'twitter_handle': 'McLarenF1', 'chassis': 'MCL60', 'world_championships': '8', 'highest_race_finish': '1 (x183)', 'pole_positions': '156'}, 'ferrari': {'twitter_handle': 'ScuderiaFerrari', 'chassis': 'SF-23', 'world_championships': '16', 'highest_race_finish': '1 (x243)', 'pole_positions': '245'}}
    constructor_info = self.get_constructor_information_from_urls(urls)

    all_completly_updated = True
    for key, value in constructor_info.items():
      request = requests.patch(f'http://localhost:3000/api/constructors/{key}', json=value)
      if (request.status_code == 404 or request.status_code == 500):
        print(f'Error {request.status_code} updating constructor: {key}')
        all_completly_updated = False
      elif (request.status_code == 200):
        print(f'Successfully updated constructor: {key}')
      else:
        print(f'Unknown error updating constructor: {key}')
        all_completly_updated = False

    if all_completly_updated:
      print('All constructors updated')
    else:
      print('Issue updating some constructors')
    return
    

urls =[
      # 'https://www.formula1.com/en/teams/Red-Bull-Racing.html',
      # 'https://www.formula1.com/en/teams/Mercedes.html',
      # 'https://www.formula1.com/en/teams/AlphaTauri.html',
      'https://www.formula1.com/en/teams/Aston-Martin.html'
      # 'https://www.formula1.com/en/teams/Alfa-Romeo.html',
      # 'https://www.formula1.com/en/teams/Alpine.html',
      # 'https://www.formula1.com/en/teams/Haas-F1-Team.html',
      # 'https://www.formula1.com/en/teams/Williams.html',
      # 'https://www.formula1.com/en/teams/McLaren.html',
      # 'https://www.formula1.com/en/teams/Ferrari.html',
      ]


constructor_parser = ConstructorParser(urls)
constructor_parser.constructor_update(urls)








