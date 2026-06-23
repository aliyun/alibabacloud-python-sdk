# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableProcessDefinitionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        id: str = None,
    ):
        # An idempotence token used to make the request idempotent. A universally unique identifier (UUID) is recommended.
        self.client_token = client_token
        # The process definition ID.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

