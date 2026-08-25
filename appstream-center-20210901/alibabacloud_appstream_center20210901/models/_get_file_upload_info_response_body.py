# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetFileUploadInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFileUploadInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # Returns None.
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetFileUploadInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFileUploadInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        bucket_name: str = None,
        expiration: str = None,
        file_path: str = None,
        max_file_size: int = None,
        oss_point: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        sts_token: str = None,
    ):
        # The temporary AccessKey ID returned by Security Token Service (STS).
        self.access_key_id = access_key_id
        # The bucket name.
        self.bucket_name = bucket_name
        # The expiration time.
        self.expiration = expiration
        # The folder path.
        self.file_path = file_path
        # The maximum file size in bytes.
        self.max_file_size = max_file_size
        # The OSS endpoint.
        self.oss_point = oss_point
        # The PostObject policy (Base64-encoded).
        self.policy = policy
        # The request ID.
        self.request_id = request_id
        # The PostObject policy signature (HMAC-SHA1).
        self.signature = signature
        # The temporary token returned by STS.
        self.sts_token = sts_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.max_file_size is not None:
            result['MaxFileSize'] = self.max_file_size

        if self.oss_point is not None:
            result['OssPoint'] = self.oss_point

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.sts_token is not None:
            result['StsToken'] = self.sts_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('MaxFileSize') is not None:
            self.max_file_size = m.get('MaxFileSize')

        if m.get('OssPoint') is not None:
            self.oss_point = m.get('OssPoint')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')

        return self

