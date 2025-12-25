# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetApprovalDetailResponseBody(DaraModel):
    def __init__(
        self,
        approval_detail: main_models.GetApprovalDetailResponseBodyApprovalDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The approval details of the ticket.
        self.approval_detail = approval_detail
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        if self.approval_detail:
            self.approval_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_detail is not None:
            result['ApprovalDetail'] = self.approval_detail.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalDetail') is not None:
            temp_model = main_models.GetApprovalDetailResponseBodyApprovalDetail()
            self.approval_detail = temp_model.from_map(m.get('ApprovalDetail'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetApprovalDetailResponseBodyApprovalDetail(DaraModel):
    def __init__(
        self,
        audit_id: int = None,
        create_time: str = None,
        current_handlers: main_models.GetApprovalDetailResponseBodyApprovalDetailCurrentHandlers = None,
        description: str = None,
        order_id: int = None,
        order_type: str = None,
        reason_list: main_models.GetApprovalDetailResponseBodyApprovalDetailReasonList = None,
        template_id: int = None,
        thirdparty_workflow_comment: str = None,
        thirdparty_workflow_url: str = None,
        title: str = None,
        workflow_ins_code: str = None,
        workflow_nodes: main_models.GetApprovalDetailResponseBodyApprovalDetailWorkflowNodes = None,
    ):
        # The ID of the approval process.
        self.audit_id = audit_id
        # The time when the approval process was created.
        self.create_time = create_time
        # The information about the approver.
        self.current_handlers = current_handlers
        # The description of the approval process.
        self.description = description
        # The ID of the ticket.
        self.order_id = order_id
        # The type of the ticket. Valid values:
        # 
        # *   **NDDL**: a schema design ticket
        # *   **DATA_TRACK**: a data tracking ticket
        # *   **TABLE_SYNC**: a table synchronization ticket
        # *   **PERM_APPLY**: a permission application ticket
        # *   **DATA_EXPORT**: a data export ticket
        # *   **DATA_CORRECT**: a data change ticket
        # *   **OWNER_APPLY**: an owner role application ticket
        # *   **SENSITIVITY**: a column sensitivity level change ticket
        self.order_type = order_type
        # The reasons for the approval.
        self.reason_list = reason_list
        # The ID of the workflow template.
        self.template_id = template_id
        # Third-party approval flow remarks.
        self.thirdparty_workflow_comment = thirdparty_workflow_comment
        # The third-party approval flow link.
        self.thirdparty_workflow_url = thirdparty_workflow_url
        # The title of the approval process.
        self.title = title
        # The approval status of the ticket. Valid values:
        # 
        # *   **AUDITING**: The ticket is being reviewed.
        # *   **REJECT**: The ticket was rejected.
        # *   **CANCEL**: The ticket was revoked.
        # *   **APPROVED**: The ticket was approved.
        # 
        # > An approval process contains multiple approval nodes, and this parameter is returned for each approval node.
        self.workflow_ins_code = workflow_ins_code
        # The details of approval nodes.
        self.workflow_nodes = workflow_nodes

    def validate(self):
        if self.current_handlers:
            self.current_handlers.validate()
        if self.reason_list:
            self.reason_list.validate()
        if self.workflow_nodes:
            self.workflow_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_id is not None:
            result['AuditId'] = self.audit_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.current_handlers is not None:
            result['CurrentHandlers'] = self.current_handlers.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.reason_list is not None:
            result['ReasonList'] = self.reason_list.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.thirdparty_workflow_comment is not None:
            result['ThirdpartyWorkflowComment'] = self.thirdparty_workflow_comment

        if self.thirdparty_workflow_url is not None:
            result['ThirdpartyWorkflowUrl'] = self.thirdparty_workflow_url

        if self.title is not None:
            result['Title'] = self.title

        if self.workflow_ins_code is not None:
            result['WorkflowInsCode'] = self.workflow_ins_code

        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditId') is not None:
            self.audit_id = m.get('AuditId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CurrentHandlers') is not None:
            temp_model = main_models.GetApprovalDetailResponseBodyApprovalDetailCurrentHandlers()
            self.current_handlers = temp_model.from_map(m.get('CurrentHandlers'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ReasonList') is not None:
            temp_model = main_models.GetApprovalDetailResponseBodyApprovalDetailReasonList()
            self.reason_list = temp_model.from_map(m.get('ReasonList'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('ThirdpartyWorkflowComment') is not None:
            self.thirdparty_workflow_comment = m.get('ThirdpartyWorkflowComment')

        if m.get('ThirdpartyWorkflowUrl') is not None:
            self.thirdparty_workflow_url = m.get('ThirdpartyWorkflowUrl')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('WorkflowInsCode') is not None:
            self.workflow_ins_code = m.get('WorkflowInsCode')

        if m.get('WorkflowNodes') is not None:
            temp_model = main_models.GetApprovalDetailResponseBodyApprovalDetailWorkflowNodes()
            self.workflow_nodes = temp_model.from_map(m.get('WorkflowNodes'))

        return self

class GetApprovalDetailResponseBodyApprovalDetailWorkflowNodes(DaraModel):
    def __init__(
        self,
        workflow_node: List[main_models.GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNode] = None,
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
                temp_model = main_models.GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNode()
                self.workflow_node.append(temp_model.from_map(k1))

        return self

class GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNode(DaraModel):
    def __init__(
        self,
        audit_user_id_list: main_models.GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNodeAuditUserIdList = None,
        node_name: str = None,
        operate_comment: str = None,
        operate_time: str = None,
        operator_id: int = None,
        workflow_ins_code: str = None,
    ):
        # The IDs of the approvers.
        self.audit_user_id_list = audit_user_id_list
        # The name of the approval node.
        self.node_name = node_name
        # The remarks of the approval.
        self.operate_comment = operate_comment
        # The time when the ticket was submitted.
        self.operate_time = operate_time
        # The ID of the user who submitted the ticket.
        self.operator_id = operator_id
        # The approval status of the ticket. Valid values:
        # 
        # *   **START**: The ticket was submitted.
        # *   **ERROR**: An error occurred.
        # *   **AUDITING**: The ticket is being reviewed.
        # *   **REJECT**: The ticket was rejected.
        # *   **CANCEL**: The ticket was revoked.
        # *   **APPROVED**: The ticket was approved.
        self.workflow_ins_code = workflow_ins_code

    def validate(self):
        if self.audit_user_id_list:
            self.audit_user_id_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_user_id_list is not None:
            result['AuditUserIdList'] = self.audit_user_id_list.to_map()

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.operate_comment is not None:
            result['OperateComment'] = self.operate_comment

        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time

        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id

        if self.workflow_ins_code is not None:
            result['WorkflowInsCode'] = self.workflow_ins_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditUserIdList') is not None:
            temp_model = main_models.GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNodeAuditUserIdList()
            self.audit_user_id_list = temp_model.from_map(m.get('AuditUserIdList'))

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('OperateComment') is not None:
            self.operate_comment = m.get('OperateComment')

        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')

        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')

        if m.get('WorkflowInsCode') is not None:
            self.workflow_ins_code = m.get('WorkflowInsCode')

        return self

class GetApprovalDetailResponseBodyApprovalDetailWorkflowNodesWorkflowNodeAuditUserIdList(DaraModel):
    def __init__(
        self,
        audit_user_ids: List[str] = None,
    ):
        self.audit_user_ids = audit_user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_user_ids is not None:
            result['AuditUserIds'] = self.audit_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditUserIds') is not None:
            self.audit_user_ids = m.get('AuditUserIds')

        return self

class GetApprovalDetailResponseBodyApprovalDetailReasonList(DaraModel):
    def __init__(
        self,
        reasons: List[str] = None,
    ):
        self.reasons = reasons

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reasons is not None:
            result['Reasons'] = self.reasons

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reasons') is not None:
            self.reasons = m.get('Reasons')

        return self

class GetApprovalDetailResponseBodyApprovalDetailCurrentHandlers(DaraModel):
    def __init__(
        self,
        current_handler: List[main_models.GetApprovalDetailResponseBodyApprovalDetailCurrentHandlersCurrentHandler] = None,
    ):
        self.current_handler = current_handler

    def validate(self):
        if self.current_handler:
            for v1 in self.current_handler:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CurrentHandler'] = []
        if self.current_handler is not None:
            for k1 in self.current_handler:
                result['CurrentHandler'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.current_handler = []
        if m.get('CurrentHandler') is not None:
            for k1 in m.get('CurrentHandler'):
                temp_model = main_models.GetApprovalDetailResponseBodyApprovalDetailCurrentHandlersCurrentHandler()
                self.current_handler.append(temp_model.from_map(k1))

        return self

class GetApprovalDetailResponseBodyApprovalDetailCurrentHandlersCurrentHandler(DaraModel):
    def __init__(
        self,
        id: int = None,
        nick_name: str = None,
    ):
        # The ID of the user.
        self.id = id
        # The nickname of the user.
        self.nick_name = nick_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        return self

