# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRulesRequest(DaraModel):
    def __init__(
        self,
        event_bus_name: str = None,
        limit: int = None,
        next_token: str = None,
        rule_name_prefix: str = None,
    ):
        # The name of the event bus.
        # 
        # This parameter is required.
        self.event_bus_name = event_bus_name
        # The maximum number of entries to be returned in a single call. You can use this parameter and the NextToken parameter to implement paging. A maximum of 100 entries can be returned in a single call.
        self.limit = limit
        # If you set the Limit parameter and excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The prefix of the rule name.
        self.rule_name_prefix = rule_name_prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.rule_name_prefix is not None:
            result['RuleNamePrefix'] = self.rule_name_prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RuleNamePrefix') is not None:
            self.rule_name_prefix = m.get('RuleNamePrefix')

        return self

