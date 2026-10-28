# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SchedulingRule(DaraModel):
    def __init__(
        self,
        cron_tab: str = None,
        end_at: str = None,
        execute_once: bool = None,
        start_at: str = None,
    ):
        # The cron tab. Only the minute, hour, day, month, and week fields are currently supported. Second-level configurations are discarded.
        self.cron_tab = cron_tab
        # The stop time of the task.
        self.end_at = end_at
        # Specifies whether the task is executed only once.
        self.execute_once = execute_once
        # The start time of the effective period for the node.
        self.start_at = start_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_tab is not None:
            result['CronTab'] = self.cron_tab

        if self.end_at is not None:
            result['EndAt'] = self.end_at

        if self.execute_once is not None:
            result['ExecuteOnce'] = self.execute_once

        if self.start_at is not None:
            result['StartAt'] = self.start_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronTab') is not None:
            self.cron_tab = m.get('CronTab')

        if m.get('EndAt') is not None:
            self.end_at = m.get('EndAt')

        if m.get('ExecuteOnce') is not None:
            self.execute_once = m.get('ExecuteOnce')

        if m.get('StartAt') is not None:
            self.start_at = m.get('StartAt')

        return self

