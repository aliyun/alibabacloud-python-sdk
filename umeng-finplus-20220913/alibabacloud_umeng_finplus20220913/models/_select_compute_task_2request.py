# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SelectComputeTask2Request(DaraModel):
    def __init__(
        self,
        bc_confirm: bool = None,
        bc_id: int = None,
        client_id: int = None,
    ):
        self.bc_confirm = bc_confirm
        self.bc_id = bc_id
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bc_confirm is not None:
            result['bcConfirm'] = self.bc_confirm

        if self.bc_id is not None:
            result['bcId'] = self.bc_id

        if self.client_id is not None:
            result['clientId'] = self.client_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcConfirm') is not None:
            self.bc_confirm = m.get('bcConfirm')

        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')

        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        return self

