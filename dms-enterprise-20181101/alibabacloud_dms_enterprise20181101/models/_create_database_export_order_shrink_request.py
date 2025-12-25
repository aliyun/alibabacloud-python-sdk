# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatabaseExportOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        parent_id: int = None,
        plugin_param_shrink: str = None,
        related_user_list_shrink: str = None,
        tid: int = None,
    ):
        # The key of the attachment that provides more instructions for the ticket. You can call the [GetUserUploadFileJob](https://help.aliyun.com/document_detail/206069.html) operation to obtain the attachment key.
        self.attachment_key = attachment_key
        # The purpose or objective of the ticket. This parameter helps reduce unnecessary communication.
        # 
        # This parameter is required.
        self.comment = comment
        # The ID of the parent ticket.
        self.parent_id = parent_id
        # The parameters of the ticket.
        # 
        # This parameter is required.
        self.plugin_param_shrink = plugin_param_shrink
        # The stakeholders involved in this operation.
        self.related_user_list_shrink = related_user_list_shrink
        # The tenant ID.
        # 
        # > To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the DMS console. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
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

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.plugin_param_shrink is not None:
            result['PluginParam'] = self.plugin_param_shrink

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

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('PluginParam') is not None:
            self.plugin_param_shrink = m.get('PluginParam')

        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

