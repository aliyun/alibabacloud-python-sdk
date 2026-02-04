# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDcdnDomainStagingConfigRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        functions: str = None,
    ):
        # The accelerated domain name. Separate multiple accelerated domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The list of features. Format: `[{"functionArgs":[{"argName":"parameter key","argValue":"parameter value"},{"argName":"xx","argValue":"xx"}],"functionName": feature name"}]`
        # 
        # > Separate multiple parameters with commas (,).
        # 
        # This parameter is required.
        self.functions = functions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.functions is not None:
            result['Functions'] = self.functions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Functions') is not None:
            self.functions = m.get('Functions')

        return self

