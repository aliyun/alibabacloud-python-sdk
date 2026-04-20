# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailianvoicebot20250101 import models as main_models
from darabonba.model import DaraModel

class GenerateFileUploadParamsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GenerateFileUploadParamsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GenerateFileUploadParamsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GenerateFileUploadParamsResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket: str = None,
        expiration_time: int = None,
        file_key: str = None,
        host: str = None,
        policy: str = None,
        region: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.bucket = bucket
        self.expiration_time = expiration_time
        self.file_key = file_key
        self.host = host
        self.policy = policy
        self.region = region
        self.security_token = security_token
        self.signature = signature

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

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.host is not None:
            result['Host'] = self.host

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.region is not None:
            result['Region'] = self.region

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.signature is not None:
            result['Signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

