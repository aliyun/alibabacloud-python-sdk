# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTaskGroupRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        reg_id: str = None,
        sample_ids: str = None,
        scenes: str = None,
        service_codes: str = None,
        service_names: str = None,
        tab: str = None,
        task_group_name: str = None,
        type: str = None,
    ):
        self.lang = lang
        self.reg_id = reg_id
        self.sample_ids = sample_ids
        self.scenes = scenes
        self.service_codes = service_codes
        self.service_names = service_names
        self.tab = tab
        self.task_group_name = task_group_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.sample_ids is not None:
            result['SampleIds'] = self.sample_ids

        if self.scenes is not None:
            result['Scenes'] = self.scenes

        if self.service_codes is not None:
            result['ServiceCodes'] = self.service_codes

        if self.service_names is not None:
            result['ServiceNames'] = self.service_names

        if self.tab is not None:
            result['Tab'] = self.tab

        if self.task_group_name is not None:
            result['TaskGroupName'] = self.task_group_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('SampleIds') is not None:
            self.sample_ids = m.get('SampleIds')

        if m.get('Scenes') is not None:
            self.scenes = m.get('Scenes')

        if m.get('ServiceCodes') is not None:
            self.service_codes = m.get('ServiceCodes')

        if m.get('ServiceNames') is not None:
            self.service_names = m.get('ServiceNames')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('TaskGroupName') is not None:
            self.task_group_name = m.get('TaskGroupName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

