# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchCreateModelItemDTO(DaraModel):
    def __init__(
        self,
        description: str = None,
        extensions: str = None,
        in_out: str = None,
        max_input_length: str = None,
        max_output_length: str = None,
        model_id: str = None,
        model_type: str = None,
        name: str = None,
        tags: str = None,
    ):
        self.description = description
        self.extensions = extensions
        self.in_out = in_out
        self.max_input_length = max_input_length
        self.max_output_length = max_output_length
        # This parameter is required.
        self.model_id = model_id
        # This parameter is required.
        self.model_type = model_type
        # This parameter is required.
        self.name = name
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.extensions is not None:
            result['extensions'] = self.extensions

        if self.in_out is not None:
            result['inOut'] = self.in_out

        if self.max_input_length is not None:
            result['maxInputLength'] = self.max_input_length

        if self.max_output_length is not None:
            result['maxOutputLength'] = self.max_output_length

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.name is not None:
            result['name'] = self.name

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('extensions') is not None:
            self.extensions = m.get('extensions')

        if m.get('inOut') is not None:
            self.in_out = m.get('inOut')

        if m.get('maxInputLength') is not None:
            self.max_input_length = m.get('maxInputLength')

        if m.get('maxOutputLength') is not None:
            self.max_output_length = m.get('maxOutputLength')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

