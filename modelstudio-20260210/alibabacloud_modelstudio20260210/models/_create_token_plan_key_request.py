# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTokenPlanKeyRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        description: str = None,
    ):
        # The account ID.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The description of the key.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

