# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeSQLPlanTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[main_models.DescribeSQLPlanTaskResponseBodyTaskList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried task.
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for v1 in self.task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskList'] = []
        if self.task_list is not None:
            for k1 in self.task_list:
                result['TaskList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_list = []
        if m.get('TaskList') is not None:
            for k1 in m.get('TaskList'):
                temp_model = main_models.DescribeSQLPlanTaskResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k1))

        return self

class DescribeSQLPlanTaskResponseBodyTaskList(DaraModel):
    def __init__(
        self,
        elapsed_time: int = None,
        input_rows: int = None,
        input_size: int = None,
        operator_cost: int = None,
        output_rows: int = None,
        output_size: int = None,
        peak_memory: int = None,
        scan_cost: int = None,
        scan_rows: int = None,
        scan_size: int = None,
        state: str = None,
        task_id: int = None,
    ):
        # The time elapsed from when the task was created to when the task was complete. Unit: milliseconds.
        self.elapsed_time = elapsed_time
        # The number of input rows in the task.
        self.input_rows = input_rows
        # The amount of input data in the task. Unit: bytes.
        self.input_size = input_size
        # The total amount of time consumed by all operators in the task on a specific node. This parameter can be used to determine whether long tails occur in computing. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The number of output rows in the task.
        self.output_rows = output_rows
        # The amount of output data in the task. Unit: bytes.
        self.output_size = output_size
        # The peak memory of the task on a specific node. Unit: bytes.
        self.peak_memory = peak_memory
        # The amount of time consumed to scan data from a data source in the task. Unit: milliseconds.
        self.scan_cost = scan_cost
        # The number of rows scanned from a data source in the task.
        self.scan_rows = scan_rows
        # The amount of data scanned from a data source in the task. Unit: bytes.
        self.scan_size = scan_size
        # The final execution status of the task. Valid values:
        # 
        # *   FINISHED
        # *   CANCELED
        # *   ABORTED
        # *   FAILED
        self.state = state
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time

        if self.input_rows is not None:
            result['InputRows'] = self.input_rows

        if self.input_size is not None:
            result['InputSize'] = self.input_size

        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost

        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows

        if self.output_size is not None:
            result['OutputSize'] = self.output_size

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.scan_cost is not None:
            result['ScanCost'] = self.scan_cost

        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows

        if self.scan_size is not None:
            result['ScanSize'] = self.scan_size

        if self.state is not None:
            result['State'] = self.state

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')

        if m.get('InputRows') is not None:
            self.input_rows = m.get('InputRows')

        if m.get('InputSize') is not None:
            self.input_size = m.get('InputSize')

        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')

        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')

        if m.get('OutputSize') is not None:
            self.output_size = m.get('OutputSize')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('ScanCost') is not None:
            self.scan_cost = m.get('ScanCost')

        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')

        if m.get('ScanSize') is not None:
            self.scan_size = m.get('ScanSize')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

