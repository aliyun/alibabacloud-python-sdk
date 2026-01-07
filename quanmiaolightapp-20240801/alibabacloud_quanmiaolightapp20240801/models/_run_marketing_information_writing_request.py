# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunMarketingInformationWritingRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        custom_limitation: str = None,
        custom_prompt: str = None,
        input_example: str = None,
        model_id: str = None,
        output_example: str = None,
        source_material: str = None,
        writing_type: str = None,
    ):
        self.api_key = api_key
        self.custom_limitation = custom_limitation
        self.custom_prompt = custom_prompt
        self.input_example = input_example
        self.model_id = model_id
        self.output_example = output_example
        self.source_material = source_material
        self.writing_type = writing_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.custom_limitation is not None:
            result['customLimitation'] = self.custom_limitation

        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt

        if self.input_example is not None:
            result['inputExample'] = self.input_example

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.output_example is not None:
            result['outputExample'] = self.output_example

        if self.source_material is not None:
            result['sourceMaterial'] = self.source_material

        if self.writing_type is not None:
            result['writingType'] = self.writing_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('customLimitation') is not None:
            self.custom_limitation = m.get('customLimitation')

        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')

        if m.get('inputExample') is not None:
            self.input_example = m.get('inputExample')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('outputExample') is not None:
            self.output_example = m.get('outputExample')

        if m.get('sourceMaterial') is not None:
            self.source_material = m.get('sourceMaterial')

        if m.get('writingType') is not None:
            self.writing_type = m.get('writingType')

        return self

