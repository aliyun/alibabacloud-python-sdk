# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CredentialConfiguration(DaraModel):
    def __init__(
        self,
        credential_name: str = None,
    ):
        # 凭证的唯一标识符
        self.credential_name = credential_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        return self

