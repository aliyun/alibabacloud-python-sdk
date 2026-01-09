# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class MLServiceAnalysisParam(DaraModel):
    def __init__(
        self,
        input: List[Dict[str, str]] = None,
        parameter: Dict[str, str] = None,
    ):
        self.input = input
        self.parameter = parameter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['input'] = self.input

        if self.parameter is not None:
            result['parameter'] = self.parameter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')

        if m.get('parameter') is not None:
            self.parameter = m.get('parameter')

        return self

