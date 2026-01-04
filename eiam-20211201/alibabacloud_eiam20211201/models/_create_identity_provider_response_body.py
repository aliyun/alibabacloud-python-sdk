# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        identity_provider_id: str = None,
        request_id: str = None,
    ):
        # Identity provider ID.
        self.identity_provider_id = identity_provider_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

