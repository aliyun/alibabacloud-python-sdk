# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class MedicalAnswerMessage(DaraModel):
    def __init__(
        self,
        content: str = None,
        meta_data: main_models.MedicalAnswerMetaData = None,
    ):
        self.content = content
        self.meta_data = meta_data

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('metaData') is not None:
            temp_model = main_models.MedicalAnswerMetaData()
            self.meta_data = temp_model.from_map(m.get('metaData'))

        return self

