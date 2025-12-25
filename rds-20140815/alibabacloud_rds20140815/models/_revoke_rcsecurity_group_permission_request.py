# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RevokeRCSecurityGroupPermissionRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        region_id: str = None,
        security_group_id: str = None,
        security_group_rule_id_list: List[str] = None,
    ):
        # The direction of the security group rules that you want to delete. Valid values:
        # 
        # *   **ingress**: inbound security group rules.
        # *   **egress**: outbound security group rules.
        # 
        # >  You can specify security group rules only in the same direction in a request.
        self.direction = direction
        # The region ID.
        self.region_id = region_id
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The IDs of the security group rules that you want to delete.
        self.security_group_rule_id_list = security_group_rule_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_rule_id_list is not None:
            result['SecurityGroupRuleIdList'] = self.security_group_rule_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupRuleIdList') is not None:
            self.security_group_rule_id_list = m.get('SecurityGroupRuleIdList')

        return self

