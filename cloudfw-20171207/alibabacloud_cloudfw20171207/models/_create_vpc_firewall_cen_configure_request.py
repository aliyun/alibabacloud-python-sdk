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
        # The Cloud Enterprise Network (CEN) instance ID.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The switch status of the VPC border firewall. Valid values:
        # 
        # - **open** (default): Protection is automatically enabled after the VPC border firewall is created.
        # - **close**: Protection is not automatically enabled after the VPC border firewall is created. You can call the [ModifyVpcFirewallCenSwitchStatus](https://help.aliyun.com/document_detail/345780.html) operation to enable protection.
        # 
        # This parameter is required.
        self.firewall_switch = firewall_switch
        # The vSwitch CIDR block used by the firewall. You must configure a CIDR block with a subnet mask no larger than 29 bits that does not conflict with the network plan to allocate a vSwitch CIDR block for the firewall creation process. This is used to automatically create a vSwitch (Cloud_Firewall_VSWITCH) within the firewall security VPC for traffic redirection. The vSwitch CIDR block must be a subnet of the firewall VPC CIDR block.
        # 
        # If this parameter is not specified, the CIDR block 10.219.219.216/29 is automatically allocated by default.
        # 
        # > This parameter is only valid when a VPC firewall is created for the first time in this CEN region.
        self.firewall_vswitch_cidr_block = firewall_vswitch_cidr_block
        # The VPC CIDR block used by the firewall. You must configure a CIDR block with a subnet mask no larger than 28 bits to allocate a VPC CIDR block for the firewall creation process. This is used to automatically create a firewall security VPC (Cloud_Firewall_VPC) for traffic redirection.
        # 
        # If this parameter is not specified, the CIDR block 10.0.0.0/8 is automatically allocated by default.
        # 
        # > This parameter is only valid when a VPC firewall is created for the first time in this CEN region.
        self.firewall_vpc_cidr_block = firewall_vpc_cidr_block
        # The standby availability zone ID of the firewall. The firewall automatically switches to the standby availability zone and continues to run only when the primary availability zone service is unavailable.
        # 
        # If this parameter is not specified, the firewall standby availability zone is automatically allocated by default.
        # 
        # 
        # 
        # > This parameter is only valid when a VPC firewall is created for the first time in this CEN region.
        self.firewall_vpc_standby_zone_id = firewall_vpc_standby_zone_id
        # The primary availability zone ID of the firewall.
        # If your business is latency-sensitive, you can customize the firewall availability zone to be the same as your business VPC vSwitch availability zone to reduce latency.
        # 
        # If this parameter is not specified, the firewall availability zone is automatically allocated by default.
        # 
        # 
        # 
        # > This parameter is only valid when a VPC firewall is created for the first time in this CEN region.
        self.firewall_vpc_zone_id = firewall_vpc_zone_id
        # The language type for the request and response messages. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The member account UID of the current Alibaba Cloud account.
        self.member_uid = member_uid
        # The VPC instance ID for which the VPC border firewall is created.
        # 
        # This parameter is required.
        self.network_instance_id = network_instance_id
        # The vSwitch ID to which the Cloud Firewall interface belongs.
        self.v_switch_id = v_switch_id
        # The instance name of the VPC border firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_name = vpc_firewall_name
        # The region ID of the VPC for which the VPC border firewall is created.
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

