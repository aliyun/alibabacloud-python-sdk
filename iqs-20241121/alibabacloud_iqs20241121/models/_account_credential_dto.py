# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AccountCredentialDTO(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        caller_identity: str = None,
        id: int = None,
    ):
        self.account_id = account_id
        self.caller_identity = caller_identity
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

        if self.caller_identity is not None:
            result['callerIdentity'] = self.caller_identity

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('callerIdentity') is not None:
            self.caller_identity = m.get('callerIdentity')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

