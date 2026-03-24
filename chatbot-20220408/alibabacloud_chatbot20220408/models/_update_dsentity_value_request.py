# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateDSEntityValueRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        entity_id: int = None,
        entity_value_id: int = None,
        instance_id: str = None,
        synonyms: List[str] = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.entity_value_id = entity_value_id
        # This parameter is required.
        self.instance_id = instance_id
        self.synonyms = synonyms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.content is not None:
            result['Content'] = self.content

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_value_id is not None:
            result['EntityValueId'] = self.entity_value_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityValueId') is not None:
            self.entity_value_id = m.get('EntityValueId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')

        return self

