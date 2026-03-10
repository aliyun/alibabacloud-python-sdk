# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CustomExtractionStrategy(DaraModel):
    def __init__(
        self,
        description: str = None,
        extraction_prompt: str = None,
        strategy_name: str = None,
        strategy_type: str = None,
        update_prompt: str = None,
    ):
        self.description = description
        self.extraction_prompt = extraction_prompt
        self.strategy_name = strategy_name
        self.strategy_type = strategy_type
        self.update_prompt = update_prompt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.extraction_prompt is not None:
            result['extractionPrompt'] = self.extraction_prompt

        if self.strategy_name is not None:
            result['strategyName'] = self.strategy_name

        if self.strategy_type is not None:
            result['strategyType'] = self.strategy_type

        if self.update_prompt is not None:
            result['updatePrompt'] = self.update_prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('extractionPrompt') is not None:
            self.extraction_prompt = m.get('extractionPrompt')

        if m.get('strategyName') is not None:
            self.strategy_name = m.get('strategyName')

        if m.get('strategyType') is not None:
            self.strategy_type = m.get('strategyType')

        if m.get('updatePrompt') is not None:
            self.update_prompt = m.get('updatePrompt')

        return self

