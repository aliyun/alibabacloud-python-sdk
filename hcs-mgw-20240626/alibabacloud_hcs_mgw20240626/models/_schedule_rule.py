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
        self.max_schedule_count = max_schedule_count
        self.start_cron_expression = start_cron_expression
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

