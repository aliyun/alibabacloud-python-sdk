# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetKeylessServerRequest(DaraModel):
    def __init__(
        self,
        ca_certificate: str = None,
        client_certificate: str = None,
        client_private_key: str = None,
        host: str = None,
        id: str = None,
        name: str = None,
        port: int = None,
        site_id: int = None,
        verify: bool = None,
    ):
        # The CA certificate used to verify the server certificate of the keyless server. This parameter applies only when `Verify` is set to `true`.
        self.ca_certificate = ca_certificate
        # The client certificate. This parameter must be used with the `ClientPrivateKey` parameter.
        self.client_certificate = client_certificate
        # The client private key. This parameter must be used with the `ClientCertificate` parameter.
        self.client_private_key = client_private_key
        # The hostname of the keyless server. The value can be a domain name or an IP address.
        # 
        # This parameter is required.
        self.host = host
        # The keyless server ID.
        self.id = id
        # The keyless server name.
        # 
        # This parameter is required.
        self.name = name
        # The keyless server port.
        # 
        # This parameter is required.
        self.port = port
        # The site ID. You can obtain this ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Specifies whether to verify the server certificate of the keyless server. Default: false.
        self.verify = verify

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_certificate is not None:
            result['CaCertificate'] = self.ca_certificate

        if self.client_certificate is not None:
            result['ClientCertificate'] = self.client_certificate

        if self.client_private_key is not None:
            result['ClientPrivateKey'] = self.client_private_key

        if self.host is not None:
            result['Host'] = self.host

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.port is not None:
            result['Port'] = self.port

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.verify is not None:
            result['Verify'] = self.verify

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCertificate') is not None:
            self.ca_certificate = m.get('CaCertificate')

        if m.get('ClientCertificate') is not None:
            self.client_certificate = m.get('ClientCertificate')

        if m.get('ClientPrivateKey') is not None:
            self.client_private_key = m.get('ClientPrivateKey')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Verify') is not None:
            self.verify = m.get('Verify')

        return self

