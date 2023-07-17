# from bs4 import BeautifulSoup
# import requests

# # URL of the page to be scraped
# result = {}
# stats_needed = {
#   'points': True,
#   'podiums': True,
#   'grands_prix_entered': True,
#   'world_championships': True,
#   "highest_race_finish": True,
#   "highest_grid_position": True,

# }
# urls = ['https://www.formula1.com/en/drivers/max-verstappen.html', 
#         'https://www.formula1.com/en/drivers/lewis-hamilton.html', 
#         'https://www.formula1.com/en/drivers/alexander-albon.html',
#         'https://www.formula1.com/en/drivers/nico-hulkenberg.html',
#         'https://www.formula1.com/en/drivers/sergio-perez.html',
#         'https://www.formula1.com/en/drivers/logan-sargeant.html',
#         'https://www.formula1.com/en/drivers/fernando-alonso.html',
#         'https://www.formula1.com/en/drivers/charles-leclerc.html',
#         'https://www.formula1.com/en/drivers/oscar-piastri.html',
#         'https://www.formula1.com/en/drivers/lance-stroll.html',
#         'https://www.formula1.com/en/drivers/valtteri-bottas.html',
#         'https://www.formula1.com/en/drivers/kevin-magnussen.html',
#         'https://www.formula1.com/en/drivers/daniel-ricciardo.html',
#         'https://www.formula1.com/en/drivers/yuki-tsunoda.html',
#         'https://www.formula1.com/en/drivers/pierre-gasly.html',
#         'https://www.formula1.com/en/drivers/lando-norris.html',
#         'https://www.formula1.com/en/drivers/george-russell.html',
#         'https://www.formula1.com/en/drivers/esteban-ocon.html',
#         'https://www.formula1.com/en/drivers/carlos-sainz.html',
#         'https://www.formula1.com/en/drivers/guanyu-zhou.html',
#         ]

# for url in urls:
#   page = requests.get(url)

#   soup = BeautifulSoup(page.content, 'html.parser')
#   driver = soup.find('h1', class_='driver-name').text.strip().lower().replace(' ', '_')
#   print(driver)

#   # Find the driver's headers
#   driver_headers = soup.find_all('th', class_='stat-key')
#   # print(driver_headers)

#   # Find the driver's stats
#   driver_stats = soup.find_all('td', class_='stat-value')
#   # print(driver_stats)

#   h = {}
#   for index, driverObj in enumerate(driver_headers):
#       key = driverObj.text.strip().replace(' ', '_').lower()
#       value = driver_stats[index].text.strip()
#       if stats_needed.get(key):
#         h[key] = value
#   result[driver] = h

# print(result)

