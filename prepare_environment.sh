awslocal s3 mb s3://tutorial --region us-east-1
awslocal s3api put-bucket-acl --bucket tutorial --acl public-read
