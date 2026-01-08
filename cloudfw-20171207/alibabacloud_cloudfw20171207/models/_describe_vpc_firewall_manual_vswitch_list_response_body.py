# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallManualVSwitchListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        v_switch_list: List[main_models.DescribeVpcFirewallManualVSwitchListResponseBodyVSwitchList] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.v_switch_list = v_switch_list

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VSwitchList'] = []
        if self.v_switch_list is not None:
            for k1 in self.v_switch_list:
                result['VSwitchList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.v_switch_list = []
        if m.get('VSwitchList') is not None:
            for k1 in m.get('VSwitchList'):
                temp_model = main_models.DescribeVpcFirewallManualVSwitchListResponseBodyVSwitchList()
                self.v_switch_list.append(temp_model.from_map(k1))

        return self

class DescribeVpcFirewallManualVSwitchListResponseBodyVSwitchList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        available_ip_address_count: int = None,
        cidr_block: str = None,
        owner_id: int = None,
        region_no: str = None,
        route_table_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.available_ip_address_count = available_ip_address_count
        self.cidr_block = cidr_block
        self.owner_id = owner_id
        self.region_no = region_no
        self.route_table_id = route_table_id
        self.status = status
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

