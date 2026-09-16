# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class GetLumaDocumentDownloadUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetLumaDocumentDownloadUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of Success indicates that the call succeeds. If the call fails, a specific error code is returned.
        self.code = code
        # The pre-signed download URL information for the original document.
        self.data = data
        # The message returned by the operation. The value is Operation success if the call succeeds, or a specific error description if the call fails.
        self.message = message
        # The unique identifier of the request. Use this ID for troubleshooting or when submitting a ticket.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates that the call succeeds.
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
            temp_model = main_models.GetLumaDocumentDownloadUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetLumaDocumentDownloadUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        expire_at: str = None,
    ):
        # The pre-signed download URL for the original document. The URL is valid for a limited period of time.
        self.download_url = download_url
        # The expiration time of the download URL in UTC.
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

