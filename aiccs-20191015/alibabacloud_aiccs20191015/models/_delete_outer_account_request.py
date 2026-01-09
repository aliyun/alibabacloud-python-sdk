# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteOuterAccountRequest(DaraModel):
    def __init__(
        self,
        outer_account_id: str = None,
        outer_account_type: str = None,
    ):
        # This parameter is required.
        self.outer_account_id = outer_account_id
        # This parameter is required.
        self.outer_account_type = outer_account_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id

        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')

        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')

        return self

