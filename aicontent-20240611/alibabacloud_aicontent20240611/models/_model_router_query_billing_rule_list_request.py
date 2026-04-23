# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterQueryBillingRuleListRequest(DaraModel):
    def __init__(
        self,
        active_only: bool = None,
        max_results: int = None,
        model_code: str = None,
        model_id: int = None,
        model_type: str = None,
        next_token: str = None,
        page: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.active_only = active_only
        # maxResults
        self.max_results = max_results
        self.model_code = model_code
        self.model_id = model_id
        self.model_type = model_type
        # nextToken
        self.next_token = next_token
        self.page = page
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_only is not None:
            result['activeOnly'] = self.active_only

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page is not None:
            result['page'] = self.page

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeOnly') is not None:
            self.active_only = m.get('activeOnly')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

