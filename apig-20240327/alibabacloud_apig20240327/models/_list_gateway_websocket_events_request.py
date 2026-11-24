# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayWebsocketEventsRequest(DaraModel):
    def __init__(
        self,
        connection_id: str = None,
        end_time: int = None,
        max_results: int = None,
        model: str = None,
        next_token: str = None,
        provider: str = None,
        source: str = None,
        start_time: int = None,
        turn_id: str = None,
    ):
        # The connection identifier.
        self.connection_id = connection_id
        # The end time. The value is a UNIX timestamp in seconds since the UTC epoch. Example: 1793919600.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The maximum number of results per page for cursor-based pagination.
        self.max_results = max_results
        # The model.
        self.model = model
        # The pagination token for the next page.
        self.next_token = next_token
        # The provider.
        self.provider = provider
        # The log source.
        self.source = source
        # The start time. The value is a UNIX timestamp in seconds since the UTC epoch. Example: 1793916000.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The turn identifier.
        self.turn_id = turn_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_id is not None:
            result['connectionId'] = self.connection_id

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.model is not None:
            result['model'] = self.model

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.provider is not None:
            result['provider'] = self.provider

        if self.source is not None:
            result['source'] = self.source

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.turn_id is not None:
            result['turnId'] = self.turn_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectionId') is not None:
            self.connection_id = m.get('connectionId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('turnId') is not None:
            self.turn_id = m.get('turnId')

        return self

