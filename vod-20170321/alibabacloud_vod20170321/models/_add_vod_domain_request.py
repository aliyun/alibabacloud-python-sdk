# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddVodDomainRequest(DaraModel):
    def __init__(
        self,
        check_url: str = None,
        domain_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        scope: str = None,
        security_token: str = None,
        sources: str = None,
        top_level_domain: str = None,
    ):
        # The health check URL.
        self.check_url = check_url
        # The accelerated domain name to be added to ApsaraVideo VOD. Wildcard domain names are supported, starting with a period (.), such as .example.com.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # This parameter is valid for international users and Chinese mainland users of L3 or higher. Valid values:
        # - **domestic** (default): the Chinese mainland.
        # - **overseas**: Hong Kong (China), Macao (China), Taiwan (China), and regions outside China.
        # - **global**: global acceleration.
        self.scope = scope
        self.security_token = security_token
        # The list of origin addresses. For more information about the parameters, see the **Sources** table below.
        # 
        # This parameter is required.
        self.sources = sources
        # The top-level domain name.
        self.top_level_domain = top_level_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.sources is not None:
            result['Sources'] = self.sources

        if self.top_level_domain is not None:
            result['TopLevelDomain'] = self.top_level_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Sources') is not None:
            self.sources = m.get('Sources')

        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')

        return self

