# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgentShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        metadata_shrink: str = None,
        name: str = None,
        prompt: str = None,
    ):
        # The description of the event bus.
        self.description = description
        # The associated metadata.
        self.metadata_shrink = metadata_shrink
        # The name of the agent.
        # 
        # This parameter is required.
        self.name = name
        # You are an IoT data analytics assistant...
        self.prompt = prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.metadata_shrink is not None:
            result['Metadata'] = self.metadata_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Metadata') is not None:
            self.metadata_shrink = m.get('Metadata')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        return self

