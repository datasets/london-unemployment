import datetime
from dataflows import Flow,dump_to_path, printer, ResourceWrapper, PackageWrapper
import pandas as pd
import numpy as np


def get_data():
    unemployment = pd.read_excel('https://data.london.gov.uk/download/unemployment-rate-region/8a29ec0c-9de3-4777-832f-49ef8c2b4d14/unemployment-region.xls',sheet_name=1);
    unemploymentArray = np.array(unemployment) # getting table
    unemployment_london_real_num = unemploymentArray[1, :] # getting unemployment in thousands in London
    unemployment_london_rate = unemploymentArray[17, :] # getting unemployment rate in London

    unemployment_dates = np.array(unemployment.columns.values) # getting dates of recorded unemployment

    for row in range(1,unemployment_dates.__len__()):
       #print (unemployment_dates[row])
       yield dict(
           date = datetime.datetime.date(unemployment_dates[row]),
           unemployment_real_numbers = unemployment_london_real_num[row],
           unemployment_rate = unemployment_london_rate[row]
       )


def change_path(package: PackageWrapper):
    # Add 'name' in descriptor:
    package.pkg.descriptor['name'] = 'unemployment-rate'
    package.pkg.descriptor['title'] = 'London unemployment rate'
    # Change path and name for the resource:
    package.pkg.descriptor['resources'][0]['path'] = 'data/unemployment-rate.csv'
    package.pkg.descriptor['resources'][0]['name'] = 'unemployment-rate'

    yield package.pkg
    res_iter = iter(package)
    first: ResourceWrapper = next(res_iter)
    yield first.it
    yield from package


Flow(
    get_data(),
    change_path,
    dump_to_path('data'),
    printer()
).process()