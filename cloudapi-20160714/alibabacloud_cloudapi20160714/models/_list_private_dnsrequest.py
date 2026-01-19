# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPrivateDNSRequest(DaraModel):
    def __init__(
        self,
        intranet_domain: str = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        type: str = None,
    ):
        # The internal domain name.
        self.intranet_domain = intranet_domain
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        # The internal domain name resolution type. Valid values:
        # 
        # *   VPC: resolution for virtual private cloud (VPC) access authorizations. A resolution of this type can be bound only to traditional dedicated instances.
        # *   A: resolution that supports A records. A resolution of this type can be bound only to VPC integration dedicated instances.
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

