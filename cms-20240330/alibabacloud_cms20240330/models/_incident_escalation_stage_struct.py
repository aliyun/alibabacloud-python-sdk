# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentEscalationStageStruct(DaraModel):
    def __init__(
        self,
        contact: List[main_models.IncidentContactStruct] = None,
        cycle_notify_count: int = None,
        cycle_notify_time: int = None,
        description: str = None,
        effect_time: str = None,
        name: str = None,
        stage_index: int = None,
        time_zone: str = None,
        wait_to_next_stage_time: int = None,
    ):
        self.contact = contact
        self.cycle_notify_count = cycle_notify_count
        self.cycle_notify_time = cycle_notify_time
        self.description = description
        self.effect_time = effect_time
        self.name = name
        self.stage_index = stage_index
        self.time_zone = time_zone
        self.wait_to_next_stage_time = wait_to_next_stage_time

    def validate(self):
        if self.contact:
            for v1 in self.contact:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['contact'] = []
        if self.contact is not None:
            for k1 in self.contact:
                result['contact'].append(k1.to_map() if k1 else None)

        if self.cycle_notify_count is not None:
            result['cycleNotifyCount'] = self.cycle_notify_count

        if self.cycle_notify_time is not None:
            result['cycleNotifyTime'] = self.cycle_notify_time

        if self.description is not None:
            result['description'] = self.description

        if self.effect_time is not None:
            result['effectTime'] = self.effect_time

        if self.name is not None:
            result['name'] = self.name

        if self.stage_index is not None:
            result['stageIndex'] = self.stage_index

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        if self.wait_to_next_stage_time is not None:
            result['waitToNextStageTime'] = self.wait_to_next_stage_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact = []
        if m.get('contact') is not None:
            for k1 in m.get('contact'):
                temp_model = main_models.IncidentContactStruct()
                self.contact.append(temp_model.from_map(k1))

        if m.get('cycleNotifyCount') is not None:
            self.cycle_notify_count = m.get('cycleNotifyCount')

        if m.get('cycleNotifyTime') is not None:
            self.cycle_notify_time = m.get('cycleNotifyTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('effectTime') is not None:
            self.effect_time = m.get('effectTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('stageIndex') is not None:
            self.stage_index = m.get('stageIndex')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        if m.get('waitToNextStageTime') is not None:
            self.wait_to_next_stage_time = m.get('waitToNextStageTime')

        return self

