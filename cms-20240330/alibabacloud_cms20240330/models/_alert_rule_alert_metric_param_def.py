# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AlertRuleAlertMetricParamDef(DaraModel):
    def __init__(
        self,
        max_width: int = None,
        min_width: int = None,
        name: str = None,
        placeholder_cn: str = None,
        placeholder_en: str = None,
        type: str = None,
        value: str = None,
        values: List[main_models.AlertRuleAlertMetricParamDefValues] = None,
    ):
        self.max_width = max_width
        self.min_width = min_width
        self.name = name
        self.placeholder_cn = placeholder_cn
        self.placeholder_en = placeholder_en
        self.type = type
        self.value = value
        self.values = values

    def validate(self):
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_width is not None:
            result['maxWidth'] = self.max_width

        if self.min_width is not None:
            result['minWidth'] = self.min_width

        if self.name is not None:
            result['name'] = self.name

        if self.placeholder_cn is not None:
            result['placeholderCn'] = self.placeholder_cn

        if self.placeholder_en is not None:
            result['placeholderEn'] = self.placeholder_en

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        result['values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxWidth') is not None:
            self.max_width = m.get('maxWidth')

        if m.get('minWidth') is not None:
            self.min_width = m.get('minWidth')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('placeholderCn') is not None:
            self.placeholder_cn = m.get('placeholderCn')

        if m.get('placeholderEn') is not None:
            self.placeholder_en = m.get('placeholderEn')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        self.values = []
        if m.get('values') is not None:
            for k1 in m.get('values'):
                temp_model = main_models.AlertRuleAlertMetricParamDefValues()
                self.values.append(temp_model.from_map(k1))

        return self

class AlertRuleAlertMetricParamDefValues(DaraModel):
    def __init__(
        self,
        label_cn: str = None,
        label_en: str = None,
        value: str = None,
    ):
        self.label_cn = label_cn
        self.label_en = label_en
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_cn is not None:
            result['labelCn'] = self.label_cn

        if self.label_en is not None:
            result['labelEn'] = self.label_en

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelCn') is not None:
            self.label_cn = m.get('labelCn')

        if m.get('labelEn') is not None:
            self.label_en = m.get('labelEn')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

