from bs4 import BeautifulSoup
import requests


class DriverParser:
  def __init__(self, url):
    self.url = url
  
  def driver_name_to_driver_id(self, driver_name):
    match driver_name:
      case 'max_verstappen':
        driver = 'max_verstappen'
      case 'lewis_hamilton':
        driver = 'hamilton'
      case 'alexander_albon':
        driver = 'albon'
      case 'nico_hulkenberg':
        driver = 'hulkenberg'
      case 'sergio_perez':
        driver = 'perez'
      case 'logan_sargeant':
        driver = 'sargeant'
      case 'fernando_alonso':
        driver = 'alonso'
      case 'charles_leclerc': 
        driver = 'leclerc'
      case 'oscar_piastri':
        driver = 'piastri'
      case 'lance_stroll':  
        driver = 'stroll'
      case 'valtteri_bottas': 
        driver = 'bottas'
      case 'kevin_magnussen':
        driver = 'kevin_magnussen'
      case 'daniel_ricciardo':
        driver = 'ricciardo'
      case 'yuki_tsunoda':  
        driver = 'tsunoda'
      case 'pierre_gasly':
        driver = 'gasly'
      case 'lando_norris':  
        driver = 'norris'
      case 'george_russell':  
        driver = 'russell'
      case 'esteban_ocon':  
        driver = 'ocon'
      case 'carlos_sainz':  
        driver = 'sainz'
      case 'zhou_guanyu':
        driver = 'zhou'
      case _:
        driver = 'unknown'
    return driver
  
  def driver_id_to_driver_twitter_handle(self, driver_name):
    match driver_name:
      case 'max_verstappen':
        driver = 'Max33Verstappen'
      case 'hamilton':
        driver = 'LewisHamilton'
      case 'albon':
        driver = 'alex_albon'
      case 'hulkenberg':
        driver = 'HulkHulkenberg'
      case 'perez':
        driver = 'SChecoPerez'
      case 'sargeant':
        driver = 'LoganSargeant'
      case 'alonso':
        driver = 'alo_oficial'
      case 'leclerc': 
        driver = 'Charles_Leclerc'
      case 'piastri':
        driver = 'OscarPiastri'
      case 'stroll':  
        driver = 'lance_stroll'
      case 'bottas': 
        driver = 'ValtteriBottas'
      case 'kevin_magnussen':
        driver = 'KevinMagnussen'
      case 'ricciardo':
        driver = 'danielricciardo'
      case 'tsunoda':  
        driver = 'yukitsunoda07'
      case 'gasly':
        driver = 'PierreGASLY'
      case 'norris':  
        driver = 'LandoNorris'
      case 'russell':  
        driver = 'GeorgeRussell63'
      case 'ocon':  
        driver = 'OconEsteban'
      case 'sainz':  
        driver = 'Carlossainz55'
      case 'zhou':
        driver = 'ZhouGuanyu24'
      case _:
        driver = 'unknown'
    return driver

  def get_driver_information_from_urls(self, urls):
    result = {}
    stats_needed = {
      'points': True,
      'podiums': True,
      'grands_prix_entered': True,
      'world_championships': True,
      "highest_race_finish": True,
      "highest_grid_position": True,
    }

    for url in urls:
      page = requests.get(url)

      soup = BeautifulSoup(page.content, 'html.parser')
      driver_name = soup.find('h1', class_='driver-name').text.strip().lower().replace(' ', '_')
      driver = self.driver_name_to_driver_id(driver_name)

      # Find the driver's headers
      driver_headers = soup.find_all('th', class_='stat-key')
      # print(driver_headers)

      # Find the driver's stats
      driver_stats = soup.find_all('td', class_='stat-value')
      # print(driver_stats)

      # Create a dictionary of the driver's stats
      h = {}
      h["twitter_handle"] = self.driver_id_to_driver_twitter_handle(driver)
      for index, driverObj in enumerate(driver_headers):
          key = driverObj.text.strip().replace(' ', '_').lower()
          value = driver_stats[index].text.strip()
          if stats_needed.get(key):
            h[key] = value
      result[driver] = h

    # print(result)
    return result

  def driver_update(self, urls):
    # hard coded data to avoid scrappping while building
    driver_info = {'max_verstappen': {'twitter_handle': 'Max33Verstappen', 'podiums': '89', 'points': '2325.5', 'grands_prix_entered': '175', 'world_championships': '2', 'highest_race_finish': '1 (x45)', 'highest_grid_position': '1'}, 'hamilton': {'twitter_handle': 'LewisHamilton', 'podiums': '195', 'points': '4553.5', 'grands_prix_entered': '322', 'world_championships': '7', 'highest_race_finish': '1 (x103)', 'highest_grid_position': '1'}, 'albon': {'twitter_handle': 'alex_albon', 'podiums': '2', 'points': '212', 'grands_prix_entered': '71', 'world_championships': 'N/A', 'highest_race_finish': '3 (x2)', 'highest_grid_position': '4'}, 'hulkenberg': {'twitter_handle': 'HulkHulkenberg', 'podiums': 'N/A', 'points': '530', 'grands_prix_entered': '196', 'world_championships': 'N/A', 'highest_race_finish': '4 (x3)', 'highest_grid_position': '1'}, 'perez': {'twitter_handle': 'SChecoPerez', 'podiums': '33', 'points': '1390', 'grands_prix_entered': '248', 'world_championships': 'N/A', 'highest_race_finish': '1 (x6)', 'highest_grid_position': '1'}, 'sargeant': {'twitter_handle': 'LoganSargeant', 'podiums': 'N/A', 'points': '0', 'grands_prix_entered': '12', 'world_championships': 'N/A', 'highest_race_finish': '11 (x1)', 'highest_grid_position': '14'}, 'alonso': {'twitter_handle': 'alo_oficial', 'podiums': '104', 'points': '2210', 'grands_prix_entered': '370', 'world_championships': '2', 'highest_race_finish': '1 (x32)', 'highest_grid_position': '1'}, 'leclerc': {'twitter_handle': 'Charles_Leclerc', 'podiums': '27', 'points': '967', 'grands_prix_entered': '115', 'world_championships': 'N/A', 'highest_race_finish': '1 (x5)', 'highest_grid_position': '1'}, 'piastri': {'twitter_handle': 'OscarPiastri', 'podiums': 'N/A', 'points': '34', 'grands_prix_entered': '12', 'world_championships': 'N/A', 'highest_race_finish': '4 (x1)', 'highest_grid_position': '3'}, 'stroll': {'twitter_handle': 'lance_stroll', 'podiums': '3', 'points': '241', 'grands_prix_entered': '134', 'world_championships': 'N/A', 'highest_race_finish': '3 (x3)', 'highest_grid_position': '1'}, 'bottas': {'twitter_handle': 'ValtteriBottas', 'podiums': '67', 'points': '1792', 'grands_prix_entered': '212', 'world_championships': 'N/A', 'highest_race_finish': '1 (x10)', 'highest_grid_position': '1'}, 'kevin_magnussen': {'twitter_handle': 'KevinMagnussen', 'podiums': '1', 'points': '185', 'grands_prix_entered': '154', 'world_championships': 'N/A', 'highest_race_finish': '2 (x1)', 'highest_grid_position': '4'}, 'ricciardo': {'twitter_handle': 'danielricciardo', 'podiums': '32', 'points': '1311', 'grands_prix_entered': '234', 'world_championships': 'N/A', 'highest_race_finish': '1 (x8)', 'highest_grid_position': '1'}, 'tsunoda': {'twitter_handle': 'yukitsunoda07', 'podiums': 'N/A', 'points': '47', 'grands_prix_entered': '56', 'world_championships': 'N/A', 'highest_race_finish': '4 (x1)', 'highest_grid_position': '7'}, 'gasly': {'twitter_handle': 'PierreGASLY', 'podiums': '3', 'points': '354', 'grands_prix_entered': '120', 'world_championships': 'N/A', 'highest_race_finish': '1 (x1)', 'highest_grid_position': '2'}, 'norris': {'twitter_handle': 'LandoNorris', 'podiums': '8', 'points': '497', 'grands_prix_entered': '94', 'world_championships': 'N/A', 'highest_race_finish': '2 (x3)', 'highest_grid_position': '1'}, 'russell': {'twitter_handle': 'GeorgeRussell63', 'podiums': '10', 'points': '393', 'grands_prix_entered': '94', 'world_championships': 'N/A', 'highest_race_finish': '1 (x1)', 'highest_grid_position': '1'}, 'ocon': {'twitter_handle': 'OconEsteban', 'podiums': '3', 'points': '399', 'grands_prix_entered': '123', 'world_championships': 'N/A', 'highest_race_finish': '1 (x1)', 'highest_grid_position': '3'}, 'sainz': {'twitter_handle': 'Carlossainz55', 'podiums': '15', 'points': '874.5', 'grands_prix_entered': '175', 'world_championships': 'N/A', 'highest_race_finish': '1 (x1)', 'highest_grid_position': '1'}, 'zhou': {'twitter_handle': 'ZhouGuanyu24', 'podiums': 'N/A', 'points': '10', 'grands_prix_entered': '34', 'world_championships': 'N/A', 'highest_race_finish': '8 (x1)', 'highest_grid_position': '5'}}
    # driver_info = self.get_driver_information_from_urls(urls)

    all_completly_updated = True
    for key, value in driver_info.items():
      request = requests.patch(f'http://localhost:3000/api/drivers/{key}', json=value)
      if (request.status_code == 404 or request.status_code == 500):
        print(f'Error {request.status_code} updating driver: {key}')
        all_completly_updated = False
      elif (request.status_code == 200):
        print(f'Successfully updated driver: {key}')
      else:
        print(f'Unknown error updating driver: {key}')
        all_completly_updated = False

    if all_completly_updated:
      print('All drivers updated')
    else:
      print('Issue updating some drivers')
    return

