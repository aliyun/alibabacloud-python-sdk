# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagValuesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_type: str = None,
        tag_key: str = None,
        value_filter: str = None,
    ):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The resource type.
        # 
        # The value Account indicates the members of the resource directory.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag key. This parameter specifies a filter condition for the query.
        # 
        # This parameter is required.
        self.tag_key = tag_key
        # The tag value for a fuzzy query.
        self.value_filter = value_filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.value_filter is not None:
            result['ValueFilter'] = self.value_filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('ValueFilter') is not None:
            self.value_filter = m.get('ValueFilter')

        return self

