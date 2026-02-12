# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ObtainCredentialRequest(DaraModel):
    def __init__(
        self,
        credential_identifier: str = None,
    ):
        # This parameter is required.
        self.credential_identifier = credential_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_identifier is not None:
            result['credentialIdentifier'] = self.credential_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialIdentifier') is not None:
            self.credential_identifier = m.get('credentialIdentifier')

        return self

