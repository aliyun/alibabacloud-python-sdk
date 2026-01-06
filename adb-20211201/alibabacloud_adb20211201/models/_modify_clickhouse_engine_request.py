# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyClickhouseEngineRequest(DaraModel):
    def __init__(
        self,
        cache_size: int = None,
        dbcluster_id: str = None,
        enabled: bool = None,
        owner_id: str = None,
    ):
        # The disk cache size of the wide table engine. Unit: GB. Default value: 100. Valid values: 100 to 1000.
        self.cache_size = cache_size
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable the wide table engine feature. Valid values:
        # 
        # - true
        # 
        # - false
        self.enabled = enabled
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

