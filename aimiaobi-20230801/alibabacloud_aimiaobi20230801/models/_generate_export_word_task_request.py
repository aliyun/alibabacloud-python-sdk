# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateExportWordTaskRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        generated_content_id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.generated_content_id = generated_content_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.generated_content_id is not None:
            result['GeneratedContentId'] = self.generated_content_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('GeneratedContentId') is not None:
            self.generated_content_id = m.get('GeneratedContentId')

        return self

