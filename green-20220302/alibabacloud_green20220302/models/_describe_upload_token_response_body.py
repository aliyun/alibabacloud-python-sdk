# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class DescribeUploadTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeUploadTokenResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        # The returned HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
        self.msg = msg
        # The request ID.
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

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeUploadTokenResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUploadTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket_name: str = None,
        expiration: int = None,
        file_name_prefix: str = None,
        oss_internal_end_point: str = None,
        oss_internet_end_point: str = None,
        security_token: str = None,
    ):
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The AccessKey secret.
        self.access_key_secret = access_key_secret
        # The bucket name.
        self.bucket_name = bucket_name
        # The time when the file sharing link expires.
        self.expiration = expiration
        # The file prefix.
        self.file_name_prefix = file_name_prefix
        # the oss intranet point.
        self.oss_internal_end_point = oss_internal_end_point
        # the oss internet point.
        self.oss_internet_end_point = oss_internet_end_point
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

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.file_name_prefix is not None:
            result['FileNamePrefix'] = self.file_name_prefix

        if self.oss_internal_end_point is not None:
            result['OssInternalEndPoint'] = self.oss_internal_end_point

        if self.oss_internet_end_point is not None:
            result['OssInternetEndPoint'] = self.oss_internet_end_point

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

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('FileNamePrefix') is not None:
            self.file_name_prefix = m.get('FileNamePrefix')

        if m.get('OssInternalEndPoint') is not None:
            self.oss_internal_end_point = m.get('OssInternalEndPoint')

        if m.get('OssInternetEndPoint') is not None:
            self.oss_internet_end_point = m.get('OssInternetEndPoint')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

