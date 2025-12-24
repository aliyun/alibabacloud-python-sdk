# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeVirtualBorderRoutersResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        virtual_border_router_set: main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSet = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.virtual_border_router_set = virtual_border_router_set

    def validate(self):
        if self.virtual_border_router_set:
            self.virtual_border_router_set.validate()

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.virtual_border_router_set is not None:
            result['VirtualBorderRouterSet'] = self.virtual_border_router_set.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VirtualBorderRouterSet') is not None:
            temp_model = main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSet()
            self.virtual_border_router_set = temp_model.from_map(m.get('VirtualBorderRouterSet'))

        return self

class DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSet(DaraModel):
    def __init__(
        self,
        virtual_border_router_type: List[main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterType] = None,
    ):
        self.virtual_border_router_type = virtual_border_router_type

    def validate(self):
        if self.virtual_border_router_type:
            for v1 in self.virtual_border_router_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VirtualBorderRouterType'] = []
        if self.virtual_border_router_type is not None:
            for k1 in self.virtual_border_router_type:
                result['VirtualBorderRouterType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.virtual_border_router_type = []
        if m.get('VirtualBorderRouterType') is not None:
            for k1 in m.get('VirtualBorderRouterType'):
                temp_model = main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterType()
                self.virtual_border_router_type.append(temp_model.from_map(k1))

        return self

class DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterType(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        activation_time: str = None,
        circuit_code: str = None,
        creation_time: str = None,
        description: str = None,
        local_gateway_ip: str = None,
        name: str = None,
        peer_gateway_ip: str = None,
        peering_subnet_mask: str = None,
        physical_connection_business_status: str = None,
        physical_connection_id: str = None,
        physical_connection_owner_uid: str = None,
        physical_connection_status: str = None,
        recovery_time: str = None,
        route_table_id: str = None,
        status: str = None,
        termination_time: str = None,
        vbr_id: str = None,
        vlan_id: int = None,
        vlan_interface_id: str = None,
    ):
        self.access_point_id = access_point_id
        self.activation_time = activation_time
        self.circuit_code = circuit_code
        self.creation_time = creation_time
        self.description = description
        self.local_gateway_ip = local_gateway_ip
        self.name = name
        self.peer_gateway_ip = peer_gateway_ip
        self.peering_subnet_mask = peering_subnet_mask
        self.physical_connection_business_status = physical_connection_business_status
        self.physical_connection_id = physical_connection_id
        self.physical_connection_owner_uid = physical_connection_owner_uid
        self.physical_connection_status = physical_connection_status
        self.recovery_time = recovery_time
        self.route_table_id = route_table_id
        self.status = status
        self.termination_time = termination_time
        self.vbr_id = vbr_id
        self.vlan_id = vlan_id
        self.vlan_interface_id = vlan_interface_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.activation_time is not None:
            result['ActivationTime'] = self.activation_time

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip

        if self.name is not None:
            result['Name'] = self.name

        if self.peer_gateway_ip is not None:
            result['PeerGatewayIp'] = self.peer_gateway_ip

        if self.peering_subnet_mask is not None:
            result['PeeringSubnetMask'] = self.peering_subnet_mask

        if self.physical_connection_business_status is not None:
            result['PhysicalConnectionBusinessStatus'] = self.physical_connection_business_status

        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id

        if self.physical_connection_owner_uid is not None:
            result['PhysicalConnectionOwnerUid'] = self.physical_connection_owner_uid

        if self.physical_connection_status is not None:
            result['PhysicalConnectionStatus'] = self.physical_connection_status

        if self.recovery_time is not None:
            result['RecoveryTime'] = self.recovery_time

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.status is not None:
            result['Status'] = self.status

        if self.termination_time is not None:
            result['TerminationTime'] = self.termination_time

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        if self.vlan_interface_id is not None:
            result['VlanInterfaceId'] = self.vlan_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('ActivationTime') is not None:
            self.activation_time = m.get('ActivationTime')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PeerGatewayIp') is not None:
            self.peer_gateway_ip = m.get('PeerGatewayIp')

        if m.get('PeeringSubnetMask') is not None:
            self.peering_subnet_mask = m.get('PeeringSubnetMask')

        if m.get('PhysicalConnectionBusinessStatus') is not None:
            self.physical_connection_business_status = m.get('PhysicalConnectionBusinessStatus')

        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')

        if m.get('PhysicalConnectionOwnerUid') is not None:
            self.physical_connection_owner_uid = m.get('PhysicalConnectionOwnerUid')

        if m.get('PhysicalConnectionStatus') is not None:
            self.physical_connection_status = m.get('PhysicalConnectionStatus')

        if m.get('RecoveryTime') is not None:
            self.recovery_time = m.get('RecoveryTime')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TerminationTime') is not None:
            self.termination_time = m.get('TerminationTime')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        if m.get('VlanInterfaceId') is not None:
            self.vlan_interface_id = m.get('VlanInterfaceId')

        return self

