# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeZonesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zones: main_models.DescribeZonesResponseBodyZones = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The zones.
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
        zone: List[main_models.DescribeZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for v1 in self.zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Zone'] = []
        if self.zone is not None:
            for k1 in self.zone:
                result['Zone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k1 in m.get('Zone'):
                temp_model = main_models.DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k1))

        return self

class DescribeZonesResponseBodyZonesZone(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        slave_zones: main_models.DescribeZonesResponseBodyZonesZoneSlaveZones = None,
        zone_id: str = None,
    ):
        # The name of the zone.
        self.local_name = local_name
        # The secondary zones.
        self.slave_zones = slave_zones
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        if self.slave_zones:
            self.slave_zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.slave_zones is not None:
            result['SlaveZones'] = self.slave_zones.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('SlaveZones') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneSlaveZones()
            self.slave_zones = temp_model.from_map(m.get('SlaveZones'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeZonesResponseBodyZonesZoneSlaveZones(DaraModel):
    def __init__(
        self,
        slave_zone: List[main_models.DescribeZonesResponseBodyZonesZoneSlaveZonesSlaveZone] = None,
    ):
        self.slave_zone = slave_zone

    def validate(self):
        if self.slave_zone:
            for v1 in self.slave_zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlaveZone'] = []
        if self.slave_zone is not None:
            for k1 in self.slave_zone:
                result['SlaveZone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slave_zone = []
        if m.get('SlaveZone') is not None:
            for k1 in m.get('SlaveZone'):
                temp_model = main_models.DescribeZonesResponseBodyZonesZoneSlaveZonesSlaveZone()
                self.slave_zone.append(temp_model.from_map(k1))

        return self

class DescribeZonesResponseBodyZonesZoneSlaveZonesSlaveZone(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        # The name of the secondary zone.
        self.local_name = local_name
        # The ID of the secondary zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

