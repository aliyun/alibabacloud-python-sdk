# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLgfShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        instance_id: str = None,
        lgf_definition_shrink: str = None,
        lgf_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.lgf_definition_shrink = lgf_definition_shrink
        # LGF ID
        # 
        # This parameter is required.
        self.lgf_id = lgf_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lgf_definition_shrink is not None:
            result['LgfDefinition'] = self.lgf_definition_shrink

        if self.lgf_id is not None:
            result['LgfId'] = self.lgf_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LgfDefinition') is not None:
            self.lgf_definition_shrink = m.get('LgfDefinition')

        if m.get('LgfId') is not None:
            self.lgf_id = m.get('LgfId')

        return self

