# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAlertTypeRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        rule_type: str = None,
    ):
        # The region of the data management center for threat analysis. Specify the management center region based on the region where your assets reside. Valid values:
        # - cn-hangzhou: assets in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: assets outside China.
        self.region_id = region_id
        # The user ID that the administrator switches to for viewing as another member.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # - 1: the view of all accounts in the enterprise.
        self.role_type = role_type
        # The rule type. Valid values:
        # - predefine: predefined.
        # - customize: custom.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

