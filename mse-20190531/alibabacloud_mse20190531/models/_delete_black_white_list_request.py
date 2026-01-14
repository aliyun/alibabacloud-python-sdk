# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBlackWhiteListRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
    ):
        self.accept_language = accept_language
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

