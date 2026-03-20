# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class GetJobInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetJobInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The information about the job instance.
        self.data = data
        # The error message that is returned only if the corresponding error occurs.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.GetJobInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetJobInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        job_instance_detail: main_models.GetJobInstanceResponseBodyDataJobInstanceDetail = None,
    ):
        # The details of the job instance.
        self.job_instance_detail = job_instance_detail

    def validate(self):
        if self.job_instance_detail:
            self.job_instance_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_instance_detail is not None:
            result['JobInstanceDetail'] = self.job_instance_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobInstanceDetail') is not None:
            temp_model = main_models.GetJobInstanceResponseBodyDataJobInstanceDetail()
            self.job_instance_detail = temp_model.from_map(m.get('JobInstanceDetail'))

        return self

class GetJobInstanceResponseBodyDataJobInstanceDetail(DaraModel):
    def __init__(
        self,
        data_time: str = None,
        end_time: str = None,
        executor: str = None,
        instance_id: int = None,
        job_id: int = None,
        job_name: str = None,
        parameters: str = None,
        progress: str = None,
        result: str = None,
        schedule_time: str = None,
        start_time: str = None,
        status: int = None,
        time_type: int = None,
        trace_id: str = None,
        trigger_type: int = None,
        work_addr: str = None,
    ):
        # The data timestamp of the job instance.
        self.data_time = data_time
        # The end time of the job execution.
        self.end_time = end_time
        # The user who executes the job.
        self.executor = executor
        # The job instance ID.
        self.instance_id = instance_id
        # The job ID.
        self.job_id = job_id
        # The job name.
        self.job_name = job_name
        # The parameters of the job instance.
        self.parameters = parameters
        # The progress of the job instance.
        self.progress = progress
        # The execution results of the job instance.
        self.result = result
        # The time when the job was scheduled to run.
        self.schedule_time = schedule_time
        # The start time of the job execution.
        self.start_time = start_time
        # The state of the job instance. Valid values:
        # 
        # *   **1**: The job instance is waiting for execution.
        # *   **3**: The job instance is running.
        # *   **4**: The job instance is successful.
        # *   **5**: The job instance failed.
        # *   **9**: The job instance is rejected.
        # 
        # Enumeration class: com.alibaba.schedulerx.common.domain.InstanceStatus
        self.status = status
        # The method that is used to specify the time when to schedule the job instance. Valid values:
        # 
        # *   **1**: cron
        # *   **3**: fix_rate
        # *   **4**: second_delay
        # *   **100**: api
        # 
        # Enumeration class: com.alibaba.schedulerx.common.domain.TimeType
        self.time_type = time_type
        # The trace ID, which can be used to query trace details.
        self.trace_id = trace_id
        # The trigger type of the job instance. Valid values:
        # 
        # *   **1**: The job instance was triggered at the scheduled time.
        # *   **2**: The job instance was triggered due to data update.
        # *   **3**: The job instance was triggered by an API call.
        # *   **4**: The job instance was triggered because it is manually rerun.
        # *   **5**: The job instance was triggered because the system automatically reruns the job instance upon a system exception, such as a database exception.
        # 
        # Enumeration class: com.alibaba.schedulerx.common.domain.TriggerType
        self.trigger_type = trigger_type
        # The endpoint of the triggered client. The value is in the IP address:Port number format.
        self.work_addr = work_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.executor is not None:
            result['Executor'] = self.executor

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.result is not None:
            result['Result'] = self.result

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.work_addr is not None:
            result['WorkAddr'] = self.work_addr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Executor') is not None:
            self.executor = m.get('Executor')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('WorkAddr') is not None:
            self.work_addr = m.get('WorkAddr')

        return self

