# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MaintenanceWindow(DaraModel):
    def __init__(
        self,
        duration: str = None,
        enable: bool = None,
        maintenance_time: str = None,
        recurrence: str = None,
        weekly_period: str = None,
    ):
        # The duration of the cluster maintenance window. 
        # 
        # Valid values: 1 to 24. 
        # 
        # Unit: hours.
        # 
        # Default value: 3.
        self.duration = duration
        # Specifies whether to enable the cluster maintenance window. Valid values:
        # 
        # *   `true`: enables the cluster maintenance window.
        # *   `false`: disables the cluster maintenance window.
        # 
        # Default value: `false`.
        self.enable = enable
        # The start time of the cluster maintenance window. The value follows a standard time format in Golang. Example: 15:04:05Z.
        self.maintenance_time = maintenance_time
        # Defines a maintenance window recurrence rule by using the RFC5545 recurrence rule. Currently, only FREQ=WEEKLY is supported, and you cannot specify COUNT or UNTIL.
        self.recurrence = recurrence
        # The day of the week when maintenance is performed. Separate multiple days with commas (,). 
        # 
        # Valid values: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday.
        # 
        # Default value: `Thursday`.
        self.weekly_period = weekly_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['duration'] = self.duration

        if self.enable is not None:
            result['enable'] = self.enable

        if self.maintenance_time is not None:
            result['maintenance_time'] = self.maintenance_time

        if self.recurrence is not None:
            result['recurrence'] = self.recurrence

        if self.weekly_period is not None:
            result['weekly_period'] = self.weekly_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('maintenance_time') is not None:
            self.maintenance_time = m.get('maintenance_time')

        if m.get('recurrence') is not None:
            self.recurrence = m.get('recurrence')

        if m.get('weekly_period') is not None:
            self.weekly_period = m.get('weekly_period')

        return self

