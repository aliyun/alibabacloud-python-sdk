# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class CreateLoadBalancerUDPListenerRequest(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_status: str = None,
        acl_type: str = None,
        backend_server_port: int = None,
        bandwidth: int = None,
        description: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_switch: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        master_slave_server_group_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        proxy_protocol_v2enabled: bool = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheduler: str = None,
        tag: List[main_models.CreateLoadBalancerUDPListenerRequestTag] = None,
        unhealthy_threshold: int = None,
        vserver_group_id: str = None,
        health_check_exp: str = None,
        health_check_interval: int = None,
        health_check_req: str = None,
    ):
        # The ID of the network ACL that is associated with the listener.
        # 
        # If **AclStatus** is set to **on**, this parameter is required.
        self.acl_id = acl_id
        # Specifies whether to enable access control. Valid values:
        # 
        # *   **on**: yes
        # *   **off** (default): no
        self.acl_status = acl_status
        # The type of the network ACL. Valid values:
        # 
        # *   **white**: a whitelist. Only requests from the IP addresses or CIDR blocks in the network ACL are forwarded. Whitelists apply to scenarios in which you want to allow only specific IP addresses to access an application. After a whitelist is configured, only IP addresses in the whitelist can access the CLB listener. Risks may arise if the whitelist is improperly set.
        # 
        #     If a whitelist is configured but no IP address is added to the whitelist, the listener forwards all requests.
        # 
        # *   **black**: a blacklist. All requests from the IP addresses or CIDR blocks in the network ACL are blocked. Blacklists apply to scenarios in which you want to deny access from specific IP addresses to an application.
        # 
        #     If a blacklist is configured for a listener but no IP address is added to the blacklist, the listener forwards all requests.
        # 
        # If **AclStatus** is set to **on**, this parameter is required.
        self.acl_type = acl_type
        # The backend port used by the CLB instance.
        # 
        # Valid values: **1** to **65535**.
        # 
        # If the **VServerGroupId** parameter is not set, this parameter is required.
        self.backend_server_port = backend_server_port
        # The maximum bandwidth of the listener. Unit: Mbit/s. Valid values:
        # 
        # **-1**: For a pay-by-data-transfer Internet-facing CLB instance, you can set this parameter to **-1**. This way, the bandwidth of the listener is unlimited.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The name of the listener.
        # 
        # The name must be 1 to 256 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        self.description = description
        # The port that is used for health checks.
        # 
        # Valid values: **1** to **65535**.
        # 
        # If this parameter is not set, the backend port specified by **BackendServerPort** is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period of a health check.
        # 
        # If a backend server, such as an Elastic Compute Service (ECS) instance, does not respond to a probe packet within the specified timeout period, the server fails the health check. Unit: seconds
        # 
        # Valid values: **1** to **300**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **on** (default): yes
        # *   **off**: no
        self.health_check_switch = health_check_switch
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from **fail** to **success**.
        # 
        # Valid values: **2** to **10**
        self.healthy_threshold = healthy_threshold
        # The frontend port used by the CLB instance.
        # 
        # Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The ID of the primary/secondary server group.
        # 
        # >  You can set only one of the VServerGroupId and MasterSlaveServerGroupId parameters.
        self.master_slave_server_group_id = master_slave_server_group_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to use the Proxy protocol to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.proxy_protocol_v2enabled = proxy_protocol_v2enabled
        # The ID of the region where the CLB instance is deployed.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr** (default): Backend servers with higher weights receive more requests than those with lower weights.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        # *   **sch**: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server.
        # *   **tch**: specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are distributed to the same backend server.
        # *   **qch**: specifies consistent hashing that is based on QUIC connection IDs. Requests that contain the same QUIC connection ID are distributed to the same backend server.
        # 
        # Only high-performance CLB instances support the sch, tch, and qch consistent hashing algorithms.
        self.scheduler = scheduler
        # The tags.
        self.tag = tag
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from **success** to **fail**.
        # 
        # Valid values: **2** to **10**
        self.unhealthy_threshold = unhealthy_threshold
        # The ID of the vServer group.
        self.vserver_group_id = vserver_group_id
        # The response string for UDP listener health checks. The string must be 1 to 64 characters in length and can contain only letters and digits.
        self.health_check_exp = health_check_exp
        # The interval between two consecutive health checks. Unit: seconds.
        # 
        # Valid values: **1** to **50**.
        self.health_check_interval = health_check_interval
        # The request string for UDP listener health checks. The string must be 1 to 64 characters in length and can contain only letters and digits.
        self.health_check_req = health_check_req

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

        if self.description is not None:
            result['Description'] = self.description

        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout

        if self.health_check_switch is not None:
            result['HealthCheckSwitch'] = self.health_check_switch

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.proxy_protocol_v2enabled is not None:
            result['ProxyProtocolV2Enabled'] = self.proxy_protocol_v2enabled

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.health_check_exp is not None:
            result['healthCheckExp'] = self.health_check_exp

        if self.health_check_interval is not None:
            result['healthCheckInterval'] = self.health_check_interval

        if self.health_check_req is not None:
            result['healthCheckReq'] = self.health_check_req

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')

        if m.get('HealthCheckSwitch') is not None:
            self.health_check_switch = m.get('HealthCheckSwitch')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProxyProtocolV2Enabled') is not None:
            self.proxy_protocol_v2enabled = m.get('ProxyProtocolV2Enabled')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateLoadBalancerUDPListenerRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('healthCheckExp') is not None:
            self.health_check_exp = m.get('healthCheckExp')

        if m.get('healthCheckInterval') is not None:
            self.health_check_interval = m.get('healthCheckInterval')

        if m.get('healthCheckReq') is not None:
            self.health_check_req = m.get('healthCheckReq')

        return self

class CreateLoadBalancerUDPListenerRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key must be 1 to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

