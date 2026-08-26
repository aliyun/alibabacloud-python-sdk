# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListTagKeysResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        request_id: str = None,
        tag_keys: List[main_models.ListTagKeysResponseBodyTagKeys] = None,
        total_count: int = None,
    ):
        # The page number of the current page displayed in a paged query.
        self.current_page = current_page
        # The maximum number of entries returned in this query.
        self.max_results = max_results
        # The token for the next query. An empty value of NextToken indicates that there is no next page.
        self.next_token = next_token
        # The maximum number of entries per page in a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of tag keys.
        self.tag_keys = tag_keys
        # The total number of entries in the list.
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

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
        tag_count: int = None,
        tag_key: str = None,
    ):
        # The total number of tag keys.
        self.tag_count = tag_count
        # The tag key.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

