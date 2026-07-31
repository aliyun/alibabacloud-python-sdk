# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class QueryFormationInstsByTaskIDResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryFormationInstsByTaskIDResponseBodyData] = None,
        http_status_code: int = None,
        items: List[Dict[str, Any]] = None,
        message: str = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: str = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The returned task list.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The task list.
        self.items = items
        # The response message. OK is returned if the request was successful.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The total number of pages.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.items is not None:
            result['Items'] = self.items

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryFormationInstsByTaskIDResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Items') is not None:
            self.items = m.get('Items')

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

class QueryFormationInstsByTaskIDResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        last_task_inst_cost_time: str = None,
        last_task_inst_id: str = None,
        last_task_inst_message: str = None,
        last_task_inst_state: str = None,
        schedule_state: str = None,
        schema: str = None,
        source_type: str = None,
        sync_time: str = None,
        task_id: str = None,
        task_name: str = None,
        task_type: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The execution duration of the most recent task.
        self.last_task_inst_cost_time = last_task_inst_cost_time
        # The instance ID of the most recent task.
        self.last_task_inst_id = last_task_inst_id
        # The error message of the most recent task.
        self.last_task_inst_message = last_task_inst_message
        # The instance status of the most recent node.
        self.last_task_inst_state = last_task_inst_state
        # The task status.
        self.schedule_state = schedule_state
        # The schema ID assigned to the instance by the system.
        self.schema = schema
        # The task source. Valid values:
        # - **system**: system.
        # - **custom**: custom.
        self.source_type = source_type
        # The synchronization time, accurate to milliseconds. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.sync_time = sync_time
        # The task ID.
        self.task_id = task_id
        # The task name.
        self.task_name = task_name
        # The task type.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.last_task_inst_cost_time is not None:
            result['LastTaskInstCostTime'] = self.last_task_inst_cost_time

        if self.last_task_inst_id is not None:
            result['LastTaskInstID'] = self.last_task_inst_id

        if self.last_task_inst_message is not None:
            result['LastTaskInstMessage'] = self.last_task_inst_message

        if self.last_task_inst_state is not None:
            result['LastTaskInstState'] = self.last_task_inst_state

        if self.schedule_state is not None:
            result['ScheduleState'] = self.schedule_state

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.sync_time is not None:
            result['SyncTime'] = self.sync_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LastTaskInstCostTime') is not None:
            self.last_task_inst_cost_time = m.get('LastTaskInstCostTime')

        if m.get('LastTaskInstID') is not None:
            self.last_task_inst_id = m.get('LastTaskInstID')

        if m.get('LastTaskInstMessage') is not None:
            self.last_task_inst_message = m.get('LastTaskInstMessage')

        if m.get('LastTaskInstState') is not None:
            self.last_task_inst_state = m.get('LastTaskInstState')

        if m.get('ScheduleState') is not None:
            self.schedule_state = m.get('ScheduleState')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SyncTime') is not None:
            self.sync_time = m.get('SyncTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

