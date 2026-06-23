# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class CreateAutoRepairPolicyRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        resource_sub_type: str = None,
        resource_type: str = None,
        rules: List[main_models.CreateAutoRepairPolicyRequestRules] = None,
    ):
        # The name of the self-healing rule.
        self.name = name
        # The resource subtype that the self-healing rule can be bound to.
        self.resource_sub_type = resource_sub_type
        # The resource type that the self-healing rule can be bound to.
        self.resource_type = resource_type
        # The list of self-healing sub-rules.
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

        if self.resource_sub_type is not None:
            result['resource_sub_type'] = self.resource_sub_type

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resource_sub_type') is not None:
            self.resource_sub_type = m.get('resource_sub_type')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.CreateAutoRepairPolicyRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class CreateAutoRepairPolicyRequestRules(DaraModel):
    def __init__(
        self,
        incidents: List[main_models.CreateAutoRepairPolicyRequestRulesIncidents] = None,
        repair_procedure: List[main_models.CreateAutoRepairPolicyRequestRulesRepairProcedure] = None,
    ):
        # The list of identified faults.
        self.incidents = incidents
        # The repair procedure.
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
                temp_model = main_models.CreateAutoRepairPolicyRequestRulesIncidents()
                self.incidents.append(temp_model.from_map(k1))

        self.repair_procedure = []
        if m.get('repair_procedure') is not None:
            for k1 in m.get('repair_procedure'):
                temp_model = main_models.CreateAutoRepairPolicyRequestRulesRepairProcedure()
                self.repair_procedure.append(temp_model.from_map(k1))

        return self

class CreateAutoRepairPolicyRequestRulesRepairProcedure(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        intervention: main_models.CreateAutoRepairPolicyRequestRulesRepairProcedureIntervention = None,
        name: str = None,
    ):
        # The configuration parameters of the repair procedure.
        self.config = config
        # The configuration for manual intervention in the procedure.
        self.intervention = intervention
        # The name of the procedure.
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
            temp_model = main_models.CreateAutoRepairPolicyRequestRulesRepairProcedureIntervention()
            self.intervention = temp_model.from_map(m.get('intervention'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class CreateAutoRepairPolicyRequestRulesRepairProcedureIntervention(DaraModel):
    def __init__(
        self,
        approved_label: main_models.CreateAutoRepairPolicyRequestRulesRepairProcedureInterventionApprovedLabel = None,
        enable: bool = None,
        inquiring_label: main_models.CreateAutoRepairPolicyRequestRulesRepairProcedureInterventionInquiringLabel = None,
        type: str = None,
    ):
        # The label configuration for authorization confirmation. When you add the following label to the node, you authorize ACK to execute the action in this stage. After completing the action in this stage, ACK automatically removes the authorization inquiry and authorization confirmation labels for this stage. If you do not add the following label to authorize the action promptly, ACK does not execute the action in this stage or subsequent actions, and the node may remain in a damaged state.
        self.approved_label = approved_label
        # Specifies whether to enable manual approval.
        self.enable = enable
        # The label configuration for authorization inquiry. When this stage is reached, ACK adds the following label to your node and waits for you to authorize the execution of the action in this stage.
        self.inquiring_label = inquiring_label
        # The type of manual approval.
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
            temp_model = main_models.CreateAutoRepairPolicyRequestRulesRepairProcedureInterventionApprovedLabel()
            self.approved_label = temp_model.from_map(m.get('approved_label'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('inquiring_label') is not None:
            temp_model = main_models.CreateAutoRepairPolicyRequestRulesRepairProcedureInterventionInquiringLabel()
            self.inquiring_label = temp_model.from_map(m.get('inquiring_label'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateAutoRepairPolicyRequestRulesRepairProcedureInterventionInquiringLabel(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the label.
        self.key = key
        # The value of the label.
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

class CreateAutoRepairPolicyRequestRulesRepairProcedureInterventionApprovedLabel(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the label.
        self.key = key
        # The value of the label.
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

class CreateAutoRepairPolicyRequestRulesIncidents(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the fault.
        self.name = name
        # The type of the fault.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

