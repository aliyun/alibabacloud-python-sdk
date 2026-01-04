# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecoverAICInstanceRequest(DaraModel):
    def __init__(
        self,
        server_id: str = None,
    ):
        # The ID of the server.
        # 
        # This parameter is required.
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.server_id is not None:
            result['ServerId'] = self.server_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        return self

