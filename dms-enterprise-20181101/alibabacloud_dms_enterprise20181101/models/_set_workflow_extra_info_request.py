# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetWorkflowExtraInfoRequest(DaraModel):
    def __init__(
        self,
        render_add_approval_node: bool = None,
        render_agree: bool = None,
        render_cancel: bool = None,
        render_reject: bool = None,
        render_transfer: bool = None,
        thirdparty_workflow_comment: str = None,
        thirdparty_workflow_url: str = None,
        tid: int = None,
        workflow_instance_id: int = None,
    ):
        # Specifies whether the Sign button is displayed in the ticket approval section of the DMS console for a third-party approval workflow. Valid values:
        # 
        # *   **true** (default): The Sign button is displayed.
        # *   **false**: The Sign button is not displayed.
        self.render_add_approval_node = render_add_approval_node
        # Specifies whether the Agree button is displayed in the ticket approval section of the DMS console for a third-party approval workflow. Valid values:
        # 
        # *   **true** (default): The Agree button is displayed.
        # *   **false**: The Agree button is not displayed.
        self.render_agree = render_agree
        # Specifies whether the Revoke button is displayed in the ticket approval section of the DMS console for a third-party approval workflow. Valid values:
        # 
        # *   **true** (default): The Revoke button is displayed.
        # *   **false**: The Revoke button is not displayed.
        self.render_cancel = render_cancel
        # Specifies whether the Reject button is displayed in the ticket approval section of the DMS console for a third-party approval workflow. Valid values:
        # 
        # *   **true** (default): The Reject button is displayed.
        # *   **false**: The Reject button is not displayed.
        self.render_reject = render_reject
        # Specifies whether the Forward button is displayed in the ticket approval section of the DMS console for a third-party approval workflow. Valid values:
        # 
        # *   **true** (default): The Forward button is displayed.
        # *   **false**: The Forward button is not displayed.
        self.render_transfer = render_transfer
        # The remarks of approval workflow for third parties.
        self.thirdparty_workflow_comment = thirdparty_workflow_comment
        # The link of approval workflow for third parties.
        self.thirdparty_workflow_url = thirdparty_workflow_url
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, go to the DMS console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid
        # The ID of the approval workflow. You can call the [GetOrderBaseInfo](https://help.aliyun.com/document_detail/144642.html) operation to query the ID of the approval workflow.
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
        if self.render_add_approval_node is not None:
            result['RenderAddApprovalNode'] = self.render_add_approval_node

        if self.render_agree is not None:
            result['RenderAgree'] = self.render_agree

        if self.render_cancel is not None:
            result['RenderCancel'] = self.render_cancel

        if self.render_reject is not None:
            result['RenderReject'] = self.render_reject

        if self.render_transfer is not None:
            result['RenderTransfer'] = self.render_transfer

        if self.thirdparty_workflow_comment is not None:
            result['ThirdpartyWorkflowComment'] = self.thirdparty_workflow_comment

        if self.thirdparty_workflow_url is not None:
            result['ThirdpartyWorkflowUrl'] = self.thirdparty_workflow_url

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderAddApprovalNode') is not None:
            self.render_add_approval_node = m.get('RenderAddApprovalNode')

        if m.get('RenderAgree') is not None:
            self.render_agree = m.get('RenderAgree')

        if m.get('RenderCancel') is not None:
            self.render_cancel = m.get('RenderCancel')

        if m.get('RenderReject') is not None:
            self.render_reject = m.get('RenderReject')

        if m.get('RenderTransfer') is not None:
            self.render_transfer = m.get('RenderTransfer')

        if m.get('ThirdpartyWorkflowComment') is not None:
            self.thirdparty_workflow_comment = m.get('ThirdpartyWorkflowComment')

        if m.get('ThirdpartyWorkflowUrl') is not None:
            self.thirdparty_workflow_url = m.get('ThirdpartyWorkflowUrl')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')

        return self

