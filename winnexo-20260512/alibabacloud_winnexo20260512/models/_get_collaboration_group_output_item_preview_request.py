# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCollaborationGroupOutputItemPreviewRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        item_id: str = None,
        tenant_id: str = None,
    ):
        # 协作空间ID，必填，长度1至64。调用者必须是该租户下该空间的有效成员。可从ListCollaborationGroups返回的items中获取。
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 对话生成文件的产出明细ID。取GetNodeDetail返回的artifacts中ref.kind为USER_OUTPUT_ITEM的ref.id；不是artifactId。
        # 
        # This parameter is required.
        self.item_id = item_id
        # 业务租户ID，可选。必须属于当前调用身份的可访问租户；无权访问时拒绝请求。未传时按现有鉴权规则解析租户，多租户用户无法唯一确定时需显式指定。
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

