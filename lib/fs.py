import sys, os, urllib3

def delete_file(file_path):
    return os.remove(file_path)


def create_directories(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_file(file_path, contents, mode):
    directory = "/".join(file_path.split("/")[:-1])
    create_directories(directory)
    with open(file_path, mode) as f:
        f.write(contents)


def download_file(url, file_path):
    directory = "/".join(file_path.split("/")[:-1])
    create_directories(directory)
    http = urllib3.PoolManager()
    r = http.request('GET', url, preload_content=False)
    with open(file_path, 'wb') as f:
        while True:
            data = r.read(16)
            if not data:
                break
            f.write(data)
    r.release_conn()
