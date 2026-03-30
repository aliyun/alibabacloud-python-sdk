# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ObtainJwtAuthenticationTokenRequest(DaraModel):
    def __init__(
        self,
        authentication_token_id: str = None,
        consumer_id: str = None,
    ):
        # This parameter is required.
        self.authentication_token_id = authentication_token_id
        # This parameter is required.
        self.consumer_id = consumer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_token_id is not None:
            result['authenticationTokenId'] = self.authentication_token_id

        if self.consumer_id is not None:
            result['consumerId'] = self.consumer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authenticationTokenId') is not None:
            self.authentication_token_id = m.get('authenticationTokenId')

        if m.get('consumerId') is not None:
            self.consumer_id = m.get('consumerId')

        return self

