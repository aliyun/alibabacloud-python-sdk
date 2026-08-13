# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConversationShrinkRequest(DaraModel):
    def __init__(
        self,
        metadata: str = None,
        object_id: str = None,
        operating_object_name_shrink: str = None,
        tenant_id: str = None,
    ):
        # 会话元数据，可含 model 等透传字段（model 需为合法抽象模型名，否则回退默认）
        self.metadata = metadata
        # 关联业务对象ID
        self.object_id = object_id
        # operatingObjectName
        self.operating_object_name_shrink = operating_object_name_shrink
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.operating_object_name_shrink is not None:
            result['operatingObjectName'] = self.operating_object_name_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name_shrink = m.get('operatingObjectName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

