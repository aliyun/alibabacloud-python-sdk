# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class UpdateLoadBalancerShrinkRequest(DaraModel):
    def __init__(
        self,
        adaptive_routing_shrink: str = None,
        default_pools_shrink: str = None,
        description: str = None,
        enabled: bool = None,
        fallback_pool: int = None,
        id: int = None,
        monitor_shrink: str = None,
        random_steering_shrink: str = None,
        region_pools: Any = None,
        rules_shrink: str = None,
        session_affinity: str = None,
        site_id: int = None,
        steering_policy: str = None,
        sub_region_pools: Any = None,
        ttl: int = None,
    ):
        # Configures origin-pull behavior across address pools.
        self.adaptive_routing_shrink = adaptive_routing_shrink
        # A list of default address pool IDs.
        self.default_pools_shrink = default_pools_shrink
        # An optional description of the load balancer for easier identification and management.
        self.description = description
        # Specifies whether the load balancer is enabled.
        # 
        # - `true`: The load balancer is enabled.
        # 
        # - `false`: The load balancer is disabled.
        self.enabled = enabled
        # The ID of the fallback address pool. Traffic is routed to this pool when all other address pools are unavailable.
        self.fallback_pool = fallback_pool
        # The ID of the load balancer. You can obtain this ID by calling the [ListLoadBalancers](https://help.aliyun.com/document_detail/2868897.html) API operation.
        # 
        # This parameter is required.
        self.id = id
        # The health check monitor configuration.
        self.monitor_shrink = monitor_shrink
        # The configuration for weighted round-robin. This setting controls the weight of traffic distributed to different address pools.
        self.random_steering_shrink = random_steering_shrink
        # A map of primary regions to their corresponding address pools.
        self.region_pools = region_pools
        # A list of rules that define behavior overrides for specific conditions.
        self.rules_shrink = rules_shrink
        # The method for session affinity, which ensures that requests from the same client are routed to the same origin server. Valid values:
        # 
        # - `off`: Disables session affinity.
        # 
        # - `ip`: Enables session affinity based on the client IP address.
        # 
        # - `cookie`: Enables session affinity based on a cookie.
        self.session_affinity = session_affinity
        # The ID of the Site. You can obtain this ID by calling the [ListSites](~~ListSites~~) API operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The traffic steering policy, which determines how traffic is distributed among the address pools.
        self.steering_policy = steering_policy
        # A map of secondary regions to their corresponding address pools. To assign the same address pools to multiple secondary regions, combine their codes into a single, comma-separated key.
        self.sub_region_pools = sub_region_pools
        # The Time to Live (TTL) for the DNS record, in seconds. The default is 30. The value must be between 10 and 600, inclusive.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptive_routing_shrink is not None:
            result['AdaptiveRouting'] = self.adaptive_routing_shrink

        if self.default_pools_shrink is not None:
            result['DefaultPools'] = self.default_pools_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.fallback_pool is not None:
            result['FallbackPool'] = self.fallback_pool

        if self.id is not None:
            result['Id'] = self.id

        if self.monitor_shrink is not None:
            result['Monitor'] = self.monitor_shrink

        if self.random_steering_shrink is not None:
            result['RandomSteering'] = self.random_steering_shrink

        if self.region_pools is not None:
            result['RegionPools'] = self.region_pools

        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

        if self.session_affinity is not None:
            result['SessionAffinity'] = self.session_affinity

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.steering_policy is not None:
            result['SteeringPolicy'] = self.steering_policy

        if self.sub_region_pools is not None:
            result['SubRegionPools'] = self.sub_region_pools

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdaptiveRouting') is not None:
            self.adaptive_routing_shrink = m.get('AdaptiveRouting')

        if m.get('DefaultPools') is not None:
            self.default_pools_shrink = m.get('DefaultPools')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('FallbackPool') is not None:
            self.fallback_pool = m.get('FallbackPool')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Monitor') is not None:
            self.monitor_shrink = m.get('Monitor')

        if m.get('RandomSteering') is not None:
            self.random_steering_shrink = m.get('RandomSteering')

        if m.get('RegionPools') is not None:
            self.region_pools = m.get('RegionPools')

        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        if m.get('SessionAffinity') is not None:
            self.session_affinity = m.get('SessionAffinity')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SteeringPolicy') is not None:
            self.steering_policy = m.get('SteeringPolicy')

        if m.get('SubRegionPools') is not None:
            self.sub_region_pools = m.get('SubRegionPools')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

