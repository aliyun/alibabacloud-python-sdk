# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetAgentCodePackageUploadUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAgentCodePackageUploadUrlResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetAgentCodePackageUploadUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetAgentCodePackageUploadUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        expires_at: str = None,
        headers: Dict[str, str] = None,
        max_size: int = None,
        source_uri: str = None,
        upload_method: str = None,
        upload_url: str = None,
    ):
        # The expiration time of the upload URL.
        self.expires_at = expires_at
        # The HTTP headers that must be included in the direct upload request.
        self.headers = headers
        # The maximum compressed size of the code package.
        self.max_size = max_size
        # The temporary Object Storage Service (OSS) URI of the code package.
        self.source_uri = source_uri
        # The HTTP method for direct upload.
        self.upload_method = upload_method
        # The time-limited presigned upload URL.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.headers is not None:
            result['headers'] = self.headers

        if self.max_size is not None:
            result['maxSize'] = self.max_size

        if self.source_uri is not None:
            result['sourceUri'] = self.source_uri

        if self.upload_method is not None:
            result['uploadMethod'] = self.upload_method

        if self.upload_url is not None:
            result['uploadUrl'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('maxSize') is not None:
            self.max_size = m.get('maxSize')

        if m.get('sourceUri') is not None:
            self.source_uri = m.get('sourceUri')

        if m.get('uploadMethod') is not None:
            self.upload_method = m.get('uploadMethod')

        if m.get('uploadUrl') is not None:
            self.upload_url = m.get('uploadUrl')

        return self

