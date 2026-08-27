# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScheduledTasksShrinkRequest(DaraModel):
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
        visibilities_shrink: str = None,
    ):
        # The ID of the collaboration group (such as cg_101). If specified, a group task is created (the caller must be a valid group member). If left empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # Specifies whether to return only tasks created by the caller. This parameter takes effect only in the group dimension (in the personal dimension, only the caller\\"s own tasks are returned). If not specified, no filtering is applied.
        self.creator_only = creator_only
        # The keyword of the rule name, used for fuzzy match.
        self.keyword = keyword
        # The maximum number of entries returned in this request.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The page number. Default value: 1.
        self.page = page
        # The number of entries per page.
        # 
        # > The maximum number of entries per page is 30.
        self.page_size = page_size
        # The tenant ID that takes effect.
        self.tenant_id = tenant_id
        # Filters by visibility. Valid values:
        # - PRIVATE: visible only to the creator and group owner.
        # - COLLABORATIVE: visible to specified collaborators.
        # - PUBLIC: visible to all group members.
        # 
        # If not specified or an empty list is passed, no filtering is applied. This parameter takes effect only in the group dimension (when collaborationGroupId is specified) and is ignored in the personal dimension.
        self.visibilities_shrink = visibilities_shrink

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

        if self.visibilities_shrink is not None:
            result['visibilities'] = self.visibilities_shrink

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
            self.visibilities_shrink = m.get('visibilities')

        return self

