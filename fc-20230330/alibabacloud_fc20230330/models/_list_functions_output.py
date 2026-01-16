# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class ListFunctionsOutput(DaraModel):
    def __init__(
        self,
        functions: List[main_models.Function] = None,
        next_token: str = None,
    ):
        self.functions = functions
        self.next_token = next_token

    def validate(self):
        if self.functions:
            for v1 in self.functions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['functions'] = []
        if self.functions is not None:
            for k1 in self.functions:
                result['functions'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('functions') is not None:
            for k1 in m.get('functions'):
                temp_model = main_models.Function()
                self.functions.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

