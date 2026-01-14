# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListBasicAccelerateIpsResponseBody(DaraModel):
    def __init__(
        self,
        accelerate_ips: List[main_models.ListBasicAccelerateIpsResponseBodyAccelerateIps] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The accelerated IP addresses of the basic GA instance.
        self.accelerate_ips = accelerate_ips
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If **NextToken** was not returned, it indicates that no additional results exist.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.accelerate_ips:
            for v1 in self.accelerate_ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccelerateIps'] = []
        if self.accelerate_ips is not None:
            for k1 in self.accelerate_ips:
                result['AccelerateIps'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accelerate_ips = []
        if m.get('AccelerateIps') is not None:
            for k1 in m.get('AccelerateIps'):
                temp_model = main_models.ListBasicAccelerateIpsResponseBodyAccelerateIps()
                self.accelerate_ips.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBasicAccelerateIpsResponseBodyAccelerateIps(DaraModel):
    def __init__(
        self,
        accelerate_ip_address: str = None,
        accelerate_ip_id: str = None,
        accelerator_id: str = None,
        ip_set_id: str = None,
        state: str = None,
    ):
        # The accelerated IP address of the basic GA instance.
        self.accelerate_ip_address = accelerate_ip_address
        # The ID of the accelerated IP address of the basic GA instance.
        self.accelerate_ip_id = accelerate_ip_id
        # The ID of the basic GA instance.
        self.accelerator_id = accelerator_id
        # The ID of the acceleration region.
        self.ip_set_id = ip_set_id
        # The status of the accelerated IP address. Valid values:
        # 
        # *   **active**: The accelerated IP address is available.
        # *   **binding**: The accelerated IP address is being associated.
        # *   **bound**: The accelerated IP address is associated.
        # *   **unbinding**: The accelerated IP address is being disassociated.
        # *   **deleting**: The accelerated IP address is being deleted.
        # 
        # >  This parameter is unavailable when the accelerated IP address is being created.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_ip_address is not None:
            result['AccelerateIpAddress'] = self.accelerate_ip_address

        if self.accelerate_ip_id is not None:
            result['AccelerateIpId'] = self.accelerate_ip_id

        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateIpAddress') is not None:
            self.accelerate_ip_address = m.get('AccelerateIpAddress')

        if m.get('AccelerateIpId') is not None:
            self.accelerate_ip_id = m.get('AccelerateIpId')

        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

