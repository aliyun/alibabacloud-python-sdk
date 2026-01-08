# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpcFirewallConfigureRequest(DaraModel):
    def __init__(
        self,
        firewall_switch: str = None,
        lang: str = None,
        local_vpc_cidr_table_list: str = None,
        local_vpc_id: str = None,
        local_vpc_region: str = None,
        member_uid: str = None,
        peer_vpc_cidr_table_list: str = None,
        peer_vpc_id: str = None,
        peer_vpc_region: str = None,
        vpc_firewall_name: str = None,
    ):
        # The status of the VPC firewall after you create the firewall. Valid values:
        # 
        # *   **open**: After you create the VPC firewall, the VPC firewall is automatically enabled. This is the default value.
        # *   **close**: After you create the VPC firewall, the VPC firewall is disabled. To enable the firewall, you can call the [ModifyVpcFirewallSwitchStatus](https://help.aliyun.com/document_detail/342935.html) operation.
        # 
        # This parameter is required.
        self.firewall_switch = firewall_switch
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English.
        self.lang = lang
        # The CIDR blocks of the local VPC. The value is a JSON string that contains the following parameters:
        # 
        # *   **RouteTableId**: the ID of the route table for the local VPC.
        # *   **RouteEntryList**: The value is a JSON string that contains the DestinationCidr and NextHopInstanceId parameters. The DestinationCidr parameter indicates the destination CIDR block of the local VPC. The NextHopInstanceId parameter indicates the instance ID of the next hop for the local VPC.
        # 
        # This parameter is required.
        self.local_vpc_cidr_table_list = local_vpc_cidr_table_list
        # The ID of the local VPC.
        # 
        # This parameter is required.
        self.local_vpc_id = local_vpc_id
        # The region ID of the local VPC.
        # 
        # >  For more information about the regions in which Cloud Firewall is available, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        # 
        # This parameter is required.
        self.local_vpc_region = local_vpc_region
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The CIDR blocks of the peer VPC. The value is a JSON string that contains the following parameters:
        # 
        # *   **RouteTableId**: the ID of the route table for the peer VPC.
        # *   **RouteEntryList**: The value is a JSON string that contains the DestinationCidr and NextHopInstanceId parameters. The DestinationCidr parameter indicates the destination CIDR block of the peer VPC. The NextHopInstanceId parameter indicates the instance ID of the next hop for the peer VPC.
        # 
        # This parameter is required.
        self.peer_vpc_cidr_table_list = peer_vpc_cidr_table_list
        # The ID of the peer VPC.
        # 
        # This parameter is required.
        self.peer_vpc_id = peer_vpc_id
        # The region ID of the peer VPC.
        # 
        # >  For more information about Cloud Firewall supported regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        # 
        # This parameter is required.
        self.peer_vpc_region = peer_vpc_region
        # The instance name of the VPC firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.local_vpc_cidr_table_list is not None:
            result['LocalVpcCidrTableList'] = self.local_vpc_cidr_table_list

        if self.local_vpc_id is not None:
            result['LocalVpcId'] = self.local_vpc_id

        if self.local_vpc_region is not None:
            result['LocalVpcRegion'] = self.local_vpc_region

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.peer_vpc_cidr_table_list is not None:
            result['PeerVpcCidrTableList'] = self.peer_vpc_cidr_table_list

        if self.peer_vpc_id is not None:
            result['PeerVpcId'] = self.peer_vpc_id

        if self.peer_vpc_region is not None:
            result['PeerVpcRegion'] = self.peer_vpc_region

        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LocalVpcCidrTableList') is not None:
            self.local_vpc_cidr_table_list = m.get('LocalVpcCidrTableList')

        if m.get('LocalVpcId') is not None:
            self.local_vpc_id = m.get('LocalVpcId')

        if m.get('LocalVpcRegion') is not None:
            self.local_vpc_region = m.get('LocalVpcRegion')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PeerVpcCidrTableList') is not None:
            self.peer_vpc_cidr_table_list = m.get('PeerVpcCidrTableList')

        if m.get('PeerVpcId') is not None:
            self.peer_vpc_id = m.get('PeerVpcId')

        if m.get('PeerVpcRegion') is not None:
            self.peer_vpc_region = m.get('PeerVpcRegion')

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        return self

