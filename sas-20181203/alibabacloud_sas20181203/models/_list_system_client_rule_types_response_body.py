# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListSystemClientRuleTypesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule_types: List[str] = None,
    ):
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The list of rule types.
        self.rule_types = rule_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_types is not None:
            result['RuleTypes'] = self.rule_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleTypes') is not None:
            self.rule_types = m.get('RuleTypes')

        return self

