# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDomainProxyTokenResponseBody(DaraModel):
    def __init__(
        self,
        domain_proxy_token_id: str = None,
        request_id: str = None,
    ):
        # The ID of the proxy token of the domain name.
        self.domain_proxy_token_id = domain_proxy_token_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_proxy_token_id is not None:
            result['DomainProxyTokenId'] = self.domain_proxy_token_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainProxyTokenId') is not None:
            self.domain_proxy_token_id = m.get('DomainProxyTokenId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

