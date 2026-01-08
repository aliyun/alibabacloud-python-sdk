# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeFirewallVswitchResourcesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        vswitch_list: List[main_models.DescribeFirewallVswitchResourcesResponseBodyVswitchList] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.vswitch_list = vswitch_list

    def validate(self):
        if self.vswitch_list:
            for v1 in self.vswitch_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VswitchList'] = []
        if self.vswitch_list is not None:
            for k1 in self.vswitch_list:
                result['VswitchList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vswitch_list = []
        if m.get('VswitchList') is not None:
            for k1 in m.get('VswitchList'):
                temp_model = main_models.DescribeFirewallVswitchResourcesResponseBodyVswitchList()
                self.vswitch_list.append(temp_model.from_map(k1))

        return self

class DescribeFirewallVswitchResourcesResponseBodyVswitchList(DaraModel):
    def __init__(
        self,
        available_ip_count: str = None,
        cidr_block: str = None,
        detail: str = None,
        firewall_list: List[main_models.DescribeFirewallVswitchResourcesResponseBodyVswitchListFirewallList] = None,
        route_table_id: str = None,
        route_table_type: str = None,
        status: str = None,
        vswitch_id: str = None,
        vswitch_name: str = None,
        zone_id: str = None,
    ):
        self.available_ip_count = available_ip_count
        self.cidr_block = cidr_block
        self.detail = detail
        self.firewall_list = firewall_list
        self.route_table_id = route_table_id
        self.route_table_type = route_table_type
        self.status = status
        self.vswitch_id = vswitch_id
        self.vswitch_name = vswitch_name
        self.zone_id = zone_id

    def validate(self):
        if self.firewall_list:
            for v1 in self.firewall_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_ip_count is not None:
            result['AvailableIpCount'] = self.available_ip_count

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.detail is not None:
            result['Detail'] = self.detail

        result['FirewallList'] = []
        if self.firewall_list is not None:
            for k1 in self.firewall_list:
                result['FirewallList'].append(k1.to_map() if k1 else None)

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.route_table_type is not None:
            result['RouteTableType'] = self.route_table_type

        if self.status is not None:
            result['Status'] = self.status

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.vswitch_name is not None:
            result['VswitchName'] = self.vswitch_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpCount') is not None:
            self.available_ip_count = m.get('AvailableIpCount')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        self.firewall_list = []
        if m.get('FirewallList') is not None:
            for k1 in m.get('FirewallList'):
                temp_model = main_models.DescribeFirewallVswitchResourcesResponseBodyVswitchListFirewallList()
                self.firewall_list.append(temp_model.from_map(k1))

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('RouteTableType') is not None:
            self.route_table_type = m.get('RouteTableType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('VswitchName') is not None:
            self.vswitch_name = m.get('VswitchName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeFirewallVswitchResourcesResponseBodyVswitchListFirewallList(DaraModel):
    def __init__(
        self,
        firewall_id: str = None,
        firewall_name: str = None,
        firewall_type: str = None,
    ):
        self.firewall_id = firewall_id
        self.firewall_name = firewall_name
        self.firewall_type = firewall_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        return self

