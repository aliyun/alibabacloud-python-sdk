# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PublicTemplateStep(DaraModel):
    def __init__(
        self,
        args: List[str] = None,
        type: str = None,
    ):
        # The build step parameter list.
        self.args = args
        # The build instruction type, such as RUN.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['args'] = self.args

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            self.args = m.get('args')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

