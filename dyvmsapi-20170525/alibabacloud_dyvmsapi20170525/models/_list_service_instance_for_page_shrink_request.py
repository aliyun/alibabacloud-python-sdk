# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceInstanceForPageShrinkRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        owner_id: int = None,
        pager_shrink: str = None,
        relation_number: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scene_id: int = None,
        usage_id: int = None,
    ):
        # 服务实例号
        self.code = code
        self.owner_id = owner_id
        self.pager_shrink = pager_shrink
        # 关联实体号码
        self.relation_number = relation_number
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 场景ID
        self.scene_id = scene_id
        # 用途ID
        self.usage_id = usage_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pager_shrink is not None:
            result['Pager'] = self.pager_shrink

        if self.relation_number is not None:
            result['RelationNumber'] = self.relation_number

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.usage_id is not None:
            result['UsageId'] = self.usage_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Pager') is not None:
            self.pager_shrink = m.get('Pager')

        if m.get('RelationNumber') is not None:
            self.relation_number = m.get('RelationNumber')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('UsageId') is not None:
            self.usage_id = m.get('UsageId')

        return self

