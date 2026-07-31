# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UploadSemanticFileResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UploadSemanticFileResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The attachment upload slot information. PUT the file to Data.UploadUrl before Data.ExpiresAt, and then use Data.FileId to create a single-file semantic job.
        self.data = data
        # The request ID. You can use this ID to locate logs and troubleshoot issues.
        self.request_id = request_id
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.UploadSemanticFileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UploadSemanticFileResponseBodyData(DaraModel):
    def __init__(
        self,
        expires_at: int = None,
        file_id: str = None,
        upload_url: str = None,
    ):
        # The expiration time of UploadUrl, expressed as a UNIX timestamp in milliseconds. After this time, call UploadSemanticFile again to request a new URL.
        self.expires_at = expires_at
        # The unique identifier of the attachment. After the PUT upload to UploadUrl is complete, pass this value to the ReferenceFileIds parameter of CreateSemanticJob.
        self.file_id = file_id
        # The temporary OSS PUT upload URL. The URL is valid for 30 minutes and can only be used to upload the specified object. Use the ContentType specified in the request when you perform the PUT request. Do not log or distribute the full URL.
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

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')

        return self

