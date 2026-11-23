# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetContextDatabaseCreditUsageSummaryResponseBody(DaraModel):
    def __init__(
        self,
        buckets: List[main_models.GetContextDatabaseCreditUsageSummaryResponseBodyBuckets] = None,
        dimension: str = None,
        end_time: str = None,
        interval: str = None,
        request_id: str = None,
        start_time: str = None,
        total_credits: str = None,
        workspace_id: str = None,
    ):
        # The bucketing results, sorted by BucketStart, Item, and SubItem in sequence. Unpriced records are included in Quantity and RecordCount, but not in Credits.
        self.buckets = buckets
        # The query dimension. Valid values: Workspace (a single workspace) and Account (all workspaces under the caller account).
        self.dimension = dimension
        # The end time of the query range passed in the request, exclusive.
        self.end_time = end_time
        # The actual bucketing granularity used. Valid values: Hour (hourly) and Day (daily). If the request parameter is omitted, the automatically selected granularity is returned.
        self.interval = interval
        # The ID of the OpenAPI request, which is used to troubleshoot call issues.
        self.request_id = request_id
        # The start time of the query range passed in the request, inclusive.
        self.start_time = start_time
        # The total credit consumption of priced records that meet the filter conditions within the query range. The value is returned as a decimal string with up to 6 decimal places. 1 credit = 1 CNY. If there are no priced records, the string 0 is returned. Unpriced records are not included in the total amount. Do not treat this value as the final bill amount.
        self.total_credits = total_credits
        # The ID of the queried workspace. This parameter has a value only when Dimension is Workspace. It is empty for the account dimension.
        self.workspace_id = workspace_id

    def validate(self):
        if self.buckets:
            for v1 in self.buckets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Buckets'] = []
        if self.buckets is not None:
            for k1 in self.buckets:
                result['Buckets'].append(k1.to_map() if k1 else None)

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_credits is not None:
            result['TotalCredits'] = self.total_credits

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.buckets = []
        if m.get('Buckets') is not None:
            for k1 in m.get('Buckets'):
                temp_model = main_models.GetContextDatabaseCreditUsageSummaryResponseBodyBuckets()
                self.buckets.append(temp_model.from_map(k1))

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalCredits') is not None:
            self.total_credits = m.get('TotalCredits')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetContextDatabaseCreditUsageSummaryResponseBodyBuckets(DaraModel):
    def __init__(
        self,
        bucket_start: str = None,
        credits: str = None,
        item: str = None,
        quantity: int = None,
        record_count: int = None,
        sub_item: str = None,
        unit: str = None,
    ):
        # The start time of the bucket, in ISO 8601 UTC time format ending with Z.
        self.bucket_start = bucket_start
        # The total credit consumption of priced records in the bucket. The value is returned as a decimal string with up to 6 decimal places. 1 credit = 1 CNY. If all records are unpriced, the string 0 is returned.
        self.credits = credits
        # The billing item corresponding to the bucket. Valid values: KnowledgeBaseRead (knowledge base read), MemoryRead (memory read), MemoryWrite (memory write), KnowledgeBaseWriteToken (knowledge base write token), and ContextGrowth (context evolution).
        self.item = item
        # The total usage of all records in the bucket, including unpriced records. The unit is specified by Unit.
        self.quantity = quantity
        # The number of metering records in the bucket, including unpriced records.
        self.record_count = record_count
        # The context evolution sub-item. Recognized values include KnowledgeOrganization (knowledge organization), MemoryPromotion (memory promotion), KnowledgeReview (knowledge review), KnowledgeEvolution (knowledge evolution), and MemoryEvolution (memory evolution). For other billing items, missing sub-items, or unrecognized sub-items, null is returned.
        self.sub_item = sub_item
        # The unit of measurement. Valid values: Count (number of times), Token (number of tokens), and MicroCredit (one millionth of a credit).
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_start is not None:
            result['BucketStart'] = self.bucket_start

        if self.credits is not None:
            result['Credits'] = self.credits

        if self.item is not None:
            result['Item'] = self.item

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.record_count is not None:
            result['RecordCount'] = self.record_count

        if self.sub_item is not None:
            result['SubItem'] = self.sub_item

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketStart') is not None:
            self.bucket_start = m.get('BucketStart')

        if m.get('Credits') is not None:
            self.credits = m.get('Credits')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')

        if m.get('SubItem') is not None:
            self.sub_item = m.get('SubItem')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

