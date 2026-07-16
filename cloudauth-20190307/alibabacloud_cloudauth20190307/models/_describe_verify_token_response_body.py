# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifyTokenResponseBody(DaraModel):
    def __init__(
        self,
        oss_upload_token: main_models.DescribeVerifyTokenResponseBodyOssUploadToken = None,
        request_id: str = None,
        verify_page_url: str = None,
        verify_token: str = None,
    ):
        # The OSS upload token information.
        self.oss_upload_token = oss_upload_token
        # The ID of this request.
        self.request_id = request_id
        # The entry URL for the legacy H5 authentication scheme. This scheme has been discontinued and no longer accepts new integrations. If you need H5 authentication, use the [PC or mobile H5 web integration scheme](https://help.aliyun.com/document_detail/173779.html) of financial-grade ID Verification.
        self.verify_page_url = verify_page_url
        # The token for this authentication, which is used to connect the various operations in the authentication request. The token is valid for 30 minutes.
        self.verify_token = verify_token

    def validate(self):
        if self.oss_upload_token:
            self.oss_upload_token.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_upload_token is not None:
            result['OssUploadToken'] = self.oss_upload_token.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.verify_page_url is not None:
            result['VerifyPageUrl'] = self.verify_page_url

        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssUploadToken') is not None:
            temp_model = main_models.DescribeVerifyTokenResponseBodyOssUploadToken()
            self.oss_upload_token = temp_model.from_map(m.get('OssUploadToken'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VerifyPageUrl') is not None:
            self.verify_page_url = m.get('VerifyPageUrl')

        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')

        return self

class DescribeVerifyTokenResponseBodyOssUploadToken(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        end_point: str = None,
        expired: int = None,
        key: str = None,
        path: str = None,
        secret: str = None,
        token: str = None,
    ):
        # The OSS bucket for file storage.
        self.bucket = bucket
        # The endpoint.
        self.end_point = end_point
        # The expiration time. The value is in UNIX timestamp format. Unit: milliseconds.
        self.expired = expired
        # The key required for file upload.
        self.key = key
        # The file storage path.
        self.path = path
        # The secret required for file upload.
        self.secret = secret
        # The token required for file upload.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.end_point is not None:
            result['EndPoint'] = self.end_point

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.key is not None:
            result['Key'] = self.key

        if self.path is not None:
            result['Path'] = self.path

        if self.secret is not None:
            result['Secret'] = self.secret

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Secret') is not None:
            self.secret = m.get('Secret')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

