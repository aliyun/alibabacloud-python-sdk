# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateScheduleResponseBody(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        cron_expression: str = None,
        description: str = None,
        enable: bool = None,
        last_modified_time: str = None,
        payload: str = None,
        request_id: str = None,
        schedule_id: str = None,
        schedule_name: str = None,
    ):
        # The time when the time-based schedule was created.
        self.created_time = created_time
        # The CRON expression.
        self.cron_expression = cron_expression
        # The description of the time-based schedule.
        self.description = description
        # Indicates whether the time-based schedule is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable = enable
        # The time when the time-based schedule was last updated.
        self.last_modified_time = last_modified_time
        # The trigger message of the time-based schedule.
        self.payload = payload
        # The request ID.
        self.request_id = request_id
        # The ID of the time-based schedule.
        self.schedule_id = schedule_id
        # The name of the time-based schedule.
        self.schedule_name = schedule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.description is not None:
            result['Description'] = self.description

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id

        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')

        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')

        return self

