# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class UpdateMemoryStoreRequest(DaraModel):
    def __init__(
        self,
        custom_extraction_strategies: List[main_models.CustomExtractionStrategy] = None,
        description: str = None,
        extraction_strategies: List[str] = None,
        short_term_ttl: int = None,
    ):
        # Custom extraction strategies.
        self.custom_extraction_strategies = custom_extraction_strategies
        # Description.
        self.description = description
        # Extraction strategies. Supports "Episodic", "Summary", and "Fact".
        self.extraction_strategies = extraction_strategies
        # Short-term memory retention time.
        self.short_term_ttl = short_term_ttl

    def validate(self):
        if self.custom_extraction_strategies:
            for v1 in self.custom_extraction_strategies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['customExtractionStrategies'] = []
        if self.custom_extraction_strategies is not None:
            for k1 in self.custom_extraction_strategies:
                result['customExtractionStrategies'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.extraction_strategies is not None:
            result['extractionStrategies'] = self.extraction_strategies

        if self.short_term_ttl is not None:
            result['shortTermTtl'] = self.short_term_ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_extraction_strategies = []
        if m.get('customExtractionStrategies') is not None:
            for k1 in m.get('customExtractionStrategies'):
                temp_model = main_models.CustomExtractionStrategy()
                self.custom_extraction_strategies.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('extractionStrategies') is not None:
            self.extraction_strategies = m.get('extractionStrategies')

        if m.get('shortTermTtl') is not None:
            self.short_term_ttl = m.get('shortTermTtl')

        return self

