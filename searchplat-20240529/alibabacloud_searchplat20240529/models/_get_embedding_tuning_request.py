# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class GetEmbeddingTuningRequest(DaraModel):
    def __init__(
        self,
        input: List[List[float]] = None,
        parameters: Dict[str, Any] = None,
    ):
        self.input = input
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['input'] = self.input

        if self.parameters is not None:
            result['parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        return self

