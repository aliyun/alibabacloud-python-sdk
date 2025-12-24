# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rules: main_models.DescribeRulesResponseBodyRules = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The forwarding rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            self.rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rules') is not None:
            temp_model = main_models.DescribeRulesResponseBodyRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        return self

class DescribeRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribeRulesResponseBodyRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for v1 in self.rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rule'] = []
        if self.rule is not None:
            for k1 in self.rule:
                result['Rule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.DescribeRulesResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribeRulesResponseBodyRulesRule(DaraModel):
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
        listener_sync: str = None,
        rule_id: str = None,
        rule_name: str = None,
        scheduler: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        unhealthy_threshold: int = None,
        url: str = None,
        vserver_group_id: str = None,
    ):
        # The cookie that is configured on the backend server.
        # 
        # The value must be 1 to 200 characters in length, and can contain only ASCII letters and digits. It cannot contain commas (,), semicolons (;), or spaces. It cannot start with a dollar sign ($).
        # 
        # >  If you set the **StickySession** parameter to **on** and the **StickySessionType** parameter to **server**, this parameter is required.
        self.cookie = cookie
        # The timeout period of a cookie. Valid values: **1 to 86400**. Unit: seconds.
        # 
        # >  If you set the **StickySession** parameter to **on** and the **StickySessionType** parameter to **insert**, this parameter is required.
        self.cookie_timeout = cookie_timeout
        # The requested domain name specified in the forwarding rule.
        self.domain = domain
        # Indicates whether health checks are enabled.
        # 
        # Valid values: **on** and **off**.
        # 
        # >  If you set the **ListenerSync** parameter to **off**, this parameter is required. If you set the parameter to **on**, the configuration of the listener is used.
        self.health_check = health_check
        # The backend port that is used for health checks.
        # 
        # Valid values: **1 to 65535**.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required. If this parameter is empty but **HealthCheck** is set to **on**, the listener port is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$_ip**: The private IP address of the backend server.
        # 
        #     If you do not set this parameter or set the parameter to $_ip, the SLB instance uses the private IP address of each backend server as the domain name for health checks.
        # 
        # *   **domain**: The domain name must be 1 to 80 characters in length. The domain name can contain only letters, digits, periods (.),and hyphens (-).
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.health_check_domain = health_check_domain
        # The HTTP status code that indicates a successful health check. Multiple HTTP status codes are separated by commas (,). Default value: **http_2xx**.
        # 
        # Valid values: **http_2xx**, **http_3xx**, **http_4xx**, and **http_5xx**.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.health_check_http_code = health_check_http_code
        # The time interval between two consecutive health checks.
        # 
        # Valid values: **1 to 50**. Unit: seconds.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.health_check_interval = health_check_interval
        # The timeout period of a health check response. If a backend ECS instance does not respond within the specified timeout period, the ECS instance fails the health check. Unit: seconds
        # 
        # Valid values: **1 to 300**.
        # 
        # >  When you set the **HealthCheck** parameter to **on**, this parameter takes effect.
        self.health_check_timeout = health_check_timeout
        # The URI that is used for health checks.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.health_check_uri = health_check_uri
        # Specifies the number of successful health checks that must be consecutively performed before a backend server can be declared healthy (from **fail** to **success**).
        # 
        # Valid values: **2 to 10**.
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.healthy_threshold = healthy_threshold
        # Indicates whether the forwarding rule uses the scheduling algorithm, session persistence, and health check configurations of the listener.
        # 
        # Valid values: **on** and **off**.
        # 
        # *   **off**: does not use the configurations of the listener. You can customize health check and session persistence configurations for the forwarding rule.
        # *   **on**: uses the configurations of the listener.
        self.listener_sync = listener_sync
        # The ID of the forwarding rule.
        self.rule_id = rule_id
        # The name of the forwarding rule. The name must be 1 to 80 characters in length, and can contain only letters, digits, hyphens (-), forward slashes (/), periods (.),and underscores (_).
        # 
        # >  The name of each forwarding rule must be unique within a listener.
        self.rule_name = rule_name
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr** (default): Backend servers that have higher weights receive more requests than backend servers that have lower weights.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        # 
        # >  If you set the **ListenerSync** parameter to **off**, this parameter is required. If you set the parameter to **on**, the configuration of the listener is used.
        self.scheduler = scheduler
        # Specifies whether to enable session persistence.
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
        # Specifies the number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy (from **success** to **fail**).
        # 
        # Valid values: **2 to 10**
        # 
        # >  If you set the **HealthCheck** parameter to **on**, this parameter is required.
        self.unhealthy_threshold = unhealthy_threshold
        # The requested path specified in the forwarding rule.
        self.url = url
        # The ID of the destination vServer group specified in the forwarding rule.
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

        if self.listener_sync is not None:
            result['ListenerSync'] = self.listener_sync

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

        if m.get('ListenerSync') is not None:
            self.listener_sync = m.get('ListenerSync')

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

