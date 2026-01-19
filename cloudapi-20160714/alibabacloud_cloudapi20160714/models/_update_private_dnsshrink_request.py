# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePrivateDNSShrinkRequest(DaraModel):
    def __init__(
        self,
        intranet_domain: str = None,
        records_shrink: str = None,
        security_token: str = None,
        type: str = None,
    ):
        # The internal domain name.
        # 
        # This parameter is required.
        self.intranet_domain = intranet_domain
        # The resolution records. This parameter is valid only when Type is set to A.
        # 
        # This parameter is required.
        self.records_shrink = records_shrink
        self.security_token = security_token
        # The internal domain name resolution type. Valid values:
        # 
        # *   VPC: resolution for virtual private cloud (VPC) access authorizations. A resolution of this type can be bound only to traditional dedicated instances.
        # *   A: resolution that supports A records. A resolution of this type can be bound only to VPC integration dedicated instances.
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
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain

        if self.records_shrink is not None:
            result['Records'] = self.records_shrink

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')

        if m.get('Records') is not None:
            self.records_shrink = m.get('Records')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

