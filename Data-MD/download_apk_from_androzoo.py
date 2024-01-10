import os
from six.moves import urllib



def download_single_apk(url,save_path):

    apk_name=url.split("=")[-1]  #apk is named by sha256
    apk_save_path=os.path.join(save_path,apk_name+".apk")
    try:
        if os.path.exists(apk_save_path):
            print(apk_name,"Already exists, no need to download")
            return
        urllib.request.urlretrieve(url, apk_save_path)
    except Exception as r:
        print("error:",r)
        os.remove(apk_save_path)
    print('\nSuccessfully downloaded',apk_name)

def

="

for item in sha256_list:
    cur_url=url_base+item
    url_list.append(cur_url)
    save_path_list.append(save_path_base)