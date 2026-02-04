# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRDDomainConfigRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        function_name: str = None,
    ):
        # The accelerated domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The name of the feature. Default value: source_group.
        self.function_name = function_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        return self

