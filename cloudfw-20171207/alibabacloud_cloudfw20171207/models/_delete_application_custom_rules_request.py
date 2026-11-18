# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteApplicationCustomRulesRequest(DaraModel):
    def __init__(
        self,
        application_custom_rule_ids: List[str] = None,
    ):
        # The list of IDs of the custom application rules to delete. You can specify up to 100 IDs in a single request. The IDs cannot be empty and must be unique.
        # 
        # This parameter is required.
        self.application_custom_rule_ids = application_custom_rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_custom_rule_ids is not None:
            result['ApplicationCustomRuleIds'] = self.application_custom_rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCustomRuleIds') is not None:
            self.application_custom_rule_ids = m.get('ApplicationCustomRuleIds')

        return self

