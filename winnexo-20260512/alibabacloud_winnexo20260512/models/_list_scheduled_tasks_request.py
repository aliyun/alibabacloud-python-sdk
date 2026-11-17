# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListScheduledTasksRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        creator_only: bool = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        tenant_id: str = None,
        visibilities: List[str] = None,
    ):
        # The ID of the collaboration group to which the task belongs, such as cg_101. If this parameter is specified, a group space task is created, and the caller must be a valid group member. If this parameter is left empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # Specifies whether to view only tasks created by yourself. This parameter takes effect only at the group level (at the personal level, tasks are always your own). If this parameter is not specified, no filtering is applied.
        self.creator_only = creator_only
        # The keyword in the rule name for fuzzy matching.
        self.keyword = keyword
        # The maximum number of records to return for this request.
        self.max_results = max_results
        # The pagination token used to retrieve the next page.
        self.next_token = next_token
        # The page number for pagination. Default value: 1.
        self.page = page
        # The number of entries to return per page.
        # 
        # > The maximum number of entries per page is 30.
        self.page_size = page_size
        # The effective tenant ID.
        self.tenant_id = tenant_id
        # Filters tasks by visibility scope. Multiple values can be selected. Valid values: PRIVATE (visible only to the creator and group owner), COLLABORATIVE (visible to specified collaboration members), and PUBLIC (visible to all group members). If this parameter is not specified or an empty list is passed, no filtering is applied. This parameter takes effect only at the group level (when collaborationGroupId is specified) and is ignored at the personal level.
        self.visibilities = visibilities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.creator_only is not None:
            result['creatorOnly'] = self.creator_only

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

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.visibilities is not None:
            result['visibilities'] = self.visibilities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('creatorOnly') is not None:
            self.creator_only = m.get('creatorOnly')

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

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('visibilities') is not None:
            self.visibilities = m.get('visibilities')

        return self

