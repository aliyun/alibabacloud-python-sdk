# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GlobalSceneItem(DaraModel):
    def __init__(
        self,
        detail: str = None,
        type: str = None,
    ):
        # The detailed information in JSON format.
        self.detail = detail
        # The type of the vertical data.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['detail'] = self.detail

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

