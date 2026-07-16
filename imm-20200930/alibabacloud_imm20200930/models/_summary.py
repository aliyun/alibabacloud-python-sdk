# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Summary(DaraModel):
    def __init__(
        self,
        image: main_models.Illustration = None,
        text: str = None,
    ):
        self.image = image
        self.text = text

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['Image'] = self.image.to_map()

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            temp_model = main_models.Illustration()
            self.image = temp_model.from_map(m.get('Image'))

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

