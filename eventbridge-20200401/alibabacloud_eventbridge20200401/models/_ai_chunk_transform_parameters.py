# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AiChunkTransformParameters(DaraModel):
    def __init__(
        self,
        chunking_type: str = None,
        input_field: main_models.AiTransformField = None,
        max_overlap_size: int = None,
        max_segment_size: int = None,
        step_name: str = None,
        unpack: bool = None,
    ):
        # The chunking algorithm. Valid values: markdown_header and recursive_character.
        self.chunking_type = chunking_type
        # The text field to chunk. This operator does not use InputField.
        self.input_field = input_field
        # The chunk overlap length. Default value: 10.
        self.max_overlap_size = max_overlap_size
        # The maximum chunk length. Default value: 1000.
        self.max_segment_size = max_segment_size
        # The field name in the CloudEvent to which the output is attached. Default value: transform0.
        self.step_name = step_name
        # Specifies whether to split the output into multiple events. Default value: true.
        self.unpack = unpack

    def validate(self):
        if self.input_field:
            self.input_field.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunking_type is not None:
            result['ChunkingType'] = self.chunking_type

        if self.input_field is not None:
            result['InputField'] = self.input_field.to_map()

        if self.max_overlap_size is not None:
            result['MaxOverlapSize'] = self.max_overlap_size

        if self.max_segment_size is not None:
            result['MaxSegmentSize'] = self.max_segment_size

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.unpack is not None:
            result['Unpack'] = self.unpack

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkingType') is not None:
            self.chunking_type = m.get('ChunkingType')

        if m.get('InputField') is not None:
            temp_model = main_models.AiTransformField()
            self.input_field = temp_model.from_map(m.get('InputField'))

        if m.get('MaxOverlapSize') is not None:
            self.max_overlap_size = m.get('MaxOverlapSize')

        if m.get('MaxSegmentSize') is not None:
            self.max_segment_size = m.get('MaxSegmentSize')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('Unpack') is not None:
            self.unpack = m.get('Unpack')

        return self

