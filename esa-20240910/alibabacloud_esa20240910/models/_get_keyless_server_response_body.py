# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKeylessServerResponseBody(DaraModel):
    def __init__(
        self,
        ca_certificate: str = None,
        client_certificate: str = None,
        client_private_key: str = None,
        create_time: str = None,
        host: str = None,
        id: str = None,
        name: str = None,
        port: int = None,
        request_id: str = None,
        site_id: int = None,
        site_name: str = None,
        update_time: str = None,
        verify: bool = None,
    ):
        self.ca_certificate = ca_certificate
        self.client_certificate = client_certificate
        self.client_private_key = client_private_key
        self.create_time = create_time
        self.host = host
        # Keyless server ID。
        self.id = id
        self.name = name
        self.port = port
        self.request_id = request_id
        self.site_id = site_id
        self.site_name = site_name
        self.update_time = update_time
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.host is not None:
            result['Host'] = self.host

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.port is not None:
            result['Port'] = self.port

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Verify') is not None:
            self.verify = m.get('Verify')

        return self

