# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tags_shrink: str = None,
    ):
        # The maximum number of tagged resources that you want to return. Valid values: 0 to 200. If you do not specify this parameter or set the parameter to 0, the default value of 100 is used.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken. Tagged resources are returned in lexicographical order starting from the position that is specified by this parameter.
        self.next_token = next_token
        # The resource IDs, which are instance names.
        self.resource_ids_shrink = resource_ids_shrink
        # The type of the resource. valid value:
        # 
        # instance: instance
        self.resource_type = resource_type
        # The tags.
        self.tags_shrink = tags_shrink

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

        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

