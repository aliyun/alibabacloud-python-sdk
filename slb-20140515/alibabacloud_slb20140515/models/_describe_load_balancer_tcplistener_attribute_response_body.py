# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerTCPListenerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_ids: main_models.DescribeLoadBalancerTCPListenerAttributeResponseBodyAclIds = None,
        acl_status: str = None,
        acl_type: str = None,
        backend_server_port: int = None,
        bandwidth: int = None,
        connection_drain: str = None,
        connection_drain_timeout: int = None,
        description: str = None,
        established_timeout: int = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        master_slave_server_group_id: str = None,
        persistence_timeout: int = None,
        proxy_protocol_v2enabled: bool = None,
        request_id: str = None,
        scheduler: str = None,
        status: str = None,
        syn_proxy: str = None,
        tags: main_models.DescribeLoadBalancerTCPListenerAttributeResponseBodyTags = None,
        unhealthy_threshold: int = None,
        vserver_group_id: str = None,
    ):
        # The ID of the network ACL that is associated with the listener.
        # 
        # If **AclStatus** is set to **on**, this parameter is returned.
        self.acl_id = acl_id
        # The IDs of the ACLs.
        self.acl_ids = acl_ids
        # Indicates whether access control is enabled. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        self.acl_status = acl_status
        # The type of the ACL. Valid values:
        # 
        # *   **white**: a whitelist. Only requests from the IP addresses or CIDR blocks in the network ACL are forwarded. Whitelists apply to scenarios in which you want to allow only specific IP addresses to access an application.
        # 
        #     Your service may be adversely affected if the whitelist is not properly configured. After a whitelist is configured, only requests from IP addresses that are added to the whitelist are forwarded by the listener.
        # 
        #     If you enable a whitelist but do not add an IP address to the ACL, the listener forwards all requests.
        # 
        # *   **black**: a blacklist. All requests from the IP addresses or CIDR blocks in the network ACL are rejected. Blacklists apply to scenarios in which you want to block access from specified IP addresses to an application.
        # 
        #     If a blacklist is configured for a listener but no IP address is added to the blacklist, the listener forwards all requests.
        # 
        # >  If **AclStatus** is set to **on**, this parameter is returned.
        self.acl_type = acl_type
        # The backend port used by the CLB instance.
        # 
        # >  If the listener is associated with a vServer group, this parameter is not returned.
        self.backend_server_port = backend_server_port
        # The maximum bandwidth of the listener. Unit: Mbit/s. Valid values:
        # 
        # *   **-1**: For a pay-by-data-transfer Internet-facing CLB instance, this parameter is set to -1. This indicates that the bandwidth of the listener is unlimited.
        # *   **1** to **5120**: For a pay-by-bandwidth Internet-facing CLB instance, you can specify the maximum bandwidth of each listener. The sum of maximum bandwidth of all listeners cannot exceed the maximum bandwidth of the CLB instance.
        self.bandwidth = bandwidth
        # Indicates whether connection draining is enabled. If **ConnectionDrain** is set to **on**, the parameter is returned. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        self.connection_drain = connection_drain
        # The timeout period of connection draining. If **ConnectionDrain** is set to **on**, the parameter is returned.
        # 
        # Valid values: 10 to 900. Unit: seconds.
        self.connection_drain_timeout = connection_drain_timeout
        # The description of the listener.
        self.description = description
        # The timeout period of a connection.
        self.established_timeout = established_timeout
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        self.health_check = health_check
        # The port that is used for health checks. Valid values: **1** to **65535**. If this parameter is not set, the port specified by BackendServerPort is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$_ip**: the private IP addresses of backend servers. If you do not set the HealthCheckDomain parameter or set the parameter to $_ip, the CLB instance uses the private IP address of each backend server for health checks.
        # *   **domain**: The domain name is 1 to 80 characters in length, and can contain letters, digits, periods (.), and hyphens (-).
        self.health_check_domain = health_check_domain
        # The HTTP status code for a successful health check.
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Valid values: **1** to **50**. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The health check method.
        self.health_check_method = health_check_method
        # The health check method that is used by the TCP listener.
        # 
        # Valid values: **tcp** and **http**.
        self.health_check_type = health_check_type
        # The URL that is used for health checks. The URL must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), percent signs (%), question marks (?), number signs (#), and ampersands (&). The URL is not a single forward slash (/) but it starts with a forward slash (/).
        self.health_check_uri = health_check_uri
        # The healthy threshold. The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from **fail** to **success**. Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The frontend port used by the CLB instance.
        self.listener_port = listener_port
        # The ID of the CLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the primary/secondary server group that is associated with the listener.
        self.master_slave_server_group_id = master_slave_server_group_id
        # The timeout period of session persistence.
        # 
        # Valid values: **0** to **3600**. Unit: seconds. Default value: **0**. If the default value is used, the system disables session persistence.
        self.persistence_timeout = persistence_timeout
        # Indicates whether the Proxy protocol is used to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.proxy_protocol_v2enabled = proxy_protocol_v2enabled
        # The ID of the request.
        self.request_id = request_id
        # The scheduling algorithm.
        # 
        # *   **wrr** (default): Backend servers with higher weights receive more requests than backend servers with lower weights.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        # *   **sch**: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server.
        # *   **tch**: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are distributed to the same backend server.
        # 
        # > Only high-performance CLB instances support the sch and tch algorithms.
        self.scheduler = scheduler
        # The status of the listener. Valid values:
        # 
        # *   **running**
        # *   **stopped**
        self.status = status
        # Indicates whether the SynProxy feature of CLB is enabled for protection.
        # 
        # We recommend that you use the default value of this parameter. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.syn_proxy = syn_proxy
        # The tags.
        self.tags = tags
        # The unhealthy threshold. The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from **success** to **fail**. Valid values: **2** to **10**.
        self.unhealthy_threshold = unhealthy_threshold
        # The ID of the associated server group.
        self.vserver_group_id = vserver_group_id

    def validate(self):
        if self.acl_ids:
            self.acl_ids.validate()
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

        if self.connection_drain is not None:
            result['ConnectionDrain'] = self.connection_drain

        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout

        if self.description is not None:
            result['Description'] = self.description

        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout

        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain

        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id

        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout

        if self.proxy_protocol_v2enabled is not None:
            result['ProxyProtocolV2Enabled'] = self.proxy_protocol_v2enabled

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.status is not None:
            result['Status'] = self.status

        if self.syn_proxy is not None:
            result['SynProxy'] = self.syn_proxy

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclIds') is not None:
            temp_model = main_models.DescribeLoadBalancerTCPListenerAttributeResponseBodyAclIds()
            self.acl_ids = temp_model.from_map(m.get('AclIds'))

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ConnectionDrain') is not None:
            self.connection_drain = m.get('ConnectionDrain')

        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')

        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')

        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')

        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')

        if m.get('ProxyProtocolV2Enabled') is not None:
            self.proxy_protocol_v2enabled = m.get('ProxyProtocolV2Enabled')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SynProxy') is not None:
            self.syn_proxy = m.get('SynProxy')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeLoadBalancerTCPListenerAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self

class DescribeLoadBalancerTCPListenerAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeLoadBalancerTCPListenerAttributeResponseBodyTagsTag] = None,
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
                temp_model = main_models.DescribeLoadBalancerTCPListenerAttributeResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerTCPListenerAttributeResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of tag N. Valid values of N: **1** to **20**. The tag value cannot be an empty string. The tag key can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
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

class DescribeLoadBalancerTCPListenerAttributeResponseBodyAclIds(DaraModel):
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

