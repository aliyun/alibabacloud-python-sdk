# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerUDPListenerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_ids: main_models.DescribeLoadBalancerUDPListenerAttributeResponseBodyAclIds = None,
        acl_status: str = None,
        acl_type: str = None,
        backend_server_port: int = None,
        bandwidth: int = None,
        description: str = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_exp: str = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        master_slave_server_group_id: str = None,
        proxy_protocol_v2enabled: bool = None,
        request_id: str = None,
        scheduler: str = None,
        status: str = None,
        tags: main_models.DescribeLoadBalancerUDPListenerAttributeResponseBodyTags = None,
        unhealthy_threshold: int = None,
        vserver_group_id: str = None,
    ):
        # The ID of the network ACL.
        self.acl_id = acl_id
        # The ID of the access control list (ACL).
        self.acl_ids = acl_ids
        # Indicates whether access control is enabled. Valid values: **on** and **off**. Default value: off.
        self.acl_status = acl_status
        # The type of the ACL. Valid values:
        # 
        # *   **white**: a whitelist. Only requests from the IP addresses or CIDR blocks in the network ACL are forwarded. Whitelists apply to scenarios in which you want to allow only specified IP addresses to access an application.
        # 
        #     Your service may be adversely affected if the whitelist is not properly configured. After a whitelist is configured, only requests from IP addresses that are added to the whitelist are forwarded by the listener. If you enable a whitelist but do not add an IP address to the ACL, the listener forwards all requests.
        # 
        # *   **black**: a blacklist. All requests from the IP addresses or CIDR blocks in the network ACL are blocked. Blacklists apply to scenarios in which you want to deny access from specific IP addresses or CIDR blocks to an application.
        # 
        #     If a blacklist is configured for a listener but no IP address is added to the blacklist, the listener forwards all requests.
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
        # The description of the listener.
        self.description = description
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        self.health_check = health_check
        # The port that is used for health checks. Valid values: **1** to **65535**. If this parameter is not set, the port specified by BackendServerPort is used for health checks.
        # 
        # >  This parameter takes effect only when the **HealthCheck** parameter is set to **on**.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period of a health check. If a backend Elastic Compute Service (ECS) instance does not return a health check response within the specified timeout period, the server fails the health check. Valid values: **1** to **300**. Unit: seconds.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The response string for UDP listener health checks. The string is up to 64 characters in length, and can contain letters and digits.
        self.health_check_exp = health_check_exp
        # The interval between two consecutive health checks. Valid values: **1** to **50**. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The request string for UDP listener health checks. The string is up to 64 characters in length, and can contain letters and digits.
        self.health_check_req = health_check_req
        # The healthy threshold. The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from **fail** to **success**. Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The frontend port used by the CLB instance.
        self.listener_port = listener_port
        # The ID of the CLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the primary/secondary server group that is associated with the listener.
        self.master_slave_server_group_id = master_slave_server_group_id
        # Indicates whether the Proxy protocol is used to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.proxy_protocol_v2enabled = proxy_protocol_v2enabled
        # The ID of the request.
        self.request_id = request_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr** (default): Backend servers with higher weights receive more requests than backend servers with lower weights.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        self.scheduler = scheduler
        # The status of the listener. Valid values:
        # 
        # *   **running**
        # *   **stopped**
        self.status = status
        # The tags.
        self.tags = tags
        # The unhealthy threshold. The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from **success** to **fail**. Valid values: **2** to **10**.
        self.unhealthy_threshold = unhealthy_threshold
        # The ID of the vServer group that is associated with the listener.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout

        if self.health_check_exp is not None:
            result['HealthCheckExp'] = self.health_check_exp

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_req is not None:
            result['HealthCheckReq'] = self.health_check_req

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id

        if self.proxy_protocol_v2enabled is not None:
            result['ProxyProtocolV2Enabled'] = self.proxy_protocol_v2enabled

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.status is not None:
            result['Status'] = self.status

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
            temp_model = main_models.DescribeLoadBalancerUDPListenerAttributeResponseBodyAclIds()
            self.acl_ids = temp_model.from_map(m.get('AclIds'))

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')

        if m.get('HealthCheckExp') is not None:
            self.health_check_exp = m.get('HealthCheckExp')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckReq') is not None:
            self.health_check_req = m.get('HealthCheckReq')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')

        if m.get('ProxyProtocolV2Enabled') is not None:
            self.proxy_protocol_v2enabled = m.get('ProxyProtocolV2Enabled')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeLoadBalancerUDPListenerAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self

class DescribeLoadBalancerUDPListenerAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeLoadBalancerUDPListenerAttributeResponseBodyTagsTag] = None,
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
                temp_model = main_models.DescribeLoadBalancerUDPListenerAttributeResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerUDPListenerAttributeResponseBodyTagsTag(DaraModel):
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

class DescribeLoadBalancerUDPListenerAttributeResponseBodyAclIds(DaraModel):
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

