# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgentIMChannelShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        client_token: str = None,
    ):
        # The request body.
        self.body_shrink = body_shrink
        # The reserved idempotency token. The backend does not provide persistent idempotency guarantees in this phase.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_shrink is not None:
            result['body'] = self.body_shrink

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

