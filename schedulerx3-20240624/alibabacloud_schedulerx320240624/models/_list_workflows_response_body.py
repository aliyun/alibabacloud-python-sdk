# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class ListWorkflowsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListWorkflowsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
            temp_model = main_models.ListWorkflowsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListWorkflowsResponseBodyData(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        records: List[main_models.ListWorkflowsResponseBodyDataRecords] = None,
        total: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListWorkflowsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListWorkflowsResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: int = None,
        calendar: str = None,
        creator: str = None,
        current_execute_status: int = None,
        description: str = None,
        last_execute_end_time: str = None,
        last_execute_status: int = None,
        max_concurrency: int = None,
        name: str = None,
        status: int = None,
        time_expression: str = None,
        time_type: int = None,
        timezone: str = None,
        updater: str = None,
        workflow_id: int = None,
        xattrs: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.calendar = calendar
        self.creator = creator
        self.current_execute_status = current_execute_status
        self.description = description
        self.last_execute_end_time = last_execute_end_time
        self.last_execute_status = last_execute_status
        self.max_concurrency = max_concurrency
        self.name = name
        self.status = status
        self.time_expression = time_expression
        self.time_type = time_type
        self.timezone = timezone
        self.updater = updater
        self.workflow_id = workflow_id
        self.xattrs = xattrs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.calendar is not None:
            result['Calendar'] = self.calendar

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.current_execute_status is not None:
            result['CurrentExecuteStatus'] = self.current_execute_status

        if self.description is not None:
            result['Description'] = self.description

        if self.last_execute_end_time is not None:
            result['LastExecuteEndTime'] = self.last_execute_end_time

        if self.last_execute_status is not None:
            result['LastExecuteStatus'] = self.last_execute_status

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.updater is not None:
            result['Updater'] = self.updater

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.xattrs is not None:
            result['Xattrs'] = self.xattrs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CurrentExecuteStatus') is not None:
            self.current_execute_status = m.get('CurrentExecuteStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LastExecuteEndTime') is not None:
            self.last_execute_end_time = m.get('LastExecuteEndTime')

        if m.get('LastExecuteStatus') is not None:
            self.last_execute_status = m.get('LastExecuteStatus')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('Updater') is not None:
            self.updater = m.get('Updater')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('Xattrs') is not None:
            self.xattrs = m.get('Xattrs')

        return self