# dummy result info to avoid scraping
result = {'max_verstappen': {'podiums': '87', 'points': '2266.5', 'grands_prix_entered': '173', 'world_championships': '2', 'highest_race_finish': '1 (x43)', 'highest_grid_position': '1'}, 'lewis_hamilton': {'podiums': '195', 'points': '4526.5', 'grands_prix_entered': '320', 'world_championships': '7', 'highest_race_finish': '1 (x103)', 'highest_grid_position': '1'}, 'alexander_albon': {'podiums': '2', 'points': '212', 'grands_prix_entered': '69', 'world_championships': 'N/A', 'highest_race_finish': '3 (x2)', 'highest_grid_position': '4'}, 'nico_hulkenberg': {'podiums': 'N/A', 'points': '530', 'grands_prix_entered': '194', 'world_championships': 'N/A', 'highest_race_finish': '4 (x3)', 'highest_grid_position': '1'}, 'sergio_perez': {'podiums': '31', 'points': '1357', 'grands_prix_entered': '246', 'world_championships': 'N/A', 'highest_race_finish': '1 (x6)', 'highest_grid_position': '1'}, 'logan_sargeant': {'podiums': 'N/A', 'points': '0', 'grands_prix_entered': '10', 'world_championships': 'N/A', 'highest_race_finish': '11 (x1)', 'highest_grid_position': '14'}, 'fernando_alonso': {'podiums': '104', 'points': '2198', 'grands_prix_entered': '368', 'world_championships': '2', 'highest_race_finish': '1 (x32)', 'highest_grid_position': '1'}, 'charles_leclerc': {'podiums': '26', 'points': '942', 'grands_prix_entered': '113', 'world_championships': 'N/A', 'highest_race_finish': '1 (x5)', 'highest_grid_position': '1'}, 'oscar_piastri': {'podiums': 'N/A', 'points': '17', 'grands_prix_entered': '10', 'world_championships': 'N/A', 'highest_race_finish': '4 (x1)', 'highest_grid_position': '3'}, 'lance_stroll': {'podiums': '3', 'points': '238', 'grands_prix_entered': '132', 'world_championships': 'N/A', 'highest_race_finish': '3 (x3)', 'highest_grid_position': '1'}, 'valtteri_bottas': {'podiums': '67', 'points': '1792', 'grands_prix_entered': '210', 'world_championships': 'N/A', 'highest_race_finish': '1 (x10)', 'highest_grid_position': '1'}, 'kevin_magnussen': {'podiums': '1', 'points': '185', 'grands_prix_entered': '152', 'world_championships': 'N/A', 'highest_race_finish': '2 (x1)', 'highest_grid_position': '4'}, 'daniel_ricciardo': {'podiums': '32', 'points': '1311', 'grands_prix_entered': '232', 'world_championships': 'N/A', 'highest_race_finish': '1 (x8)', 'highest_grid_position': '1'}, 'yuki_tsunoda': {'podiums': 'N/A', 'points': '46', 'grands_prix_entered': '54', 'world_championships': 'N/A', 'highest_race_finish': '4 (x1)', 'highest_grid_position': '7'}, 'pierre_gasly': {'podiums': '3', 'points': '348', 'grands_prix_entered': '118', 'world_championships': 'N/A', 'highest_race_finish': '1 (x1)', 'highest_grid_position': '2'}, 'lando_norris': {'podiums': '7', 'points': '470', 'grands_prix_entered': '92', 'world_championships': 'N/A', 'highest_race_finish': '2 (x2)', 'highest_grid_position': '1'}, 'george_russell': {'podiums': '10', 'points': '376', 'grands_prix_entered': '92', 'world_championships': 'N/A', 'highest_race_finish': '1 (x1)', 'highest_grid_position': '1'}, 'esteban_ocon': {'podiums': '3', 'points': '395', 'grands_prix_entered': '121', 'world_championships': 'N/A', 'highest_race_finish': '1 (x1)', 'highest_grid_position': '3'}, 'carlos_sainz': {'podiums': '15', 'points': '865.5', 'grands_prix_entered': '173', 'world_championships': 'N/A', 'highest_race_finish': '1 (x1)', 'highest_grid_position': '1'}, 'zhou_guanyu': {'podiums': 'N/A', 'points': '10', 'grands_prix_entered': '32', 'world_championships': 'N/A', 'highest_race_finish': '8 (x1)', 'highest_grid_position': '9'}}

## open and re-write the new drivers information to the drivers.json file

# open the drivers.json file
file_path = '/Users/bmklei8p/Projects/active/f1_app/utils/drivers.json'
file = open(file_path, 'r+')
lines = file.readlines()
driverLineStartLookup = {}
for key, value in result.items():
    search_key = 'driverId'
    search_value = key
    
    for i, line in enumerate(lines, start=1):
        if search_key in line and search_value in line:
            pos = i
            driverLineStartLookup[key] = pos
            break
    else:
        print("Key-value pair not found in the file.")
  # # formattedKey = f'{"driverId": "{key}"}'
  # print(key)
  # test_key = '"driverId": "max_verstappen"'
  # pos = lines.index(test_key)
  # print(pos)
  # # positions = []
  # # for line in lines:
  # #  if key in line:
  # #    positions.append(lines.index(line))
  # # for position in positions:
  # #   print(position)
  # #   print(lines[position])
    

# write the result to the file
# close the file
print(driverLineStartLookup)
file.close()