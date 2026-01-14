# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAlipayTransferStatusRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        workspace_id: str = None,
    ):
        self.code = code
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.workspace_id is not None:
            result['workspace_id'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('workspace_id') is not None:
            self.workspace_id = m.get('workspace_id')

        return self

