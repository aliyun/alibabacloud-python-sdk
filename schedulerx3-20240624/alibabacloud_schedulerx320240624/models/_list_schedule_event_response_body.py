# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class ListScheduleEventResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListScheduleEventResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListScheduleEventResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListScheduleEventResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[main_models.ListScheduleEventResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.records = records
        self.total = total

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListScheduleEventResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListScheduleEventResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        content: str = None,
        event: str = None,
        event_type: str = None,
        job_execution_id: str = None,
        job_name: str = None,
        time: str = None,
        worker_addr: str = None,
        workflow_execution_id: str = None,
        workflow_name: str = None,
    ):
        self.app_name = app_name
        self.content = content
        self.event = event
        self.event_type = event_type
        # 130
        self.job_execution_id = job_execution_id
        self.job_name = job_name
        self.time = time
        self.worker_addr = worker_addr
        self.workflow_execution_id = workflow_execution_id
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.content is not None:
            result['Content'] = self.content

        if self.event is not None:
            result['Event'] = self.event

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.time is not None:
            result['Time'] = self.time

        if self.worker_addr is not None:
            result['WorkerAddr'] = self.worker_addr

        if self.workflow_execution_id is not None:
            result['WorkflowExecutionId'] = self.workflow_execution_id

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('WorkerAddr') is not None:
            self.worker_addr = m.get('WorkerAddr')

        if m.get('WorkflowExecutionId') is not None:
            self.workflow_execution_id = m.get('WorkflowExecutionId')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        return self

