# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class VideoInsightsCaptionConfig(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        person_reference: main_models.PersonReferenceConfig = None,
        prompt: str = None,
    ):
        self.enable = enable
        self.person_reference = person_reference
        self.prompt = prompt

    def validate(self):
        if self.person_reference:
            self.person_reference.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.person_reference is not None:
            result['PersonReference'] = self.person_reference.to_map()

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('PersonReference') is not None:
            temp_model = main_models.PersonReferenceConfig()
            self.person_reference = temp_model.from_map(m.get('PersonReference'))

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        return self

