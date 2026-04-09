# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserExclusiveCredentialResponseBody(DaraModel):
    def __init__(
        self,
        credential_id: str = None,
        credential_identifier: str = None,
    ):
        self.credential_id = credential_id
        # 凭据标识。
        self.credential_identifier = credential_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        if self.credential_identifier is not None:
            result['credentialIdentifier'] = self.credential_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        if m.get('credentialIdentifier') is not None:
            self.credential_identifier = m.get('credentialIdentifier')

        return self

