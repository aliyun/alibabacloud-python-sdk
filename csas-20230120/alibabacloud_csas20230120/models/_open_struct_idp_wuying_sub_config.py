# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OpenStructIdpWuyingSubConfig(DaraModel):
    def __init__(
        self,
        aliuids: List[str] = None,
    ):
        self.aliuids = aliuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliuids is not None:
            result['Aliuids'] = self.aliuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuids') is not None:
            self.aliuids = m.get('Aliuids')

        return self

