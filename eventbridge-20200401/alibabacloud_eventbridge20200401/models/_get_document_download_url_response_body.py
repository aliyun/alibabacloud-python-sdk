# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class GetDocumentDownloadUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDocumentDownloadUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of Success indicates that the call was successful. If the call fails, a specific error code is returned.
        self.code = code
        # The document download URL information.
        self.data = data
        # The response message. If the call is successful, the value is Operation success. If the call fails, a specific error description is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. A value of true indicates that the call was successful.
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
            temp_model = main_models.GetDocumentDownloadUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDocumentDownloadUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        expire_at: str = None,
    ):
        # The short-lived presigned GET URL. Clients use this URL to download the original file.
        self.download_url = download_url
        # The expiration time of the presigned download URL in ISO 8601 format and UTC.
        self.expire_at = expire_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')

        return self

