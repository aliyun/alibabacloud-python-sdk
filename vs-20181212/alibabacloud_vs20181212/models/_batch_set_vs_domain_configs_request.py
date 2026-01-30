# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSetVsDomainConfigsRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        functions: str = None,
        owner_id: int = None,
    ):
        # This parameter is required.
        self.domain_names = domain_names
        # This parameter is required.
        self.functions = functions
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.functions is not None:
            result['Functions'] = self.functions

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('Functions') is not None:
            self.functions = m.get('Functions')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

