# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryCostModelListRequest(DaraModel):
    def __init__(
        self,
        client_id: int = None,
        end_time: int = None,
        granularity: str = None,
        max_results: int = None,
        model_types: str = None,
        next_token: str = None,
        search: str = None,
        start_time: int = None,
    ):
        self.client_id = client_id
        # This parameter is required.
        self.end_time = end_time
        self.granularity = granularity
        self.max_results = max_results
        self.model_types = model_types
        # nextToken
        self.next_token = next_token
        self.search = search
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.model_types is not None:
            result['modelTypes'] = self.model_types

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.search is not None:
            result['search'] = self.search

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('modelTypes') is not None:
            self.model_types = m.get('modelTypes')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('search') is not None:
            self.search = m.get('search')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

