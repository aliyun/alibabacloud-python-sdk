# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ExecutePeriod(DaraModel):
    def __init__(
        self,
        effect_day: main_models.ExecutePeriodEffectDay = None,
        effect_time: main_models.ExecutePeriodEffectTime = None,
        schedule_effect: main_models.ExecutePeriodScheduleEffect = None,
        valid_type: str = None,
    ):
        self.effect_day = effect_day
        self.effect_time = effect_time
        self.schedule_effect = schedule_effect
        self.valid_type = valid_type

    def validate(self):
        if self.effect_day:
            self.effect_day.validate()
        if self.effect_time:
            self.effect_time.validate()
        if self.schedule_effect:
            self.schedule_effect.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect_day is not None:
            result['EffectDay'] = self.effect_day.to_map()

        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time.to_map()

        if self.schedule_effect is not None:
            result['ScheduleEffect'] = self.schedule_effect.to_map()

        if self.valid_type is not None:
            result['ValidType'] = self.valid_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectDay') is not None:
            temp_model = main_models.ExecutePeriodEffectDay()
            self.effect_day = temp_model.from_map(m.get('EffectDay'))

        if m.get('EffectTime') is not None:
            temp_model = main_models.ExecutePeriodEffectTime()
            self.effect_time = temp_model.from_map(m.get('EffectTime'))

        if m.get('ScheduleEffect') is not None:
            temp_model = main_models.ExecutePeriodScheduleEffect()
            self.schedule_effect = temp_model.from_map(m.get('ScheduleEffect'))

        if m.get('ValidType') is not None:
            self.valid_type = m.get('ValidType')

        return self

class ExecutePeriodScheduleEffect(DaraModel):
    def __init__(
        self,
        frequency: str = None,
        interval: int = None,
    ):
        self.frequency = frequency
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.interval is not None:
            result['Interval'] = self.interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        return self

class ExecutePeriodEffectTime(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
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

class ExecutePeriodEffectDay(DaraModel):
    def __init__(
        self,
        friday: bool = None,
        monday: bool = None,
        saturday: bool = None,
        sunday: bool = None,
        thursday: bool = None,
        tuesday: bool = None,
        wednesday: bool = None,
    ):
        self.friday = friday
        self.monday = monday
        self.saturday = saturday
        self.sunday = sunday
        self.thursday = thursday
        self.tuesday = tuesday
        self.wednesday = wednesday

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.friday is not None:
            result['Friday'] = self.friday

        if self.monday is not None:
            result['Monday'] = self.monday

        if self.saturday is not None:
            result['Saturday'] = self.saturday

        if self.sunday is not None:
            result['Sunday'] = self.sunday

        if self.thursday is not None:
            result['Thursday'] = self.thursday

        if self.tuesday is not None:
            result['Tuesday'] = self.tuesday

        if self.wednesday is not None:
            result['Wednesday'] = self.wednesday

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Friday') is not None:
            self.friday = m.get('Friday')

        if m.get('Monday') is not None:
            self.monday = m.get('Monday')

        if m.get('Saturday') is not None:
            self.saturday = m.get('Saturday')

        if m.get('Sunday') is not None:
            self.sunday = m.get('Sunday')

        if m.get('Thursday') is not None:
            self.thursday = m.get('Thursday')

        if m.get('Tuesday') is not None:
            self.tuesday = m.get('Tuesday')

        if m.get('Wednesday') is not None:
            self.wednesday = m.get('Wednesday')

        return self

