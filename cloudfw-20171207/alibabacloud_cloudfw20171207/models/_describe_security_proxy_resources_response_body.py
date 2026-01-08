# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityProxyResourcesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_list: List[main_models.DescribeSecurityProxyResourcesResponseBodyResourceList] = None,
    ):
        self.request_id = request_id
        self.resource_list = resource_list

    def validate(self):
        if self.resource_list:
            for v1 in self.resource_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceList'] = []
        if self.resource_list is not None:
            for k1 in self.resource_list:
                result['ResourceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k1 in m.get('ResourceList'):
                temp_model = main_models.DescribeSecurityProxyResourcesResponseBodyResourceList()
                self.resource_list.append(temp_model.from_map(k1))

        return self

class DescribeSecurityProxyResourcesResponseBodyResourceList(DaraModel):
    def __init__(
        self,
        region_no: str = None,
        vpc_list: List[main_models.DescribeSecurityProxyResourcesResponseBodyResourceListVpcList] = None,
    ):
        self.region_no = region_no
        self.vpc_list = vpc_list

    def validate(self):
        if self.vpc_list:
            for v1 in self.vpc_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        result['VpcList'] = []
        if self.vpc_list is not None:
            for k1 in self.vpc_list:
                result['VpcList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        self.vpc_list = []
        if m.get('VpcList') is not None:
            for k1 in m.get('VpcList'):
                temp_model = main_models.DescribeSecurityProxyResourcesResponseBodyResourceListVpcList()
                self.vpc_list.append(temp_model.from_map(k1))

        return self

class DescribeSecurityProxyResourcesResponseBodyResourceListVpcList(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        member_uid: str = None,
        nat_gateways: List[main_models.DescribeSecurityProxyResourcesResponseBodyResourceListVpcListNatGateways] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.member_uid = member_uid
        self.nat_gateways = nat_gateways
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        if self.nat_gateways:
            for v1 in self.nat_gateways:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        result['NatGateways'] = []
        if self.nat_gateways is not None:
            for k1 in self.nat_gateways:
                result['NatGateways'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        self.nat_gateways = []
        if m.get('NatGateways') is not None:
            for k1 in m.get('NatGateways'):
                temp_model = main_models.DescribeSecurityProxyResourcesResponseBodyResourceListVpcListNatGateways()
                self.nat_gateways.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeSecurityProxyResourcesResponseBodyResourceListVpcListNatGateways(DaraModel):
    def __init__(
        self,
        detail: str = None,
        nat_gateway_id: str = None,
        nat_gateway_name: str = None,
        nat_route_entry_list: List[main_models.DescribeSecurityProxyResourcesResponseBodyResourceListVpcListNatGatewaysNatRouteEntryList] = None,
        status: str = None,
    ):
        self.detail = detail
        self.nat_gateway_id = nat_gateway_id
        self.nat_gateway_name = nat_gateway_name
        self.nat_route_entry_list = nat_route_entry_list
        self.status = status

    def validate(self):
        if self.nat_route_entry_list:
            for v1 in self.nat_route_entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_name is not None:
            result['NatGatewayName'] = self.nat_gateway_name

        result['NatRouteEntryList'] = []
        if self.nat_route_entry_list is not None:
            for k1 in self.nat_route_entry_list:
                result['NatRouteEntryList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayName') is not None:
            self.nat_gateway_name = m.get('NatGatewayName')

        self.nat_route_entry_list = []
        if m.get('NatRouteEntryList') is not None:
            for k1 in m.get('NatRouteEntryList'):
                temp_model = main_models.DescribeSecurityProxyResourcesResponseBodyResourceListVpcListNatGatewaysNatRouteEntryList()
                self.nat_route_entry_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeSecurityProxyResourcesResponseBodyResourceListVpcListNatGatewaysNatRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        route_table_id: str = None,
    ):
        self.destination_cidr = destination_cidr
        self.next_hop_id = next_hop_id
        self.next_hop_type = next_hop_type
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

