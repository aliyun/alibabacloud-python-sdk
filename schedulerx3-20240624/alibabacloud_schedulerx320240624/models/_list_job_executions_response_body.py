# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class ListJobExecutionsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListJobExecutionsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The query result.
        self.data = data
        # The error message returned if the request fails.
        # 
        # This parameter is required.
        self.message = message
        # The unique identifier for the request. Alibaba Cloud generates this ID to help troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
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
            temp_model = main_models.ListJobExecutionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListJobExecutionsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        records: List[main_models.ListJobExecutionsResponseBodyDataRecords] = None,
        total: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # A list of job instances.
        self.records = records
        # The total number of entries found.
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
                temp_model = main_models.ListJobExecutionsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListJobExecutionsResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        attempt: int = None,
        data_time: str = None,
        duration: int = None,
        end_time: str = None,
        executor: str = None,
        job_execution_id: str = None,
        job_id: int = None,
        job_name: str = None,
        job_type: str = None,
        parameters: str = None,
        result: str = None,
        route_strategy: int = None,
        schedule_time: str = None,
        server_ip: str = None,
        status: int = None,
        time_type: int = None,
        total_tokens: int = None,
        trigger_type: int = None,
        work_addr: str = None,
        workflow_execution_id: str = None,
        workflow_id: int = None,
        workflow_name: str = None,
        xattrs: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The attempt number for this execution. `1` indicates the initial run.
        self.attempt = attempt
        # The data timestamp for the job execution.
        self.data_time = data_time
        # The duration of the job execution.
        self.duration = duration
        # The time when the job execution ended.
        self.end_time = end_time
        # The ID of the executor.
        self.executor = executor
        # The job execution ID.
        self.job_execution_id = job_execution_id
        # The job ID.
        self.job_id = job_id
        # The name of the job.
        self.job_name = job_name
        # The type of the job.
        self.job_type = job_type
        # The parameters of the job.
        self.parameters = parameters
        # The execution result.
        self.result = result
        # The strategy for routing the job to a worker. Valid values:
        # 
        # - 1: Round-robin
        # 
        # - 2: Random
        # 
        # - 3: First
        # 
        # - 4: Last
        # 
        # - 5: Least Frequently Used
        # 
        # - 6: Least Recently Used
        # 
        # - 7: Consistent Hashing
        # 
        # - 8: Sharded Broadcasting
        self.route_strategy = route_strategy
        # The time when the job was scheduled.
        self.schedule_time = schedule_time
        # The IP address of the scheduler node.
        self.server_ip = server_ip
        # The job execution status. Valid values:
        # 
        # - 0: UNKNOWN
        # 
        # - 1: WAITING
        # 
        # - 2: READY
        # 
        # - 3: RUNNING
        # 
        # - 4: SUCCESS
        # 
        # - 5: FAILED
        # 
        # - 6: PAUSED
        # 
        # - 7: SUBMITTED
        # 
        # - 8: REJECTED
        # 
        # - 9: ACCEPTED
        # 
        # - 10: PARTIAL_FAILED
        # 
        # - 11: SKIPPED
        # 
        # - 12: REMOVED
        self.status = status
        # The scheduling type. Valid values:
        # 
        # - -1: none<br>
        # 
        # - 1: cron<br>
        # 
        # - 3: fix_rate<br>
        # 
        # - 5: one_time<br>
        # 
        # - 100: api
        self.time_type = time_type
        # The total number of tokens consumed by the job execution.
        self.total_tokens = total_tokens
        # The method that triggered the job. Valid values:
        # 
        # - 0: unknown
        # 
        # - 1: schedule
        # 
        # - 2: rerun
        # 
        # - 3: api
        # 
        # - 4: user_retry
        # 
        # - 5: system_retry
        # 
        # - 6: manual
        self.trigger_type = trigger_type
        # The address of the worker that executed the job instance.
        self.work_addr = work_addr
        # The ID of the parent workflow instance, if applicable.
        self.workflow_execution_id = workflow_execution_id
        # The ID of the parent workflow, if applicable.
        self.workflow_id = workflow_id
        # The name of the parent workflow, if applicable.
        self.workflow_name = workflow_name
        # The extended attributes.
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

        if self.attempt is not None:
            result['Attempt'] = self.attempt

        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.executor is not None:
            result['Executor'] = self.executor

        if self.job_execution_id is not None:
            result['JobExecutionId'] = self.job_execution_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.result is not None:
            result['Result'] = self.result

        if self.route_strategy is not None:
            result['RouteStrategy'] = self.route_strategy

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.work_addr is not None:
            result['WorkAddr'] = self.work_addr

        if self.workflow_execution_id is not None:
            result['WorkflowExecutionId'] = self.workflow_execution_id

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        if self.xattrs is not None:
            result['XAttrs'] = self.xattrs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Attempt') is not None:
            self.attempt = m.get('Attempt')

        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Executor') is not None:
            self.executor = m.get('Executor')

        if m.get('JobExecutionId') is not None:
            self.job_execution_id = m.get('JobExecutionId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('RouteStrategy') is not None:
            self.route_strategy = m.get('RouteStrategy')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('WorkAddr') is not None:
            self.work_addr = m.get('WorkAddr')

        if m.get('WorkflowExecutionId') is not None:
            self.workflow_execution_id = m.get('WorkflowExecutionId')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        if m.get('XAttrs') is not None:
            self.xattrs = m.get('XAttrs')

        return self

