import json
import logging
import os

import boto3

LOGGER = logging.getLogger()
ENVIRONMENT = os.environ.get('ENVIRONMENT')


def generate_presigned_post(bucket, key, expiration=3600):
    """
    Create all resource for upload any file to s3
    :param bucket: Bucket name
    :param key: File name
    :param expiration: time out for url
    :return:
    """
    s3 = boto3.client('s3')
    try:
        response = s3.generate_presigned_post(Bucket=bucket,
                                              Key=key,
                                              Field=None,
                                              Conditions=None,
                                              ExpiresIn=expiration)
    except Exception as e:
        LOGGER.error(e)
        return None
    return response


def get_ssm_parameter(parameter_name):
    """
    Search an parameter on the system parameter store
    :param parameter_name:
    :return:
    """
    ssm = boto3.client('ssm')
    try:
        parameter_name = f'{parameter_name}-{ENVIRONMENT}'
        response = ssm.get_parameter(Name=parameter_name)['Parameter']['Value']
    except Exception as e:
        LOGGER.error(e)
        return {}
    else:
        parameters = json.loads(response)
        return parameters
