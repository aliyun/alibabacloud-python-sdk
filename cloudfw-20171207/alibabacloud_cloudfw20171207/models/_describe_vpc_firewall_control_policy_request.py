# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallControlPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_action: str = None,
        acl_uuid: str = None,
        current_page: str = None,
        description: str = None,
        destination: str = None,
        lang: str = None,
        member_uid: str = None,
        page_size: str = None,
        proto: str = None,
        release: str = None,
        repeat_type: str = None,
        source: str = None,
        vpc_firewall_id: str = None,
    ):
        # The action that is performed on traffic. Valid values:
        # 
        # - **accept**: allows the traffic.
        # 
        # - **drop**: denies the traffic.
        # 
        # - **log**: monitors the traffic.
        # 
        # > If you do not set this parameter, policies of all actions are queried.
        self.acl_action = acl_action
        # The unique ID of the access control policy.
        self.acl_uuid = acl_uuid
        # The page number.
        self.current_page = current_page
        # The description of the access control policy. Fuzzy match is supported.
        self.description = description
        # The destination address in the access control policy. Fuzzy match is supported.
        # 
        # > The value can be a CIDR block, a domain name, or an address book.
        self.destination = destination
        # The language of the request and response.
        # 
        # Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The number of entries per page.
        # 
        # Maximum value: 50.
        self.page_size = page_size
        # The protocol type in the access control policy. Valid values:
        # 
        # - **TCP**
        # 
        # - **UDP**
        # 
        # - **ICMP**
        # 
        # - **ANY**: all protocols
        # 
        # > If you do not set this parameter, policies of all protocols are queried.
        self.proto = proto
        # The status of the access control policy. Valid values:
        # 
        # - **true**: enabled
        # 
        # - **false**: disabled
        self.release = release
        # The recurrence type of the access control policy. Valid values:
        # 
        # - **Permanent** (default): The policy is always in effect.
        # 
        # - **None**: The policy is a one-time policy.
        # 
        # - **Daily**: The policy recurs daily.
        # 
        # - **Weekly**: The policy recurs weekly.
        # 
        # - **Monthly**: The policy recurs monthly.
        self.repeat_type = repeat_type
        # The source address in the access control policy. Fuzzy match is supported.
        # 
        # > The value can be a CIDR block or an address book.
        self.source = source
        # The instance ID of the VPC boundary firewall. You can specify one of the following IDs:
        # 
        # - The ID of a Cloud Enterprise Network (CEN) instance if the firewall protects traffic between two VPCs connected via the CEN instance.
        # 
        # - The instance ID of the VPC boundary firewall if the firewall protects traffic between two VPCs connected via an Express Connect circuit.
        # 
        # > You can call the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/159760.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_action is not None:
            result['AclAction'] = self.acl_action

        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.description is not None:
            result['Description'] = self.description

        if self.destination is not None:
            result['Destination'] = self.destination

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.release is not None:
            result['Release'] = self.release

        if self.repeat_type is not None:
            result['RepeatType'] = self.repeat_type

        if self.source is not None:
            result['Source'] = self.source

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclAction') is not None:
            self.acl_action = m.get('AclAction')

        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Destination') is not None:
            self.destination = m.get('Destination')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('Release') is not None:
            self.release = m.get('Release')

        if m.get('RepeatType') is not None:
            self.repeat_type = m.get('RepeatType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

