# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallCenDetailResponseBody(DaraModel):
    def __init__(
        self,
        connect_type: str = None,
        firewall_switch_status: str = None,
        firewall_vpc: main_models.DescribeVpcFirewallCenDetailResponseBodyFirewallVpc = None,
        local_vpc: main_models.DescribeVpcFirewallCenDetailResponseBodyLocalVpc = None,
        request_id: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The connection type of the VPC firewall. The value is fixed as **cen**, which indicates CEN instances.
        self.connect_type = connect_type
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: enabled
        # *   **closed**: disabled
        # *   **notconfigured**: not configured
        self.firewall_switch_status = firewall_switch_status
        # The firewall VPC.
        self.firewall_vpc = firewall_vpc
        # The details about the VPC.
        self.local_vpc = local_vpc
        # The ID of the request.
        self.request_id = request_id
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        if self.firewall_vpc:
            self.firewall_vpc.validate()
        if self.local_vpc:
            self.local_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status

        if self.firewall_vpc is not None:
            result['FirewallVpc'] = self.firewall_vpc.to_map()

        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')

        if m.get('FirewallVpc') is not None:
            temp_model = main_models.DescribeVpcFirewallCenDetailResponseBodyFirewallVpc()
            self.firewall_vpc = temp_model.from_map(m.get('FirewallVpc'))

        if m.get('LocalVpc') is not None:
            temp_model = main_models.DescribeVpcFirewallCenDetailResponseBodyLocalVpc()
            self.local_vpc = temp_model.from_map(m.get('LocalVpc'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        return self

class DescribeVpcFirewallCenDetailResponseBodyLocalVpc(DaraModel):
    def __init__(
        self,
        attachment_id: str = None,
        attachment_name: str = None,
        defend_cidr_list: List[str] = None,
        eni_list: List[main_models.DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList] = None,
        manual_vswitch_id: str = None,
        network_instance_id: str = None,
        network_instance_name: str = None,
        network_instance_type: str = None,
        owner_id: str = None,
        region_no: str = None,
        route_mode: str = None,
        support_manual_mode: str = None,
        transit_router_id: str = None,
        transit_router_type: str = None,
        vpc_cidr_table_list: List[main_models.DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The ID of the connection between two network instances.
        self.attachment_id = attachment_id
        # The name of the connection between two network instances.
        self.attachment_name = attachment_name
        # An array consisting of the CIDR blocks that are protected by the VPC firewall.
        self.defend_cidr_list = defend_cidr_list
        # The Elastic Network Interfaces (ENIs).
        self.eni_list = eni_list
        # The ID of the specified vSwitch when the routing mode is manual.
        self.manual_vswitch_id = manual_vswitch_id
        # The ID of the VPC for which the VPC firewall is created.
        self.network_instance_id = network_instance_id
        # The name of the network instance.
        self.network_instance_name = network_instance_name
        # The type of the network instance. The value is fixed as **VPC**.
        self.network_instance_type = network_instance_type
        # The UID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id
        # The ID of the region in which the VPC resides.
        self.region_no = region_no
        # The routing mode. Valid values:
        # 
        # *   auto: automatic mode
        # *   manual: manual mode
        self.route_mode = route_mode
        # Indicates whether the manual routing mode is supported. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.support_manual_mode = support_manual_mode
        # The instance ID of the CEN transit router.
        self.transit_router_id = transit_router_id
        # The edition of the CEN transit router. Valid values:
        # 
        # *   **Basic**: Basic Edition
        # *   **Enterprise**: Enterprise Edition
        self.transit_router_type = transit_router_type
        # An array that consists of the CIDR blocks of the VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.eni_list:
            for v1 in self.eni_list:
                 if v1:
                    v1.validate()
        if self.vpc_cidr_table_list:
            for v1 in self.vpc_cidr_table_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id

        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name

        if self.defend_cidr_list is not None:
            result['DefendCidrList'] = self.defend_cidr_list

        result['EniList'] = []
        if self.eni_list is not None:
            for k1 in self.eni_list:
                result['EniList'].append(k1.to_map() if k1 else None)

        if self.manual_vswitch_id is not None:
            result['ManualVSwitchId'] = self.manual_vswitch_id

        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name

        if self.network_instance_type is not None:
            result['NetworkInstanceType'] = self.network_instance_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode

        if self.support_manual_mode is not None:
            result['SupportManualMode'] = self.support_manual_mode

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type

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
        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')

        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')

        if m.get('DefendCidrList') is not None:
            self.defend_cidr_list = m.get('DefendCidrList')

        self.eni_list = []
        if m.get('EniList') is not None:
            for k1 in m.get('EniList'):
                temp_model = main_models.DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList()
                self.eni_list.append(temp_model.from_map(k1))

        if m.get('ManualVSwitchId') is not None:
            self.manual_vswitch_id = m.get('ManualVSwitchId')

        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')

        if m.get('NetworkInstanceType') is not None:
            self.network_instance_type = m.get('NetworkInstanceType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')

        if m.get('SupportManualMode') is not None:
            self.support_manual_mode = m.get('SupportManualMode')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')

        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k1 in m.get('VpcCidrTableList'):
                temp_model = main_models.DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableList(DaraModel):
    def __init__(
        self,
        route_entry_list: List[main_models.DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # The route entries for the VPC.
        self.route_entry_list = route_entry_list
        # The route table ID of the VPC.
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
                temp_model = main_models.DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k1))

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class DescribeVpcFirewallCenDetailResponseBodyLocalVpcVpcCidrTableListRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the VPC.
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

class DescribeVpcFirewallCenDetailResponseBodyLocalVpcEniList(DaraModel):
    def __init__(
        self,
        eni_id: str = None,
        eni_private_ip_address: str = None,
        eni_vswitch_id: str = None,
    ):
        # The ID of the ENI that belongs to the VPC.
        self.eni_id = eni_id
        # The private IP address of the ENI that belongs to the VPC.
        self.eni_private_ip_address = eni_private_ip_address
        # The ID of the vSwitch to which the ENI is connected.
        self.eni_vswitch_id = eni_vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eni_id is not None:
            result['EniId'] = self.eni_id

        if self.eni_private_ip_address is not None:
            result['EniPrivateIpAddress'] = self.eni_private_ip_address

        if self.eni_vswitch_id is not None:
            result['EniVSwitchId'] = self.eni_vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')

        if m.get('EniPrivateIpAddress') is not None:
            self.eni_private_ip_address = m.get('EniPrivateIpAddress')

        if m.get('EniVSwitchId') is not None:
            self.eni_vswitch_id = m.get('EniVSwitchId')

        return self

class DescribeVpcFirewallCenDetailResponseBodyFirewallVpc(DaraModel):
    def __init__(
        self,
        allow_configuration: int = None,
        standby_zone_id: str = None,
        vpc_cidr: str = None,
        vpc_id: str = None,
        vswitch_cidr: str = None,
        vswitch_id: str = None,
        vswitch_zone_id: str = None,
        zone_id: str = None,
    ):
        # Indicates whether you can specify a CIDR block when you create a VPC firewall for a Basic Edition transit router of a CEN instance. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.allow_configuration = allow_configuration
        # Firewall backup availability zone ID.
        self.standby_zone_id = standby_zone_id
        # The CIDR block of the VPC.
        self.vpc_cidr = vpc_cidr
        # The VPC ID.
        self.vpc_id = vpc_id
        # The CIDR block of the vSwitch.
        self.vswitch_cidr = vswitch_cidr
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The availability zone ID of the virtual switch.
        self.vswitch_zone_id = vswitch_zone_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_configuration is not None:
            result['AllowConfiguration'] = self.allow_configuration

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.vpc_cidr is not None:
            result['VpcCidr'] = self.vpc_cidr

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_cidr is not None:
            result['VswitchCidr'] = self.vswitch_cidr

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.vswitch_zone_id is not None:
            result['VswitchZoneId'] = self.vswitch_zone_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowConfiguration') is not None:
            self.allow_configuration = m.get('AllowConfiguration')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('VpcCidr') is not None:
            self.vpc_cidr = m.get('VpcCidr')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchCidr') is not None:
            self.vswitch_cidr = m.get('VswitchCidr')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('VswitchZoneId') is not None:
            self.vswitch_zone_id = m.get('VswitchZoneId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

