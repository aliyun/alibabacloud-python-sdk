# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PreloadVodObjectCachesRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        l_2preload: bool = None,
        object_path: str = None,
        owner_id: int = None,
        security_token: str = None,
        with_header: str = None,
    ):
        # The acceleration region in which you want to prefetch content. If you do not specify a region, the value overseas is used.
        # 
        # *   **domestic**: Chinese mainland
        # *   **overseas**: outside the Chinese mainland
        self.area = area
        # Specifies whether to prefetch content to POPs. Valid values:
        # 
        # *   **true**: prefetches content to nodes that include L2 DCDN nodes.
        # *   **false**: prefetches content to L2 POPs or L3 POPs.
        self.l_2preload = l_2preload
        # The URL of the file to be prefetched. Separate multiple URLs with line breaks (\\n or \\r\\n).
        # 
        # This parameter is required.
        self.object_path = object_path
        self.owner_id = owner_id
        self.security_token = security_token
        # The custom header for prefetch in the JSON format.
        self.with_header = with_header

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.l_2preload is not None:
            result['L2Preload'] = self.l_2preload

        if self.object_path is not None:
            result['ObjectPath'] = self.object_path

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.with_header is not None:
            result['WithHeader'] = self.with_header

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('L2Preload') is not None:
            self.l_2preload = m.get('L2Preload')

        if m.get('ObjectPath') is not None:
            self.object_path = m.get('ObjectPath')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('WithHeader') is not None:
            self.with_header = m.get('WithHeader')

        return self

