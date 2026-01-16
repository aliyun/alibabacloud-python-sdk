# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecommendTemplatesRequest(DaraModel):
    def __init__(
        self,
        usage_scenario: str = None,
    ):
        # *
        # *
        # *
        # *
        # *
        # 
        # **
        # 
        # ****
        # 
        # This parameter is required.
        self.usage_scenario = usage_scenario

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.usage_scenario is not None:
            result['usageScenario'] = self.usage_scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('usageScenario') is not None:
            self.usage_scenario = m.get('usageScenario')

        return self

