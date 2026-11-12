# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkflowRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        calendar: str = None,
        client_token: str = None,
        cluster_id: str = None,
        description: str = None,
        max_concurrency: int = None,
        name: str = None,
        time_expression: str = None,
        time_type: int = None,
        timezone: str = None,
        workflow_id: int = None,
    ):
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The custom calendar.
        self.calendar = calendar
        # The client token that is used to ensure the idempotence of the request. You can generate the value on the client side. Ensure that the value is unique across different requests and contains a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The workflow description.
        self.description = description
        # The maximum concurrency.
        # > The maximum number of instances that can run concurrently for the same workflow. A value of 1 indicates that concurrent execution is not allowed. If the concurrency limit is exceeded, the current scheduling task is skipped.
        self.max_concurrency = max_concurrency
        # The workflow name.
        self.name = name
        # The time expression. Configure the time expression based on the selected time type.
        # - none: Leave this parameter empty.
        # - cron: Enter a standard cron expression. Online verification is supported.
        # - api: Leave this parameter empty.
        self.time_expression = time_expression
        # The scheduling type. Valid values:
        # - -1: none
        # - 1: cron
        # - 100: api
        self.time_type = time_type
        # The time zone.
        # > By default, the time zone of the SchedulerX server is used.
        self.timezone = timezone
        # The workflow ID.
        # 
        # This parameter is required.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.calendar is not None:
            result['Calendar'] = self.calendar

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.name is not None:
            result['Name'] = self.name

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Calendar') is not None:
            self.calendar = m.get('Calendar')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

