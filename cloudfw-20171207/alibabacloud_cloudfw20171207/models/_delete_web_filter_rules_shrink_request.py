# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWebFilterRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        web_filter_rule_ids_shrink: str = None,
    ):
        # The list of web filtering rule IDs to delete. You can specify up to 100 IDs in a single request. The IDs cannot be empty and must be unique.
        # 
        # This parameter is required.
        self.web_filter_rule_ids_shrink = web_filter_rule_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.web_filter_rule_ids_shrink is not None:
            result['WebFilterRuleIds'] = self.web_filter_rule_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WebFilterRuleIds') is not None:
            self.web_filter_rule_ids_shrink = m.get('WebFilterRuleIds')

        return self

