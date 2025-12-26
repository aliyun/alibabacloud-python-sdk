# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTagCloudResourcesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        scope: str = None,
    ):
        # The number of entries per page. Maximum value: 1000. Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The resource IDs. You can specify up to 50 resource IDs. You do not need to specify this parameter if you set ResourceType to AliUid.
        self.resource_ids = resource_ids
        # The type of the cloud resource.
        # 
        # Valid values:
        # 
        # *   AppId: app ID.
        # *   WyId: Alibaba Cloud Workspace user ID.
        # *   AppInstanceGroupId: delivery group ID.
        # *   AliUid: tenant ID.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag type.
        # 
        # Valid values:
        # 
        # *   All (default): all tags.
        # *   Custom: custom tag.
        # *   System: system tag.
        self.scope = scope

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

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

