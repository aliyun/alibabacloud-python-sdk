# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TogglePrimaryObjectFavoriteShrinkRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        object_ids_shrink: str = None,
        object_type: str = None,
        operating_object_name: str = None,
        tenant_id: str = None,
    ):
        # 操作：add-关注，remove-取消关注
        # 
        # This parameter is required.
        self.action = action
        # 主对象业务ID列表
        # 
        # This parameter is required.
        self.object_ids_shrink = object_ids_shrink
        # 对象类型（如 customer、project）
        # 
        # This parameter is required.
        self.object_type = object_type
        # 运营对象名称（如 customer_1）
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.object_ids_shrink is not None:
            result['objectIds'] = self.object_ids_shrink

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('objectIds') is not None:
            self.object_ids_shrink = m.get('objectIds')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

