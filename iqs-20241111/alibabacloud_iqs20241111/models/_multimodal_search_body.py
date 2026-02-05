# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class MultimodalSearchBody(DaraModel):
    def __init__(
        self,
        advanced_params: Dict[str, Any] = None,
        query: str = None,
    ):
        self.advanced_params = advanced_params
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_params is not None:
            result['advancedParams'] = self.advanced_params

        if self.query is not None:
            result['query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advancedParams') is not None:
            self.advanced_params = m.get('advancedParams')

        if m.get('query') is not None:
            self.query = m.get('query')

        return self

