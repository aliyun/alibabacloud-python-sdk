# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class UpdateJobRequest(DaraModel):
    def __init__(
        self,
        app_group_id: int = None,
        app_name: str = None,
        attempt_interval: int = None,
        calendar: str = None,
        child_job_id: str = None,
        cluster_id: str = None,
        dependent_strategy: int = None,
        description: str = None,
        executor_block_strategy: int = None,
        job_handler: str = None,
        job_id: int = None,
        max_attempt: int = None,
        max_concurrency: int = None,
        name: str = None,
        notice_config: main_models.UpdateJobRequestNoticeConfig = None,
        notice_contacts: List[main_models.UpdateJobRequestNoticeContacts] = None,
        parameters: str = None,
        priority: int = None,
        route_strategy: int = None,
        script: str = None,
        start_time: int = None,
        start_time_type: str = None,
        time_expression: str = None,
        time_type: int = None,
        timezone: str = None,
        weight: int = None,
        xattrs: str = None,
    ):
        self.app_group_id = app_group_id
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The retry interval upon node failure.
        self.attempt_interval = attempt_interval
        # The custom calendar.
        self.calendar = calendar
        # The child node IDs, separated by commas.
        self.child_job_id = child_job_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The dependency strategy.
        self.dependent_strategy = dependent_strategy
        # The node description.
        self.description = description
        # The client blocking strategy. Valid values:
        # - 1: serial execution on a single machine
        # - 2: ignore subsequent scheduling
        # - 3: override previous scheduling
        self.executor_block_strategy = executor_block_strategy
        # The JobHandler name.
        self.job_handler = job_handler
        # The node ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The maximum number of retry attempts upon node failure.
        self.max_attempt = max_attempt
        # The maximum number of concurrent instances for the node.
        # >The maximum number of instances that can run simultaneously for the same node. A value of 1 indicates that repeated execution is not allowed. If the concurrency limit is exceeded, the current scheduling is skipped.
        self.max_concurrency = max_concurrency
        # The node name.
        self.name = name
        # The notification configuration.
        self.notice_config = notice_config
        # The notification contact configuration.
        self.notice_contacts = notice_contacts
        # The node parameters.
        self.parameters = parameters
        # The node execution priority. Valid values:
        # 
        # - 1: low
        # - 5: medium
        # - 10: high
        # - 15: very high
        self.priority = priority
        # The routing strategy. Valid values:
        # 
        # - 1: round robin
        # - 2: random
        # - 3: first
        # - 4: last
        # - 5: least frequently used
        # - 6: least recently used
        # - 7: consistent hashing
        # - 8: shard broadcast
        self.route_strategy = route_strategy
        # The script content for non-BEAN nodes. Use this field to configure the script.
        self.script = script
        # The scheduling start time.
        self.start_time = start_time
        # The start time type.
        self.start_time_type = start_time_type
        # The time expression. Set the time expression based on the selected time type.
        # 
        # - none: No value is required.
        # - cron: Specify a standard cron expression. Online verification is supported.
        # - api: No value is required.
        # - fixed_rate: Specify a fixed frequency value in seconds. For example, 30 indicates that the node is triggered every 30 seconds.
        # - one_time: Specify a scheduling time in the format of yyyy-MM-dd HH:mm:ss or a timestamp in milliseconds. For example, "2022-10-10 10:10:00".
        self.time_expression = time_expression
        # The time type. Valid values:
        # 
        # - -1: none
        # - 1: cron
        # - 3: fix_rate
        # - 5: one_time
        # - 100: api
        self.time_type = time_type
        # The time zone.
        # > The default value is the time zone of the SchedulerX server.
        self.timezone = timezone
        # The node weight.
        self.weight = weight
        self.xattrs = xattrs

    def validate(self):
        if self.notice_config:
            self.notice_config.validate()
        if self.notice_contacts:
            for v1 in self.notice_contacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.attempt_interval is not None:
            result['AttemptInterval'] = self.attempt_interval

        if self.calendar is not None:
            result['Calendar'] = self.calendar

        if self.child_job_id is not None:
            result['ChildJobId'] = self.child_job_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

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

        if self.max_attempt is not None:
            result['MaxAttempt'] = self.max_attempt

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.name is not None:
            result['Name'] = self.name

        if self.notice_config is not None:
            result['NoticeConfig'] = self.notice_config.to_map()

        result['NoticeContacts'] = []
        if self.notice_contacts is not None:
            for k1 in self.notice_contacts:
                result['NoticeContacts'].append(k1.to_map() if k1 else None)

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.route_strategy is not None:
            result['RouteStrategy'] = self.route_strategy

        if self.script is not None:
            result['Script'] = self.script

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_time_type is not None:
            result['StartTimeType'] = self.start_time_type

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.weight is not None:
            result['Weight'] = self.weight

        if self.xattrs is not None:
            result['XAttrs'] = self.xattrs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AttemptInterval') is not None:
            self.attempt_interval = m.get('AttemptInterval')

        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')

        if m.get('ChildJobId') is not None:
            self.child_job_id = m.get('ChildJobId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

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

        if m.get('MaxAttempt') is not None:
            self.max_attempt = m.get('MaxAttempt')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NoticeConfig') is not None:
            temp_model = main_models.UpdateJobRequestNoticeConfig()
            self.notice_config = temp_model.from_map(m.get('NoticeConfig'))

        self.notice_contacts = []
        if m.get('NoticeContacts') is not None:
            for k1 in m.get('NoticeContacts'):
                temp_model = main_models.UpdateJobRequestNoticeContacts()
                self.notice_contacts.append(temp_model.from_map(k1))

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RouteStrategy') is not None:
            self.route_strategy = m.get('RouteStrategy')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartTimeType') is not None:
            self.start_time_type = m.get('StartTimeType')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('XAttrs') is not None:
            self.xattrs = m.get('XAttrs')

        return self

class UpdateJobRequestNoticeContacts(DaraModel):
    def __init__(
        self,
        contact_type: int = None,
        name: str = None,
    ):
        # The contact type. 
        # > Default configurations: 1.
        self.contact_type = contact_type
        # The contact name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_type is not None:
            result['ContactType'] = self.contact_type

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateJobRequestNoticeConfig(DaraModel):
    def __init__(
        self,
        end_early: int = None,
        end_early_enable: bool = None,
        fail_enable: bool = None,
        fail_limit_times: int = None,
        miss_worker_enable: bool = None,
        send_channel: str = None,
        success_notice: bool = None,
        timeout: int = None,
        timeout_enable: bool = None,
        timeout_kill_enable: bool = None,
    ):
        # The early termination threshold, in seconds.
        self.end_early = end_early
        # Specifies whether to enable the early termination alert.
        self.end_early_enable = end_early_enable
        # Specifies whether to enable the failure alert. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.fail_enable = fail_enable
        # The number of consecutive failures.
        # > An alert is sent only when the number of consecutive failures exceeds the configured value.
        self.fail_limit_times = fail_limit_times
        # Specifies whether to enable the no-available-machine alert. Valid values:
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.miss_worker_enable = miss_worker_enable
        # The notification channel. Valid values:
        # - sms: text message
        # - phone: phone call
        # - mail: email
        # - webhook: webhook
        # > Separate multiple notification channels with commas.
        self.send_channel = send_channel
        # Specifies whether to enable the success notification. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.success_notice = success_notice
        # The node execution timeout period, in seconds.
        self.timeout = timeout
        # Specifies whether to enable the timeout alert. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        self.timeout_enable = timeout_enable
        # Specifies whether to enable the timeout termination for the current trigger. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.timeout_kill_enable = timeout_kill_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_early is not None:
            result['EndEarly'] = self.end_early

        if self.end_early_enable is not None:
            result['EndEarlyEnable'] = self.end_early_enable

        if self.fail_enable is not None:
            result['FailEnable'] = self.fail_enable

        if self.fail_limit_times is not None:
            result['FailLimitTimes'] = self.fail_limit_times

        if self.miss_worker_enable is not None:
            result['MissWorkerEnable'] = self.miss_worker_enable

        if self.send_channel is not None:
            result['SendChannel'] = self.send_channel

        if self.success_notice is not None:
            result['SuccessNotice'] = self.success_notice

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.timeout_enable is not None:
            result['TimeoutEnable'] = self.timeout_enable

        if self.timeout_kill_enable is not None:
            result['TimeoutKillEnable'] = self.timeout_kill_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndEarly') is not None:
            self.end_early = m.get('EndEarly')

        if m.get('EndEarlyEnable') is not None:
            self.end_early_enable = m.get('EndEarlyEnable')

        if m.get('FailEnable') is not None:
            self.fail_enable = m.get('FailEnable')

        if m.get('FailLimitTimes') is not None:
            self.fail_limit_times = m.get('FailLimitTimes')

        if m.get('MissWorkerEnable') is not None:
            self.miss_worker_enable = m.get('MissWorkerEnable')

        if m.get('SendChannel') is not None:
            self.send_channel = m.get('SendChannel')

        if m.get('SuccessNotice') is not None:
            self.success_notice = m.get('SuccessNotice')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('TimeoutEnable') is not None:
            self.timeout_enable = m.get('TimeoutEnable')

        if m.get('TimeoutKillEnable') is not None:
            self.timeout_kill_enable = m.get('TimeoutKillEnable')

        return self

