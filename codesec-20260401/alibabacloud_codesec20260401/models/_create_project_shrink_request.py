# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProjectShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        engines_shrink: str = None,
        instruction_prompt: str = None,
        name: str = None,
        source_shrink: str = None,
    ):
        # The description.
        self.description = description
        # The engine switches for the project or scan snapshot. Only SAST and SCA are supported.
        self.engines_shrink = engines_shrink
        # The natural language prompt that describes scanning or result processing preferences, such as ignoring low-risk vulnerabilities.
        self.instruction_prompt = instruction_prompt
        # The project name.
        # 
        # This parameter is required.
        self.name = name
        # The project source.
        self.source_shrink = source_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.engines_shrink is not None:
            result['engines'] = self.engines_shrink

        if self.instruction_prompt is not None:
            result['instructionPrompt'] = self.instruction_prompt

        if self.name is not None:
            result['name'] = self.name

        if self.source_shrink is not None:
            result['source'] = self.source_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('engines') is not None:
            self.engines_shrink = m.get('engines')

        if m.get('instructionPrompt') is not None:
            self.instruction_prompt = m.get('instructionPrompt')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source_shrink = m.get('source')

        return self

