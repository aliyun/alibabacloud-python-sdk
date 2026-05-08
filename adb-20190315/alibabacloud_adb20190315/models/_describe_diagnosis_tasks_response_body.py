# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosisTasksResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[main_models.DescribeDiagnosisTasksResponseBodyTaskList] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried tasks.
        self.task_list = task_list
        # The total number of tasks in the stage.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_list = []
        if m.get('TaskList') is not None:
            for k1 in m.get('TaskList'):
                temp_model = main_models.DescribeDiagnosisTasksResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiagnosisTasksResponseBodyTaskList(DaraModel):
    def __init__(
        self,
        compute_time_ratio: str = None,
        drivers: str = None,
        elapsed_time: int = None,
        input_data_size: int = None,
        input_rows: int = None,
        operator_cost: int = None,
        output_data_size: int = None,
        output_rows: int = None,
        peak_memory: int = None,
        queued_time: str = None,
        scan_cost: int = None,
        scan_data_size: int = None,
        scan_rows: int = None,
        state: str = None,
        task_create_time: int = None,
        task_end_time: int = None,
        task_host: str = None,
        task_id: str = None,
    ):
        # The compute time ratio, which can be used to determine whether the task is really time-consuming. This parameter can be calculated by using the following formula: OperatorCost/Drivers/ElapsedTime. A greater value indicates that the task was executed for computing for most of the task time. A less value indicates that the task was waiting for scheduling or blocked due to other reasons for most of the task time.
        self.compute_time_ratio = compute_time_ratio
        # The number of tasks that can be executed concurrently.
        self.drivers = drivers
        # The amount of time that elapsed from when the task was created to when the task was completed. Unit: milliseconds.
        self.elapsed_time = elapsed_time
        # The amount of input data in the task. Unit: bytes.
        self.input_data_size = input_data_size
        # The number of input rows in the task.
        self.input_rows = input_rows
        # The total amount of time that is consumed by all operators in the task on a node. This parameter can be used to determine whether long tails occur in computing. Unit: milliseconds.
        self.operator_cost = operator_cost
        # The amount of output data in the task. Unit: bytes.
        self.output_data_size = output_data_size
        # The number of output rows in the task.
        self.output_rows = output_rows
        # The peak memory of the task. Unit: bytes.
        self.peak_memory = peak_memory
        # The queuing duration of the task. Unit: milliseconds.
        self.queued_time = queued_time
        # The amount of time that is consumed to scan data from a data source in the task. Unit: milliseconds.
        self.scan_cost = scan_cost
        # The amount of scanned data in the task. Unit: bytes.
        self.scan_data_size = scan_data_size
        # The number of rows that are scanned from a data source in the task.
        self.scan_rows = scan_rows
        # The final execution state of the task. Valid values:
        # 
        # *   FINISHED
        # *   CANCELED
        # *   ABORTED
        # *   FAILED
        self.state = state
        # The timestamp when the task was created.
        self.task_create_time = task_create_time
        # The timestamp when the task ends.
        self.task_end_time = task_end_time
        # The IP address of the host where the task was executed.
        self.task_host = task_host
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_time_ratio is not None:
            result['ComputeTimeRatio'] = self.compute_time_ratio

        if self.drivers is not None:
            result['Drivers'] = self.drivers

        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time

        if self.input_data_size is not None:
            result['InputDataSize'] = self.input_data_size

        if self.input_rows is not None:
            result['InputRows'] = self.input_rows

        if self.operator_cost is not None:
            result['OperatorCost'] = self.operator_cost

        if self.output_data_size is not None:
            result['OutputDataSize'] = self.output_data_size

        if self.output_rows is not None:
            result['OutputRows'] = self.output_rows

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.queued_time is not None:
            result['QueuedTime'] = self.queued_time

        if self.scan_cost is not None:
            result['ScanCost'] = self.scan_cost

        if self.scan_data_size is not None:
            result['ScanDataSize'] = self.scan_data_size

        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows

        if self.state is not None:
            result['State'] = self.state

        if self.task_create_time is not None:
            result['TaskCreateTime'] = self.task_create_time

        if self.task_end_time is not None:
            result['TaskEndTime'] = self.task_end_time

        if self.task_host is not None:
            result['TaskHost'] = self.task_host

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeTimeRatio') is not None:
            self.compute_time_ratio = m.get('ComputeTimeRatio')

        if m.get('Drivers') is not None:
            self.drivers = m.get('Drivers')

        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')

        if m.get('InputDataSize') is not None:
            self.input_data_size = m.get('InputDataSize')

        if m.get('InputRows') is not None:
            self.input_rows = m.get('InputRows')

        if m.get('OperatorCost') is not None:
            self.operator_cost = m.get('OperatorCost')

        if m.get('OutputDataSize') is not None:
            self.output_data_size = m.get('OutputDataSize')

        if m.get('OutputRows') is not None:
            self.output_rows = m.get('OutputRows')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('QueuedTime') is not None:
            self.queued_time = m.get('QueuedTime')

        if m.get('ScanCost') is not None:
            self.scan_cost = m.get('ScanCost')

        if m.get('ScanDataSize') is not None:
            self.scan_data_size = m.get('ScanDataSize')

        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskCreateTime') is not None:
            self.task_create_time = m.get('TaskCreateTime')

        if m.get('TaskEndTime') is not None:
            self.task_end_time = m.get('TaskEndTime')

        if m.get('TaskHost') is not None:
            self.task_host = m.get('TaskHost')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

