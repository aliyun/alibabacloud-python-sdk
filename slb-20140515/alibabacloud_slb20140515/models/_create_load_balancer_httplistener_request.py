# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class CreateLoadBalancerHTTPListenerRequest(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
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
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        request_timeout: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheduler: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        tag: List[main_models.CreateLoadBalancerHTTPListenerRequestTag] = None,
        unhealthy_threshold: int = None,
        vserver_group_id: str = None,
        xforwarded_for: str = None,
        xforwarded_for_client_src_port: str = None,
        xforwarded_for_slbid: str = None,
        xforwarded_for_slbip: str = None,
        xforwarded_for_slbport: str = None,
        xforwarded_for_proto: str = None,
    ):
        # The ID of the network access control list (ACL) that is associated with the listener.
        # 
        # >  If **AclStatus** is set to **on**, this parameter is required.
        self.acl_id = acl_id
        # Specifies whether to enable access control. Valid values:
        # 
        # *   **on**: yes
        # *   **off** (default): no
        self.acl_status = acl_status
        # The type of access control. Valid values:
        # 
        # *   **white**: Only requests from IP addresses and CIDR blocks on the whitelist are forwarded by the listener. Your service may be adversely affected if the whitelist is not properly configured. If a whitelist is configured, the listener forwards only requests from IP addresses that are added to the whitelist.
        # 
        #     If you configure a whitelist but do not add an IP address to the whitelist, the listener forwards all requests.
        # 
        # *   **black**: Requests from the IP addresses and CIDR blocks on the blacklist are blocked.
        # 
        #     If you configure a blacklist but do not add an IP address to the blacklist, the listener forwards all requests.
        # 
        # >  When **AclStatus** is set to **on**, this parameter takes effect.
        self.acl_type = acl_type
        # The backend port that is used by the CLB instance.
        # 
        # Valid values: **1** to **65535**.
        # 
        # >  If the VServerGroupId parameter is not specified, this parameter is required.
        self.backend_server_port = backend_server_port
        # The maximum bandwidth of the listener. Unit: Mbit/s. Valid values:
        # 
        # **-1**: specifies that the bandwidth of the listener is unlimited.
        self.bandwidth = bandwidth
        # The cookie configured for the server.
        # 
        # The cookie must be 1 to 200 characters in length, and can contain only ASCII letters and digits. It cannot contain commas (,), semicolons (;), space characters, or start with a dollar sign ($).
        # 
        # >  This parameter is required when the **StickySession** parameter is set to **on** and the **StickySessionType** parameter is set to **server**.
        self.cookie = cookie
        # The timeout period of a cookie. Unit: seconds.
        # 
        # Valid values: **1** to **86400**.
        # 
        # >  If **StickySession** is set to **on** and **StickySessionType** is set to **insert**, this parameter is required.
        self.cookie_timeout = cookie_timeout
        # The name of the listener.
        # 
        # The name must be 1 to 256 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        self.description = description
        # The listening port that is used to redirect HTTP requests to HTTPS.
        self.forward_port = forward_port
        # Specifies whether to enable `GZIP` compression to compress specific types of files. Valid values:
        # 
        # *   **on** (default)
        # *   **off**
        self.gzip = gzip
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        # 
        # This parameter is required.
        self.health_check = health_check
        # The backend port that is used for health checks.
        # 
        # Valid values: **1** to **65535**.
        # 
        # >  This parameter takes effect only if the **HealthCheck** parameter is set to **on**.
        self.health_check_connect_port = health_check_connect_port
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$_ip**: the private IP address of a backend server. If an IP address is specified, or this parameter is not specified, the CLB instance uses the private IP address of each backend server as the domain name for health checks.
        # *   **domain**: The domain name must be 1 to 80 characters in length, and can contain letters, digits, periods (.), and hyphens (-).
        # 
        # >  This parameter takes effect only if the **HealthCheck** parameter is set to **on**.
        self.health_check_domain = health_check_domain
        # The HTTP status code for a successful health check. Separate multiple HTTP status codes with commas (,).
        # 
        # Valid values: **http_2xx** (default), **http_3xx**, **http_4xx**, and **http_5xx**.
        # 
        # >  This parameter takes effect only if the **HealthCheck** parameter is set to **on**.
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Unit: seconds.
        # 
        # Valid values: **1** to **50**.
        # 
        # >  This parameter takes effect only if the **HealthCheck** parameter is set to **on**.
        self.health_check_interval = health_check_interval
        # The health check method used in HTTP health checks. Valid values: **head** and **get**.
        # 
        # >  This parameter takes effect only if the **HealthCheck** parameter is set to **on**.
        self.health_check_method = health_check_method
        # The timeout period of a health check response. If a backend ECS instance does not respond within the specified timeout period, the ECS instance fails the health check. Unit: seconds
        # 
        # Valid values: **1** to **300**.
        # 
        # >  This parameter takes effect only if the **HealthCheck** parameter is set to **on**.
        self.health_check_timeout = health_check_timeout
        # The URI that is used for health checks.
        # 
        # The URI must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URI must start with a forward slash (/) but cannot be a single forward slash (/).
        # 
        # >  This parameter takes effect only if the **HealthCheck** parameter is set to **on**.
        self.health_check_uri = health_check_uri
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        # 
        # >  This parameter takes effect only if the **HealthCheck** parameter is set to **on**.
        self.healthy_threshold = healthy_threshold
        # The timeout period of an idle connection. Unit: seconds.
        # 
        # Default value: **15**. Valid values: **1** to **60**.
        # 
        # If no request is received within the specified timeout period, SLB closes the connection. When a request is received, SLB establishes a new connection.
        self.idle_timeout = idle_timeout
        # Specifies whether to enable HTTP-to-HTTPS redirection. Valid values:
        # 
        # *   **on**: yes
        # *   **off** (default): no
        self.listener_forward = listener_forward
        # The frontend port that is used by the CLB instance.
        # 
        # Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the CLB instance is deployed.
        # 
        # You can query the region ID from the [Regions and zones](https://help.aliyun.com/document_detail/40654.html) list or by calling the [DescribeRegions](https://help.aliyun.com/document_detail/27584.html) operation.
        self.region_id = region_id
        # The timeout period of a request. Unit: seconds.
        # 
        # Default value: **60**. Valid values: **1** to **180**.
        # 
        # If no response is received from the backend server within the specified timeout period, CLB sends an `HTTP 504` error code to the client.
        self.request_timeout = request_timeout
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr** (default): Backend servers with higher weights receive more requests than those with lower weights.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        self.scheduler = scheduler
        # Specifies whether to enable session persistence. Valid values:
        # 
        # *   **on**
        # *   **off** (default)
        self.sticky_session = sticky_session
        # The method that is used to handle cookies. Valid values:
        # 
        # *   **insert**: inserts a cookie.
        # 
        #     The first time a client accesses CLB, CLB inserts a cookie into the response packet. Subsequent requests from the client that carry the cookie are distributed to the same backend server as the first request.
        # 
        # *   **server**: rewrites the original cookie.
        # 
        #     CLB rewrites the custom cookies in requests from a client. Subsequent requests from the client that carry the new cookie are forwarded to the same backend server as the first request.
        # 
        # >  This parameter is required if the **StickySession** parameter is set to **on**.
        self.sticky_session_type = sticky_session_type
        # The tags.
        self.tag = tag
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        # 
        # >  This parameter takes effect only if the **HealthCheck** parameter is set to **on**.
        self.unhealthy_threshold = unhealthy_threshold
        # The ID of the vServer group.
        self.vserver_group_id = vserver_group_id
        # Specifies whether to use the `X-Forwarded-For` header to retrieve client IP addresses. Valid values:
        # 
        # *   **on** (default)
        # *   **off**
        self.xforwarded_for = xforwarded_for
        # Specifies whether to use the `XForwardedFor_ClientSrcPort` header to retrieve the client port. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_client_src_port = xforwarded_for_client_src_port
        # Specifies whether to use the `SLB-ID` header to retrieve the ID of the CLB instance. Valid values:
        # 
        # *   **on**
        # *   **off** (default)
        self.xforwarded_for_slbid = xforwarded_for_slbid
        # Specifies whether to use the `SLB-IP` header to retrieve the virtual IP address of the client. Valid values:
        # 
        # *   **on**
        # *   **off** (default)
        self.xforwarded_for_slbip = xforwarded_for_slbip
        # Specifies whether to use the `XForwardedFor_SLBPORT` header to retrieve the listener port of the CLB instance. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_slbport = xforwarded_for_slbport
        # Specifies whether to use the `X-Forwarded-Proto` header to retrieve the listener protocol. Valid values:
        # 
        # *   **on**
        # *   **off** (default)
        self.xforwarded_for_proto = xforwarded_for_proto

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
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

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

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateLoadBalancerHTTPListenerRequestTag()
                self.tag.append(temp_model.from_map(k1))

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

class CreateLoadBalancerHTTPListenerRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the bastion host. Valid values of N: **1 to 20**. The tag key cannot be an empty string.
        # 
        # The tag key can be at most 64 characters in length, and cannot contain `http://` or `https://`. It must not start with `aliyun` or `acs:`.
        self.key = key
        # The tag value. Valid values of N: **1 to 20**. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag value cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

