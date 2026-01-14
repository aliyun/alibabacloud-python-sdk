# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_intelligentcreation20240313 import models as main_models
from darabonba.model import DaraModel

class TextResult(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        text: main_models.Text = None,
    ):
        self.request_id = request_id
        # This parameter is required.
        self.text = text

    def validate(self):
        if self.text:
            self.text.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.text is not None:
            result['text'] = self.text.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('text') is not None:
            temp_model = main_models.Text()
            self.text = temp_model.from_map(m.get('text'))

        return self

