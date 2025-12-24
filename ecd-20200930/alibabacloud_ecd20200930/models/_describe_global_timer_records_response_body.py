# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalTimerRecordsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        next_token: str = None,
        request_id: str = None,
        results: List[main_models.DescribeGlobalTimerRecordsResponseBodyResults] = None,
    ):
        # The total number of entries returned.
        self.count = count
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The response parameters.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.DescribeGlobalTimerRecordsResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class DescribeGlobalTimerRecordsResponseBodyResults(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        batch_id: str = None,
        context: str = None,
        create_time: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        display_result_name: str = None,
        finish_time: str = None,
        region_id: str = None,
        retryable: bool = None,
        timer_group_id: str = None,
        timer_record_id: str = None,
        timer_result: str = None,
        timer_type: str = None,
    ):
        self.action_type = action_type
        # The ID of the batch in which the scheduled task is executed.
        self.batch_id = batch_id
        self.context = context
        # The time when the execution record was created.
        self.create_time = create_time
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The cloud computer name.
        self.desktop_name = desktop_name
        self.display_result_name = display_result_name
        # The time when the scheduled task ended.
        self.finish_time = finish_time
        # The region ID.
        self.region_id = region_id
        self.retryable = retryable
        # The ID of the scheduled task group.
        self.timer_group_id = timer_group_id
        self.timer_record_id = timer_record_id
        # The execution result of the scheduled task.
        self.timer_result = timer_result
        # The type of the scheduled task.
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.context is not None:
            result['Context'] = self.context

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.display_result_name is not None:
            result['DisplayResultName'] = self.display_result_name

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.retryable is not None:
            result['Retryable'] = self.retryable

        if self.timer_group_id is not None:
            result['TimerGroupId'] = self.timer_group_id

        if self.timer_record_id is not None:
            result['TimerRecordId'] = self.timer_record_id

        if self.timer_result is not None:
            result['TimerResult'] = self.timer_result

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('Context') is not None:
            self.context = m.get('Context')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('DisplayResultName') is not None:
            self.display_result_name = m.get('DisplayResultName')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Retryable') is not None:
            self.retryable = m.get('Retryable')

        if m.get('TimerGroupId') is not None:
            self.timer_group_id = m.get('TimerGroupId')

        if m.get('TimerRecordId') is not None:
            self.timer_record_id = m.get('TimerRecordId')

        if m.get('TimerResult') is not None:
            self.timer_result = m.get('TimerResult')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

