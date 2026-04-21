# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class OmniAnswerResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        id: str = None,
        event: str = None,
        body: str = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.id = id
        self.event = event
        self.body = body

    def validate(self):
        pass

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
            result['body'] = self.body

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
            self.body = m.get('body')

        return self

