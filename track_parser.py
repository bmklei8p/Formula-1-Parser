from bs4 import BeautifulSoup
import requests


class TrackParser:
  def __init__(self, url):
    self.url = url

  def track_name_to_circuit_id(self, track_name):
    match track_name:
      case 'bahrain2023':
        circuit_id = 'bahrain'
      case 'australia2023':
        circuit_id = 'albert_park'
      case 'azerbaijan2023':
        circuit_id = 'baku'
      case 'spain2023':
        circuit_id = 'catalunya'
      case 'hungary2023':
        circuit_id = 'hungaroring'
      case 'brazil2023':
        circuit_id = 'interlagos'
      case 'saudi_arabia2023':
        circuit_id = 'jeddah'
      case 'qatar2023':
        circuit_id = 'losail'
      case 'singapore2023':
        circuit_id = 'marina_bay'
      case 'monaco2023':
        circuit_id = 'monaco'
      case 'austria2023':
        circuit_id = 'red_bull_ring'
      case 'mexico2023':
        circuit_id = 'rodriguez'
      case 'great_britain2023':
        circuit_id = 'silverstone'
      case 'belgium2023':
        circuit_id = 'spa'
      case 'japan2023':
        circuit_id = 'suzuka'
      case 'canada2023':
        circuit_id = 'villeneuve'
      case 'abu_dhabi2023':
        circuit_id = 'yas_marina'
      case 'netherlands2023':
        circuit_id = 'zandvoort'
      case 'italy2023':
        circuit_id = 'monza'
      case _:
        circuit_id = ''


    return circuit_id

  def get_track_information_from_urls(self, urls):
    result = {}
    stats_needed = {
      'first_grand_prix': True,
      'number_of_laps': True,
      'circuit_length': True,
      'race_distance': True,
      "lap_record": True,
    }
    first = True
    second = True

    for url in urls:
      page = requests.get(url)

      soup = BeautifulSoup(page.content, 'html.parser')
      track_name = soup.find('h1').text.strip().lower().replace(' ', '_')

      ## there are three united_states2023 tracks and this handles them before sending it to the url

      if track_name == 'united_states2023' and first:
        circuit_id = 'miami'
        first = False
      elif track_name == 'united_states2023' and second:
        circuit_id = 'americas'
        second = False
      elif track_name == 'united_states2023':
        circuit_id = 'vegas'
      else:
        circuit_id = self.track_name_to_circuit_id(track_name)

      # Find official race name
      official_track_name_all_lowercase = soup.find('p', class_='f1--s').text.strip().lower()
      words = official_track_name_all_lowercase.split(" ")
      modified_words = [word.capitalize() for word in words]
      official_track_name = " ".join(modified_words)

      # Find circuit name
      circuit_name = soup.find('span', class_='d-none d-lg-block').text.strip()
      print(circuit_name)


      # Find the driver's headers
      track_headers = soup.find_all('p', class_='misc--label')


      # Find the driver's stats
      track_stats = soup.find_all('p', class_='f1-bold--stat')


      # Create a dictionary of the driver's stats
      h = {}
      h["official_track_name"] = official_track_name
      h["circuit_name"] = circuit_name
      for index, track_object in enumerate(track_headers):
          key = track_object.text.strip().replace(' ', '_').lower()
          value = track_stats[index].text.strip()
          if stats_needed.get(key):
            h[key] = value
          if key == 'lap_record':
            break
      result[circuit_id] = h
    print(result)
    return result

  def track_update(self, urls):
    # hard coded data to avoid scrappping while building
    # hard coded from url request 7/26/23
    track_info = {'bahrain': {'official_track_name': 'Formula 1 Gulf Air Bahrain Grand Prix 2023', 'circuit_name': 'Bahrain International Circuit', 'first_grand_prix': '2004', 'number_of_laps': '57', 'circuit_length': '5.412km', 'race_distance': '308.238 km', 'lap_record': '1:31.447 Pedro de la Rosa (2005)'}, 'jeddah': {'official_track_name': 'Formula 1 Stc Saudi Arabian Grand Prix 2023', 'circuit_name': 'Jeddah Corniche Circuit', 'first_grand_prix': '2021', 'number_of_laps': '50', 'circuit_length': '6.174km', 'race_distance': '308.45 km', 'lap_record': '1:30.734 Lewis Hamilton (2021)'}, 'albert_park': {'official_track_name': 'Formula 1 Rolex Australian Grand Prix 2023', 'circuit_name': 'Albert Park Circuit', 'first_grand_prix': '1996', 'number_of_laps': '58', 'circuit_length': '5.278km', 'race_distance': '306.124 km', 'lap_record': '1:20.235 Sergio Perez (2023)'}, 'baku': {'official_track_name': 'Formula 1 Azerbaijan Grand Prix 2023', 'circuit_name': 'Baku City Circuit', 'first_grand_prix': '2016', 'number_of_laps': '51', 'circuit_length': '6.003km', 'race_distance': '306.049 km', 'lap_record': '1:43.009 Charles Leclerc (2019)'}, 'miami': {'official_track_name': 'Formula 1 Crypto.com Miami Grand Prix 2023', 'circuit_name': 'Miami International Autodrome', 'first_grand_prix': '2022', 'number_of_laps': '57', 'circuit_length': '5.412km', 'race_distance': '308.326 km', 'lap_record': '1:29.708 Max Verstappen (2023)'}, 'monaco': {'official_track_name': 'Formula 1 Grand Prix De Monaco 2023', 'circuit_name': 'Circuit de Monaco', 'first_grand_prix': '1950', 'number_of_laps': '78', 'circuit_length': '3.337km', 'race_distance': '260.286 km', 'lap_record': '1:12.909 Lewis Hamilton (2021)'}, 'catalunya': {'official_track_name': 'Formula 1 Aws Gran Premio De España 2023', 'circuit_name': 'Circuit de Barcelona-Catalunya', 'first_grand_prix': '1991', 'number_of_laps': '66', 'circuit_length': '4.657km', 'race_distance': '307.236 km', 'lap_record': '1:16.330 Max Verstappen (2023)'}, 'villeneuve': {'official_track_name': 'Formula 1 Pirelli Grand Prix Du Canada 2023', 'circuit_name': 'Circuit Gilles-Villeneuve', 'first_grand_prix': '1978', 'number_of_laps': '70', 'circuit_length': '4.361km', 'race_distance': '305.27 km', 'lap_record': '1:13.078 Valtteri Bottas (2019)'}, 'red_bull_ring': {'official_track_name': 'Formula 1 Rolex Grosser Preis Von Österreich 2023', 'circuit_name': 'Red Bull Ring', 'first_grand_prix': '1970', 'number_of_laps': '71', 'circuit_length': '4.318km', 'race_distance': '306.452 km', 'lap_record': '1:05.619 Carlos Sainz (2020)'}, 'silverstone': {'official_track_name': 'Formula 1 Aramco British Grand Prix 2023', 'circuit_name': 'Silverstone Circuit', 'first_grand_prix': '1950', 'number_of_laps': '52', 'circuit_length': '5.891km', 'race_distance': '306.198 km', 'lap_record': '1:27.097 Max Verstappen (2020)'}, 'hungaroring': {'official_track_name': 'Formula 1 Qatar Airways Hungarian Grand Prix 2023', 'circuit_name': 'Hungaroring', 'first_grand_prix': '1986', 'number_of_laps': '70', 'circuit_length': '4.381km', 'race_distance': '306.63 km', 'lap_record': '1:16.627 Lewis Hamilton (2020)'}, 'spa': {'official_track_name': 'Formula 1 Msc Cruises Belgian Grand Prix 2023', 'circuit_name': 'Circuit de Spa-Francorchamps', 'first_grand_prix': '1950', 'number_of_laps': '44', 'circuit_length': '7.004km', 'race_distance': '308.052 km', 'lap_record': '1:46.286 Valtteri Bottas (2018)'}, 'zandvoort': {'official_track_name': 'Formula 1 Heineken Dutch Grand Prix 2023', 'circuit_name': 'Circuit Zandvoort', 'first_grand_prix': '1952', 'number_of_laps': '72', 'circuit_length': '4.259km', 'race_distance': '306.587 km', 'lap_record': '1:11.097 Lewis Hamilton (2021)'}, 'monza': {'official_track_name': 'Formula 1 Pirelli Gran Premio D’italia 2023', 'circuit_name': 'Autodromo Nazionale Monza', 'first_grand_prix': '1950', 'number_of_laps': '53', 'circuit_length': '5.793km', 'race_distance': '306.72 km', 'lap_record': '1:21.046 Rubens Barrichello (2004)'}, 'suzuka': {'official_track_name': 'Formula 1 Lenovo Japanese Grand Prix 2023', 'circuit_name': 'Suzuka International Racing Course', 'first_grand_prix': '1987', 'number_of_laps': '53', 'circuit_length': '5.807km', 'race_distance': '307.471 km', 'lap_record': '1:30.983 Lewis Hamilton (2019)'}, 'losail': {'official_track_name': 'Formula 1 Qatar Airways Qatar Grand Prix 2023', 'circuit_name': 'Lusail International Circuit', 'first_grand_prix': '2021', 'number_of_laps': '57', 'circuit_length': '5.418km', 'race_distance': '308.826 km', 'lap_record': 'null null (null)'}, 'americas': {'official_track_name': 'Formula 1 Lenovo United States Grand Prix 2023', 'circuit_name': 'Circuit of The Americas', 'first_grand_prix': '2012', 'number_of_laps': '56', 'circuit_length': '5.513km', 'race_distance': '308.405 km', 'lap_record': '1:36.169 Charles Leclerc (2019)'}, 'rodriguez': {'official_track_name': 'Formula 1 Gran Premio De La Ciudad De México 2023', 'circuit_name': 'Autódromo Hermanos Rodríguez', 'first_grand_prix': '1963', 'number_of_laps': '71', 'circuit_length': '4.304km', 'race_distance': '305.354 km', 'lap_record': '1:17.774 Valtteri Bottas (2021)'}, 'interlagos': {'official_track_name': 'Formula 1 Rolex Grande Prêmio De São Paulo 2023', 'circuit_name': 'Autódromo José Carlos Pace', 'first_grand_prix': '1973', 'number_of_laps': '71', 'circuit_length': '4.309km', 'race_distance': '305.879 km', 'lap_record': '1:10.540 Valtteri Bottas (2018)'}, 'vegas': {'official_track_name': 'Formula 1 Heineken Silver Las Vegas Grand Prix 2023', 'circuit_name': 'Las Vegas', 'first_grand_prix': '2023', 'number_of_laps': '50', 'circuit_length': '6.12km', 'race_distance': '305.88 km', 'lap_record': 'N/A  (N/A)'}, 'yas_marina': {'official_track_name': 'Formula 1 Etihad Airways Abu Dhabi Grand Prix 2023', 'circuit_name': 'Yas Marina Circuit', 'first_grand_prix': '2009', 'number_of_laps': '58', 'circuit_length': '5.281km', 'race_distance': '306.183 km', 'lap_record': '1:26.103 Max Verstappen (2021)'}}
    # track_info = self.get_track_information_from_urls(urls)

    all_completly_updated = True
    for key, value in track_info.items():
      request = requests.patch(f'http://localhost:3000/api/tracks/{key}', json=value)
      if (request.status_code == 404 or request.status_code == 500):
        print(f'Error updating track: {key}')
        all_completly_updated = False
      elif (request.status_code == 200):
        print(f'Successfully updated track: {key}')
      else:
        print(f'Unknown error updating track: {key}')
        all_completly_updated = False

    if all_completly_updated:
      print('All tracks updated')
    else:
      print('Issue updating some tracks')
    return


