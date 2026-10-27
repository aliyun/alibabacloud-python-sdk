# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetAgentCodePackageDownloadUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAgentCodePackageDownloadUrlResponseBodyData = None,
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
            temp_model = main_models.GetAgentCodePackageDownloadUrlResponseBodyData()
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

class GetAgentCodePackageDownloadUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        crc_64: str = None,
        download_url: str = None,
        etag: str = None,
        expires_at: str = None,
        file_name: str = None,
        file_size: int = None,
        format: str = None,
        resource_version_id: str = None,
    ):
        # The CRC64 value of the code package object.
        self.crc_64 = crc_64
        # The time-limited, read-only download URL for the code package.
        self.download_url = download_url
        # The ETag of the code package object.
        self.etag = etag
        # The expiration time of the download URL.
        self.expires_at = expires_at
        # The original file name of the code package.
        self.file_name = file_name
        # The compressed size of the code package.
        self.file_size = file_size
        # The format of the code package.
        self.format = format
        # The resource version ID corresponding to the currently saved configuration.
        self.resource_version_id = resource_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crc_64 is not None:
            result['crc64'] = self.crc_64

        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.etag is not None:
            result['etag'] = self.etag

        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.format is not None:
            result['format'] = self.format

        if self.resource_version_id is not None:
            result['resourceVersionId'] = self.resource_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crc64') is not None:
            self.crc_64 = m.get('crc64')

        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('etag') is not None:
            self.etag = m.get('etag')

        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('resourceVersionId') is not None:
            self.resource_version_id = m.get('resourceVersionId')

        return self

