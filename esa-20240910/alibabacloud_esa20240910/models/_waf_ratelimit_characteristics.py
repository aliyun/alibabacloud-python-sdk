# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class WafRatelimitCharacteristics(DaraModel):
    def __init__(
        self,
        criteria: List[main_models.WafRatelimitCharacteristicsCriteria] = None,
        logic: str = None,
        match_type: str = None,
    ):
        self.criteria = criteria
        self.logic = logic
        self.match_type = match_type

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
        result['Criteria'] = []
        if self.criteria is not None:
            for k1 in self.criteria:
                result['Criteria'].append(k1.to_map() if k1 else None)

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.criteria = []
        if m.get('Criteria') is not None:
            for k1 in m.get('Criteria'):
                temp_model = main_models.WafRatelimitCharacteristicsCriteria()
                self.criteria.append(temp_model.from_map(k1))

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        return self

class WafRatelimitCharacteristicsCriteria(DaraModel):
    def __init__(
        self,
        criteria: List[main_models.WafRatelimitCharacteristicsCriteriaCriteria] = None,
        logic: str = None,
        match_type: str = None,
    ):
        self.criteria = criteria
        self.logic = logic
        self.match_type = match_type

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
        result['Criteria'] = []
        if self.criteria is not None:
            for k1 in self.criteria:
                result['Criteria'].append(k1.to_map() if k1 else None)

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.criteria = []
        if m.get('Criteria') is not None:
            for k1 in m.get('Criteria'):
                temp_model = main_models.WafRatelimitCharacteristicsCriteriaCriteria()
                self.criteria.append(temp_model.from_map(k1))

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        return self

class WafRatelimitCharacteristicsCriteriaCriteria(DaraModel):
    def __init__(
        self,
        criteria: List[main_models.WafRatelimitCharacteristicsCriteriaCriteriaCriteria] = None,
        logic: str = None,
        match_type: str = None,
    ):
        self.criteria = criteria
        self.logic = logic
        self.match_type = match_type

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
        result['Criteria'] = []
        if self.criteria is not None:
            for k1 in self.criteria:
                result['Criteria'].append(k1.to_map() if k1 else None)

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.criteria = []
        if m.get('Criteria') is not None:
            for k1 in m.get('Criteria'):
                temp_model = main_models.WafRatelimitCharacteristicsCriteriaCriteriaCriteria()
                self.criteria.append(temp_model.from_map(k1))

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        return self

class WafRatelimitCharacteristicsCriteriaCriteriaCriteria(DaraModel):
    def __init__(
        self,
        match_type: str = None,
    ):
        self.match_type = match_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['MatchType'] = self.match_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        return self

