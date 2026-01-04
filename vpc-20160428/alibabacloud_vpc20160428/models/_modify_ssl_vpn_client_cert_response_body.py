# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySslVpnClientCertResponseBody(DaraModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
        ssl_vpn_client_cert_id: str = None,
    ):
        # The name of the SSL client certificate.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The ID of the SSL client certificate.
        self.ssl_vpn_client_cert_id = ssl_vpn_client_cert_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ssl_vpn_client_cert_id is not None:
            result['SslVpnClientCertId'] = self.ssl_vpn_client_cert_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SslVpnClientCertId') is not None:
            self.ssl_vpn_client_cert_id = m.get('SslVpnClientCertId')

        return self

