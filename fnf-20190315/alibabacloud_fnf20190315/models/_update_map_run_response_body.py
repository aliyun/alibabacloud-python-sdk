# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMapRunResponseBody(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
        execution_name: str = None,
        flow_name: str = None,
        map_run_name: str = None,
        request_id: str = None,
        tolerated_failed_count: int = None,
        tolerated_failed_percentage: float = None,
    ):
        self.concurrency = concurrency
        self.execution_name = execution_name
        self.flow_name = flow_name
        self.map_run_name = map_run_name
        # Id of the request
        self.request_id = request_id
        self.tolerated_failed_count = tolerated_failed_count
        self.tolerated_failed_percentage = tolerated_failed_percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.map_run_name is not None:
            result['MapRunName'] = self.map_run_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('MapRunName') is not None:
            self.map_run_name = m.get('MapRunName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ToleratedFailedCount') is not None:
            self.tolerated_failed_count = m.get('ToleratedFailedCount')

        if m.get('ToleratedFailedPercentage') is not None:
            self.tolerated_failed_percentage = m.get('ToleratedFailedPercentage')

        return self

