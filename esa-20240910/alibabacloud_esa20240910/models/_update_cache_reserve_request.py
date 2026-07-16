# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCacheReserveRequest(DaraModel):
    def __init__(
        self,
        cache_reserve_instance_id: str = None,
        enable: str = None,
        site_id: int = None,
    ):
        # The cache reserve instance ID.
        self.cache_reserve_instance_id = cache_reserve_instance_id
        # The switch. Valid values:
        # 
        # - **on**: enabled.
        # - **off**: disabled.
        self.enable = enable
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
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
        if self.cache_reserve_instance_id is not None:
            result['CacheReserveInstanceId'] = self.cache_reserve_instance_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheReserveInstanceId') is not None:
            self.cache_reserve_instance_id = m.get('CacheReserveInstanceId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

