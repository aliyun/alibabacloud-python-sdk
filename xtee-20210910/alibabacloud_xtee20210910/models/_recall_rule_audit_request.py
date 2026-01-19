# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecallRuleAuditRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        reg_id: str = None,
    ):
        # Primary key ID
        # 
        # This parameter is required.
        self.id = id
        # Region code
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

