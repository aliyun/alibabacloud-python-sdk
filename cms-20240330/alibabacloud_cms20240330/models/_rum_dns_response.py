# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RumDnsResponse(DaraModel):
    def __init__(
        self,
        domain: str = None,
        message: str = None,
        result: bool = None,
    ):
        self.domain = domain
        self.message = message
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        if self.message is not None:
            result['message'] = self.message

        if self.result is not None:
            result['result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('result') is not None:
            self.result = m.get('result')

        return self

