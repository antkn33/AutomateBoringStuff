import requests
# requests.readthedocs.org

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code 
# 200 if successful
# 
# res.text # to display the downloaded text file
# print(res.text[:500]) # print first 500 characters

res.raise_for_status() # display error if it occurs

#
playFile = open('RomeoAndJuliet.txt', 'wb') # wb is write binary, for a downloaded file
# write to file
for chunk in res.iter_content(100000): # Write 100,000 bytes per chunk
    playFile.write(chunk)
