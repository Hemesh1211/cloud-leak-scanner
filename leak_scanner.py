
import argparse
import boto3
from botocore import UNSIGNED
from botocore.config import Config
from botocore.exceptions import (
    ClientError,
    BotoCoreError,
    EndpointConnectionError,
)


def check_bucket_public(bucket_name):
    print(f"\n[*] Checking bucket: {bucket_name}")

    # Use unsigned requests to test anonymous access.
    s3 = boto3.client(
        "s3",
        config=Config(signature_version=UNSIGNED),
    )

    try:
        # Check whether anonymous users can list objects.
        response = s3.list_objects_v2(
            Bucket=bucket_name,
            MaxKeys=1,
        )

        print(
            "[!] Anonymous object listing is permitted."
        )

        if response.get("Contents"):
            print(
                "[!] At least one object is listed "
                "anonymously."
            )
        else:
            print(
                "[i] Listing succeeded, but no objects "
                "were returned."
            )

        return True

    except ClientError as error:
        response = error.response
        status = response.get(
            "ResponseMetadata", {}
        ).get("HTTPStatusCode")
        code = response.get(
            "Error", {}
        ).get("Code", "Unknown")

        if status == 403 or code in (
            "AccessDenied",
            "AllAccessDisabled",
        ):
            print("[OK] Anonymous listing denied.")

        elif status == 404 or code in (
            "NoSuchBucket",
            "NotFound",
        ):
            print("[-] Bucket not found.")

        else:
            print(
                f"[?] AWS returned {code} "
                f"(HTTP {status})."
            )

        return False

    except EndpointConnectionError as error:
        print(f"[-] Endpoint connection error: {error}")
        return False

    except BotoCoreError as error:
        print(f"[-] AWS SDK error: {error}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Check anonymous S3 object-listing access "
            "for authorized buckets."
        )
    )

    parser.add_argument(
        "buckets",
        nargs="+",
        help="S3 bucket names you own or are authorized to test",
    )

    args = parser.parse_args()

    print("Cloud Storage Access Check")
    print("-" * 40)

    for bucket_name in args.buckets:
        check_bucket_public(bucket_name)

    print("\n[+] Check complete.")
    print(
        "Note: this checks anonymous listing access only. "
        "It does not establish whether every object is public."
    )


if __name__ == "__main__":
    main()
