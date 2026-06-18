# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWafQuotaRequest(DaraModel):
    def __init__(
        self,
        paths: str = None,
    ):
        # The path of the WAF quota. Valid values:
        # 
        # - managed_rules_group: The quota for managed rule groups.
        # 
        # - list: The quota for custom lists.
        # 
        # - page: The quota for custom response pages.
        # 
        # - scene_policy: The quota for scene-based protection.
        self.paths = paths

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paths is not None:
            result['Paths'] = self.paths

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        return self

