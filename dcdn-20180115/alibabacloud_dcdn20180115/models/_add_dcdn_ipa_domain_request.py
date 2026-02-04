# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDcdnIpaDomainRequest(DaraModel):
    def __init__(
        self,
        check_url: str = None,
        domain_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        protocol: str = None,
        resource_group_id: str = None,
        scope: str = None,
        security_token: str = None,
        sources: str = None,
        top_level_domain: str = None,
    ):
        # The URL that is used for health checks.
        self.check_url = check_url
        # The domain name to be added to IPA.
        # 
        # A wildcard domain that starts with a period (.) is supported, such as .example.com.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The protocol. Valid values:
        # 
        # *   **udp**
        # *   **tcp**
        # 
        # **
        # 
        # **Description** For example: `{"protocol":"udp"}`.
        self.protocol = protocol
        # The ID of the resource group. If you do not specify a value for this parameter, the system automatically assigns the ID of the default resource group.
        self.resource_group_id = resource_group_id
        # The acceleration region. Default value: domestic. Valid values:
        # 
        # *   **domestic**: Chinese mainland
        # *   **overseas**: outside the Chinese mainland
        # *   **global**: global
        self.scope = scope
        self.security_token = security_token
        # The information about the addresses of origin servers.
        # 
        # This parameter is required.
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
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

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

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Sources') is not None:
            self.sources = m.get('Sources')

        if m.get('TopLevelDomain') is not None:
            self.top_level_domain = m.get('TopLevelDomain')

        return self

