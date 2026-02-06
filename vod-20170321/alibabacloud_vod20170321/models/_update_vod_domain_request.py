# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVodDomainRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        owner_id: int = None,
        security_token: str = None,
        sources: str = None,
        top_level_domain: str = None,
    ):
        # The domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.security_token = security_token
        # The information about the addresses of origin servers.
        self.sources = sources
        # The top-level domain.
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.sources is not None:
            result['Sources'] = self.sources

        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Sources') is not None:
            self.sources = m.get('Sources')

        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')

        return self

