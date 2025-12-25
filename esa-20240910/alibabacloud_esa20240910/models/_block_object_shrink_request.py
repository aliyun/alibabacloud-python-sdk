# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BlockObjectShrinkRequest(DaraModel):
    def __init__(
        self,
        content_shrink: str = None,
        extension: str = None,
        maxage: int = None,
        site_id: int = None,
        type: str = None,
    ):
        # The content to block.
        # 
        # This parameter is required.
        self.content_shrink = content_shrink
        # The blocking period that you can extend. Set the value to 2year.
        self.extension = extension
        # The period of time during which the URL is blocked. Unit: seconds. Specify this parameter if Type is set to block.
        self.maxage = maxage
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The type. Valid values:
        # 
        # *   **block**
        # *   **unblock**
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.maxage is not None:
            result['Maxage'] = self.maxage

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('Maxage') is not None:
            self.maxage = m.get('Maxage')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

