# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataCronClearOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param_shrink: str = None,
        related_user_list_shrink: str = None,
        tid: int = None,
    ):
        # The key of the attachment for the ticket. The attachment provides more instructions for this operation.
        # 
        # You can call the [GetUserUploadFileJob](https://help.aliyun.com/document_detail/206069.html) operation to query the key of the attachment.
        self.attachment_key = attachment_key
        # The purpose or objective of the data change. This reduces unnecessary communication.
        # 
        # This parameter is required.
        self.comment = comment
        # The parameters of the ticket.
        # 
        # This parameter is required.
        self.param_shrink = param_shrink
        # The stakeholders of this operation. All stakeholders can view the ticket details and assist in the approval process. Irrelevant users other than Data Management (DMS) administrators and database administrators (DBAs) are not allowed to view the ticket details.
        self.related_user_list_shrink = related_user_list_shrink
        # The ID of the tenant.
        # 
        # >  The ID of the tenant is displayed when you move the pointer over the profile picture in the upper-right corner of the DMS console. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the Manage DMS tenants topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.param_shrink is not None:
            result['Param'] = self.param_shrink

        if self.related_user_list_shrink is not None:
            result['RelatedUserList'] = self.related_user_list_shrink

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')

        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

