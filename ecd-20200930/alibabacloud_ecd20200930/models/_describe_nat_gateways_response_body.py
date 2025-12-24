# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeNatGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        nat_gateways: List[main_models.DescribeNatGatewaysResponseBodyNatGateways] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.max_results = max_results
        self.nat_gateways = nat_gateways
        self.next_token = next_token
        self.request_id = request_id

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['NatGateways'] = []
        if self.nat_gateways is not None:
            for k1 in self.nat_gateways:
                result['NatGateways'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.nat_gateways = []
        if m.get('NatGateways') is not None:
            for k1 in m.get('NatGateways'):
                temp_model = main_models.DescribeNatGatewaysResponseBodyNatGateways()
                self.nat_gateways.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNatGatewaysResponseBodyNatGateways(DaraModel):
    def __init__(
        self,
        forward_table_ids: List[str] = None,
        ip_lists: List[main_models.DescribeNatGatewaysResponseBodyNatGatewaysIpLists] = None,
        name: str = None,
        nat_gateway_id: str = None,
        snat_table_ids: List[str] = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.forward_table_ids = forward_table_ids
        self.ip_lists = ip_lists
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        self.snat_table_ids = snat_table_ids
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        if self.ip_lists:
            for v1 in self.ip_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_table_ids is not None:
            result['ForwardTableIds'] = self.forward_table_ids

        result['IpLists'] = []
        if self.ip_lists is not None:
            for k1 in self.ip_lists:
                result['IpLists'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.snat_table_ids is not None:
            result['SnatTableIds'] = self.snat_table_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardTableIds') is not None:
            self.forward_table_ids = m.get('ForwardTableIds')

        self.ip_lists = []
        if m.get('IpLists') is not None:
            for k1 in m.get('IpLists'):
                temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysIpLists()
                self.ip_lists.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('SnatTableIds') is not None:
            self.snat_table_ids = m.get('SnatTableIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysIpLists(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        ip_address: str = None,
        private_ip_address: str = None,
        snat_entry_enabled: str = None,
        using_status: str = None,
    ):
        self.allocation_id = allocation_id
        self.ip_address = ip_address
        self.private_ip_address = private_ip_address
        self.snat_entry_enabled = snat_entry_enabled
        self.using_status = using_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.snat_entry_enabled is not None:
            result['SnatEntryEnabled'] = self.snat_entry_enabled

        if self.using_status is not None:
            result['UsingStatus'] = self.using_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('SnatEntryEnabled') is not None:
            self.snat_entry_enabled = m.get('SnatEntryEnabled')

        if m.get('UsingStatus') is not None:
            self.using_status = m.get('UsingStatus')

        return self

