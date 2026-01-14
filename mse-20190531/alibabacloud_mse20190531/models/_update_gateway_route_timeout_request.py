# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayRouteTimeoutRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
        timeout_json: main_models.UpdateGatewayRouteTimeoutRequestTimeoutJSON = None,
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
        # The timeout period.
        self.timeout_json = timeout_json

    def validate(self):
        if self.timeout_json:
            self.timeout_json.validate()

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

        if self.timeout_json is not None:
            result['TimeoutJSON'] = self.timeout_json.to_map()

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

        if m.get('TimeoutJSON') is not None:
            temp_model = main_models.UpdateGatewayRouteTimeoutRequestTimeoutJSON()
            self.timeout_json = temp_model.from_map(m.get('TimeoutJSON'))

        return self

class UpdateGatewayRouteTimeoutRequestTimeoutJSON(DaraModel):
    def __init__(
        self,
        status: str = None,
        time_unit: str = None,
        unit_num: int = None,
    ):
        # The status of the policy.
        self.status = status
        # The unit of time. A value of s indicates seconds.
        self.time_unit = time_unit
        # The value of the timeout period.
        self.unit_num = unit_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')

        return self

