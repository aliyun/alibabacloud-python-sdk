# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
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
        # The request status code.
        self.code = code
        # The node list information.
        self.data = data
        # The error message. This parameter is returned only if an error occurs.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # - **true**: The call was successful.
        # 
        # - **false**: The call failed.
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
        jobs: List[main_models.ListJobsResponseBodyDataJobs] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The node list and node details.
        self.jobs = jobs
        # The page number.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # The total number of records.
        self.total = total

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['Jobs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k1 in m.get('Jobs'):
                temp_model = main_models.ListJobsResponseBodyDataJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListJobsResponseBodyDataJobs(DaraModel):
    def __init__(
        self,
        attempt_interval: int = None,
        class_name: str = None,
        content: str = None,
        description: str = None,
        execute_mode: str = None,
        jar_url: str = None,
        job_id: int = None,
        job_monitor_info: main_models.ListJobsResponseBodyDataJobsJobMonitorInfo = None,
        job_type: str = None,
        map_task_xattrs: main_models.ListJobsResponseBodyDataJobsMapTaskXAttrs = None,
        max_attempt: int = None,
        max_concurrency: str = None,
        name: str = None,
        parameters: str = None,
        start_time: int = None,
        status: int = None,
        time_config: main_models.ListJobsResponseBodyDataJobsTimeConfig = None,
        xattrs: str = None,
    ):
        # The retry interval on error, in seconds. Default value: 30.
        self.attempt_interval = attempt_interval
        # The full path of the node interface class. This field is returned only when the node is of the Java type.
        self.class_name = class_name
        # The script code content for Python, Shell, or Go node types.
        self.content = content
        # The node description.
        self.description = description
        # The node execution mode. Valid values:
        # 
        # - **standalone**: standalone
        # 
        # - **broadcast**: broadcast
        # 
        # - **parallel**: parallel computing
        # 
        # - **grid**: memory grid
        # 
        # - **batch**: grid computing
        # 
        # - **shard**: shard
        self.execute_mode = execute_mode
        # The full path of the JAR package in OSS.
        self.jar_url = jar_url
        # The node ID.
        self.job_id = job_id
        # The node monitoring information.
        self.job_monitor_info = job_monitor_info
        # The node type.
        self.job_type = job_type
        # The advanced configuration. This is used only for parallel computing, memory grid, and grid computing.
        self.map_task_xattrs = map_task_xattrs
        # The maximum number of retries on error. Set this based on business requirements. Default value: 0.
        self.max_attempt = max_attempt
        # The maximum number of concurrently running instances. Default value: 1. This means that if the previous trigger has not finished running, the next trigger will not be initiated even if the scheduled time has arrived.
        self.max_concurrency = max_concurrency
        # The node name.
        self.name = name
        # The user-defined parameters that can be obtained at runtime.
        self.parameters = parameters
        self.start_time = start_time
        # The node status. Valid values:
        # 
        # - **1**: Enabled. The node can be triggered normally.
        # 
        # - **0**: Disabled. The node will not be triggered.
        self.status = status
        # The time configuration information.
        self.time_config = time_config
        # The node extension field.
        self.xattrs = xattrs

    def validate(self):
        if self.job_monitor_info:
            self.job_monitor_info.validate()
        if self.map_task_xattrs:
            self.map_task_xattrs.validate()
        if self.time_config:
            self.time_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval

        if self.class_name is not None:
            result['ClassName'] = self.class_name

        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode

        if self.jar_url is not None:
            result['JarUrl'] = self.jar_url

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_monitor_info is not None:
            result['JobMonitorInfo'] = self.job_monitor_info.to_map()

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.map_task_xattrs is not None:
            result['MapTaskXAttrs'] = self.map_task_xattrs.to_map()

        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.time_config is not None:
            result['TimeConfig'] = self.time_config.to_map()

        if self.xattrs is not None:
            result['XAttrs'] = self.xattrs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')

        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')

        if m.get('JarUrl') is not None:
            self.jar_url = m.get('JarUrl')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobMonitorInfo') is not None:
            temp_model = main_models.ListJobsResponseBodyDataJobsJobMonitorInfo()
            self.job_monitor_info = temp_model.from_map(m.get('JobMonitorInfo'))

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MapTaskXAttrs') is not None:
            temp_model = main_models.ListJobsResponseBodyDataJobsMapTaskXAttrs()
            self.map_task_xattrs = temp_model.from_map(m.get('MapTaskXAttrs'))

        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeConfig') is not None:
            temp_model = main_models.ListJobsResponseBodyDataJobsTimeConfig()
            self.time_config = temp_model.from_map(m.get('TimeConfig'))

        if m.get('XAttrs') is not None:
            self.xattrs = m.get('XAttrs')

        return self

class ListJobsResponseBodyDataJobsTimeConfig(DaraModel):
    def __init__(
        self,
        calendar: str = None,
        data_offset: int = None,
        time_expression: str = None,
        time_type: int = None,
    ):
        # The custom calendar that can be specified for the cron type.
        self.calendar = calendar
        # The time offset that can be specified for the cron type, in seconds.
        self.data_offset = data_offset
        # The time expression. Valid values:
        # 
        # - **api**: No time expression.
        # 
        # - **fix_rate**: A specific fixed frequency value. For example, 30 indicates that the node is triggered every 30 seconds.
        # 
        # - **cron**: A standard cron expression.
        # 
        # - **second_delay**: A fixed delay in seconds before each execution (1s to 60s).
        self.time_expression = time_expression
        # The time configuration type. Valid values:
        # 
        # - **1**: cron
        # 
        # - **3**: fix_rate
        # 
        # - **4**: second_delay
        # 
        # - **100**: api
        self.time_type = time_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar is not None:
            result['Calendar'] = self.calendar

        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')

        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        return self

class ListJobsResponseBodyDataJobsMapTaskXAttrs(DaraModel):
    def __init__(
        self,
        consumer_size: int = None,
        dispatcher_size: int = None,
        page_size: int = None,
        queue_size: int = None,
        task_attempt_interval: int = None,
        task_max_attempt: int = None,
    ):
        # The number of threads for a single trigger on a single machine. Default value: 5.
        self.consumer_size = consumer_size
        # The number of subtask dispatch threads. Default value: 5.
        self.dispatcher_size = dispatcher_size
        # The number of subtasks pulled per batch for a parallel node. Default value: 100.
        self.page_size = page_size
        # The upper limit of the subtask queue cache. Default value: 10000.
        self.queue_size = queue_size
        # The retry interval for a subtask on failure.
        self.task_attempt_interval = task_attempt_interval
        # The number of retries for a subtask on failure.
        self.task_max_attempt = task_max_attempt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_size is not None:
            result['ConsumerSize'] = self.consumer_size

        if self.dispatcher_size is not None:
            result['DispatcherSize'] = self.dispatcher_size

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.queue_size is not None:
            result['QueueSize'] = self.queue_size

        if self.task_attempt_interval is not None:
            result['TaskAttemptInterval'] = self.task_attempt_interval

        if self.task_max_attempt is not None:
            result['TaskMaxAttempt'] = self.task_max_attempt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerSize') is not None:
            self.consumer_size = m.get('ConsumerSize')

        if m.get('DispatcherSize') is not None:
            self.dispatcher_size = m.get('DispatcherSize')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueueSize') is not None:
            self.queue_size = m.get('QueueSize')

        if m.get('TaskAttemptInterval') is not None:
            self.task_attempt_interval = m.get('TaskAttemptInterval')

        if m.get('TaskMaxAttempt') is not None:
            self.task_max_attempt = m.get('TaskMaxAttempt')

        return self

class ListJobsResponseBodyDataJobsJobMonitorInfo(DaraModel):
    def __init__(
        self,
        contact_info: List[main_models.ListJobsResponseBodyDataJobsJobMonitorInfoContactInfo] = None,
        monitor_config: main_models.ListJobsResponseBodyDataJobsJobMonitorInfoMonitorConfig = None,
    ):
        # The contact information.
        self.contact_info = contact_info
        # The alert switch and threshold configuration.
        self.monitor_config = monitor_config

    def validate(self):
        if self.contact_info:
            for v1 in self.contact_info:
                 if v1:
                    v1.validate()
        if self.monitor_config:
            self.monitor_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContactInfo'] = []
        if self.contact_info is not None:
            for k1 in self.contact_info:
                result['ContactInfo'].append(k1.to_map() if k1 else None)

        if self.monitor_config is not None:
            result['MonitorConfig'] = self.monitor_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_info = []
        if m.get('ContactInfo') is not None:
            for k1 in m.get('ContactInfo'):
                temp_model = main_models.ListJobsResponseBodyDataJobsJobMonitorInfoContactInfo()
                self.contact_info.append(temp_model.from_map(k1))

        if m.get('MonitorConfig') is not None:
            temp_model = main_models.ListJobsResponseBodyDataJobsJobMonitorInfoMonitorConfig()
            self.monitor_config = temp_model.from_map(m.get('MonitorConfig'))

        return self

class ListJobsResponseBodyDataJobsJobMonitorInfoMonitorConfig(DaraModel):
    def __init__(
        self,
        fail_enable: bool = None,
        miss_worker_enable: bool = None,
        send_channel: str = None,
        timeout: int = None,
        timeout_enable: bool = None,
        timeout_kill_enable: bool = None,
    ):
        # Specifies whether to enable the failure alert switch. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.fail_enable = fail_enable
        # Specifies whether to enable the no-available-machine alert.
        self.miss_worker_enable = miss_worker_enable
        # The alert notification method. Currently, only sms is supported.
        self.send_channel = send_channel
        # The timeout threshold, in seconds. Default value: 7200.
        self.timeout = timeout
        # Specifies whether to enable the timeout alert switch. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.timeout_enable = timeout_enable
        # Specifies whether to enable the timeout termination switch for the current trigger. This is disabled by default. Valid values:
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.timeout_kill_enable = timeout_kill_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable

        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable

        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable

        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')

        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')

        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')

        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')

        return self

class ListJobsResponseBodyDataJobsJobMonitorInfoContactInfo(DaraModel):
    def __init__(
        self,
        ding: str = None,
        user_mail: str = None,
        user_name: str = None,
        user_phone: str = None,
    ):
        # The webhook URL of the DingTalk chatbot.
        self.ding = ding
        # The email address of the user.
        self.user_mail = user_mail
        # The username.
        self.user_name = user_name
        # The mobile phone number of the user.
        self.user_phone = user_phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ding is not None:
            result['Ding'] = self.ding

        if self.user_mail is not None:
            result['UserMail'] = self.user_mail

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_phone is not None:
            result['UserPhone'] = self.user_phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ding') is not None:
            self.ding = m.get('Ding')

        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserPhone') is not None:
            self.user_phone = m.get('UserPhone')

        return self

