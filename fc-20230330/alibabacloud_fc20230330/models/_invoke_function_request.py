# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class InvokeFunctionRequest(DaraModel):
    def __init__(
        self,
        body: BinaryIO = None,
        qualifier: str = None,
    ):
        # The request parameters of function invocation.
        self.body = body
        # The version or alias of the function.
        self.qualifier = qualifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        return self

