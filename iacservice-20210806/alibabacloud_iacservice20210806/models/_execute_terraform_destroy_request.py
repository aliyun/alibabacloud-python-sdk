# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteTerraformDestroyRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        state_id: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.state_id = state_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.state_id is not None:
            result['stateId'] = self.state_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('stateId') is not None:
            self.state_id = m.get('stateId')

        return self

