# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunMarketingInformationWritingShrinkRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        custom_limitation: str = None,
        custom_prompt: str = None,
        ext_parameters_shrink: str = None,
        generate_count: str = None,
        input_example: str = None,
        keywords: str = None,
        language: str = None,
        model_id: str = None,
        other_requirements: str = None,
        output_example: str = None,
        prompt: str = None,
        source_material: str = None,
        word_count_range: str = None,
        writing_type: str = None,
    ):
        self.api_key = api_key
        self.custom_limitation = custom_limitation
        self.custom_prompt = custom_prompt
        self.ext_parameters_shrink = ext_parameters_shrink
        self.generate_count = generate_count
        self.input_example = input_example
        self.keywords = keywords
        self.language = language
        self.model_id = model_id
        self.other_requirements = other_requirements
        self.output_example = output_example
        self.prompt = prompt
        self.source_material = source_material
        self.word_count_range = word_count_range
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

        if self.ext_parameters_shrink is not None:
            result['extParameters'] = self.ext_parameters_shrink

        if self.generate_count is not None:
            result['generateCount'] = self.generate_count

        if self.input_example is not None:
            result['inputExample'] = self.input_example

        if self.keywords is not None:
            result['keywords'] = self.keywords

        if self.language is not None:
            result['language'] = self.language

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.other_requirements is not None:
            result['otherRequirements'] = self.other_requirements

        if self.output_example is not None:
            result['outputExample'] = self.output_example

        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.source_material is not None:
            result['sourceMaterial'] = self.source_material

        if self.word_count_range is not None:
            result['wordCountRange'] = self.word_count_range

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

        if m.get('extParameters') is not None:
            self.ext_parameters_shrink = m.get('extParameters')

        if m.get('generateCount') is not None:
            self.generate_count = m.get('generateCount')

        if m.get('inputExample') is not None:
            self.input_example = m.get('inputExample')

        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('otherRequirements') is not None:
            self.other_requirements = m.get('otherRequirements')

        if m.get('outputExample') is not None:
            self.output_example = m.get('outputExample')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('sourceMaterial') is not None:
            self.source_material = m.get('sourceMaterial')

        if m.get('wordCountRange') is not None:
            self.word_count_range = m.get('wordCountRange')

        if m.get('writingType') is not None:
            self.writing_type = m.get('writingType')

        return self

