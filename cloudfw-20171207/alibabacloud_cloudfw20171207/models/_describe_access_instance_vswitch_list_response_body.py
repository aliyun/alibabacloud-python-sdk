# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessInstanceVSwitchListResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        zones: List[main_models.DescribeAccessInstanceVSwitchListResponseBodyZones] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['Zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.zones = []
        if m.get('Zones') is not None:
            for k1 in m.get('Zones'):
                temp_model = main_models.DescribeAccessInstanceVSwitchListResponseBodyZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class DescribeAccessInstanceVSwitchListResponseBodyZones(DaraModel):
    def __init__(
        self,
        v_switch_list: List[main_models.DescribeAccessInstanceVSwitchListResponseBodyZonesVSwitchList] = None,
        zone_id: str = None,
    ):
        self.v_switch_list = v_switch_list
        self.zone_id = zone_id

    def validate(self):
        if self.v_switch_list:
            for v1 in self.v_switch_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VSwitchList'] = []
        if self.v_switch_list is not None:
            for k1 in self.v_switch_list:
                result['VSwitchList'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_switch_list = []
        if m.get('VSwitchList') is not None:
            for k1 in m.get('VSwitchList'):
                temp_model = main_models.DescribeAccessInstanceVSwitchListResponseBodyZonesVSwitchList()
                self.v_switch_list.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAccessInstanceVSwitchListResponseBodyZonesVSwitchList(DaraModel):
    def __init__(
        self,
        available_ip_address_count: int = None,
        cidr_block: str = None,
        firewall_vswitch: bool = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
    ):
        self.available_ip_address_count = available_ip_address_count
        self.cidr_block = cidr_block
        self.firewall_vswitch = firewall_vswitch
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.firewall_vswitch is not None:
            result['FirewallVSwitch'] = self.firewall_vswitch

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('FirewallVSwitch') is not None:
            self.firewall_vswitch = m.get('FirewallVSwitch')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

