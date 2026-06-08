# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetProcessDefinitionResponseBody(DaraModel):
    def __init__(
        self,
        process_definition: main_models.GetProcessDefinitionResponseBodyProcessDefinition = None,
        request_id: str = None,
    ):
        self.process_definition = process_definition
        self.request_id = request_id

    def validate(self):
        if self.process_definition:
            self.process_definition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_definition is not None:
            result['ProcessDefinition'] = self.process_definition.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessDefinition') is not None:
            temp_model = main_models.GetProcessDefinitionResponseBodyProcessDefinition()
            self.process_definition = temp_model.from_map(m.get('ProcessDefinition'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProcessDefinitionResponseBodyProcessDefinition(DaraModel):
    def __init__(
        self,
        approval_nodes: List[main_models.GetProcessDefinitionResponseBodyProcessDefinitionApprovalNodes] = None,
        description: str = None,
        enabled: bool = None,
        id: str = None,
        is_system: bool = None,
        name: str = None,
        notification_services: List[main_models.GetProcessDefinitionResponseBodyProcessDefinitionNotificationServices] = None,
        rule_conditions: List[main_models.GetProcessDefinitionResponseBodyProcessDefinitionRuleConditions] = None,
        sub_type: str = None,
        type: str = None,
    ):
        self.approval_nodes = approval_nodes
        self.description = description
        self.enabled = enabled
        self.id = id
        self.is_system = is_system
        self.name = name
        self.notification_services = notification_services
        self.rule_conditions = rule_conditions
        self.sub_type = sub_type
        self.type = type

    def validate(self):
        if self.approval_nodes:
            for v1 in self.approval_nodes:
                 if v1:
                    v1.validate()
        if self.notification_services:
            for v1 in self.notification_services:
                 if v1:
                    v1.validate()
        if self.rule_conditions:
            for v1 in self.rule_conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApprovalNodes'] = []
        if self.approval_nodes is not None:
            for k1 in self.approval_nodes:
                result['ApprovalNodes'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.is_system is not None:
            result['IsSystem'] = self.is_system

        if self.name is not None:
            result['Name'] = self.name

        result['NotificationServices'] = []
        if self.notification_services is not None:
            for k1 in self.notification_services:
                result['NotificationServices'].append(k1.to_map() if k1 else None)

        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k1 in self.rule_conditions:
                result['RuleConditions'].append(k1.to_map() if k1 else None)

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approval_nodes = []
        if m.get('ApprovalNodes') is not None:
            for k1 in m.get('ApprovalNodes'):
                temp_model = main_models.GetProcessDefinitionResponseBodyProcessDefinitionApprovalNodes()
                self.approval_nodes.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsSystem') is not None:
            self.is_system = m.get('IsSystem')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.notification_services = []
        if m.get('NotificationServices') is not None:
            for k1 in m.get('NotificationServices'):
                temp_model = main_models.GetProcessDefinitionResponseBodyProcessDefinitionNotificationServices()
                self.notification_services.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.GetProcessDefinitionResponseBodyProcessDefinitionRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetProcessDefinitionResponseBodyProcessDefinitionRuleConditions(DaraModel):
    def __init__(
        self,
        expression: str = None,
        scope: str = None,
        type: str = None,
    ):
        self.expression = expression
        self.scope = scope
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetProcessDefinitionResponseBodyProcessDefinitionNotificationServices(DaraModel):
    def __init__(
        self,
        channel: str = None,
        extension: str = None,
        receiver: str = None,
    ):
        self.channel = channel
        self.extension = extension
        self.receiver = receiver

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.receiver is not None:
            result['Receiver'] = self.receiver

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')

        return self

class GetProcessDefinitionResponseBodyProcessDefinitionApprovalNodes(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        assignees: List[str] = None,
        extension_properties: Dict[str, Any] = None,
        id: str = None,
        name: str = None,
    ):
        self.account_type = account_type
        self.assignees = assignees
        self.extension_properties = extension_properties
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.assignees is not None:
            result['Assignees'] = self.assignees

        if self.extension_properties is not None:
            result['ExtensionProperties'] = self.extension_properties

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('Assignees') is not None:
            self.assignees = m.get('Assignees')

        if m.get('ExtensionProperties') is not None:
            self.extension_properties = m.get('ExtensionProperties')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

