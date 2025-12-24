# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLoadBalancerUDPListenerAttributeRequest(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_status: str = None,
        acl_type: str = None,
        bandwidth: int = None,
        description: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_interval: int = None,
        health_check_switch: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        master_slave_server_group: str = None,
        master_slave_server_group_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        proxy_protocol_v2enabled: bool = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
        vserver_group: str = None,
        vserver_group_id: str = None,
        health_check_exp: str = None,
        health_check_req: str = None,
    ):
        # The ID of the network access control list (ACL) that is associated with the listener.
        # 
        # >  If **AclStatus** is set to **on**, this parameter is required.
        self.acl_id = acl_id
        # Specifies whether to enable access control. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        self.acl_status = acl_status
        # The type of the network ACL. Valid values:
        # 
        # *   **white**: a whitelist. Only requests from the IP addresses or CIDR blocks in the network ACL are forwarded. Whitelists apply to scenarios where you want to allow only specific IP addresses to access an application. Your service may be adversely affected if the whitelist is not properly configured. After a whitelist is configured, only requests from IP addresses that are added to the whitelist are forwarded by the listener.
        # 
        #     If you enable a whitelist but do not add an IP address to the ACL, the listener forwards all requests.
        # 
        # *   **black**: a blacklist. All requests from the IP addresses or CIDR blocks in the network ACL are denied. Blacklists apply to scenarios where you want to block access from specified IP addresses to an application.
        # 
        #     If a blacklist is configured for a listener but no IP address is added to the blacklist, the listener forwards all requests.
        # 
        # >  If **AclStatus** is set to **on**, this parameter is required.
        self.acl_type = acl_type
        # The maximum bandwidth of the listener. Unit: Mbit/s. Valid values:
        # 
        # *   **-1**: For a pay-by-data-transfer Internet-facing CLB instance, you can set this parameter to **-1**. This way, the bandwidth of the listener is unlimited.
        # *   **1** to **5120**: For a pay-by-bandwidth Internet-facing CLB instance, you can specify the maximum bandwidth of each listener. The sum of bandwidth limits that you set for all listeners cannot exceed the maximum bandwidth of the CLB instance.
        self.bandwidth = bandwidth
        # The name of the listener.
        # 
        # The name must be 1 to 256 characters in length and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        self.description = description
        # The port that is used for health checks.
        # 
        # Valid values: **1** to **65535**.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period of a health check. If a backend server, such as an Elastic Compute Service (ECS) instance, does not return a health check response within the specified timeout period, the server fails the health check. Unit: seconds.
        # 
        # Valid values: **1** to **300**.
        # 
        # >  If the value of the **HealthCheckConnectTimeout** parameter is smaller than that of the **HealthCheckInterval** parameter, the timeout period specified by the **HealthCheckConnectTimeout** parameter is ignored and the period of time specified by the **HealthCheckInterval** parameter is used as the timeout period.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The interval at which health checks are performed. Unit: seconds.
        # 
        # Valid values: **1** to **50**.
        self.health_check_interval = health_check_interval
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **on** (default): yes
        # *   **off**: no
        self.health_check_switch = health_check_switch
        # The number of times that an unhealthy backend server must consecutively pass health checks before it can be declared healthy (from **fail** to **success**).
        # 
        # Valid values: **1** to **10**.
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
        # Specifies whether to use a primary/secondary server group. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        # 
        # >  You cannot set **VserverGroup** and **MasterSlaveServerGroup** both to **on**.
        self.master_slave_server_group = master_slave_server_group
        # The ID of the primary/secondary server group.
        # 
        # >  You cannot specify both VServerGroupId and MasterSlaveServerGroupId.
        self.master_slave_server_group_id = master_slave_server_group_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to use the Proxy protocol to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.proxy_protocol_v2enabled = proxy_protocol_v2enabled
        # The region ID of the CLB instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr**: Backend servers with higher weights receive more requests than those with lower weights.
        # 
        #     If two backend servers have the same weight, the backend server that has fewer connections is expected to receive more requests.
        # 
        # *   **rr**: Requests are distributed to backend servers in sequence.
        # 
        # *   **sch**: specifies consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server.
        # 
        # *   **tch**: specifies consistent hashing that is based on the following parameters: source IP address, destination IP address, source port, and destination port. Requests that contain the same preceding information are distributed to the same backend server.
        # 
        # *   **qch**: specifies consistent hashing that is based on QUIC connection IDs. Requests that contain the same QUIC connection ID are distributed to the same backend server.
        # 
        # > *   Only high-performance CLB instances support **sch**, **tch**, and **qch**.
        # > *   You cannot switch the algorithm used by a CLB instance from **wrr** or **rr** to consistent hashing or from consistent hashing to weighted round robin or round robin.
        self.scheduler = scheduler
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from **success** to **fail**.
        # 
        # Valid values: **1** to **10**.
        self.unhealthy_threshold = unhealthy_threshold
        # Specifies whether to use a vServer group. Valid values:
        # 
        # *   **on**: yes
        # *   **off**: no
        # 
        # >  You cannot set both **VserverGroup** and **MasterSlaveServerGroup** to **on**.
        self.vserver_group = vserver_group
        # The ID of the vServer group.
        self.vserver_group_id = vserver_group_id
        # The response string for UDP listener health checks. The string must be 1 to 64 characters in length and can contain only letters and digits.
        self.health_check_exp = health_check_exp
        # The request string for UDP listener health checks. The string must be 1 to 64 characters in length and can contain only letters and digits.
        self.health_check_req = health_check_req

    def validate(self):
        pass

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

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.description is not None:
            result['Description'] = self.description

        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_switch is not None:
            result['HealthCheckSwitch'] = self.health_check_switch

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.master_slave_server_group is not None:
            result['MasterSlaveServerGroup'] = self.master_slave_server_group

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

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        if self.vserver_group is not None:
            result['VServerGroup'] = self.vserver_group

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.health_check_exp is not None:
            result['healthCheckExp'] = self.health_check_exp

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

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckSwitch') is not None:
            self.health_check_switch = m.get('HealthCheckSwitch')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('MasterSlaveServerGroup') is not None:
            self.master_slave_server_group = m.get('MasterSlaveServerGroup')

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

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        if m.get('VServerGroup') is not None:
            self.vserver_group = m.get('VServerGroup')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('healthCheckExp') is not None:
            self.health_check_exp = m.get('healthCheckExp')

        if m.get('healthCheckReq') is not None:
            self.health_check_req = m.get('healthCheckReq')

        return self