urls =[
      'https://www.formula1.com/en/drivers/max-verstappen.html', 
      'https://www.formula1.com/en/drivers/lewis-hamilton.html', 
      'https://www.formula1.com/en/drivers/alexander-albon.html',
      'https://www.formula1.com/en/drivers/nico-hulkenberg.html',
      'https://www.formula1.com/en/drivers/sergio-perez.html',
      'https://www.formula1.com/en/drivers/logan-sargeant.html',
      'https://www.formula1.com/en/drivers/fernando-alonso.html',
      'https://www.formula1.com/en/drivers/charles-leclerc.html',
      'https://www.formula1.com/en/drivers/oscar-piastri.html',
      'https://www.formula1.com/en/drivers/lance-stroll.html',
      'https://www.formula1.com/en/drivers/valtteri-bottas.html',
      'https://www.formula1.com/en/drivers/kevin-magnussen.html',
      'https://www.formula1.com/en/drivers/daniel-ricciardo.html',
      'https://www.formula1.com/en/drivers/yuki-tsunoda.html',
      'https://www.formula1.com/en/drivers/pierre-gasly.html',
      'https://www.formula1.com/en/drivers/lando-norris.html',
      'https://www.formula1.com/en/drivers/george-russell.html',
      'https://www.formula1.com/en/drivers/esteban-ocon.html',
      'https://www.formula1.com/en/drivers/carlos-sainz.html',
      'https://www.formula1.com/en/drivers/guanyu-zhou.html',
      ]


driver_parser = DriverParser(urls)
driver_parser.driver_update(urls)








