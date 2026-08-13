# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVpcFirewallConfigureRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        local_vpc_cidr_table_list: str = None,
        member_uid: str = None,
        peer_vpc_cidr_table_list: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The CIDR block information of the local VPC, in JSON format. The following parameters are included:
        # 
        # - **RouteTableId**: the routing table ID of the local VPC.
        # 
        # - **RouteEntryList**: specified in JSON format and contains DestinationCidr (the destination CIDR block of the local VPC) and NextHopInstanceId (the next hop instance ID of the local VPC).
        # 
        # > You can invoke the [DescribeVpcFirewallDetail](https://help.aliyun.com/document_detail/342892.html) operation to query the CIDR block information of the local VPC for the virtual private cloud (VPC) firewall.
        # 
        # This parameter is required.
        self.local_vpc_cidr_table_list = local_vpc_cidr_table_list
        # The UID of the member accounts of the current Alibaba Cloud account.
        self.member_uid = member_uid
        # The CIDR block information of the peer VPC, in JSON format. The following parameters are included:
        # 
        # - **RouteTableId**: the routing table ID of the peer VPC.
        # 
        # - **RouteEntryList**: specified in JSON format and contains DestinationCidr (the destination CIDR block of the peer VPC) and NextHopInstanceId (the next hop instance ID of the peer VPC).
        # 
        # > You can invoke the [DescribeVpcFirewallDetail](https://help.aliyun.com/document_detail/342892.html) operation to query the CIDR block information of the peer VPC for the virtual private cloud (VPC) firewall.
        # 
        # This parameter is required.
        self.peer_vpc_cidr_table_list = peer_vpc_cidr_table_list
        # The instance ID of the virtual private cloud (VPC) firewall.
        # 
        # > You can invoke the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/342932.html) operation to query the instance ID of the virtual private cloud (VPC) firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the virtual private cloud (VPC) firewall.
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
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.local_vpc_cidr_table_list is not None:
            result['LocalVpcCidrTableList'] = self.local_vpc_cidr_table_list

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.peer_vpc_cidr_table_list is not None:
            result['PeerVpcCidrTableList'] = self.peer_vpc_cidr_table_list

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LocalVpcCidrTableList') is not None:
            self.local_vpc_cidr_table_list = m.get('LocalVpcCidrTableList')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PeerVpcCidrTableList') is not None:
            self.peer_vpc_cidr_table_list = m.get('PeerVpcCidrTableList')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        return self

