# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateKnowledgeObjectUploadResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateKnowledgeObjectUploadResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business error code, which is used to determine the error type when the request fails.
        self.code = code
        # The business data returned when the request is successful.
        self.data = data
        # The error message returned when the request fails.
        self.message = message
        # The unique identifier of the request, which can be used to troubleshoot issues.
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
            temp_model = main_models.CreateKnowledgeObjectUploadResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateKnowledgeObjectUploadResponseBodyData(DaraModel):
    def __init__(
        self,
        expires_at: int = None,
        required_headers: Dict[str, str] = None,
        upload_id: str = None,
        upload_url: str = None,
    ):
        # The expiration time of the UploadUrl, represented as a UNIX timestamp in milliseconds. The maximum validity period is 30 minutes, subject to the upper limit of the OSS signature configuration and the remaining time of the session. This field prevails.
        self.expires_at = expires_at
        # The HTTP headers that must be included in the direct upload request. The key is the actual header name, and the value is the header value.
        self.required_headers = required_headers
        # The identifier of the upload session to be consumed by document creation, model update, or model import tasks. This is not a KnowledgeObjectId or TaskId.
        self.upload_id = upload_id
        # The temporary direct upload URL.
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.required_headers is not None:
            result['RequiredHeaders'] = self.required_headers

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('RequiredHeaders') is not None:
            self.required_headers = m.get('RequiredHeaders')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')

        return self

