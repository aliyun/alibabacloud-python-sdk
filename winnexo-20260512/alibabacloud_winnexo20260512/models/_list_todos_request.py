# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTodosRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        priorities: List[str] = None,
        read_status: List[str] = None,
        sort_by: str = None,
        source_types: List[str] = None,
        statuses: List[str] = None,
        tenant_id: str = None,
    ):
        # The collaboration workspace ID. This is an optional filter. If not specified, items from all workspaces are returned.
        self.collaboration_group_id = collaboration_group_id
        # The keyword for fuzzy search in the title or summary.
        self.keyword = keyword
        # The maximum number of entries to return per page. Valid values: 1 to 100. This parameter takes precedence over pageSize if both are specified.
        self.max_results = max_results
        # The pagination token. Use the nextToken value returned in the previous response. This parameter takes precedence over page if both are specified.
        self.next_token = next_token
        # The page number. This parameter is ignored if nextToken is specified.
        self.page = page
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size
        # The priority filter. Valid values: HIGH, MEDIUM, and LOW.
        self.priorities = priorities
        # The read status filter. Valid values: UNREAD and READ. The status is determined by the readAt field of the assignee.
        self.read_status = read_status
        # The sorting method.
        self.sort_by = sort_by
        # The to-do type filter. Valid values: WORKFLOW and OPEN_API.
        self.source_types = source_types
        # The to-do status filter. Valid values: PENDING, COMPLETED, and CANCELLED.
        self.statuses = statuses
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

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

        if self.read_status is not None:
            result['readStatus'] = self.read_status

        if self.sort_by is not None:
            result['sortBy'] = self.sort_by

        if self.source_types is not None:
            result['sourceTypes'] = self.source_types

        if self.statuses is not None:
            result['statuses'] = self.statuses

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

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

        if m.get('readStatus') is not None:
            self.read_status = m.get('readStatus')

        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')

        if m.get('sourceTypes') is not None:
            self.source_types = m.get('sourceTypes')

        if m.get('statuses') is not None:
            self.statuses = m.get('statuses')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

