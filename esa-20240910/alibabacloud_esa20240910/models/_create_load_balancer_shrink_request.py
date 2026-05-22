# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class CreateLoadBalancerShrinkRequest(DaraModel):
    def __init__(
        self,
        adaptive_routing_shrink: str = None,
        default_pools_shrink: str = None,
        description: str = None,
        enabled: bool = None,
        fallback_pool: int = None,
        monitor_shrink: str = None,
        name: str = None,
        random_steering_shrink: str = None,
        region_pools: Any = None,
        rules_shrink: str = None,
        session_affinity: str = None,
        site_id: int = None,
        steering_policy: str = None,
        sub_region_pools: Any = None,
        ttl: int = None,
    ):
        # Configuration for failover across pools.
        self.adaptive_routing_shrink = adaptive_routing_shrink
        # List of default pools.
        # 
        # This parameter is required.
        self.default_pools_shrink = default_pools_shrink
        # Detailed description of the load balancer, for easier management and identification.
        self.description = description
        # Whether the load balancer is enabled.
        # 
        # - true: Enabled.
        # - false: Not enabled.
        self.enabled = enabled
        # Fallback pool ID, where traffic will be directed when all other pools are unavailable.
        # 
        # This parameter is required.
        self.fallback_pool = fallback_pool
        # Monitor configuration, used for health checks.
        # 
        # This parameter is required.
        self.monitor_shrink = monitor_shrink
        # The name of the load balancer, which must meet the domain name format validation and be a subdomain under the site.
        # 
        # This parameter is required.
        self.name = name
        # Weighted round-robin configuration, used to control the traffic distribution weights among different pools.
        self.random_steering_shrink = random_steering_shrink
        # Address pools corresponding to primary regions.
        self.region_pools = region_pools
        # Rule information.
        self.rules_shrink = rules_shrink
        # Session persistence, with possible values:
        # - off: Not enabled.
        # - ip: Session persistence by IP.
        # - cookie: Session persistence by cookie.
        self.session_affinity = session_affinity
        # Site ID, which can be obtained by calling the [ListSites](~~ListSites~~) interface.
        # 
        # This parameter is required.
        self.site_id = site_id
        # Load balancing strategy.
        # 
        # - geo: Geographical strategy.
        # - random: Weighted round-robin.
        # - order: Primary and backup method.
        # 
        # This parameter is required.
        self.steering_policy = steering_policy
        # Address pools corresponding to secondary regions. When multiple secondary regions share the same set of address pools, the keys can be concatenated with commas.
        self.sub_region_pools = sub_region_pools
        # TTL value, the time-to-live for DNS records, with a default of 30 seconds. The value range is 10-600.
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

        if self.monitor_shrink is not None:
            result['Monitor'] = self.monitor_shrink

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('Monitor') is not None:
            self.monitor_shrink = m.get('Monitor')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

