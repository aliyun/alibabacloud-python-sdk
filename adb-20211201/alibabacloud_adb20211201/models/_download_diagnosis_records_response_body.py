# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadDiagnosisRecordsResponseBody(DaraModel):
    def __init__(
        self,
        download_id: int = None,
        request_id: str = None,
    ):
        # The download ID.
        self.download_id = download_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_id is not None:
            result['DownloadId'] = self.download_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadId') is not None:
            self.download_id = m.get('DownloadId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

