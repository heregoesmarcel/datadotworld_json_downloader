import sys, json, re
import datadotworld as dw
from urllib.request import urlopen

def writeToFile(output_directory, data): 
    if not output_directory.endswith('/'):
        output_directory += '/'
    filename = output_directory + data['id'] + '.json'
    print('Writing ', filename, '...')
    #json = json.dumps(data)
    #print(json)
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

help = "Usage:\nclient.py <output directory> <dataset locations> -> Downloads a dataset from data.world to <output directory>\nclient.py get-all <output directory> <username>  -> Downloads all existing datasets in a user libary to <output directory>\nclient.py get-bookmarked <output directory>      -> Downloads all bookmarked datasets to <output directory>"

if len(sys.argv) < 2 or sys.argv[1] == 'help' or sys.argv[1] == '--help':
    print(help)
    exit()

client = dw.api_client()

if sys.argv[1] == 'get-all':
    output_dir = sys.argv[2]
    user_url = "https://data.world/" + sys.argv[3] + "/"
    print("Reading ", user_url)
    user_page = urlopen(user_url)
    page_data = user_page.read()
    #print(page_data)
    print('Placeholder function.')
    #datasets_it = re.findall(r'<a class="dw-dataset-name DatasetCard__name___2U4-H" target="" href="/agriculture/(.*?)">', str(page_data), re.DOTALL)

elif sys.argv[1] == 'get-bookmarked':
    output_dir = sys.argv[2]
    datasets = client.fetch_liked_datasets()
    print(datasets['count'], 'retrieved datasets.')
    for i in range(datasets['count']):
        writeToFile(output_dir, datasets['records'][i])
        #print(datasets['records'][i])

else:
    output_dir = sys.argv[1]
    dataset_dirs = [None] * (len(sys.argv) - 2)
    #print('The following datasets: ', dataset_dirs)
    #print('Dataset location:', sys.argv[1], ', downloading to: ', sys.argv[2])
    for i in range(len(dataset_dirs)):
        dataset = client.get_dataset(dataset_dirs[i])
        #print(output_dir)
        writeToFile(output_dir, dataset)

print('Done.')
