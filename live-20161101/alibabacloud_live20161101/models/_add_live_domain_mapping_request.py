# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddLiveDomainMappingRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        pull_domain: str = None,
        push_domain: str = None,
        security_token: str = None,
    ):
        self.owner_id = owner_id
        # The streaming domain. The type of the domain name is **liveVideo**.
        # 
        # This parameter is required.
        self.pull_domain = pull_domain
        # The ingest domain. The type of the domain name is **liveEdge**.
        # 
        # This parameter is required.
        self.push_domain = push_domain
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pull_domain is not None:
            result['PullDomain'] = self.pull_domain

        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PullDomain') is not None:
            self.pull_domain = m.get('PullDomain')

        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

