# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreloadCachesShrinkRequest(DaraModel):
    def __init__(
        self,
        content_shrink: str = None,
        headers_shrink: str = None,
        site_id: int = None,
    ):
        # The files to be prefetched.
        self.content_shrink = content_shrink
        # By default, prefetch requests include the Accept-Encoding:gzip header. If you want a prefetch request to include other headers or implement multi-replica prefetch, you can specify a custom prefetch header by configuring the Headers parameter.
        self.headers_shrink = headers_shrink
        # The website ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the ID.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.headers_shrink is not None:
            result['Headers'] = self.headers_shrink

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('Headers') is not None:
            self.headers_shrink = m.get('Headers')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

