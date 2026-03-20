# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class GetJobInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetJobInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The details of the job.
        self.data = data
        # The error message returned only if an error occurs.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the job details were obtained. Valid values:
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
            temp_model = main_models.GetJobInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetJobInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        job_config_info: main_models.GetJobInfoResponseBodyDataJobConfigInfo = None,
    ):
        # The configurations of the job.
        self.job_config_info = job_config_info

    def validate(self):
        if self.job_config_info:
            self.job_config_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_config_info is not None:
            result['JobConfigInfo'] = self.job_config_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobConfigInfo') is not None:
            temp_model = main_models.GetJobInfoResponseBodyDataJobConfigInfo()
            self.job_config_info = temp_model.from_map(m.get('JobConfigInfo'))

        return self

class GetJobInfoResponseBodyDataJobConfigInfo(DaraModel):
    def __init__(
        self,
        attempt_interval: int = None,
        class_name: str = None,
        content: str = None,
        description: str = None,
        execute_mode: str = None,
        jar_url: str = None,
        job_id: int = None,
        job_monitor_info: main_models.GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfo = None,
        job_type: str = None,
        map_task_xattrs: main_models.GetJobInfoResponseBodyDataJobConfigInfoMapTaskXAttrs = None,
        max_attempt: int = None,
        max_concurrency: str = None,
        name: str = None,
        parameters: str = None,
        status: int = None,
        time_config: main_models.GetJobInfoResponseBodyDataJobConfigInfoTimeConfig = None,
        xattrs: str = None,
    ):
        # The interval at which the system retried to run the job after a job failure. Default value: 30. Unit: seconds.
        self.attempt_interval = attempt_interval
        # The full path of the job interface class. This parameter is returned only for jobs whose job type is Java.
        self.class_name = class_name
        # The script of a script job.
        self.content = content
        # The description of the job.
        self.description = description
        # The execution mode of the job. Valid values:
        # 
        # *   **Stand-alone operation**: standalone
        # *   **Broadcast run**: broadcast
        # *   **Visual MapReduce**: parallel
        # *   **MapReduce**: batch
        # *   **Shard run**: sharding
        self.execute_mode = execute_mode
        # The full path used to upload files to Object Storage Service (OSS).
        # 
        # If you use a JAR package, you can upload the JAR package to this OSS path.
        self.jar_url = jar_url
        # The job ID.
        self.job_id = job_id
        # The monitoring information of the job.
        self.job_monitor_info = job_monitor_info
        # The job type.
        self.job_type = job_type
        # The advanced configurations of the job.
        self.map_task_xattrs = map_task_xattrs
        # The maximum number of retries after a job failure. This parameter was specified based on your business requirements. Default value: 0.
        self.max_attempt = max_attempt
        # The maximum number of concurrent instances. Default value: 1. The default value indicates that if the last triggered instance is running, the next instance is not triggered even if the scheduled point in time for running the next instance is reached.
        self.max_concurrency = max_concurrency
        # The job name.
        self.name = name
        # The user-defined parameters that you can obtain when the job is running.
        self.parameters = parameters
        # Indicates whether the job was enabled. Valid values:
        # 
        # *   **1**: The job was enabled and could be triggered.
        # *   **0**: The job was disabled and could not be triggered.
        self.status = status
        # The time configurations.
        self.time_config = time_config
        # The extended fields.
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
            temp_model = main_models.GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfo()
            self.job_monitor_info = temp_model.from_map(m.get('JobMonitorInfo'))

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MapTaskXAttrs') is not None:
            temp_model = main_models.GetJobInfoResponseBodyDataJobConfigInfoMapTaskXAttrs()
            self.map_task_xattrs = temp_model.from_map(m.get('MapTaskXAttrs'))

        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeConfig') is not None:
            temp_model = main_models.GetJobInfoResponseBodyDataJobConfigInfoTimeConfig()
            self.time_config = temp_model.from_map(m.get('TimeConfig'))

        if m.get('XAttrs') is not None:
            self.xattrs = m.get('XAttrs')

        return self

