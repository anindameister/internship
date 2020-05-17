import wikipedia
import pandas as pd

page = wikipedia.page("elephant")


af = pd.DataFrame(data={"object_1": page.images[0:]})
af.to_csv("./imgs_url.csv", sep=',',index=False)

import urllib.request
import wikipedia
page = wikipedia.page("elephant")
image_link = page.images[0]
urllib.request.urlretrieve(image_link , "local-filename.jpg")

# import modules
import pandas as pd
import urllib.request
def url2jpg(i,url,file_path):
    """
    --i :number of images
    --url:url address
    --filepath:where to save the final image
    """
    filename='image-{}.jpg'.format(i)
    full_path="{}{}".format(file_path, filename)
    urllib.request.urlretrieve(url, filepath)
    return None
# set constants
filename="imgs_url.csv"
filepath='/images'
#read lists of url using pandas dataframe
urls=pd.read_csv(filename)
# save images to the directory by iterating through the list
for i,url in enumerate(urls.values):
    url2jpg(i,url[0],filepath)
