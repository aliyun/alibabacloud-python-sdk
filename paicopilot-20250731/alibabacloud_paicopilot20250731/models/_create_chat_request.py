# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_paicopilot20250731 import models as main_models
from darabonba.model import DaraModel

class CreateChatRequest(DaraModel):
    def __init__(
        self,
        extra_data: str = None,
        payload: Dict[str, Any] = None,
        question: main_models.ChatDetail = None,
        title: str = None,
    ):
        self.extra_data = extra_data
        self.payload = payload
        self.question = question
        self.title = title

    def validate(self):
        if self.question:
            self.question.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.question is not None:
            result['Question'] = self.question.to_map()

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        if m.get('Question') is not None:
            temp_model = main_models.ChatDetail()
            self.question = temp_model.from_map(m.get('Question'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

