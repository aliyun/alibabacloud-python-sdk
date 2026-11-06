# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertAggregationsRequest(DaraModel):
    def __init__(
        self,
        aggregation_type: str = None,
        end_time: int = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        query_condition: str = None,
        query_view_id: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        start_time: int = None,
    ):
        # The aggregation method.
        self.aggregation_type = aggregation_type
        # The time when the alert ended.
        self.end_time = end_time
        # The language of the response message. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return for this request.
        self.max_results = max_results
        # The token for the next query. If this is the first query or no subsequent query is required, you do not need to specify this parameter. If a subsequent query is required, set the value to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The current page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The query filter conditions in JSON format. Valid values:
        # 
        # - `{"Type":"maxCost", "Value":"100"}`: The top 100 queries that take the longest time.
        # - `{"Type":"status","Value":"finished"}`: Completed queries.
        # - `{"Type":"status","Value":"running"}`: Running queries.
        # - `{"Type":"cost","Min":"30","Max":"50"}`: Custom duration queries. You can specify the minimum and maximum query durations. **Min** specifies the minimum duration, and **Max** specifies the maximum duration. Unit: milliseconds.
        #     - If only **Min** is specified, the query returns queries whose execution duration is greater than the specified value.
        #     - If only **Max** is specified, the query returns queries whose execution duration is less than the specified value.
        #     - If both **Min** and **Max** are specified, the query returns queries whose execution duration is greater than or equal to the value of **Min** and less than or equal to the value of **Max**.
        self.query_condition = query_condition
        # The unique identifier of the query view.
        self.query_view_id = query_view_id
        # The region where the data management center of Threat Analysis is located. Select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland.
        # - ap-southeast-1: Assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the member whose view the administrator switches to.
        self.role_for = role_for
        # The view type. Valid values:
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # - 1: The view of all accounts in the enterprise.
        self.role_type = role_type
        # The time when the alert first occurred.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregation_type is not None:
            result['AggregationType'] = self.aggregation_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition

        if self.query_view_id is not None:
            result['QueryViewId'] = self.query_view_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationType') is not None:
            self.aggregation_type = m.get('AggregationType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')

        if m.get('QueryViewId') is not None:
            self.query_view_id = m.get('QueryViewId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

