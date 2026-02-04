# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnOriginSiteHealthStatusResponseBody(DaraModel):
    def __init__(
        self,
        origin_site_status: List[main_models.DescribeDcdnOriginSiteHealthStatusResponseBodyOriginSiteStatus] = None,
        request_id: str = None,
    ):
        # The information about the origin server of the accelerated domain name.
        self.origin_site_status = origin_site_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.origin_site_status:
            for v1 in self.origin_site_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OriginSiteStatus'] = []
        if self.origin_site_status is not None:
            for k1 in self.origin_site_status:
                result['OriginSiteStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.origin_site_status = []
        if m.get('OriginSiteStatus') is not None:
            for k1 in m.get('OriginSiteStatus'):
                temp_model = main_models.DescribeDcdnOriginSiteHealthStatusResponseBodyOriginSiteStatus()
                self.origin_site_status.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnOriginSiteHealthStatusResponseBodyOriginSiteStatus(DaraModel):
    def __init__(
        self,
        health_status: str = None,
        host: str = None,
    ):
        # The health status of the origin server. Each point of presence (POP) periodically initiates a probe request to the configured origin domain name. If the POP receives a response from the origin server in 5 seconds, the probe is considered successful. After the probe data for each POP is collected, the health status of the origin server is calculated based on the proportion of successful probes. Valid values:
        # 
        # *   unknown: The probe data of the origin server is not obtained because the configurations of the origin server have been changed recently. Try again later.
        # *   healthy: The proportion of successful probes is higher than 80%.
        # *   degraded: The proportion of successful probes is higher than 0% and lower than or equal to 80%.
        # *   critical: All probing requests to the origin server failed.
        self.health_status = health_status
        # The origin domain name that you configured in the DCDN console, which can be an IPv4 address, IPv6 address, common domain name, or Object Storage Service (OSS) domain name.
        self.host = host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.host is not None:
            result['Host'] = self.host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        return self

