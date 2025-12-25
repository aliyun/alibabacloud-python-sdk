# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApproveOrderRequest(DaraModel):
    def __init__(
        self,
        approval_node_id: int = None,
        approval_node_pos: str = None,
        approval_type: str = None,
        comment: str = None,
        new_approver: int = None,
        new_approver_list: str = None,
        old_approver: int = None,
        real_login_user_uid: str = None,
        tid: int = None,
        workflow_instance_id: int = None,
    ):
        # If ApprovalType is set to ADD_APPROVAL_NODE, you need to specify this parameter. The ID of the user that is added as the new approval node. This node must be a user-defined approval node. You can call the ListUserDefineWorkFlowNodes operation to obtain the value of this parameter.
        self.approval_node_id = approval_node_id
        # The position of the new approval node. You must specify this parameter if ApprovalType is set to ADD_APPROVAL_NODE. Valid values:
        # 
        # *   **PRE_ADD_APPROVAL_NODE**: before the current approval node.
        # *   **POST_ADD_APPROVAL_NODE**: after the current approval node.
        self.approval_node_pos = approval_node_pos
        # The action that you want to perform on the ticket. Valid values:
        # 
        # *   **AGREE**
        # *   **CANCEL**
        # *   **REJECT**
        # *   **TRANSFER**
        # *   **ADD_APPROVAL_NODE**
        # 
        # This parameter is required.
        self.approval_type = approval_type
        # The description of the ticket.
        self.comment = comment
        # The ID of the user to which the ticket is transferred. If ApprovalType is set to TRANSFER, you need to specify this parameter.
        self.new_approver = new_approver
        # >  You can specify this parameter if ApprovalType is set to TRANSFER. You need to only specify one of NewApproverList and NewApprover.
        # 
        # The IDs of the users to whom the ticket is transferred. Separate multiple IDs with commas (,).
        self.new_approver_list = new_approver_list
        # The ID of the user that transfers the ticket to another user. The default value is the ID of the current user. If the current user is an administrator or a database administrator (DBA), the user can change the value of this parameter to the ID of another user.
        self.old_approver = old_approver
        # The UID of the Alibaba Cloud account that actually calls the API.
        self.real_login_user_uid = real_login_user_uid
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to obtain the tenant ID.
        self.tid = tid
        # The ID of the approval process. You can call the [GetOrderBaseInfo](https://help.aliyun.com/document_detail/144642.html) operation to obtain the ID of the approval process.
        # 
        # This parameter is required.
        self.workflow_instance_id = workflow_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_node_id is not None:
            result['ApprovalNodeId'] = self.approval_node_id

        if self.approval_node_pos is not None:
            result['ApprovalNodePos'] = self.approval_node_pos

        if self.approval_type is not None:
            result['ApprovalType'] = self.approval_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.new_approver is not None:
            result['NewApprover'] = self.new_approver

        if self.new_approver_list is not None:
            result['NewApproverList'] = self.new_approver_list

        if self.old_approver is not None:
            result['OldApprover'] = self.old_approver

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalNodeId') is not None:
            self.approval_node_id = m.get('ApprovalNodeId')

        if m.get('ApprovalNodePos') is not None:
            self.approval_node_pos = m.get('ApprovalNodePos')

        if m.get('ApprovalType') is not None:
            self.approval_type = m.get('ApprovalType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('NewApprover') is not None:
            self.new_approver = m.get('NewApprover')

        if m.get('NewApproverList') is not None:
            self.new_approver_list = m.get('NewApproverList')

        if m.get('OldApprover') is not None:
            self.old_approver = m.get('OldApprover')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')

        return self

