needocr = ['https://www.mass.gov/doc/james-brenda-v-boston-police-department-related-superior-court-decision-122217/download',
'https://www.mass.gov/doc/leeman-pagliuca-v-haverhill-related-appeals-court-decision-62017/download',
'https://www.mass.gov/doc/mccormack-v-department-of-state-police-related-appeals-court-decision-81417-0/download',
'https://www.mass.gov/doc/mcgoldrick-patricia-v-boston-police-department-33017/download',
'https://www.mass.gov/doc/otero-daniel-v-city-of-lowell-related-superior-court-decision-112817/download']

needocrnames = ['james','leeman','mccormack','mcgoldrick','otero']

noocr = ['https://www.mass.gov/doc/godere-jeffrey-v-city-of-chicopee-21320/download',
'https://www.mass.gov/doc/gould-david-v-town-of-north-attleborough-6718/download',
'https://www.mass.gov/doc/grasso-moccio-v-town-of-agawam-91417-0/download',
'https://www.mass.gov/doc/green-william-v-city-of-lawrence-121919/download',
'https://www.mass.gov/doc/halcovich-angela-v-city-of-revere-22720/download',
'https://www.mass.gov/doc/labelle-richard-v-springfield-police-department-41119/download',
'https://www.mass.gov/doc/lewandowski-gregory-v-town-of-charlton-4920/download',
'https://www.mass.gov/doc/levesque-adam-v-town-of-middleborough-31419/download',
'https://www.mass.gov/doc/merricks-kirk-v-boston-police-department-51018/download',
'https://www.mass.gov/doc/reger-crespi-adams-russell-v-department-of-state-police-32819/download',
'https://www.mass.gov/doc/torres-vicente-v-city-of-chicopee-12717/download',
'https://www.mass.gov/doc/wolski-joseph-v-city-of-gardner-3118/download']

noocrnames = ["godere","gould","grasso","green","halcovich","labelle","lewandowski","levesque",'merricks',"reger","torres","wolski"]

import requests
for i, url in enumerate(needocr):
    response = requests.get(url)
    name = needocrnames[i]
    
    with open(f'needocr/{name}.pdf', 'wb') as f:
        f.write(response.content)