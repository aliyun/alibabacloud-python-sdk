# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnDomainConfigsRequest(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        domain_name: str = None,
        function_names: str = None,
        owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the configuration.
        self.config_id = config_id
        # The accelerated domain name. You can specify only one domain name in each request.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The names of the features to query. Separate features with commas (,).
        self.function_names = function_names
        self.owner_id = owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.function_names is not None:
            result['FunctionNames'] = self.function_names

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('FunctionNames') is not None:
            self.function_names = m.get('FunctionNames')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

