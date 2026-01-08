# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetChatappUploadAuthorizationResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetChatappUploadAuthorizationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Access denied for detailed information.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetChatappUploadAuthorizationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetChatappUploadAuthorizationResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket_name: str = None,
        dir: str = None,
        end_point: str = None,
        expire: int = None,
        security_token: str = None,
    ):
        # The AccessKey ID that is used to authorize a user to upload a file to Object Storage Service (OSS).
        self.access_key_id = access_key_id
        # The AccessKey secret that is used to authorize a user to upload a file to OSS.
        self.access_key_secret = access_key_secret
        # The name of the bucket to which a file is uploaded in OSS.
        self.bucket_name = bucket_name
        # The directory to which the file is uploaded in Object Storage Service (OSS).
        self.dir = dir
        # The address of the OSS server to which a file is uploaded.
        self.end_point = end_point
        # The timeout period.
        self.expire = expire
        # The security token.
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

        if self.dir is not None:
            result['Dir'] = self.dir

        if self.end_point is not None:
            result['EndPoint'] = self.end_point

        if self.expire is not None:
            result['Expire'] = self.expire

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

        if m.get('Dir') is not None:
            self.dir = m.get('Dir')

        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

