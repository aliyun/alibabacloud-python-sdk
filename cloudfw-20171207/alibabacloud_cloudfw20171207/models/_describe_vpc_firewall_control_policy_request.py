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
        # The action (settings) that Cloud Firewall performs on the traffic in the access control policy of the virtual private cloud (VPC) firewall. Valid values:
        self.acl_action = acl_action
        # The unique identity ID of the access control policy of the virtual private cloud (VPC) firewall.
        self.acl_uuid = acl_uuid
        # The page number in a paged query. Settings the current page number for paging.
        self.current_page = current_page
        # The description of the access control policy of the virtual private cloud (VPC) firewall. Fuzzy queries are supported.
        self.description = description
        # The destination address in the access control policy of the virtual private cloud (VPC) firewall. Fuzzy queries are supported.
        self.destination = destination
        # The language type for requests and responses.
        self.lang = lang
        # The UID of a member account of the current Alibaba Cloud account.
        self.member_uid = member_uid
        # The number of access control policies for the virtual private cloud (VPC) firewall on each page in a paged query. Settings the number of policies per page for paging.
        self.page_size = page_size
        # The protocol type of the traffic in the access control policy of the virtual private cloud (VPC) firewall. Valid values:
        self.proto = proto
        # The enabled status of the access control policy. Valid values:
        self.release = release
        # The recurrence type of the policy validity period for the access control policy. Valid values:
        self.repeat_type = repeat_type
        # The source address in the access control policy of the virtual private cloud (VPC) firewall. Fuzzy queries are supported.
        self.source = source
        # The instance ID of the virtual private cloud (VPC) firewall. Valid values:
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

