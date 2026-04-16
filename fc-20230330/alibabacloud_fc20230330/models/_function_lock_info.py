# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FunctionLockInfo(DaraModel):
    def __init__(
        self,
        locked_at: str = None,
        locked_by: str = None,
        locked_resources: List[str] = None,
    ):
        # 锁定时间
        self.locked_at = locked_at
        # 锁定方名称
        self.locked_by = locked_by
        # 锁定的资源类型列表
        self.locked_resources = locked_resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.locked_at is not None:
            result['lockedAt'] = self.locked_at

        if self.locked_by is not None:
            result['lockedBy'] = self.locked_by

        if self.locked_resources is not None:
            result['lockedResources'] = self.locked_resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lockedAt') is not None:
            self.locked_at = m.get('lockedAt')

        if m.get('lockedBy') is not None:
            self.locked_by = m.get('lockedBy')

        if m.get('lockedResources') is not None:
            self.locked_resources = m.get('lockedResources')

        return self

