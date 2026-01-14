# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayRouteAuthRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        auth_json: main_models.UpdateGatewayRouteAuthRequestAuthJSON = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The authentication configurations.
        # 
        # This parameter is required.
        self.auth_json = auth_json
        # The gateway ID.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The route ID.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        if self.auth_json:
            self.auth_json.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.auth_json is not None:
            result['AuthJSON'] = self.auth_json.to_map()

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

        if m.get('AuthJSON') is not None:
            temp_model = main_models.UpdateGatewayRouteAuthRequestAuthJSON()
            self.auth_json = temp_model.from_map(m.get('AuthJSON'))

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class UpdateGatewayRouteAuthRequestAuthJSON(DaraModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The authentication type. If an empty string is passed, no authentication type is available. Valid values:
        # 
        # *   JWT
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

