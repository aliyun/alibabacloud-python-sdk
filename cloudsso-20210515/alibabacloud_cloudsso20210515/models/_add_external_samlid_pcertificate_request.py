# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddExternalSAMLIdPCertificateRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        x_509certificate: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The X.509 certificate in the PEM format.
        # 
        # The certificate is provided by the SAML identity provider (IdP).
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')

        return self

