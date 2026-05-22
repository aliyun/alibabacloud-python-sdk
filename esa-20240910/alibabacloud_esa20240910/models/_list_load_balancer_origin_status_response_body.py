# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListLoadBalancerOriginStatusResponseBody(DaraModel):
    def __init__(
        self,
        origin_status: List[main_models.ListLoadBalancerOriginStatusResponseBodyOriginStatus] = None,
        request_id: str = None,
    ):
        # List of origin statuses under the load balancer.
        self.origin_status = origin_status
        # Request ID, used for tracking the request.
        self.request_id = request_id

    def validate(self):
        if self.origin_status:
            for v1 in self.origin_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OriginStatus'] = []
        if self.origin_status is not None:
            for k1 in self.origin_status:
                result['OriginStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.origin_status = []
        if m.get('OriginStatus') is not None:
            for k1 in m.get('OriginStatus'):
                temp_model = main_models.ListLoadBalancerOriginStatusResponseBodyOriginStatus()
                self.origin_status.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLoadBalancerOriginStatusResponseBodyOriginStatus(DaraModel):
    def __init__(
        self,
        load_balancer_id: int = None,
        origin_id: int = None,
        pool_id: int = None,
        pool_type: str = None,
        reason: str = None,
        status: str = None,
    ):
        # ID of the load balancer.
        self.load_balancer_id = load_balancer_id
        # ID of the origin.
        self.origin_id = origin_id
        # ID of the source address pool.
        self.pool_id = pool_id
        # The origin pool to which the source belongs, under this load balancer. Only \\"default_pool\\" (default address pool) will be displayed; other types will return an empty string.
        self.pool_type = pool_type
        # Reason for the probe failure.
        self.reason = reason
        # Status of the origin:
        # - Healthy(healthy): The probe result is available.
        # - Unhealthy(unhealthy): The probe result is unavailable.
        # - Unknown(unknown): Unknown, the monitor has not yet probed.
        # - Undetected(undetected): The load balancer to which the origin belongs is not bound to a monitor.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.origin_id is not None:
            result['OriginId'] = self.origin_id

        if self.pool_id is not None:
            result['PoolId'] = self.pool_id

        if self.pool_type is not None:
            result['PoolType'] = self.pool_type

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('OriginId') is not None:
            self.origin_id = m.get('OriginId')

        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')

        if m.get('PoolType') is not None:
            self.pool_type = m.get('PoolType')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

