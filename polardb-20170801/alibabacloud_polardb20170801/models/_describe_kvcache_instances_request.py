# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeKVCacheInstancesRequest(DaraModel):
    def __init__(
        self,
        kvcache_instance_description: str = None,
        kvcache_instance_ids: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        relative_dbcluster_id: str = None,
    ):
        # The description of the KVCache instance.
        self.kvcache_instance_description = kvcache_instance_description
        # The KVCache instance IDs. Separate multiple instance IDs with commas (,).
        self.kvcache_instance_ids = kvcache_instance_ids
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The instance ID of the associated PolarDB instance.
        self.relative_dbcluster_id = relative_dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kvcache_instance_description is not None:
            result['KVCacheInstanceDescription'] = self.kvcache_instance_description

        if self.kvcache_instance_ids is not None:
            result['KVCacheInstanceIds'] = self.kvcache_instance_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.relative_dbcluster_id is not None:
            result['RelativeDBClusterId'] = self.relative_dbcluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KVCacheInstanceDescription') is not None:
            self.kvcache_instance_description = m.get('KVCacheInstanceDescription')

        if m.get('KVCacheInstanceIds') is not None:
            self.kvcache_instance_ids = m.get('KVCacheInstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelativeDBClusterId') is not None:
            self.relative_dbcluster_id = m.get('RelativeDBClusterId')

        return self

