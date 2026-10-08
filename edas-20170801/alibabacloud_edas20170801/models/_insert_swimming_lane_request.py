# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertSwimmingLaneRequest(DaraModel):
    def __init__(
        self,
        app_infos: str = None,
        enable_rules: bool = None,
        entry_rules: str = None,
        group_id: int = None,
        logical_region_id: str = None,
        name: str = None,
        tag: str = None,
    ):
        # The information about applications related to the lane.
        self.app_infos = app_infos
        # Specifies whether to enable the throttling rule.
        self.enable_rules = enable_rules
        # The throttling conditions.
        # 
        # This parameter is required.
        self.entry_rules = entry_rules
        # The ID of the lane group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the custom namespace. The ID is in the `physical region ID:custom namespace identifier` format. Example: `cn-hangzhou:test`.
        # 
        # This parameter is required.
        self.logical_region_id = logical_region_id
        # The name of the lane.
        # 
        # This parameter is required.
        self.name = name
        # The tag.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_infos is not None:
            result['AppInfos'] = self.app_infos

        if self.enable_rules is not None:
            result['EnableRules'] = self.enable_rules

        if self.entry_rules is not None:
            result['EntryRules'] = self.entry_rules

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        if self.name is not None:
            result['Name'] = self.name

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfos') is not None:
            self.app_infos = m.get('AppInfos')

        if m.get('EnableRules') is not None:
            self.enable_rules = m.get('EnableRules')

        if m.get('EntryRules') is not None:
            self.entry_rules = m.get('EntryRules')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

