# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListWorkFlowNodesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        workflow_nodes: main_models.ListWorkFlowNodesResponseBodyWorkflowNodes = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The details of approval nodes.
        self.workflow_nodes = workflow_nodes

    def validate(self):
        if self.workflow_nodes:
            self.workflow_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('WorkflowNodes') is not None:
            temp_model = main_models.ListWorkFlowNodesResponseBodyWorkflowNodes()
            self.workflow_nodes = temp_model.from_map(m.get('WorkflowNodes'))

        return self

class ListWorkFlowNodesResponseBodyWorkflowNodes(DaraModel):
    def __init__(
        self,
        workflow_node: List[main_models.ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNode] = None,
    ):
        self.workflow_node = workflow_node

    def validate(self):
        if self.workflow_node:
            for v1 in self.workflow_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WorkflowNode'] = []
        if self.workflow_node is not None:
            for k1 in self.workflow_node:
                result['WorkflowNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.workflow_node = []
        if m.get('WorkflowNode') is not None:
            for k1 in m.get('WorkflowNode'):
                temp_model = main_models.ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNode()
                self.workflow_node.append(temp_model.from_map(k1))

        return self

class ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNode(DaraModel):
    def __init__(
        self,
        audit_users: main_models.ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsers = None,
        comment: str = None,
        create_user_id: int = None,
        create_user_nick_name: str = None,
        node_id: int = None,
        node_name: str = None,
        node_type: str = None,
    ):
        # The details about approvers.
        self.audit_users = audit_users
        # The description of the approval template.
        self.comment = comment
        # The ID of the creator. This ID is different from the ID of the Alibaba Cloud account of the creator.
        self.create_user_id = create_user_id
        # The name of the user who creates the approval node.
        self.create_user_nick_name = create_user_nick_name
        # The ID of the approval node.
        self.node_id = node_id
        # The name of the approval node.
        self.node_name = node_name
        # The type of the approval node. Valid values:
        # 
        # *   SYS: The approval node is predefined by the system.
        # *   USER_LIST: The approval node is created by a user.
        self.node_type = node_type

    def validate(self):
        if self.audit_users:
            self.audit_users.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_users is not None:
            result['AuditUsers'] = self.audit_users.to_map()

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.create_user_nick_name is not None:
            result['CreateUserNickName'] = self.create_user_nick_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditUsers') is not None:
            temp_model = main_models.ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsers()
            self.audit_users = temp_model.from_map(m.get('AuditUsers'))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CreateUserNickName') is not None:
            self.create_user_nick_name = m.get('CreateUserNickName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

class ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsers(DaraModel):
    def __init__(
        self,
        audit_user: List[main_models.ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsersAuditUser] = None,
    ):
        self.audit_user = audit_user

    def validate(self):
        if self.audit_user:
            for v1 in self.audit_user:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuditUser'] = []
        if self.audit_user is not None:
            for k1 in self.audit_user:
                result['AuditUser'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audit_user = []
        if m.get('AuditUser') is not None:
            for k1 in m.get('AuditUser'):
                temp_model = main_models.ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsersAuditUser()
                self.audit_user.append(temp_model.from_map(k1))

        return self

class ListWorkFlowNodesResponseBodyWorkflowNodesWorkflowNodeAuditUsersAuditUser(DaraModel):
    def __init__(
        self,
        nick_name: str = None,
        real_name: str = None,
        user_id: int = None,
    ):
        # The nickname of the approver.
        self.nick_name = nick_name
        # The real name of the approver.
        self.real_name = real_name
        # The ID of the approver. The ID is different from the ID of the Alibaba Cloud account of the approver.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.real_name is not None:
            result['RealName'] = self.real_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

