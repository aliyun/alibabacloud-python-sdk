# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeDataFlowSubTasksResponseBody(DaraModel):
    def __init__(
        self,
        data_flow_sub_task: main_models.DescribeDataFlowSubTasksResponseBodyDataFlowSubTask = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.data_flow_sub_task = data_flow_sub_task
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_flow_sub_task:
            self.data_flow_sub_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_flow_sub_task is not None:
            result['DataFlowSubTask'] = self.data_flow_sub_task.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataFlowSubTask') is not None:
            temp_model = main_models.DescribeDataFlowSubTasksResponseBodyDataFlowSubTask()
            self.data_flow_sub_task = temp_model.from_map(m.get('DataFlowSubTask'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDataFlowSubTasksResponseBodyDataFlowSubTask(DaraModel):
    def __init__(
        self,
        data_flow_sub_task: List[main_models.DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTask] = None,
    ):
        self.data_flow_sub_task = data_flow_sub_task

    def validate(self):
        if self.data_flow_sub_task:
            for v1 in self.data_flow_sub_task:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataFlowSubTask'] = []
        if self.data_flow_sub_task is not None:
            for k1 in self.data_flow_sub_task:
                result['DataFlowSubTask'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_flow_sub_task = []
        if m.get('DataFlowSubTask') is not None:
            for k1 in m.get('DataFlowSubTask'):
                temp_model = main_models.DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTask()
                self.data_flow_sub_task.append(temp_model.from_map(k1))

        return self

class DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTask(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_flow_id: str = None,
        data_flow_sub_task_id: str = None,
        data_flow_task_id: str = None,
        dst_file_path: str = None,
        end_time: str = None,
        error_msg: str = None,
        file_detail: main_models.DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskFileDetail = None,
        file_system_id: str = None,
        progress: int = None,
        progress_stats: main_models.DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskProgressStats = None,
        src_file_path: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.data_flow_id = data_flow_id
        self.data_flow_sub_task_id = data_flow_sub_task_id
        self.data_flow_task_id = data_flow_task_id
        self.dst_file_path = dst_file_path
        self.end_time = end_time
        self.error_msg = error_msg
        self.file_detail = file_detail
        self.file_system_id = file_system_id
        self.progress = progress
        self.progress_stats = progress_stats
        self.src_file_path = src_file_path
        self.start_time = start_time
        self.status = status

    def validate(self):
        if self.file_detail:
            self.file_detail.validate()
        if self.progress_stats:
            self.progress_stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.data_flow_sub_task_id is not None:
            result['DataFlowSubTaskId'] = self.data_flow_sub_task_id

        if self.data_flow_task_id is not None:
            result['DataFlowTaskId'] = self.data_flow_task_id

        if self.dst_file_path is not None:
            result['DstFilePath'] = self.dst_file_path

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.file_detail is not None:
            result['FileDetail'] = self.file_detail.to_map()

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.progress_stats is not None:
            result['ProgressStats'] = self.progress_stats.to_map()

        if self.src_file_path is not None:
            result['SrcFilePath'] = self.src_file_path

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('DataFlowSubTaskId') is not None:
            self.data_flow_sub_task_id = m.get('DataFlowSubTaskId')

        if m.get('DataFlowTaskId') is not None:
            self.data_flow_task_id = m.get('DataFlowTaskId')

        if m.get('DstFilePath') is not None:
            self.dst_file_path = m.get('DstFilePath')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('FileDetail') is not None:
            temp_model = main_models.DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskFileDetail()
            self.file_detail = temp_model.from_map(m.get('FileDetail'))

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ProgressStats') is not None:
            temp_model = main_models.DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskProgressStats()
            self.progress_stats = temp_model.from_map(m.get('ProgressStats'))

        if m.get('SrcFilePath') is not None:
            self.src_file_path = m.get('SrcFilePath')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskProgressStats(DaraModel):
    def __init__(
        self,
        actual_bytes: int = None,
        average_speed: int = None,
        bytes_done: int = None,
        bytes_total: int = None,
    ):
        self.actual_bytes = actual_bytes
        self.average_speed = average_speed
        self.bytes_done = bytes_done
        self.bytes_total = bytes_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_bytes is not None:
            result['ActualBytes'] = self.actual_bytes

        if self.average_speed is not None:
            result['AverageSpeed'] = self.average_speed

        if self.bytes_done is not None:
            result['BytesDone'] = self.bytes_done

        if self.bytes_total is not None:
            result['BytesTotal'] = self.bytes_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualBytes') is not None:
            self.actual_bytes = m.get('ActualBytes')

        if m.get('AverageSpeed') is not None:
            self.average_speed = m.get('AverageSpeed')

        if m.get('BytesDone') is not None:
            self.bytes_done = m.get('BytesDone')

        if m.get('BytesTotal') is not None:
            self.bytes_total = m.get('BytesTotal')

        return self

class DescribeDataFlowSubTasksResponseBodyDataFlowSubTaskDataFlowSubTaskFileDetail(DaraModel):
    def __init__(
        self,
        checksum: str = None,
        modify_time: int = None,
        size: int = None,
    ):
        self.checksum = checksum
        self.modify_time = modify_time
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checksum is not None:
            result['Checksum'] = self.checksum

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checksum') is not None:
            self.checksum = m.get('Checksum')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

