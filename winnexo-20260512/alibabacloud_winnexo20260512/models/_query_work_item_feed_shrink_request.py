# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryWorkItemFeedShrinkRequest(DaraModel):
    def __init__(
        self,
        business_statuses_shrink: str = None,
        collaboration_group_id: str = None,
        cursor: str = None,
        item_types_shrink: str = None,
        keyword: str = None,
        page_size: int = None,
        priorities_shrink: str = None,
        scope: str = None,
        source_task_id: str = None,
        tenant_id: str = None,
        view: str = None,
    ):
        # The business status filter (seven states).
        self.business_statuses_shrink = business_statuses_shrink
        # The ID of the collaboration workspace.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The pagination cursor. Use the nextCursor value from the previous response.
        self.cursor = cursor
        # The work item type filter.
        self.item_types_shrink = item_types_shrink
        # The keyword for fuzzy search in the title or description.
        self.keyword = keyword
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size
        # The priority filter.
        self.priorities_shrink = priorities_shrink
        # The personal scope filter.
        self.scope = scope
        # The ID of the source task. If specified, the flat sub-items of the task are returned.
        self.source_task_id = source_task_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The view type. Valid values: FLAT (flat view) and TREE (task grouping).
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_statuses_shrink is not None:
            result['businessStatuses'] = self.business_statuses_shrink

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.cursor is not None:
            result['cursor'] = self.cursor

        if self.item_types_shrink is not None:
            result['itemTypes'] = self.item_types_shrink

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.priorities_shrink is not None:
            result['priorities'] = self.priorities_shrink

        if self.scope is not None:
            result['scope'] = self.scope

        if self.source_task_id is not None:
            result['sourceTaskId'] = self.source_task_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.view is not None:
            result['view'] = self.view

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessStatuses') is not None:
            self.business_statuses_shrink = m.get('businessStatuses')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('itemTypes') is not None:
            self.item_types_shrink = m.get('itemTypes')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('priorities') is not None:
            self.priorities_shrink = m.get('priorities')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('sourceTaskId') is not None:
            self.source_task_id = m.get('sourceTaskId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('view') is not None:
            self.view = m.get('view')

        return self

