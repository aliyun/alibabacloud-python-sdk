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
        # The instance ID of the CEN instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # Settings for the virtual private cloud (VPC) firewall switch status. Valid values:
        # 
        # - **open** (default): The VPC firewall is automatically enabled after you create a VPC firewall.
        # - **close**: The VPC firewall is not automatically enabled after you create a VPC firewall. You can invoke the [ModifyVpcFirewallCenSwitchStatus](https://help.aliyun.com/document_detail/345780.html) operation to enable the VPC firewall.
        # 
        # This parameter is required.
        self.firewall_switch = firewall_switch
        # The CIDR block of the vSwitch used by the firewall. Specify a CIDR block with a subnet mask of no more than 29 bits that does not conflict with your network planning. This CIDR block is allocated to the vSwitch during the procedure for automatic creation of the firewall security VPC (Cloud_Firewall_VSWITCH) for traffic redirection. The vSwitch CIDR block must be a subnet of the firewall VPC CIDR block.
        # 
        # If you leave this parameter empty, the default CIDR block 10.219.219.216/29 is automatically assigned.
        # 
        # > This parameter takes effect only when you create a VPC firewall for the first time in the local region of the CEN instance.
        self.firewall_vswitch_cidr_block = firewall_vswitch_cidr_block
        # The CIDR block of the VPC used by the firewall. Specify a CIDR block with a subnet mask of no more than 28 bits. This CIDR block is allocated to the VPC that is created during the procedure to create a VPC firewall (Cloud_Firewall_VPC) for automatic creation of the firewall security VPC for traffic redirection.
        # 
        # If you leave this parameter empty, the default CIDR block 10.0.0.0/8 is automatically assigned.
        # 
        # > This parameter takes effect only when a VPC firewall is created for the first time in the local region of the CEN instance.
        self.firewall_vpc_cidr_block = firewall_vpc_cidr_block
        # The ID of the secondary zone of the firewall. The firewall performs an automatic switchover to the secondary zone to continue running only when the primary zone becomes unavailable.
        # 
        # If you leave this parameter empty, a default active secondary zone is automatically allocated.
        # 
        # 
        # 
        # > This parameter takes effect only when you create a VPC firewall for the first time in the local region of the CEN instance.
        self.firewall_vpc_standby_zone_id = firewall_vpc_standby_zone_id
        # The ID of the primary zone of the firewall. If your business is latency-sensitive, set this parameter to the same zone as the vSwitch of the business VPC to reduce latency.
        # 
        # If you leave this parameter empty, a default active zone is automatically allocated.
        # 
        # 
        # 
        # > This parameter takes effect only when you create a VPC firewall for the first time in the local region of the CEN instance.
        self.firewall_vpc_zone_id = firewall_vpc_zone_id
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The UID of the member account of the current Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance ID of the VPC-connected instance for which you want to create a virtual private cloud (VPC) firewall.
        # 
        # This parameter is required.
        self.network_instance_id = network_instance_id
        # The ID of the vSwitch to which the Cloud Firewall interface belongs.
        self.v_switch_id = v_switch_id
        # The instance name of the virtual private cloud (VPC) firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_name = vpc_firewall_name
        # The region ID of the VPC for which you want to create a virtual private cloud (VPC) firewall.
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

