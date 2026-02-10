# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSyncAssetTaskListResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeSyncAssetTaskListResponseBodyPageInfo = None,
        request_id: str = None,
        task_records: List[main_models.DescribeSyncAssetTaskListResponseBodyTaskRecords] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # The IDC scan tasks.
        self.task_records = task_records

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.task_records:
            for v1 in self.task_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TaskRecords'] = []
        if self.task_records is not None:
            for k1 in self.task_records:
                result['TaskRecords'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeSyncAssetTaskListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.task_records = []
        if m.get('TaskRecords') is not None:
            for k1 in m.get('TaskRecords'):
                temp_model = main_models.DescribeSyncAssetTaskListResponseBodyTaskRecords()
                self.task_records.append(temp_model.from_map(k1))

        return self

class DescribeSyncAssetTaskListResponseBodyTaskRecords(DaraModel):
    def __init__(
        self,
        asset_count: int = None,
        ip_segments: str = None,
        process_rate: int = None,
        root_task_id: str = None,
        task_end_time: int = None,
        task_name: str = None,
        task_start_time: int = None,
        task_status: str = None,
        task_type: str = None,
    ):
        # The number of assets that are detected by the task.
        self.asset_count = asset_count
        # The CIDR blocks that are used for scanning. Multiple CIDR blocks are separated by commas (,).
        self.ip_segments = ip_segments
        # The progress of the task, in percentage.
        self.process_rate = process_rate
        # The ID of the root task.
        self.root_task_id = root_task_id
        # The timestamp when the task ended.
        self.task_end_time = task_end_time
        # The name of the task.
        self.task_name = task_name
        # The timestamp when the task started. Unit: milliseconds.
        self.task_start_time = task_start_time
        # The status of the IDC scan task. Valid Values:
        # 
        # *   **INIT**: The task is not started.
        # *   **START**: The task is started.
        # *   **MESSAGE_SEND**: The command is sent.
        # *   **SUCCESS**: The task is complete.
        # *   **FAIL**: The task failed.
        # *   **TIMEOUT**: The task timed out.
        self.task_status = task_status
        # The type of the task. The value is fixed as **IDC_PROBE_SCAN**, which indicates an IDC scan task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_count is not None:
            result['AssetCount'] = self.asset_count

        if self.ip_segments is not None:
            result['IpSegments'] = self.ip_segments

        if self.process_rate is not None:
            result['ProcessRate'] = self.process_rate

        if self.root_task_id is not None:
            result['RootTaskId'] = self.root_task_id

        if self.task_end_time is not None:
            result['TaskEndTime'] = self.task_end_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetCount') is not None:
            self.asset_count = m.get('AssetCount')

        if m.get('IpSegments') is not None:
            self.ip_segments = m.get('IpSegments')

        if m.get('ProcessRate') is not None:
            self.process_rate = m.get('ProcessRate')

        if m.get('RootTaskId') is not None:
            self.root_task_id = m.get('RootTaskId')

        if m.get('TaskEndTime') is not None:
            self.task_end_time = m.get('TaskEndTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class DescribeSyncAssetTaskListResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of IDC scan tasks on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of IDC scan tasks per page. Default value: 20. If you leave this parameter empty, 20 IDC scan tasks are returned on each page.
        self.page_size = page_size
        # The total number of IDC scan tasks returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

