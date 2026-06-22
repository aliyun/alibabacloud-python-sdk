# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DiskSize(DaraModel):
    def __init__(
        self,
        category: str = None,
        size: int = None,
    ):
        # 磁盘类型。
        # 
        # This parameter is required.
        self.category = category
        # 单位GB。
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

