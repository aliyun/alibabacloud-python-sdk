# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryCostModelDetailRequest(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        client_id: int = None,
        client_ids: str = None,
        end_time: int = None,
        max_results: int = None,
        member_user_ids: str = None,
        model_id: int = None,
        next_token: str = None,
        page: int = None,
        page_index: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # Optional. Filters by API Key ID. This parameter is linked to the department and requires clientId to be specified first.
        self.api_key_id = api_key_id
        # The department ID used to filter results.
        self.client_id = client_id
        # The list of department IDs, separated by commas. Supports querying data for multiple departments. This parameter is mutually exclusive with clientId.
        self.client_ids = client_ids
        # The end time, in UNIX timestamp (seconds).
        # 
        # This parameter is required.
        self.end_time = end_time
        # maxResults
        self.max_results = max_results
        # Optional. Filters by member IDs, separated by commas. If not specified, the department and all its members are included. If an empty value is specified, only the department is included without members.
        self.member_user_ids = member_user_ids
        # The model ID.
        # 
        # This parameter is required.
        self.model_id = model_id
        # nextToken
        self.next_token = next_token
        # The page number. Default value: 1.
        self.page = page
        # The page number. This parameter takes priority over the page parameter.
        self.page_index = page_index
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The start time, in UNIX timestamp (seconds).
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

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.member_user_ids is not None:
            result['memberUserIds'] = self.member_user_ids

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page is not None:
            result['page'] = self.page

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

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

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('memberUserIds') is not None:
            self.member_user_ids = m.get('memberUserIds')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

