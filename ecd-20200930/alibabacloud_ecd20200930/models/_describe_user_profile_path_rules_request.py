# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserProfilePathRulesRequest(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        region_id: str = None,
        rule_type: str = None,
    ):
        # The desktop group ID. This parameter is required when you set RuleType parameter to DesktopGroup.
        self.desktop_group_id = desktop_group_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The rule type that you want to configure for the directory.
        # 
        # Valid values:
        # 
        # *   DesktopGroup
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Default
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

