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
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The CIDR block information of the local VPC. The value is a JSON string and contains the following parameters:
        # 
        # - **RouteTableId**: The ID of the route table for the local VPC.
        # 
        # - **RouteEntryList**: The route entries for the local VPC. This parameter is a JSON string that contains DestinationCidr (the destination CIDR block of the local VPC) and NextHopInstanceId (the ID of the next hop instance for the local VPC).
        # 
        # > Call the [DescribeVpcFirewallDetail](https://help.aliyun.com/document_detail/342892.html) operation to query the CIDR block information of the local VPC for the VPC firewall.
        # 
        # This parameter is required.
        self.local_vpc_cidr_table_list = local_vpc_cidr_table_list
        # The UID of the member account.
        self.member_uid = member_uid
        # The CIDR block information of the peer VPC. The value is a JSON string and contains the following parameters:
        # 
        # - **RouteTableId**: The ID of the route table for the peer VPC.
        # 
        # - **RouteEntryList**: The route entries for the peer VPC. This parameter is a JSON string that contains DestinationCidr (the destination CIDR block of the peer VPC) and NextHopInstanceId (the ID of the next hop instance for the peer VPC).
        # 
        # > Call the [DescribeVpcFirewallDetail](https://help.aliyun.com/document_detail/342892.html) operation to query the CIDR block information of the peer VPC for the VPC firewall.
        # 
        # This parameter is required.
        self.peer_vpc_cidr_table_list = peer_vpc_cidr_table_list
        # The instance ID of the VPC firewall.
        # 
        # > Call the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/342932.html) operation to query the instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id
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

