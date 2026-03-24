# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchSetGrayDomainFunctionRequest(DaraModel):
    def __init__(
        self,
        configs: str = None,
        domain_names: str = None,
    ):
        # This parameter is required.
        self.configs = configs
        # This parameter is required.
        self.domain_names = domain_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs is not None:
            result['Configs'] = self.configs

        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')

        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        return self

