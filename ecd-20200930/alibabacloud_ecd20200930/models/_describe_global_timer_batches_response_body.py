# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalTimerBatchesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        next_token: str = None,
        request_id: str = None,
        results: List[main_models.DescribeGlobalTimerBatchesResponseBodyResults] = None,
    ):
        self.count = count
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
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
                temp_model = main_models.DescribeGlobalTimerBatchesResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class DescribeGlobalTimerBatchesResponseBodyResults(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        create_time: str = None,
        failed_count: int = None,
        running_count: int = None,
        skipped_count: int = None,
        succeed_count: int = None,
        timer_type: str = None,
    ):
        self.batch_id = batch_id
        self.create_time = create_time
        self.failed_count = failed_count
        self.running_count = running_count
        self.skipped_count = skipped_count
        self.succeed_count = succeed_count
        self.timer_type = timer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.running_count is not None:
            result['RunningCount'] = self.running_count

        if self.skipped_count is not None:
            result['SkippedCount'] = self.skipped_count

        if self.succeed_count is not None:
            result['SucceedCount'] = self.succeed_count

        if self.timer_type is not None:
            result['TimerType'] = self.timer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('RunningCount') is not None:
            self.running_count = m.get('RunningCount')

        if m.get('SkippedCount') is not None:
            self.skipped_count = m.get('SkippedCount')

        if m.get('SucceedCount') is not None:
            self.succeed_count = m.get('SucceedCount')

        if m.get('TimerType') is not None:
            self.timer_type = m.get('TimerType')

        return self

