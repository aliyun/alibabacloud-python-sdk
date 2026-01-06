# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListApsOptimizationTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListApsOptimizationTasksResponseBodyItems] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The HTTP status code or the error code.
        self.code = code
        # The response code. The status code 200 indicates that the request was successful.
        self.http_status_code = http_status_code
        # The queried optimization jobs.
        self.items = items
        # The returned message. Valid values:
        # 
        # *   If the request was successful, a success message is returned.****
        # *   If the request failed, an error message is returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The total number of entries returned.
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
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListApsOptimizationTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApsOptimizationTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        compute_unit: str = None,
        created_time: str = None,
        dbcluster_id: str = None,
        modified_time: str = None,
        strategy_type: str = None,
        task_desc: str = None,
        task_duration: int = None,
        task_id: str = None,
        task_message: str = None,
        task_status: str = None,
    ):
        # The computing resources used by the optimization job.
        self.compute_unit = compute_unit
        # The time when the optimization job was created.
        self.created_time = created_time
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The time when the optimization job was modified.
        self.modified_time = modified_time
        # The type of the lifecycle management policy.
        self.strategy_type = strategy_type
        # The description of the optimization job.
        self.task_desc = task_desc
        # The execution duration of the optimization job.
        self.task_duration = task_duration
        # The job ID.
        self.task_id = task_id
        # The error message.
        self.task_message = task_message
        # The execution status. Valid values:
        # 
        # 1.  NEW
        # 2.  RUNNING
        # 3.  SUCCESS
        # 4.  STOPPED
        # 5.  FAILED
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_unit is not None:
            result['ComputeUnit'] = self.compute_unit

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type

        if self.task_desc is not None:
            result['TaskDesc'] = self.task_desc

        if self.task_duration is not None:
            result['TaskDuration'] = self.task_duration

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_message is not None:
            result['TaskMessage'] = self.task_message

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeUnit') is not None:
            self.compute_unit = m.get('ComputeUnit')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')

        if m.get('TaskDesc') is not None:
            self.task_desc = m.get('TaskDesc')

        if m.get('TaskDuration') is not None:
            self.task_duration = m.get('TaskDuration')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskMessage') is not None:
            self.task_message = m.get('TaskMessage')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

