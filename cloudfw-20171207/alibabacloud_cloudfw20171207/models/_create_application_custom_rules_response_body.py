# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateApplicationCustomRulesResponseBody(DaraModel):
    def __init__(
        self,
        application_custom_rule_ids: List[str] = None,
        request_id: str = None,
    ):
        # The list of IDs for the newly created custom application rules. The order of the IDs corresponds to the order of the rules in the Rules request parameter.
        self.application_custom_rule_ids = application_custom_rule_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_custom_rule_ids is not None:
            result['ApplicationCustomRuleIds'] = self.application_custom_rule_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCustomRuleIds') is not None:
            self.application_custom_rule_ids = m.get('ApplicationCustomRuleIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

