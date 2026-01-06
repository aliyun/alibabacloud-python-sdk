# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTempFileUploadUrlResponseBody(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        code: str = None,
        endpoint: str = None,
        expire_time: int = None,
        message: str = None,
        oss_access_key_id: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        success: bool = None,
        temp_file_key: str = None,
    ):
        # The name of the OSS bucket to which the file is uploaded.
        self.bucket_name = bucket_name
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The endpoint that is used to upload the file to OSS.
        self.endpoint = endpoint
        # The expiration time of the signature that is used to upload the file to OSS. This value is a UNIX timestamp. Unit: seconds.
        self.expire_time = expire_time
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The AccessKey ID that is used to upload the file to OSS.
        self.oss_access_key_id = oss_access_key_id
        # The policy that is used to upload the file to OSS.
        self.policy = policy
        # The ID of the request.
        self.request_id = request_id
        # The signature that is used to upload the file to OSS.
        self.signature = signature
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The key that is used to upload the file to OSS.
        self.temp_file_key = temp_file_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.code is not None:
            result['Code'] = self.code

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.message is not None:
            result['Message'] = self.message

        if self.oss_access_key_id is not None:
            result['OssAccessKeyId'] = self.oss_access_key_id

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.success is not None:
            result['Success'] = self.success

        if self.temp_file_key is not None:
            result['TempFileKey'] = self.temp_file_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OssAccessKeyId') is not None:
            self.oss_access_key_id = m.get('OssAccessKeyId')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TempFileKey') is not None:
            self.temp_file_key = m.get('TempFileKey')

        return self

