# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DsgDesensPlanAddOrUpdateShrinkRequest(DaraModel):
    def __init__(
        self,
        desens_rules_shrink: str = None,
    ):
        # A collection of data masking rules that you want to add or modify.
        # 
        # This parameter is required.
        self.desens_rules_shrink = desens_rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desens_rules_shrink is not None:
            result['DesensRules'] = self.desens_rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesensRules') is not None:
            self.desens_rules_shrink = m.get('DesensRules')

        return self

