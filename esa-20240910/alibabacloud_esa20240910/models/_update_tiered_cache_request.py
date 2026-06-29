# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTieredCacheRequest(DaraModel):
    def __init__(
        self,
        cache_architecture_mode: str = None,
        site_id: int = None,
    ):
        # The multi-level cache architecture mode. Valid values:
        # - edge: edge cache layer.
        # - edge_smart: edge cache layer + smart cache layer.
        # - edge_regional: edge cache layer + regional cache layer.
        # - edge_regional_smart: edge cache layer + regional cache layer + smart cache layer.
        # 
        # This parameter is required.
        self.cache_architecture_mode = cache_architecture_mode
        # The site ID. You can call [ListSites](https://help.aliyun.com/document_detail/2850189.html) to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_architecture_mode is not None:
            result['CacheArchitectureMode'] = self.cache_architecture_mode

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheArchitectureMode') is not None:
            self.cache_architecture_mode = m.get('CacheArchitectureMode')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

