# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class UpdateRateLimitRuleInput(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        windows: List[main_models.WindowLimit] = None,
    ):
        # Specifies whether to enable the rate limit rule.
        self.enabled = enabled
        # A list of time window configurations. Providing this parameter replaces the entire existing list.
        self.windows = windows

    def validate(self):
        if self.windows:
            for v1 in self.windows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        result['windows'] = []
        if self.windows is not None:
            for k1 in self.windows:
                result['windows'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        self.windows = []
        if m.get('windows') is not None:
            for k1 in m.get('windows'):
                temp_model = main_models.WindowLimit()
                self.windows.append(temp_model.from_map(k1))

        return self

