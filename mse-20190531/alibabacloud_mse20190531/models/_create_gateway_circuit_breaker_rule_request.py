# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGatewayCircuitBreakerRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        behavior_type: int = None,
        body_encoding: int = None,
        enable: int = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        max_allowed_ms: int = None,
        min_request_amount: int = None,
        recovery_timeout_sec: int = None,
        response_content_body: str = None,
        response_redirect_url: str = None,
        response_status_code: int = None,
        route_id: int = None,
        route_name: str = None,
        stat_duration_sec: int = None,
        strategy: int = None,
        trigger_ratio: int = None,
    ):
        # The language in which you want the results to be displayed. Valid values: zh (default): Chinese. en: English.
        self.accept_language = accept_language
        # The type of the web fallback behavior.
        # 
        # 0: returns the specified content.
        # 
        # 1: redirects to the specified page.
        # 
        # This parameter is required.
        self.behavior_type = behavior_type
        # The encoding type.
        # 
        # 0: plain text
        # 
        # 1: JSON
        self.body_encoding = body_encoding
        # Specifies whether to enable the rule.
        # 
        # 0: disables the rule.
        # 
        # 1: enables the rule.
        # 
        # This parameter is required.
        self.enable = enable
        # The gateway ID.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The threshold in slow call proportion mode.
        self.max_allowed_ms = max_allowed_ms
        # The minimum number of requests to trigger circuit breaking.
        # 
        # This parameter is required.
        self.min_request_amount = min_request_amount
        # The circuit breaking timeout period.
        # 
        # This parameter is required.
        self.recovery_timeout_sec = recovery_timeout_sec
        # The HTTP text to be returned.
        self.response_content_body = response_content_body
        # The redirection URL.
        self.response_redirect_url = response_redirect_url
        # The HTTP status code.
        self.response_status_code = response_status_code
        # The route ID.
        # 
        # This parameter is required.
        self.route_id = route_id
        # The route name.
        # 
        # This parameter is required.
        self.route_name = route_name
        # The statistical duration for triggering circuit breaking.
        # 
        # This parameter is required.
        self.stat_duration_sec = stat_duration_sec
        # The type of the threshold.
        # 
        # 0: slow call proportion
        # 
        # 1: failure proportion
        # 
        # This parameter is required.
        self.strategy = strategy
        # The request percentage that triggers circuit breaking.
        # 
        # This parameter is required.
        self.trigger_ratio = trigger_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

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

        if self.max_allowed_ms is not None:
            result['MaxAllowedMs'] = self.max_allowed_ms

        if self.min_request_amount is not None:
            result['MinRequestAmount'] = self.min_request_amount

        if self.recovery_timeout_sec is not None:
            result['RecoveryTimeoutSec'] = self.recovery_timeout_sec

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
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

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

        if m.get('MaxAllowedMs') is not None:
            self.max_allowed_ms = m.get('MaxAllowedMs')

        if m.get('MinRequestAmount') is not None:
            self.min_request_amount = m.get('MinRequestAmount')

        if m.get('RecoveryTimeoutSec') is not None:
            self.recovery_timeout_sec = m.get('RecoveryTimeoutSec')

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

