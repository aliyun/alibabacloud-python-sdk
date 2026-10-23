# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartInstanceRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        client_token: str = None,
        force: bool = None,
    ):
        # The restart parameters.
        self.body = body
        # The client token that is used to ensure the idempotence of the request. You can generate the value of this parameter on the client side. Ensure that the value is unique across different requests and contains a maximum of 64 ASCII characters.
        self.client_token = client_token
        # Specifies whether to ignore the cluster state and force a restart. Valid values:
        # - true: Ignores the cluster state.
        # - false: Does not ignore the cluster state. This is the default value.
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.force is not None:
            result['force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('force') is not None:
            self.force = m.get('force')

        return self

