# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthInfoConfigValue(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        private_domain: str = None,
        project: str = None,
        public_domain: str = None,
    ):
        # The credential.
        self.auth_token = auth_token
        # The private domain name.
        self.private_domain = private_domain
        # The project space.
        self.project = project
        # The public domain name.
        self.public_domain = public_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.private_domain is not None:
            result['PrivateDomain'] = self.private_domain

        if self.project is not None:
            result['Project'] = self.project

        if self.public_domain is not None:
            result['PublicDomain'] = self.public_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('PrivateDomain') is not None:
            self.private_domain = m.get('PrivateDomain')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('PublicDomain') is not None:
            self.public_domain = m.get('PublicDomain')

        return self

