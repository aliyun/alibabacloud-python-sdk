# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FunctionCall(DaraModel):
    def __init__(
        self,
        arguments: str = None,
        name: str = None,
    ):
        # The parameters detected by the large language model.
        self.arguments = arguments
        # The function name.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arguments is not None:
            result['Arguments'] = self.arguments

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

