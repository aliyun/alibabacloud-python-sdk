# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeComfyProductionDownloadUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        download_url: str = None,
        expired_time: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The download link for the production. Use an Alibaba Cloud Object Storage Service (OSS) SDK to download the file.
        self.download_url = download_url
        # The download link\\"s expiration time.
        self.expired_time = expired_time
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

