# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_milvusknowledgebase20260604 import models as main_models
from darabonba.model import DaraModel

class GetKnowledgeBasePreSignedUrlResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        data: main_models.GetKnowledgeBasePreSignedUrlResponseBodyData = None,
        http_status_code: int = None,
        success: bool = None,
    ):
        # The details of the permission verification failure.
        self.access_denied_detail = access_denied_detail
        # The business status code.
        self.code = code
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetKnowledgeBasePreSignedUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetKnowledgeBasePreSignedUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        expires_in: int = None,
        pre_signed_urls: List[str] = None,
    ):
        # The bucket name.
        self.bucket_name = bucket_name
        # The validity period of the pre-signed URL in seconds.
        self.expires_in = expires_in
        # The list of pre-signed PUT URLs. **The order corresponds one-to-one with the `Documents` in the request.**
        self.pre_signed_urls = pre_signed_urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.expires_in is not None:
            result['expiresIn'] = self.expires_in

        if self.pre_signed_urls is not None:
            result['preSignedUrls'] = self.pre_signed_urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('expiresIn') is not None:
            self.expires_in = m.get('expiresIn')

        if m.get('preSignedUrls') is not None:
            self.pre_signed_urls = m.get('preSignedUrls')

        return self

