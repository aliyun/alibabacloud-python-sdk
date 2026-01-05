# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListTagKeysResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tag_keys: List[main_models.ListTagKeysResponseBodyTagKeys] = None,
        total_count: int = None,
    ):
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tag keys.
        self.tag_keys = tag_keys
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.tag_keys:
            for v1 in self.tag_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k1 in self.tag_keys:
                result['TagKeys'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k1 in m.get('TagKeys'):
                temp_model = main_models.ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTagKeysResponseBodyTagKeys(DaraModel):
    def __init__(
        self,
        category: str = None,
        tag_key: str = None,
    ):
        # The type of the tag.
        # 
        # Valid values: **Custom**, **System**, and **All**.
        # 
        # Default value: **All**.
        self.category = category
        # The tag that matches all filter conditions.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

