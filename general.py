import os



# Each website you crawl is a separate project (folder)


# create a new folder
from typing import Set


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating Project ' + directory)
        os.makedirs(directory)

# we should have weo list, one is waiting list:
# for all url are waiting to crawl
# can another list is stored what we have crawled.
#
# create queue and crawled files

def create_data_file(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

create_project_dir('thenewboston')
create_data_file('thenewboston', 'http://thenewboston.com/')

# add data onto an existing file
def appen_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        # pass = do nothing
        pass

# set can only have unique elements

# read a file and convert each line to set items
def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))

    return results

# interate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        appen_to_file(file, link)




