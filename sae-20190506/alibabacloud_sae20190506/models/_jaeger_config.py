# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JaegerConfig(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
    ):
        self.endpoint = endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        return self

