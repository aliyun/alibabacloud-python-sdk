# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        page: int = None,
        resource_ids: str = None,
        resource_type: str = None,
        size: int = None,
        tags: str = None,
    ):
        # The token for the next query.
        self.next_token = next_token
        # The page number of the resource relationship list. This parameter is deprecated.
        self.page = page
        # The list of instance IDs to query. The value is in JSON array format and can contain up to 20 items.
        self.resource_ids = resource_ids
        # The resource type definition.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The number of entries per page in Settings for paged query and paging. This field is deprecated.
        self.size = size
        # The list of tags to query. The value is in JSON string format and can contain up to 20 items.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page is not None:
            result['Page'] = self.page

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.size is not None:
            result['Size'] = self.size

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

