# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTargetsRequest(DaraModel):
    def __init__(
        self,
        arn: str = None,
        event_bus_name: str = None,
        limit: int = None,
        next_token: str = None,
        rule_name: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the event rule.
        self.arn = arn
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The maximum number of returned entries in a call.
        self.limit = limit
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The name of the event rule.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

