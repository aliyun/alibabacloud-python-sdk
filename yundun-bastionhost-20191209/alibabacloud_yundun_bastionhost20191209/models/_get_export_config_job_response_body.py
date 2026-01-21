# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetExportConfigJobResponseBody(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        expire_time: int = None,
        job_id: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.download_url = download_url
        self.expire_time = expire_time
        self.job_id = job_id
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

