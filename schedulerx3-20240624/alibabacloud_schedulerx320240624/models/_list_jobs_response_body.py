# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class ListJobsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListJobsResponseBodyData = None,
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
            temp_model = main_models.ListJobsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListJobsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[main_models.ListJobsResponseBodyDataRecords] = None,
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
                temp_model = main_models.ListJobsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListJobsResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        attempt_interval: int = None,
        calendar: str = None,
        child_job_id: str = None,
        clean_mode: str = None,
        creator: str = None,
        current_execute_status: int = None,
        data_offset: int = None,
        dependent_strategy: int = None,
        description: str = None,
        executor_block_strategy: str = None,
        job_handler: str = None,
        job_id: int = None,
        job_type: str = None,
        last_execute_end_time: str = None,
        last_execute_status: int = None,
        max_attempt: int = None,
        max_concurrency: int = None,
        name: str = None,
        node_type: int = None,
        notice_config: str = None,
        notice_contacts: str = None,
        parameters: str = None,
        priority: int = None,
        route_strategy: int = None,
        script: str = None,
        start_time_type: int = None,
        status: int = None,
        time_expression: str = None,
        time_type: int = None,
        time_zone: str = None,
        timezone: str = None,
        updater: str = None,
        weight: int = None,
        workflow_id: int = None,
        xattrs: str = None,
    ):
        self.app_name = app_name
        self.attempt_interval = attempt_interval
        self.calendar = calendar
        self.child_job_id = child_job_id
        self.clean_mode = clean_mode
        self.creator = creator
        self.current_execute_status = current_execute_status
        self.data_offset = data_offset
        self.dependent_strategy = dependent_strategy
        self.description = description
        self.executor_block_strategy = executor_block_strategy
        self.job_handler = job_handler
        self.job_id = job_id
        self.job_type = job_type
        self.last_execute_end_time = last_execute_end_time
        self.last_execute_status = last_execute_status
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        self.name = name
        self.node_type = node_type
        self.notice_config = notice_config
        self.notice_contacts = notice_contacts
        self.parameters = parameters
        self.priority = priority
        self.route_strategy = route_strategy
        self.script = script
        self.start_time_type = start_time_type
        self.status = status
        self.time_expression = time_expression
        self.time_type = time_type
        self.time_zone = time_zone
        self.timezone = timezone
        self.updater = updater
        self.weight = weight
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

        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval

        if self.calendar is not None:
            result['Calendar'] = self.calendar

        if self.child_job_id is not None:
            result['ChildJobId'] = self.child_job_id

        if self.clean_mode is not None:
            result['CleanMode'] = self.clean_mode

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.current_execute_status is not None:
            result['CurrentExecuteStatus'] = self.current_execute_status

        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset

        if self.dependent_strategy is not None:
            result['DependentStrategy'] = self.dependent_strategy

        if self.description is not None:
            result['Description'] = self.description

        if self.executor_block_strategy is not None:
            result['ExecutorBlockStrategy'] = self.executor_block_strategy

        if self.job_handler is not None:
            result['JobHandler'] = self.job_handler

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.last_execute_end_time is not None:
            result['LastExecuteEndTime'] = self.last_execute_end_time

        if self.last_execute_status is not None:
            result['LastExecuteStatus'] = self.last_execute_status

        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.name is not None:
            result['Name'] = self.name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.notice_config is not None:
            result['NoticeConfig'] = self.notice_config

        if self.notice_contacts is not None:
            result['NoticeContacts'] = self.notice_contacts

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.route_strategy is not None:
            result['RouteStrategy'] = self.route_strategy

        if self.script is not None:
            result['Script'] = self.script

        if self.start_time_type is not None:
            result['StartTimeType'] = self.start_time_type

        if self.status is not None:
            result['Status'] = self.status

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.updater is not None:
            result['Updater'] = self.updater

        if self.weight is not None:
            result['Weight'] = self.weight

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.xattrs is not None:
            result['Xattrs'] = self.xattrs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')

        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')

        if m.get('ChildJobId') is not None:
            self.child_job_id = m.get('ChildJobId')

        if m.get('CleanMode') is not None:
            self.clean_mode = m.get('CleanMode')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CurrentExecuteStatus') is not None:
            self.current_execute_status = m.get('CurrentExecuteStatus')

        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')

        if m.get('DependentStrategy') is not None:
            self.dependent_strategy = m.get('DependentStrategy')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutorBlockStrategy') is not None:
            self.executor_block_strategy = m.get('ExecutorBlockStrategy')

        if m.get('JobHandler') is not None:
            self.job_handler = m.get('JobHandler')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('LastExecuteEndTime') is not None:
            self.last_execute_end_time = m.get('LastExecuteEndTime')

        if m.get('LastExecuteStatus') is not None:
            self.last_execute_status = m.get('LastExecuteStatus')

        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('NoticeConfig') is not None:
            self.notice_config = m.get('NoticeConfig')

        if m.get('NoticeContacts') is not None:
            self.notice_contacts = m.get('NoticeContacts')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RouteStrategy') is not None:
            self.route_strategy = m.get('RouteStrategy')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        if m.get('StartTimeType') is not None:
            self.start_time_type = m.get('StartTimeType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('Updater') is not None:
            self.updater = m.get('Updater')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('Xattrs') is not None:
            self.xattrs = m.get('Xattrs')

        return self

