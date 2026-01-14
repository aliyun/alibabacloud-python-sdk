# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryComponentPerformanceRequest(DaraModel):
    def __init__(
        self,
        cost_time_avg_min: int = None,
        page_num: int = None,
        page_size: int = None,
        query_type: str = None,
        report_id: str = None,
        resource_type: str = None,
        workspace_id: str = None,
    ):
        # The average duration (minutes).
        self.cost_time_avg_min = cost_time_avg_min
        # The current page number of the workspace member list:
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
        self.page_num = page_num
        # The number of rows per page in a paged query.
        # 
        # *   Default value: 10.
        # *   Maximum value: 1,000.
        self.page_size = page_size
        # The query type. Valid values:
        # 
        # *   **lastDay**: Yesterday
        # *   **sevenDays**: Within seven days
        # *   **thirtyDays**: Within 30 days
        # 
        # This parameter is required.
        self.query_type = query_type
        # The ID of the work. The works here include BI portal, dashboards, spreadsheets, and self-service access.
        self.report_id = report_id
        # The resource types.
        self.resource_type = resource_type
        # The workspace ID.
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
        if self.cost_time_avg_min is not None:
            result['CostTimeAvgMin'] = self.cost_time_avg_min

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTimeAvgMin') is not None:
            self.cost_time_avg_min = m.get('CostTimeAvgMin')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

