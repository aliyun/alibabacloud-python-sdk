# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVirtualBorderRoutersForPhysicalConnectionResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        virtual_border_router_for_physical_connection_set: main_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSet = None,
    ):
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count
        # The information about VBRs.
        self.virtual_border_router_for_physical_connection_set = virtual_border_router_for_physical_connection_set

    def validate(self):
        if self.virtual_border_router_for_physical_connection_set:
            self.virtual_border_router_for_physical_connection_set.validate()

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

        if self.virtual_border_router_for_physical_connection_set is not None:
            result['VirtualBorderRouterForPhysicalConnectionSet'] = self.virtual_border_router_for_physical_connection_set.to_map()

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

        if m.get('VirtualBorderRouterForPhysicalConnectionSet') is not None:
            temp_model = main_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSet()
            self.virtual_border_router_for_physical_connection_set = temp_model.from_map(m.get('VirtualBorderRouterForPhysicalConnectionSet'))

        return self

class DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSet(DaraModel):
    def __init__(
        self,
        virtual_border_router_for_physical_connection_type: List[main_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType] = None,
    ):
        self.virtual_border_router_for_physical_connection_type = virtual_border_router_for_physical_connection_type

    def validate(self):
        if self.virtual_border_router_for_physical_connection_type:
            for v1 in self.virtual_border_router_for_physical_connection_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VirtualBorderRouterForPhysicalConnectionType'] = []
        if self.virtual_border_router_for_physical_connection_type is not None:
            for k1 in self.virtual_border_router_for_physical_connection_type:
                result['VirtualBorderRouterForPhysicalConnectionType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.virtual_border_router_for_physical_connection_type = []
        if m.get('VirtualBorderRouterForPhysicalConnectionType') is not None:
            for k1 in m.get('VirtualBorderRouterForPhysicalConnectionType'):
                temp_model = main_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType()
                self.virtual_border_router_for_physical_connection_type.append(temp_model.from_map(k1))

        return self

class DescribeVirtualBorderRoutersForPhysicalConnectionResponseBodyVirtualBorderRouterForPhysicalConnectionSetVirtualBorderRouterForPhysicalConnectionType(DaraModel):
    def __init__(
        self,
        activation_time: str = None,
        bandwidth: str = None,
        bandwidth_status: str = None,
        circuit_code: str = None,
        creation_time: str = None,
        ecc_id: str = None,
        enable_ipv_6: bool = None,
        local_gateway_ip: str = None,
        local_ipv_6gateway_ip: str = None,
        pconn_vbr_bussiness_status: str = None,
        pconn_vbr_charge_type: str = None,
        pconn_vbr_expire_time: str = None,
        peer_gateway_ip: str = None,
        peer_ipv_6gateway_ip: str = None,
        peering_ipv_6subnet_mask: str = None,
        peering_subnet_mask: str = None,
        recovery_time: str = None,
        status: str = None,
        termination_time: str = None,
        type: str = None,
        vbr_id: str = None,
        vbr_owner_uid: int = None,
        vlan_id: int = None,
    ):
        # The time when the VBR was first activated.
        self.activation_time = activation_time
        # The bandwidth of the VBR that is associated with the Express Connect circuit. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The status of the bandwidth. Valid values:
        # 
        # *   **Active**
        # *   **Inactive**
        self.bandwidth_status = bandwidth_status
        # The circuit code of the Express Connect circuit. The circuit code is provided by the connectivity provider.
        self.circuit_code = circuit_code
        # The time when the VBR was created.
        self.creation_time = creation_time
        # The ID of the ECC instance.
        self.ecc_id = ecc_id
        # Indicates whether IPv6 is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_ipv_6 = enable_ipv_6
        # The IPv4 address of the gateway device on the Alibaba Cloud side.
        self.local_gateway_ip = local_gateway_ip
        # The IPv6 address of the gateway device on the Alibaba Cloud side.
        self.local_ipv_6gateway_ip = local_ipv_6gateway_ip
        # The status of the VBR associated with the Express Connect circuit. Valid values:
        # 
        # *   **Normal**
        # *   **FinancialLocked**
        self.pconn_vbr_bussiness_status = pconn_vbr_bussiness_status
        # The billing method of the VBR. Valid values:
        # 
        # *   **PrePaid**: subscription. If you choose this billing method, make sure that your Apsara Stack account supports balance payments or credit payments.
        # *   **PostPaid**: pay-as-you-go.
        self.pconn_vbr_charge_type = pconn_vbr_charge_type
        # The time when the VBR associated with the Express Connect circuit expires.
        self.pconn_vbr_expire_time = pconn_vbr_expire_time
        # The IPv4 address of the gateway device on the user side.
        self.peer_gateway_ip = peer_gateway_ip
        # The IPv6 address of the gateway device on the user side.
        # 
        # This parameter is required when you create a VBR for the owner of the Express Connect circuit. You can ignore this parameter when you create a VBR for another Alibaba Cloud account.
        self.peer_ipv_6gateway_ip = peer_ipv_6gateway_ip
        # The subnet mask for the IPv6 addresses of the gateway devices on the Alibaba Cloud side and on the user side.
        # 
        # The two IPv6 addresses must fall within the same subnet.
        self.peering_ipv_6subnet_mask = peering_ipv_6subnet_mask
        # The subnet mask of the IPv4 addresses configured on the user side and Alibaba Cloud side.
        # 
        # The two IPv4 addresses must fall within the same subnet.
        self.peering_subnet_mask = peering_subnet_mask
        # The last time when the status of the VBR changed from Terminated to Active.
        self.recovery_time = recovery_time
        # The status of the VBR. Valid values:
        # 
        # *   **unconfirmed**
        # *   **active**
        # *   **terminating**
        # *   **terminated**
        # *   **recovering**
        # *   **deleting**
        self.status = status
        # The last time when the VBR was disabled.
        self.termination_time = termination_time
        # The VBR type.
        self.type = type
        # The VBR ID.
        self.vbr_id = vbr_id
        # The ID of the Alibaba Cloud account to which the VBR belongs.
        # 
        # If the owner of the VBR is the same as that of the Express Connect circuit, this parameter is empty.
        self.vbr_owner_uid = vbr_owner_uid
        # The VLAN ID of the VBR.
        self.vlan_id = vlan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation_time is not None:
            result['ActivationTime'] = self.activation_time

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_status is not None:
            result['BandwidthStatus'] = self.bandwidth_status

        if self.circuit_code is not None:
            result['CircuitCode'] = self.circuit_code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.ecc_id is not None:
            result['EccId'] = self.ecc_id

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.local_gateway_ip is not None:
            result['LocalGatewayIp'] = self.local_gateway_ip

        if self.local_ipv_6gateway_ip is not None:
            result['LocalIpv6GatewayIp'] = self.local_ipv_6gateway_ip

        if self.pconn_vbr_bussiness_status is not None:
            result['PConnVbrBussinessStatus'] = self.pconn_vbr_bussiness_status

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

        if self.recovery_time is not None:
            result['RecoveryTime'] = self.recovery_time

        if self.status is not None:
            result['Status'] = self.status

        if self.termination_time is not None:
            result['TerminationTime'] = self.termination_time

        if self.type is not None:
            result['Type'] = self.type

        if self.vbr_id is not None:
            result['VbrId'] = self.vbr_id

        if self.vbr_owner_uid is not None:
            result['VbrOwnerUid'] = self.vbr_owner_uid

        if self.vlan_id is not None:
            result['VlanId'] = self.vlan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationTime') is not None:
            self.activation_time = m.get('ActivationTime')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthStatus') is not None:
            self.bandwidth_status = m.get('BandwidthStatus')

        if m.get('CircuitCode') is not None:
            self.circuit_code = m.get('CircuitCode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('EccId') is not None:
            self.ecc_id = m.get('EccId')

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('LocalGatewayIp') is not None:
            self.local_gateway_ip = m.get('LocalGatewayIp')

        if m.get('LocalIpv6GatewayIp') is not None:
            self.local_ipv_6gateway_ip = m.get('LocalIpv6GatewayIp')

        if m.get('PConnVbrBussinessStatus') is not None:
            self.pconn_vbr_bussiness_status = m.get('PConnVbrBussinessStatus')

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

        if m.get('RecoveryTime') is not None:
            self.recovery_time = m.get('RecoveryTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TerminationTime') is not None:
            self.termination_time = m.get('TerminationTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VbrId') is not None:
            self.vbr_id = m.get('VbrId')

        if m.get('VbrOwnerUid') is not None:
            self.vbr_owner_uid = m.get('VbrOwnerUid')

        if m.get('VlanId') is not None:
            self.vlan_id = m.get('VlanId')

        return self

