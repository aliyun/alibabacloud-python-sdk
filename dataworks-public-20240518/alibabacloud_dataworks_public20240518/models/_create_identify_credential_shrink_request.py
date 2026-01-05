# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIdentifyCredentialShrinkRequest(DaraModel):
    def __init__(
        self,
        identify_credential_shrink: str = None,
    ):
        # The user credential object.
        self.identify_credential_shrink = identify_credential_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identify_credential_shrink is not None:
            result['IdentifyCredential'] = self.identify_credential_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyCredential') is not None:
            self.identify_credential_shrink = m.get('IdentifyCredential')

        return self

