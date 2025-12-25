# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        plugin_param_shrink: str = None,
        plugin_type: str = None,
        related_user_list: str = None,
        tid: int = None,
    ):
        # The key of an attachment that is returned after the attachment is uploaded. You can call the [GetUserUploadFileJob](https://help.aliyun.com/document_detail/206069.html) operation to query the key of the attachment.
        self.attachment_key = attachment_key
        # The description of the ticket to be created.
        # 
        # This parameter is required.
        self.comment = comment
        # The ticket creation parameter. The value is a JSON string. The value of this parameter differs based on the type of the ticket. For more information, see the **PluginParam parameter** section in this topic.
        # 
        # This parameter is required.
        self.plugin_param_shrink = plugin_param_shrink
        # The type of the ticket. For more information, see [PluginType parameter](https://help.aliyun.com/document_detail/429109.html).
        # 
        # This parameter is required.
        self.plugin_type = plugin_type
        # The IDs of the stakeholders that are involved in the ticket. Separate multiple IDs with commas (,).
        self.related_user_list = related_user_list
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
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

        if self.plugin_param_shrink is not None:
            result['PluginParam'] = self.plugin_param_shrink

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('PluginParam') is not None:
            self.plugin_param_shrink = m.get('PluginParam')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

