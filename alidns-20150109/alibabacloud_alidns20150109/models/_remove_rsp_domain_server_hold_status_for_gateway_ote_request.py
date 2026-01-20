# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveRspDomainServerHoldStatusForGatewayOteRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        domain_name: str = None,
        status_msg: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.domain_name = domain_name
        self.status_msg = status_msg

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.status_msg is not None:
            result['StatusMsg'] = self.status_msg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('StatusMsg') is not None:
            self.status_msg = m.get('StatusMsg')

        return self

