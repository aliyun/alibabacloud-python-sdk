# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AppConfigMapping(DaraModel):
    def __init__(
        self,
        alias: str = None,
        model_id: str = None,
    ):
        self.alias = alias
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.model_id is not None:
            result['modelId'] = self.model_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        return self

