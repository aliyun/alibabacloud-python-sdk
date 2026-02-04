# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnDomainStagingConfigRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        function_names: str = None,
    ):
        # The accelerated domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The names of the features to query. You can separate multiple features with commas (,).
        # 
        # This parameter is required.
        self.function_names = function_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.function_names is not None:
            result['FunctionNames'] = self.function_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')

        return self

