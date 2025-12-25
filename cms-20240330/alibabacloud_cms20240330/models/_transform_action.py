# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class TransformAction(DaraModel):
    def __init__(
        self,
        filter_setting: main_models.FilterSetting = None,
        label_key: str = None,
        mapping: Dict[str, str] = None,
        reg_exp: str = None,
        source: str = None,
        target: str = None,
        type: str = None,
        value: str = None,
        variable: str = None,
    ):
        self.filter_setting = filter_setting
        self.label_key = label_key
        self.mapping = mapping
        self.reg_exp = reg_exp
        self.source = source
        self.target = target
        self.type = type
        self.value = value
        self.variable = variable

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()

        if self.label_key is not None:
            result['labelKey'] = self.label_key

        if self.mapping is not None:
            result['mapping'] = self.mapping

        if self.reg_exp is not None:
            result['regExp'] = self.reg_exp

        if self.source is not None:
            result['source'] = self.source

        if self.target is not None:
            result['target'] = self.target

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        if self.variable is not None:
            result['variable'] = self.variable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterSetting') is not None:
            temp_model = main_models.FilterSetting()
            self.filter_setting = temp_model.from_map(m.get('filterSetting'))

        if m.get('labelKey') is not None:
            self.label_key = m.get('labelKey')

        if m.get('mapping') is not None:
            self.mapping = m.get('mapping')

        if m.get('regExp') is not None:
            self.reg_exp = m.get('regExp')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('variable') is not None:
            self.variable = m.get('variable')

        return self

