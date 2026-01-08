# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVpcFirewallIPSWhitelistRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        list_type: int = None,
        list_value: str = None,
        member_uid: int = None,
        vpc_firewall_id: str = None,
        white_type: int = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The type of the list. Valid values:
        # 
        # *   **1**: user-defined
        # *   **2**: address book
        # 
        # This parameter is required.
        self.list_type = list_type
        # The entry in the list.
        self.list_value = list_value
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance ID of the VPC firewall.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id
        # The type of the whitelist. Valid values:
        # 
        # *   **1**: destination
        # *   **2**: source
        # 
        # This parameter is required.
        self.white_type = white_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.list_value is not None:
            result['ListValue'] = self.list_value

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        if self.white_type is not None:
            result['WhiteType'] = self.white_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('ListValue') is not None:
            self.list_value = m.get('ListValue')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('WhiteType') is not None:
            self.white_type = m.get('WhiteType')

        return self

