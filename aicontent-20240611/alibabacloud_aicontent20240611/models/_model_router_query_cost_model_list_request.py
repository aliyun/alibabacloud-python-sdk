# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryCostModelListRequest(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        client_id: int = None,
        end_time: int = None,
        granularity: str = None,
        max_results: int = None,
        member_user_ids: str = None,
        model_types: str = None,
        next_token: str = None,
        search: str = None,
        start_time: int = None,
    ):
        # Optional. Filters results by API key ID. This parameter works in conjunction with the department and requires clientId to be specified first.
        self.api_key_id = api_key_id
        # Filters results by department ID.
        self.client_id = client_id
        # The end time, as a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Automatic aggregation. You do not need to pass this parameter. Granularity: hourly/daily. Default value: hourly.
        self.granularity = granularity
        # The maximum number of results to return.
        self.max_results = max_results
        # Optional. Filters results by member IDs, separated by commas. If not specified, the department and all its members are included. If an empty value is passed, only the department is included without members.
        self.member_user_ids = member_user_ids
        # The model types, separated by commas.
        self.model_types = model_types
        # nextToken
        self.next_token = next_token
        # Performs a fuzzy match on the model name or code.
        self.search = search
        # The start time, as a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['apiKeyId'] = self.api_key_id

        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.member_user_ids is not None:
            result['memberUserIds'] = self.member_user_ids

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
        if m.get('apiKeyId') is not None:
            self.api_key_id = m.get('apiKeyId')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('memberUserIds') is not None:
            self.member_user_ids = m.get('memberUserIds')

        if m.get('modelTypes') is not None:
            self.model_types = m.get('modelTypes')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('search') is not None:
            self.search = m.get('search')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

