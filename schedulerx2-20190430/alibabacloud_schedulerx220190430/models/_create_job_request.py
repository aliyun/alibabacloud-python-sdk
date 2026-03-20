# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class CreateJobRequest(DaraModel):
    def __init__(
        self,
        attempt_interval: int = None,
        calendar: str = None,
        class_name: str = None,
        consumer_size: int = None,
        contact_info: List[main_models.CreateJobRequestContactInfo] = None,
        content: str = None,
        data_offset: int = None,
        description: str = None,
        dispatcher_size: int = None,
        execute_mode: str = None,
        fail_enable: bool = None,
        fail_times: int = None,
        group_id: str = None,
        job_type: str = None,
        max_attempt: int = None,
        max_concurrency: int = None,
        miss_worker_enable: bool = None,
        name: str = None,
        namespace: str = None,
        namespace_source: str = None,
        page_size: int = None,
        parameters: str = None,
        priority: int = None,
        queue_size: int = None,
        region_id: str = None,
        send_channel: str = None,
        status: int = None,
        success_notice_enable: bool = None,
        task_attempt_interval: int = None,
        task_max_attempt: int = None,
        time_expression: str = None,
        time_type: int = None,
        timeout: int = None,
        timeout_enable: bool = None,
        timeout_kill_enable: bool = None,
        timezone: str = None,
        xattrs: str = None,
    ):
        # The time interval between retry attempts in case of a job failure. Unit: seconds. Default value: 30.
        self.attempt_interval = attempt_interval
        # If you set TimeType to 1 (cron), you can specify calendar days.
        self.calendar = calendar
        # The full path of the job interface class.
        # 
        # This parameter is available only when you set JobType to java. You must enter a full path.
        self.class_name = class_name
        # The number of threads that a single worker triggers simultaneously. You can specify this parameter for MapReduce jobs. Default value: 5.
        self.consumer_size = consumer_size
        # The information about the alert contact.
        self.contact_info = contact_info
        # The script content. This parameter is required when you set JobType to python, shell, go, or k8s.
        self.content = content
        # If you set TimeType to 1 (cron), you can specify a time offset. Unit: seconds.
        self.data_offset = data_offset
        # The job description.
        self.description = description
        # The number of task distribution threads. This parameter is an advanced configuration item of the MapReduce job. Default value: 5.
        self.dispatcher_size = dispatcher_size
        # The execution mode of the job. Valid values:
        # 
        # *   **Stand-alone operation**
        # *   **Broadcast run**
        # *   **Visual MapReduce**
        # *   **MapReduce**
        # *   **Shard run**
        # 
        # This parameter is required.
        self.execute_mode = execute_mode
        # Specifies whether to trigger an alert when a job fails. Valid values:
        # 
        # *   **true**: triggers an alert when a job fails.
        # *   **false**: does not trigger an alert when a job fails.
        self.fail_enable = fail_enable
        # The maximum number of consecutive failures before an alert is triggered. An alert will be triggered if the number of consecutive failures reaches the value of this parameter.
        self.fail_times = fail_times
        # The application ID. You can obtain the application ID on the Application Management page in the SchedulerX console.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The job type. Valid values:
        # 
        # *   java
        # *   python
        # *   shell
        # *   go
        # *   http
        # *   xxljob
        # *   dataworks
        # *   k8s
        # *   springschedule
        # 
        # This parameter is required.
        self.job_type = job_type
        # The maximum number of retry attempts in case of a job failure. Specify this parameter based on your business requirements. Default value: 0.
        self.max_attempt = max_attempt
        # The maximum number of concurrent instances. By default, only one instance can run at a time. When an instance is running, the next instance is not triggered even if the scheduled start time arrives.
        self.max_concurrency = max_concurrency
        # Specifies whether to generate an alert if no machines are available to run the job. Valid values:
        # 
        # *   **true**: generates an alert if no machines are available to run the job.
        # *   **false**: does not generate an alert if no machines are available to run the job.
        self.miss_worker_enable = miss_worker_enable
        # The job name.
        # 
        # This parameter is required.
        self.name = name
        # The namespace ID. You can obtain the namespace ID on the Namespace page in the SchedulerX console.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The source of the namespace. You must specify this parameter only if the namespace is provided by a third party.
        self.namespace_source = namespace_source
        # The number of entries per page. You can specify this parameter for MapReduce jobs. Default value: 100.
        self.page_size = page_size
        # The user-defined parameters that you can obtain when the job is running.
        self.parameters = parameters
        self.priority = priority
        # The maximum capacity of the task queue. You can specify this parameter for MapReduce jobs. Default value: 10000.
        self.queue_size = queue_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The method that is used to send alerts. Set the value to sms. Default value: sms.
        self.send_channel = send_channel
        # Specifies whether to enable the job. If this parameter is set to 0, the job is disabled. If this parameter is set to 1, the job is enabled. Default value: 1.
        self.status = status
        # Specifies whether to send notifications for successfully running the job.
        self.success_notice_enable = success_notice_enable
        # The time interval between retry attempts in case of a job failure. This parameter is an advanced configuration item of the MapReduce job. Default value: 0.
        self.task_attempt_interval = task_attempt_interval
        # The maximum number of retry attempts in case of a job failure. This parameter is an advanced configuration item of the MapReduce job. Default value: 0.
        self.task_max_attempt = task_max_attempt
        # The time expression. Specify the time expression based on the value of TimeType:
        # 
        # *   If you set TimeType to **1** (cron), specify this parameter to a standard CRON expression.
        # *   If you set TimeType to **100** (api), no time expression is required.
        # *   If you set TimeType to **3** (fixed_rate), specify this parameter to a fixed frequency in seconds. For example, if you set this parameter to 30, the system triggers a job every 30 seconds.
        # *   If you set TimeType to **4** (second_delay), specify this parameter to a fixed delay after which the job is triggered. Valid values: 1 to 60. Unit: seconds.
        # *   If you set TimeType to **5** (one_time), specify this parameter to a specific time point at which the job is triggered. The time is in the format of yyyy-MM-dd HH:mm:ss, such as 2022-10-10 10:10:00, or a timestamp in milliseconds.
        self.time_expression = time_expression
        # The time type. Valid values:
        # 
        # *   **1**: cron
        # *   **3**: fixed_rate
        # *   **4**: second_delay
        # *   **5**: one_time
        # *   **100**: api
        # 
        # This parameter is required.
        self.time_type = time_type
        # The timeout threshold. Unit: seconds. Default value: 7200.
        self.timeout = timeout
        # Specifies whether to enable the timeout alert feature. If the feature is enabled, an alert will be triggered upon a timeout. Valid values:
        # 
        # *   **true**: enables the timeout alert feature.
        # *   **false**: disables the timeout alert feature.
        self.timeout_enable = timeout_enable
        # Specifies whether to enable the timeout termination feature. If the feature is enabled, a job will automatically be terminated if it times out. Valid values:
        # 
        # *   **true**: enables the timeout termination feature.
        # *   **false**: disables the timeout termination feature.
        self.timeout_kill_enable = timeout_kill_enable
        # Time zone.
        self.timezone = timezone
        # The extended attributes. If you set JobType to k8s, this parameter is required. For a job whose resource type is Job-YAML, set this parameter to {"resource":"job"}. For a job whose resource type is Shell-Script, set this parameter to {"image":"busybox","resource":"shell"}.
        self.xattrs = xattrs

    def validate(self):
        if self.contact_info:
            for v1 in self.contact_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval

        if self.calendar is not None:
            result['Calendar'] = self.calendar

        if self.class_name is not None:
            result['ClassName'] = self.class_name

        if self.consumer_size is not None:
            result['ConsumerSize'] = self.consumer_size

        result['ContactInfo'] = []
        if self.contact_info is not None:
            for k1 in self.contact_info:
                result['ContactInfo'].append(k1.to_map() if k1 else None)

        if self.content is not None:
            result['Content'] = self.content

        if self.data_offset is not None:
            result['DataOffset'] = self.data_offset

        if self.description is not None:
            result['Description'] = self.description

        if self.dispatcher_size is not None:
            result['DispatcherSize'] = self.dispatcher_size

        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode

        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable

        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_source is not None:
            result['NamespaceSource'] = self.namespace_source

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.queue_size is not None:
            result['QueueSize'] = self.queue_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel

        if self.status is not None:
            result['Status'] = self.status

        if self.success_notice_enable is not None:
            result['SuccessNoticeEnable'] = self.success_notice_enable

        if self.task_attempt_interval is not None:
            result['TaskAttemptInterval'] = self.task_attempt_interval

        if self.task_max_attempt is not None:
            result['TaskMaxAttempt'] = self.task_max_attempt

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable

        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.xattrs is not None:
            result['XAttrs'] = self.xattrs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')

        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')

        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')

        if m.get('ConsumerSize') is not None:
            self.consumer_size = m.get('ConsumerSize')

        self.contact_info = []
        if m.get('ContactInfo') is not None:
            for k1 in m.get('ContactInfo'):
                temp_model = main_models.CreateJobRequestContactInfo()
                self.contact_info.append(temp_model.from_map(k1))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataOffset') is not None:
            self.data_offset = m.get('DataOffset')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DispatcherSize') is not None:
            self.dispatcher_size = m.get('DispatcherSize')

        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')

        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')

        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceSource') is not None:
            self.namespace_source = m.get('NamespaceSource')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QueueSize') is not None:
            self.queue_size = m.get('QueueSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuccessNoticeEnable') is not None:
            self.success_notice_enable = m.get('SuccessNoticeEnable')

        if m.get('TaskAttemptInterval') is not None:
            self.task_attempt_interval = m.get('TaskAttemptInterval')

        if m.get('TaskMaxAttempt') is not None:
            self.task_max_attempt = m.get('TaskMaxAttempt')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')

        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('XAttrs') is not None:
            self.xattrs = m.get('XAttrs')

        return self

class CreateJobRequestContactInfo(DaraModel):
    def __init__(
        self,
        ding: str = None,
        user_mail: str = None,
        user_name: str = None,
        user_phone: str = None,
    ):
        # The webhook URL of the DingTalk chatbot.[](https://open.dingtalk.com/document/org/application-types)
        self.ding = ding
        # The email address of the alert contact.
        self.user_mail = user_mail
        # The name of the alert contact.
        self.user_name = user_name
        # The mobile number of the alert contact.
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

