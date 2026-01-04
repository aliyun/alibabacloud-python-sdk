# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
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
        # The number of entries per page. Valid values: **1** to **100**.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # A list of server groups.
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
        address_ipversion: str = None,
        ali_uid: int = None,
        any_port_enabled: bool = None,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
        health_check: main_models.ListServerGroupsResponseBodyServerGroupsHealthCheck = None,
        preserve_client_ip_enabled: bool = None,
        protocol: str = None,
        region_id: str = None,
        related_load_balancer_ids: List[str] = None,
        resource_group_id: str = None,
        scheduler: str = None,
        server_count: int = None,
        server_group_id: str = None,
        server_group_name: str = None,
        server_group_status: str = None,
        server_group_type: str = None,
        tags: List[main_models.ListServerGroupsResponseBodyServerGroupsTags] = None,
        vpc_id: str = None,
    ):
        # The IP version. Valid values:
        # 
        # *   **ipv4**
        # *   **DualStack**
        self.address_ipversion = address_ipversion
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # Indicates whether the feature of forwarding requests to all ports is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.any_port_enabled = any_port_enabled
        # Indicates whether connection draining is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.connection_drain_enabled = connection_drain_enabled
        # The timeout period of connection draining. Unit: seconds. Valid values: **10** to **900**.
        self.connection_drain_timeout = connection_drain_timeout
        # The configurations of health checks.
        self.health_check = health_check
        # Indicates whether client IP preservation is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is set to **true** by default when **AddressIPVersion** is set to **ipv4**. This parameter is set to **false** when **AddressIPVersion** is set to **ipv6**. **true** will be supported by later versions.
        self.preserve_client_ip_enabled = preserve_client_ip_enabled
        # The backend protocol. Valid values: **TCP** and **UDP**.
        self.protocol = protocol
        # The region ID of the NLB instance.
        self.region_id = region_id
        # The NLB instances.
        self.related_load_balancer_ids = related_load_balancer_ids
        # The ID of the resource group to which the server group belongs.
        self.resource_group_id = resource_group_id
        # The routing algorithm. Valid values:
        # 
        # *   **Wrr**: Backend servers with higher weights receive more requests than backend servers with lower weights.
        # *   **rr**: Requests are forwarded to the backend servers in sequence. sch: Requests are forwarded to the backend servers based on source IP address hashing.
        # *   **sch**: Requests from the same source IP address are forwarded to the same backend server.
        # *   **tch**: Four-element hashing, which specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are forwarded to the same backend server.
        # *   **qch**: QUIC ID hashing. Requests that contain the same QUIC ID are forwarded to the same backend server.
        self.scheduler = scheduler
        # The number of server groups associated with the NLB instances.
        self.server_count = server_count
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
        # The type of server group. Valid values:
        # 
        # *   **Instance** : contains servers of the **Ecs**, **Ens**, and **Eci** types.
        # *   **Ip**: contains servers specified by IP addresses.
        self.server_group_type = server_group_type
        # The tag.
        self.tags = tags
        # The ID of the VPC to which the server group belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.health_check:
            self.health_check.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.any_port_enabled is not None:
            result['AnyPortEnabled'] = self.any_port_enabled

        if self.connection_drain_enabled is not None:
            result['ConnectionDrainEnabled'] = self.connection_drain_enabled

        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()

        if self.preserve_client_ip_enabled is not None:
            result['PreserveClientIpEnabled'] = self.preserve_client_ip_enabled

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.related_load_balancer_ids is not None:
            result['RelatedLoadBalancerIds'] = self.related_load_balancer_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_count is not None:
            result['ServerCount'] = self.server_count

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
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AnyPortEnabled') is not None:
            self.any_port_enabled = m.get('AnyPortEnabled')

        if m.get('ConnectionDrainEnabled') is not None:
            self.connection_drain_enabled = m.get('ConnectionDrainEnabled')

        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')

        if m.get('HealthCheck') is not None:
            temp_model = main_models.ListServerGroupsResponseBodyServerGroupsHealthCheck()
            self.health_check = temp_model.from_map(m.get('HealthCheck'))

        if m.get('PreserveClientIpEnabled') is not None:
            self.preserve_client_ip_enabled = m.get('PreserveClientIpEnabled')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelatedLoadBalancerIds') is not None:
            self.related_load_balancer_ids = m.get('RelatedLoadBalancerIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerCount') is not None:
            self.server_count = m.get('ServerCount')

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
        # The tag key. At most 10 tag keys are returned.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key
        # The tag value. At most 10 tag values are returned.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
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

class ListServerGroupsResponseBodyServerGroupsHealthCheck(DaraModel):
    def __init__(
        self,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_enabled: bool = None,
        health_check_exp: str = None,
        health_check_http_code: List[str] = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        health_check_type: str = None,
        health_check_url: str = None,
        healthy_threshold: int = None,
        http_check_method: str = None,
        unhealthy_threshold: int = None,
    ):
        # The backend port that is used for health checks.
        # 
        # Valid values: **0** to **65535**.
        # 
        # A value of **0** indicates that the port on a backend server is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The maximum timeout period of a health check response. Unit: seconds. Default value: **5**.
        # 
        # Valid values: **1** to **300**
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name that you want to use for health checks. Valid values:
        # 
        # *   **$SERVER_IP**: the private IP address of a backend server.
        # *   **domain**: a specified domain name. The domain name must be 1 to 80 characters in length, and can contain lowercase letters, digits, hyphens (-), and periods (.).
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_domain = health_check_domain
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.health_check_enabled = health_check_enabled
        # The response string of UDP health checks. The string must be 1 to 512 characters in length, and can contain letters and digits.
        self.health_check_exp = health_check_exp
        # The HTTP status codes returned for health checks. Multiple HTTP status codes are separated by commas (,). Valid values: **http_2xx**, **http_3xx**, **http_4xx**, and **http_5xx**.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_http_code = health_check_http_code
        # The version of the HTTP protocol. Valid values: **HTTP1.0** and **HTTP1.1**.
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.health_check_http_version = health_check_http_version
        # The interval at which health checks are performed. Unit: seconds. Default value: **5**.
        # 
        # *   If you set **HealthCheckType** to **TCP** or **HTTP**, valid values are **1 to 50**.
        # *   If you set **HealthCheckType** to **UDP**, valid values are **1 to 300**. Set the health check interval equal to or larger than the response timeout period to ensure that UDP response timeouts are not determined as no responses.
        self.health_check_interval = health_check_interval
        # The request string of UDP health checks. The string must be 1 to 512 characters in length, and can contain letters and digits.
        self.health_check_req = health_check_req
        # The protocol that is used for health checks. Valid values:
        # 
        # *   **TCP**
        # *   **HTTP**
        # *   **UDP**
        self.health_check_type = health_check_type
        # The path to which health check probes are sent.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_url = health_check_url
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The HTTP method that is used for health checks. Valid values: **GET** and **HEAD**.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.http_check_method = http_check_method
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

        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_req is not None:
            result['HealthCheckReq'] = self.health_check_req

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.http_check_method is not None:
            result['HttpCheckMethod'] = self.http_check_method

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

        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckReq') is not None:
            self.health_check_req = m.get('HealthCheckReq')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('HttpCheckMethod') is not None:
            self.http_check_method = m.get('HttpCheckMethod')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

