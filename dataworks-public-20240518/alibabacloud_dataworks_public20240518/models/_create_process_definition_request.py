# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateProcessDefinitionRequest(DaraModel):
    def __init__(
        self,
        approval_nodes: List[main_models.CreateProcessDefinitionRequestApprovalNodes] = None,
        client_token: str = None,
        description: str = None,
        enabled: bool = None,
        name: str = None,
        notification_services: List[main_models.CreateProcessDefinitionRequestNotificationServices] = None,
        rule_conditions: List[main_models.CreateProcessDefinitionRequestRuleConditions] = None,
        sub_type: str = None,
        type: str = None,
    ):
        # The list of approval nodes.
        # 
        # This parameter is required.
        self.approval_nodes = approval_nodes
        # The idempotency token. We recommend that you use a UUID.
        self.client_token = client_token
        # The description of the process definition.
        # 
        # This parameter is required.
        self.description = description
        # Specifies whether to enable the process definition.
        self.enabled = enabled
        # The name of the process definition.
        # 
        # This parameter is required.
        self.name = name
        # The notification service declarations.
        self.notification_services = notification_services
        # The list of condition rules.
        # 
        # This parameter is required.
        self.rule_conditions = rule_conditions
        # The subtype. Valid values:
        # 
        # - Table
        # - Column
        # - Database
        # - Schema
        # - Default
        self.sub_type = sub_type
        # The type of the process definition. Valid values:
        # 
        # 1. MaxCompute
        # 2. DataService
        # 3. Extension
        # 4. Hologres
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

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
                temp_model = main_models.CreateProcessDefinitionRequestApprovalNodes()
                self.approval_nodes.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.notification_services = []
        if m.get('NotificationServices') is not None:
            for k1 in m.get('NotificationServices'):
                temp_model = main_models.CreateProcessDefinitionRequestNotificationServices()
                self.notification_services.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.CreateProcessDefinitionRequestRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateProcessDefinitionRequestRuleConditions(DaraModel):
    def __init__(
        self,
        expression: str = None,
        scope: str = None,
        type: str = None,
    ):
        # The condition expression in the format of ((#type==\\"typeValue\\")). Example: ((#odpsProject==\\"PX_BEIJING_TEST\\")).
        self.expression = expression
        # The stage at which the rule takes effect:
        # - `Deployment`: used to determine whether the approval policy matches when a request is submitted.
        # - `Running`: used to determine whether approval is exempted during the execution of the approval process. This value is supported only for the MaxCompute type.
        self.scope = scope
        # The condition type. Valid values:
        # 
        # - `odpsProject`
        # - `hologresInstanceId`
        # - `sensibleLevel`
        # - `tableGuid`
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

class CreateProcessDefinitionRequestNotificationServices(DaraModel):
    def __init__(
        self,
        channel: str = None,
        extension: str = None,
        receiver: str = None,
    ):
        # The notification channel. Valid values:
        # 
        # - Mail
        # - Sms
        # - DingRobot
        # - Weixin
        self.channel = channel
        # The extension information in JSON format. Example: `{"atAll":"true"}`, which specifies whether to mention all members.
        self.extension = extension
        # The WebhookUrl that must be specified when Channel is set to DingRobot or Weixin.
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

class CreateProcessDefinitionRequestApprovalNodes(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        assignees: List[str] = None,
        extension_properties: Dict[str, Any] = None,
        name: str = None,
    ):
        # The type of approver for the node:
        # - DataWorksProjectRole: workspace role.
        # - DataWorksProjectMember: workspace member.
        # - TableAdministrator: table owner.
        # - TableOrProjectAdministrator: table or workspace administrator.
        # - AliyunResourceOwner: Alibaba Cloud account.
        # - MaxComputeRole: MaxCompute administrator.
        # - DLFAdmin: DLF Legacy administrator.
        # - DLFNextAdmin: DLF Next administrator.
        # - TenantRole: tenant role.
        # - EmrAdministrator: EMR administrator.
        # - LindormAdministrator: Lindorm administrator.
        # - AliyunRamUser: RAM user.
        self.account_type = account_type
        # The semantics of this parameter varies based on the value of `AccountType`:
        # - DataWorksProjectMember: the user ID of the workspace member.
        # - DataWorksProjectRole: the code of the workspace role. If a custom workspace role is required, set this parameter to "custom-role" and further configure the role in ExtensionProperties.
        # - MaxComputeRole: the MaxCompute role.
        # - TenantRole: the code of the tenant role.
        # - AliyunRamUser: the RAM user ID.
        self.assignees = assignees
        # The additional declarations required based on the value of `AccountType`:
        # 
        # - DataWorksProjectMember: specify different workspace member user IDs. The key is the workspace ID, and the value is the user ID of the workspace member. Separate multiple user IDs with commas (,).
        # 
        # - DataWorksProjectRole: specify different custom workspace role codes. The key is the workspace ID, and the value is the custom workspace role code. Separate multiple role codes with commas (,).
        # 
        # - MaxComputeRole: specify the roles under a MaxCompute project. The key is the MaxCompute project name, and the value is the role name in MaxCompute. Separate multiple role names with commas (,).
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

