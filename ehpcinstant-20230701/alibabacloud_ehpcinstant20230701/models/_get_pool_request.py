# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPoolRequest(DaraModel):
    def __init__(
        self,
        pool_name: str = None,
    ):
        # The name of the resource pool.
        # 
        # *   The value can be up to 15 characters in length.
        # *   It can contain digits, uppercase letters, lowercase letters, underscores (_), and dots (.).
        # 
        # This parameter is required.
        self.pool_name = pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')

        return self

