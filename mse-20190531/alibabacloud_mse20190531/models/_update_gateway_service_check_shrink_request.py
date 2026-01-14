# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayServiceCheckShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        check: bool = None,
        expected_statuses_shrink: str = None,
        gateway_unique_id: str = None,
        healthy_threshold: int = None,
        http_host: str = None,
        http_path: str = None,
        interval: int = None,
        protocol: str = None,
        service_id: str = None,
        timeout: int = None,
        unhealthy_threshold: int = None,
    ):
        # The language in which you want to display the results. Valid values: zh and en. zh indicates Chinese, which is the default value. en indicates English.
        self.accept_language = accept_language
        # Specifies whether to enable the health check.
        self.check = check
        # The expected status code, which is required if the health check protocol is HTTP.
        self.expected_statuses_shrink = expected_statuses_shrink
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The healthy threshold of the health check.
        self.healthy_threshold = healthy_threshold
        # The health check domain name, which is optional if the health check protocol is HTTP.
        self.http_host = http_host
        # The health check path, which is required if the health check protocol is HTTP.
        self.http_path = http_path
        # The interval at which the health check is performed.
        self.interval = interval
        # The health check protocol. Valid values:
        # 
        # *   HTTP
        # *   TCP
        self.protocol = protocol
        # The ID of the service.
        self.service_id = service_id
        # The timeout period of responses to the health check. Unit: seconds.
        self.timeout = timeout
        # The unhealthy threshold of the health check.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.check is not None:
            result['Check'] = self.check

        if self.expected_statuses_shrink is not None:
            result['ExpectedStatuses'] = self.expected_statuses_shrink

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.http_host is not None:
            result['HttpHost'] = self.http_host

        if self.http_path is not None:
            result['HttpPath'] = self.http_path

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Check') is not None:
            self.check = m.get('Check')

        if m.get('ExpectedStatuses') is not None:
            self.expected_statuses_shrink = m.get('ExpectedStatuses')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('HttpHost') is not None:
            self.http_host = m.get('HttpHost')

        if m.get('HttpPath') is not None:
            self.http_path = m.get('HttpPath')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

