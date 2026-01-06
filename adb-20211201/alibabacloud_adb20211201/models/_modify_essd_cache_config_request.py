# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEssdCacheConfigRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        enable_essd_cache: bool = None,
        essd_cache_size: int = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable the disk cache feature.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is required.
        self.enable_essd_cache = enable_essd_cache
        # The disk cache size. Unit: GB.
        self.essd_cache_size = essd_cache_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable_essd_cache is not None:
            result['EnableEssdCache'] = self.enable_essd_cache

        if self.essd_cache_size is not None:
            result['EssdCacheSize'] = self.essd_cache_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EnableEssdCache') is not None:
            self.enable_essd_cache = m.get('EnableEssdCache')

        if m.get('EssdCacheSize') is not None:
            self.essd_cache_size = m.get('EssdCacheSize')

        return self

