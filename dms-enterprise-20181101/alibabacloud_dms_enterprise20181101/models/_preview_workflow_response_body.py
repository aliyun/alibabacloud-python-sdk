# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class PreviewWorkflowResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        workflow_detail: main_models.PreviewWorkflowResponseBodyWorkflowDetail = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The request ID. You can use the request ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The details of the workflow.
        self.workflow_detail = workflow_detail

    def validate(self):
        if self.workflow_detail:
            self.workflow_detail.validate()

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

        if self.workflow_detail is not None:
            result['WorkflowDetail'] = self.workflow_detail.to_map()

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

        if m.get('WorkflowDetail') is not None:
            temp_model = main_models.PreviewWorkflowResponseBodyWorkflowDetail()
            self.workflow_detail = temp_model.from_map(m.get('WorkflowDetail'))

        return self

class PreviewWorkflowResponseBodyWorkflowDetail(DaraModel):
    def __init__(
        self,
        comment: str = None,
        wf_cate_name: str = None,
        workflow_node_list: main_models.PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeList = None,
    ):
        # The remarks of the approval template.
        self.comment = comment
        # The name of the approval template.
        self.wf_cate_name = wf_cate_name
        # The approval nodes.
        self.workflow_node_list = workflow_node_list

    def validate(self):
        if self.workflow_node_list:
            self.workflow_node_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.wf_cate_name is not None:
            result['WfCateName'] = self.wf_cate_name

        if self.workflow_node_list is not None:
            result['WorkflowNodeList'] = self.workflow_node_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('WfCateName') is not None:
            self.wf_cate_name = m.get('WfCateName')

        if m.get('WorkflowNodeList') is not None:
            temp_model = main_models.PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeList()
            self.workflow_node_list = temp_model.from_map(m.get('WorkflowNodeList'))

        return self

class PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeList(DaraModel):
    def __init__(
        self,
        workflow_node: List[main_models.PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeListWorkflowNode] = None,
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
                temp_model = main_models.PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeListWorkflowNode()
                self.workflow_node.append(temp_model.from_map(k1))

        return self

class PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeListWorkflowNode(DaraModel):
    def __init__(
        self,
        audit_user_list: main_models.PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeListWorkflowNodeAuditUserList = None,
        comment: str = None,
        node_name: str = None,
        node_type: str = None,
    ):
        # The approvers.
        self.audit_user_list = audit_user_list
        # The remarks of the approval node.
        self.comment = comment
        # The name of the approval node.
        self.node_name = node_name
        # The type of the approval node.
        # 
        # Valid values:
        # 
        # *   USER_LIST: The approval node is created by a user.
        # *   UNKNOWN: The source of the approval node is unknown.
        # *   SYS: The approval node is predefined by the system.
        self.node_type = node_type

    def validate(self):
        if self.audit_user_list:
            self.audit_user_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_user_list is not None:
            result['AuditUserList'] = self.audit_user_list.to_map()

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditUserList') is not None:
            temp_model = main_models.PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeListWorkflowNodeAuditUserList()
            self.audit_user_list = temp_model.from_map(m.get('AuditUserList'))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

class PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeListWorkflowNodeAuditUserList(DaraModel):
    def __init__(
        self,
        audit_user: List[main_models.PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeListWorkflowNodeAuditUserListAuditUser] = None,
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
                temp_model = main_models.PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeListWorkflowNodeAuditUserListAuditUser()
                self.audit_user.append(temp_model.from_map(k1))

        return self

class PreviewWorkflowResponseBodyWorkflowDetailWorkflowNodeListWorkflowNodeAuditUserListAuditUser(DaraModel):
    def __init__(
        self,
        nick_name: str = None,
        real_name: str = None,
        user_id: int = None,
    ):
        # The nickname of the approver.
        self.nick_name = nick_name
        # The name of the approver.
        self.real_name = real_name
        # The ID of the approver.
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

