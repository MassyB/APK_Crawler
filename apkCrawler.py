import subprocess
import os
import re


#getting the list of files .txt ones
#opening each of them 
#create a dir for each one 
#moving to the dir
#download the app

GOOGLE_LOGIN = None
GOOGLE_PASSWORD = None
ANDROID_ID = None

def get_input_files()->list:
    """ return a list of text files containing the list of apk IDs.
        those files begin with 'topselling_free' and end with '.txt'"""
    input_file_regex = re.compile(r'topselling_free_\w+\.txt')
    list_file_names = os.listdir(os.getcwd())
    return [ os.path.join(os.getcwd(),file_name) for file_name in list_file_names if input_file_regex.search(file_name) != None]




input_files = get_input_files()
print("inpute files: \n"+ str(input_files))

if not all([GOOGLE_LOGIN, GOOGLE_PASSWORD, ANDROID_ID]):
   print("you must initialize : GOOGLE_LOGIN, GOOGLE_PASSWORD and ANDROID_ID")
   exit()

os.environ['GOOGLE_LOGIN'] = GOOGLE_LOGIN
os.environ['GOOGLE_PASSWORD'] = GOOGLE_PASSWORD
os.environ['ANDROID_ID'] = ANDROID_ID

print("env variables set")

for file_name in input_files:
    if not os.path.exists(file_name[:-4]):
        os.makedirs(file_name[:-4])
    else:
        print(file_name[:-4]+" already exists")

    os.chdir(file_name[:-4])

    with open(file_name, 'r') as file:

        apk_ids = [line.strip() for line in file.readlines()]
        for apk_id in apk_ids:
           if not os.path.exists(apk_id+".apk"):
              try:
                  print("downloading ... "+apk_id)
                  with open(apk_id+'.apk','w') as apk_file:
                      subprocess.run(['gp-download',apk_id],stdout=apk_file)
                  print(apk_id+" ... downloaded")
              except Exception:
                  print("an error occurred while downloading .... removing the apk")
                  os.remove(apk_id+'.apk')
           else:
              print(apk_id+" already exists")
    
    print(file_name[:-4]+ " ... all downloaded")
    os.chdir('../')
