# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kvcachestore20260617 import models as main_models
from darabonba.model import DaraModel

class ListKVCacheStoreAvailableHpnZonesResponseBody(DaraModel):
    def __init__(
        self,
        instance_hpn_zones: List[main_models.ListKVCacheStoreAvailableHpnZonesResponseBodyInstanceHpnZones] = None,
        request_id: str = None,
    ):
        self.instance_hpn_zones = instance_hpn_zones
        self.request_id = request_id

    def validate(self):
        if self.instance_hpn_zones:
            for v1 in self.instance_hpn_zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceHpnZones'] = []
        if self.instance_hpn_zones is not None:
            for k1 in self.instance_hpn_zones:
                result['InstanceHpnZones'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_hpn_zones = []
        if m.get('InstanceHpnZones') is not None:
            for k1 in m.get('InstanceHpnZones'):
                temp_model = main_models.ListKVCacheStoreAvailableHpnZonesResponseBodyInstanceHpnZones()
                self.instance_hpn_zones.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListKVCacheStoreAvailableHpnZonesResponseBodyInstanceHpnZones(DaraModel):
    def __init__(
        self,
        available_hpn_zones: List[main_models.ListKVCacheStoreAvailableHpnZonesResponseBodyInstanceHpnZonesAvailableHpnZones] = None,
        kvcs_id: str = None,
        zone_id: str = None,
    ):
        self.available_hpn_zones = available_hpn_zones
        self.kvcs_id = kvcs_id
        self.zone_id = zone_id

    def validate(self):
        if self.available_hpn_zones:
            for v1 in self.available_hpn_zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableHpnZones'] = []
        if self.available_hpn_zones is not None:
            for k1 in self.available_hpn_zones:
                result['AvailableHpnZones'].append(k1.to_map() if k1 else None)

        if self.kvcs_id is not None:
            result['KvcsId'] = self.kvcs_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_hpn_zones = []
        if m.get('AvailableHpnZones') is not None:
            for k1 in m.get('AvailableHpnZones'):
                temp_model = main_models.ListKVCacheStoreAvailableHpnZonesResponseBodyInstanceHpnZonesAvailableHpnZones()
                self.available_hpn_zones.append(temp_model.from_map(k1))

        if m.get('KvcsId') is not None:
            self.kvcs_id = m.get('KvcsId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListKVCacheStoreAvailableHpnZonesResponseBodyInstanceHpnZonesAvailableHpnZones(DaraModel):
    def __init__(
        self,
        hpn_zone: str = None,
    ):
        self.hpn_zone = hpn_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        return self

