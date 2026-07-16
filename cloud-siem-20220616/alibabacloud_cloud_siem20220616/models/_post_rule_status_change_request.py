# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PostRuleStatusChangeRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
        in_use: bool = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        rule_type: str = None,
    ):
        # A JSON array of rule IDs.
        self.ids = ids
        # The status of the rule. Valid values:
        # 
        # - true: enabled
        # 
        # - false: disabled
        self.in_use = in_use
        # The region where the Data Management center of threat analysis is located. Select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: Your assets are in a region outside China.
        self.region_id = region_id
        # The user ID of a member. An administrator can specify this parameter to switch to the perspective of the member.
        self.role_for = role_for
        # The type of the view.
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # 
        # - 1: the view of all accounts that belong to the enterprise.
        self.role_type = role_type
        # The type of the rule. Valid values:
        # 
        # - predefine: predefined rule
        # 
        # - customize: custom rule
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.in_use is not None:
            result['InUse'] = self.in_use

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

