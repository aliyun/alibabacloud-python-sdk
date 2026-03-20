# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gwlb20240415 import models as main_models
from darabonba.model import DaraModel

class ListServerGroupsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        server_groups: List[main_models.ListServerGroupsResponseBodyServerGroups] = None,
        total_count: int = None,
    ):
        # The number of entries per page.
        # 
        # Valid values: 1 to 1000.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The configurations of the server group.
        self.server_groups = server_groups
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.server_groups:
            for v1 in self.server_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServerGroups'] = []
        if self.server_groups is not None:
            for k1 in self.server_groups:
                result['ServerGroups'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.server_groups = []
        if m.get('ServerGroups') is not None:
            for k1 in m.get('ServerGroups'):
                temp_model = main_models.ListServerGroupsResponseBodyServerGroups()
                self.server_groups.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServerGroupsResponseBodyServerGroups(DaraModel):
    def __init__(
        self,
        connection_drain_config: main_models.ListServerGroupsResponseBodyServerGroupsConnectionDrainConfig = None,
        create_time: str = None,
        health_check_config: main_models.ListServerGroupsResponseBodyServerGroupsHealthCheckConfig = None,
        protocol: str = None,
        related_load_balancer_ids: List[str] = None,
        resource_group_id: str = None,
        scheduler: str = None,
        server_count: int = None,
        server_failover_mode: str = None,
        server_group_id: str = None,
        server_group_name: str = None,
        server_group_status: str = None,
        server_group_type: str = None,
        tags: List[main_models.ListServerGroupsResponseBodyServerGroupsTags] = None,
        vpc_id: str = None,
    ):
        # The configurations of connection draining.
        self.connection_drain_config = connection_drain_config
        # The time when the resource was created. The time follows the ISO 8601 standard in the **yyyy-MM-ddTHH:mm:ssZ** format. The time is displayed in UTC.
        self.create_time = create_time
        # The configuration of health checks.
        self.health_check_config = health_check_config
        # The backend protocol. Valid values:
        # 
        # *   **GENEVE**.
        self.protocol = protocol
        # The IDs of the GWLB instances that are associated with the server group.
        self.related_load_balancer_ids = related_load_balancer_ids
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **5TCH**: indicates consistent hashing that is based on the following factors: source IP address, destination IP address, source port, protocol, and destination port. Requests that contain the same information based on the preceding factors are forwarded to the same backend server.
        # *   **3TCH**: indicates consistent hashing that is based on the following factors: source IP address, destination IP address, and protocol. Requests that contain the same information based on the preceding factors are forwarded to the same backend server.
        # *   **2TCH**: indicates consistent hashing that is based on the following factors: source IP address and destination IP address. Requests that contain the same information based on the preceding factors are forwarded to the same backend server.
        self.scheduler = scheduler
        # The number of server groups.
        self.server_count = server_count
        # Specifies how GWLB processes requests over existing connections when a backend server is not running as expected. Valid values:
        # 
        # *   **NoRebalance**: GWLB continues to forward requests over existing connections to the unhealthy backend server.
        # *   **Rebalance**: GWLB forwards requests over existing connections to the remaining healthy backend servers.
        self.server_failover_mode = server_failover_mode
        # The server group ID.
        self.server_group_id = server_group_id
        # The server group name.
        self.server_group_name = server_group_name
        # The status of the server group. Valid values:
        # 
        # *   **Creating**
        # *   **Available**
        # *   **Configuring**
        self.server_group_status = server_group_status
        # The server group type. Valid values:
        # 
        # *   **Instance**: allows you to specify servers of the **Ecs**, **Eni**, or **Eci** type.
        # *   **Ip**: allows you to add servers of by specifying IP addresses.
        self.server_group_type = server_group_type
        # The tags.
        self.tags = tags
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        if self.connection_drain_config:
            self.connection_drain_config.validate()
        if self.health_check_config:
            self.health_check_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_drain_config is not None:
            result['ConnectionDrainConfig'] = self.connection_drain_config.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.related_load_balancer_ids is not None:
            result['RelatedLoadBalancerIds'] = self.related_load_balancer_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_count is not None:
            result['ServerCount'] = self.server_count

        if self.server_failover_mode is not None:
            result['ServerFailoverMode'] = self.server_failover_mode

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name

        if self.server_group_status is not None:
            result['ServerGroupStatus'] = self.server_group_status

        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionDrainConfig') is not None:
            temp_model = main_models.ListServerGroupsResponseBodyServerGroupsConnectionDrainConfig()
            self.connection_drain_config = temp_model.from_map(m.get('ConnectionDrainConfig'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('HealthCheckConfig') is not None:
            temp_model = main_models.ListServerGroupsResponseBodyServerGroupsHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m.get('HealthCheckConfig'))

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RelatedLoadBalancerIds') is not None:
            self.related_load_balancer_ids = m.get('RelatedLoadBalancerIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerCount') is not None:
            self.server_count = m.get('ServerCount')

        if m.get('ServerFailoverMode') is not None:
            self.server_failover_mode = m.get('ServerFailoverMode')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')

        if m.get('ServerGroupStatus') is not None:
            self.server_group_status = m.get('ServerGroupStatus')

        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListServerGroupsResponseBodyServerGroupsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListServerGroupsResponseBodyServerGroupsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key cannot be an empty string. The tag key can be up to 128 characters in length, and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The tag value can be up to 256 characters in length and cannot contain `http://` or `https://`.
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

class ListServerGroupsResponseBodyServerGroupsHealthCheckConfig(DaraModel):
    def __init__(
        self,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_enabled: bool = None,
        health_check_exp: str = None,
        health_check_http_code: List[str] = None,
        health_check_interval: int = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_req: str = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # The backend server port that is used for health checks.
        # 
        # Valid values: **1** to **65535**.
        self.health_check_connect_port = health_check_connect_port
        # The maximum timeout period of a health check.
        # 
        # Unit: seconds
        # 
        # Valid values: **1** to **300**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$SERVER_IP**: the internal IP address of a backend server.
        # *   **domain**: a domain name. The domain name must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), and periods (.).
        # 
        # > This parameter takes effect only if you set **HealthCheckProtocol** to **HTTP**.
        self.health_check_domain = health_check_domain
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.health_check_enabled = health_check_enabled
        self.health_check_exp = health_check_exp
        # The HTTP status codes that the system returns for health checks.
        self.health_check_http_code = health_check_http_code
        # The interval at which health checks are performed.
        # 
        # Unit: seconds
        # 
        # Valid values: **1** to **50**.
        self.health_check_interval = health_check_interval
        # The URL that is used for health checks.
        # 
        # The URL must be 1 to 80 characters in length, and can contain letters, digits, and the following special characters: ` - / . % ? # &  `The URL must start with a forward slash (/).
        # 
        # > This parameter takes effect only if you set **HealthCheckProtocol** to **HTTP**.
        self.health_check_path = health_check_path
        # The protocol that is used for health checks. Valid values:
        # 
        # *   **TCP**: TCP health checks send TCP SYN packets to a backend server to check whether the port of the backend server is reachable.
        # *   **HTTP**: HTTP health checks simulate a process that uses a web browser to access resources by sending HEAD or GET requests to an instance. These requests are used to check whether the instance is healthy.
        self.health_check_protocol = health_check_protocol
        self.health_check_req = health_check_req
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status changes from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout

        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain

        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled

        if self.health_check_exp is not None:
            result['HealthCheckExp'] = self.health_check_exp

        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path

        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol

        if self.health_check_req is not None:
            result['HealthCheckReq'] = self.health_check_req

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')

        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')

        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')

        if m.get('HealthCheckExp') is not None:
            self.health_check_exp = m.get('HealthCheckExp')

        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')

        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')

        if m.get('HealthCheckReq') is not None:
            self.health_check_req = m.get('HealthCheckReq')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

class ListServerGroupsResponseBodyServerGroupsConnectionDrainConfig(DaraModel):
    def __init__(
        self,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
    ):
        # Indicates whether connection draining is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.connection_drain_enabled = connection_drain_enabled
        # The timeout period of connection draining.
        # 
        # Unit: seconds
        # 
        # Valid values: 1 to 3600.
        self.connection_drain_timeout = connection_drain_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_drain_enabled is not None:
            result['ConnectionDrainEnabled'] = self.connection_drain_enabled

        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionDrainEnabled') is not None:
            self.connection_drain_enabled = m.get('ConnectionDrainEnabled')

        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')

        return self

