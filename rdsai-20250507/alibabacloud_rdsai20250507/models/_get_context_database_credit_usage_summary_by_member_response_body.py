# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetContextDatabaseCreditUsageSummaryByMemberResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        items: List[main_models.GetContextDatabaseCreditUsageSummaryByMemberResponseBodyItems] = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
        total: int = None,
        workspace_id: str = None,
    ):
        # The end time of the query range passed in the request, exclusive.
        self.end_time = end_time
        # The member summaries on the current page, sorted in descending order of total credit consumption. Each record covers the entire query range.
        self.items = items
        # The actual page number used for the query.
        self.page = page
        # The actual number of items per page used for the query.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The start time of the query range passed in the request, inclusive.
        self.start_time = start_time
        # The total number of members that match the filter criteria. This is not the number of metering records and is not affected by pagination.
        self.total = total
        # The ID of the workspace queried.
        self.workspace_id = workspace_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total is not None:
            result['Total'] = self.total

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetContextDatabaseCreditUsageSummaryByMemberResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetContextDatabaseCreditUsageSummaryByMemberResponseBodyItems(DaraModel):
    def __init__(
        self,
        credits: str = None,
        member_id: str = None,
        quantity: int = None,
        record_count: int = None,
    ):
        # The total credit consumption of priced records for the member. Returned as a decimal string with up to 6 decimal places. 1 credit equals 1 CNY. The value is null if there are no priced records.
        self.credits = credits
        # The member ID. Historical or system records may not have a member ID.
        self.member_id = member_id
        # The total metered quantity of records that match the filter criteria for the member, including unpriced records. To view the usage of a specific billable item, specify Item in the request.
        self.quantity = quantity
        # The number of metering records that match the filter criteria for the member, including unpriced records.
        self.record_count = record_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credits is not None:
            result['Credits'] = self.credits

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credits') is not None:
            self.credits = m.get('Credits')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        return self

