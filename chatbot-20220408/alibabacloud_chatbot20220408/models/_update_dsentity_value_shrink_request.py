# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDSEntityValueShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        entity_id: int = None,
        entity_value_id: int = None,
        instance_id: str = None,
        synonyms_shrink: str = None,
    ):
        # The business space key. If this parameter is not set, the default business space is accessed. Obtain the key value from the business management page of the main account.
        self.agent_key = agent_key
        # When the entity type is synonyms, this parameter specifies the normalized value of the entity. When the entity type is regex, this parameter specifies the regular expression text.
        # 
        # This parameter is required.
        self.content = content
        # The entity ID. This parameter can be left empty when you modify an entity member.
        # 
        # This parameter is required.
        self.entity_id = entity_id
        # The entity member ID. This parameter is left empty when you create an entity member.
        # 
        # This parameter is required.
        self.entity_value_id = entity_value_id
        # The chatbot ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The list of synonyms.
        self.synonyms_shrink = synonyms_shrink

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

        if self.synonyms_shrink is not None:
            result['Synonyms'] = self.synonyms_shrink

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
            self.synonyms_shrink = m.get('Synonyms')

        return self

