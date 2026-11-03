# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpcFirewallCenConfigureRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        firewall_switch: str = None,
        firewall_vswitch_cidr_block: str = None,
        firewall_vswitch_zone_id: str = None,
        firewall_vpc_cidr_block: str = None,
        firewall_vpc_standby_zone_id: str = None,
        firewall_vpc_zone_id: str = None,
        lang: str = None,
        member_uid: str = None,
        network_instance_id: str = None,
        v_switch_id: str = None,
        vpc_firewall_name: str = None,
        vpc_region: str = None,
    ):
        # The instance ID of the CEN.
        # 
        # > Prerequisite: The CEN instance must be created by invoking the CreateCen operation.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The settings for the switch status of the virtual private cloud (VPC) firewalls at the border. Valid values:
        # 
        # - **open** (default): Automatically enables protection after you create a VPC and the virtual private cloud (VPC) firewalls at the border are created.
        # - **close**: Does not automatically enable protection after the virtual private cloud (VPC) firewalls at the border are created. You can invoke the [ModifyVpcFirewallCenSwitchStatus](https://help.aliyun.com/document_detail/345780.html) operation to enable protection.
        # 
        # This parameter is required.
        self.firewall_switch = firewall_switch
        # The vSwitch CIDR block used by the firewall. You must configure a CIDR block with a subnet mask of no more than 29 bits that does not conflict with your network planning to allocate to the vSwitch CIDR block required for the procedure of creating the firewall, in order to perform automatic creation of the vSwitch (Cloud_Firewall_VSWITCH) in the firewall secure VPC for traffic diversion and processing. The vSwitch CIDR block must be a subnet of the firewall VPC CIDR block.
        # 
        # If you do not specify this parameter, the default is to automatically allocate the 10.219.219.216/29 CIDR block.
        # 
        # > This parameter takes effect only when you create a VPC firewall in the local region of the CEN for the first time.
        self.firewall_vswitch_cidr_block = firewall_vswitch_cidr_block
        # The ID of the zone to which the firewall vSwitch belongs.
        self.firewall_vswitch_zone_id = firewall_vswitch_zone_id
        # The VPC CIDR block used by the firewall. You must configure a CIDR block with a subnet mask of no more than 28 bits to allocate to the VPC CIDR block required for the procedure of creating the firewall, in order to perform automatic creation of the firewall secure VPC (Cloud_Firewall_VPC) for traffic diversion and processing.
        # 
        # If you do not specify this parameter, the default is to automatically allocate the 10.0.0.0/8 CIDR block.
        # 
        # > This parameter takes effect only when you create a VPC firewall in the local region of the CEN for the first time.
        self.firewall_vpc_cidr_block = firewall_vpc_cidr_block
        # The ID of the secondary zone to which the firewall belongs. Only when the primary zone service is not active, the firewall will perform automatic switchover to the secondary zone to continue running.
        # 
        # If you do not specify this parameter, the default is to automatically allocate the secondary zone for the firewall.
        # 
        # 
        # 
        # > This parameter takes effect only when you create a VPC firewall in the local region of the CEN for the first time.
        self.firewall_vpc_standby_zone_id = firewall_vpc_standby_zone_id
        # The ID of the primary zone to which the firewall belongs.
        # If your business is sensitive to latency, you can set the zone of the firewall to be the same as the zone of the vSwitch in your business VPC to reduce latency.
        # 
        # If you do not specify this parameter, the system automatically assigns a zone for the firewall.
        # 
        # 
        # 
        # > This parameter takes effect only when you create a VPC firewall in the local region of the CEN for the first time.
        self.firewall_vpc_zone_id = firewall_vpc_zone_id
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The UID of the member accounts of the current Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance ID of the VPC-connected instance for which you want to create virtual private cloud (VPC) firewalls at the border.
        # 
        # > Prerequisite: The VPC must be added to the CEN specified by the CenId parameter by invoking the AttachCenChildInstance operation.
        # 
        # This parameter is required.
        self.network_instance_id = network_instance_id
        # The ID of the vSwitch to which the Cloud Firewall interface belongs.
        self.v_switch_id = v_switch_id
        # The instance name of the virtual private cloud (VPC) firewalls at the border.
        # 
        # This parameter is required.
        self.vpc_firewall_name = vpc_firewall_name
        # The region ID of the VPC for which you want to create virtual private cloud (VPC) firewalls at the border.
        # 
        # > For more information about the regions supported by Cloud Firewall, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        # 
        # This parameter is required.
        self.vpc_region = vpc_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch

        if self.firewall_vswitch_cidr_block is not None:
            result['FirewallVSwitchCidrBlock'] = self.firewall_vswitch_cidr_block

        if self.firewall_vswitch_zone_id is not None:
            result['FirewallVSwitchZoneId'] = self.firewall_vswitch_zone_id

        if self.firewall_vpc_cidr_block is not None:
            result['FirewallVpcCidrBlock'] = self.firewall_vpc_cidr_block

        if self.firewall_vpc_standby_zone_id is not None:
            result['FirewallVpcStandbyZoneId'] = self.firewall_vpc_standby_zone_id

        if self.firewall_vpc_zone_id is not None:
            result['FirewallVpcZoneId'] = self.firewall_vpc_zone_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name

        if self.vpc_region is not None:
            result['VpcRegion'] = self.vpc_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')

        if m.get('FirewallVSwitchCidrBlock') is not None:
            self.firewall_vswitch_cidr_block = m.get('FirewallVSwitchCidrBlock')

        if m.get('FirewallVSwitchZoneId') is not None:
            self.firewall_vswitch_zone_id = m.get('FirewallVSwitchZoneId')

        if m.get('FirewallVpcCidrBlock') is not None:
            self.firewall_vpc_cidr_block = m.get('FirewallVpcCidrBlock')

        if m.get('FirewallVpcStandbyZoneId') is not None:
            self.firewall_vpc_standby_zone_id = m.get('FirewallVpcStandbyZoneId')

        if m.get('FirewallVpcZoneId') is not None:
            self.firewall_vpc_zone_id = m.get('FirewallVpcZoneId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        if m.get('VpcRegion') is not None:
            self.vpc_region = m.get('VpcRegion')

        return self

