# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PersonalSpaceInfo(DaraModel):
    def __init__(
        self,
        total_size: int = None,
        used_size: int = None,
    ):
        self.total_size = total_size
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_size is not None:
            result['total_size'] = self.total_size

        if self.used_size is not None:
            result['used_size'] = self.used_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')

        return self

