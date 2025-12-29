# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstanceMetadataOptions(DaraModel):
    def __init__(
        self,
        http_tokens: str = None,
    ):
        self.http_tokens = http_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_tokens is not None:
            result['http_tokens'] = self.http_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('http_tokens') is not None:
            self.http_tokens = m.get('http_tokens')

        return self

