# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListWafPhasesResponseBody(DaraModel):
    def __init__(
        self,
        phases: List[main_models.ListWafPhasesResponseBodyPhases] = None,
        request_id: str = None,
    ):
        # List of WAF operation phases.
        self.phases = phases
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.phases:
            for v1 in self.phases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Phases'] = []
        if self.phases is not None:
            for k1 in self.phases:
                result['Phases'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.phases = []
        if m.get('Phases') is not None:
            for k1 in m.get('Phases'):
                temp_model = main_models.ListWafPhasesResponseBodyPhases()
                self.phases.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListWafPhasesResponseBodyPhases(DaraModel):
    def __init__(
        self,
        phase: str = None,
        rulesets: List[main_models.ListWafPhasesResponseBodyPhasesRulesets] = None,
    ):
        # Name of the WAF operation phase.
        self.phase = phase
        # List of WAF rulesets.
        self.rulesets = rulesets

    def validate(self):
        if self.rulesets:
            for v1 in self.rulesets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phase is not None:
            result['Phase'] = self.phase

        result['Rulesets'] = []
        if self.rulesets is not None:
            for k1 in self.rulesets:
                result['Rulesets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        self.rulesets = []
        if m.get('Rulesets') is not None:
            for k1 in m.get('Rulesets'):
                temp_model = main_models.ListWafPhasesResponseBodyPhasesRulesets()
                self.rulesets.append(temp_model.from_map(k1))

        return self

class ListWafPhasesResponseBodyPhasesRulesets(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        rules: List[main_models.WafRuleConfig] = None,
        shared: main_models.WafBatchRuleShared = None,
    ):
        # ID of the WAF ruleset.
        self.id = id
        # Name of the WAF ruleset.
        self.name = name
        # List of rule configurations in the WAF ruleset.
        self.rules = rules
        # Shared configuration for rules in the WAF ruleset.
        self.shared = shared

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.shared:
            self.shared.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.shared is not None:
            result['Shared'] = self.shared.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.WafRuleConfig()
                self.rules.append(temp_model.from_map(k1))

        if m.get('Shared') is not None:
            temp_model = main_models.WafBatchRuleShared()
            self.shared = temp_model.from_map(m.get('Shared'))

        return self

