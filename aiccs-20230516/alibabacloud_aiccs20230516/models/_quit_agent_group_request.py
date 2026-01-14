# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QuitAgentGroupRequest(DaraModel):
    def __init__(
        self,
        agent_group_id: int = None,
        agent_ids: List[int] = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 坐席组ID
        # 
        # This parameter is required.
        self.agent_group_id = agent_group_id
        # 坐席ID列表
        # 
        # This parameter is required.
        self.agent_ids = agent_ids
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_group_id is not None:
            result['AgentGroupId'] = self.agent_group_id

        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentGroupId') is not None:
            self.agent_group_id = m.get('AgentGroupId')

        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

