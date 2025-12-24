# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class GetLindormV2StorageUsageResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        capacity_by_disk_category: List[Dict[str, Any]] = None,
        instance_storage_zone_map: Dict[str, Any] = None,
        request_id: str = None,
        usage_by_disk_category: List[Dict[str, Any]] = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.capacity_by_disk_category = capacity_by_disk_category
        self.instance_storage_zone_map = instance_storage_zone_map
        self.request_id = request_id
        self.usage_by_disk_category = usage_by_disk_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.capacity_by_disk_category is not None:
            result['CapacityByDiskCategory'] = self.capacity_by_disk_category

        if self.instance_storage_zone_map is not None:
            result['InstanceStorageZoneMap'] = self.instance_storage_zone_map

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.usage_by_disk_category is not None:
            result['UsageByDiskCategory'] = self.usage_by_disk_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('CapacityByDiskCategory') is not None:
            self.capacity_by_disk_category = m.get('CapacityByDiskCategory')

        if m.get('InstanceStorageZoneMap') is not None:
            self.instance_storage_zone_map = m.get('InstanceStorageZoneMap')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UsageByDiskCategory') is not None:
            self.usage_by_disk_category = m.get('UsageByDiskCategory')

        return self

