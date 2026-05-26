# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSAMLIdentityProviderCertificateRequest(DaraModel):
    def __init__(
        self,
        user_pool_name: str = None,
        x_509certificate: str = None,
    ):
        self.user_pool_name = user_pool_name
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')

        return self

