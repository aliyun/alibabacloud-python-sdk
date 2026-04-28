# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProductListRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        token: str = None,
    ):
        self.language = language
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

