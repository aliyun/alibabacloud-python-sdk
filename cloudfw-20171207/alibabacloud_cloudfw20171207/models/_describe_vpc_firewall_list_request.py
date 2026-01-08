# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallListRequest(DaraModel):
    def __init__(
        self,
        connect_sub_type: str = None,
        current_page: str = None,
        firewall_switch_status: str = None,
        lang: str = None,
        member_uid: str = None,
        page_size: str = None,
        peer_uid: str = None,
        region_no: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
        vpc_id: str = None,
    ):
        # The sub-type of the connection. Valid values:
        # 
        # *   **vpc2vpc**: Express Connect connection
        # *   **vpcpeer**: peer connection
        self.connect_sub_type = connect_sub_type
        # The number of the page to return.
        # 
        # Pages start from page **1**. Default value: **1**.
        self.current_page = current_page
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        # *   **configured**: The VPC firewall is configured.
        # 
        # > If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The number of entries to return on each page.
        # 
        # Default value: **10**. Maximum value: **50**.
        self.page_size = page_size
        # The UID of the Alibaba Cloud account to which the peer VPC belongs.
        self.peer_uid = peer_uid
        # The region ID of the VPC.
        # 
        # > For more information about the regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_no = region_no
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_sub_type is not None:
            result['ConnectSubType'] = self.connect_sub_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.peer_uid is not None:
            result['PeerUid'] = self.peer_uid

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectSubType') is not None:
            self.connect_sub_type = m.get('ConnectSubType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PeerUid') is not None:
            self.peer_uid = m.get('PeerUid')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

