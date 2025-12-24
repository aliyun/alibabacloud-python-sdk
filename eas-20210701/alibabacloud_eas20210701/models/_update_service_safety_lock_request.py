# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceSafetyLockRequest(DaraModel):
    def __init__(
        self,
        lock: str = None,
    ):
        # The lock scope. Valid values:
        # 
        # *   all: locks all operations.
        # *   dangerous: locks dangerous operations such as delete and stop operations.
        # *   none: locks no operations.
        # 
        # This parameter is required.
        self.lock = lock

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock is not None:
            result['Lock'] = self.lock

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lock') is not None:
            self.lock = m.get('Lock')

        return self

