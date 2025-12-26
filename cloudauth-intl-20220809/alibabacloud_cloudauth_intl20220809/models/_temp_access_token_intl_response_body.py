# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class TempAccessTokenIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.TempAccessTokenIntlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Return code
        self.code = code
        # Return result.
        self.data = data
        # Return message.
        self.message = message
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.TempAccessTokenIntlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class TempAccessTokenIntlResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket_name: str = None,
        file_name_prefix: str = None,
        oss_end_point: str = None,
        security_token: str = None,
    ):
        # AccessKeyId for temporary file upload credentials.
        self.access_key_id = access_key_id
        # Temporary authorization secret.
        self.access_key_secret = access_key_secret
        # Bucket name.
        self.bucket_name = bucket_name
        # File prefix.
        self.file_name_prefix = file_name_prefix
        # OSS endpoint.
        self.oss_end_point = oss_end_point
        # Security token for temporary file upload credentials.
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.file_name_prefix is not None:
            result['FileNamePrefix'] = self.file_name_prefix

        if self.oss_end_point is not None:
            result['OssEndPoint'] = self.oss_end_point

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('FileNamePrefix') is not None:
            self.file_name_prefix = m.get('FileNamePrefix')

        if m.get('OssEndPoint') is not None:
            self.oss_end_point = m.get('OssEndPoint')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

