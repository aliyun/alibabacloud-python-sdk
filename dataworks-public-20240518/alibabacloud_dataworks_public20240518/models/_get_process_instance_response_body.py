# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetProcessInstanceResponseBody(DaraModel):
    def __init__(
        self,
        process_instance: main_models.GetProcessInstanceResponseBodyProcessInstance = None,
        request_id: str = None,
    ):
        # Details of the approval process instance.
        self.process_instance = process_instance
        # The request ID. Use this ID to locate logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.process_instance:
            self.process_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_instance is not None:
            result['ProcessInstance'] = self.process_instance.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessInstance') is not None:
            temp_model = main_models.GetProcessInstanceResponseBodyProcessInstance()
            self.process_instance = temp_model.from_map(m.get('ProcessInstance'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProcessInstanceResponseBodyProcessInstance(DaraModel):
    def __init__(
        self,
        applicator: str = None,
        applicator_name: str = None,
        approval_process_definition: main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinition = None,
        approval_tasks: List[main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalTasks] = None,
        auth_error_message: str = None,
        id: str = None,
        reason: str = None,
        start_time: Any = None,
        status: str = None,
        title: str = None,
    ):
        # The user ID of the applicant.
        self.applicator = applicator
        # The username of the applicant\\"s Alibaba Cloud account.
        self.applicator_name = applicator_name
        # The approval policy applied to this process instance.
        self.approval_process_definition = approval_process_definition
        # The approval tasks.
        self.approval_tasks = approval_tasks
        # The authorization failure message.
        # 
        # **Note**: This parameter is returned only if the authorization fails.
        self.auth_error_message = auth_error_message
        # The process instance ID.
        self.id = id
        # The reason for the request.
        self.reason = reason
        # The time when the approval process started.
        self.start_time = start_time
        # The status of the process instance. Valid values:
        # 
        # - `Completed`: The request is approved.
        # 
        # - `Running`: The request is in the approval process.
        # 
        # - `Aborted`: The request is withdrawn.
        self.status = status
        # The name of the process instance.
        self.title = title

    def validate(self):
        if self.approval_process_definition:
            self.approval_process_definition.validate()
        if self.approval_tasks:
            for v1 in self.approval_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicator is not None:
            result['Applicator'] = self.applicator

        if self.applicator_name is not None:
            result['ApplicatorName'] = self.applicator_name

        if self.approval_process_definition is not None:
            result['ApprovalProcessDefinition'] = self.approval_process_definition.to_map()

        result['ApprovalTasks'] = []
        if self.approval_tasks is not None:
            for k1 in self.approval_tasks:
                result['ApprovalTasks'].append(k1.to_map() if k1 else None)

        if self.auth_error_message is not None:
            result['AuthErrorMessage'] = self.auth_error_message

        if self.id is not None:
            result['Id'] = self.id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Applicator') is not None:
            self.applicator = m.get('Applicator')

        if m.get('ApplicatorName') is not None:
            self.applicator_name = m.get('ApplicatorName')

        if m.get('ApprovalProcessDefinition') is not None:
            temp_model = main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinition()
            self.approval_process_definition = temp_model.from_map(m.get('ApprovalProcessDefinition'))

        self.approval_tasks = []
        if m.get('ApprovalTasks') is not None:
            for k1 in m.get('ApprovalTasks'):
                temp_model = main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalTasks()
                self.approval_tasks.append(temp_model.from_map(k1))

        if m.get('AuthErrorMessage') is not None:
            self.auth_error_message = m.get('AuthErrorMessage')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetProcessInstanceResponseBodyProcessInstanceApprovalTasks(DaraModel):
    def __init__(
        self,
        approval_comment: str = None,
        approval_decision: str = None,
        approval_node: main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalTasksApprovalNode = None,
        assignee: str = None,
        assignee_name: str = None,
        complete_time: int = None,
        create_time: int = None,
        id: str = None,
        status: str = None,
        task_candidates: List[main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalTasksTaskCandidates] = None,
    ):
        # The approval comment.
        self.approval_comment = approval_comment
        # The approval decision. Valid values:
        # 
        # - `Agree`
        # 
        # - `Deny`
        self.approval_decision = approval_decision
        # The approval node from the corresponding approval policy.
        self.approval_node = approval_node
        # The user ID of the actual approver.
        self.assignee = assignee
        # The name of the actual approver.
        self.assignee_name = assignee_name
        # The time when the task was completed.
        self.complete_time = complete_time
        # The time when the task was created.
        self.create_time = create_time
        # The approval task ID.
        self.id = id
        # The status of the task. Valid values:
        # 
        # - `Completed`: The task is complete.
        # 
        # - `Pending`: The task is pending.
        # 
        # - `Aborted`: The task is aborted.
        self.status = status
        # The candidate approvers for the task.
        self.task_candidates = task_candidates

    def validate(self):
        if self.approval_node:
            self.approval_node.validate()
        if self.task_candidates:
            for v1 in self.task_candidates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_comment is not None:
            result['ApprovalComment'] = self.approval_comment

        if self.approval_decision is not None:
            result['ApprovalDecision'] = self.approval_decision

        if self.approval_node is not None:
            result['ApprovalNode'] = self.approval_node.to_map()

        if self.assignee is not None:
            result['Assignee'] = self.assignee

        if self.assignee_name is not None:
            result['AssigneeName'] = self.assignee_name

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        result['TaskCandidates'] = []
        if self.task_candidates is not None:
            for k1 in self.task_candidates:
                result['TaskCandidates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalComment') is not None:
            self.approval_comment = m.get('ApprovalComment')

        if m.get('ApprovalDecision') is not None:
            self.approval_decision = m.get('ApprovalDecision')

        if m.get('ApprovalNode') is not None:
            temp_model = main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalTasksApprovalNode()
            self.approval_node = temp_model.from_map(m.get('ApprovalNode'))

        if m.get('Assignee') is not None:
            self.assignee = m.get('Assignee')

        if m.get('AssigneeName') is not None:
            self.assignee_name = m.get('AssigneeName')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.task_candidates = []
        if m.get('TaskCandidates') is not None:
            for k1 in m.get('TaskCandidates'):
                temp_model = main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalTasksTaskCandidates()
                self.task_candidates.append(temp_model.from_map(k1))

        return self

class GetProcessInstanceResponseBodyProcessInstanceApprovalTasksTaskCandidates(DaraModel):
    def __init__(
        self,
        member_name: str = None,
        member_user_id: str = None,
    ):
        # The name of the approver.
        self.member_name = member_name
        # The user ID of the approver.
        self.member_user_id = member_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.member_user_id is not None:
            result['MemberUserId'] = self.member_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('MemberUserId') is not None:
            self.member_user_id = m.get('MemberUserId')

        return self

class GetProcessInstanceResponseBodyProcessInstanceApprovalTasksApprovalNode(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        assignees: List[str] = None,
        id: str = None,
        name: str = None,
    ):
        # The type of the approver for the node. Valid values:
        # 
        # - `DataWorksProjectRole`: A workspace role
        # 
        # - `DataWorksProjectMember`: A workspace member
        # 
        # - `TableAdministrator`: A table administrator
        # 
        # - `TableOrProjectAdministrator`: A table or workspace administrator
        # 
        # - `AliyunResourceOwner`: An Alibaba Cloud account
        # 
        # - `MaxComputeRole`: A MaxCompute role
        # 
        # - `DLFAdmin`: A DlfLegacy administrator
        # 
        # - `DLFNextAdmin`: A DLFNext administrator
        # 
        # - `TenantRole`: A tenant role
        # 
        # - `EmrAdministrator`: An Emr administrator
        # 
        # - `LindormAdministrator`: A Lindorm administrator
        # 
        # - `AliyunRamUser`: A RAM user
        self.account_type = account_type
        # The specified approvers.
        # 
        # The contents of this parameter depend on the `AccountType` value:
        # 
        # - If `AccountType` is `DataWorksProjectMember`, this parameter contains the user IDs of workspace members.
        # 
        # - If `AccountType` is `DataWorksProjectRole`, this parameter contains the codes of workspace roles.
        # 
        # - If `AccountType` is `MaxComputeRole`, this parameter contains the MaxCompute roles.
        # 
        # - If `AccountType` is `TenantRole`, this parameter contains the codes of tenant roles.
        # 
        # - If `AccountType` is `AliyunRamUser`, this parameter contains the user IDs of RAM users.
        self.assignees = assignees
        # The node ID.
        self.id = id
        # The node name.
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

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinition(DaraModel):
    def __init__(
        self,
        approval_nodes: List[main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinitionApprovalNodes] = None,
        description: str = None,
        enabled: bool = None,
        id: str = None,
        name: str = None,
        notification_services: List[main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinitionNotificationServices] = None,
        rule_conditions: List[main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinitionRuleConditions] = None,
        sub_type: str = None,
        type: str = None,
    ):
        # The approval nodes.
        self.approval_nodes = approval_nodes
        # The description of the approval policy.
        self.description = description
        # Indicates whether the policy is enabled.
        self.enabled = enabled
        # The approval policy ID.
        self.id = id
        # The name of the approval policy.
        self.name = name
        # The notification services.
        self.notification_services = notification_services
        # The rules that determine when the approval policy takes effect.
        self.rule_conditions = rule_conditions
        # The subtype of the approval policy. Valid values:
        # 
        # - `Table`
        # 
        # - `Column`
        # 
        # - `Database`
        # 
        # - `Schema`
        # 
        # - `Default`
        self.sub_type = sub_type
        # The type of the approval policy. Valid values:
        # 
        # - `MaxCompute`
        # 
        # - `DataService`
        # 
        # - `DlfV1` (Custom creation is not supported)
        # 
        # - `Extension`
        # 
        # - `Hologres`
        # 
        # - `Emr` (Custom creation is not supported)
        # 
        # - `DataAssetGovernance` (Custom creation is not supported)
        # 
        # - `Lindorm` (Custom creation is not supported)
        # 
        # - `StarRocks` (Custom creation is not supported)
        # 
        # - `DlfNext` (Custom creation is not supported)
        # 
        # - `DataWorks` (Custom creation is not supported)
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
                temp_model = main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinitionApprovalNodes()
                self.approval_nodes.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.notification_services = []
        if m.get('NotificationServices') is not None:
            for k1 in m.get('NotificationServices'):
                temp_model = main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinitionNotificationServices()
                self.notification_services.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinitionRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinitionRuleConditions(DaraModel):
    def __init__(
        self,
        expression: str = None,
        scope: str = None,
        type: str = None,
    ):
        # The expression of the rule condition. Format: `((#type==\\"typeValue\\"))`.
        self.expression = expression
        # The rule scope. Valid values:
        # 
        # - `Deployment`: Determines whether the policy applies when a request is submitted.
        # 
        # - `Running`: Determines whether to skip approval while the process instance runs. This value is supported only for MaxCompute approval policies.
        self.scope = scope
        # The type of the rule condition. Valid values:
        # 
        # - `odpsProject`: Applies to a specific MaxCompute project.
        # 
        # - `hologresInstanceId`: Applies to a specific Hologres instance.
        # 
        # - `sensibleLevel`: Applies to a specific security level.
        # 
        # - `tableGuid`: Applies to a specific table.
        # 
        # - `projectId`: Applies to a specific workspace.
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

class GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinitionNotificationServices(DaraModel):
    def __init__(
        self,
        channel: str = None,
        extension: str = None,
        receiver: str = None,
    ):
        # The notification channel. Valid values:
        # 
        # - `Mail`
        # 
        # - `Sms`
        # 
        # - `DingRobot`
        # 
        # - `Weixin`
        self.channel = channel
        # Additional information in JSON format. For example, `{"atAll":"true"}` indicates whether to @all members.
        self.extension = extension
        # If `Channel` is set to `DingRobot` or `Weixin`, the value of this parameter must be the webhook URL.
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

class GetProcessInstanceResponseBodyProcessInstanceApprovalProcessDefinitionApprovalNodes(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        assignees: List[str] = None,
        extension_properties: str = None,
        id: str = None,
        name: str = None,
    ):
        # The type of the approver for the node. Valid values:
        # 
        # - `DataWorksProjectRole`: A workspace role
        # 
        # - `DataWorksProjectMember`: A workspace member
        # 
        # - `TableAdministrator`: A table administrator
        # 
        # - `TableOrProjectAdministrator`: A table or workspace administrator
        # 
        # - `AliyunResourceOwner`: An Alibaba Cloud account
        # 
        # - `MaxComputeRole`: A MaxCompute role
        # 
        # - `DLFAdmin`: A DlfLegacy administrator
        # 
        # - `DLFNextAdmin`: A DLFNext administrator
        # 
        # - `TenantRole`: A tenant role
        # 
        # - `EmrAdministrator`: An Emr administrator
        # 
        # - `LindormAdministrator`: A Lindorm administrator
        # 
        # - `AliyunRamUser`: A RAM user
        self.account_type = account_type
        # The specified approvers.
        # 
        # The contents of this parameter depend on the `AccountType` value:
        # 
        # - If `AccountType` is `DataWorksProjectMember`, this parameter contains the user IDs of workspace members.
        # 
        # - If `AccountType` is `DataWorksProjectRole`, this parameter contains the codes of workspace roles.
        # 
        # - If `AccountType` is `MaxComputeRole`, this parameter contains the MaxCompute roles.
        # 
        # - If `AccountType` is `TenantRole`, this parameter contains the codes of tenant roles.
        # 
        # - If `AccountType` is `AliyunRamUser`, this parameter contains the user IDs of RAM users.
        self.assignees = assignees
        # The extended description of the approval node.
        self.extension_properties = extension_properties
        # The node ID.
        self.id = id
        # The node name.
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

