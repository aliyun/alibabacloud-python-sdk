# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeZonesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
        zones: main_models.DescribeZonesResponseBodyZones = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of returned pages.
        self.total_pages = total_pages
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        if self.zones is not None:
            result['Zones'] = self.zones.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

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
        create_time: str = None,
        create_timestamp: int = None,
        creator: str = None,
        creator_sub_type: str = None,
        dns_group: str = None,
        dns_group_changing: bool = None,
        is_ptr: bool = None,
        proxy_pattern: str = None,
        record_count: int = None,
        remark: str = None,
        resource_group_id: str = None,
        resource_tags: main_models.DescribeZonesResponseBodyZonesZoneResourceTags = None,
        slave_dns_status: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        zone_id: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        zone_type: str = None,
    ):
        self.create_time = create_time
        self.create_timestamp = create_timestamp
        self.creator = creator
        self.creator_sub_type = creator_sub_type
        self.dns_group = dns_group
        self.dns_group_changing = dns_group_changing
        self.is_ptr = is_ptr
        self.proxy_pattern = proxy_pattern
        self.record_count = record_count
        self.remark = remark
        self.resource_group_id = resource_group_id
        self.resource_tags = resource_tags
        self.slave_dns_status = slave_dns_status
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.zone_tag = zone_tag
        self.zone_type = zone_type

    def validate(self):
        if self.resource_tags:
            self.resource_tags.validate()

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

        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type

        if self.dns_group is not None:
            result['DnsGroup'] = self.dns_group

        if self.dns_group_changing is not None:
            result['DnsGroupChanging'] = self.dns_group_changing

        if self.is_ptr is not None:
            result['IsPtr'] = self.is_ptr

        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_tags is not None:
            result['ResourceTags'] = self.resource_tags.to_map()

        if self.slave_dns_status is not None:
            result['SlaveDnsStatus'] = self.slave_dns_status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

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

        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')

        if m.get('DnsGroup') is not None:
            self.dns_group = m.get('DnsGroup')

        if m.get('DnsGroupChanging') is not None:
            self.dns_group_changing = m.get('DnsGroupChanging')

        if m.get('IsPtr') is not None:
            self.is_ptr = m.get('IsPtr')

        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceTags') is not None:
            temp_model = main_models.DescribeZonesResponseBodyZonesZoneResourceTags()
            self.resource_tags = temp_model.from_map(m.get('ResourceTags'))

        if m.get('SlaveDnsStatus') is not None:
            self.slave_dns_status = m.get('SlaveDnsStatus')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

class DescribeZonesResponseBodyZonesZoneResourceTags(DaraModel):
    def __init__(
        self,
        resource_tag: List[main_models.DescribeZonesResponseBodyZonesZoneResourceTagsResourceTag] = None,
    ):
        self.resource_tag = resource_tag

    def validate(self):
        if self.resource_tag:
            for v1 in self.resource_tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourceTag'] = []
        if self.resource_tag is not None:
            for k1 in self.resource_tag:
                result['ResourceTag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_tag = []
        if m.get('ResourceTag') is not None:
            for k1 in m.get('ResourceTag'):
                temp_model = main_models.DescribeZonesResponseBodyZonesZoneResourceTagsResourceTag()
                self.resource_tag.append(temp_model.from_map(k1))

        return self

class DescribeZonesResponseBodyZonesZoneResourceTagsResourceTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

