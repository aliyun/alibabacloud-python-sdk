# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteClientKeyRequest(DaraModel):
    def __init__(
        self,
        client_key_id: str = None,
    ):
        # The ID of the client key.
        # 
        # This parameter is required.
        self.client_key_id = client_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_key_id is not None:
            result['ClientKeyId'] = self.client_key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientKeyId') is not None:
            self.client_key_id = m.get('ClientKeyId')

        return self

