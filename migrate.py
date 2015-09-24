# -*- coding: utf-8 -*-
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key

connection = S3Connection(
     host = 's3.amazonaws.com', # S3 Compatible Services
     is_secure = True,
     aws_access_key_id = 'access_key_id',  # Add your access key
     aws_secret_access_key = 'secret_access_key' # Add your secret key
)

bucket = connection.get_bucket('bucket_name', validate = True)
COMMON_PATH = '/common_folder/' # COMMON PATH OF YOUR S3 AND YOUR SERVER
BASE = os.path.dirname(os.path.abspath(__file__))


def upload(path, filename):
    path_file = '%s/%s'%(BASE, filename)
    if COMMON_PATH in path_file:
        path_upload = ROOT_PATH + path_file.rsplit(COMMON_PATH, 1)[1]
        print '  Upload to : %s' % path_upload
        key = Key(bucket, path_upload)
        key.set_contents_from_filename(path_file)
    else:
        print '  Upload path not found.'


if __name__ == '__main__':
    count = 1
    for path, subdirs, files in os.walk('.'):
        for name in files:
            if name not in os.path.basename(__file__):
                print '> Execute File (%s/%s) : %s '% (count, len(files)-1, os.path.join(path, name)[1:])
                upload(path, name)
                count += 1
