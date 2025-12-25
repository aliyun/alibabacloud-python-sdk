# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class MaintainWindowForView(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        effect_time_range: main_models.MaintainWindowForViewEffectTimeRange = None,
        effective: str = None,
        enable: bool = None,
        end_time: str = None,
        filter_setting: main_models.FilterSetting = None,
        maintain_window_id: str = None,
        maintain_window_name: str = None,
        start_time: str = None,
        update_time: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.effect_time_range = effect_time_range
        self.effective = effective
        self.enable = enable
        self.end_time = end_time
        self.filter_setting = filter_setting
        self.maintain_window_id = maintain_window_id
        # This parameter is required.
        self.maintain_window_name = maintain_window_name
        self.start_time = start_time
        self.update_time = update_time
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.effect_time_range:
            self.effect_time_range.validate()
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.effect_time_range is not None:
            result['effectTimeRange'] = self.effect_time_range.to_map()

        if self.effective is not None:
            result['effective'] = self.effective

        if self.enable is not None:
            result['enable'] = self.enable

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.maintain_window_id is not None:
            result['maintainWindowId'] = self.maintain_window_id

        if self.maintain_window_name is not None:
            result['maintainWindowName'] = self.maintain_window_name

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('effectTimeRange') is not None:
            temp_model = main_models.MaintainWindowForViewEffectTimeRange()
            self.effect_time_range = temp_model.from_map(m.get('effectTimeRange'))

        if m.get('effective') is not None:
            self.effective = m.get('effective')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('maintainWindowId') is not None:
            self.maintain_window_id = m.get('maintainWindowId')

        if m.get('maintainWindowName') is not None:
            self.maintain_window_name = m.get('maintainWindowName')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class MaintainWindowForViewEffectTimeRange(DaraModel):
    def __init__(
        self,
        day_in_week: List[int] = None,
        end_time_in_minute: int = None,
        start_time_in_minute: int = None,
        time_zone: str = None,
    ):
        self.day_in_week = day_in_week
        self.end_time_in_minute = end_time_in_minute
        self.start_time_in_minute = start_time_in_minute
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day_in_week is not None:
            result['dayInWeek'] = self.day_in_week

        if self.end_time_in_minute is not None:
            result['endTimeInMinute'] = self.end_time_in_minute

        if self.start_time_in_minute is not None:
            result['startTimeInMinute'] = self.start_time_in_minute

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayInWeek') is not None:
            self.day_in_week = m.get('dayInWeek')

        if m.get('endTimeInMinute') is not None:
            self.end_time_in_minute = m.get('endTimeInMinute')

        if m.get('startTimeInMinute') is not None:
            self.start_time_in_minute = m.get('startTimeInMinute')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

