# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class BeginSessionResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        id: str = None,
        event: str = None,
        body: main_models.BeginSessionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.id = id
        self.event = event
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        if self.id is not None:
            result['id'] = self.id

        if self.event is not None:
            result['event'] = self.event

        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('body') is not None:
            temp_model = main_models.BeginSessionResponseBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

