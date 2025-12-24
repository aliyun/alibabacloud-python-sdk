# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerListenersResponseBody(DaraModel):
    def __init__(
        self,
        listeners: List[main_models.DescribeLoadBalancerListenersResponseBodyListeners] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A list of listeners of the CLB instance.
        # 
        # >  This parameter is not returned if the CLB instance does not have a listener.
        self.listeners = listeners
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If **NextToken** is empty, it indicates that no subsequent query is to be sent.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.listeners:
            for v1 in self.listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Listeners'] = []
        if self.listeners is not None:
            for k1 in self.listeners:
                result['Listeners'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k1 in m.get('Listeners'):
                temp_model = main_models.DescribeLoadBalancerListenersResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLoadBalancerListenersResponseBodyListeners(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_ids: List[str] = None,
        acl_status: str = None,
        acl_type: str = None,
        backend_server_port: int = None,
        bandwidth: int = None,
        description: str = None,
        httplistener_config: main_models.DescribeLoadBalancerListenersResponseBodyListenersHTTPListenerConfig = None,
        httpslistener_config: main_models.DescribeLoadBalancerListenersResponseBodyListenersHTTPSListenerConfig = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
        scheduler: str = None,
        status: str = None,
        tcplistener_config: main_models.DescribeLoadBalancerListenersResponseBodyListenersTCPListenerConfig = None,
        tags: List[main_models.DescribeLoadBalancerListenersResponseBodyListenersTags] = None,
        udplistener_config: main_models.DescribeLoadBalancerListenersResponseBodyListenersUDPListenerConfig = None,
        vserver_group_id: str = None,
    ):
        # The ID of the access control list (ACL).
        self.acl_id = acl_id
        # The IDs of the ACLs.
        self.acl_ids = acl_ids
        # Indicates whether access control is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.acl_status = acl_status
        # The type of access control. Valid values:
        # 
        # *   **white**: The listener forwards requests only from IP addresses and CIDR blocks on the whitelist. Your service may be adversely affected if the whitelist is not properly configured. If a whitelist is configured, the listener forwards requests only from IP addresses that are added to the whitelist.
        # 
        # If you configure a whitelist but no IP address is added to the whitelist, the listener forwards all requests.
        # 
        # *   **black**: The listener blocks requests from IP addresses and CIDR blocks on the blacklist.
        # 
        # If you configure a blacklist but no IP address is added to the blacklist, the listener forwards all requests.
        self.acl_type = acl_type
        # The port of the backend server.
        # 
        # >  This parameter takes effect only when the `VServerGroupId` and `MasterSlaveServerGroupId` parameters are both empty.
        self.backend_server_port = backend_server_port
        # The maximum bandwidth of the listener. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The description of the listener.
        self.description = description
        # The configurations of the HTTP listener.
        self.httplistener_config = httplistener_config
        # The configurations of the HTTPS listener.
        self.httpslistener_config = httpslistener_config
        # The listener port.
        self.listener_port = listener_port
        # The protocol used by the listener.
        self.listener_protocol = listener_protocol
        # The ID of the CLB instance.
        self.load_balancer_id = load_balancer_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr**: Backend servers with higher weights receive more requests than those with lower weights.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        # *   **sch**: consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server.
        # *   **tch**: specifies consistent hashing based on the source IP address, destination IP address, source port, and destination port. Requests that have the same four factors are distributed to the same backend server.
        # *   **qch**: specifies consistent hashing based on Quick UDP Internet Connection (QUIC) IDs. Requests that contain the same QUIC ID are scheduled to the same backend server.
        # 
        # >  Only high-performance CLB instances support the **sch**, **tch**, and **qch** consistent hashing algorithms.
        self.scheduler = scheduler
        # The status of the listener. Valid values:
        # 
        # *   **running**
        # *   **stopped**
        self.status = status
        # The configurations of the TCP listener.
        self.tcplistener_config = tcplistener_config
        # A list of tags.
        self.tags = tags
        # The configurations of the UDP listener.
        self.udplistener_config = udplistener_config
        # The ID of the vServer group associated with the listener.
        self.vserver_group_id = vserver_group_id

    def validate(self):
        if self.httplistener_config:
            self.httplistener_config.validate()
        if self.httpslistener_config:
            self.httpslistener_config.validate()
        if self.tcplistener_config:
            self.tcplistener_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.udplistener_config:
            self.udplistener_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_ids is not None:
            result['AclIds'] = self.acl_ids

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

        if self.httplistener_config is not None:
            result['HTTPListenerConfig'] = self.httplistener_config.to_map()

        if self.httpslistener_config is not None:
            result['HTTPSListenerConfig'] = self.httpslistener_config.to_map()

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.status is not None:
            result['Status'] = self.status

        if self.tcplistener_config is not None:
            result['TCPListenerConfig'] = self.tcplistener_config.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.udplistener_config is not None:
            result['UDPListenerConfig'] = self.udplistener_config.to_map()

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclIds') is not None:
            self.acl_ids = m.get('AclIds')

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

        if m.get('HTTPListenerConfig') is not None:
            temp_model = main_models.DescribeLoadBalancerListenersResponseBodyListenersHTTPListenerConfig()
            self.httplistener_config = temp_model.from_map(m.get('HTTPListenerConfig'))

        if m.get('HTTPSListenerConfig') is not None:
            temp_model = main_models.DescribeLoadBalancerListenersResponseBodyListenersHTTPSListenerConfig()
            self.httpslistener_config = temp_model.from_map(m.get('HTTPSListenerConfig'))

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TCPListenerConfig') is not None:
            temp_model = main_models.DescribeLoadBalancerListenersResponseBodyListenersTCPListenerConfig()
            self.tcplistener_config = temp_model.from_map(m.get('TCPListenerConfig'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeLoadBalancerListenersResponseBodyListenersTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UDPListenerConfig') is not None:
            temp_model = main_models.DescribeLoadBalancerListenersResponseBodyListenersUDPListenerConfig()
            self.udplistener_config = temp_model.from_map(m.get('UDPListenerConfig'))

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self

class DescribeLoadBalancerListenersResponseBodyListenersUDPListenerConfig(DaraModel):
    def __init__(
        self,
        connection_drain: str = None,
        connection_drain_timeout: int = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_exp: str = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        healthy_threshold: int = None,
        master_slave_server_group_id: str = None,
        proxy_protocol_v2enabled: str = None,
        unhealthy_threshold: int = None,
    ):
        # Indicates whether connection draining is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.connection_drain = connection_drain
        # The timeout period of connection draining. Unit: seconds.
        # 
        # Value values: **10 to 900**.
        self.connection_drain_timeout = connection_drain_timeout
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.health_check = health_check
        # The port that is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period for a health check response.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The response string of UDP health checks.
        self.health_check_exp = health_check_exp
        # The interval between two consecutive health checks. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The request string of UDP health checks.
        self.health_check_req = health_check_req
        # The number of times that a backend server must consecutively pass health checks before it is declared healthy.
        self.healthy_threshold = healthy_threshold
        # The ID of the primary/secondary server group that is associated with the listener.
        self.master_slave_server_group_id = master_slave_server_group_id
        # Indicates whether the Proxy protocol is used to pass source client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: enables the burst feature for the data disk.
        # *   **false**: The task is not being retried.
        self.proxy_protocol_v2enabled = proxy_protocol_v2enabled
        # The number of times that a backend server must consecutively fail health checks before it is declared unhealthy.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_drain is not None:
            result['ConnectionDrain'] = self.connection_drain

        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout

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

        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id

        if self.proxy_protocol_v2enabled is not None:
            result['ProxyProtocolV2Enabled'] = self.proxy_protocol_v2enabled

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionDrain') is not None:
            self.connection_drain = m.get('ConnectionDrain')

        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')

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

        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')

        if m.get('ProxyProtocolV2Enabled') is not None:
            self.proxy_protocol_v2enabled = m.get('ProxyProtocolV2Enabled')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

class DescribeLoadBalancerListenersResponseBodyListenersTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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

class DescribeLoadBalancerListenersResponseBodyListenersTCPListenerConfig(DaraModel):
    def __init__(
        self,
        connection_drain: str = None,
        connection_drain_timeout: int = None,
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
        master_slave_server_group_id: str = None,
        persistence_timeout: int = None,
        proxy_protocol_v2enabled: str = None,
        unhealthy_threshold: int = None,
    ):
        # Indicates whether connection draining is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.connection_drain = connection_drain
        # The timeout period of connection draining. Unit: seconds.
        # 
        # Value values: **10 to 900**.
        self.connection_drain_timeout = connection_drain_timeout
        # The timeout period of a connection. Unit: seconds.
        self.established_timeout = established_timeout
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.health_check = health_check
        # The port that is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period of health checks. Unit: seconds.
        # 
        # Valid values: **1** to **300**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name that is used for health checks.
        self.health_check_domain = health_check_domain
        # The HTTP status code that indicates a healthy backend server.
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The health check method.
        self.health_check_method = health_check_method
        # The protocol that you want to use for health checks.
        self.health_check_type = health_check_type
        # The URI that is used for health checks.
        self.health_check_uri = health_check_uri
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health check status of the backend server changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The ID of the primary/secondary server group associated with the listener.
        self.master_slave_server_group_id = master_slave_server_group_id
        # Indicates whether session persistence is enabled. Unit: seconds.
        # 
        # Valid values: **0** to **3600**.
        # 
        # **0** indicates that session persistence is disabled.
        self.persistence_timeout = persistence_timeout
        # Indicates whether the Proxy protocol is used to pass source client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: enables the burst feature for the data disk.
        # *   **false**: The task is not being retried.
        self.proxy_protocol_v2enabled = proxy_protocol_v2enabled
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health check status of the backend server changes from **success** to **fail**.
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
        if self.connection_drain is not None:
            result['ConnectionDrain'] = self.connection_drain

        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout

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

        if self.master_slave_server_group_id is not None:
            result['MasterSlaveServerGroupId'] = self.master_slave_server_group_id

        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout

        if self.proxy_protocol_v2enabled is not None:
            result['ProxyProtocolV2Enabled'] = self.proxy_protocol_v2enabled

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionDrain') is not None:
            self.connection_drain = m.get('ConnectionDrain')

        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')

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

        if m.get('MasterSlaveServerGroupId') is not None:
            self.master_slave_server_group_id = m.get('MasterSlaveServerGroupId')

        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')

        if m.get('ProxyProtocolV2Enabled') is not None:
            self.proxy_protocol_v2enabled = m.get('ProxyProtocolV2Enabled')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

class DescribeLoadBalancerListenersResponseBodyListenersHTTPSListenerConfig(DaraModel):
    def __init__(
        self,
        cacertificate_id: str = None,
        cookie: str = None,
        cookie_timeout: int = None,
        enable_http_2: str = None,
        gzip: str = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        idle_timeout: int = None,
        request_timeout: int = None,
        server_certificate_id: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        tlscipher_policy: str = None,
        unhealthy_threshold: int = None,
        xforwarded_for: str = None,
        xforwarded_for_client_cert_client_verify: str = None,
        xforwarded_for_client_cert_fingerprint: str = None,
        xforwarded_for_client_cert_issuer_dn: str = None,
        xforwarded_for_client_cert_subject_dn: str = None,
        xforwarded_for_client_src_port: str = None,
        xforwarded_for_slbid: str = None,
        xforwarded_for_slbip: str = None,
        xforwarded_for_slbport: str = None,
        xforwarded_for_proto: str = None,
    ):
        # The ID of the CA certificate.
        self.cacertificate_id = cacertificate_id
        # The cookie configures for the server.
        self.cookie = cookie
        # The maximum amount of time to wait before the session cookie expires. Unit: seconds.
        # 
        # Valid values: **1** to **86400**.
        self.cookie_timeout = cookie_timeout
        # Indicates whether `HTTP 2.0` is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.enable_http_2 = enable_http_2
        # Indicates whether GZIP compression is enabled. Valid values:
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
        self.health_check_connect_port = health_check_connect_port
        # The domain name that is used for health checks.
        self.health_check_domain = health_check_domain
        # The HTTP status code that indicates a healthy backend server.
        self.health_check_http_code = health_check_http_code
        # The HTTP version for health checks.
        self.health_check_http_version = health_check_http_version
        # The interval at which health checks are performed. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The health check method.
        self.health_check_method = health_check_method
        # The timeout period of a health check response. Unit: seconds.
        self.health_check_timeout = health_check_timeout
        # The protocol that you want to use for health checks.
        self.health_check_type = health_check_type
        # The URI that is used for health checks.
        self.health_check_uri = health_check_uri
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health check status of the backend server changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1** to **60**.
        # 
        # If no request is received within the specified timeout period, CLB closes the connection. When a request is received, CLB establishes a new connection.
        self.idle_timeout = idle_timeout
        # The request timeout period. Unit: seconds. Valid values: **1** to **180**.
        # 
        # If no response is received from a backend server during the request timeout period, CLB sends the `HTTP 504` status code to the client.
        self.request_timeout = request_timeout
        # The ID of the server certificate.
        self.server_certificate_id = server_certificate_id
        # Indicates whether session persistence is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.sticky_session = sticky_session
        # The method used to handle the cookie.
        # 
        # *   **insert**: inserts a cookie. CLB inserts the SERVERID cookie to the HTTP or HTTPS response to the first request from a client. Subsequent requests that carry the SERVERID cookie from the client are forwarded to the same backend server as the first request.
        # *   **server**: rewrites the original cookie. CLB rewrites the custom cookies in requests from a client. Subsequent requests from the client that carry the new cookie are forwarded to the same backend server as the first request.
        self.sticky_session_type = sticky_session_type
        # A TLS security policy contains TLS protocols and cipher suites available for HTTPS.
        # 
        # *   **tls_cipher_policy_1_0**:
        # 
        #     Supported TLS versions: TLSv1.0, TLSv1.1, and TLSv1.2.
        # 
        #     Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # *   **tls_cipher_policy_1_1**:
        # 
        #     Supported TLS versions: TLSv1.1 and TLSv1.2.
        # 
        #     Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # *   **tls_cipher_policy_1_2**
        # 
        #     Supported TLS versions: TLSv1.2.
        # 
        #     Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, AES128-GCM-SHA256, AES256-GCM-SHA384, AES128-SHA256, AES256-SHA256, ECDHE-RSA-AES128-SHA, ECDHE-RSA-AES256-SHA, AES128-SHA, AES256-SHA, and DES-CBC3-SHA.
        # 
        # *   **tls_cipher_policy_1_2_strict**
        # 
        #     Supported TLS versions: TLSv1.2.
        # 
        #     Supported cipher suites: ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA.
        # 
        # *   **tls_cipher_policy_1_2_strict_with_1_3**
        # 
        #     Supported TLS versions: TLSv1.2 and TLSv1.3.
        # 
        #     Supported cipher suites: TLS_AES_128_GCM_SHA256, TLS_AES_256_GCM_SHA384, TLS_CHACHA20_POLY1305_SHA256, TLS_AES_128_CCM_SHA256, TLS_AES_128_CCM_8_SHA256, ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384, ECDHE-ECDSA-AES128-SHA256, ECDHE-ECDSA-AES256-SHA384, ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-AES128-SHA256, ECDHE-RSA-AES256-SHA384, ECDHE-ECDSA-AES128-SHA, ECDHE-ECDSA-AES256-SHA, ECDHE-RSA-AES128-SHA, and ECDHE-RSA-AES256-SHA.
        self.tlscipher_policy = tlscipher_policy
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health check status of the backend server changes from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        self.unhealthy_threshold = unhealthy_threshold
        # Indicates whether the `X-Forwarded-For` header is used to retrieve client IP addresses. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for = xforwarded_for
        # Indicates whether the `XForwardedFor_ClientCertClientVerify` header is used to obtain the verification result of the client certificate. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_client_cert_client_verify = xforwarded_for_client_cert_client_verify
        # Indicates whether the `XForwardedFor_ClientCertFingerprint` header is used to obtain the fingerprint of the client certificate. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_client_cert_fingerprint = xforwarded_for_client_cert_fingerprint
        # Indicates whether the `XForwardedFor_ClientCertIssuerDN` header is used to obtain information about the authority that issues the client certificate. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_client_cert_issuer_dn = xforwarded_for_client_cert_issuer_dn
        # Indicates whether the `XForwardedFor_ClientCertSubjectDN` header is used to obtain information about the owner of the client certificate. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_client_cert_subject_dn = xforwarded_for_client_cert_subject_dn
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
        # Indicates whether the `SLB-IP` header is used to retrieve the VIP of the client. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_slbip = xforwarded_for_slbip
        # Indicates whether the `XForwardedFor_SLBPORT` header is used to retrieve the listener port of the CLB instance. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_slbport = xforwarded_for_slbport
        # Indicates whether the `X-Forwarded-Proto` header is used to obtain the listener protocol. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_proto = xforwarded_for_proto

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id

        if self.cookie is not None:
            result['Cookie'] = self.cookie

        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout

        if self.enable_http_2 is not None:
            result['EnableHttp2'] = self.enable_http_2

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

        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method

        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id

        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        if self.tlscipher_policy is not None:
            result['TLSCipherPolicy'] = self.tlscipher_policy

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for

        if self.xforwarded_for_client_cert_client_verify is not None:
            result['XForwardedFor_ClientCertClientVerify'] = self.xforwarded_for_client_cert_client_verify

        if self.xforwarded_for_client_cert_fingerprint is not None:
            result['XForwardedFor_ClientCertFingerprint'] = self.xforwarded_for_client_cert_fingerprint

        if self.xforwarded_for_client_cert_issuer_dn is not None:
            result['XForwardedFor_ClientCertIssuerDN'] = self.xforwarded_for_client_cert_issuer_dn

        if self.xforwarded_for_client_cert_subject_dn is not None:
            result['XForwardedFor_ClientCertSubjectDN'] = self.xforwarded_for_client_cert_subject_dn

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
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')

        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

        if m.get('EnableHttp2') is not None:
            self.enable_http_2 = m.get('EnableHttp2')

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

        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')

        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')

        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        if m.get('TLSCipherPolicy') is not None:
            self.tlscipher_policy = m.get('TLSCipherPolicy')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')

        if m.get('XForwardedFor_ClientCertClientVerify') is not None:
            self.xforwarded_for_client_cert_client_verify = m.get('XForwardedFor_ClientCertClientVerify')

        if m.get('XForwardedFor_ClientCertFingerprint') is not None:
            self.xforwarded_for_client_cert_fingerprint = m.get('XForwardedFor_ClientCertFingerprint')

        if m.get('XForwardedFor_ClientCertIssuerDN') is not None:
            self.xforwarded_for_client_cert_issuer_dn = m.get('XForwardedFor_ClientCertIssuerDN')

        if m.get('XForwardedFor_ClientCertSubjectDN') is not None:
            self.xforwarded_for_client_cert_subject_dn = m.get('XForwardedFor_ClientCertSubjectDN')

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

class DescribeLoadBalancerListenersResponseBodyListenersHTTPListenerConfig(DaraModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        forward_port: int = None,
        gzip: str = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        idle_timeout: int = None,
        listener_forward: str = None,
        request_timeout: int = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        unhealthy_threshold: int = None,
        xforwarded_for: str = None,
        xforwarded_for_client_src_port: str = None,
        xforwarded_for_slbid: str = None,
        xforwarded_for_slbip: str = None,
        xforwarded_for_slbport: str = None,
        xforwarded_for_proto: str = None,
    ):
        # The cookie configures for the server.
        self.cookie = cookie
        # The maximum amount of time to wait before the session cookie expires. Unit: seconds.
        # 
        # Valid values: **1** to **86400**.
        self.cookie_timeout = cookie_timeout
        # The listener port that is used for HTTP-to-HTTPS redirection.
        # 
        # >  If the **ListenerForward** parameter is set to **off**, this parameter is not returned.
        self.forward_port = forward_port
        # Indicates whether GZIP compression is enabled. Valid values:
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
        # >  This parameter takes effect only when **HealthCheck** is set to **on**.
        self.health_check_connect_port = health_check_connect_port
        # The domain name that is used for health checks.
        self.health_check_domain = health_check_domain
        # The HTTP status code that indicates a healthy backend server.
        self.health_check_http_code = health_check_http_code
        # The HTTP version for health checks.
        self.health_check_http_version = health_check_http_version
        # The interval at which health checks are performed. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The health check method. Valid values: **head** and **get**.
        self.health_check_method = health_check_method
        # The maximum timeout period of a health check. Unit: seconds.
        self.health_check_timeout = health_check_timeout
        # The protocol that you want to use for health checks.
        self.health_check_type = health_check_type
        # The URI that is used for health checks.
        self.health_check_uri = health_check_uri
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health check status of the backend server changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1** to **60**.
        # 
        # If no request is received within the specified timeout period, CLB closes the connection. When a request is received, CLB establishes a new connection.
        self.idle_timeout = idle_timeout
        # Indicates whether HTTP-to-HTTPS redirection is enabled for the listener. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.listener_forward = listener_forward
        # The timeout period of a request. Unit: seconds. Valid values: **1** to **180**.
        # 
        # If no response is received from a backend server during the request timeout period, CLB sends the `HTTP 504` status code to the client.
        self.request_timeout = request_timeout
        # Indicates whether session persistence is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.sticky_session = sticky_session
        # The method used to handle the cookie. Valid values:
        # 
        # *   **insert**: inserts a cookie. CLB inserts the SERVERID cookie to the HTTP or HTTPS response to the first request from a client. Subsequent requests that carry the SERVERID cookie from the client are forwarded to the same backend server as the first request.
        # *   **server**: rewrites the original cookie. CLB rewrites the custom cookies in requests from a client. Subsequent requests from the client that carry the new cookie are forwarded to the same backend server as the first request.
        self.sticky_session_type = sticky_session_type
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health check status of the backend server changes from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        self.unhealthy_threshold = unhealthy_threshold
        # Indicates whether the `X-Forwarded-For` header is used to preserve client IP addresses. Valid values:
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
        # Indicates whether the `SLB-IP` header is used to retrieve the VIP of the client. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_slbip = xforwarded_for_slbip
        # Indicates whether the `XForwardedFor_SLBPORT` header is used to retrieve the listener port of the CLB instance. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_slbport = xforwarded_for_slbport
        # Indicates whether the `X-Forwarded-Proto` header is used to obtain the listener protocol. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.xforwarded_for_proto = xforwarded_for_proto

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

        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method

        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

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
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

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

        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')

        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

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

