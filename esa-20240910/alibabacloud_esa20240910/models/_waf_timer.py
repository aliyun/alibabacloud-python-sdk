# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class WafTimer(DaraModel):
    def __init__(
        self,
        periods: List[main_models.WafTimerPeriods] = None,
        scopes: str = None,
        weekly_periods: List[main_models.WafTimerWeeklyPeriods] = None,
        zone: int = None,
    ):
        # The effective periods.
        self.periods = periods
        # The timer type: permanently effective (permanent/empty), effective during time periods (periods), or periodically effective (weekly).
        self.scopes = scopes
        # The weekly effective periods.
        self.weekly_periods = weekly_periods
        # The time zone. Default value: UTC+00:00.<br>Example: 8 indicates UTC+8, -8 indicates UTC-8.<br>Valid range: -12 to +14.
        self.zone = zone

    def validate(self):
        if self.periods:
            for v1 in self.periods:
                 if v1:
                    v1.validate()
        if self.weekly_periods:
            for v1 in self.weekly_periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Periods'] = []
        if self.periods is not None:
            for k1 in self.periods:
                result['Periods'].append(k1.to_map() if k1 else None)

        if self.scopes is not None:
            result['Scopes'] = self.scopes

        result['WeeklyPeriods'] = []
        if self.weekly_periods is not None:
            for k1 in self.weekly_periods:
                result['WeeklyPeriods'].append(k1.to_map() if k1 else None)

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.periods = []
        if m.get('Periods') is not None:
            for k1 in m.get('Periods'):
                temp_model = main_models.WafTimerPeriods()
                self.periods.append(temp_model.from_map(k1))

        if m.get('Scopes') is not None:
            self.scopes = m.get('Scopes')

        self.weekly_periods = []
        if m.get('WeeklyPeriods') is not None:
            for k1 in m.get('WeeklyPeriods'):
                temp_model = main_models.WafTimerWeeklyPeriods()
                self.weekly_periods.append(temp_model.from_map(k1))

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

class WafTimerWeeklyPeriods(DaraModel):
    def __init__(
        self,
        daily_periods: List[main_models.WafTimerWeeklyPeriodsDailyPeriods] = None,
        days: str = None,
    ):
        # The effective period within the epoch.
        self.daily_periods = daily_periods
        # The days of the week, separated by commas. Values 1-7 represent Monday through Sunday.<br>Example: Monday and Wednesday is "1,3".
        self.days = days

    def validate(self):
        if self.daily_periods:
            for v1 in self.daily_periods:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DailyPeriods'] = []
        if self.daily_periods is not None:
            for k1 in self.daily_periods:
                result['DailyPeriods'].append(k1.to_map() if k1 else None)

        if self.days is not None:
            result['Days'] = self.days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.daily_periods = []
        if m.get('DailyPeriods') is not None:
            for k1 in m.get('DailyPeriods'):
                temp_model = main_models.WafTimerWeeklyPeriodsDailyPeriods()
                self.daily_periods.append(temp_model.from_map(k1))

        if m.get('Days') is not None:
            self.days = m.get('Days')

        return self

class WafTimerWeeklyPeriodsDailyPeriods(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # The end time in HH:mm:ss format.
        self.end = end
        # The start time in HH:mm:ss format.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class WafTimerPeriods(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # The end time in RFC 3339 UTC format.
        self.end = end
        # The start time in RFC 3339 UTC format.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

