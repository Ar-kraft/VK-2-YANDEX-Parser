import requests
from req import YaUploader
from req import token


token_v = "WRITE YOUR TOKEN HERE"
#service token to get access
version = 5.77
#actual version of API
owner_id = 552934290
album_id = 'profile'
photo_sizes  = 1
extended = 1
#identificator of donor user
#method of vk api - photos.get
response = requests.get('https://api.vk.com/method/photos.get/',
                        params={
                        'access_token': token_v,
                        'v': version,
                        'owner_id':owner_id,
                        'album_id':album_id,
                        'photo_sizes':photo_sizes,
                        'extended':extended
                        }
                        )
#new method open
data = response.json()['response']['items'][0]['sizes'][-1]['url']
dict_save = {}
data_raw= response.json()['response']
iii = range(0, data_raw['count'])
print('qqqqqqqqqqqqqqqqqqqqqqq')
for i in iii:
    url = response.json()['response']['items'][i]['sizes'][-1]['url']
    name_of_file = str(response.json()['response']['items'][i]['likes']['count']) + '.jpeg'
    rq = requests.get(url)
    with open(name_of_file, "wb") as code:
       code.write(rq.content)

    uploader = YaUploader(name_of_file, token)
    result = uploader.upload()
    print(name_of_file + ' ' + str(result) + '\n')

