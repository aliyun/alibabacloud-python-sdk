# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetContextDatabaseCreditUsageSummaryRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: str = None,
        item: str = None,
        member_id: str = None,
        start_time: str = None,
        sub_item: str = None,
        workspace_id: str = None,
    ):
        # The end time of the query range, exclusive. This time must be later than StartTime. Use the ISO 8601 time format, such as 2026-10-15T00:00:00Z (UTC). The maximum time range is 7 days for hourly statistics and 31 days for daily statistics.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The bucketing granularity. Valid values: Hour (hourly) and Day (daily). The values are case-insensitive. If omitted, Hour is used by default for a time range of up to 7 days, and Day is used for a time range exceeding 7 days. The maximum time range is 7 days for Hour and 31 days for Day. If the limit is exceeded, InvalidParameter is returned.
        self.interval = interval
        # The billing item used to filter records. Supported values include KnowledgeBaseRead (knowledge base read), MemoryRead (memory read), MemoryWrite (memory write), KnowledgeBaseWriteToken (knowledge base write token), and ContextGrowth (context evolution). If omitted, all billing items that consume credits are included. Storage items or unlisted values return InvalidParameter.
        self.item = item
        # The member ID used to filter records. If specified, WorkspaceId must also be provided. Otherwise, InvalidParameter is returned. A member ID is unique only within its workspace. This parameter only filters data and does not change the caller identity. Records without a member ID are not matched. Results are still bucketed by time and billing item, and are not split by member.
        self.member_id = member_id
        # The start time of the query range, inclusive. Use the ISO 8601 time format, such as 2026-09-15T00:00:00Z (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The context evolution sub-item used to filter records. Supported values include KnowledgeOrganization (knowledge organization), MemoryPromotion (memory promotion), KnowledgeReview (knowledge review), KnowledgeEvolution (knowledge evolution), and MemoryEvolution (memory evolution). The values are case-sensitive. If only SubItem is provided, the billing item is automatically restricted to ContextGrowth. If other Item values are provided simultaneously or the sub-item is not in the list, InvalidParameter is returned.
        self.sub_item = sub_item
        # The ID of the workspace to query. If specified, only the data of this workspace under the caller account is queried. Locked workspaces can also be queried. If omitted, all workspaces under the caller account are queried.
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

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.item is not None:
            result['Item'] = self.item

        if self.member_id is not None:
            result['MemberId'] = self.member_id

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

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SubItem') is not None:
            self.sub_item = m.get('SubItem')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

