# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserDefinedEventSourcesRequest(DaraModel):
    def __init__(
        self,
        event_bus_name: str = None,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
    ):
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The maximum number of entries to return per request. You can use this parameter with NextToken for pagination. The maximum value is 100.
        self.limit = limit
        # The prefix of the event source name.
        self.name_prefix = name_prefix
        # The token used to retrieve the next page of results. Set this parameter to the NextToken value returned from a previous call.
        self.next_token = next_token

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

        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

