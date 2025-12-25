# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class PreloadCachesRequest(DaraModel):
    def __init__(
        self,
        content: List[str] = None,
        headers: Dict[str, str] = None,
        site_id: int = None,
    ):
        # The files to be prefetched.
        self.content = content
        # By default, prefetch requests include the Accept-Encoding:gzip header. If you want a prefetch request to include other headers or implement multi-replica prefetch, you can specify a custom prefetch header by configuring the Headers parameter.
        self.headers = headers
        # The website ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.headers is not None:
            result['Headers'] = self.headers

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

