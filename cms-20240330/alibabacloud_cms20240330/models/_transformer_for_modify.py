# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class TransformerForModify(DaraModel):
    def __init__(
        self,
        actions: List[main_models.TransformAction] = None,
        description: str = None,
        filter_setting: main_models.FilterSetting = None,
        quit_after_match: bool = None,
        sort_id: int = None,
        transformer_name: str = None,
    ):
        self.actions = actions
        self.description = description
        self.filter_setting = filter_setting
        self.quit_after_match = quit_after_match
        self.sort_id = sort_id
        # This parameter is required.
        self.transformer_name = transformer_name

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['actions'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.quit_after_match is not None:
            result['quitAfterMatch'] = self.quit_after_match

        if self.sort_id is not None:
            result['sortId'] = self.sort_id

        if self.transformer_name is not None:
            result['transformerName'] = self.transformer_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('actions') is not None:
            for k1 in m.get('actions'):
                temp_model = main_models.TransformAction()
                self.actions.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('quitAfterMatch') is not None:
            self.quit_after_match = m.get('quitAfterMatch')

        if m.get('sortId') is not None:
            self.sort_id = m.get('sortId')

        if m.get('transformerName') is not None:
            self.transformer_name = m.get('transformerName')

        return self

