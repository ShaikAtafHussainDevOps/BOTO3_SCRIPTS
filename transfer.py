import boto3

def copy_file(source_bucket, source_key, destination_bucket, destination_key):
    """Copy a file from one S3 bucket to another."""
    
    # Initialize the S3 client
    s3 = boto3.client("s3")

    # Construct the CopySource parameter
    copy_source = {'Bucket': source_bucket, 'Key': source_key}

    # Copy the object
    s3.copy_object(
        CopySource=copy_source,
        Bucket=destination_bucket,
        Key=destination_key,
        ACL='bucket-owner-full-control'  # Optional: Set ACL for the copied object
    )

def main():
    """Transfer all files from one S3 folder to another."""

    source_bucket = "azsource"
    source_prefix = "azsource/"
    destination_bucket = "azdestination"
    destination_prefix = "azdestinationFolder/"

    # Initialize the S3 client
    s3 = boto3.client("s3")

    # List objects in the source bucket with the specified prefix
    objects = s3.list_objects(Bucket=source_bucket, Prefix=source_prefix)

    # For each file, copy it to the destination bucket with the updated key
    for obj in objects.get("Contents", []):
        source_key = obj["Key"]
        # Remove the source_prefix and add destination_prefix to the key
        destination_key = destination_prefix + source_key[len(source_prefix):]
        copy_file(source_bucket, source_key, destination_bucket, destination_key)

if __name__ == "__main__":
    main()
