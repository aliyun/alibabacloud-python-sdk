# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunMarketingInformationExtractRequest(DaraModel):
    def __init__(
        self,
        custom_prompt: str = None,
        extract_type: str = None,
        model_id: str = None,
        source_materials: List[str] = None,
    ):
        self.custom_prompt = custom_prompt
        self.extract_type = extract_type
        self.model_id = model_id
        self.source_materials = source_materials

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

        if self.source_materials is not None:
            result['sourceMaterials'] = self.source_materials

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
            self.source_materials = m.get('sourceMaterials')

        return self

