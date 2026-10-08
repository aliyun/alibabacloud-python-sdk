# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSwimmingLaneRequest(DaraModel):
    def __init__(
        self,
        app_infos: str = None,
        enable_rules: bool = None,
        entry_rules: str = None,
        lane_id: int = None,
        name: str = None,
    ):
        # A list of applications associated with the swimming lane.
        self.app_infos = app_infos
        # Specifies whether the throttling rule is enabled.
        # 
        # This parameter is required.
        self.enable_rules = enable_rules
        # The configuration of the throttling rule.
        self.entry_rules = entry_rules
        # The ID of the swimming lane.
        # 
        # This parameter is required.
        self.lane_id = lane_id
        # The name of the swimming lane.
        self.name = name

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

        if self.lane_id is not None:
            result['LaneId'] = self.lane_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfos') is not None:
            self.app_infos = m.get('AppInfos')

        if m.get('EnableRules') is not None:
            self.enable_rules = m.get('EnableRules')

        if m.get('EntryRules') is not None:
            self.entry_rules = m.get('EntryRules')

        if m.get('LaneId') is not None:
            self.lane_id = m.get('LaneId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

