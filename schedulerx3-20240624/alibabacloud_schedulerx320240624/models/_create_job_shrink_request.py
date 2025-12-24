# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJobShrinkRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        attempt_interval: int = None,
        calendar: str = None,
        child_job_id: str = None,
        cluster_id: str = None,
        coordinate_shrink: str = None,
        dependent_strategy: int = None,
        description: str = None,
        executor_block_strategy: int = None,
        job_handler: str = None,
        job_type: str = None,
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
        start_time_type: int = None,
        status: int = None,
        time_expression: str = None,
        time_type: int = None,
        timezone: str = None,
        weight: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        self.attempt_interval = attempt_interval
        self.calendar = calendar
        self.child_job_id = child_job_id
        # This parameter is required.
        self.cluster_id = cluster_id
        self.coordinate_shrink = coordinate_shrink
        self.dependent_strategy = dependent_strategy
        self.description = description
        self.executor_block_strategy = executor_block_strategy
        self.job_handler = job_handler
        # This parameter is required.
        self.job_type = job_type
        self.max_attempt = max_attempt
        self.max_concurrency = max_concurrency
        # This parameter is required.
        self.name = name
        self.notice_config_shrink = notice_config_shrink
        self.notice_contacts_shrink = notice_contacts_shrink
        self.parameters = parameters
        self.priority = priority
        self.route_strategy = route_strategy
        self.script = script
        self.start_time = start_time
        self.start_time_type = start_time_type
        self.status = status
        self.time_expression = time_expression
        # This parameter is required.
        self.time_type = time_type
        self.timezone = timezone
        self.weight = weight

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

        if self.coordinate_shrink is not None:
            result['Coordinate'] = self.coordinate_shrink

        if self.dependent_strategy is not None:
            result['DependentStrategy'] = self.dependent_strategy

        if self.description is not None:
            result['Description'] = self.description

        if self.executor_block_strategy is not None:
            result['ExecutorBlockStrategy'] = self.executor_block_strategy

        if self.job_handler is not None:
            result['JobHandler'] = self.job_handler

        if self.job_type is not None:
            result['JobType'] = self.job_type

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

        if self.status is not None:
            result['Status'] = self.status

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.weight is not None:
            result['Weight'] = self.weight

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

        if m.get('Coordinate') is not None:
            self.coordinate_shrink = m.get('Coordinate')

        if m.get('DependentStrategy') is not None:
            self.dependent_strategy = m.get('DependentStrategy')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutorBlockStrategy') is not None:
            self.executor_block_strategy = m.get('ExecutorBlockStrategy')

        if m.get('JobHandler') is not None:
            self.job_handler = m.get('JobHandler')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

