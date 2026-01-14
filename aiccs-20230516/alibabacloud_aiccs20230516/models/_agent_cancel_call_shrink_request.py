# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgentCancelCallShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_id: int = None,
        agent_tag: str = None,
        numbers_shrink: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags_shrink: str = None,
    ):
        # 坐席ID
        self.agent_id = agent_id
        # 坐席标签
        self.agent_tag = agent_tag
        # 号码列表
        self.numbers_shrink = numbers_shrink
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 用户自定义标签列表
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag

        if self.numbers_shrink is not None:
            result['Numbers'] = self.numbers_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')

        if m.get('Numbers') is not None:
            self.numbers_shrink = m.get('Numbers')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

