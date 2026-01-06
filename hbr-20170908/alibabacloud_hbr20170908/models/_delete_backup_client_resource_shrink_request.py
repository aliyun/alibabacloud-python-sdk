# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBackupClientResourceShrinkRequest(DaraModel):
    def __init__(
        self,
        client_ids_shrink: str = None,
    ):
        # The IDs of HBR clients. The value can be a JSON array that consists of up to 100 client IDs. Separate the IDs with commas (,).
        # 
        # This parameter is required.
        self.client_ids_shrink = client_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_ids_shrink is not None:
            result['ClientIds'] = self.client_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIds') is not None:
            self.client_ids_shrink = m.get('ClientIds')

        return self

