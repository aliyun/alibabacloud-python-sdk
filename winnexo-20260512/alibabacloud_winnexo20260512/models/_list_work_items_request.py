# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListWorkItemsRequest(DaraModel):
    def __init__(
        self,
        business_statuses: List[str] = None,
        collaboration_group_id: str = None,
        item_types: List[str] = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        priorities: List[str] = None,
        scope: str = None,
        tenant_id: str = None,
    ):
        # The business statuses used for filtering.
        self.business_statuses = business_statuses
        # The ID of the collaboration workspace.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The work item types used for filtering.
        self.item_types = item_types
        # The keyword for fuzzy search in the title or description.
        self.keyword = keyword
        # The maximum number of entries to return per page. Valid values: 1 to 100. This parameter takes precedence over pageSize if both are specified.
        self.max_results = max_results
        # The pagination token. Obtain the token from the nextToken parameter in the previous response. This parameter takes precedence over page if both are specified.
        self.next_token = next_token
        # The page number. This parameter is ignored if nextToken is specified.
        self.page = page
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size
        # The priorities used for filtering.
        self.priorities = priorities
        # The personal scope used for filtering.
        self.scope = scope
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_statuses is not None:
            result['businessStatuses'] = self.business_statuses

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.item_types is not None:
            result['itemTypes'] = self.item_types

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.priorities is not None:
            result['priorities'] = self.priorities

        if self.scope is not None:
            result['scope'] = self.scope

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessStatuses') is not None:
            self.business_statuses = m.get('businessStatuses')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('itemTypes') is not None:
            self.item_types = m.get('itemTypes')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('priorities') is not None:
            self.priorities = m.get('priorities')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

