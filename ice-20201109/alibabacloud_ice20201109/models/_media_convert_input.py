# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertInput(DaraModel):
    def __init__(
        self,
        input_file: main_models.MediaObject = None,
        name: str = None,
    ):
        self.input_file = input_file
        self.name = name

    def validate(self):
        if self.input_file:
            self.input_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_file is not None:
            result['InputFile'] = self.input_file.to_map()

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputFile') is not None:
            temp_model = main_models.MediaObject()
            self.input_file = temp_model.from_map(m.get('InputFile'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

