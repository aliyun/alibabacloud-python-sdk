# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryBillingCostBreakdownRequest(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        client_id: int = None,
        end_time: int = None,
        granularity: str = None,
        max_results: int = None,
        model_id: int = None,
        model_types: str = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        self.api_key_id = api_key_id
        # The ID of the client to query. If not specified, data for all clients is returned.
        self.client_id = client_id
        # The end time for the query, specified as a Unix timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The granularity for data aggregation. Valid values: `hourly` and `daily`.
        # 
        # This parameter is required.
        self.granularity = granularity
        # The maximum number of results to return. This parameter is used for pagination along with `nextToken` and is mutually exclusive with `page` and `pageSize`.
        self.max_results = max_results
        # The ID of the model to query. If not specified, data for all models is returned.
        self.model_id = model_id
        # The types of the models to query, separated by commas. For example: `Chat,Embedding`. If not specified, data for all model types is returned.
        self.model_types = model_types
        # The pagination token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The page number. Default: 1.
        self.page = page
        # The number of entries per page. Default: 20. Maximum: 500.
        self.page_size = page_size
        # The start time for the query, specified as a Unix timestamp in seconds.
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

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_types is not None:
            result['modelTypes'] = self.model_types

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page is not None:
            result['page'] = self.page

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

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelTypes') is not None:
            self.model_types = m.get('modelTypes')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

