# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKnowledgeBasesRequest(DaraModel):
    def __init__(
        self,
        filters: str = None,
        max_results: int = None,
        name_pattern: str = None,
        next_token: str = None,
        sort_field_name: str = None,
        sort_order: str = None,
        tag: str = None,
    ):
        # The filter conditions for the knowledge bases, specified as a JSON string. The only supported key is `state`. Valid values are `0` and `1`.
        self.filters = filters
        # The maximum number of entries to return on each page. Use this parameter with the `NextToken` parameter to implement pagination.
        self.max_results = max_results
        # A keyword to search for in the names of knowledge bases.
        self.name_pattern = name_pattern
        # The token used to retrieve the next page of results. Valid values:
        # 
        # - Omit this parameter for the first request.
        # 
        # - If the previous response returned a **NextToken** value, use it to retrieve the next page of results.
        self.next_token = next_token
        # The sort field. Valid values:
        # 
        # - `id`: Sorts by knowledge base ID. This is the default.
        # 
        # - `name`: Sorts by knowledge base name.
        self.sort_field_name = sort_field_name
        # The sort order. Valid values:
        # 
        # - **ASC**: Ascending order. This is the default.
        # 
        # - **DESC**: Descending order.
        self.sort_order = sort_order
        # The tag of the knowledge base. In DataAgent, this is the space ID.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filters is not None:
            result['Filters'] = self.filters

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name_pattern is not None:
            result['NamePattern'] = self.name_pattern

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.sort_field_name is not None:
            result['SortFieldName'] = self.sort_field_name

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NamePattern') is not None:
            self.name_pattern = m.get('NamePattern')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SortFieldName') is not None:
            self.sort_field_name = m.get('SortFieldName')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

