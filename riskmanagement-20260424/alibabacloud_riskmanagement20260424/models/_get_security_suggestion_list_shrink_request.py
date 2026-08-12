# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSecuritySuggestionListShrinkRequest(DaraModel):
    def __init__(
        self,
        list_config_rules_request_shrink: str = None,
    ):
        # The request parameters.
        self.list_config_rules_request_shrink = list_config_rules_request_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_config_rules_request_shrink is not None:
            result['ListConfigRulesRequest'] = self.list_config_rules_request_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListConfigRulesRequest') is not None:
            self.list_config_rules_request_shrink = m.get('ListConfigRulesRequest')

        return self

