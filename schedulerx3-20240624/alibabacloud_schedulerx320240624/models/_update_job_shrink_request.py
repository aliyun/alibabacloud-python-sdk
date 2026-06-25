# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateJobShrinkRequest(DaraModel):
    def __init__(
        self,
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
        notice_config_shrink: str = None,
        notice_contacts_shrink: str = None,
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
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The interval in seconds between retry attempts.
        self.attempt_interval = attempt_interval
        # The custom calendar.
        self.calendar = calendar
        # The client blocking strategy.
        # 
        # - 1: Serial execution
        # 
        # - 2: Ignore later schedules
        # 
        # - 3: Overwrite earlier schedules
        self.child_job_id = child_job_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        self.dependent_strategy = dependent_strategy
        # The job description.
        self.description = description
        # Notification contact configuration
        self.executor_block_strategy = executor_block_strategy
        # The job handler name.
        self.job_handler = job_handler
        # The job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The maximum number of retries for a failed job.
        self.max_attempt = max_attempt
        # The maximum number of concurrent job instances.
        # 
        # > This parameter defines the maximum number of instances for a single job that can run concurrently. A value of `1` prevents duplicate execution. If this limit is exceeded, the scheduler skips the current job.
        self.max_concurrency = max_concurrency
        # The job name.
        self.name = name
        # Time zone
        # 
        # > The default is the time zone of the SchedulerX server.
        self.notice_config_shrink = notice_config_shrink
        # Notification configuration
        self.notice_contacts_shrink = notice_contacts_shrink
        # The job parameters.
        self.parameters = parameters
        # The job execution priority. Valid values:
        # 
        # - `1`: Low
        # 
        # - `5`: Medium
        # 
        # - `10`: High
        # 
        # - `15`: Very High
        self.priority = priority
        # The routing strategy. Valid values:
        # 
        # - `1`: round-robin
        # 
        # - `2`: random
        # 
        # - `3`: first
        # 
        # - `4`: last
        # 
        # - `5`: least frequently used
        # 
        # - `6`: least recently used
        # 
        # - `7`: consistent hashing
        # 
        # - `8`: sharded broadcast
        self.route_strategy = route_strategy
        # The script content for non-BEAN jobs.
        self.script = script
        # The type of the start time.
        self.start_time = start_time
        # The task execution priority. The following values are supported:
        # 
        # - 1: Low
        # 
        # - 5: Medium
        # 
        # - 10: High
        # 
        # - 15: Very High
        self.start_time_type = start_time_type
        # The time expression. The expression format depends on the `TimeType`.
        # 
        # - `none`: Leave this parameter empty.
        # 
        # - `cron`: Specify a standard cron expression. Online validation is supported.
        # 
        # - `api`: Leave this parameter empty.
        # 
        # - `fixed_rate`: An integer that represents a fixed interval in seconds. For example, `30` triggers the job every 30 seconds.
        # 
        # - `one_time`: A single execution time, specified in the `yyyy-MM-dd HH:mm:ss` format or as a timestamp in milliseconds. For example, "2022-10-10 10:10:00".
        self.time_expression = time_expression
        # The time type. Valid values:
        # 
        # - `-1`: none
        # 
        # - `1`: cron
        # 
        # - `3`: fixed_rate
        # 
        # - `5`: one_time
        # 
        # - `100`: api
        self.time_type = time_type
        # The start time of the schedule.
        self.timezone = timezone
        # The ID of the child job. Separate multiple IDs with a comma.
        self.weight = weight
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

        if self.notice_config_shrink is not None:
            result['NoticeConfig'] = self.notice_config_shrink

        if self.notice_contacts_shrink is not None:
            result['NoticeContacts'] = self.notice_contacts_shrink

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
            self.notice_config_shrink = m.get('NoticeConfig')

        if m.get('NoticeContacts') is not None:
            self.notice_contacts_shrink = m.get('NoticeContacts')

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

