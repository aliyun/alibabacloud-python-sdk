# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePublishCronRequest(DaraModel):
    def __init__(
        self,
        cron: str = None,
        cron_day: str = None,
        cron_time: int = None,
        cron_type: str = None,
        duration: int = None,
    ):
        # The cron expression that is used to specify the start time of the upgrade.
        # 
        # This parameter is required.
        self.cron = cron
        # The day of a week on which you want to perform the upgrade. Valid values:
        # 
        # *   **MON**
        # *   **TUE**
        # *   **WED**
        # *   **THU**
        # *   **FRI**
        # *   **SAT**
        # *   **SUN**
        self.cron_day = cron_day
        # The start timestamp. Unit: milliseconds.
        self.cron_time = cron_time
        # The type of the upgrade cycle. Valid values:
        # 
        # *   **day**: every day
        # *   **week**: every week
        self.cron_type = cron_type
        # The duration of the upgrade. Unit: hours.
        # 
        # This parameter is required.
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['Cron'] = self.cron

        if self.cron_day is not None:
            result['CronDay'] = self.cron_day

        if self.cron_time is not None:
            result['CronTime'] = self.cron_time

        if self.cron_type is not None:
            result['CronType'] = self.cron_type

        if self.duration is not None:
            result['Duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('CronDay') is not None:
            self.cron_day = m.get('CronDay')

        if m.get('CronTime') is not None:
            self.cron_time = m.get('CronTime')

        if m.get('CronType') is not None:
            self.cron_type = m.get('CronType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        return self

