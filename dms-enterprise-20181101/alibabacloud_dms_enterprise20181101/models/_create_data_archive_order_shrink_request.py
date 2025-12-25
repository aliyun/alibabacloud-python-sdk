# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataArchiveOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        param_shrink: str = None,
        parent_id: int = None,
        plugin_type: str = None,
        related_user_list_shrink: str = None,
        tid: int = None,
    ):
        # The description of the task.
        # 
        # This parameter is required.
        self.comment = comment
        # The parameters for archiving data.
        # 
        # This parameter is required.
        self.param_shrink = param_shrink
        # The ID of the parent ticket. A parent ticket is generated only when a child ticket is created.
        self.parent_id = parent_id
        # The type of the plug-in. Default value: DATA_ARCHIVE.
        self.plugin_type = plugin_type
        # The list of the related users.
        self.related_user_list_shrink = related_user_list_shrink
        # The tenant ID. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.param_shrink is not None:
            result['Param'] = self.param_shrink

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.related_user_list_shrink is not None:
            result['RelatedUserList'] = self.related_user_list_shrink

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

