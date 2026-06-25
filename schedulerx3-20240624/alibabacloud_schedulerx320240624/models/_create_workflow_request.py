# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkflowRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        calendar: str = None,
        client_token: str = None,
        cluster_id: str = None,
        description: str = None,
        max_concurrency: int = None,
        name: str = None,
        status: int = None,
        time_expression: str = None,
        time_type: int = None,
        timezone: str = None,
    ):
        # The application name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The custom calendar. This parameter applies only when `TimeType` is `cron`.
        self.calendar = calendar
        # A unique client token to ensure request idempotence. The token must contain only ASCII characters. If you omit this parameter, the system uses the RequestId as the ClientToken. The RequestId is unique to each request.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The workflow description.
        self.description = description
        # The maximum concurrency for the workflow.
        self.max_concurrency = max_concurrency
        # The workflow name.
        # 
        # This parameter is required.
        self.name = name
        # The status of the workflow. By default, the workflow is disabled. Valid values:
        # 
        # - 0: Disabled
        # 
        # - 1: Enabled
        self.status = status
        # The time expression, which depends on the `TimeType` parameter.
        # 
        # - **none**: This parameter is not required.
        # 
        # - **cron**: Enter a standard cron expression. Online validation is supported.
        # 
        # - **api**: This parameter is not required.
        self.time_expression = time_expression
        # The schedule type. Valid values:
        # 
        # - -1: none<br>
        # 
        # - 1: cron<br>
        # 
        # - 100: api
        self.time_type = time_type
        # The time zone for the schedule.
        self.timezone = timezone

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

        if self.status is not None:
            result['Status'] = self.status

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.timezone is not None:
            result['Timezone'] = self.timezone

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self

