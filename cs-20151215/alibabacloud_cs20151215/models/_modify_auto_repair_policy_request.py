# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ModifyAutoRepairPolicyRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        rules: List[main_models.ModifyAutoRepairPolicyRequestRules] = None,
    ):
        self.name = name
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.ModifyAutoRepairPolicyRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class ModifyAutoRepairPolicyRequestRules(DaraModel):
    def __init__(
        self,
        incidents: List[main_models.ModifyAutoRepairPolicyRequestRulesIncidents] = None,
        repair_procedure: List[main_models.ModifyAutoRepairPolicyRequestRulesRepairProcedure] = None,
    ):
        self.incidents = incidents
        self.repair_procedure = repair_procedure

    def validate(self):
        if self.incidents:
            for v1 in self.incidents:
                 if v1:
                    v1.validate()
        if self.repair_procedure:
            for v1 in self.repair_procedure:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['incidents'] = []
        if self.incidents is not None:
            for k1 in self.incidents:
                result['incidents'].append(k1.to_map() if k1 else None)

        result['repair_procedure'] = []
        if self.repair_procedure is not None:
            for k1 in self.repair_procedure:
                result['repair_procedure'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.incidents = []
        if m.get('incidents') is not None:
            for k1 in m.get('incidents'):
                temp_model = main_models.ModifyAutoRepairPolicyRequestRulesIncidents()
                self.incidents.append(temp_model.from_map(k1))

        self.repair_procedure = []
        if m.get('repair_procedure') is not None:
            for k1 in m.get('repair_procedure'):
                temp_model = main_models.ModifyAutoRepairPolicyRequestRulesRepairProcedure()
                self.repair_procedure.append(temp_model.from_map(k1))

        return self

class ModifyAutoRepairPolicyRequestRulesRepairProcedure(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        intervention: main_models.ModifyAutoRepairPolicyRequestRulesRepairProcedureIntervention = None,
        name: str = None,
    ):
        self.config = config
        self.intervention = intervention
        self.name = name

    def validate(self):
        if self.intervention:
            self.intervention.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.intervention is not None:
            result['intervention'] = self.intervention.to_map()

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('intervention') is not None:
            temp_model = main_models.ModifyAutoRepairPolicyRequestRulesRepairProcedureIntervention()
            self.intervention = temp_model.from_map(m.get('intervention'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ModifyAutoRepairPolicyRequestRulesRepairProcedureIntervention(DaraModel):
    def __init__(
        self,
        approved_label: main_models.ModifyAutoRepairPolicyRequestRulesRepairProcedureInterventionApprovedLabel = None,
        enable: bool = None,
        inquiring_label: main_models.ModifyAutoRepairPolicyRequestRulesRepairProcedureInterventionInquiringLabel = None,
        type: str = None,
    ):
        self.approved_label = approved_label
        self.enable = enable
        self.inquiring_label = inquiring_label
        self.type = type

    def validate(self):
        if self.approved_label:
            self.approved_label.validate()
        if self.inquiring_label:
            self.inquiring_label.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approved_label is not None:
            result['approved_label'] = self.approved_label.to_map()

        if self.enable is not None:
            result['enable'] = self.enable

        if self.inquiring_label is not None:
            result['inquiring_label'] = self.inquiring_label.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approved_label') is not None:
            temp_model = main_models.ModifyAutoRepairPolicyRequestRulesRepairProcedureInterventionApprovedLabel()
            self.approved_label = temp_model.from_map(m.get('approved_label'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('inquiring_label') is not None:
            temp_model = main_models.ModifyAutoRepairPolicyRequestRulesRepairProcedureInterventionInquiringLabel()
            self.inquiring_label = temp_model.from_map(m.get('inquiring_label'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ModifyAutoRepairPolicyRequestRulesRepairProcedureInterventionInquiringLabel(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ModifyAutoRepairPolicyRequestRulesRepairProcedureInterventionApprovedLabel(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ModifyAutoRepairPolicyRequestRulesIncidents(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.ModifyAutoRepairPolicyRequestRulesIncidentsConditions] = None,
        events: List[main_models.ModifyAutoRepairPolicyRequestRulesIncidentsEvents] = None,
        name: str = None,
        type: str = None,
    ):
        self.conditions = conditions
        self.events = events
        self.name = name
        self.type = type

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        result['events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['events'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.ModifyAutoRepairPolicyRequestRulesIncidentsConditions()
                self.conditions.append(temp_model.from_map(k1))

        self.events = []
        if m.get('events') is not None:
            for k1 in m.get('events'):
                temp_model = main_models.ModifyAutoRepairPolicyRequestRulesIncidentsEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ModifyAutoRepairPolicyRequestRulesIncidentsEvents(DaraModel):
    def __init__(
        self,
        reason: str = None,
        type: str = None,
    ):
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['reason'] = self.reason

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ModifyAutoRepairPolicyRequestRulesIncidentsConditions(DaraModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        self.reason = reason
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['reason'] = self.reason

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

