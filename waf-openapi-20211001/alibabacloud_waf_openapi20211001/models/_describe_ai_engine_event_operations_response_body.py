# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAiEngineEventOperationsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeAiEngineEventOperationsResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of event status change records, sorted in descending order by operation time.
        self.items = items
        # The number of entries to return on each page during paging in a paged query. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token. If a next page exists, this field returns a value.
        # > If this parameter returns a value, it indicates that a next page exists. You can use the returned **NextToken** as a request parameter to obtain the data on the next page until no value is returned, which indicates that all data is obtained.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of operation records for the event.
        self.total_count = total_count

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
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAiEngineEventOperationsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAiEngineEventOperationsResponseBodyItems(DaraModel):
    def __init__(
        self,
        from_status: str = None,
        operated_at: int = None,
        operation_id: str = None,
        to_status: str = None,
    ):
        # The event processing status before the modification. Valid values:
        # 
        # - **unhandled**: Unprocessed.
        # - **handling**: Processing.
        # - **handled**: Processed.
        self.from_status = from_status
        # The event operation time. The value is a UNIX timestamp in milliseconds.
        self.operated_at = operated_at
        # The ID of the operation record.
        self.operation_id = operation_id
        # The event processing status after the modification. Valid values:
        # 
        # - **unhandled**: Unprocessed.
        # - **handling**: Processing.
        # - **handled**: Processed.
        self.to_status = to_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_status is not None:
            result['FromStatus'] = self.from_status

        if self.operated_at is not None:
            result['OperatedAt'] = self.operated_at

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.to_status is not None:
            result['ToStatus'] = self.to_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromStatus') is not None:
            self.from_status = m.get('FromStatus')

        if m.get('OperatedAt') is not None:
            self.operated_at = m.get('OperatedAt')

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('ToStatus') is not None:
            self.to_status = m.get('ToStatus')

        return self

