# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayOptionRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        gateway_id: int = None,
        gateway_option: main_models.GatewayOption = None,
        gateway_unique_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The detailed configurations of the gateway.
        # 
        # *   **TraceDetails**: the sampling description of Managed Service for OpenTelemetry. Content: TraceEnabled indicates whether Managed Service for OpenTelemetry is activated. Sample indicates the sampling rate of Managed Service for OpenTelemetry.
        # *   **LogConfigDetails**: the description of Simple Log Service. Content: LogEnabled indicates whether Simple Log Service is activated. ProjectName indicates the Simple Log Service project to which logs are delivered. LogStoreName indicates the name of the Logstore.
        # *   **EnableHardwareAcceleration**: indicates whether hardware acceleration is enabled.
        # *   **DisableHttp2Alpn**: indicates whether the HTTP/2 protocol is disabled.
        # *   **EnableWaf**: indicates whether Web Application Firewall (WAF) is enabled.
        self.gateway_option = gateway_option
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id

    def validate(self):
        if self.gateway_option:
            self.gateway_option.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_option is not None:
            result['GatewayOption'] = self.gateway_option.to_map()

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayOption') is not None:
            temp_model = main_models.GatewayOption()
            self.gateway_option = temp_model.from_map(m.get('GatewayOption'))

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        return self

