# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteVpcFirewallCenConfigureRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: str = None,
        vpc_firewall_id_list: List[str] = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id_list = vpc_firewall_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.vpc_firewall_id_list is not None:
            result['VpcFirewallIdList'] = self.vpc_firewall_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('VpcFirewallIdList') is not None:
            self.vpc_firewall_id_list = m.get('VpcFirewallIdList')

        return self

