# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayRouteCORSRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cors_json: main_models.UpdateGatewayRouteCORSRequestCorsJSON = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
    ):
        # The language of the response. In compliance with [RFC 7231](https://tools.ietf.org/html/rfc7231), the backend service must return a response based on the language used by the user.
        # 
        # *   No default value.
        # *   zh-CN: Chinese
        # *   en-US: English
        self.accept_language = accept_language
        # The information about the CORS policy.
        self.cors_json = cors_json
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the associated record.
        self.id = id

    def validate(self):
        if self.cors_json:
            self.cors_json.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cors_json is not None:
            result['CorsJSON'] = self.cors_json.to_map()

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

        if m.get('CorsJSON') is not None:
            temp_model = main_models.UpdateGatewayRouteCORSRequestCorsJSON()
            self.cors_json = temp_model.from_map(m.get('CorsJSON'))

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class UpdateGatewayRouteCORSRequestCorsJSON(DaraModel):
    def __init__(
        self,
        allow_credentials: bool = None,
        allow_headers: str = None,
        allow_methods: str = None,
        allow_origins: str = None,
        expose_headers: str = None,
        status: str = None,
        time_unit: str = None,
        unit_num: int = None,
    ):
        # The credentials allowed.
        self.allow_credentials = allow_credentials
        # The request headers allowed.
        self.allow_headers = allow_headers
        # The HTTP methods allowed.
        self.allow_methods = allow_methods
        # The origins from which access is allowed.
        self.allow_origins = allow_origins
        # The response headers allowed.
        self.expose_headers = expose_headers
        # The status of the policy.
        self.status = status
        # The unit of time.
        self.time_unit = time_unit
        # The value of time.
        self.unit_num = unit_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_credentials is not None:
            result['AllowCredentials'] = self.allow_credentials

        if self.allow_headers is not None:
            result['AllowHeaders'] = self.allow_headers

        if self.allow_methods is not None:
            result['AllowMethods'] = self.allow_methods

        if self.allow_origins is not None:
            result['AllowOrigins'] = self.allow_origins

        if self.expose_headers is not None:
            result['ExposeHeaders'] = self.expose_headers

        if self.status is not None:
            result['Status'] = self.status

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCredentials') is not None:
            self.allow_credentials = m.get('AllowCredentials')

        if m.get('AllowHeaders') is not None:
            self.allow_headers = m.get('AllowHeaders')

        if m.get('AllowMethods') is not None:
            self.allow_methods = m.get('AllowMethods')

        if m.get('AllowOrigins') is not None:
            self.allow_origins = m.get('AllowOrigins')

        if m.get('ExposeHeaders') is not None:
            self.expose_headers = m.get('ExposeHeaders')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')

        return self

