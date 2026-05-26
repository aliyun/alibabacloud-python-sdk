# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class VideoInsightsCaptionConfig(DaraModel):
    def __init__(
        self,
        person_reference: main_models.PersonReferenceConfig = None,
    ):
        self.person_reference = person_reference

    def validate(self):
        if self.person_reference:
            self.person_reference.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.person_reference is not None:
            result['PersonReference'] = self.person_reference.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PersonReference') is not None:
            temp_model = main_models.PersonReferenceConfig()
            self.person_reference = temp_model.from_map(m.get('PersonReference'))

        return self

