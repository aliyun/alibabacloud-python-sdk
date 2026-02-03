# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        region_ids: main_models.DescribeRegionsResponseBodyRegionIds = None,
        request_id: str = None,
    ):
        # The **region IDs**.
        self.region_ids = region_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionIds') is not None:
            temp_model = main_models.DescribeRegionsResponseBodyRegionIds()
            self.region_ids = temp_model.from_map(m.get('RegionIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRegionsResponseBodyRegionIds(DaraModel):
    def __init__(
        self,
        kvstore_region: List[main_models.DescribeRegionsResponseBodyRegionIdsKVStoreRegion] = None,
    ):
        self.kvstore_region = kvstore_region

    def validate(self):
        if self.kvstore_region:
            for v1 in self.kvstore_region:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KVStoreRegion'] = []
        if self.kvstore_region is not None:
            for k1 in self.kvstore_region:
                result['KVStoreRegion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kvstore_region = []
        if m.get('KVStoreRegion') is not None:
            for k1 in m.get('KVStoreRegion'):
                temp_model = main_models.DescribeRegionsResponseBodyRegionIdsKVStoreRegion()
                self.kvstore_region.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyRegionIdsKVStoreRegion(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        zone_id_list: main_models.DescribeRegionsResponseBodyRegionIdsKVStoreRegionZoneIdList = None,
        zone_ids: str = None,
    ):
        # The name of the region.
        self.local_name = local_name
        # The endpoint of the region.
        self.region_endpoint = region_endpoint
        # The ID of the region.
        self.region_id = region_id
        # The zone IDs.
        self.zone_id_list = zone_id_list
        # The IDs of the zones in the region.
        self.zone_ids = zone_ids

    def validate(self):
        if self.zone_id_list:
            self.zone_id_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id_list is not None:
            result['ZoneIdList'] = self.zone_id_list.to_map()

        if self.zone_ids is not None:
            result['ZoneIds'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneIdList') is not None:
            temp_model = main_models.DescribeRegionsResponseBodyRegionIdsKVStoreRegionZoneIdList()
            self.zone_id_list = temp_model.from_map(m.get('ZoneIdList'))

        if m.get('ZoneIds') is not None:
            self.zone_ids = m.get('ZoneIds')

        return self

class DescribeRegionsResponseBodyRegionIdsKVStoreRegionZoneIdList(DaraModel):
    def __init__(
        self,
        zone_id: List[str] = None,
    ):
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

