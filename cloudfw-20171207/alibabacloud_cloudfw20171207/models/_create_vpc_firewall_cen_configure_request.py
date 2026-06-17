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
        # The ID of the CEN instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The status of the VPC firewall. Valid values:
        # 
        # - **open** (default): The VPC firewall is enabled after it is created.
        # 
        # - **close**: The VPC firewall is disabled after it is created. Call the [ModifyVpcFirewallCenSwitchStatus](https://help.aliyun.com/document_detail/345780.html) operation to enable the firewall.
        # 
        # This parameter is required.
        self.firewall_switch = firewall_switch
        # The CIDR block of the vSwitch that is used by the firewall. Specify a CIDR block with a subnet mask of 29 bits or less that does not conflict with your network plan. This CIDR block is allocated to the vSwitch that is automatically created in the firewall VPC (Cloud_Firewall_VSWITCH) for traffic redirection. The vSwitch CIDR block must be a subnet of the firewall VPC CIDR block. If you do not specify this parameter, the system automatically allocates the 10.219.219.216/29 CIDR block.
        # 
        # If you leave this parameter empty, the CIDR block 10.219.219.216/29 is automatically allocated.
        # 
        # > This parameter is valid only when you create a VPC firewall for the first time in the current region of the CEN.
        self.firewall_vswitch_cidr_block = firewall_vswitch_cidr_block
        # The CIDR block of the VPC that is used by the firewall. Specify a CIDR block with a subnet mask of 28 bits or less. This CIDR block is allocated to the VPC that is automatically created for the firewall for traffic redirection. If you do not specify this parameter, the system automatically allocates the 10.0.0.0/8 CIDR block.
        # 
        # If you leave this property empty, the CIDR block 10.0.0.0/8 is automatically allocated.
        # 
        # > This parameter is valid only when you create a VPC firewall for the first time in the current region of the CEN.
        self.firewall_vpc_cidr_block = firewall_vpc_cidr_block
        # The ID of the secondary zone for the firewall. If the service in the primary zone becomes unavailable, the firewall automatically switches to the secondary zone. If you do not specify this parameter, the system automatically assigns a secondary zone for the firewall.
        # 
        # If you do not specify a value, a zone is automatically allocated to the VPC firewall.
        # 
        # > This parameter is valid only when you create a VPC firewall for the first time in the current region of the CEN.
        self.firewall_vpc_standby_zone_id = firewall_vpc_standby_zone_id
        # The ID of the primary zone for the firewall. If your business is sensitive to latency, specify the same zone for the firewall and the vSwitch of your business VPC to reduce latency. If you do not specify this parameter, the system automatically assigns a zone for the firewall.
        # 
        # If you do not specify a value, a zone is automatically allocated to the VPC firewall.
        # 
        # > This parameter is valid only when you create a VPC firewall for the first time in the current region of the CEN.
        self.firewall_vpc_zone_id = firewall_vpc_zone_id
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The UID of the member account.
        self.member_uid = member_uid
        # The ID of the VPC for which you want to create the VPC firewall.
        # 
        # This parameter is required.
        self.network_instance_id = network_instance_id
        # The ID of the vSwitch that is used by the Cloud Firewall interface.
        self.v_switch_id = v_switch_id
        # The name of the VPC firewall instance.
        # 
        # This parameter is required.
        self.vpc_firewall_name = vpc_firewall_name
        # The region ID of the VPC for which you want to create the VPC firewall.
        # 
        # > For more information about the regions that Cloud Firewall supports, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
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

