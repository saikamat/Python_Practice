"""1. Grab URL from a cell in a spreadsheet
2. download image from that URL
3. do it for all images in the spreadsheet
"""
import urllib.request
import subprocess
import csv
import operator
from csv import writer
# import pandas as pd
# filename = "Vrbo_highscore_samples"
filename = "test_csv"
Good_Count = 2488
Bad_Count = 2741
# newfilename="new_file_url"

# def sort_by_scores(filename):
#     # df = pd.read_csv("{0}.csv".format(filename))
#     df = pd.read_csv('test_url.csv')
#     print(df.head())
#     df = df.sort_values('aesthetic_score')
#     df.to_csv("{0}.csv".format(newfilename), index=False)
    
# with open('test_url.csv') as fp:
#     crdr = csv.reader(fp)
#     # set key1 and key2 to column numbers of keys
#     filedata = sorted(crdr, key=lambda row: (row['aesthetic_score']))
def download_from_csv(filename):
    with open("{0}.csv".format(filename), 'r') as csvfile:
        i = 0
        for line in csvfile:
            splitted_line = line.split(';')
        # check whether we have image URL
            if splitted_line[0] != '' and splitted_line[0] != "\n" and splitted_line[0] != 'url':
                try:
                    urllib.request.urlretrieve(splitted_line[0], filename + "_" + str(i) + ".jpg")
                except:
                    print('**** 404 Error at :', splitted_line[0])
                else:
                    print ("Image saved for {0}".format(splitted_line[0]))

                finally:
                    i+=1
            else:
                print ("No result for {0}".format(splitted_line[0]))


def copy_to_dir(filename):
    # os.system("mkdir low_scores")
    # os.system("ls | sort -R | tail -$N2 | while read file; do mv $file ../old2/use_case_1/val ; done")
    subprocess.call(["mkdir", filename])
    subprocess.call(["cp *.jpg ", filename])


def make_datasets(filename):
    subprocess.call(["mkdir smartly/negatives"])
    subprocess.call(["cd smartly/", filename])
    subprocess.call(["ls | sort -R | tail ",(0.35*Bad_Count)," | while read file; do mv $file ../negatives/ ; done"])

# sort_by_scores(filename)
download_from_csv(filename)
# download_from_csv2(filename)
# make_datasets(filename)
# copy_to_dir(filename)
