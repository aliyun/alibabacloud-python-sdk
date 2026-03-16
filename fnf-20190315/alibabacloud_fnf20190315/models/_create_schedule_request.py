# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScheduleRequest(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        description: str = None,
        enable: bool = None,
        flow_name: str = None,
        payload: str = None,
        schedule_name: str = None,
        signature_version: str = None,
    ):
        # The CRON expression.
        # 
        # This parameter is required.
        self.cron_expression = cron_expression
        # The description of the time-based schedule.
        self.description = description
        # Specifies whether to enable the time-based schedule. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable = enable
        # The name of the workflow that is associated with the time-based schedule.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The trigger message of the time-based schedule. Specify the value in the JSON format.
        self.payload = payload
        # The name of the time-based schedule. The name must meet the following conventions:
        # 
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must start with a letter or an underscore (_).
        # *   It is case-sensitive.
        # *   The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.schedule_name = schedule_name
        self.signature_version = signature_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.description is not None:
            result['Description'] = self.description

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name

        if self.signature_version is not None:
            result['SignatureVersion'] = self.signature_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')

        if m.get('SignatureVersion') is not None:
            self.signature_version = m.get('SignatureVersion')

        return self

