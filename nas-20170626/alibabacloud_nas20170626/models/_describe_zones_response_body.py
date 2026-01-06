# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeZonesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zones: main_models.DescribeZonesResponseBodyZones = None,
    ):
        # The request ID.
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
        capacity: main_models.DescribeZonesResponseBodyZonesZoneCapacity = None,
        instance_types: main_models.DescribeZonesResponseBodyZonesZoneInstanceTypes = None,
        performance: main_models.DescribeZonesResponseBodyZonesZonePerformance = None,
        zone_id: str = None,
    ):
        # This parameter is reserved. You can ignore this parameter.
        self.capacity = capacity
        # The details about file system types.
        self.instance_types = instance_types
        # This parameter is reserved. You can ignore this parameter.
        self.performance = performance
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.capacity:
            self.capacity.validate()
        if self.instance_types:
            self.instance_types.validate()
        if self.performance:
            self.performance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity.to_map()

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()

        if self.performance is not None:
            result['Performance'] = self.performance.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneCapacity()
            self.capacity = temp_model.from_map(m.get('Capacity'))

        if m.get('InstanceTypes') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneInstanceTypes()
            self.instance_types = temp_model.from_map(m.get('InstanceTypes'))

        if m.get('Performance') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZonePerformance()
            self.performance = temp_model.from_map(m.get('Performance'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeZonesResponseBodyZonesZonePerformance(DaraModel):
    def __init__(
        self,
        protocol: List[str] = None,
    ):
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeZonesResponseBodyZonesZoneInstanceTypes(DaraModel):
    def __init__(
        self,
        instance_type: List[main_models.DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type:
            for v1 in self.instance_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k1 in self.instance_type:
                result['InstanceType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type = []
        if m.get('InstanceType') is not None:
            for k1 in m.get('InstanceType'):
                temp_model = main_models.DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k1))

        return self

class DescribeZonesResponseBodyZonesZoneInstanceTypesInstanceType(DaraModel):
    def __init__(
        self,
        protocol_type: str = None,
        storage_type: str = None,
    ):
        # The protocol type.
        # 
        # *   If the FileSystemType parameter is set to standard, the protocol type is nfs or smb.
        # *   If the FileSystemType parameter is set to extreme, the protocol type is nfs.
        # *   If the FileSystemType parameter is set to cpfs, the protocol type is cpfs.
        self.protocol_type = protocol_type
        # The storage type.
        # 
        # *   If the FileSystemType parameter is set to standard, the storage type is Performance or Capacity.
        # *   If the FileSystemType parameter is set to extreme, the storage type is standard or advance.
        # *   If the FileSystemType parameter is set to cpfs, the storage type is advance_100 (100 MB/s/TiB baseline) or advance_200 (200 MB/s/TiB baseline).
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class DescribeZonesResponseBodyZonesZoneCapacity(DaraModel):
    def __init__(
        self,
        protocol: List[str] = None,
    ):
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

