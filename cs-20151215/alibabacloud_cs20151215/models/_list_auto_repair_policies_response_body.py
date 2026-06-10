# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListAutoRepairPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListAutoRepairPoliciesResponseBodyItems] = None,
    ):
        # A list of auto-repair rules.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListAutoRepairPoliciesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        return self

class ListAutoRepairPoliciesResponseBodyItems(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        resource_ids: List[str] = None,
        resource_sub_type: str = None,
        resource_type: str = None,
        rules: List[main_models.ListAutoRepairPoliciesResponseBodyItemsRules] = None,
    ):
        # The ID of the auto-repair rule.
        self.id = id
        # The name of the auto-repair rule.
        self.name = name
        # The IDs of the resources that the auto-repair rule affects.
        self.resource_ids = resource_ids
        # The resource sub-type that the auto-repair rule affects.
        self.resource_sub_type = resource_sub_type
        # The resource type that the auto-repair rule affects.
        self.resource_type = resource_type
        # A list of auto-repair sub-rules.
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
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.resource_ids is not None:
            result['resource_ids'] = self.resource_ids

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
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resource_ids') is not None:
            self.resource_ids = m.get('resource_ids')

        if m.get('resource_sub_type') is not None:
            self.resource_sub_type = m.get('resource_sub_type')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.ListAutoRepairPoliciesResponseBodyItemsRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class ListAutoRepairPoliciesResponseBodyItemsRules(DaraModel):
    def __init__(
        self,
        incidents: List[main_models.ListAutoRepairPoliciesResponseBodyItemsRulesIncidents] = None,
        repair_procedure: List[main_models.ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedure] = None,
    ):
        # A list of identified incidents.
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
                temp_model = main_models.ListAutoRepairPoliciesResponseBodyItemsRulesIncidents()
                self.incidents.append(temp_model.from_map(k1))

        self.repair_procedure = []
        if m.get('repair_procedure') is not None:
            for k1 in m.get('repair_procedure'):
                temp_model = main_models.ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedure()
                self.repair_procedure.append(temp_model.from_map(k1))

        return self

class ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedure(DaraModel):
    def __init__(
        self,
        config: Dict[str, Any] = None,
        intervention: main_models.ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedureIntervention = None,
        name: str = None,
    ):
        # The configuration parameters for the procedure step.
        self.config = config
        # The manual intervention settings for this procedure step.
        self.intervention = intervention
        # The name of the procedure step.
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
            temp_model = main_models.ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedureIntervention()
            self.intervention = temp_model.from_map(m.get('intervention'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedureIntervention(DaraModel):
    def __init__(
        self,
        approved_label: main_models.ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedureInterventionApprovedLabel = None,
        enable: bool = None,
        inquiring_label: main_models.ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedureInterventionInquiringLabel = None,
        type: str = None,
    ):
        # The configuration for the approval label. Applying this label to the node authorizes Container Service for Kubernetes (ACK) to execute the action for this repair step. After the step is complete, ACK automatically removes both the inquiry and approval labels. If the approval label is not applied promptly, the repair process will not proceed, and the node may remain in an unhealthy state.
        self.approved_label = approved_label
        # Determines whether manual approval is required for the repair step.
        self.enable = enable
        # The configuration for the authorization inquiry label. When this repair step starts, Container Service for Kubernetes (ACK) applies this label to the node and pauses, awaiting approval before executing the step\\"s action.
        self.inquiring_label = inquiring_label
        # The manual approval type.
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
            temp_model = main_models.ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedureInterventionApprovedLabel()
            self.approved_label = temp_model.from_map(m.get('approved_label'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('inquiring_label') is not None:
            temp_model = main_models.ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedureInterventionInquiringLabel()
            self.inquiring_label = temp_model.from_map(m.get('inquiring_label'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedureInterventionInquiringLabel(DaraModel):
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

class ListAutoRepairPoliciesResponseBodyItemsRulesRepairProcedureInterventionApprovedLabel(DaraModel):
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

class ListAutoRepairPoliciesResponseBodyItemsRulesIncidents(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The incident name.
        self.name = name
        # The diagnosis type.
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

