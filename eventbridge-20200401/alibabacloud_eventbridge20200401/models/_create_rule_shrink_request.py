# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
        event_targets_shrink: str = None,
        filter_pattern: str = None,
        rule_name: str = None,
        status: str = None,
    ):
        # The description of the event bus.
        self.description = description
        # The name of the event bus.
        # 
        # This parameter is required.
        self.event_bus_name = event_bus_name
        # The event targets.
        self.event_targets_shrink = event_targets_shrink
        # The event pattern, in JSON format. Valid values: stringEqual and stringExpression. You can specify up to five expressions in the map data structure in each field.
        # 
        # You can specify up to five expressions in the map data structure in each field.
        # 
        # This parameter is required.
        self.filter_pattern = filter_pattern
        # The name of the event rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The status of the event rule. Valid values: ENABLE: enables the event rule. It is the default status of the event rule. DISABLE: disables the event rule.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.event_targets_shrink is not None:
            result['EventTargets'] = self.event_targets_shrink

        if self.filter_pattern is not None:
            result['FilterPattern'] = self.filter_pattern

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('EventTargets') is not None:
            self.event_targets_shrink = m.get('EventTargets')

        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

