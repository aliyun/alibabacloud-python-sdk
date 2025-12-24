# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerHTTPListenerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_ids: main_models.DescribeLoadBalancerHTTPListenerAttributeResponseBodyAclIds = None,
        acl_status: str = None,
        acl_type: str = None,
        backend_server_port: int = None,
        bandwidth: int = None,
        cookie: str = None,
        cookie_timeout: int = None,
        description: str = None,
        forward_port: int = None,
        gzip: str = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        idle_timeout: int = None,
        listener_forward: str = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        request_id: str = None,
        request_timeout: int = None,
        rules: main_models.DescribeLoadBalancerHTTPListenerAttributeResponseBodyRules = None,
        scheduler: str = None,
        security_status: str = None,
        status: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        tags: main_models.DescribeLoadBalancerHTTPListenerAttributeResponseBodyTags = None,
        unhealthy_threshold: int = None,
        vserver_group_id: str = None,
        xforwarded_for: str = None,
        xforwarded_for_client_src_port: str = None,
        xforwarded_for_slbid: str = None,
        xforwarded_for_slbip: str = None,
        xforwarded_for_slbport: str = None,
        xforwarded_for_proto: str = None,
    ):
        # The ID of the network ACL that is associated with a listener.
        # 
        # > This parameter is returned when **AclStatus** is set to **on**.
        self.acl_id = acl_id
        # The ID of the access control list (ACL).
        self.acl_ids = acl_ids
        # Indicates whether access control is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.acl_status = acl_status
        # The type of the ACL. Valid values:
        # 
        # *   **white**: a whitelist. Only requests from the IP addresses or CIDR blocks in the ACL are forwarded. Whitelists apply to scenarios where you want to allow only specific IP addresses to access an application. Your service may be adversely affected if the whitelist is not properly configured. If a whitelist is configured, only requests from IP addresses that are added to the whitelist are forwarded by the listener.
        # 
        # If you enable a whitelist but do not add an IP address to the ACL, the listener forwards all requests.
        # 
        # *   **black**: a blacklist. All requests from the IP addresses or CIDR blocks in the network ACL are rejected. Blacklists apply to scenarios where you want to block access from specified IP addresses to an application.
        # 
        # If a blacklist is configured for a listener but no IP address is added to the blacklist, the listener forwards all requests.
        # 
        # > This parameter is required when **AclStatus** is set to **on**.
        self.acl_type = acl_type
        # The backend port that is used by the CLB instance.
        self.backend_server_port = backend_server_port
        # The maximum bandwidth of the listener. Unit: Mbit/s.
        # 
        # *   **-1**: If -1 is returned, it indicates that the bandwidth of the listener is unlimited.
        # *   **1 to 5120**: If a value from 1 to 5120 is returned, the value indicates the maximum bandwidth of the listener. The sum of the maximum bandwidth of all listeners added to a CLB instance does not exceed the maximum bandwidth of the CLB instance.
        self.bandwidth = bandwidth
        # The cookie that is configured on the server.
        self.cookie = cookie
        # The timeout period of a cookie. Unit: seconds.
        self.cookie_timeout = cookie_timeout
        # The name of the listener.
        self.description = description
        # The listener port that is used to redirect HTTP requests to HTTPS.
        # 
        # >  If the **ListenerForward** parameter is set to **off**, this parameter is not displayed.
        self.forward_port = forward_port
        # Indicates whether `Gzip` compression is enabled to compress specific types of files. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.gzip = gzip
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.health_check = health_check
        # The port that is used for health checks.
        # 
        # > This parameter takes effect only when **HealthCheck** is set to **on**.
        self.health_check_connect_port = health_check_connect_port
        # The domain name that you want to use for health checks.
        self.health_check_domain = health_check_domain
        # The HTTP status code for a successful health check.
        self.health_check_http_code = health_check_http_code
        # The interval at which health checks are performed. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The health check method used by HTTP listeners. Valid values: **head** and **get**.
        # 
        # > This parameter is returned when **HealthCheck** is set to **on**.
        self.health_check_method = health_check_method
        # The timeout period of each health check. Unit: seconds.
        self.health_check_timeout = health_check_timeout
        # The URL path that is used for health checks.
        # 
        # The URI must be 1 to 80 characters in length, and can contain only digits, letters, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URI must start with a forward slash (/) but cannot be a single forward slash (/).
        self.health_check_uri = health_check_uri
        # The healthy threshold.
        self.healthy_threshold = healthy_threshold
        # The timeout period of an idle connection. Unit: seconds.
        # 
        # Default value: **15**. Valid values: **1 to 60**.
        # 
        # If no request is received within the specified timeout period, CLB closes the connection. When a request is received, CLB establishes a new connection.
        self.idle_timeout = idle_timeout
        # Indicates whether HTTP-to-HTTPS redirection is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.listener_forward = listener_forward
        # The frontend port that is used by the CLB instance.
        self.listener_port = listener_port
        # The CLB instance ID.
        self.load_balancer_id = load_balancer_id
        # The request ID.
        self.request_id = request_id
        # The timeout period of a request. Unit: seconds.
        # 
        # Default value: **60**. Valid values: **1 to 180**.
        # 
        # If no response is received from a backend server within the specified timeout period, CLB returns the HTTP 504 status code to the client.
        self.request_timeout = request_timeout
        # The list of forwarding rules.
        self.rules = rules
        # The routing algorithm. Valid values:
        # 
        # *   **wrr**: Backend servers that have higher weights receive more requests than backend servers that have lower weights.
        # *   \\*\\* rr\\*\\*: Requests are sequentially distributed to backend servers.
        self.scheduler = scheduler
        # Indicates whether the listener is in the Secure state. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.security_status = security_status
        # The status of the listener. Valid values:
        # 
        # *   **running**
        # *   **stopped**
        self.status = status
        # Indicates whether session persistence is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.sticky_session = sticky_session
        # The method that is used to handle a cookie.
        # 
        # Valid values: **insert** and **server**.
        # 
        # *   **insert**: inserts a cookie.
        # 
        #     CLB inserts a session cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. Subsequent requests to CLB carry this cookie, and CLB determines the destination servers of the requests based on the cookies.
        # 
        # *   **server**: rewrites a cookie.
        # 
        #     When CLB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. The next request from the client carries the user-defined cookie, and the listener forwards this request to the recorded backend server.
        # 
        # > This parameter is required when **StickySession** is set to **on**.
        self.sticky_session_type = sticky_session_type
        # The tags.
        self.tags = tags
        # The unhealthy threshold.
        self.unhealthy_threshold = unhealthy_threshold
        # The ID of the associated server group.
        self.vserver_group_id = vserver_group_id
        # Indicates whether the `X-Forwarded-For` header is used to preserve the real IP address of the client. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for = xforwarded_for
        # Indicates whether the `XForwardedFor_ClientSrcPort` header is used to retrieve the client port. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_client_src_port = xforwarded_for_client_src_port
        # Indicates whether the `SLB-ID` header is used to retrieve the ID of the CLB instance. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_slbid = xforwarded_for_slbid
        # Indicates whether the `SLB-IP` header is used to retrieve the virtual IP address requested by the client. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_slbip = xforwarded_for_slbip
        # Indicates whether the `XForwardedFor_SLBPORT` header is used to retrieve the listener port of the CLB instance. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_slbport = xforwarded_for_slbport
        # Indicates whether the `X-Forwarded-Proto` header is used to retrieve the listener protocol. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_proto = xforwarded_for_proto

    def validate(self):
        if self.acl_ids:
            self.acl_ids.validate()
        if self.rules:
            self.rules.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids.to_map()

        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.cookie is not None:
            result['Cookie'] = self.cookie

        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout

        if self.description is not None:
            result['Description'] = self.description

        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port

        if self.gzip is not None:
            result['Gzip'] = self.gzip

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

        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method

        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout

        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.security_status is not None:
            result['SecurityStatus'] = self.security_status

        if self.status is not None:
            result['Status'] = self.status

        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for

        if self.xforwarded_for_client_src_port is not None:
            result['XForwardedFor_ClientSrcPort'] = self.xforwarded_for_client_src_port

        if self.xforwarded_for_slbid is not None:
            result['XForwardedFor_SLBID'] = self.xforwarded_for_slbid

        if self.xforwarded_for_slbip is not None:
            result['XForwardedFor_SLBIP'] = self.xforwarded_for_slbip

        if self.xforwarded_for_slbport is not None:
            result['XForwardedFor_SLBPORT'] = self.xforwarded_for_slbport

        if self.xforwarded_for_proto is not None:
            result['XForwardedFor_proto'] = self.xforwarded_for_proto

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclIds') is not None:
            temp_model = main_models.DescribeLoadBalancerHTTPListenerAttributeResponseBodyAclIds()
            self.acl_ids = temp_model.from_map(m.get('AclIds'))

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')

        if m.get('Gzip') is not None:
            self.gzip = m.get('Gzip')

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

        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')

        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')

        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('Rules') is not None:
            temp_model = main_models.DescribeLoadBalancerHTTPListenerAttributeResponseBodyRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('SecurityStatus') is not None:
            self.security_status = m.get('SecurityStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeLoadBalancerHTTPListenerAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')

        if m.get('XForwardedFor_ClientSrcPort') is not None:
            self.xforwarded_for_client_src_port = m.get('XForwardedFor_ClientSrcPort')

        if m.get('XForwardedFor_SLBID') is not None:
            self.xforwarded_for_slbid = m.get('XForwardedFor_SLBID')

        if m.get('XForwardedFor_SLBIP') is not None:
            self.xforwarded_for_slbip = m.get('XForwardedFor_SLBIP')

        if m.get('XForwardedFor_SLBPORT') is not None:
            self.xforwarded_for_slbport = m.get('XForwardedFor_SLBPORT')

        if m.get('XForwardedFor_proto') is not None:
            self.xforwarded_for_proto = m.get('XForwardedFor_proto')

        return self

class DescribeLoadBalancerHTTPListenerAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeLoadBalancerHTTPListenerAttributeResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeLoadBalancerHTTPListenerAttributeResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerHTTPListenerAttributeResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of tag N. Valid values of N: **1** to **20**. The tag value cannot be an empty string. The tag key can be up to 64 characters in length. The key cannot start with `acs:` or `aliyun` or contain `http://` or `https://`.
        self.tag_key = tag_key
        # The value of tag N. Valid values of N: **1** to **20**. The tag value can be an empty string. The tag value can be up to 128 characters in length, and cannot start with `acs:`. It cannot contain `http://` or `https://`.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeLoadBalancerHTTPListenerAttributeResponseBodyRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribeLoadBalancerHTTPListenerAttributeResponseBodyRulesRule] = None,
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
                temp_model = main_models.DescribeLoadBalancerHTTPListenerAttributeResponseBodyRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerHTTPListenerAttributeResponseBodyRulesRule(DaraModel):
    def __init__(
        self,
        domain: str = None,
        rule_id: str = None,
        rule_name: str = None,
        url: str = None,
        vserver_group_id: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The ID of the forwarding rule.
        self.rule_id = rule_id
        # The name of the forwarding rule.
        self.rule_name = rule_name
        # The request URL.
        self.url = url
        # The ID of the server group specified in the forwarding rule.
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.url is not None:
            result['Url'] = self.url

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self

class DescribeLoadBalancerHTTPListenerAttributeResponseBodyAclIds(DaraModel):
    def __init__(
        self,
        acl_id: List[str] = None,
    ):
        self.acl_id = acl_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        return self

