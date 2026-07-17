# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyElasticPlanRequest(DaraModel):
    def __init__(
        self,
        custom_dates: List[str] = None,
        description: str = None,
        elastic_lcu: int = None,
        enabled: bool = None,
        end_hour: int = None,
        schedule_type: str = None,
        start_hour: int = None,
        dry_run: bool = None,
    ):
        self.custom_dates = custom_dates
        self.description = description
        self.elastic_lcu = elastic_lcu
        self.enabled = enabled
        self.end_hour = end_hour
        self.schedule_type = schedule_type
        self.start_hour = start_hour
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_dates is not None:
            result['customDates'] = self.custom_dates

        if self.description is not None:
            result['description'] = self.description

        if self.elastic_lcu is not None:
            result['elasticLcu'] = self.elastic_lcu

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.end_hour is not None:
            result['endHour'] = self.end_hour

        if self.schedule_type is not None:
            result['scheduleType'] = self.schedule_type

        if self.start_hour is not None:
            result['startHour'] = self.start_hour

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customDates') is not None:
            self.custom_dates = m.get('customDates')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('elasticLcu') is not None:
            self.elastic_lcu = m.get('elasticLcu')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('endHour') is not None:
            self.end_hour = m.get('endHour')

        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        if m.get('startHour') is not None:
            self.start_hour = m.get('startHour')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

