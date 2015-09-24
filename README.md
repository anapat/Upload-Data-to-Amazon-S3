# Upload-Data-to-Amazon-S3
Upload Data form linux server to Amazon S3 or S3 Compatible Services

Usage
-------
```python
connection = S3Connection(
     host = 's3.amazonaws.com', # S3 Compatible Services
     is_secure = True,
     aws_access_key_id = 'access_key_id',  # Add your access key
     aws_secret_access_key = 'secret_access_key' # Add your secret key
)
bucket = connection.get_bucket('bucket_name', validate = True)
COMMON_PATH = '/common_folder/' # COMMON PATH OF YOUR S3 AND YOUR SERVER
```

License
-------

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.


 [1]: http://square.github.io/okhttp
 [2]: https://github.com/square/okhttp/wiki
 [3]: https://search.maven.org/remote_content?g=com.squareup.okhttp&a=okhttp&v=LATEST
 [4]: https://search.maven.org/remote_content?g=com.squareup.okhttp&a=mockwebserver&v=LATEST
 [snap]: https://oss.sonatype.org/content/repositories/snapshots/
