# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRegistryNamespacesRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        type: str = None,
    ):
        # The search keyword. Fuzzy search by workspace name is supported.
        self.keyword = keyword
        # The number of entries per page in a paged query. Maximum value: 100.
        # Default value: 20.
        self.max_results = max_results
        # The query token. Set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The workspace type. Valid values:
        # 
        # - system: public workspace
        # 
        # - self: custom workspace
        # 
        # - shared: shared workspace
        # 
        # - community: community workspace
        # 
        # By default, all workspaces are returned.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