urls =[
      'https://www.formula1.com/en/racing/2023/Bahrain/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Saudi_Arabia/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Australia/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Azerbaijan/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Miami/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Monaco/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Spain/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Canada/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Austria/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Great_Britain/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Hungary/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Belgium/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Netherlands/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Italy/Circuit.html',
      # 'https://www.formula1.com/en/racing/2023/Singapore/Circuit.html',  this page does not have good info online: comes back as TBC 
      'https://www.formula1.com/en/racing/2023/Japan/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Qatar/Circuit.html',
      'https://www.formula1.com/en/racing/2023/United_States/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Mexico/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Brazil/Circuit.html',
      'https://www.formula1.com/en/racing/2023/Las_Vegas/Circuit.html',
      'https://www.formula1.com/en/racing/2023/United_Arab_Emirates/Circuit.html',
      ]


track_parser = TrackParser(urls)
track_parser.track_update(urls)



## need to extract the track name to circuit name logic to the function track_name_to_circuit_id. right now it is in the get_track_information_from_urls function due to First and Second logic
## should be able to move this to the other and use Class variables as First and Second. Not 100% sure how to do this yet


## possible issues: losail doesn't have any info on the website. comes back as null null (null) for lap record.  - verified they do not have the info
## possible issues: singapore does not have any info on the website. comes back as TBC for lap record. - verified they do not have the info
## possible issues: vegas does not have any info on the website. comes back as N/A for lap record. - verified they do not have the info
