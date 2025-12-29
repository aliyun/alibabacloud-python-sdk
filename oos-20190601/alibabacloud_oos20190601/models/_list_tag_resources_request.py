# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_ids: Dict[str, Any] = None,
        resource_type: str = None,
        tags: Dict[str, Any] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of resources. The number of resource IDs ranges from 1 to 50.
        self.resource_ids = resource_ids
        # The type of the resource. Valid values: template execution
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

