# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DirectNotifyChannel(DaraModel):
    def __init__(
        self,
        identifiers: List[str] = None,
        type: str = None,
    ):
        # 通知对象标识列表
        # 
        # This parameter is required.
        self.identifiers = identifiers
        # 通知渠道类型
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifiers is not None:
            result['identifiers'] = self.identifiers

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identifiers') is not None:
            self.identifiers = m.get('identifiers')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

