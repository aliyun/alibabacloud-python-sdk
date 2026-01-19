# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SdkGenerateByAppResponseBody(DaraModel):
    def __init__(
        self,
        download_link: str = None,
        request_id: str = None,
    ):
        self.download_link = download_link
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_link is not None:
            result['DownloadLink'] = self.download_link

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadLink') is not None:
            self.download_link = m.get('DownloadLink')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

