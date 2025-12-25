# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLoadBalancerOriginStatusRequest(DaraModel):
    def __init__(
        self,
        load_balancer_ids: str = None,
        pool_type: str = None,
        site_id: int = None,
    ):
        # Load balancer ID. When querying multiple load balancers, separate the IDs with commas. A maximum of 100 load balancer IDs can be passed at once. Load balancer IDs can be obtained by calling the [ListLoadBalancers](https://help.aliyun.com/document_detail/2868897.html) interface.
        # 
        # This parameter is required.
        self.load_balancer_ids = load_balancer_ids
        # Source address pool type. Various source address pools are configured under the load balancer, including default pools, fallback pools, and primary region pools. Only the status of origins in the default pool affects the status of the load balancer itself. Passing `default_pool` means only querying the status of origins in the default source address pool under the load balancer.
        self.pool_type = pool_type
        # Site ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids

        if self.pool_type is not None:
            result['PoolType'] = self.pool_type

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')

        if m.get('PoolType') is not None:
            self.pool_type = m.get('PoolType')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

