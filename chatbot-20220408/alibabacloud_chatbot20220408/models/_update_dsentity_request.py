# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDSEntityRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        entity_id: int = None,
        entity_name: str = None,
        entity_type: str = None,
        instance_id: str = None,
    ):
        # The business space key. If you do not specify this parameter, the system uses the default business space. You can get this key from the business management page of your Alibaba Cloud account.
        self.agent_key = agent_key
        # The ID of the entity.
        # 
        # This parameter is required.
        self.entity_id = entity_id
        # The new name for the entity. The name can contain only Chinese characters, letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.entity_name = entity_name
        # The type of the entity. This parameter cannot be modified. Valid values: `synonyms` and `regex`.
        self.entity_type = entity_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

