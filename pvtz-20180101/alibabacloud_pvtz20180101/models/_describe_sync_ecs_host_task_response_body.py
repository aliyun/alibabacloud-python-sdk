# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeSyncEcsHostTaskResponseBody(DaraModel):
    def __init__(
        self,
        ecs_regions: main_models.DescribeSyncEcsHostTaskResponseBodyEcsRegions = None,
        regions: main_models.DescribeSyncEcsHostTaskResponseBodyRegions = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
        zone_id: str = None,
    ):
        # The synchronized regions where the ECS instances are deployed.
        self.ecs_regions = ecs_regions
        # The synchronized region IDs of the ECS instances.
        self.regions = regions
        # The request ID.
        self.request_id = request_id
        # Indicates whether hostname automatic synchronization is enabled. Valid values:
        # 
        # *   ON: Hostname automatic synchronization is enabled. After this feature is enabled, the system automatically reads the hostnames of the Elastic Compute Service (ECS) instances in the specified regions and updates Domain Name System (DNS) records at an interval of 1 minute.
        # *   OFF: Hostname automatic synchronization is disabled.
        self.status = status
        # Indicates whether the task was successful. Valid values:
        # 
        # *   True
        # *   False
        self.success = success
        # The zone ID. This ID uniquely identifies the zone.
        self.zone_id = zone_id

    def validate(self):
        if self.ecs_regions:
            self.ecs_regions.validate()
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_regions is not None:
            result['EcsRegions'] = self.ecs_regions.to_map()

        if self.regions is not None:
            result['Regions'] = self.regions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsRegions') is not None:
            temp_model = main_models.DescribeSyncEcsHostTaskResponseBodyEcsRegions()
            self.ecs_regions = temp_model.from_map(m.get('EcsRegions'))

        if m.get('Regions') is not None:
            temp_model = main_models.DescribeSyncEcsHostTaskResponseBodyRegions()
            self.regions = temp_model.from_map(m.get('Regions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeSyncEcsHostTaskResponseBodyRegions(DaraModel):
    def __init__(
        self,
        region_id: List[str] = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeSyncEcsHostTaskResponseBodyEcsRegions(DaraModel):
    def __init__(
        self,
        ecs_region: List[main_models.DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegion] = None,
    ):
        self.ecs_region = ecs_region

    def validate(self):
        if self.ecs_region:
            for v1 in self.ecs_region:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EcsRegion'] = []
        if self.ecs_region is not None:
            for k1 in self.ecs_region:
                result['EcsRegion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_region = []
        if m.get('EcsRegion') is not None:
            for k1 in m.get('EcsRegion'):
                temp_model = main_models.DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegion()
                self.ecs_region.append(temp_model.from_map(k1))

        return self

class DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegion(DaraModel):
    def __init__(
        self,
        region_ids: main_models.DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegionRegionIds = None,
        user_id: int = None,
    ):
        # The synchronized region IDs.
        self.region_ids = region_ids
        # The user ID to which the region belongs. This parameter is used in cross-account synchronization scenarios.
        self.user_id = user_id

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionIds') is not None:
            temp_model = main_models.DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegionRegionIds()
            self.region_ids = temp_model.from_map(m.get('RegionIds'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeSyncEcsHostTaskResponseBodyEcsRegionsEcsRegionRegionIds(DaraModel):
    def __init__(
        self,
        region_id: List[str] = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

