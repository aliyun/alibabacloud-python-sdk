# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitializeOperationRoleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        body: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. The client generates the value. The value must be unique among different requests and can be up to 64 ASCII characters long.
        self.client_token = client_token
        # The name of the Elasticsearch service-linked role to be created.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.body is not None:
            result['body'] = self.body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('body') is not None:
            self.body = m.get('body')

        return self

