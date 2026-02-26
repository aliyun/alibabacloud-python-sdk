# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class OCRContents(DaraModel):
    def __init__(
        self,
        boundary: main_models.Boundary = None,
        confidence: float = None,
        contents: str = None,
        language: str = None,
    ):
        # The boundary information.
        self.boundary = boundary
        # The confidence level of the content. Valid values: 0 to 1. The value 0 indicates the lowest confidence level. The value 1 indicates the highest confidence level.
        self.confidence = confidence
        # The content.
        self.contents = contents
        # The BCP 47 language code. This parameter is not supported in the current version.
        self.language = language

    def validate(self):
        if self.boundary:
            self.boundary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boundary is not None:
            result['Boundary'] = self.boundary.to_map()

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.contents is not None:
            result['Contents'] = self.contents

        if self.language is not None:
            result['Language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Boundary') is not None:
            temp_model = main_models.Boundary()
            self.boundary = temp_model.from_map(m.get('Boundary'))

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Contents') is not None:
            self.contents = m.get('Contents')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        return self

