# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagKeysRequest(DaraModel):
    def __init__(
        self,
        key_filter: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_type: str = None,
    ):
        # The tag key for a fuzzy query.
        self.key_filter = key_filter
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The token that is used to start the next query.
        self.next_token = next_token
        # The resource type.
        # 
        # The value Account indicates the members of the resource directory.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_filter is not None:
            result['KeyFilter'] = self.key_filter

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyFilter') is not None:
            self.key_filter = m.get('KeyFilter')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

