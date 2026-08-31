# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryBillingDetailsRequest(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        client_id: int = None,
        client_ids: str = None,
        end_time: int = None,
        model_codes: str = None,
        model_id: int = None,
        model_types: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        start_time: int = None,
    ):
        # Optional. Filters results by API Key ID.
        self.api_key_id = api_key_id
        # Optional. Filters results by department ID (single value).
        self.client_id = client_id
        # The list of department IDs, separated by commas. Supports querying data for multiple departments. This parameter is mutually exclusive with clientId.
        self.client_ids = client_ids
        # The query end time, in UNIX timestamp (seconds).
        # 
        # This parameter is required.
        self.end_time = end_time
        # Optional. Filters results by model code. Separate multiple values with commas.
        self.model_codes = model_codes
        # Optional. Filters results by model ID.
        self.model_id = model_id
        # Optional. Filters results by model type. Separate multiple values with commas.
        self.model_types = model_types
        # The page number. Default value: 1.
        self.page = page
        # The number of entries per page. Default value: 20. Maximum value: 500.
        self.page_size = page_size
        # Optional. Filters results by exact match of the request ID.
        self.request_id = request_id
        # The query start time, in UNIX timestamp (seconds).
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

        if self.model_codes is not None:
            result['modelCodes'] = self.model_codes

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_types is not None:
            result['modelTypes'] = self.model_types

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        if m.get('modelCodes') is not None:
            self.model_codes = m.get('modelCodes')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelTypes') is not None:
            self.model_types = m.get('modelTypes')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

