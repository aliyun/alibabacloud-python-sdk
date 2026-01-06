# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConnectionRequest(DaraModel):
    def __init__(
        self,
        connection_name: str = None,
    ):
        # The connection name.
        # 
        # This parameter is required.
        self.connection_name = connection_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        return self

