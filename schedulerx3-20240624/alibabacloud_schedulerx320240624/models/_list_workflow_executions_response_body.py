# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class ListWorkflowExecutionsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListWorkflowExecutionsResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # -
        self.data = data
        self.max_results = max_results
        # This parameter is required.
        self.message = message
        self.next_token = next_token
        # Id of the request
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
            temp_model = main_models.ListWorkflowExecutionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListWorkflowExecutionsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[main_models.ListWorkflowExecutionsResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # -
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
                temp_model = main_models.ListWorkflowExecutionsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListWorkflowExecutionsResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        data_time: str = None,
        end_time: str = None,
        executor: str = None,
        schedule_time: str = None,
        start_time: str = None,
        status: int = None,
        workflow_execution_id: str = None,
        workflow_id: str = None,
        workflow_name: str = None,
    ):
        self.app_name = app_name
        self.data_time = data_time
        self.end_time = end_time
        self.executor = executor
        self.schedule_time = schedule_time
        self.start_time = start_time
        self.status = status
        self.workflow_execution_id = workflow_execution_id
        self.workflow_id = workflow_id
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

        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.executor is not None:
            result['Executor'] = self.executor

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.workflow_execution_id is not None:
            result['WorkflowExecutionId'] = self.workflow_execution_id

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Executor') is not None:
            self.executor = m.get('Executor')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkflowExecutionId') is not None:
            self.workflow_execution_id = m.get('WorkflowExecutionId')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        return self

