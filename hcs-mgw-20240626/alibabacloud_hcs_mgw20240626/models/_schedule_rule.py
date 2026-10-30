# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScheduleRule(DaraModel):
    def __init__(
        self,
        max_schedule_count: int = None,
        start_cron_expression: str = None,
        suspend_cron_expression: str = None,
    ):
        # The maximum number of automatic scheduling rounds. Within this limit, a task execution ID is automatically scheduled based on the start and pause times. One round consists of a complete task execution from start to finish. If the limit is exceeded, automatic scheduling stops, but the task can still be executed manually.
        self.max_schedule_count = max_schedule_count
        # The start time specified by a cron expression. The interval must be at least 1 hour.
        self.start_cron_expression = start_cron_expression
        # The pause time specified by a cron expression. The interval must be at least 1 hour.
        self.suspend_cron_expression = suspend_cron_expression

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_schedule_count is not None:
            result['MaxScheduleCount'] = self.max_schedule_count

        if self.start_cron_expression is not None:
            result['StartCronExpression'] = self.start_cron_expression

        if self.suspend_cron_expression is not None:
            result['SuspendCronExpression'] = self.suspend_cron_expression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxScheduleCount') is not None:
            self.max_schedule_count = m.get('MaxScheduleCount')

        if m.get('StartCronExpression') is not None:
            self.start_cron_expression = m.get('StartCronExpression')

        if m.get('SuspendCronExpression') is not None:
            self.suspend_cron_expression = m.get('SuspendCronExpression')

        return self

