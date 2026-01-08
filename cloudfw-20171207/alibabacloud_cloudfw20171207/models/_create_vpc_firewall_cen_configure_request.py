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
        # Specifies whether to enable the VPC firewall. Valid values:
        # 
        # *   **open**: After you create the VPC firewall, the VPC firewall is automatically enabled. This is the default value.
        # *   **close**: After you create the VPC firewall, the VPC firewall is disabled. You can call the [ModifyVpcFirewallCenSwitchStatus](https://help.aliyun.com/document_detail/345780.html) operation to manually enable the VPC firewall.
        # 
        # This parameter is required.
        self.firewall_switch = firewall_switch
        # The CIDR block of the vSwitch that is automatically created for the VPC firewall. You must specify a CIDR block for the Cloud_Firewall_VSWITCH VPC that is automatically created for the VPC firewall for traffic redirection. The CIDR block does not conflict with your network plan. The subnet mask of the CIDR block must be less than or equal to 29 bits in length. The CIDR block of the vSwitch must be within the network segment of the VPC.
        # 
        # If you do not specify a value, the CIDR block 10.219.219.216/29 is automatically allocated.
        # 
        # >  This parameter takes effect only when you create a VPC firewall for the first time in the current CEN instance and region.
        self.firewall_vswitch_cidr_block = firewall_vswitch_cidr_block
        # The CIDR block of the VPC that is automatically created for the VPC firewall. You must specify a CIDR block for the Cloud_Firewall_VPC VPC that is automatically created for the VPC firewall for traffic redirection. The subnet mask of the CIDR block must be less than or equal to 28 bits in length.
        # 
        # If you do not specify a value, the CIDR block 10.0.0.0/8 is automatically allocated.
        # 
        # >  This parameter takes effect only when you create a VPC firewall for the first time in the current CEN instance and region.
        self.firewall_vpc_cidr_block = firewall_vpc_cidr_block
        # The ID of the backup availability zone to which the firewall belongs. The firewall will automatically switch to the backup availability zone to continue running only if the primary availability zone service is unavailable.
        # If this parameter is not filled, the backup availability zone for the firewall will be automatically assigned.
        # > This parameter is only effective when creating a VPC firewall for the first time in this CEN region.
        self.firewall_vpc_standby_zone_id = firewall_vpc_standby_zone_id
        # The ID of the zone to which the vSwitch belongs. If your service is latency-sensitive, you can specify the same zone for the vSwitch of the firewall and the vSwitch of your business VPC to minimize latency.
        # 
        # If you do not specify a value, a zone is automatically assigned for the vSwitch.
        # 
        # >  This parameter takes effect only when you create a VPC firewall for the first time in the current CEN instance and region. For more information about zones that are supported by each region, see [Query zones](https://help.aliyun.com/document_detail/36064.html).
        self.firewall_vpc_zone_id = firewall_vpc_zone_id
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The ID of the VPC for which you want to create the VPC firewall.
        # 
        # This parameter is required.
        self.network_instance_id = network_instance_id
        # The ID of the vSwitch that is used to associate with the elastic network interface (ENI) required by the VPC firewall.
        self.v_switch_id = v_switch_id
        # The instance name of the VPC firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_name = vpc_firewall_name
        # The ID of the region to which the VPC belongs.
        # 
        # > For more information about the regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
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

