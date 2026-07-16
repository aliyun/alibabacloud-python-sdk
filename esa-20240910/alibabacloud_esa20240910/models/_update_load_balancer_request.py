# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class UpdateLoadBalancerRequest(DaraModel):
    def __init__(
        self,
        adaptive_routing: main_models.UpdateLoadBalancerRequestAdaptiveRouting = None,
        default_pools: List[int] = None,
        description: str = None,
        enabled: bool = None,
        fallback_pool: int = None,
        id: int = None,
        monitor: main_models.UpdateLoadBalancerRequestMonitor = None,
        random_steering: main_models.UpdateLoadBalancerRequestRandomSteering = None,
        region_pools: Any = None,
        rules: List[main_models.UpdateLoadBalancerRequestRules] = None,
        session_affinity: str = None,
        site_id: int = None,
        steering_policy: str = None,
        sub_region_pools: Any = None,
        ttl: int = None,
    ):
        # Configures origin-pull behavior across address pools.
        self.adaptive_routing = adaptive_routing
        # A list of default address pool IDs.
        self.default_pools = default_pools
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
        self.monitor = monitor
        # The configuration for weighted round-robin. This setting controls the weight of traffic distributed to different address pools.
        self.random_steering = random_steering
        # A map of primary regions to their corresponding address pools.
        self.region_pools = region_pools
        # A list of rules that define behavior overrides for specific conditions.
        self.rules = rules
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
        if self.adaptive_routing:
            self.adaptive_routing.validate()
        if self.monitor:
            self.monitor.validate()
        if self.random_steering:
            self.random_steering.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptive_routing is not None:
            result['AdaptiveRouting'] = self.adaptive_routing.to_map()

        if self.default_pools is not None:
            result['DefaultPools'] = self.default_pools

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.fallback_pool is not None:
            result['FallbackPool'] = self.fallback_pool

        if self.id is not None:
            result['Id'] = self.id

        if self.monitor is not None:
            result['Monitor'] = self.monitor.to_map()

        if self.random_steering is not None:
            result['RandomSteering'] = self.random_steering.to_map()

        if self.region_pools is not None:
            result['RegionPools'] = self.region_pools

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.UpdateLoadBalancerRequestAdaptiveRouting()
            self.adaptive_routing = temp_model.from_map(m.get('AdaptiveRouting'))

        if m.get('DefaultPools') is not None:
            self.default_pools = m.get('DefaultPools')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('FallbackPool') is not None:
            self.fallback_pool = m.get('FallbackPool')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Monitor') is not None:
            temp_model = main_models.UpdateLoadBalancerRequestMonitor()
            self.monitor = temp_model.from_map(m.get('Monitor'))

        if m.get('RandomSteering') is not None:
            temp_model = main_models.UpdateLoadBalancerRequestRandomSteering()
            self.random_steering = temp_model.from_map(m.get('RandomSteering'))

        if m.get('RegionPools') is not None:
            self.region_pools = m.get('RegionPools')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.UpdateLoadBalancerRequestRules()
                self.rules.append(temp_model.from_map(k1))

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

class UpdateLoadBalancerRequestRules(DaraModel):
    def __init__(
        self,
        fixed_response: main_models.UpdateLoadBalancerRequestRulesFixedResponse = None,
        overrides: Any = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        terminates: bool = None,
    ):
        # The fixed response to return when the rule\\"s condition is met.
        self.fixed_response = fixed_response
        # The settings to override for requests that match this rule\\"s condition. These settings take precedence over the load balancer\\"s main configuration.
        self.overrides = overrides
        # The content of the rule, specified as a conditional expression to match user requests. This parameter is not required when you configure global settings. Use cases:
        # 
        # - To match all incoming requests, set the value to `true`.
        # 
        # - To match specific requests, set the value to a custom expression, such as `(http.host eq "video.example.com")`.
        self.rule = rule
        # Specifies whether the rule is enabled. This parameter is not required when you configure global settings. Valid values:
        # 
        # - `on`: Enabled.
        # 
        # - `off`: Disabled.
        self.rule_enable = rule_enable
        # The name of the rule. This parameter is not required when you configure global settings.
        self.rule_name = rule_name
        # The execution priority of the rule. This parameter is optional. If you do not specify this parameter, rules are executed in the order they are listed. If specified, the value must be an integer greater than 0. A larger value indicates a higher priority.
        self.sequence = sequence
        # Specifies whether to stop processing subsequent rules after this rule is matched.
        # 
        # - `true`: Stop processing subsequent rules.
        # 
        # - `false`: Continue processing subsequent rules. This is the default value.
        self.terminates = terminates

    def validate(self):
        if self.fixed_response:
            self.fixed_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fixed_response is not None:
            result['FixedResponse'] = self.fixed_response.to_map()

        if self.overrides is not None:
            result['Overrides'] = self.overrides

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.rule_enable is not None:
            result['RuleEnable'] = self.rule_enable

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.terminates is not None:
            result['Terminates'] = self.terminates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedResponse') is not None:
            temp_model = main_models.UpdateLoadBalancerRequestRulesFixedResponse()
            self.fixed_response = temp_model.from_map(m.get('FixedResponse'))

        if m.get('Overrides') is not None:
            self.overrides = m.get('Overrides')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('RuleEnable') is not None:
            self.rule_enable = m.get('RuleEnable')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('Terminates') is not None:
            self.terminates = m.get('Terminates')

        return self

