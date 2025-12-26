# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CredentialGetResultIntlRequest(DaraModel):
    def __init__(
        self,
        transaction_id: str = None,
    ):
        # Unique identifier for the authentication request
        # 
        # This parameter is required.
        self.transaction_id = transaction_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        return self

