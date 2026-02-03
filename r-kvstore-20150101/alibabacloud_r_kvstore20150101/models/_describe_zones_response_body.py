# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeZonesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zones: main_models.DescribeZonesResponseBodyZones = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The queried zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.zones is not None:
            result['Zones'] = self.zones.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Zones') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m.get('Zones'))

        return self

class DescribeZonesResponseBodyZones(DaraModel):
    def __init__(
        self,
        kvstore_zone: List[main_models.DescribeZonesResponseBodyZonesKVStoreZone] = None,
    ):
        self.kvstore_zone = kvstore_zone

    def validate(self):
        if self.kvstore_zone:
            for v1 in self.kvstore_zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KVStoreZone'] = []
        if self.kvstore_zone is not None:
            for k1 in self.kvstore_zone:
                result['KVStoreZone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kvstore_zone = []
        if m.get('KVStoreZone') is not None:
            for k1 in m.get('KVStoreZone'):
                temp_model = main_models.DescribeZonesResponseBodyZonesKVStoreZone()
                self.kvstore_zone.append(temp_model.from_map(k1))

        return self

class DescribeZonesResponseBodyZonesKVStoreZone(DaraModel):
    def __init__(
        self,
        disabled: bool = None,
        is_rds: bool = None,
        region_id: str = None,
        switch_network: bool = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        # Indicates whether Tair (Redis OSS-compatible) instances can be created in the current zone. Valid values:
        # 
        # *   **true**: Tair (Redis OSS-compatible) instances cannot be created in the current zone.
        # *   **false**: Tair (Redis OSS-compatible) instances can be created in the current zone.
        self.disabled = disabled
        # Indicates whether the zone is managed by ApsaraDB RDS. The return value of this parameter is **true** in Tair (Redis OSS-compatible).
        self.is_rds = is_rds
        # The ID of the region.
        self.region_id = region_id
        # Indicates whether the network type of the instance can be changed from the classic network to Virtual Private Cloud (VPC). Valid values:
        # 
        # *   **true**: The network type of the instance can be changed from the classic network to VPC.
        # *   **false**: The network type of the instance cannot be changed from the classic network to VPC.
        self.switch_network = switch_network
        # The ID of the zone within the specified region.
        self.zone_id = zone_id
        # The name of the zone within the specified region.
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.is_rds is not None:
            result['IsRds'] = self.is_rds

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_network is not None:
            result['SwitchNetwork'] = self.switch_network

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('IsRds') is not None:
            self.is_rds = m.get('IsRds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchNetwork') is not None:
            self.switch_network = m.get('SwitchNetwork')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

