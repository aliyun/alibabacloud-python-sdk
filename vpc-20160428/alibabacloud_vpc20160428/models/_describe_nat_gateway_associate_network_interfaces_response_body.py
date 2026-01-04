# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeNatGatewayAssociateNetworkInterfacesResponseBody(DaraModel):
    def __init__(
        self,
        associate_network_interfaces: main_models.DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfaces = None,
        count: int = None,
        max_results: int = None,
        nat_gateway_id: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ENIs associated with the VPC NAT gateway.
        self.associate_network_interfaces = associate_network_interfaces
        # Number of associated ENIs.
        self.count = count
        # The number of entries to return per page. Valid values: **1 to 100**. Default value: **20**.
        self.max_results = max_results
        # The ID of the VPC NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # Indicates whether the token for the next query exists. Valid value:
        # 
        # *   If **NextToken** is empty, there is no next page.
        # *   If the value returned of **NextToken** is not empty, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.associate_network_interfaces:
            self.associate_network_interfaces.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associate_network_interfaces is not None:
            result['AssociateNetworkInterfaces'] = self.associate_network_interfaces.to_map()

        if self.count is not None:
            result['Count'] = self.count

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociateNetworkInterfaces') is not None:
            temp_model = main_models.DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfaces()
            self.associate_network_interfaces = temp_model.from_map(m.get('AssociateNetworkInterfaces'))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfaces(DaraModel):
    def __init__(
        self,
        associate_network_interface: List[main_models.DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfacesAssociateNetworkInterface] = None,
    ):
        self.associate_network_interface = associate_network_interface

    def validate(self):
        if self.associate_network_interface:
            for v1 in self.associate_network_interface:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssociateNetworkInterface'] = []
        if self.associate_network_interface is not None:
            for k1 in self.associate_network_interface:
                result['AssociateNetworkInterface'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associate_network_interface = []
        if m.get('AssociateNetworkInterface') is not None:
            for k1 in m.get('AssociateNetworkInterface'):
                temp_model = main_models.DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfacesAssociateNetworkInterface()
                self.associate_network_interface.append(temp_model.from_map(k1))

        return self

class DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfacesAssociateNetworkInterface(DaraModel):
    def __init__(
        self,
        ipv_4sets: main_models.DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfacesAssociateNetworkInterfaceIPv4Sets = None,
        network_interface_id: str = None,
        resource_id: str = None,
        resource_owner_id: str = None,
        resource_type: str = None,
        resource_vpc_id: str = None,
        tunnel_index: str = None,
    ):
        # The IPv4 addresses of the ENIs.
        self.ipv_4sets = ipv_4sets
        # The ID of the ENI.
        self.network_interface_id = network_interface_id
        # The ID of the service resource.
        self.resource_id = resource_id
        # The UID of the account to which the service resource belongs.
        self.resource_owner_id = resource_owner_id
        # The type of the service resource.
        self.resource_type = resource_type
        self.resource_vpc_id = resource_vpc_id
        # The ID of the tunnel index.
        self.tunnel_index = tunnel_index

    def validate(self):
        if self.ipv_4sets:
            self.ipv_4sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4sets is not None:
            result['IPv4Sets'] = self.ipv_4sets.to_map()

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_vpc_id is not None:
            result['ResourceVpcId'] = self.resource_vpc_id

        if self.tunnel_index is not None:
            result['TunnelIndex'] = self.tunnel_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPv4Sets') is not None:
            temp_model = main_models.DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfacesAssociateNetworkInterfaceIPv4Sets()
            self.ipv_4sets = temp_model.from_map(m.get('IPv4Sets'))

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceVpcId') is not None:
            self.resource_vpc_id = m.get('ResourceVpcId')

        if m.get('TunnelIndex') is not None:
            self.tunnel_index = m.get('TunnelIndex')

        return self

class DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfacesAssociateNetworkInterfaceIPv4Sets(DaraModel):
    def __init__(
        self,
        ipv_4set: List[main_models.DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfacesAssociateNetworkInterfaceIPv4SetsIPv4Set] = None,
    ):
        self.ipv_4set = ipv_4set

    def validate(self):
        if self.ipv_4set:
            for v1 in self.ipv_4set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IPv4Set'] = []
        if self.ipv_4set is not None:
            for k1 in self.ipv_4set:
                result['IPv4Set'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_4set = []
        if m.get('IPv4Set') is not None:
            for k1 in m.get('IPv4Set'):
                temp_model = main_models.DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfacesAssociateNetworkInterfaceIPv4SetsIPv4Set()
                self.ipv_4set.append(temp_model.from_map(k1))

        return self

class DescribeNatGatewayAssociateNetworkInterfacesResponseBodyAssociateNetworkInterfacesAssociateNetworkInterfaceIPv4SetsIPv4Set(DaraModel):
    def __init__(
        self,
        ipv_4address: str = None,
        primary: bool = None,
    ):
        # The primary private IP address of the ENI.
        self.ipv_4address = ipv_4address
        # Indicates whether the IP address is the primary private IP address. Valid values:
        # 
        # *   true: Primary private IP address
        # *   false: Secondary private IP addresses
        self.primary = primary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4address is not None:
            result['IPv4Address'] = self.ipv_4address

        if self.primary is not None:
            result['Primary'] = self.primary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPv4Address') is not None:
            self.ipv_4address = m.get('IPv4Address')

        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        return self

