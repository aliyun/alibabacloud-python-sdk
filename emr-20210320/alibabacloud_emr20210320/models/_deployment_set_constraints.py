# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class DeploymentSetConstraints(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        enable_state: str = None,
        replacement_strategy: main_models.ReplacementStrategy = None,
        values: List[str] = None,
    ):
        # 默认值。
        self.default_value = default_value
        self.enable_state = enable_state
        # 替换策略。
        self.replacement_strategy = replacement_strategy
        # 枚举值。
        self.values = values

    def validate(self):
        if self.replacement_strategy:
            self.replacement_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.enable_state is not None:
            result['EnableState'] = self.enable_state

        if self.replacement_strategy is not None:
            result['ReplacementStrategy'] = self.replacement_strategy.to_map()

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('EnableState') is not None:
            self.enable_state = m.get('EnableState')

        if m.get('ReplacementStrategy') is not None:
            temp_model = main_models.ReplacementStrategy()
            self.replacement_strategy = temp_model.from_map(m.get('ReplacementStrategy'))

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

