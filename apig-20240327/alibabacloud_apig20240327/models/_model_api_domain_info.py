# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelApiDomainInfo(DaraModel):
    def __init__(
        self,
        default: bool = None,
        domain_id: str = None,
        domain_scope: str = None,
        name: str = None,
        protocol: str = None,
    ):
        # Indicates whether it is the default domain name of the instance.
        self.default = default
        # The domain name ID.
        self.domain_id = domain_id
        # The domain name scope.
        self.domain_scope = domain_scope
        # The domain name.
        self.name = name
        # The access protocol.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['default'] = self.default

        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.domain_scope is not None:
            result['domainScope'] = self.domain_scope

        if self.name is not None:
            result['name'] = self.name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')

        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('domainScope') is not None:
            self.domain_scope = m.get('domainScope')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

