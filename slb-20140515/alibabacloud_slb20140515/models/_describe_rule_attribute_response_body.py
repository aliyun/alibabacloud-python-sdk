# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRuleAttributeResponseBody(DaraModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        domain: str = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_timeout: int = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        listener_port: str = None,
        listener_sync: str = None,
        load_balancer_id: str = None,
        request_id: str = None,
        rule_id: str = None,
        rule_name: str = None,
        scheduler: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        unhealthy_threshold: int = None,
        url: str = None,
        vserver_group_id: str = None,
    ):
        # The cookie to be configured on the backend server.
        # 
        # The cookie must be 1 to 200 characters in length and can contain ASCII letters and digits. It cannot contain commas (,), semicolons (;), or whitespace characters. It cannot start with a dollar sign ($).
        # 
        # If you set the **StickySession** parameter to **on** and the **StickySessionType** parameter to **server**, this parameter is required.
        self.cookie = cookie
        # The timeout period of a cookie.
        # 
        # Valid values: **1 to 86400**. Unit: seconds.
        # 
        # >  If you set the **StickySession** parameter to **on** and the **StickySessionType** parameter to **insert**, this parameter is required.
        self.cookie_timeout = cookie_timeout
        # The domain name that is configured in the forwarding rule.
        self.domain = domain
        # Specifies whether to enable health checks.
        # 
        # Valid values: **on** and **off**.
        # 
        # >  If you set the **ListenerSync** parameter to **off**, this parameter is required. If you set the parameter to **on**, the configuration of the listener is used.
        self.health_check = health_check
        # The backend port that is used for health checks.
        # 
        # Valid values: **1** to **65535**.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required. If this parameter is empty but **HealthCheck** is set to **on**, the listener port is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$_ip**: The private IP address of the backend server. If the $_ip parameter is set or the HealthCheckDomain parameter is not set, SLB uses the private IP addresses of backend servers as the domain names for health checks.
        # *   **domain**: The domain name must be 1 to 80 characters in length. It can contain only letters, digits, periods (.),and hyphens (-).
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.health_check_domain = health_check_domain
        # The HTTP status code that indicates a successful health check. Separate multiple HTTP status codes with commas (,). Default value: **http_2xx**.
        # 
        # Valid values: **http_2xx**, **http_3xx**, **http_4xx**, and **http_5xx**.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.health_check_http_code = health_check_http_code
        # The time interval between two consecutive health checks.
        # 
        # Valid values: **1** to **50**. Unit: seconds.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.health_check_interval = health_check_interval
        # The timeout period of a health check response. If a backend ECS instance does not respond within the specified timeout period, the ECS instance fails the health check.
        # 
        # Valid values: **1** to **300**. Unit: seconds.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.health_check_timeout = health_check_timeout
        # The URI that is used for health checks.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.health_check_uri = health_check_uri
        # The number of consecutive successful health checks that must occur before an unhealthy backend server is declared healthy. In this case, the health check state is changed from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.healthy_threshold = healthy_threshold
        # The listener port that is used by the SLB instance.
        self.listener_port = listener_port
        # Indicates whether the forwarding rule uses the scheduling algorithm, session persistence, and health check configurations of the listener.
        # 
        # Valid values: **on** and **off**.
        # 
        # *   **off**: does not use the configurations of the listener. You can customize health check and session persistence configurations for the forwarding rule.
        # *   **on**: uses the configurations of the listener.
        self.listener_sync = listener_sync
        # The ID of the SLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the forwarding rule.
        self.rule_id = rule_id
        # The name of the forwarding rule.
        self.rule_name = rule_name
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr** (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        # 
        # >  If you set the **ListenerSync** parameter to **off**, this parameter is required. If you set the parameter to **on**, the configuration of the listener is used.
        self.scheduler = scheduler
        # Indicates whether session persistence is enabled.
        # 
        # Valid values: **on** and **off**.
        # 
        # >  If you set the **ListenerSync** parameter to **off**, this parameter is required. If you set the parameter to **on**, the configuration of the listener is used.
        self.sticky_session = sticky_session
        # The method that is used to handle a cookie. Valid values:
        # 
        # *   **insert**: inserts a cookie into the response. SLB inserts a cookie (SERVERID) into the first HTTP or HTTPS response packet that is sent to a client. The next request from the client will contain this cookie, and the listener will distribute this request to the recorded backend server.
        # *   **server**: rewrites a cookie. When SLB detects a user-defined cookie, SLB overwrites the original cookie with the user-defined cookie. The next request from the client contains the user-defined cookie, and the listener distributes the request to the recorded backend server.
        # 
        # >  If you set the **StickySession** parameter to **on**, this parameter is required.
        self.sticky_session_type = sticky_session_type
        # The number of consecutive failed health checks that must occur before a healthy backend server is declared unhealthy. In this case, the health check state is changed from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.unhealthy_threshold = unhealthy_threshold
        # The URL that is configured in the forwarding rule.
        self.url = url
        # The ID of the vServer group that is associated with the forwarding rule.
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cookie is not None:
            result['Cookie'] = self.cookie

        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain

        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout

        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_sync is not None:
            result['ListenerSync'] = self.listener_sync

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        if self.url is not None:
            result['Url'] = self.url

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')

        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')

        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerSync') is not None:
            self.listener_sync = m.get('ListenerSync')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self

