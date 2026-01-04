# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeNatGatewaysResponseBody(DaraModel):
    def __init__(
        self,
        nat_gateways: List[main_models.DescribeNatGatewaysResponseBodyNatGateways] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the NAT gateways.
        self.nat_gateways = nat_gateways
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of NAT gateways that are returned.
        self.total_count = total_count

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
        result['NatGateways'] = []
        if self.nat_gateways is not None:
            for k1 in self.nat_gateways:
                result['NatGateways'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nat_gateways = []
        if m.get('NatGateways') is not None:
            for k1 in m.get('NatGateways'):
                temp_model = main_models.DescribeNatGatewaysResponseBodyNatGateways()
                self.nat_gateways.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNatGatewaysResponseBodyNatGateways(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        ens_region_id: str = None,
        ip_lists: List[main_models.DescribeNatGatewaysResponseBodyNatGatewaysIpLists] = None,
        name: str = None,
        nat_gateway_id: str = None,
        network_id: str = None,
        spec: str = None,
        status: str = None,
        tags: List[main_models.DescribeNatGatewaysResponseBodyNatGatewaysTags] = None,
        v_switch_id: str = None,
    ):
        # The time when the NAT gateway was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The ID of the ENS node.
        self.ens_region_id = ens_region_id
        # The EIPs that are associated with the NAT gateway.
        self.ip_lists = ip_lists
        # The name of the NAT gateway.
        self.name = name
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The ID of the network.
        self.network_id = network_id
        # The type of the NAT gateway.
        self.spec = spec
        # The status of the NAT gateway. Valid values:
        # 
        # *   **Creating**: After you send a request to create a NAT gateway, the system creates the NAT gateway in the background. The NAT gateway remains in the Creating state until the operation is completed.
        # *   **Available**: The NAT gateway is in the Available state after the creation is complete.
        # *   **Deleting**: After you send a request to delete a NAT gateway, the system deletes the NAT gateway in the background. The NAT gateway remains in the Deleting state until the operation is completed.
        self.status = status
        self.tags = tags
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.ip_lists:
            for v1 in self.ip_lists:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        result['IpLists'] = []
        if self.ip_lists is not None:
            for k1 in self.ip_lists:
                result['IpLists'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        self.ip_lists = []
        if m.get('IpLists') is not None:
            for k1 in m.get('IpLists'):
                temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysIpLists()
                self.ip_lists.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeNatGatewaysResponseBodyNatGatewaysTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        tag_key: str = None,
        tag_value: str = None,
        value: str = None,
    ):
        self.key = key
        self.tag_key = tag_key
        self.tag_value = tag_value
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

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeNatGatewaysResponseBodyNatGatewaysIpLists(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        ip_address: str = None,
        using_status: str = None,
    ):
        # The ID of the EIP.
        self.allocation_id = allocation_id
        # The EIP.
        self.ip_address = ip_address
        # The association between the EIP and the Internet NAT gateway. Valid values:
        # 
        # *   **UsedByForwardTable**: The EIP is specified in a DNAT entry.
        # *   **UsedBySnatTable**: The EIP is specified in an SNAT entry.
        # *   **Idle**: The EIP is not specified in an SNAT entry or a DNAT entry.
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

        if self.using_status is not None:
            result['UsingStatus'] = self.using_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('UsingStatus') is not None:
            self.using_status = m.get('UsingStatus')

        return self

