# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGatewayFlowRuleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        behavior_type: int = None,
        body_encoding: int = None,
        enable: int = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        response_content_body: str = None,
        response_redirect_url: str = None,
        response_status_code: int = None,
        route_id: int = None,
        route_name: str = None,
        threshold: int = None,
    ):
        # The language in which you want to display the results. Valid values: zh and en. zh indicates Chinese, which is the default value. en indicates English.
        self.accept_language = accept_language
        # The type of the web fallback behavior.
        # 
        # 0: returns the specified content.
        # 
        # 1: redirects to the specified page.
        # 
        # This parameter is required.
        self.behavior_type = behavior_type
        # The encoding format.
        # 
        # 0: normal text
        # 
        # 1: JSON
        self.body_encoding = body_encoding
        # Specifies whether to enable the throttling rule.
        # 
        # 0: disables the throttling rule.
        # 
        # 1: enables the throttling rule.
        # 
        # This parameter is required.
        self.enable = enable
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        # 
        # This parameter is required.
        self.gateway_unique_id = gateway_unique_id
        # The HTTP text to be returned.
        self.response_content_body = response_content_body
        # The address to be redirected to.
        self.response_redirect_url = response_redirect_url
        # The HTTP status code.
        self.response_status_code = response_status_code
        # The ID of the route.
        # 
        # This parameter is required.
        self.route_id = route_id
        # The name of the routing rule.
        # 
        # This parameter is required.
        self.route_name = route_name
        # The overall queries per second (QPS) threshold.
        # 
        # This parameter is required.
        self.threshold = threshold

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

        if self.threshold is not None:
            result['Threshold'] = self.threshold

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

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

