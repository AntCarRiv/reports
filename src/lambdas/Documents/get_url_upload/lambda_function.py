import uuid

import boto3
from tools_lambda.decorators import web_response
from tools_lambda.generic_tools import get_query_params


@web_response
def lambda_handler(event, context):
    """
    Create an preassigned url for upload any document in the s3
    :param event:
    :param context:
    :return:
    """
    query_params = get_query_params(event)
    if not query_params:
        return 400, 'bad request'
    extension = query_params.get('extension')
    path = query_params.get('path')
    s3_client = boto3.client('s3')
    response = s3_client.generate_presigned_post("dev-documents-891074642359",
                                                 f"{path}/{uuid.uuid4()}.{extension}",
                                                 ExpiresIn=300)
    return 200, response
