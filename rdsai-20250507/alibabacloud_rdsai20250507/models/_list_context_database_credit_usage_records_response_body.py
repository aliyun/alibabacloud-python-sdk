# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListContextDatabaseCreditUsageRecordsResponseBody(DaraModel):
    def __init__(
        self,
        dimension: str = None,
        end_time: str = None,
        page: int = None,
        page_size: int = None,
        records: List[main_models.ListContextDatabaseCreditUsageRecordsResponseBodyRecords] = None,
        request_id: str = None,
        start_time: str = None,
        total: int = None,
        workspace_id: str = None,
    ):
        # The query dimension. Valid values: Workspace indicates a single workspace, and Account indicates all workspaces under the caller account.
        self.dimension = dimension
        # The end time of the query range passed in the request, exclusive.
        self.end_time = end_time
        # The actual page number used for this query.
        self.page = page
        # The actual page size used for this query.
        self.page_size = page_size
        # The metering records on the current page. If SortBy is not specified, the records are sorted in descending order of request time.
        self.records = records
        # The ID of the OpenAPI request, which is used to troubleshoot call issues.
        self.request_id = request_id
        # The start time of the query range passed in the request, inclusive.
        self.start_time = start_time
        # The total number of metering records that match the filter conditions, which is not affected by pagination.
        self.total = total
        # The ID of the queried workspace. This parameter has a value only when Dimension is Workspace. It is empty for the account dimension.
        self.workspace_id = workspace_id

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

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
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListContextDatabaseCreditUsageRecordsResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ListContextDatabaseCreditUsageRecordsResponseBodyRecords(DaraModel):
    def __init__(
        self,
        credits: str = None,
        item: str = None,
        member_id: str = None,
        quantity: int = None,
        request_time: str = None,
        sub_item: str = None,
        unit: str = None,
        workspace_id: str = None,
    ):
        # The credit consumption of this record. It is returned as a decimal string with up to 6 decimal places. 1 credit = 1 CNY. The amount is recorded at the time of metering and does not change with subsequent price adjustments. It is null when unpriced, which does not indicate zero consumption.
        self.credits = credits
        # The billing item of this record. Valid values: KnowledgeBaseRead (knowledge base read), MemoryRead (memory base read), MemoryWrite (memory base write), KnowledgeBaseWriteToken (knowledge base write token), and ContextGrowth (context growth).
        self.item = item
        # The ID of the member that generated this record. Historical or system records may not have a member ID, in which case null is returned.
        self.member_id = member_id
        # The usage of this record. The unit is specified by Unit in the same record.
        self.quantity = quantity
        # The request time when this metering record was generated, in ISO 8601 UTC time format ending with Z.
        self.request_time = request_time
        # The context growth sub-item. Recognized values include KnowledgeOrganization (knowledge organization), MemoryPromotion (memory promotion), KnowledgeReview (knowledge review), KnowledgeEvolution (knowledge evolution), and MemoryEvolution (memory evolution). null is returned for other billing items, missing sub-items, or unrecognized sub-items.
        self.sub_item = sub_item
        # The metering unit. Valid values: Count indicates the number of times, Token indicates the number of tokens, and MicroCredit indicates one millionth of a credit.
        self.unit = unit
        # The ID of the workspace to which this record belongs. Even if queried by account, each record still indicates its workspace.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credits is not None:
            result['Credits'] = self.credits

        if self.item is not None:
            result['Item'] = self.item

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.request_time is not None:
            result['RequestTime'] = self.request_time

        if self.sub_item is not None:
            result['SubItem'] = self.sub_item

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credits') is not None:
            self.credits = m.get('Credits')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')

        if m.get('SubItem') is not None:
            self.sub_item = m.get('SubItem')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

