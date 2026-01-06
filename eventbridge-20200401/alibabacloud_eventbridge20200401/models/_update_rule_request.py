# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRuleRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
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
        # The event pattern, in JSON format. Valid values: stringEqual stringExpression Each field can have a maximum of five expressions in the map data structure.
        # 
        # Each field can have a maximum of five expressions in the map data structure.
        # 
        # This parameter is required.
        self.filter_pattern = filter_pattern
        # The name of the event rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The status of the event rule. Valid values: ENABLE: The event rule is enabled. It is the default state of the event rule. DISABLE: The event rule is disabled.
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

        if m.get('FilterPattern') is not None:
            self.filter_pattern = m.get('FilterPattern')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

