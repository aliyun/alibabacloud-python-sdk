# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateProcessDefinitionRequest(DaraModel):
    def __init__(
        self,
        approval_nodes: List[main_models.UpdateProcessDefinitionRequestApprovalNodes] = None,
        client_token: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        notification_services: List[main_models.UpdateProcessDefinitionRequestNotificationServices] = None,
        rule_conditions: List[main_models.UpdateProcessDefinitionRequestRuleConditions] = None,
    ):
        # A list of approval nodes. This parameter does not apply to system policies.
        self.approval_nodes = approval_nodes
        # An idempotent parameter. It ensures that retried requests do not result in duplicate operations.
        self.client_token = client_token
        # The description of the process definition.
        self.description = description
        # The ID of the process definition.
        # 
        # This parameter is required.
        self.id = id
        # The name of the process definition.
        self.name = name
        # The notification service configurations.
        self.notification_services = notification_services
        # A list of rule conditions. This parameter does not apply to system policies.
        self.rule_conditions = rule_conditions

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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approval_nodes = []
        if m.get('ApprovalNodes') is not None:
            for k1 in m.get('ApprovalNodes'):
                temp_model = main_models.UpdateProcessDefinitionRequestApprovalNodes()
                self.approval_nodes.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.notification_services = []
        if m.get('NotificationServices') is not None:
            for k1 in m.get('NotificationServices'):
                temp_model = main_models.UpdateProcessDefinitionRequestNotificationServices()
                self.notification_services.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.UpdateProcessDefinitionRequestRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        return self

class UpdateProcessDefinitionRequestRuleConditions(DaraModel):
    def __init__(
        self,
        expression: str = None,
        scope: str = None,
        type: str = None,
    ):
        # The conditional expression. Format: ((#type==\\"typeValue\\")). For example: ((#odpsProject==\\"PX_BEIJING_TEST\\")).
        self.expression = expression
        # The phase in which the rule takes effect. Valid values:
        # 
        # - **Deployment**: Determines whether the approval policy applies when an application is submitted.
        # 
        # - **Running**: Determines whether to skip the approval during the approval process. This phase is supported only for MaxCompute.
        self.scope = scope
        # The type of the condition. Valid values:
        # 
        # - `odpsProject`
        # 
        # - `hologresInstanceId`
        # 
        # - `sensibleLevel`
        # 
        # - `tableGuid`
        # 
        # - `projectId`
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

class UpdateProcessDefinitionRequestNotificationServices(DaraModel):
    def __init__(
        self,
        channel: str = None,
        extension: str = None,
        receiver: str = None,
    ):
        # The notification channel. Valid values:
        # 
        # - Mail
        # 
        # - Sms
        # 
        # - DingRobot
        # 
        # - Weixin
        self.channel = channel
        # Additional information in JSON format. For example, use {"atAll":"true"} to specify whether to notify all members.
        self.extension = extension
        # The webhook URL. This parameter is required when `Channel` is set to `DingRobot` or `Weixin`.
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

class UpdateProcessDefinitionRequestApprovalNodes(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        assignees: str = None,
        extension_properties: Dict[str, Any] = None,
        name: str = None,
    ):
        # The approver type for the node. Valid values:
        # 
        # - `DataWorksProjectRole`: A workspace role.
        # 
        # - `DataWorksProjectMember`: A workspace member.
        # 
        # - `TableAdministrator`: A table administrator.
        # 
        # - `TableOrProjectAdministrator`: The administrator of the table or project.
        # 
        # - `AliyunResourceOwner`: An Alibaba Cloud account.
        # 
        # - `MaxComputeRole`: A MaxCompute administrator.
        # 
        # - `DLFAdmin`: A DlfLegacy administrator.
        # 
        # - `DLFNextAdmin`: A DLFNext administrator.
        # 
        # - `TenantRole`: A tenant role.
        # 
        # - `EmrAdministrator`: An EMR administrator.
        # 
        # - `LindormAdministrator`: A Lindorm administrator.
        # 
        # - `AliyunRamUser`: A RAM user.
        self.account_type = account_type
        # Specifies the approvers. The required value depends on the `AccountType`:
        # 
        # - If `AccountType` is `DataWorksProjectMember`, this parameter specifies the user IDs of workspace members.
        # 
        # - If `AccountType` is `DataWorksProjectRole`, this parameter specifies the codes of workspace roles.
        # 
        # - If `AccountType` is `MaxComputeRole`, this parameter specifies the MaxCompute roles.
        # 
        # - If `AccountType` is `TenantRole`, this parameter specifies the codes of tenant roles.
        # 
        # - If `AccountType` is `AliyunRamUser`, this parameter specifies the user IDs of RAM users.
        self.assignees = assignees
        # Additional properties that are required for specific `AccountType` values:
        # 
        # - If `AccountType` is `DataWorksProjectMember`: The key is `projectId` and the value is the user ID of a workspace member. Use commas (,) to separate multiple user IDs.
        # 
        # - If `AccountType` is `MaxComputeRole`: The key is the MaxCompute project name and the value is the role name in MaxCompute. Use commas (,) to separate multiple role names.
        self.extension_properties = extension_properties
        # The name of the node.
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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

