# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayCircuitBreakerRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        filter_params: str = None,
    ):
        self.accept_language = accept_language
        # just for POP
        # 
        # This parameter is required.
        self.filter_params = filter_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.filter_params is not None:
            result['FilterParams'] = self.filter_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('FilterParams') is not None:
            self.filter_params = m.get('FilterParams')

        return self

