# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableDomainProxyTokenRequest(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        domain_proxy_token_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the domain name.
        # 
        # This parameter is required.
        self.domain_id = domain_id
        # The ID of the proxy token of the domain name.
        # 
        # This parameter is required.
        self.domain_proxy_token_id = domain_proxy_token_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_proxy_token_id is not None:
            result['DomainProxyTokenId'] = self.domain_proxy_token_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainProxyTokenId') is not None:
            self.domain_proxy_token_id = m.get('DomainProxyTokenId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

