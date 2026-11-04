# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class CreateTimeTemplateRequest(DaraModel):
    def __init__(
        self,
        all_day: int = None,
        name: str = None,
        time_sections: List[main_models.CreateTimeTemplateRequestTimeSections] = None,
    ):
        # Specifies whether to enable 24/7 recording. Valid values:
        # - 1: Yes.
        # - 0: No. You must configure the TimeSections.N.DayOfWeek, TimeSections.N.Begin, and TimeSections.N.End parameters.
        # 
        # This parameter is required.
        self.all_day = all_day
        # The name of the time template.
        # 
        # The name must be fewer than 48 characters in length and can contain letters, digits, and the following special characters: hyphens (-), underscores (_), at signs (@), periods (.), and colons (:).
        # 
        # This parameter is required.
        self.name = name
        # The list of time ranges.
        self.time_sections = time_sections

    def validate(self):
        if self.time_sections:
            for v1 in self.time_sections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_day is not None:
            result['AllDay'] = self.all_day

        if self.name is not None:
            result['Name'] = self.name

        result['TimeSections'] = []
        if self.time_sections is not None:
            for k1 in self.time_sections:
                result['TimeSections'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.time_sections = []
        if m.get('TimeSections') is not None:
            for k1 in m.get('TimeSections'):
                temp_model = main_models.CreateTimeTemplateRequestTimeSections()
                self.time_sections.append(temp_model.from_map(k1))

        return self

class CreateTimeTemplateRequestTimeSections(DaraModel):
    def __init__(
        self,
        begin: int = None,
        day_of_week: int = None,
        end: int = None,
    ):
        # The start time of each day. Valid values: 0 to 86399. Unit: seconds.
        self.begin = begin
        # The day of the week. Valid values: 0 to 6, which represent Sunday through Saturday.
        self.day_of_week = day_of_week
        # The end time of each day. Valid values: 1 to 86399. Unit: seconds.
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week

        if self.end is not None:
            result['End'] = self.end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')

        if m.get('End') is not None:
            self.end = m.get('End')

        return self

