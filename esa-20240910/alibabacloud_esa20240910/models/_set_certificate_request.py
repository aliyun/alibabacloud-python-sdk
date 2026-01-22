# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCertificateRequest(DaraModel):
    def __init__(
        self,
        cas_id: int = None,
        certificate: str = None,
        id: str = None,
        key_server_id: str = None,
        name: str = None,
        owner_id: int = None,
        private_key: str = None,
        region: str = None,
        security_token: str = None,
        site_id: int = None,
        type: str = None,
    ):
        # The certificate ID on Certificate Management Service.
        self.cas_id = cas_id
        # The certificate content.
        self.certificate = certificate
        # The certificate ID on ESA.
        self.id = id
        self.key_server_id = key_server_id
        # The certificate name.
        self.name = name
        self.owner_id = owner_id
        # The private key of the certificate.
        self.private_key = private_key
        # The region.
        self.region = region
        self.security_token = security_token
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The certificate type. Valid values:
        # 
        # *   cas: a certificate purchased by using Certificate Management Service.
        # *   upload: a custom certificate that you upload.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cas_id is not None:
            result['CasId'] = self.cas_id

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.id is not None:
            result['Id'] = self.id

        if self.key_server_id is not None:
            result['KeyServerId'] = self.key_server_id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.region is not None:
            result['Region'] = self.region

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasId') is not None:
            self.cas_id = m.get('CasId')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KeyServerId') is not None:
            self.key_server_id = m.get('KeyServerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

