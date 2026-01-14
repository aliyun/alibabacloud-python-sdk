# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayRouteRetryRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
        retry_json: main_models.UpdateGatewayRouteRetryRequestRetryJSON = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The ID of the associated record.
        self.id = id
        # The information about the retry policy.
        self.retry_json = retry_json

    def validate(self):
        if self.retry_json:
            self.retry_json.validate()

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

        if self.retry_json is not None:
            result['RetryJSON'] = self.retry_json.to_map()

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

        if m.get('RetryJSON') is not None:
            temp_model = main_models.UpdateGatewayRouteRetryRequestRetryJSON()
            self.retry_json = temp_model.from_map(m.get('RetryJSON'))

        return self

class UpdateGatewayRouteRetryRequestRetryJSON(DaraModel):
    def __init__(
        self,
        attempts: int = None,
        http_codes: List[str] = None,
        retry_on: List[str] = None,
        status: str = None,
    ):
        # The number of retries.
        self.attempts = attempts
        # The HTTP status codes.
        self.http_codes = http_codes
        # The retry conditions.
        self.retry_on = retry_on
        # The status of the policy.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempts is not None:
            result['Attempts'] = self.attempts

        if self.http_codes is not None:
            result['HttpCodes'] = self.http_codes

        if self.retry_on is not None:
            result['RetryOn'] = self.retry_on

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attempts') is not None:
            self.attempts = m.get('Attempts')

        if m.get('HttpCodes') is not None:
            self.http_codes = m.get('HttpCodes')

        if m.get('RetryOn') is not None:
            self.retry_on = m.get('RetryOn')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

