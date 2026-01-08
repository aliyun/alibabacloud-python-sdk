# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeFirewallVSwitchResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        vswitch_list: List[main_models.DescribeFirewallVSwitchResponseBodyVswitchList] = None,
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
                temp_model = main_models.DescribeFirewallVSwitchResponseBodyVswitchList()
                self.vswitch_list.append(temp_model.from_map(k1))

        return self

class DescribeFirewallVSwitchResponseBodyVswitchList(DaraModel):
    def __init__(
        self,
        available_ip_count: str = None,
        cidr_block: str = None,
        firewall_count: str = None,
        firewall_list: List[main_models.DescribeFirewallVSwitchResponseBodyVswitchListFirewallList] = None,
        member_uid: str = None,
        region_no: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        vswitch_name: str = None,
        zone_id: str = None,
    ):
        self.available_ip_count = available_ip_count
        self.cidr_block = cidr_block
        self.firewall_count = firewall_count
        self.firewall_list = firewall_list
        self.member_uid = member_uid
        self.region_no = region_no
        self.vpc_id = vpc_id
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

        if self.firewall_count is not None:
            result['FirewallCount'] = self.firewall_count

        result['FirewallList'] = []
        if self.firewall_list is not None:
            for k1 in self.firewall_list:
                result['FirewallList'].append(k1.to_map() if k1 else None)

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

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

        if m.get('FirewallCount') is not None:
            self.firewall_count = m.get('FirewallCount')

        self.firewall_list = []
        if m.get('FirewallList') is not None:
            for k1 in m.get('FirewallList'):
                temp_model = main_models.DescribeFirewallVSwitchResponseBodyVswitchListFirewallList()
                self.firewall_list.append(temp_model.from_map(k1))

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('VswitchName') is not None:
            self.vswitch_name = m.get('VswitchName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeFirewallVSwitchResponseBodyVswitchListFirewallList(DaraModel):
    def __init__(
        self,
        firewall_id: str = None,
        firewall_name: str = None,
    ):
        self.firewall_id = firewall_id
        self.firewall_name = firewall_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')

        return self

