# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutTargetsShrinkRequest(DaraModel):
    def __init__(
        self,
        event_bus_name: str = None,
        rule_name: str = None,
        targets_shrink: str = None,
    ):
        # The name of the event bus.
        # 
        # This parameter is required.
        self.event_bus_name = event_bus_name
        # The name of the event rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The event targets to be created or updated. For more information, see [Limits](https://help.aliyun.com/document_detail/163289.html).
        # 
        # This parameter is required.
        self.targets_shrink = targets_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.targets_shrink is not None:
            result['Targets'] = self.targets_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Targets') is not None:
            self.targets_shrink = m.get('Targets')

        return self

