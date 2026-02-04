# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListAccountsRequest(DaraModel):
    def __init__(
        self,
        include_tags: bool = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        query_keyword: str = None,
        tag: List[main_models.ListAccountsRequestTag] = None,
    ):
        # Specifies whether to return information about tags. Valid values:
        # 
        # *   false (default value)
        # *   true
        self.include_tags = include_tags
        # The number of entries per page. After you configure this parameter, token-based paging is preferentially used.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The keyword used for the query, such as the display name of a member.
        # 
        # Fuzzy match is supported.
        self.query_keyword = query_keyword
        # The tags. This parameter specifies a filter condition.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_keyword is not None:
            result['QueryKeyword'] = self.query_keyword

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryKeyword') is not None:
            self.query_keyword = m.get('QueryKeyword')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListAccountsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListAccountsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

