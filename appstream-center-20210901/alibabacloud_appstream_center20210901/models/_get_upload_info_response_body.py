# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetUploadInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetUploadInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return code of the API. A value of 200 indicates success. If the call fails, the corresponding error code is returned.
        self.code = code
        # The file upload endpoint and temporary credentials.
        self.data = data
        # The message returned by the API.
        self.message = message
        # The ID of the request. It is used to locate and troubleshoot the request.
        self.request_id = request_id
        # Indicates whether the API call is successful. Valid values:
        # - true: The call is successful.
        # - false: The call fails.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetUploadInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetUploadInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket_name: str = None,
        expiration: str = None,
        file_path: str = None,
        oss_point: str = None,
        oss_point_internal: str = None,
        sts_token: str = None,
    ):
        # The AccessKey ID of the STS temporary access credential.
        self.access_key_id = access_key_id
        # The AccessKey Secret of the STS temporary access credential. It is used together with AccessKeyId and StsToken.
        self.access_key_secret = access_key_secret
        # The name of the destination OSS bucket for the upload.
        self.bucket_name = bucket_name
        # Not supported.
        self.expiration = expiration
        # The OSS directory prefix where files are allowed to be uploaded. The path of the uploaded object must be located under this directory.
        self.file_path = file_path
        # The OSS endpoint for public network access.
        self.oss_point = oss_point
        # The internal OSS endpoint.
        self.oss_point_internal = oss_point_internal
        # The STS temporary security token. It is used together with AccessKeyId and AccessKeySecret for file uploads.
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

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.oss_point is not None:
            result['OssPoint'] = self.oss_point

        if self.oss_point_internal is not None:
            result['OssPointInternal'] = self.oss_point_internal

        if self.sts_token is not None:
            result['StsToken'] = self.sts_token

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

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('OssPoint') is not None:
            self.oss_point = m.get('OssPoint')

        if m.get('OssPointInternal') is not None:
            self.oss_point_internal = m.get('OssPointInternal')

        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')

        return self

