# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayCircuitBreakerRuleResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateGatewayCircuitBreakerRuleResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.UpdateGatewayCircuitBreakerRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateGatewayCircuitBreakerRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        behavior_type: int = None,
        body_encoding: int = None,
        enable: int = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
        id_list: List[int] = None,
        limit_mode: int = None,
        max_allowed_ms: int = None,
        min_request_amount: int = None,
        recovery_timeout_sec: int = None,
        response_additional_headers: str = None,
        response_content_body: str = None,
        response_redirect_url: str = None,
        response_status_code: int = None,
        route_id: int = None,
        route_name: str = None,
        stat_duration_sec: int = None,
        strategy: int = None,
        trigger_ratio: int = None,
    ):
        self.behavior_type = behavior_type
        self.body_encoding = body_encoding
        self.enable = enable
        self.gateway_id = gateway_id
        self.gateway_unique_id = gateway_unique_id
        self.id = id
        self.id_list = id_list
        self.limit_mode = limit_mode
        self.max_allowed_ms = max_allowed_ms
        self.min_request_amount = min_request_amount
        self.recovery_timeout_sec = recovery_timeout_sec
        self.response_additional_headers = response_additional_headers
        self.response_content_body = response_content_body
        self.response_redirect_url = response_redirect_url
        self.response_status_code = response_status_code
        self.route_id = route_id
        self.route_name = route_name
        self.stat_duration_sec = stat_duration_sec
        self.strategy = strategy
        self.trigger_ratio = trigger_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.behavior_type is not None:
            result['BehaviorType'] = self.behavior_type

        if self.body_encoding is not None:
            result['BodyEncoding'] = self.body_encoding

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        if self.id_list is not None:
            result['IdList'] = self.id_list

        if self.limit_mode is not None:
            result['LimitMode'] = self.limit_mode

        if self.max_allowed_ms is not None:
            result['MaxAllowedMs'] = self.max_allowed_ms

        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount

        if self.recovery_timeout_sec is not None:
            result['RecoveryTimeoutSec'] = self.recovery_timeout_sec

        if self.response_additional_headers is not None:
            result['ResponseAdditionalHeaders'] = self.response_additional_headers

        if self.response_content_body is not None:
            result['ResponseContentBody'] = self.response_content_body

        if self.response_redirect_url is not None:
            result['ResponseRedirectUrl'] = self.response_redirect_url

        if self.response_status_code is not None:
            result['ResponseStatusCode'] = self.response_status_code

        if self.route_id is not None:
            result['RouteId'] = self.route_id

        if self.route_name is not None:
            result['RouteName'] = self.route_name

        if self.stat_duration_sec is not None:
            result['StatDurationSec'] = self.stat_duration_sec

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        if self.trigger_ratio is not None:
            result['TriggerRatio'] = self.trigger_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BehaviorType') is not None:
            self.behavior_type = m.get('BehaviorType')

        if m.get('BodyEncoding') is not None:
            self.body_encoding = m.get('BodyEncoding')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')

        if m.get('LimitMode') is not None:
            self.limit_mode = m.get('LimitMode')

        if m.get('MaxAllowedMs') is not None:
            self.max_allowed_ms = m.get('MaxAllowedMs')

        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')

        if m.get('RecoveryTimeoutSec') is not None:
            self.recovery_timeout_sec = m.get('RecoveryTimeoutSec')

        if m.get('ResponseAdditionalHeaders') is not None:
            self.response_additional_headers = m.get('ResponseAdditionalHeaders')

        if m.get('ResponseContentBody') is not None:
            self.response_content_body = m.get('ResponseContentBody')

        if m.get('ResponseRedirectUrl') is not None:
            self.response_redirect_url = m.get('ResponseRedirectUrl')

        if m.get('ResponseStatusCode') is not None:
            self.response_status_code = m.get('ResponseStatusCode')

        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')

        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')

        if m.get('StatDurationSec') is not None:
            self.stat_duration_sec = m.get('StatDurationSec')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        if m.get('TriggerRatio') is not None:
            self.trigger_ratio = m.get('TriggerRatio')

        return self