class GetJobInfoResponseBodyDataJobConfigInfoTimeConfig(DaraModel):
    def __init__(
        self,
        calendar: str = None,
        data_offset: int = None,
        time_expression: str = None,
        time_type: int = None,
    ):
        # Custom calendar days specified if TimeType is set to **1** (cron).
        self.calendar = calendar
        # The time offset specified if TimeType is set to **1** (cron). Unit: seconds.
        self.data_offset = data_offset
        # The time expression specified based on the value of TimeType:
        # 
        # *   If TimeType is set to **100** (api), no time expression is required.
        # *   If TimeType is set to **3** (fix_rate), this parameter value indicates the specific and fixed frequency. For example, if the value is 30, the system triggers a job every 30 seconds.
        # *   If TimeType is set to **1** (cron), this parameter value indicates the standard CRON expression used to specify the time when to schedule the job.
        # *   If TimeType is set to **4** (second_delay), this parameter value indicates the fixed delay after which the job is triggered. Valid values: 1 to 60. Unit: seconds.
        self.time_expression = time_expression
        # The time type. Valid values:
        # 
        # *   **1**: cron
        # *   **3**: fix_rate
        # *   **4**: second_delay
        # *   **5**: one_time
        # *   **100**: api
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

class GetJobInfoResponseBodyDataJobConfigInfoMapTaskXAttrs(DaraModel):
    def __init__(
        self,
        consumer_size: int = None,
        dispatcher_size: int = None,
        page_size: int = None,
        queue_size: int = None,
        task_attempt_interval: int = None,
        task_max_attempt: int = None,
    ):
        # The number of threads that were triggered by a single worker at a time. Default value: 5.
        self.consumer_size = consumer_size
        # The number of task distribution threads. Default value: 5.
        self.dispatcher_size = dispatcher_size
        # The number of tasks that were pulled by a parallel job at a time. Default value: 100.
        self.page_size = page_size
        # The maximum number of tasks that can be queued. Default value: 10000.
        self.queue_size = queue_size
        # The interval at which the system retried to run the task after a task failure.
        self.task_attempt_interval = task_attempt_interval
        # The number of retries after a task failure.
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

class GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfo(DaraModel):
    def __init__(
        self,
        contact_info: List[main_models.GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoContactInfo] = None,
        monitor_config: main_models.GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoMonitorConfig = None,
    ):
        # The alert contact Information.
        self.contact_info = contact_info
        # The configurations of the alerting features and the alert thresholds.
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
                temp_model = main_models.GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoContactInfo()
                self.contact_info.append(temp_model.from_map(k1))

        if m.get('MonitorConfig') is not None:
            temp_model = main_models.GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoMonitorConfig()
            self.monitor_config = temp_model.from_map(m.get('MonitorConfig'))

        return self

class GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoMonitorConfig(DaraModel):
    def __init__(
        self,
        fail_enable: bool = None,
        miss_worker_enable: bool = None,
        send_channel: str = None,
        timeout: int = None,
        timeout_enable: bool = None,
        timeout_kill_enable: bool = None,
    ):
        # Indicates whether the Failure alarm switch was turned on. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fail_enable = fail_enable
        # Indicates whether the No machine alarm available switch was turned on.
        self.miss_worker_enable = miss_worker_enable
        # The method used to send alerts. Only Short Message Service (SMS) is supported.
        self.send_channel = send_channel
        # The timeout threshold. Default value: 7200. Unit: seconds.
        self.timeout = timeout
        # Indicates whether the Timeout alarm switch was turned on. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.timeout_enable = timeout_enable
        # Indicates whether the Timeout termination switch was turned on. The switch is turned off by default.
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

class GetJobInfoResponseBodyDataJobConfigInfoJobMonitorInfoContactInfo(DaraModel):
    def __init__(
        self,
        ding: str = None,
        user_mail: str = None,
        user_name: str = None,
        user_phone: str = None,
    ):
        # The webhook URL of the DingTalk chatbot.
        self.ding = ding
        # The email address of the alert contact.
        self.user_mail = user_mail
        # The name of the alert contact.
        self.user_name = user_name
        # The mobile phone number of the alert contact.
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

