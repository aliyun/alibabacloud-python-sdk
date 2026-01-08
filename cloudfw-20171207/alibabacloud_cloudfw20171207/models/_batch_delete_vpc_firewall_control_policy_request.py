# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchDeleteVpcFirewallControlPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_uuid_list: List[str] = None,
        vpc_firewall_id: str = None,
    ):
        # The UUIDs of access control policies.
        # 
        # This parameter is required.
        self.acl_uuid_list = acl_uuid_list
        # The instance ID of the VPC firewall.
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
        if self.acl_uuid_list is not None:
            result['AclUuidList'] = self.acl_uuid_list

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuidList') is not None:
            self.acl_uuid_list = m.get('AclUuidList')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

