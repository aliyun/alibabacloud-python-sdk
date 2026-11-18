# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWebFilterRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        rules_shrink: str = None,
    ):
        # The list of web filtering rules to be updated. You can specify up to 20 rules at a time. The rule IDs in the list must be unique.
        # 
        # This parameter is required.
        self.rules_shrink = rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        return self

