# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetRuleRequest(DaraModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_timeout: int = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        listener_sync: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rule_id: str = None,
        rule_name: str = None,
        scheduler: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        unhealthy_threshold: int = None,
        vserver_group_id: str = None,
    ):
        # The cookie that is configured on the server.
        # 
        # The cookie must be 1 to 200 characters in length and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($).
        # 
        # >  This parameter is required and takes effect if **StickySession** is set to **on** and **StickySessionType** is set to **server**.
        self.cookie = cookie
        # The timeout period of a cookie. Unit: seconds. Valid values: **1** to **86400**.
        # 
        # >  This parameter is required and takes effect if **StickySession** is set to **on** and **StickySessionType** is set to **insert**.
        self.cookie_timeout = cookie_timeout
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        # 
        # >  This parameter is required and takes effect if the **ListenerSync** parameter is set to **off**.
        self.health_check = health_check
        # The port that is used for health checks. Valid values: **1** to **65535**.
        # 
        # >  This parameter takes effect when the **HealthCheck** parameter is set to **on**.
        self.health_check_connect_port = health_check_connect_port
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$_ip**: the private IP address of a backend server. If you do not set this parameter or set the parameter to $_ip, the SLB instance uses the private IP address of each backend server for health checks.
        # *   **domain**: The domain name must be 1 to 80 characters in length, and can contain letters, digits, periods (.), and hyphens (-).
        # 
        # >  This parameter takes effect if the **HealthCheck** parameter is set to **on**.
        self.health_check_domain = health_check_domain
        # The HTTP status code for a successful health check. Multiple HTTP status codes are separated by commas (,).
        # 
        # Valid values: **http_2xx**, **http_3xx**, **http_4xx**, and **http_5xx**.
        # 
        # >  This parameter is required and takes effect if the **HealthCheck** parameter is set to **on**.
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Unit: seconds. Valid values: **1** to **50**.
        # 
        # >  This parameter is required and takes effect if the **HealthCheck** parameter is set to **on**.
        self.health_check_interval = health_check_interval
        # The timeout period of a health check response. If a backend server, such as an Elastic Compute Service (ECS) instance, does not return a health check response within the specified timeout period, the server fails the health check. Unit: seconds. Valid values: **1** to **300**.
        # 
        # >  This parameter is required and takes effect if the **HealthCheck** parameter is set to **on**.
        self.health_check_timeout = health_check_timeout
        # The URI that is used for health checks.
        # 
        # >  This parameter is required and takes effect if the **HealthCheck** parameter is set to **on**.
        self.health_check_uri = health_check_uri
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        # 
        # >  This parameter is required and takes effect if the **HealthCheck** parameter is set to **on**.
        self.healthy_threshold = healthy_threshold
        # Specifies whether to use the scheduling algorithm, session persistence, and health check configurations of the listener. Valid values:
        # 
        # *   **on**: uses the configurations of the listener.
        # *   **off**: does not use the configurations of the listener. You can customize the health check and session persistence configurations for the forwarding rule.
        self.listener_sync = listener_sync
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the Classic Load Balancer (CLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the forwarding rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the forwarding rule. The name must be 1 to 40 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        # 
        # > On the same listener, the forwarding rule names must be unique.
        self.rule_name = rule_name
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr**: Backend servers with higher weights receive more requests than those with lower weights.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        # 
        # >  This parameter is required and takes effect if the **ListenerSync** parameter is set to **off**.
        self.scheduler = scheduler
        # Specifies whether to enable session persistence. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        # 
        # This parameter is required and takes effect if the **ListenerSync** parameter is set to **off**.
        self.sticky_session = sticky_session
        # The method that is used to handle a cookie. Valid values:
        # 
        # *   **insert**: inserts a cookie.
        # 
        #     CLB inserts the backend server ID as a cookie into the first HTTP or HTTPS response that is sent to a client. The next request from the client will contain this cookie, and the listener will distribute this request to the recorded backend server.
        # 
        # *   **server**: rewrites a cookie.
        # 
        #     When CLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client will contain the user-defined cookie, and the listener will distribute this request to the recorded backend server.
        # 
        # >  This parameter is required and takes effect if the **StickySession** parameter is set to **on**.
        self.sticky_session_type = sticky_session_type
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        # 
        # >  This parameter is required and takes effect if the **HealthCheck** parameter is set to **on**.
        self.unhealthy_threshold = unhealthy_threshold
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

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

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

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

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

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

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

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self

