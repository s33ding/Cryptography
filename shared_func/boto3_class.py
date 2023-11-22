import os 
import boto3
import json
import sys

class Boto:
    def __init__(self, aws_cred_json_file_path=None):
        self.json_file_path = aws_cred_json_file_path 
        if self.json_file_path is None:
            self.json_file_path = os.environ["AWS_TEMP_CRED"]

        self.create_boto3_session()

    def get_input(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        else:
            return input("input:")

    def get_secret(self, secret_name):
            """
            Retrieves the value of the specified AWS Secrets Manager secret using the provided session object
            
            Args:
            - secret_name (str): the name of the AWS Secrets Manager secret to retrieve
            - session (boto3.Session): the session object for initializing the Secrets Manager client
            
            Returns:
            - dct (dict): a dictionary containing the values in the specified secret
            """
            # Initialize the Secrets Manager client using the session

            session = self.session
            client = session.client('secretsmanager')

            # Use Secrets Manager client object to get secret value
            get_secret_value_response = client.get_secret_value(SecretId=secret_name)

            # Extract the values from the secret
            dct = json.loads(get_secret_value_response['SecretString'])

            return dct

    def read_aws_credentials(self):
        """
        Reads the AWS credentials from a JSON file.

        Returns:
        - Tuple containing the AWS access key ID, secret access key, and session token.
        """

        with open(self.json_file_path, "r") as f:
            credentials = json.load(f)

        aws_key = credentials.get("id")
        aws_secret = credentials.get("secret")
        aws_token = credentials.get("token")
        return aws_key, aws_secret, aws_token

    def create_boto3_session(self):
        """
        Creates a new Boto3 session using AWS credentials stored in a JSON file.
        """

        aws_key, aws_secret, aws_token = self.read_aws_credentials()

        self.session = boto3.Session(
            region_name='us-east-1',
            aws_access_key_id=aws_key,
            aws_secret_access_key=aws_secret,
            aws_session_token=aws_token
            )
