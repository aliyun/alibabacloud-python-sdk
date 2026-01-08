# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallDetailResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        connect_type: str = None,
        firewall_switch_status: str = None,
        local_vpc: main_models.DescribeVpcFirewallDetailResponseBodyLocalVpc = None,
        member_uid: str = None,
        peer_vpc: main_models.DescribeVpcFirewallDetailResponseBodyPeerVpc = None,
        request_id: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The bandwidth of the Express Connect circuit. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The connection type of the VPC firewall. The value is fixed as **expressconnect**, which indicates Express Connect circuits.
        self.connect_type = connect_type
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        # *   **configured**: The VPC firewall is configured.
        self.firewall_switch_status = firewall_switch_status
        # The details about the local VPC.
        self.local_vpc = local_vpc
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The details about the peer VPC.
        self.peer_vpc = peer_vpc
        # The ID of the request.
        self.request_id = request_id
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        if self.local_vpc:
            self.local_vpc.validate()
        if self.peer_vpc:
            self.peer_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status

        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.peer_vpc is not None:
            result['PeerVpc'] = self.peer_vpc.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')

        if m.get('LocalVpc') is not None:
            temp_model = main_models.DescribeVpcFirewallDetailResponseBodyLocalVpc()
            self.local_vpc = temp_model.from_map(m.get('LocalVpc'))

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PeerVpc') is not None:
            temp_model = main_models.DescribeVpcFirewallDetailResponseBodyPeerVpc()
            self.peer_vpc = temp_model.from_map(m.get('PeerVpc'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        return self

class DescribeVpcFirewallDetailResponseBodyPeerVpc(DaraModel):
    def __init__(
        self,
        eni_id: str = None,
        eni_private_ip_address: str = None,
        region_no: str = None,
        router_interface_id: str = None,
        vpc_cidr_table_list: List[main_models.DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The ID of the ENI for the peer VPC.
        self.eni_id = eni_id
        # The private IP address of the ENI for the peer VPC.
        self.eni_private_ip_address = eni_private_ip_address
        # The region ID of the peer VPC.
        self.region_no = region_no
        # The router interface ID of the peer VPC.
        self.router_interface_id = router_interface_id
        # The CIDR blocks of the peer VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the peer VPC.
        self.vpc_id = vpc_id
        # The name of the peer VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.vpc_cidr_table_list:
            for v1 in self.vpc_cidr_table_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eni_id is not None:
            result['EniId'] = self.eni_id

        if self.eni_private_ip_address is not None:
            result['EniPrivateIpAddress'] = self.eni_private_ip_address

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id

        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k1 in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')

        if m.get('EniPrivateIpAddress') is not None:
            self.eni_private_ip_address = m.get('EniPrivateIpAddress')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')

        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k1 in m.get('VpcCidrTableList'):
                temp_model = main_models.DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableList(DaraModel):
    def __init__(
        self,
        route_entry_list: List[main_models.DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # The route entries of the peer VPC.
        self.route_entry_list = route_entry_list
        # The ID of the route table for the peer VPC.
        self.route_table_id = route_table_id

    def validate(self):
        if self.route_entry_list:
            for v1 in self.route_entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k1 in self.route_entry_list:
                result['RouteEntryList'].append(k1.to_map() if k1 else None)

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k1 in m.get('RouteEntryList'):
                temp_model = main_models.DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k1))

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class DescribeVpcFirewallDetailResponseBodyPeerVpcVpcCidrTableListRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the peer VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the peer VPC.
        self.next_hop_instance_id = next_hop_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')

        return self

class DescribeVpcFirewallDetailResponseBodyLocalVpc(DaraModel):
    def __init__(
        self,
        eni_id: str = None,
        eni_private_ip_address: str = None,
        region_no: str = None,
        router_interface_id: str = None,
        vpc_cidr_table_list: List[main_models.DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The ID of the ENI for the local VPC.
        self.eni_id = eni_id
        # The private IP address of the elastic network interface (ENI) for the local VPC.
        self.eni_private_ip_address = eni_private_ip_address
        # The region ID of the local VPC.
        self.region_no = region_no
        # The router interface ID of the local VPC.
        self.router_interface_id = router_interface_id
        # The CIDR blocks of the local VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the local VPC.
        self.vpc_id = vpc_id
        # The name of the local VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.vpc_cidr_table_list:
            for v1 in self.vpc_cidr_table_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eni_id is not None:
            result['EniId'] = self.eni_id

        if self.eni_private_ip_address is not None:
            result['EniPrivateIpAddress'] = self.eni_private_ip_address

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id

        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k1 in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')

        if m.get('EniPrivateIpAddress') is not None:
            self.eni_private_ip_address = m.get('EniPrivateIpAddress')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')

        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k1 in m.get('VpcCidrTableList'):
                temp_model = main_models.DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableList(DaraModel):
    def __init__(
        self,
        route_entry_list: List[main_models.DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # The route entries of the local VPC.
        self.route_entry_list = route_entry_list
        # The ID of the route table for the local VPC.
        self.route_table_id = route_table_id

    def validate(self):
        if self.route_entry_list:
            for v1 in self.route_entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k1 in self.route_entry_list:
                result['RouteEntryList'].append(k1.to_map() if k1 else None)

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k1 in m.get('RouteEntryList'):
                temp_model = main_models.DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k1))

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class DescribeVpcFirewallDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the local VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the local VPC.
        self.next_hop_instance_id = next_hop_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')

        return self

