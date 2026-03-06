# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteApiMcpServerRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        id: str = None,
    ):
        # The client token used to ensure the idempotence of the request. Generate this value on your client and make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. Use a universally unique identifier (UUID). The token is valid for three days.
        self.client_token = client_token
        # The ID of the API MCP service.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('id') is not None:
            self.id = m.get('id')

        return self

