# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceSourceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_unique_id: str = None,
        source: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # Specifies the type of the returned service source. If this parameter is not specified, service sources of all types are returned. Valid values:
        # 
        # *   K8s
        # *   MSE
        # *   MSE_ZK
        # *   SAE
        # *   EDAS
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

