# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fnf20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeMapRunResponseBody(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
        execution_name: str = None,
        item_counts: main_models.DescribeMapRunResponseBodyItemCounts = None,
        map_run_name: str = None,
        request_id: str = None,
        started_time: str = None,
        status: str = None,
        stopped_time: str = None,
        tolerated_failed_count: int = None,
        tolerated_failed_percentage: float = None,
    ):
        self.concurrency = concurrency
        self.execution_name = execution_name
        self.item_counts = item_counts
        self.map_run_name = map_run_name
        self.request_id = request_id
        self.started_time = started_time
        self.status = status
        self.stopped_time = stopped_time
        self.tolerated_failed_count = tolerated_failed_count
        self.tolerated_failed_percentage = tolerated_failed_percentage

    def validate(self):
        if self.item_counts:
            self.item_counts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name

        if self.item_counts is not None:
            result['ItemCounts'] = self.item_counts.to_map()

        if self.map_run_name is not None:
            result['MapRunName'] = self.map_run_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.started_time is not None:
            result['StartedTime'] = self.started_time

        if self.status is not None:
            result['Status'] = self.status

        if self.stopped_time is not None:
            result['StoppedTime'] = self.stopped_time

        if self.tolerated_failed_count is not None:
            result['ToleratedFailedCount'] = self.tolerated_failed_count

        if self.tolerated_failed_percentage is not None:
            result['ToleratedFailedPercentage'] = self.tolerated_failed_percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')

        if m.get('ItemCounts') is not None:
            temp_model = main_models.DescribeMapRunResponseBodyItemCounts()
            self.item_counts = temp_model.from_map(m.get('ItemCounts'))

        if m.get('MapRunName') is not None:
            self.map_run_name = m.get('MapRunName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoppedTime') is not None:
            self.stopped_time = m.get('StoppedTime')

        if m.get('ToleratedFailedCount') is not None:
            self.tolerated_failed_count = m.get('ToleratedFailedCount')

        if m.get('ToleratedFailedPercentage') is not None:
            self.tolerated_failed_percentage = m.get('ToleratedFailedPercentage')

        return self

class DescribeMapRunResponseBodyItemCounts(DaraModel):
    def __init__(
        self,
        aborted: int = None,
        failed: int = None,
        pending: int = None,
        running: int = None,
        succeed: int = None,
        total: int = None,
    ):
        self.aborted = aborted
        self.failed = failed
        self.pending = pending
        self.running = running
        self.succeed = succeed
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aborted is not None:
            result['Aborted'] = self.aborted

        if self.failed is not None:
            result['Failed'] = self.failed

        if self.pending is not None:
            result['Pending'] = self.pending

        if self.running is not None:
            result['Running'] = self.running

        if self.succeed is not None:
            result['Succeed'] = self.succeed

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aborted') is not None:
            self.aborted = m.get('Aborted')

        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Pending') is not None:
            self.pending = m.get('Pending')

        if m.get('Running') is not None:
            self.running = m.get('Running')

        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

