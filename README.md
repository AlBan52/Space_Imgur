# Space Imgur

This project would help you to automize image posting into your Imgur account. The project consist of three independent scripts: 
```space_x_fetch.py```, ```hubble_fetch.py``` and ```imgur_image_post.py```.
The ```space_x_fetch.py```and```hubble_fetch.py``` download the magnificent images from "Space-X" and "Hubble" official internet resources. The ```imgur_image_post.py``` script edits downloaded pictures, changing the names, extensions, and resizing the pictures to facilitate the uploading process for Imgur.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

For the start using this project, you might download the pictures with the ```space_x_fetch.py``` and ```hubble_fetch.py```. Before using this scripts, you need to change directory in the variable ```file_path```, like in the example below:
```python
...

if __name__ == '__main__':

    file_path = 'd:/CODING/DEVMAN/Space_Imgur/images'
    os.makedirs(file_path, exist_ok=True)
...
```
If you have already downloaded pictures or used ```space_x_fetch.py```and```hubble_fetch.py``` scripts, you could apply 
```imgur_image_post.py``` for uploading pictures to Imgur account.
Befor start the ```imgur_image_post.py``` script you must register an application in accordance with API Imgur doc's by the next
link: [apidocs.imgur.com](https://apidocs.imgur.com/)
As result of application register you get the ```Client ID```, looks like this string: ```d25290700cbb95d``` and ```Client secret```,
looks like this: ```421b43ea43754f2ccfcfb13c05e78a3440ffd2fb```
After that, you have to get tokens on API Imgur site. Tokens have names ```ACCESS_TOKEN``` and ```REFRESH_TOKEN```
It's look like this string: ```17c09e20ad155405123ac1977542fecf00231da7```.
For script work correctly, you must create ```.env``` file in the script directory.
This file have to consider the next data like in the example below:
```
CLIENT_ID=d25290700cbb95d
CLIENT_SECRET=421b43ea43754f2ccfcfb13c05e78a3440ffd2fb
ACCESS_TOKEN=59c544160ddd698d5d7e78370633d39964ac2a5d
REFRESH_TOKEN=71b0620c1d58daeb1d3a731f6bac815e6ce8da28
```
For script running you have to start the command line and change directory to the code containing.
The next step is start the script for this template:
```
[full_dir_path] python imgur_image_post.py
```
For example: 
```
d:\CODING\DEVMAN\Space Imgur>python imgur_image_post.py
```
The scripts described above run the same

### Output results

When you run the ```space_x_fetch.py``` script, you'll see in terminal messages like this:
```
d:\CODING\DEVMAN\Space Imgur>python space_x_fetch.py
Downloading spase-X images: spacex_0.jpg
Downloading spase-X images: spacex_1.jpg
Downloading spase-X images: spacex_2.jpg
Downloading spase-X images is done
```
When you run the ```hubble_fetch.py``` script, you'll see in terminal messages like this:
```
d:\CODING\DEVMAN\Space Imgur>python hubble_fetch.py
Downloading hubbles images start...
Downloading image: 3241.jpg
Downloading image: 3242.png
Downloading image: 3243.tif
Downloading hubbles images is done
```
The ```imgur_image_post.py``` script work start with authorization process. If you register your application above and got the tokens, you have to setup this data into ```.env``` file. In this case the authorization process begin without any messages to
terminal. In another case you'll see the authorization messages in console like example below:
```
Go to the following URL: https://api.imgur.com/oauth2/authorize?client_id=24uf2b4b&response_type=pin
Enter pin code: 02071889cc
Authentication successful! Here are the details:
   Access token:  13f0n23fn230fn2309fn023fn0vn42184e94d091
   Refresh token: 1mc3894c98q4q9mc8m49ghcwogho34chmg348cgm
```
After authorization process the editing images will start. You'll see:
```
Editing images: 0.jpg
Editing images: 1.jpg
Editing images: 2.jpg
Editing images is done
```
The final process is uploading pictures. You'll see:
```
Uploading image...
Upload: 0
Upload: 1
Upload: 2
Uploading images is done
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).