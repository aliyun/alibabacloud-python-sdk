# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetLoadBalancerResponseBody(DaraModel):
    def __init__(
        self,
        adaptive_routing: main_models.GetLoadBalancerResponseBodyAdaptiveRouting = None,
        default_pools: List[int] = None,
        description: str = None,
        enabled: bool = None,
        fallback_pool: int = None,
        id: int = None,
        monitor: main_models.GetLoadBalancerResponseBodyMonitor = None,
        name: str = None,
        random_steering: main_models.GetLoadBalancerResponseBodyRandomSteering = None,
        region_pools: Any = None,
        request_id: str = None,
        rules: List[main_models.GetLoadBalancerResponseBodyRules] = None,
        session_affinity: str = None,
        site_id: int = None,
        status: str = None,
        steering_policy: str = None,
        sub_region_pools: Any = None,
        ttl: int = None,
    ):
        # Cross-pool failover configuration.
        self.adaptive_routing = adaptive_routing
        # List of default pool IDs.
        self.default_pools = default_pools
        # Description of the load balancer.
        self.description = description
        # Whether the load balancer is enabled.
        # 
        # - true: Enabled.
        # - false: Not enabled.
        self.enabled = enabled
        # The fallback pool ID, to which traffic will be redirected if all other pools are unavailable.
        self.fallback_pool = fallback_pool
        # The unique identifier ID of the load balancer.
        self.id = id
        # Monitor configuration.
        self.monitor = monitor
        # The name of the load balancer.
        self.name = name
        # Weighted round-robin configuration, used to control the traffic distribution weights among different pools.
        self.random_steering = random_steering
        # Address pools corresponding to primary regions.
        self.region_pools = region_pools
        # Request ID.
        self.request_id = request_id
        # A list of rule configurations, used to define behavior under specific conditions.
        self.rules = rules
        # Session persistence, with values:
        # - off: Not enabled.
        # - ip: Session persistence by IP.
        # - cookie: Session persistence by cookie.
        self.session_affinity = session_affinity
        # The site ID to which the load balancer belongs.
        self.site_id = site_id
        # The status of the load balancer.
        self.status = status
        # Load balancing policy.
        self.steering_policy = steering_policy
        # Address pools corresponding to secondary regions. When multiple secondary regions share a set of address pools, the keys can be concatenated with commas.
        self.sub_region_pools = sub_region_pools
        # TTL value, the time-to-live for DNS records, with a default of 30 seconds.
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

        if self.name is not None:
            result['Name'] = self.name

        if self.random_steering is not None:
            result['RandomSteering'] = self.random_steering.to_map()

        if self.region_pools is not None:
            result['RegionPools'] = self.region_pools

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.session_affinity is not None:
            result['SessionAffinity'] = self.session_affinity

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.status is not None:
            result['Status'] = self.status

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
            temp_model = main_models.GetLoadBalancerResponseBodyAdaptiveRouting()
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
            temp_model = main_models.GetLoadBalancerResponseBodyMonitor()
            self.monitor = temp_model.from_map(m.get('Monitor'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RandomSteering') is not None:
            temp_model = main_models.GetLoadBalancerResponseBodyRandomSteering()
            self.random_steering = temp_model.from_map(m.get('RandomSteering'))

        if m.get('RegionPools') is not None:
            self.region_pools = m.get('RegionPools')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.GetLoadBalancerResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('SessionAffinity') is not None:
            self.session_affinity = m.get('SessionAffinity')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SteeringPolicy') is not None:
            self.steering_policy = m.get('SteeringPolicy')

        if m.get('SubRegionPools') is not None:
            self.sub_region_pools = m.get('SubRegionPools')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

class GetLoadBalancerResponseBodyRules(DaraModel):
    def __init__(
        self,
        fixed_response: main_models.GetLoadBalancerResponseBodyRulesFixedResponse = None,
        overrides: Any = None,
        rule: str = None,
        rule_enable: str = None,
        rule_name: str = None,
        sequence: int = None,
        terminates: bool = None,
    ):
        # Executes a specified response after matching the rule.
        self.fixed_response = fixed_response
        # Modifies the load balancer configuration for the corresponding request after matching the rule. The fields in this configuration will override the corresponding fields in the load balancer\\"s configuration.
        self.overrides = overrides
        # Rule content, using conditional expressions to match user requests. This parameter is not required when adding global configurations. There are two usage scenarios:
        # - Match all incoming requests: Set the value to true
        # - Match specific requests: Set the value to a custom expression, for example: (http.host eq \\"video.example.com\\")
        self.rule = rule
        # Rule switch. This parameter is not required when adding global configurations. Possible values:
        # - on: Enabled.
        # - off: Disabled.
        self.rule_enable = rule_enable
        # Rule name. This parameter is not required when adding global configurations.
        self.rule_name = rule_name
        # Rule execution order. The higher the number, the higher the priority.
        self.sequence = sequence
        # Whether to terminate the execution of subsequent rules.
        # 
        # - true: Yes.
        # - false: No, default value.
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
            temp_model = main_models.GetLoadBalancerResponseBodyRulesFixedResponse()
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

class GetLoadBalancerResponseBodyRulesFixedResponse(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        location: str = None,
        message_body: str = None,
        status_code: int = None,
    ):
        # The Content-Type field in the HTTP Header.
        self.content_type = content_type
        # The location field in the HTTP response.
        self.location = location
        # The body value of the response.
        self.message_body = message_body
        # Status code.
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

class GetLoadBalancerResponseBodyRandomSteering(DaraModel):
    def __init__(
        self,
        default_weight: int = None,
        pool_weights: Dict[str, int] = None,
    ):
        # The default round-robin weight, used for all pools that do not have individually specified weights. The value range is 0-100.
        self.default_weight = default_weight
        # Weight configurations for each backend server pool, where the key is the pool ID and the value is the weight coefficient. The weight coefficient represents the relative traffic distribution ratio.
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

class GetLoadBalancerResponseBodyMonitor(DaraModel):
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
        # The number of consecutive failed probes required to consider the target as unhealthy, for example, `5`.
        self.consecutive_down = consecutive_down
        # The number of consecutive successful probes required to consider the target as healthy, for example, `3`.
        self.consecutive_up = consecutive_up
        # Expected status codes, such as 200, 202, for successful HTTP responses.
        self.expected_codes = expected_codes
        # Whether to follow redirects.
        # 
        # - true: Yes.
        # - false: No.
        self.follow_redirects = follow_redirects
        # The HTTP headers to be included in the probe request.
        self.header = header
        # Health check interval, in seconds.
        self.interval = interval
        # Health check method.
        self.method = method
        self.monitoring_region = monitoring_region
        # Path.
        self.path = path
        # Target port.
        self.port = port
        # The timeout for the health check, in seconds.
        self.timeout = timeout
        # Monitor protocol type, such as HTTP, used for health checks. When the value is `off`, it indicates that no check is performed.
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

class GetLoadBalancerResponseBodyAdaptiveRouting(DaraModel):
    def __init__(
        self,
        failover_across_pools: bool = None,
    ):
        # Whether to fail over across pools.
        # 
        # - true: Yes.
        # - false: No.
        self.failover_across_pools = failover_across_pools

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failover_across_pools is not None:
            result['FailoverAcrossPools'] = self.failover_across_pools

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailoverAcrossPools') is not None:
            self.failover_across_pools = m.get('FailoverAcrossPools')

        return self

