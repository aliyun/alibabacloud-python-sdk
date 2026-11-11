# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateLoadBalancerRequest(DaraModel):
    def __init__(
        self,
        adaptive_routing: main_models.CreateLoadBalancerRequestAdaptiveRouting = None,
        default_pools: List[int] = None,
        description: str = None,
        enabled: bool = None,
        fallback_pool: int = None,
        monitor: main_models.CreateLoadBalancerRequestMonitor = None,
        name: str = None,
        random_steering: main_models.CreateLoadBalancerRequestRandomSteering = None,
        region_pools: Any = None,
        rules: List[main_models.CreateLoadBalancerRequestRules] = None,
        session_affinity: str = None,
        site_id: int = None,
        steering_policy: str = None,
        sub_region_pools: Any = None,
        ttl: int = None,
    ):
        # The back-to-origin configuration across origin address pools.
        self.adaptive_routing = adaptive_routing
        # The list of default address pools.
        # 
        # This parameter is required.
        self.default_pools = default_pools
        # The detailed description of the load balancer for easy management and identification.
        self.description = description
        # Specifies whether the load balancer is enabled. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        self.enabled = enabled
        # The ID of the fallback address pool. Traffic is routed to this pool when all other pools are unavailable.
        # 
        # This parameter is required.
        self.fallback_pool = fallback_pool
        # The monitor configuration for health checks.
        # 
        # This parameter is required.
        self.monitor = monitor
        # The name of the load balancer. The name must pass the domain name format validation and be a subdomain of the site.
        # 
        # This parameter is required.
        self.name = name
        # The weighted round-robin configuration used to control the traffic distribution weights of different address pools.
        self.random_steering = random_steering
        # The address pools corresponding to primary regions.
        self.region_pools = region_pools
        # The rule information.
        self.rules = rules
        # The session persistence configuration. Valid values:
        # - off: Disabled.
        # - ip: Session persistence based on IP addresses.
        # - cookie: Session persistence based on cookies.
        # - http_header: Session persistence based on HTTP headers.
        self.session_affinity = session_affinity
        # The site ID. You can obtain the site ID by calling the [ListSites](~~ListSites~~) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The load balancing policy. Valid values:
        # - geo: Geolocation-based policy.
        # - random: Weighted round-robin.
        # - order: Active/standby mode.
        # 
        # This parameter is required.
        self.steering_policy = steering_policy
        # The address pools corresponding to secondary regions. When multiple secondary regions share the same set of address pools, you can concatenate the secondary regions with commas (,) to use as the key.
        self.sub_region_pools = sub_region_pools
        # The time-to-live (TTL) value of the DNS record. Default value: 30. Unit: seconds. Valid values: 10 to 600.
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

        if self.monitor is not None:
            result['Monitor'] = self.monitor.to_map()

        if self.name is not None:
            result['Name'] = self.name

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
            temp_model = main_models.CreateLoadBalancerRequestAdaptiveRouting()
            self.adaptive_routing = temp_model.from_map(m.get('AdaptiveRouting'))

        if m.get('DefaultPools') is not None:
            self.default_pools = m.get('DefaultPools')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('FallbackPool') is not None:
            self.fallback_pool = m.get('FallbackPool')

        if m.get('Monitor') is not None:
            temp_model = main_models.CreateLoadBalancerRequestMonitor()
            self.monitor = temp_model.from_map(m.get('Monitor'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RandomSteering') is not None:
            temp_model = main_models.CreateLoadBalancerRequestRandomSteering()
            self.random_steering = temp_model.from_map(m.get('RandomSteering'))

        if m.get('RegionPools') is not None:
            self.region_pools = m.get('RegionPools')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.CreateLoadBalancerRequestRules()
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

class CreateLoadBalancerRequestRules(DaraModel):
    def __init__(
        self,
        fixed_response: main_models.CreateLoadBalancerRequestRulesFixedResponse = None,
        overrides: Any = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        terminates: bool = None,
    ):
        # The specified content to return in the response after a rule is matched.
        self.fixed_response = fixed_response
        # The load balancing configuration modified for the corresponding request rewrite after a rule is matched. The configured fields override the corresponding fields in the load balancer configuration.
        self.overrides = overrides
        # The content of the rule. A conditional expression is used to match user requests. You do not need to set this parameter when adding a global configuration. Two scenarios are supported:
        # - Match all incoming requests: Set the value to true.
        # - Match specific requests: Set the value to a custom expression, such as (http.host eq "video.example.com").
        self.rule = rule
        # The rule switch. You do not need to set this parameter when adding a global configuration. Valid values:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # The name of the rule. You do not need to set this parameter when adding a global configuration.
        self.rule_name = rule_name
        # The execution sequence of the rule. This parameter is optional. If you do not specify this parameter, rules are executed in the order they are listed. If you specify this parameter, the value must be an integer greater than 0. A larger value indicates a higher execution priority.
        self.sequence = sequence
        # Specifies whether to stop executing subsequent rules. Valid values:
        # - true: Yes.
        # - false: No. This is the default value.
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
            temp_model = main_models.CreateLoadBalancerRequestRulesFixedResponse()
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

class CreateLoadBalancerRequestRulesFixedResponse(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        location: str = None,
        message_body: str = None,
        status_code: int = None,
    ):
        # The Content-Type field in the HTTP header.
        self.content_type = content_type
        # The Location field in the HTTP response.
        self.location = location
        # The body value of the response.
        self.message_body = message_body
        # The response status code.
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

class CreateLoadBalancerRequestRandomSteering(DaraModel):
    def __init__(
        self,
        default_weight: int = None,
        pool_weights: Dict[str, int] = None,
    ):
        # The default round-robin weight for all address pools that do not have a specified weight. Valid values: integers from 0 to 100.
        self.default_weight = default_weight
        # The weight configuration for each backend server pool. The key is the pool ID and the value is the weight coefficient. The weight coefficient indicates the proportion of relative traffic distribution.
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

class CreateLoadBalancerRequestMonitor(DaraModel):
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
        # The number of consecutive failed probes required to determine a failed health check, such as `5`.
        self.consecutive_down = consecutive_down
        # The number of consecutive successful probes required to determine a successful health check, such as `3`.
        self.consecutive_up = consecutive_up
        # The expected status codes for successful HTTP responses, such as `200,202`.
        self.expected_codes = expected_codes
        # Specifies whether to follow redirects. Valid values:
        # - true: Yes.
        # - false: No.
        self.follow_redirects = follow_redirects
        # The HTTP headers included in the probe requests.
        self.header = header
        # The monitoring interval, such as `60` seconds. This parameter specifies the check frequency.
        self.interval = interval
        # The request method of the monitor, such as `GET` in the HTTP protocol.
        self.method = method
        # The region where the probe nodes are located. Default value: Global. Valid values:
        # - Global: Global.
        # - ChineseMainland: The Chinese mainland.
        # - OutsideChineseMainland: Global (excluding the Chinese mainland).
        self.monitoring_region = monitoring_region
        # The health check path of the monitor, such as `/healthcheck`, the URI of the request.
        self.path = path
        # The origin server port.
        self.port = port
        # The timeout period for health checks. Unit: seconds. Valid values: 1 to 10.
        self.timeout = timeout
        # The protocol type of the monitor for health checks, such as HTTP. A value of off indicates that health checks are disabled. Valid values:
        # - TCP
        # - UDP
        # - SMTP
        # - HTTPS
        # - HTTP
        # - ICMP Ping
        # - off
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

class CreateLoadBalancerRequestAdaptiveRouting(DaraModel):
    def __init__(
        self,
        failover_across_pools: bool = None,
        origin_level_retry: bool = None,
    ):
        # Specifies whether to route traffic back to the origin across origin address pools. Valid values:
        # - true: Yes.
        # - false: No.
        self.failover_across_pools = failover_across_pools
        # Specifies whether to retry the next IP address if a back-to-origin request fails, the origin server is a domain name, and the domain name is resolved to multiple IP addresses.
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