class UpdateLoadBalancerRequestRulesFixedResponse(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        location: str = None,
        message_body: str = None,
        status_code: int = None,
    ):
        # The value of the `Content-Type` field in the HTTP response header.
        self.content_type = content_type
        # The value of the `Location` field in the HTTP response header. This is typically used for redirections.
        self.location = location
        # The content of the response body.
        self.message_body = message_body
        # The HTTP status code of the response.
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.location is not None:
            result['Location'] = self.location

        if self.message_body is not None:
            result['MessageBody'] = self.message_body

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('MessageBody') is not None:
            self.message_body = m.get('MessageBody')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class UpdateLoadBalancerRequestRandomSteering(DaraModel):
    def __init__(
        self,
        default_weight: int = None,
        pool_weights: Dict[str, int] = None,
    ):
        # The default weight applied to all address pools that do not have a specific weight defined. The value must be an integer from 0 to 100, inclusive.
        self.default_weight = default_weight
        # A map of pool IDs to their corresponding weights. These weights determine the proportion of traffic routed to each backend server pool.
        self.pool_weights = pool_weights

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_weight is not None:
            result['DefaultWeight'] = self.default_weight

        if self.pool_weights is not None:
            result['PoolWeights'] = self.pool_weights

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultWeight') is not None:
            self.default_weight = m.get('DefaultWeight')

        if m.get('PoolWeights') is not None:
            self.pool_weights = m.get('PoolWeights')

        return self

class UpdateLoadBalancerRequestMonitor(DaraModel):
    def __init__(
        self,
        consecutive_down: int = None,
        consecutive_up: int = None,
        expected_codes: str = None,
        follow_redirects: bool = None,
        header: Any = None,
        interval: int = None,
        method: str = None,
        monitoring_region: str = None,
        path: str = None,
        port: int = None,
        timeout: int = None,
        type: str = None,
    ):
        # The number of consecutive failed health checks required to declare an origin server unhealthy. For example, `5`.
        self.consecutive_down = consecutive_down
        # The number of consecutive successful health checks required to declare an origin server healthy. For example, `3`.
        self.consecutive_up = consecutive_up
        # The expected HTTP status codes that indicate a healthy response. For example, `200,202`.
        self.expected_codes = expected_codes
        # Specifies whether the health check monitor follows HTTP redirections.
        # 
        # - `true`: The monitor follows HTTP redirections.
        # 
        # - `false`: The monitor does not follow HTTP redirections.
        self.follow_redirects = follow_redirects
        # The HTTP request headers to send with each health check.
        self.header = header
        # The interval in seconds between each health check. For example, `60`.
        self.interval = interval
        # The HTTP method to use for the health check. For example, `GET`.
        self.method = method
        # The regions from which the health checks are performed. The default value is `Global`.
        # 
        # - `Global`: From probe locations worldwide.
        # 
        # - `ChineseMainland`: From probe locations within the Chinese mainland.
        # 
        # - `OutsideChineseMainland`: From probe locations outside the Chinese mainland.
        self.monitoring_region = monitoring_region
        # The path on the origin server to request for the health check. For example, `/healthcheck`.
        self.path = path
        # The port on the origin server to use for the health check.
        self.port = port
        # The timeout for the health check, in seconds. The value must be between 1 and 10, inclusive.
        self.timeout = timeout
        # The protocol to use for the health check, such as `HTTP`. If you set this to `off`, no health check is performed.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consecutive_down is not None:
            result['ConsecutiveDown'] = self.consecutive_down

        if self.consecutive_up is not None:
            result['ConsecutiveUp'] = self.consecutive_up

        if self.expected_codes is not None:
            result['ExpectedCodes'] = self.expected_codes

        if self.follow_redirects is not None:
            result['FollowRedirects'] = self.follow_redirects

        if self.header is not None:
            result['Header'] = self.header

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.method is not None:
            result['Method'] = self.method

        if self.monitoring_region is not None:
            result['MonitoringRegion'] = self.monitoring_region

        if self.path is not None:
            result['Path'] = self.path

        if self.port is not None:
            result['Port'] = self.port

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsecutiveDown') is not None:
            self.consecutive_down = m.get('ConsecutiveDown')

        if m.get('ConsecutiveUp') is not None:
            self.consecutive_up = m.get('ConsecutiveUp')

        if m.get('ExpectedCodes') is not None:
            self.expected_codes = m.get('ExpectedCodes')

        if m.get('FollowRedirects') is not None:
            self.follow_redirects = m.get('FollowRedirects')

        if m.get('Header') is not None:
            self.header = m.get('Header')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('MonitoringRegion') is not None:
            self.monitoring_region = m.get('MonitoringRegion')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateLoadBalancerRequestAdaptiveRouting(DaraModel):
    def __init__(
        self,
        failover_across_pools: bool = None,
        origin_level_retry: bool = None,
    ):
        # Specifies whether to perform origin-pull across address pools.
        # 
        # - `true`: Enables origin-pull across address pools.
        # 
        # - `false`: Disables origin-pull across address pools.
        self.failover_across_pools = failover_across_pools
        self.origin_level_retry = origin_level_retry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failover_across_pools is not None:
            result['FailoverAcrossPools'] = self.failover_across_pools

        if self.origin_level_retry is not None:
            result['OriginLevelRetry'] = self.origin_level_retry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailoverAcrossPools') is not None:
            self.failover_across_pools = m.get('FailoverAcrossPools')

        if m.get('OriginLevelRetry') is not None:
            self.origin_level_retry = m.get('OriginLevelRetry')

        return self

