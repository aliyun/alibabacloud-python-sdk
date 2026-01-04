# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
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
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 50**. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count
        # The information about the VBR.
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
        associated_cens: main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCens = None,
        associated_physical_connections: main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnections = None,
        bandwidth: int = None,
        circuit_code: str = None,
        cloud_box_instance_id: str = None,
        creation_time: str = None,
        description: str = None,
        detect_multiplier: int = None,
        ecc_id: str = None,
        ecr_attatch_status: str = None,
        ecr_id: str = None,
        ecr_owner_id: str = None,
        enable_ipv_6: bool = None,
        local_gateway_ip: str = None,
        local_ipv_6gateway_ip: str = None,
        min_rx_interval: int = None,
        min_tx_interval: int = None,
        mtu: int = None,
        name: str = None,
        pconn_vbr_charge_type: str = None,
        pconn_vbr_expire_time: str = None,
        peer_gateway_ip: str = None,
        peer_ipv_6gateway_ip: str = None,
        peering_ipv_6subnet_mask: str = None,
        peering_subnet_mask: str = None,
        physical_connection_business_status: str = None,
        physical_connection_id: str = None,
        physical_connection_owner_uid: str = None,
        physical_connection_status: str = None,
        recovery_time: str = None,
        resource_group_id: str = None,
        route_table_id: str = None,
        sitelink_enable: bool = None,
        status: str = None,
        tags: main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeTags = None,
        termination_time: str = None,
        type: str = None,
        vbr_id: str = None,
        vlan_id: int = None,
        vlan_interface_id: str = None,
    ):
        # The ID of the access point.
        self.access_point_id = access_point_id
        # The time when the VBR was activated for the first time.
        self.activation_time = activation_time
        # The information about the Cloud Enterprise Network (CEN) instance to which the VBR is attached.
        self.associated_cens = associated_cens
        # The information about the Express Connect circuit that is associated with the VBR.
        self.associated_physical_connections = associated_physical_connections
        # The bandwidth value of the VBR. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The circuit code of the Express Connect circuit, which is provided by the connectivity provider.
        self.circuit_code = circuit_code
        # The ID of the cloud box.
        self.cloud_box_instance_id = cloud_box_instance_id
        # The time when the VBR was created.
        self.creation_time = creation_time
        # The description of the VBR.
        self.description = description
        # The multiple of the detection time.
        # 
        # This value indicates the maximum number of dropped packets that is allowed by the receiver when the initiator transmits packets. This value can be used to check whether the connection works as expected.
        # 
        # Valid values: **3 to 10**.
        self.detect_multiplier = detect_multiplier
        # The ID of the Express Cloud Connect (ECC) instance.
        self.ecc_id = ecc_id
        # The status of the ECR. Valid values:
        # 
        # *   **Attached**
        # *   **Attaching**
        # *   **Detached**
        # *   **Detaching**
        # *   If no value is returned, the VBR is not attached to a CEN instance.
        self.ecr_attatch_status = ecr_attatch_status
        # The ID of the Express Connect Router (ECR).
        self.ecr_id = ecr_id
        # The ID of the Alibaba Cloud account (primary account)  to which the ECR belongs.
        self.ecr_owner_id = ecr_owner_id
        # Indicates whether IPv6 is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_ipv_6 = enable_ipv_6
        # The IPv4 address of the VBR on the Alibaba Cloud side.
        self.local_gateway_ip = local_gateway_ip
        # The IPv6 address of the VBR on the Alibaba Cloud side.
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        # The time interval to receive BFD packets. Valid values: **200 to 1000**. Unit: milliseconds.
        self.min_rx_interval = min_rx_interval
        # The time interval to send Bidirectional Forwarding Detection (BFD) packets. Valid values: **200 to 1000**. Unit: milliseconds.
        self.min_tx_interval = min_tx_interval
        self.mtu = mtu
        # The VBR name.
        self.name = name
        # The billing method of the VBR. Valid values:
        # 
        # *   **PrePaid:** subscription. If you choose this billing method, make sure that your account supports balance payments or credit payments.
        # *   **PostPaid:** pay-as-you-go.
        self.pconn_vbr_charge_type = pconn_vbr_charge_type
        # The time when the VBR expires.
        self.pconn_vbr_expire_time = pconn_vbr_expire_time
        # The IPv4 address of the VBR on the user side.
        self.peer_gateway_ip = peer_gateway_ip
        # The IPv6 address of the VBR on the user side.
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        # The subnet mask for the IPv6 addresses on the user side and on the Alibaba Cloud side.
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        # The subnet mask for the IPv4 addresses on the Alibaba Cloud side and on the user side.
        self.peering_subnet_mask = peering_subnet_mask
        # The business status of the Express Connect circuit. Valid values:
        # 
        # *   **Normal:** The Express Connect circuit is running as normal.
        # *   **FinancialLocked:** The Express Connect circuit is locked due to overdue payments.
        self.physical_connection_business_status = physical_connection_business_status
        # The ID of the Express Connect circuit to which the VBR belongs.
        self.physical_connection_id = physical_connection_id
        # The ID of the account to which the Express Connect circuit belongs.
        self.physical_connection_owner_uid = physical_connection_owner_uid
        # The status of the Express Connect circuit. Valid values:
        # 
        # *   **Initial:** The application is under review.
        # *   **Approved**: The application is approved.
        # *   **Allocating**: The system is allocating resources.
        # *   **Allocated**: The Express Connect circuit is under construction.
        # *   **Confirmed**: The Express Connect circuit is to be confirmed.
        # *   **Enabled**: The Express Connect circuit is enabled.
        # *   **Rejected**: The application is rejected.
        # *   **Canceled**: The application is canceled.
        # *   **Allocation Failed:** The system failed to allocate resources.
        # *   **Terminated:** The Express Connect circuit is disabled.
        self.physical_connection_status = physical_connection_status
        # The last time when the status of the VBR changed from **terminated** to **active**.
        self.recovery_time = recovery_time
        # The resource group ID.
        # 
        # For more information about resource groups, see [Resource groups](https://help.aliyun.com/document_detail/94475.html).
        self.resource_group_id = resource_group_id
        # The ID of the route table of the VBR.
        self.route_table_id = route_table_id
        # Indicates whether to allow service access between data centers. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  If no value is returned, service access between data centers is not allowed.
        self.sitelink_enable = sitelink_enable
        # The status of the VBR. Valid values:
        # 
        # *   **unconfirmed**
        # *   **active**
        # *   **terminating**
        # *   **terminated**
        # *   **recovering**
        # *   **deleting:**
        self.status = status
        # The tag of the resource.
        self.tags = tags
        # The last time when the VBR was terminated.
        self.termination_time = termination_time
        # The VBR type.
        self.type = type
        # The VBR ID.
        self.vbr_id = vbr_id
        # The VLAN ID of the VBR.
        self.vlan_id = vlan_id
        # The ID of the VBR interface.
        self.vlan_interface_id = vlan_interface_id

    def validate(self):
        if self.associated_cens:
            self.associated_cens.validate()
        if self.associated_physical_connections:
            self.associated_physical_connections.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.activation_time is not None:
            result['ActivationTime'] = self.activation_time

        if self.associated_cens is not None:
            result['AssociatedCens'] = self.associated_cens.to_map()

        if self.associated_physical_connections is not None:
            result['AssociatedPhysicalConnections'] = self.associated_physical_connections.to_map()

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.cloud_box_instance_id is not None:
            result['CloudBoxInstanceId'] = self.cloud_box_instance_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.detect_multiplier is not None:
            result['DetectMultiplier'] = self.detect_multiplier

        if self.ecc_id is not None:
            result['EccId'] = self.ecc_id

        if self.ecr_attatch_status is not None:
            result['EcrAttatchStatus'] = self.ecr_attatch_status

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.ecr_owner_id is not None:
            result['EcrOwnerId'] = self.ecr_owner_id

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip

        if self.local_ipv_6gateway_ip is not None:
            result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip

        if self.min_rx_interval is not None:
            result['MinRxInterval'] = self.min_rx_interval

        if self.min_tx_interval is not None:
            result['MinTxInterval'] = self.min_tx_interval

        if self.mtu is not None:
            result['Mtu'] = self.mtu

        if self.name is not None:
            result['Name'] = self.name

        if self.pconn_vbr_charge_type is not None:
            result['PConnVbrChargeType'] = self.pconn_vbr_charge_type

        if self.pconn_vbr_expire_time is not None:
            result['PConnVbrExpireTime'] = self.pconn_vbr_expire_time

        if self.peer_gateway_ip is not None:
            result['PeerGatewayIp'] = self.peer_gateway_ip

        if self.peer_ipv_6gateway_ip is not None:
            result['PeerIpv6GatewayIp'] = self.peer_ipv_6gateway_ip

        if self.peering_ipv_6subnet_mask is not None:
            result['PeeringIpv6SubnetMask'] = self.peering_ipv_6subnet_mask

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.sitelink_enable is not None:
            result['SitelinkEnable'] = self.sitelink_enable

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.termination_time is not None:
            result['TerminationTime'] = self.termination_time

        if self.type is not None:
            result['Type'] = self.type

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

        if m.get('AssociatedCens') is not None:
            temp_model = main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCens()
            self.associated_cens = temp_model.from_map(m.get('AssociatedCens'))

        if m.get('AssociatedPhysicalConnections') is not None:
            temp_model = main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnections()
            self.associated_physical_connections = temp_model.from_map(m.get('AssociatedPhysicalConnections'))

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('CloudBoxInstanceId') is not None:
            self.cloud_box_instance_id = m.get('CloudBoxInstanceId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DetectMultiplier') is not None:
            self.detect_multiplier = m.get('DetectMultiplier')

        if m.get('EccId') is not None:
            self.ecc_id = m.get('EccId')

        if m.get('EcrAttatchStatus') is not None:
            self.ecr_attatch_status = m.get('EcrAttatchStatus')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('EcrOwnerId') is not None:
            self.ecr_owner_id = m.get('EcrOwnerId')

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')

        if m.get('LocalIpv6GatewayIp') is not None:
            self.local_ipv_6gateway_ip = m.get('LocalIpv6GatewayIp')

        if m.get('MinRxInterval') is not None:
            self.min_rx_interval = m.get('MinRxInterval')

        if m.get('MinTxInterval') is not None:
            self.min_tx_interval = m.get('MinTxInterval')

        if m.get('Mtu') is not None:
            self.mtu = m.get('Mtu')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PConnVbrChargeType') is not None:
            self.pconn_vbr_charge_type = m.get('PConnVbrChargeType')

        if m.get('PConnVbrExpireTime') is not None:
            self.pconn_vbr_expire_time = m.get('PConnVbrExpireTime')

        if m.get('PeerGatewayIp') is not None:
            self.peer_gateway_ip = m.get('PeerGatewayIp')

        if m.get('PeerIpv6GatewayIp') is not None:
            self.peer_ipv_6gateway_ip = m.get('PeerIpv6GatewayIp')

        if m.get('PeeringIpv6SubnetMask') is not None:
            self.peering_ipv_6subnet_mask = m.get('PeeringIpv6SubnetMask')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('SitelinkEnable') is not None:
            self.sitelink_enable = m.get('SitelinkEnable')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TerminationTime') is not None:
            self.termination_time = m.get('TerminationTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        if m.get('VlanInterfaceId') is not None:
            self.vlan_interface_id = m.get('VlanInterfaceId')

        return self

class DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeTags(DaraModel):
    def __init__(
        self,
        tags: List[main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeTagsTags] = None,
    ):
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeTagsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeTagsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        self.key = key
        # The tag value of the resource.
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

class DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnections(DaraModel):
    def __init__(
        self,
        associated_physical_connection: List[main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnectionsAssociatedPhysicalConnection] = None,
    ):
        self.associated_physical_connection = associated_physical_connection

    def validate(self):
        if self.associated_physical_connection:
            for v1 in self.associated_physical_connection:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssociatedPhysicalConnection'] = []
        if self.associated_physical_connection is not None:
            for k1 in self.associated_physical_connection:
                result['AssociatedPhysicalConnection'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_physical_connection = []
        if m.get('AssociatedPhysicalConnection') is not None:
            for k1 in m.get('AssociatedPhysicalConnection'):
                temp_model = main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnectionsAssociatedPhysicalConnection()
                self.associated_physical_connection.append(temp_model.from_map(k1))

        return self

class DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedPhysicalConnectionsAssociatedPhysicalConnection(DaraModel):
    def __init__(
        self,
        circuit_code: str = None,
        enable_ipv_6: bool = None,
        local_gateway_ip: str = None,
        local_ipv_6gateway_ip: str = None,
        peer_gateway_ip: str = None,
        peer_ipv_6gateway_ip: str = None,
        peering_ipv_6subnet_mask: str = None,
        peering_subnet_mask: str = None,
        physical_connection_business_status: str = None,
        physical_connection_id: str = None,
        physical_connection_owner_uid: str = None,
        physical_connection_status: str = None,
        status: str = None,
        vlan_id: str = None,
        vlan_interface_id: str = None,
    ):
        # The circuit code of the Express Connect circuit, which is provided by the connectivity provider.
        self.circuit_code = circuit_code
        # Indicates whether IPv6 is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_ipv_6 = enable_ipv_6
        # The IPv4 address of the VBR on the Alibaba Cloud side.
        self.local_gateway_ip = local_gateway_ip
        # The IPv6 address of the VBR on the Alibaba Cloud side.
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        # The IPv4 address of the VBR on the user side.
        self.peer_gateway_ip = peer_gateway_ip
        # The IPv6 address of the VBR on the user side.
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        # The subnet mask for the IPv6 addresses on the user side and on the Alibaba Cloud side.
        # 
        # Both IPv6 addresses must belong to the same subnet.
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        # The subnet mask for the IPv4 addresses of the VBR on the user side and on the Alibaba Cloud side.
        # 
        # Both IPv4 addresses must belong to the same subnet.
        self.peering_subnet_mask = peering_subnet_mask
        # The business status of the Express Connect circuit. Valid values:
        # 
        # *   **Normal:** The Express Connect circuit is running as normal.
        # *   **FinancialLocked:** The Express Connect circuit is locked due to overdue payments.
        self.physical_connection_business_status = physical_connection_business_status
        # The ID of the Express Connect circuit.
        self.physical_connection_id = physical_connection_id
        # The ID of the account to which the Express Connect circuit belongs.
        self.physical_connection_owner_uid = physical_connection_owner_uid
        # The status of the Express Connect circuit. Valid values:
        # 
        # *   **Initial:** The application is under review.
        # *   **Approved**: The application is approved.
        # *   **Allocating**: The system is allocating resources.
        # *   **Allocated**: The Express Connect circuit is under construction.
        # *   **Confirmed**: The Express Connect circuit is to be confirmed.
        # *   **Enabled**: The Express Connect circuit is enabled.
        # *   **Rejected**: The application is rejected.
        # *   **Canceled**: The application is canceled.
        # *   **Allocation Failed:** The system failed to allocate resources.
        # *   **Terminated:** The Express Connect circuit is disabled.
        self.physical_connection_status = physical_connection_status
        # The status of the VBR. Valid values:
        # 
        # *   **unconfirmed**
        # *   **active:**
        # *   **terminating**
        # *   **terminated**
        # *   **recovering**
        # *   **deleting:**
        self.status = status
        # The VLAN ID of the VBR.
        self.vlan_id = vlan_id
        # The ID of the VBR interface, which can be used as a next hop of a VBR route.
        self.vlan_interface_id = vlan_interface_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip

        if self.local_ipv_6gateway_ip is not None:
            result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip

        if self.peer_gateway_ip is not None:
            result['PeerGatewayIp'] = self.peer_gateway_ip

        if self.peer_ipv_6gateway_ip is not None:
            result['PeerIpv6GatewayIp'] = self.peer_ipv_6gateway_ip

        if self.peering_ipv_6subnet_mask is not None:
            result['PeeringIpv6SubnetMask'] = self.peering_ipv_6subnet_mask

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

        if self.status is not None:
            result['Status'] = self.status

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        if self.vlan_interface_id is not None:
            result['VlanInterfaceId'] = self.vlan_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')

        if m.get('LocalIpv6GatewayIp') is not None:
            self.local_ipv_6gateway_ip = m.get('LocalIpv6GatewayIp')

        if m.get('PeerGatewayIp') is not None:
            self.peer_gateway_ip = m.get('PeerGatewayIp')

        if m.get('PeerIpv6GatewayIp') is not None:
            self.peer_ipv_6gateway_ip = m.get('PeerIpv6GatewayIp')

        if m.get('PeeringIpv6SubnetMask') is not None:
            self.peering_ipv_6subnet_mask = m.get('PeeringIpv6SubnetMask')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        if m.get('VlanInterfaceId') is not None:
            self.vlan_interface_id = m.get('VlanInterfaceId')

        return self

class DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCens(DaraModel):
    def __init__(
        self,
        associated_cen: List[main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCensAssociatedCen] = None,
    ):
        self.associated_cen = associated_cen

    def validate(self):
        if self.associated_cen:
            for v1 in self.associated_cen:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssociatedCen'] = []
        if self.associated_cen is not None:
            for k1 in self.associated_cen:
                result['AssociatedCen'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_cen = []
        if m.get('AssociatedCen') is not None:
            for k1 in m.get('AssociatedCen'):
                temp_model = main_models.DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCensAssociatedCen()
                self.associated_cen.append(temp_model.from_map(k1))

        return self

class DescribeVirtualBorderRoutersResponseBodyVirtualBorderRouterSetVirtualBorderRouterTypeAssociatedCensAssociatedCen(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_owner_id: int = None,
        cen_status: str = None,
    ):
        # The CEN instance ID.
        self.cen_id = cen_id
        # The ID of the account to which the CEN instance belongs.
        self.cen_owner_id = cen_owner_id
        # The status of the CEN instance. Valid values:
        # 
        # *   **Attached**
        # *   **Attaching**
        # *   **Detached**
        # *   **Detaching**
        # *   If no value is returned, the VBR is not attached to a CEN instance.
        self.cen_status = cen_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id

        if self.cen_status is not None:
            result['CenStatus'] = self.cen_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')

        if m.get('CenStatus') is not None:
            self.cen_status = m.get('CenStatus')

        return self

