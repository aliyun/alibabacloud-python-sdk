# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetSnapshotUrlsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_urls: List[str] = None,
        total: int = None,
        web_vtturl: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of snapshot URLs.
        self.snapshot_urls = snapshot_urls
        # The total number of snapshots.
        self.total = total
        # The URL of the WebVTT file.
        self.web_vtturl = web_vtturl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_urls is not None:
            result['SnapshotUrls'] = self.snapshot_urls

        if self.total is not None:
            result['Total'] = self.total

        if self.web_vtturl is not None:
            result['WebVTTUrl'] = self.web_vtturl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotUrls') is not None:
            self.snapshot_urls = m.get('SnapshotUrls')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('WebVTTUrl') is not None:
            self.web_vtturl = m.get('WebVTTUrl')

        return self

