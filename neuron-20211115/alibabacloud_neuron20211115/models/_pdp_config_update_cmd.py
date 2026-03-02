# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpConfigUpdateCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        context: str = None,
        id: int = None,
    ):
        self.account_id = account_id
        # This parameter is required.
        self.context = context
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.context is not None:
            result['context'] = self.context

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('context') is not None:
            self.context = m.get('context')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

