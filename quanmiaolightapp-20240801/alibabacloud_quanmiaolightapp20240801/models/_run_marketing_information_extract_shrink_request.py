# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunMarketingInformationExtractShrinkRequest(DaraModel):
    def __init__(
        self,
        custom_prompt: str = None,
        extract_type: str = None,
        model_id: str = None,
        source_materials_shrink: str = None,
    ):
        self.custom_prompt = custom_prompt
        self.extract_type = extract_type
        self.model_id = model_id
        self.source_materials_shrink = source_materials_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt

        if self.extract_type is not None:
            result['extractType'] = self.extract_type

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.source_materials_shrink is not None:
            result['sourceMaterials'] = self.source_materials_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')

        if m.get('extractType') is not None:
            self.extract_type = m.get('extractType')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('sourceMaterials') is not None:
            self.source_materials_shrink = m.get('sourceMaterials')

        return self

