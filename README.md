# ProgImage

A image hosting micro-service that allows uses Amazon S3 and SQS to store and process images at scale.


## Features

* Bulk image upload via either Base64 or remote url.
* Synchronous image format conversion using Celery (SQS)
* Amazon S3 Integration
* Browsable API using Django Rest Framework
 
## Demo

A hosted instance of ProgImage can be found at:

http://3.248.226.49:5000/

