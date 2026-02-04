# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDcdnWafPolicyDomainsRequest(DaraModel):
    def __init__(
        self,
        bind_domains: str = None,
        method: int = None,
        policy_id: int = None,
        unbind_domains: str = None,
    ):
        # The domain names that you want to bind to the protection policy. You can specify up to 50 domain names. Separate multiple domain names with commas (,).
        # 
        # > You can configure either **BindDomains** or **UnbindDomains**.
        self.bind_domains = bind_domains
        # The association method. Valid values:
        # 
        # *   0: replace.
        # *   1: add.
        # *   Default value: 0.
        # 
        # > 
        # 
        # *   This parameter takes effect only when you specify **BindDomains**. If you have associated a domain name indicated by **BindDomains** with the default protection policy, the `Policy.DefaultAndCustom.BindToSameDomain` error is returned.
        # 
        # *   You can only replace accelerated domain names that are bound to the default protection policy.
        self.method = method
        # The ID of the protection policy. You can specify only one ID in each request.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The domain names that you want to unbind from the protection policy. You can specify up to 50 domain names. Separate multiple domain names with commas (,).
        # 
        # > You can configure either **BindDomains** or **UnbindDomains**.
        self.unbind_domains = unbind_domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_domains is not None:
            result['BindDomains'] = self.bind_domains

        if self.method is not None:
            result['Method'] = self.method

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.unbind_domains is not None:
            result['UnbindDomains'] = self.unbind_domains

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindDomains') is not None:
            self.bind_domains = m.get('BindDomains')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('UnbindDomains') is not None:
            self.unbind_domains = m.get('UnbindDomains')

        return self

