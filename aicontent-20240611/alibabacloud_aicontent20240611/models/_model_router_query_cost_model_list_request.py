# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryCostModelListRequest(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        client_id: int = None,
        client_ids: str = None,
        end_time: int = None,
        granularity: str = None,
        max_results: int = None,
        member_user_ids: str = None,
        model_ids: str = None,
        model_types: str = None,
        next_token: str = None,
        search: str = None,
        start_time: int = None,
    ):
        # The API key ID used for filtering. This parameter is optional and associated with the department. You must specify clientId first.
        self.api_key_id = api_key_id
        # The department ID used for filtering.
        self.client_id = client_id
        # The department IDs. Separate multiple IDs with commas to query data for multiple departments. This parameter is mutually exclusive with clientId.
        self.client_ids = client_ids
        # The end time, specified as a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity for automatic aggregation. You do not need to pass this parameter. Valid values: hourly and daily. Default value: hourly.
        self.granularity = granularity
        # The maximum number of results.
        self.max_results = max_results
        # The member IDs used for filtering. Separate multiple IDs with commas. This parameter is optional. If you do not specify this parameter, the department and all its members are included. If you pass an empty value, only the department is included, excluding its members.
        self.member_user_ids = member_user_ids
        # The model IDs used for filtering. Separate multiple positive integer IDs with commas.
        self.model_ids = model_ids
        # The model types. Separate multiple values with commas.
        self.model_types = model_types
        # nextToken
        self.next_token = next_token
        # The keyword for fuzzy search by model name or code.
        self.search = search
        # The start time, specified as a UNIX timestamp in seconds.
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

        if self.client_ids is not None:
            result['clientIds'] = self.client_ids

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.member_user_ids is not None:
            result['memberUserIds'] = self.member_user_ids

        if self.model_ids is not None:
            result['modelIds'] = self.model_ids

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

        if m.get('clientIds') is not None:
            self.client_ids = m.get('clientIds')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('memberUserIds') is not None:
            self.member_user_ids = m.get('memberUserIds')

        if m.get('modelIds') is not None:
            self.model_ids = m.get('modelIds')

        if m.get('modelTypes') is not None:
            self.model_types = m.get('modelTypes')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('search') is not None:
            self.search = m.get('search')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

