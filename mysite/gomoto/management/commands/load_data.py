import csv, sys, os

sys.path.append('/Users/shanecheek/Desktop/PDX_Code/my_repos/gomoto')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from mysite.gomoto.models import Bikes


#Full path and name to your csv file csv

filepathname="/Users/shanecheek/Desktop/PDX_Code/my_repos/gomoto/mysite/dirt_bike_data.csv"

# Full path to your django project directory

your_djangoproject_home="/home/mitch/projects/wantbox.com/wantbox/"

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
for row in dataReader:
    if row[0] != 'ZIPCODE': # Ignore the header row, import everything else
        zipcode = ZipCode()
        zipcode.zipcode = row[0]
        zipcode.city = row[1]
        zipcode.statecode = row[2]
        zipcode.statename = row[3]
        zipcode.save()