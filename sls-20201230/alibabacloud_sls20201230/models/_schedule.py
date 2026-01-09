# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Schedule(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        delay: int = None,
        interval: str = None,
        run_immediately: bool = None,
        time_zone: str = None,
        type: str = None,
    ):
        self.cron_expression = cron_expression
        self.delay = delay
        self.interval = interval
        self.run_immediately = run_immediately
        self.time_zone = time_zone
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.delay is not None:
            result['delay'] = self.delay

        if self.interval is not None:
            result['interval'] = self.interval

        if self.run_immediately is not None:
            result['runImmediately'] = self.run_immediately

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('delay') is not None:
            self.delay = m.get('delay')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('runImmediately') is not None:
            self.run_immediately = m.get('runImmediately')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

