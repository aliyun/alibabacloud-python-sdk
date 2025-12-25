# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class WafRuleMatch(DaraModel):
    def __init__(
        self,
        convert_to_lower: bool = None,
        criteria: List[main_models.WafRuleMatch] = None,
        logic: str = None,
        match_operator: str = None,
        match_type: str = None,
        match_value: Any = None,
        negate: bool = None,
    ):
        self.convert_to_lower = convert_to_lower
        self.criteria = criteria
        self.logic = logic
        self.match_operator = match_operator
        self.match_type = match_type
        self.match_value = match_value
        self.negate = negate

    def validate(self):
        if self.criteria:
            for v1 in self.criteria:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.convert_to_lower is not None:
            result['ConvertToLower'] = self.convert_to_lower

        result['Criteria'] = []
        if self.criteria is not None:
            for k1 in self.criteria:
                result['Criteria'].append(k1.to_map() if k1 else None)

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.match_operator is not None:
            result['MatchOperator'] = self.match_operator

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.match_value is not None:
            result['MatchValue'] = self.match_value

        if self.negate is not None:
            result['Negate'] = self.negate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertToLower') is not None:
            self.convert_to_lower = m.get('ConvertToLower')

        self.criteria = []
        if m.get('Criteria') is not None:
            for k1 in m.get('Criteria'):
                temp_model = main_models.WafRuleMatch()
                self.criteria.append(temp_model.from_map(k1))

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('MatchOperator') is not None:
            self.match_operator = m.get('MatchOperator')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('MatchValue') is not None:
            self.match_value = m.get('MatchValue')

        if m.get('Negate') is not None:
            self.negate = m.get('Negate')

        return self

