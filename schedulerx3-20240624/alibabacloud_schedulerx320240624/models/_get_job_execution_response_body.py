# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class GetJobExecutionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetJobExecutionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # -
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the API call succeeded.
        # 
        # - `true`: The request was successful.
        # 
        # - `false`: The request failed.
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
            temp_model = main_models.GetJobExecutionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetJobExecutionResponseBodyData(DaraModel):
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
        start_time: str = None,
        status: int = None,
        time_type: int = None,
        trigger_type: int = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The number of execution attempts.
        self.attempt = attempt
        # The data timestamp for the job instance.
        self.data_time = data_time
        # The duration of the job execution.
        self.duration = duration
        # The time when the job execution ended.
        self.end_time = end_time
        # Details of the executor that ran the job. The value is a JSON string.
        self.executor = executor
        # The ID of the job execution.
        self.job_execution_id = job_execution_id
        # The ID of the job.
        self.job_id = job_id
        # The name of the job.
        self.job_name = job_name
        # The type of the job.
        self.job_type = job_type
        # The parameters of the job.
        self.parameters = parameters
        # The result of the job execution. The value is a JSON string.
        self.result = result
        # The routing strategy. Valid values:
        # 
        # - `1`: `Round Robin`
        # 
        # - `2`: `Random`
        # 
        # - `3`: `First`
        # 
        # - `4`: `Last`
        # 
        # - `5`: `Least Frequently Used`
        # 
        # - `6`: `Least Recently Used`
        # 
        # - `7`: `Consistent Hashing`
        # 
        # - `8`: `Shard Broadcasting`
        self.route_strategy = route_strategy
        # The scheduled time for the job execution.
        self.schedule_time = schedule_time
        # The IP address of the scheduling server.
        self.server_ip = server_ip
        # The time when the job execution started.
        self.start_time = start_time
        # The job execution status. Valid values:
        # 
        # - `0`: `UNKNOWN`
        # 
        # - `1`: `WAITING`
        # 
        # - `2`: `READY`
        # 
        # - `3`: `RUNNING`
        # 
        # - `4`: `SUCCESS`
        # 
        # - `5`: `FAILED`
        self.status = status
        # The scheduling type of the job. Valid values:
        # 
        # - `-1`: `none`
        # 
        # - `1`: `cron`
        # 
        # - `2`: `fixed_delay`
        # 
        # - `3`: `fixed_rate`
        # 
        # - `5`: `one_time`
        # 
        # - `100`: `api`
        self.time_type = time_type
        # Indicates how the job was triggered. Valid values:
        # 
        # - `0`: `unknown`
        # 
        # - `1`: `timer_schedule`
        # 
        # - `2`: `rerun`
        # 
        # - `3`: `api_run`
        # 
        # - `4`: `user_retry`
        # 
        # - `5`: `system_retry`
        # 
        # - `6`: `manual`
        self.trigger_type = trigger_type

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

