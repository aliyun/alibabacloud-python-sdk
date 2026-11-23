# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListContextDatabaseCreditUsageRecordsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        item: str = None,
        member_id: str = None,
        page: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        start_time: str = None,
        sub_item: str = None,
        workspace_id: str = None,
    ):
        # The end time of the query range, exclusive. It must be later than StartTime. Use the ISO 8601 time format, such as `2026-10-15T00:00:00Z` (UTC). The maximum length of the query range is 31 days. If the limit is exceeded, InvalidParameter is returned.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The billing item used to filter records. Valid values: KnowledgeBaseRead (knowledge base read), MemoryRead (memory base read), MemoryWrite (memory base write), KnowledgeBaseWriteToken (knowledge base write token), and ContextGrowth (context growth). If omitted, all billing items that consume credits are included. Storage items or unlisted values return InvalidParameter.
        self.item = item
        # The member ID used to filter records. If specified, WorkspaceId must also be provided. Otherwise, InvalidParameter is returned. A member ID is unique only within the workspace to which it belongs. This parameter only filters data and does not change the caller identity. Records without a member ID are not matched.
        self.member_id = member_id
        # The page number. Pages start from 1. Default value: 1.
        self.page = page
        # The maximum number of records to return per page. Valid values: 1 to 200. Default value: 50. The pagination offset, calculated as (Page - 1) × PageSize, must not exceed 10,000.
        self.page_size = page_size
        # The field by which to sort the records. Only credits is supported. If omitted, the records are sorted in descending order of request time. Specifying a sort field does not change the total number of filtered records.
        self.sort_by = sort_by
        # The sort order. Valid values: asc (ascending order) and desc (descending order). The values are case-insensitive. If SortBy is specified, the default value is desc. If only SortOrder is provided, InvalidParameter is returned. When sorting by credit, unpriced records are always placed at the end, and records with the same amount are sorted in descending order of request time.
        self.sort_order = sort_order
        # The start time of the query range, inclusive. Use the ISO 8601 time format, such as `2026-09-15T00:00:00Z` (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The context growth sub-item used to filter records. Valid values: KnowledgeOrganization (knowledge organization), MemoryPromotion (memory promotion), KnowledgeReview (knowledge review), KnowledgeEvolution (knowledge evolution), and MemoryEvolution (memory evolution). The values are case-sensitive. If only SubItem is provided, the billing item is automatically restricted to ContextGrowth. If other Item values are provided simultaneously or the sub-item is not in the list, InvalidParameter is returned.
        self.sub_item = sub_item
        # The ID of the workspace to query. If specified, only the data of this workspace under the caller account is queried, and locked workspaces can also be queried. If omitted, all workspaces under the caller account are queried.
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

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.sub_item is not None:
            result['SubItem'] = self.sub_item

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

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SubItem') is not None:
            self.sub_item = m.get('SubItem')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

