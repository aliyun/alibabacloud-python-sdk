# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeZoneVpcTreeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        zones: main_models.DescribeZoneVpcTreeResponseBodyZones = None,
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
            temp_model = main_models.DescribeZoneVpcTreeResponseBodyZones()
            self.zones = temp_model.from_map(m.get('Zones'))

        return self

class DescribeZoneVpcTreeResponseBodyZones(DaraModel):
    def __init__(
        self,
        zone: List[main_models.DescribeZoneVpcTreeResponseBodyZonesZone] = None,
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
                temp_model = main_models.DescribeZoneVpcTreeResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k1))

        return self

class DescribeZoneVpcTreeResponseBodyZonesZone(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        creator: str = None,
        creator_type: str = None,
        dns_group: str = None,
        dns_group_changing: bool = None,
        is_ptr: bool = None,
        record_count: int = None,
        remark: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        vpcs: main_models.DescribeZoneVpcTreeResponseBodyZonesZoneVpcs = None,
        zone_id: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        zone_type: str = None,
    ):
        # The time when the zone was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the zone was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The creator of the zone.
        self.creator = creator
        # The operator type.
        self.creator_type = creator_type
        # The logical location of the built-in authoritative module in which the zone is added. Valid values:
        # 
        # *   NORMAL_ZONE: regular module
        # *   FAST_ZONE: acceleration module
        self.dns_group = dns_group
        # Indicates whether the zone is being removed to another logical location. Valid values:
        # 
        # *   true
        # *   false
        self.dns_group_changing = dns_group_changing
        # Indicates whether the zone is a reverse lookup zone. Valid values:
        # 
        # *   true
        # *   false
        self.is_ptr = is_ptr
        # The number of Domain Name System (DNS) records added for the zone.
        self.record_count = record_count
        # The description of the zone.
        self.remark = remark
        # The time when the zone was last modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the zone was last modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp
        # The VPCs associated with the zone.
        self.vpcs = vpcs
        # The zone ID. This ID uniquely identifies the zone.
        self.zone_id = zone_id
        # The zone name.
        self.zone_name = zone_name
        # The type of the cloud service.
        # 
        # 
        # **Valid values:**
        # 
        # *   If ZoneType is set to AUTH_ZONE, no value is returned for this parameter.
        # 
        # *   If ZoneType is set to CLOUD_PRODUCT_ZONE, the type of the cloud service is returned.
        self.zone_tag = zone_tag
        # The zone type. Valid values:
        # 
        # *   AUTH_ZONE: authoritative zone
        # *   CLOUD_PRODUCT_ZONE: authoritative zone for cloud services
        self.zone_type = zone_type

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type

        if self.dns_group is not None:
            result['DnsGroup'] = self.dns_group

        if self.dns_group_changing is not None:
            result['DnsGroupChanging'] = self.dns_group_changing

        if self.is_ptr is not None:
            result['IsPtr'] = self.is_ptr

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag

        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')

        if m.get('DnsGroup') is not None:
            self.dns_group = m.get('DnsGroup')

        if m.get('DnsGroupChanging') is not None:
            self.dns_group_changing = m.get('DnsGroupChanging')

        if m.get('IsPtr') is not None:
            self.is_ptr = m.get('IsPtr')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('Vpcs') is not None:
            temp_model = main_models.DescribeZoneVpcTreeResponseBodyZonesZoneVpcs()
            self.vpcs = temp_model.from_map(m.get('Vpcs'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

class DescribeZoneVpcTreeResponseBodyZonesZoneVpcs(DaraModel):
    def __init__(
        self,
        vpc: List[main_models.DescribeZoneVpcTreeResponseBodyZonesZoneVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for v1 in self.vpc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Vpc'] = []
        if self.vpc is not None:
            for k1 in self.vpc:
                result['Vpc'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k1 in m.get('Vpc'):
                temp_model = main_models.DescribeZoneVpcTreeResponseBodyZonesZoneVpcsVpc()
                self.vpc.append(temp_model.from_map(k1))

        return self

class DescribeZoneVpcTreeResponseBodyZonesZoneVpcsVpc(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        region_name: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_type: str = None,
    ):
        # The region ID of the VPC.
        self.region_id = region_id
        # The name of the region to which the VPC belongs.
        self.region_name = region_name
        # The VPC ID. The unique ID of the VPC.
        self.vpc_id = vpc_id
        # The VPC name.
        self.vpc_name = vpc_name
        # The VPC type. Valid values:
        # 
        # *   STANDARD: standard VPC
        # *   EDS: Elastic Desktop Service (EDS) workspace VPC
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        return self

