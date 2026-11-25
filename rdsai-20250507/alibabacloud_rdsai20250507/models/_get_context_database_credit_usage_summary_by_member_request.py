# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetContextDatabaseCreditUsageSummaryByMemberRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        item: str = None,
        member_id: str = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
        workspace_id: str = None,
    ):
        # The end time of the query interval, exclusive. It must be later than `StartTime`. Use the ISO 8601 time format, such as `2026-10-08T00:00:00Z` (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The billing item used to filter records. Supported values include KnowledgeBaseRead (knowledge base read), MemoryRead (memory read), MemoryWrite (memory write), KnowledgeBaseWriteToken (knowledge base write token), and ContextGrowth (context growth). If omitted, all billing items that consume credits are included. Specifying storage items or unlisted values returns an `InvalidParameter` error.
        self.item = item
        # The member ID used to filter the aggregated results. If specified, only this member is analyzed without changing the caller identity. An empty list is returned if no matching records are found.
        self.member_id = member_id
        # The page number. Pages start from 1. Default value: 1.
        self.page = page
        # The maximum number of members to return per page. Valid values: 1 to 200. Default value: 50.
        self.page_size = page_size
        # The start time of the query interval, inclusive. Use the ISO 8601 time format, such as `2026-10-01T00:00:00Z` (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The ID of the workspace to be analyzed. This parameter is required. The workspace must belong to the caller\"s account. Locked workspaces can still be queried. Member IDs are unique only within their respective workspaces, and cross-workspace ranking is not supported.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.item is not None:
            result['Item'] = self.item

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

