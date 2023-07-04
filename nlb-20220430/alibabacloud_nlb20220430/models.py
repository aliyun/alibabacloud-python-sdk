# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddServersToServerGroupRequestServers(TeaModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        weight: int = None,
    ):
        # The description of the servers.
        # 
        # The description must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        # 
        # >  You can specify at most 40 servers in each call.
        self.description = description
        # The port used by the backend server. Valid values: **1** to **65535**.
        # 
        # >  You can specify at most 40 servers in each call.
        self.port = port
        # The ID of the server. You can specify at most 40 server IDs in each call.
        # 
        # *   If the server group type is **Instance**, set the ServerId parameter to the ID of an Elastic Compute Service (ECS) instance, an elastic network interface (ENI), or an elastic container instance. These backend servers are specified by **Ecs**, **Eni**, or **Eci**.
        # *   If the server group type is **Ip**, set the ServerId parameter to an IP address.
        self.server_id = server_id
        # The IP address of the server. If the server group type is **Ip**, set the ServerId parameter to an IP address.
        # 
        # >  You can specify at most 40 server IP addresses in each call.
        self.server_ip = server_ip
        # The type of the backend server. Valid values:
        # 
        # *   **Ecs**: an ECS instance
        # *   **Eni**: an ENI
        # *   **Eci**: an elastic container instance
        # *   **Ip**: an IP address
        # 
        # >  You can specify at most 40 servers in each call.
        self.server_type = server_type
        # The weight of the backend server. Valid values: **0** to **100**. Default value: **100**. If the weight of a backend server is set to **0**, no requests are forwarded to the backend server.
        # 
        # >  You can specify at most 40 servers in each call.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class AddServersToServerGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        server_group_id: str = None,
        servers: List[AddServersToServerGroupRequestServers] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not add the servers to the server group. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the server group.
        self.server_group_id = server_group_id
        self.servers = servers

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = AddServersToServerGroupRequestServers()
                self.servers.append(temp_model.from_map(k))
        return self


class AddServersToServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        server_group_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the server group.
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class AddServersToServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddServersToServerGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddServersToServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAdditionalCertificatesWithListenerRequest(TeaModel):
    def __init__(
        self,
        additional_certificate_ids: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.additional_certificate_ids = additional_certificate_ids
        self.client_token = client_token
        self.dry_run = dry_run
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_certificate_ids is not None:
            result['AdditionalCertificateIds'] = self.additional_certificate_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalCertificateIds') is not None:
            self.additional_certificate_ids = m.get('AdditionalCertificateIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateAdditionalCertificatesWithListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateAdditionalCertificatesWithListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateAdditionalCertificatesWithListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateAdditionalCertificatesWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachCommonBandwidthPackageToLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
    ):
        # The ID of the EIP bandwidth plan.
        self.bandwidth_package_id = bandwidth_package_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not associate the EIP bandwidth plan with the NLB instance. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachCommonBandwidthPackageToLoadBalancerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachCommonBandwidthPackageToLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachCommonBandwidthPackageToLoadBalancerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachCommonBandwidthPackageToLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateListenerRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateListenerRequest(TeaModel):
    def __init__(
        self,
        alpn_enabled: bool = None,
        alpn_policy: str = None,
        ca_certificate_ids: List[str] = None,
        ca_enabled: bool = None,
        certificate_ids: List[str] = None,
        client_token: str = None,
        cps: int = None,
        dry_run: bool = None,
        end_port: int = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
        mss: int = None,
        proxy_protocol_enabled: bool = None,
        region_id: str = None,
        sec_sensor_enabled: bool = None,
        security_policy_id: str = None,
        server_group_id: str = None,
        start_port: int = None,
        tag: List[CreateListenerRequestTag] = None,
    ):
        # Specifies whether to enable Application-Layer Protocol Negotiation (ALPN). Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.alpn_enabled = alpn_enabled
        # The ALPN policy.
        self.alpn_policy = alpn_policy
        self.ca_certificate_ids = ca_certificate_ids
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.ca_enabled = ca_enabled
        self.certificate_ids = certificate_ids
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **0** to **1000000**. **0** specifies that the number of connections is unlimited.
        self.cps = cps
        # Specifies whether to only precheck this request. Valid values:
        # 
        # *   **true**: prechecks the request without creating the resource. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The last port in the listening port range. Valid values: **0** to **65535**.
        # 
        # The number of the last port must be larger than that of the first port.
        self.end_port = end_port
        # The timeout period of an idle connection. Unit: seconds.
        # 
        # Valid values: **1** to **900**. Default value: **900**.
        self.idle_timeout = idle_timeout
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.listener_description = listener_description
        # The listening port. Valid values: **0** to **65535**.
        # 
        # If you set the value to **0**, the listener listens by port range. If you set the value to **0**, you must also set the **StartPort** and **EndPort** parameters.
        self.listener_port = listener_port
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The maximum size of a TCP segment. Unit: bytes. Valid values: **0** to **1500**.
        # 
        # **0** specifies that the maximum segment size remains unchanged.
        # 
        # >  This parameter is supported only by listeners that use SSL over TCP.
        self.mss = mss
        # Specifies whether to use the Proxy protocol to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # Specifies whether to enable fine-grained monitoring. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.sec_sensor_enabled = sec_sensor_enabled
        # The ID of the security policy. System security policies and custom security policies are supported.
        # 
        # Valid values: **tls_cipher_policy\_1\_0** (default), **tls_cipher_policy\_1\_1**, **tls_cipher_policy\_1\_2**, **tls_cipher_policy\_1\_2\_strict**, and **tls_cipher_policy\_1\_2\_strict_with\_1\_3**.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The first port in the listening port range. Valid values: **0** to **65535**.
        self.start_port = start_port
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled
        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy
        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.end_port is not None:
            result['EndPort'] = self.end_port
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.mss is not None:
            result['Mss'] = self.mss
        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.start_port is not None:
            result['StartPort'] = self.start_port
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')
        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')
        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Mss') is not None:
            self.mss = m.get('Mss')
        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateListenerRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        listener_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the listener.
        self.listener_id = listener_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerRequestDeletionProtectionConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        reason: str = None,
    ):
        # Specifies whether to enable deletion protection. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.enabled = enabled
        # The reason why the deletion protection feature is enabled or disabled. The value must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class CreateLoadBalancerRequestLoadBalancerBillingConfig(TeaModel):
    def __init__(
        self,
        pay_type: str = None,
    ):
        # The billing method of the NLB instance.
        # 
        # Set the value to **PostPay**, which specifies the pay-as-you-go billing method.
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class CreateLoadBalancerRequestModificationProtectionConfig(TeaModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
    ):
        # The reason why the configuration read-only mode is enabled. The value must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter.
        # 
        # >  This parameter takes effect only if the **Status** parameter is set to **ConsoleProtection**.
        self.reason = reason
        # Specifies whether to enable the configuration read-only mode. Valid values:
        # 
        # *   **NonProtection**: does not enable the configuration read-only mode. You cannot set the **Reason** parameter. If the **Reason** parameter is set, the value is cleared.
        # *   **ConsoleProtection**: enables the configuration read-only mode. You can set the **Reason** parameter.
        # 
        # >  If you set this parameter to **ConsoleProtection**, you cannot use the NLB console to modify instance configurations. However, you can call API operations to modify instance configurations.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateLoadBalancerRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateLoadBalancerRequestZoneMappings(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        private_ipv_4address: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the elastic IP address (EIP) that is associated with the Internet-facing NLB instance. You can specify one EIP for each zone. You must add at least two zones. You can add a maximum of 10 zones.
        self.allocation_id = allocation_id
        # The private IP address. You must add at least two zones. You can add a maximum of 10 zones.
        self.private_ipv_4address = private_ipv_4address
        # The vSwitch in the zone. You can specify only one vSwitch (subnet) in each zone of an NLB instance. You must add at least two zones. You can add a maximum of 10 zones.
        self.v_switch_id = v_switch_id
        # The ID of the zone of the NLB instance. You must add at least two zones. You can add a maximum of 10 zones.
        # 
        # You can call the [DescribeZones](~~443890~~) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.private_ipv_4address is not None:
            result['PrivateIPv4Address'] = self.private_ipv_4address
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        address_ip_version: str = None,
        address_type: str = None,
        bandwidth_package_id: str = None,
        client_token: str = None,
        deletion_protection_config: CreateLoadBalancerRequestDeletionProtectionConfig = None,
        dry_run: bool = None,
        load_balancer_billing_config: CreateLoadBalancerRequestLoadBalancerBillingConfig = None,
        load_balancer_name: str = None,
        load_balancer_type: str = None,
        modification_protection_config: CreateLoadBalancerRequestModificationProtectionConfig = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[CreateLoadBalancerRequestTag] = None,
        vpc_id: str = None,
        zone_mappings: List[CreateLoadBalancerRequestZoneMappings] = None,
    ):
        # The protocol version. Valid values:
        # 
        # *   **ipv4:** IPv4. This is the default value.
        # *   **DualStack:** dual stack.
        self.address_ip_version = address_ip_version
        # The type of IPv4 address used by the NLB instance. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. Therefore, the NLB instance can be accessed over the virtual private cloud (VPC) where the NLB instance is deployed.
        # 
        # >  To enable a public IPv6 address for an NLB instance, call the [EnableLoadBalancerIpv6Internet](~~445878~~) operation.
        self.address_type = address_type
        # The ID of the EIP bandwidth plan that is associated with the Internet-facing NLB instance.
        self.bandwidth_package_id = bandwidth_package_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request is different.
        self.client_token = client_token
        # The configuration of the deletion protection feature.
        self.deletion_protection_config = deletion_protection_config
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. This is the default value. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The billing settings of the NLB instance.
        self.load_balancer_billing_config = load_balancer_billing_config
        # The name of the NLB instance.
        # 
        # The value must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter.
        self.load_balancer_name = load_balancer_name
        # The type of the instance. Set the value to **network**, which specifies an NLB instance.
        self.load_balancer_type = load_balancer_type
        # The configuration of the configuration read-only mode.
        self.modification_protection_config = modification_protection_config
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.tag = tag
        # The ID of the VPC where the NLB instance is deployed.
        self.vpc_id = vpc_id
        # The mappings between zones and vSwitches. You must add at least two zones. You can add a maximum of 10 zones.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type
        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeletionProtectionConfig') is not None:
            temp_model = CreateLoadBalancerRequestDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m['DeletionProtectionConfig'])
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = CreateLoadBalancerRequestLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m['LoadBalancerBillingConfig'])
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')
        if m.get('ModificationProtectionConfig') is not None:
            temp_model = CreateLoadBalancerRequestModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m['ModificationProtectionConfig'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateLoadBalancerRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = CreateLoadBalancerRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class CreateLoadBalancerResponseBody(TeaModel):
    def __init__(
        self,
        loadbalancer_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        # The ID of the NLB instance.
        self.loadbalancer_id = loadbalancer_id
        # The ID of the order for the NLB instance.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.loadbalancer_id is not None:
            result['LoadbalancerId'] = self.loadbalancer_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadbalancerId') is not None:
            self.loadbalancer_id = m.get('LoadbalancerId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLoadBalancerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecurityPolicyRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateSecurityPolicyRequest(TeaModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_policy_name: str = None,
        tag: List[CreateSecurityPolicyRequestTag] = None,
        tls_versions: List[str] = None,
    ):
        self.ciphers = ciphers
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: checks the request but does not create the security policy. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the security policy.
        # 
        # The name must be 1 to 200 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        self.security_policy_name = security_policy_name
        self.tag = tag
        self.tls_versions = tls_versions

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.tls_versions is not None:
            result['TlsVersions'] = self.tls_versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateSecurityPolicyRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TlsVersions') is not None:
            self.tls_versions = m.get('TlsVersions')
        return self


class CreateSecurityPolicyResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        security_policy_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        return self


class CreateSecurityPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSecurityPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSecurityPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServerGroupRequestHealthCheckConfig(TeaModel):
    def __init__(
        self,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_enabled: bool = None,
        health_check_http_code: List[str] = None,
        health_check_interval: int = None,
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
        # Default value: **0**. If you set the value to 0, the port of a backend server is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The maximum timeout period of a health check response. Unit: seconds.
        # 
        # Valid values: **1** to **300**.
        # 
        # Default value: **5**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$SERVER_IP:** the private IP address of a backend server.
        # *   **domain:** the domain name you want to use for health checks. The domain name must be 1 to 80 characters in length and can contain lowercase letters, digits, hyphens (-), and periods (.).
        # 
        # >  This parameter takes effect only when you set **HealthCheckType** to **HTTP**.
        self.health_check_domain = health_check_domain
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **true:** yes. This is the default value.
        # *   **false:** no.
        self.health_check_enabled = health_check_enabled
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Unit: seconds.
        # 
        # Valid values: **5** to **5000**.
        # 
        # Default value: **10**.
        self.health_check_interval = health_check_interval
        # The protocol that is used for health checks. Valid values: **TCP** (default) and **HTTP**.
        self.health_check_type = health_check_type
        # The path to which health check requests are sent.
        # 
        # The path must be 1 to 80 characters in length, and can contain only letters, digits, and the following special characters: `- / . % ? # & =`. It can also contain the following extended characters: `_ ; ~ ! ( ) * [ ] @ $ ^ : \" , +`. The path must start with a forward slash (/).
        # 
        # >  This parameter takes effect only when you set **HealthCheckType** to **HTTP**.
        self.health_check_url = health_check_url
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        # 
        # Default value: **2**.
        self.healthy_threshold = healthy_threshold
        # The HTTP method that is used for health checks. Valid values: **GET** (default) and **HEAD**.
        # 
        # >  This parameter takes effect only when you set **HealthCheckType** to **HTTP**.
        self.http_check_method = http_check_method
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        # 
        # Default value: **2**.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
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
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
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


class CreateServerGroupRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateServerGroupRequest(TeaModel):
    def __init__(
        self,
        address_ipversion: str = None,
        any_port_enabled: bool = None,
        client_token: str = None,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
        dry_run: bool = None,
        health_check_config: CreateServerGroupRequestHealthCheckConfig = None,
        preserve_client_ip_enabled: bool = None,
        protocol: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        scheduler: str = None,
        server_group_name: str = None,
        server_group_type: str = None,
        tag: List[CreateServerGroupRequestTag] = None,
        vpc_id: str = None,
    ):
        # The protocol version. Valid values:
        # 
        # *   **ipv4:** IPv4. This is the default value.
        # *   **DualStack:** dual stack.
        self.address_ipversion = address_ipversion
        # Specifies whether to enable all-port forwarding. Valid values:
        # 
        # *   **true:** yes.
        # *   **false:** no. This is the default value.
        self.any_port_enabled = any_port_enabled
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The value of **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to enable connection draining. Valid values:
        # 
        # *   **true:** yes.
        # *   **false:** no. This is the default value.
        self.connection_drain_enabled = connection_drain_enabled
        # The timeout period of connection draining. Unit: seconds.
        # 
        # Valid values: **10** to **900**.
        self.connection_drain_timeout = connection_drain_timeout
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true:** performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false:** performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        self.health_check_config = health_check_config
        # Specifies whether to enable client IP preservation. Valid values:
        # 
        # *   **true:** yes.
        # *   **false:** no. This is the default value.
        self.preserve_client_ip_enabled = preserve_client_ip_enabled
        # The protocol used to forward requests to the backend servers. Valid values:
        # 
        # *   **TCP:** This is the default value.
        # *   **UDP**\
        # *   **TCPSSL**\
        self.protocol = protocol
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the server group belongs.
        self.resource_group_id = resource_group_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **Wrr:** The weighted round-robin algorithm is used. Backend servers with higher weights receive more requests than backend servers with lower weights. This is the default value.
        # *   **rr:** The round-robin algorithm is used. Requests are forwarded to backend servers in sequence.
        # *   **sch:** Source IP hashing is used. Requests from the same source IP address are forwarded to the same backend server.
        # *   **tch:** Four-element hashing is used. It specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are forwarded to the same backend server.
        # *   **qch:** QUIC ID hashing is used. Requests that contain the same QUIC ID are forwarded to the same backend server.
        self.scheduler = scheduler
        # The name of the server group.
        # 
        # The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The name must start with a letter.
        self.server_group_name = server_group_name
        # The type of the server group. Valid values:
        # 
        # *   **Instance:** allows you to add servers of the **Ecs**, **Ens**, or **Eci** type. This is the default value.
        # *   **Ip:** allows you to add servers by specifying IP addresses.
        self.server_group_type = server_group_type
        self.tag = tag
        # The ID of the VPC to which the server group belongs.
        # 
        # >  If **ServerGroupType** is set to **Instance**, only servers in the specified VPC can be added to the server group.
        self.vpc_id = vpc_id

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.any_port_enabled is not None:
            result['AnyPortEnabled'] = self.any_port_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_drain_enabled is not None:
            result['ConnectionDrainEnabled'] = self.connection_drain_enabled
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()
        if self.preserve_client_ip_enabled is not None:
            result['PreserveClientIpEnabled'] = self.preserve_client_ip_enabled
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name
        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('AnyPortEnabled') is not None:
            self.any_port_enabled = m.get('AnyPortEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionDrainEnabled') is not None:
            self.connection_drain_enabled = m.get('ConnectionDrainEnabled')
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('HealthCheckConfig') is not None:
            temp_model = CreateServerGroupRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['HealthCheckConfig'])
        if m.get('PreserveClientIpEnabled') is not None:
            self.preserve_client_ip_enabled = m.get('PreserveClientIpEnabled')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')
        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateServerGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        server_group_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the server group.
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class CreateServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServerGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteListenerRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not delete the listener. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the listener.
        self.listener_id = listener_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to only precheck this request. Valid values:
        # 
        # *   **true**: prechecks the request without deleting the NLB instance. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteLoadBalancerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLoadBalancerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecurityPolicyRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        security_policy_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can only contain ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the available regions.
        self.region_id = region_id
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        return self


class DeleteSecurityPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSecurityPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSecurityPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSecurityPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServerGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        server_group_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can only contain ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the server group.
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class DeleteServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServerGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        service_code: str = None,
    ):
        # The supported natural language. Valid values:
        # 
        # *   **zh-CN**: Chinese
        # *   **en-US** (default): English
        # *   **ja**: Japanese
        self.accept_language = accept_language
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token
        # The service code. Set the value to **nlb**.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The name of the region.
        self.local_name = local_name
        # The endpoint of the region service.
        self.region_endpoint = region_endpoint
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # A list of regions.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        client_token: str = None,
        region_id: str = None,
        service_code: str = None,
    ):
        # The supported natural language. Valid values:
        # 
        # *   **zh-CN**: Chinese
        # *   **en-US** (default): English
        # *   **ja**: Japanese
        self.accept_language = accept_language
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token
        # The ID of the region to which the zone belongs. You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The service code. Set the value to **nlb**.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        # The name of the zone.
        self.local_name = local_name
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: List[DescribeZonesResponseBodyZones] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZonesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachCommonBandwidthPackageFromLoadBalancerRequest(TeaModel):
    def __init__(
        self,
        bandwidth_package_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
    ):
        # The ID of the EIP bandwidth plan.
        self.bandwidth_package_id = bandwidth_package_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not disassociate the NLB instance from the EIP bandwidth plan. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachCommonBandwidthPackageFromLoadBalancerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachCommonBandwidthPackageFromLoadBalancerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachCommonBandwidthPackageFromLoadBalancerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachCommonBandwidthPackageFromLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableLoadBalancerIpv6InternetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not change the network type of the NLB instance. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableLoadBalancerIpv6InternetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableLoadBalancerIpv6InternetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableLoadBalancerIpv6InternetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableLoadBalancerIpv6InternetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateAdditionalCertificatesWithListenerRequest(TeaModel):
    def __init__(
        self,
        additional_certificate_ids: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        self.additional_certificate_ids = additional_certificate_ids
        self.client_token = client_token
        self.dry_run = dry_run
        self.listener_id = listener_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_certificate_ids is not None:
            result['AdditionalCertificateIds'] = self.additional_certificate_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalCertificateIds') is not None:
            self.additional_certificate_ids = m.get('AdditionalCertificateIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisassociateAdditionalCertificatesWithListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociateAdditionalCertificatesWithListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisassociateAdditionalCertificatesWithListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateAdditionalCertificatesWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableLoadBalancerIpv6InternetRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not change the network type of the NLB instance. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableLoadBalancerIpv6InternetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableLoadBalancerIpv6InternetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableLoadBalancerIpv6InternetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableLoadBalancerIpv6InternetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        job_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token
        # The ID of the asynchronous task.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The state of the task. Valid values:
        # 
        # *   **Succeeded**: The task is successful.
        # *   **processing**: The ticket is being executed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: checks the request but does not query the listener details. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the listener.
        self.listener_id = listener_id
        # The ID of the region where the Network Load Balancer (NLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetListenerAttributeResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        alpn_enabled: bool = None,
        alpn_policy: str = None,
        ca_certificate_ids: List[str] = None,
        ca_enabled: bool = None,
        certificate_ids: List[str] = None,
        cps: int = None,
        end_port: str = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        listener_status: str = None,
        load_balancer_id: str = None,
        mss: int = None,
        proxy_protocol_enabled: bool = None,
        region_id: str = None,
        request_id: str = None,
        sec_sensor_enabled: bool = None,
        security_policy_id: str = None,
        server_group_id: str = None,
        start_port: str = None,
        tags: List[GetListenerAttributeResponseBodyTags] = None,
    ):
        # Indicates whether Application-Layer Protocol Negotiation (ALPN) is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.alpn_enabled = alpn_enabled
        # The ALPN policy. Valid values:
        # 
        # *   **HTTP1Only**\
        # *   **HTTP2Only**\
        # *   **HTTP2Preferred**\
        # *   **HTTP2Optional**\
        self.alpn_policy = alpn_policy
        # The CA certificates. Only one CA certificate is supported.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.ca_certificate_ids = ca_certificate_ids
        # Indicates whether mutual authentication is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.ca_enabled = ca_enabled
        # The server certificates. Only one server certificate is supported.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.certificate_ids = certificate_ids
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **0** to **1000000**. **0** specifies that the number of connections is unlimited.
        self.cps = cps
        # The last port in the listening port range. Valid values: **0** to **65535**. The number of the last port must be smaller than that of the first port.
        self.end_port = end_port
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1** to **900**.
        self.idle_timeout = idle_timeout
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.listener_description = listener_description
        # The ID of the listener.
        self.listener_id = listener_id
        # The listening port. Valid values: **0** to **65535**. A value of **0** specifies all ports. If you set the value to **0**, you must also set the **StartPort** and **EndPort** parameters.
        self.listener_port = listener_port
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol
        # The status of the listener. Valid values:
        # 
        # *   **Provisioning**: The listener is being created.
        # *   **Running**: The listener is running.
        # *   **Configuring**: The listener is being configured.
        # *   **Stopping**: The listener is being stopped.
        # *   **Stopped**: The listener is stopped.
        # *   **Starting**: The listener is being started.
        # *   **Deleting**: The listener is being deleted.
        # *   **Deleted**: The listener is deleted.
        self.listener_status = listener_status
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The size of the largest TCP segment. Unit: bytes. Valid values: **0** to **1500**. **0** specifies that the maximum segment size remains unchanged.
        # 
        # >  This parameter is supported only by listeners that use SSL over TCP.
        self.mss = mss
        # Indicates whether the Proxy protocol is used to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # The ID of the region where the NLB instance is deployed.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether fine-grained monitoring is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sec_sensor_enabled = sec_sensor_enabled
        # The ID of the security policy. System security policies and custom security policies are supported.
        # 
        # Valid values: **tls_cipher_policy\_1\_0**, **tls_cipher_policy\_1\_1**, **tls_cipher_policy\_1\_2**, **tls_cipher_policy\_1\_2\_strict**, and **tls_cipher_policy\_1\_2\_strict_with\_1\_3**.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The first port in the listening port range. Valid values: **0** to **65535**.
        self.start_port = start_port
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled
        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy
        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.end_port is not None:
            result['EndPort'] = self.end_port
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.listener_status is not None:
            result['ListenerStatus'] = self.listener_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.mss is not None:
            result['Mss'] = self.mss
        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.start_port is not None:
            result['StartPort'] = self.start_port
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')
        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')
        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('ListenerStatus') is not None:
            self.listener_status = m.get('ListenerStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Mss') is not None:
            self.mss = m.get('Mss')
        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetListenerAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetListenerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetListenerHealthStatusRequest(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The ID of the listener of the NLB instance.
        self.listener_id = listener_id
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason(TeaModel):
    def __init__(
        self,
        reason_code: str = None,
    ):
        # The reason why the **status** is abnormal. Valid values:
        # 
        # *   **CONNECT_TIMEOUT**: The NLB instance failed to connect to the backend server within the specified period of time.
        # *   **CONNECT_FAILED**: The NLB instance failed to connect to the backend server.
        # *   **RECV_RESPONSE_TIMEOUT**: The NLB instance failed to receive a response from the backend server within the specified period of time.
        # *   **CONNECT_INTERRUPT**: The connection between the health check and the backend servers was interrupted.
        # *   **HTTP_CODE_NOT_MATCH**: The HTTP status code from the backend servers was not the expected one.
        # *   **HTTP_INVALID_HEADER**: The format of the response from the backend servers is invalid.
        self.reason_code = reason_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers(TeaModel):
    def __init__(
        self,
        port: int = None,
        reason: GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason = None,
        server_id: str = None,
        server_ip: str = None,
        status: str = None,
    ):
        # The backend port.
        self.port = port
        # The cause of the health check failure.
        self.reason = reason
        # The ID of the backend server.
        self.server_id = server_id
        # The IP address of the backend server.
        self.server_ip = server_ip
        # The health check status. Valid values:
        # 
        # *   **Initial**: indicates that health checks are configured for the NLB instance, but no data was found.
        # *   **Unhealthy**: indicates that the backend server consecutively fails health checks.
        # *   **Unused**: indicates that the weight of the backend server is 0.
        # *   **Unavailable**: indicates that health checks are disabled.
        self.status = status

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Reason') is not None:
            temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos(TeaModel):
    def __init__(
        self,
        heath_check_enabled: bool = None,
        non_normal_servers: List[GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers] = None,
        server_group_id: str = None,
    ):
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.heath_check_enabled = heath_check_enabled
        # A list of unhealthy backend servers.
        self.non_normal_servers = non_normal_servers
        # The ID of the server group.
        self.server_group_id = server_group_id

    def validate(self):
        if self.non_normal_servers:
            for k in self.non_normal_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.heath_check_enabled is not None:
            result['HeathCheckEnabled'] = self.heath_check_enabled
        result['NonNormalServers'] = []
        if self.non_normal_servers is not None:
            for k in self.non_normal_servers:
                result['NonNormalServers'].append(k.to_map() if k else None)
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeathCheckEnabled') is not None:
            self.heath_check_enabled = m.get('HeathCheckEnabled')
        self.non_normal_servers = []
        if m.get('NonNormalServers') is not None:
            for k in m.get('NonNormalServers'):
                temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers()
                self.non_normal_servers.append(temp_model.from_map(k))
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatus(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        server_group_infos: List[GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos] = None,
    ):
        # The ID of the listener of the NLB instance.
        self.listener_id = listener_id
        # The listening port.
        self.listener_port = listener_port
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol
        # The information about the server groups.
        self.server_group_infos = server_group_infos

    def validate(self):
        if self.server_group_infos:
            for k in self.server_group_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        result['ServerGroupInfos'] = []
        if self.server_group_infos is not None:
            for k in self.server_group_infos:
                result['ServerGroupInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        self.server_group_infos = []
        if m.get('ServerGroupInfos') is not None:
            for k in m.get('ServerGroupInfos'):
                temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos()
                self.server_group_infos.append(temp_model.from_map(k))
        return self


class GetListenerHealthStatusResponseBody(TeaModel):
    def __init__(
        self,
        listener_health_status: List[GetListenerHealthStatusResponseBodyListenerHealthStatus] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The health check status of the server groups that are associated with the listener.
        self.listener_health_status = listener_health_status
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # - If **NextToken** is empty, it indicates that no next query is to be sent.
        # - If a value of **NextToken** is returned, the value is the token used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.listener_health_status:
            for k in self.listener_health_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListenerHealthStatus'] = []
        if self.listener_health_status is not None:
            for k in self.listener_health_status:
                result['ListenerHealthStatus'].append(k.to_map() if k else None)
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
        self.listener_health_status = []
        if m.get('ListenerHealthStatus') is not None:
            for k in m.get('ListenerHealthStatus'):
                temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatus()
                self.listener_health_status.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetListenerHealthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetListenerHealthStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetListenerHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoadBalancerAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        self.load_balancer_id = load_balancer_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        enabled_time: str = None,
        reason: str = None,
    ):
        self.enabled = enabled
        self.enabled_time = enabled_time
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig(TeaModel):
    def __init__(
        self,
        pay_type: str = None,
    ):
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class GetLoadBalancerAttributeResponseBodyModificationProtectionConfig(TeaModel):
    def __init__(
        self,
        enabled_time: str = None,
        reason: str = None,
        status: str = None,
    ):
        self.enabled_time = enabled_time
        self.reason = reason
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetLoadBalancerAttributeResponseBodyOperationLocks(TeaModel):
    def __init__(
        self,
        lock_reason: str = None,
        lock_type: str = None,
    ):
        self.lock_reason = lock_reason
        self.lock_type = lock_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.lock_type is not None:
            result['LockType'] = self.lock_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('LockType') is not None:
            self.lock_type = m.get('LockType')
        return self


class GetLoadBalancerAttributeResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        eni_id: str = None,
        ipv_6address: str = None,
        private_ipv_4address: str = None,
        private_ipv_4hc_status: str = None,
        private_ipv_6hc_status: str = None,
        public_ipv_4address: str = None,
    ):
        self.allocation_id = allocation_id
        self.eni_id = eni_id
        self.ipv_6address = ipv_6address
        self.private_ipv_4address = private_ipv_4address
        self.private_ipv_4hc_status = private_ipv_4hc_status
        self.private_ipv_6hc_status = private_ipv_6hc_status
        self.public_ipv_4address = public_ipv_4address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address
        if self.private_ipv_4address is not None:
            result['PrivateIPv4Address'] = self.private_ipv_4address
        if self.private_ipv_4hc_status is not None:
            result['PrivateIPv4HcStatus'] = self.private_ipv_4hc_status
        if self.private_ipv_6hc_status is not None:
            result['PrivateIPv6HcStatus'] = self.private_ipv_6hc_status
        if self.public_ipv_4address is not None:
            result['PublicIPv4Address'] = self.public_ipv_4address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')
        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')
        if m.get('PrivateIPv4HcStatus') is not None:
            self.private_ipv_4hc_status = m.get('PrivateIPv4HcStatus')
        if m.get('PrivateIPv6HcStatus') is not None:
            self.private_ipv_6hc_status = m.get('PrivateIPv6HcStatus')
        if m.get('PublicIPv4Address') is not None:
            self.public_ipv_4address = m.get('PublicIPv4Address')
        return self


class GetLoadBalancerAttributeResponseBodyZoneMappings(TeaModel):
    def __init__(
        self,
        load_balancer_addresses: List[GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses] = None,
        status: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.load_balancer_addresses = load_balancer_addresses
        self.status = status
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.load_balancer_addresses:
            for k in self.load_balancer_addresses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LoadBalancerAddresses'] = []
        if self.load_balancer_addresses is not None:
            for k in self.load_balancer_addresses:
                result['LoadBalancerAddresses'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer_addresses = []
        if m.get('LoadBalancerAddresses') is not None:
            for k in m.get('LoadBalancerAddresses'):
                temp_model = GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses()
                self.load_balancer_addresses.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetLoadBalancerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        address_ip_version: str = None,
        address_type: str = None,
        bandwidth_package_id: str = None,
        cps: int = None,
        create_time: str = None,
        cross_zone_enabled: bool = None,
        dnsname: str = None,
        deletion_protection_config: GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig = None,
        ipv_6address_type: str = None,
        load_balancer_billing_config: GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig = None,
        load_balancer_business_status: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_status: str = None,
        load_balancer_type: str = None,
        modification_protection_config: GetLoadBalancerAttributeResponseBodyModificationProtectionConfig = None,
        operation_locks: List[GetLoadBalancerAttributeResponseBodyOperationLocks] = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        security_group_ids: List[str] = None,
        tags: List[GetLoadBalancerAttributeResponseBodyTags] = None,
        vpc_id: str = None,
        zone_mappings: List[GetLoadBalancerAttributeResponseBodyZoneMappings] = None,
    ):
        self.address_ip_version = address_ip_version
        self.address_type = address_type
        self.bandwidth_package_id = bandwidth_package_id
        self.cps = cps
        self.create_time = create_time
        self.cross_zone_enabled = cross_zone_enabled
        self.dnsname = dnsname
        self.deletion_protection_config = deletion_protection_config
        self.ipv_6address_type = ipv_6address_type
        self.load_balancer_billing_config = load_balancer_billing_config
        self.load_balancer_business_status = load_balancer_business_status
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name
        self.load_balancer_status = load_balancer_status
        self.load_balancer_type = load_balancer_type
        self.modification_protection_config = modification_protection_config
        self.operation_locks = operation_locks
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.security_group_ids = security_group_ids
        self.tags = tags
        self.vpc_id = vpc_id
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.operation_locks:
            for k in self.operation_locks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_zone_enabled is not None:
            result['CrossZoneEnabled'] = self.cross_zone_enabled
        if self.dnsname is not None:
            result['DNSName'] = self.dnsname
        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()
        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type
        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()
        if self.load_balancer_business_status is not None:
            result['LoadBalancerBusinessStatus'] = self.load_balancer_business_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type
        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()
        result['OperationLocks'] = []
        if self.operation_locks is not None:
            for k in self.operation_locks:
                result['OperationLocks'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')
        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')
        if m.get('DeletionProtectionConfig') is not None:
            temp_model = GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m['DeletionProtectionConfig'])
        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')
        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m['LoadBalancerBillingConfig'])
        if m.get('LoadBalancerBusinessStatus') is not None:
            self.load_balancer_business_status = m.get('LoadBalancerBusinessStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')
        if m.get('ModificationProtectionConfig') is not None:
            temp_model = GetLoadBalancerAttributeResponseBodyModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m['ModificationProtectionConfig'])
        self.operation_locks = []
        if m.get('OperationLocks') is not None:
            for k in m.get('OperationLocks'):
                temp_model = GetLoadBalancerAttributeResponseBodyOperationLocks()
                self.operation_locks.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetLoadBalancerAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = GetLoadBalancerAttributeResponseBodyZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class GetLoadBalancerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLoadBalancerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLoadBalancerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenerCertificatesRequest(TeaModel):
    def __init__(
        self,
        cert_type: str = None,
        listener_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.cert_type = cert_type
        self.listener_id = listener_id
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListListenerCertificatesResponseBodyCertificates(TeaModel):
    def __init__(
        self,
        certificate_id: str = None,
        certificate_type: str = None,
        is_default: bool = None,
        status: str = None,
    ):
        self.certificate_id = certificate_id
        self.certificate_type = certificate_type
        self.is_default = is_default
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListListenerCertificatesResponseBody(TeaModel):
    def __init__(
        self,
        certificate_ids: List[str] = None,
        certificates: List[ListListenerCertificatesResponseBodyCertificates] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.certificate_ids = certificate_ids
        self.certificates = certificates
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
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
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = ListListenerCertificatesResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenerCertificatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListListenerCertificatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListListenerCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListListenersRequest(TeaModel):
    def __init__(
        self,
        listener_ids: List[str] = None,
        listener_protocol: str = None,
        load_balancer_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        tag: List[ListListenersRequestTag] = None,
    ):
        self.listener_ids = listener_ids
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol
        self.load_balancer_ids = load_balancer_ids
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_ids is not None:
            result['ListenerIds'] = self.listener_ids
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerIds') is not None:
            self.listener_ids = m.get('ListenerIds')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListListenersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListListenersResponseBodyListenersTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListListenersResponseBodyListeners(TeaModel):
    def __init__(
        self,
        alpn_enabled: bool = None,
        alpn_policy: str = None,
        ca_certificate_ids: List[str] = None,
        ca_enabled: bool = None,
        certificate_ids: List[str] = None,
        cps: int = None,
        end_port: str = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        listener_status: str = None,
        load_balancer_id: str = None,
        mss: int = None,
        proxy_protocol_enabled: bool = None,
        region_id: str = None,
        sec_sensor_enabled: bool = None,
        security_policy_id: str = None,
        server_group_id: str = None,
        start_port: str = None,
        tags: List[ListListenersResponseBodyListenersTags] = None,
    ):
        # Indicates whether Application-Layer Protocol Negotiation (ALPN) is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.alpn_enabled = alpn_enabled
        # The ALPN policy. Valid values:
        # 
        # *   **HTTP1Only**\
        # *   **HTTP2Only**\
        # *   **HTTP2Preferred**\
        # *   **HTTP2Optional**\
        self.alpn_policy = alpn_policy
        # The list of CA certificates.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.ca_certificate_ids = ca_certificate_ids
        # Indicates whether mutual authentication is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.ca_enabled = ca_enabled
        # The list of server certificates.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.certificate_ids = certificate_ids
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **0** to **1000000**. **0** indicates that the number of connections is unlimited.
        self.cps = cps
        # The last port in the listening port range.
        self.end_port = end_port
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1** to **900**. Default value: **900**.
        self.idle_timeout = idle_timeout
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.listener_description = listener_description
        # The ID of the listener.
        self.listener_id = listener_id
        # The listening port.
        self.listener_port = listener_port
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol
        # The status of the listener. Valid values:
        # 
        # *   **Provisioning**\
        # *   **Running**\
        # *   **Configuring**\
        # *   **Stopping**\
        # *   **Stopped**\
        # *   **Starting**\
        # *   **Deleting**\
        # *   **Deleted**\
        self.listener_status = listener_status
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The maximum size of a TCP segment. Unit: bytes. Valid values: **0** to **1500**. **0** indicates that the maximum segment size remains unchanged.
        # 
        # >  This parameter is supported only by listeners that use SSL over TCP.
        self.mss = mss
        # Indicates whether the Proxy protocol is used to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # The ID of the region where the NLB instance is deployed.
        self.region_id = region_id
        # Indicates whether fine-grained monitoring is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.sec_sensor_enabled = sec_sensor_enabled
        # The ID of the security policy.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The first port in the listening port range.
        self.start_port = start_port
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled
        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy
        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.end_port is not None:
            result['EndPort'] = self.end_port
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.listener_status is not None:
            result['ListenerStatus'] = self.listener_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.mss is not None:
            result['Mss'] = self.mss
        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.start_port is not None:
            result['StartPort'] = self.start_port
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')
        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')
        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('ListenerStatus') is not None:
            self.listener_status = m.get('ListenerStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Mss') is not None:
            self.mss = m.get('Mss')
        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListListenersResponseBodyListenersTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListListenersResponseBody(TeaModel):
    def __init__(
        self,
        listeners: List[ListListenersResponseBodyListeners] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of listeners.
        self.listeners = listeners
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If **NextToken** is empty, it indicates that no next query is to be sent.
        # *   If a value of **NextToken** is returned, the value is the token used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
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
            for k in m.get('Listeners'):
                temp_model = ListListenersResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListListenersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListListenersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLoadBalancersRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListLoadBalancersRequest(TeaModel):
    def __init__(
        self,
        address_ip_version: str = None,
        address_type: str = None,
        dnsname: str = None,
        ipv_6address_type: str = None,
        load_balancer_business_status: str = None,
        load_balancer_ids: List[str] = None,
        load_balancer_names: List[str] = None,
        load_balancer_status: str = None,
        load_balancer_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[ListLoadBalancersRequestTag] = None,
        vpc_ids: List[str] = None,
        zone_id: str = None,
    ):
        self.address_ip_version = address_ip_version
        self.address_type = address_type
        self.dnsname = dnsname
        self.ipv_6address_type = ipv_6address_type
        self.load_balancer_business_status = load_balancer_business_status
        self.load_balancer_ids = load_balancer_ids
        self.load_balancer_names = load_balancer_names
        self.load_balancer_status = load_balancer_status
        self.load_balancer_type = load_balancer_type
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.tag = tag
        self.vpc_ids = vpc_ids
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.dnsname is not None:
            result['DNSName'] = self.dnsname
        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type
        if self.load_balancer_business_status is not None:
            result['LoadBalancerBusinessStatus'] = self.load_balancer_business_status
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.load_balancer_names is not None:
            result['LoadBalancerNames'] = self.load_balancer_names
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')
        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')
        if m.get('LoadBalancerBusinessStatus') is not None:
            self.load_balancer_business_status = m.get('LoadBalancerBusinessStatus')
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('LoadBalancerNames') is not None:
            self.load_balancer_names = m.get('LoadBalancerNames')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListLoadBalancersRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        enabled_time: str = None,
        reason: str = None,
    ):
        self.enabled = enabled
        self.enabled_time = enabled_time
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig(TeaModel):
    def __init__(
        self,
        pay_type: str = None,
    ):
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig(TeaModel):
    def __init__(
        self,
        enabled_time: str = None,
        reason: str = None,
        status: str = None,
    ):
        self.enabled_time = enabled_time
        self.reason = reason
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLoadBalancersResponseBodyLoadBalancersOperationLocks(TeaModel):
    def __init__(
        self,
        lock_reason: str = None,
        lock_type: str = None,
    ):
        self.lock_reason = lock_reason
        self.lock_type = lock_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.lock_type is not None:
            result['LockType'] = self.lock_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('LockType') is not None:
            self.lock_type = m.get('LockType')
        return self


class ListLoadBalancersResponseBodyLoadBalancersTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        eni_id: str = None,
        ipv_6address: str = None,
        private_ipv_4address: str = None,
        private_ipv_4hc_status: str = None,
        private_ipv_6hc_status: str = None,
        public_ipv_4address: str = None,
    ):
        self.allocation_id = allocation_id
        self.eni_id = eni_id
        self.ipv_6address = ipv_6address
        self.private_ipv_4address = private_ipv_4address
        self.private_ipv_4hc_status = private_ipv_4hc_status
        self.private_ipv_6hc_status = private_ipv_6hc_status
        self.public_ipv_4address = public_ipv_4address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address
        if self.private_ipv_4address is not None:
            result['PrivateIPv4Address'] = self.private_ipv_4address
        if self.private_ipv_4hc_status is not None:
            result['PrivateIPv4HcStatus'] = self.private_ipv_4hc_status
        if self.private_ipv_6hc_status is not None:
            result['PrivateIPv6HcStatus'] = self.private_ipv_6hc_status
        if self.public_ipv_4address is not None:
            result['PublicIPv4Address'] = self.public_ipv_4address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')
        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')
        if m.get('PrivateIPv4HcStatus') is not None:
            self.private_ipv_4hc_status = m.get('PrivateIPv4HcStatus')
        if m.get('PrivateIPv6HcStatus') is not None:
            self.private_ipv_6hc_status = m.get('PrivateIPv6HcStatus')
        if m.get('PublicIPv4Address') is not None:
            self.public_ipv_4address = m.get('PublicIPv4Address')
        return self


class ListLoadBalancersResponseBodyLoadBalancersZoneMappings(TeaModel):
    def __init__(
        self,
        load_balancer_addresses: List[ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses] = None,
        status: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.load_balancer_addresses = load_balancer_addresses
        self.status = status
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.load_balancer_addresses:
            for k in self.load_balancer_addresses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LoadBalancerAddresses'] = []
        if self.load_balancer_addresses is not None:
            for k in self.load_balancer_addresses:
                result['LoadBalancerAddresses'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer_addresses = []
        if m.get('LoadBalancerAddresses') is not None:
            for k in m.get('LoadBalancerAddresses'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses()
                self.load_balancer_addresses.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListLoadBalancersResponseBodyLoadBalancers(TeaModel):
    def __init__(
        self,
        address_ip_version: str = None,
        address_type: str = None,
        bandwidth_package_id: str = None,
        create_time: str = None,
        cross_zone_enabled: bool = None,
        dnsname: str = None,
        deletion_protection_config: ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig = None,
        ipv_6address_type: str = None,
        load_balancer_billing_config: ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig = None,
        load_balancer_business_status: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_status: str = None,
        load_balancer_type: str = None,
        modification_protection_config: ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig = None,
        operation_locks: List[ListLoadBalancersResponseBodyLoadBalancersOperationLocks] = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_ids: List[str] = None,
        tags: List[ListLoadBalancersResponseBodyLoadBalancersTags] = None,
        vpc_id: str = None,
        zone_mappings: List[ListLoadBalancersResponseBodyLoadBalancersZoneMappings] = None,
    ):
        self.address_ip_version = address_ip_version
        self.address_type = address_type
        self.bandwidth_package_id = bandwidth_package_id
        self.create_time = create_time
        self.cross_zone_enabled = cross_zone_enabled
        self.dnsname = dnsname
        self.deletion_protection_config = deletion_protection_config
        self.ipv_6address_type = ipv_6address_type
        self.load_balancer_billing_config = load_balancer_billing_config
        self.load_balancer_business_status = load_balancer_business_status
        self.load_balancer_id = load_balancer_id
        self.load_balancer_name = load_balancer_name
        self.load_balancer_status = load_balancer_status
        self.load_balancer_type = load_balancer_type
        self.modification_protection_config = modification_protection_config
        self.operation_locks = operation_locks
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.security_group_ids = security_group_ids
        self.tags = tags
        self.vpc_id = vpc_id
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.operation_locks:
            for k in self.operation_locks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_zone_enabled is not None:
            result['CrossZoneEnabled'] = self.cross_zone_enabled
        if self.dnsname is not None:
            result['DNSName'] = self.dnsname
        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()
        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type
        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()
        if self.load_balancer_business_status is not None:
            result['LoadBalancerBusinessStatus'] = self.load_balancer_business_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type
        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()
        result['OperationLocks'] = []
        if self.operation_locks is not None:
            for k in self.operation_locks:
                result['OperationLocks'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')
        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')
        if m.get('DeletionProtectionConfig') is not None:
            temp_model = ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m['DeletionProtectionConfig'])
        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')
        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m['LoadBalancerBillingConfig'])
        if m.get('LoadBalancerBusinessStatus') is not None:
            self.load_balancer_business_status = m.get('LoadBalancerBusinessStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')
        if m.get('ModificationProtectionConfig') is not None:
            temp_model = ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m['ModificationProtectionConfig'])
        self.operation_locks = []
        if m.get('OperationLocks') is not None:
            for k in m.get('OperationLocks'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancersOperationLocks()
                self.operation_locks.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancersTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancersZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class ListLoadBalancersResponseBody(TeaModel):
    def __init__(
        self,
        load_balancers: List[ListLoadBalancersResponseBodyLoadBalancers] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.load_balancers = load_balancers
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.load_balancers:
            for k in self.load_balancers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LoadBalancers'] = []
        if self.load_balancers is not None:
            for k in self.load_balancers:
                result['LoadBalancers'].append(k.to_map() if k else None)
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
        self.load_balancers = []
        if m.get('LoadBalancers') is not None:
            for k in m.get('LoadBalancers'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLoadBalancersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLoadBalancersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLoadBalancersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecurityPolicyRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag keys. You can specify up to 10 tag keys.
        # 
        # It can be at most 64 characters in length, and cannot contain `http://` or `https://`. It must not start with `aliyun` or `acs:`.
        self.key = key
        # The tag values. You can specify up to 10 tag values.
        # 
        # It can be at most 128 characters in length, and cannot contain `http://` or `https://`. It must not start with `aliyun` or `acs:`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListSecurityPolicyRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_policy_ids: List[str] = None,
        security_policy_names: List[str] = None,
        tag: List[ListSecurityPolicyRequestTag] = None,
    ):
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.security_policy_ids = security_policy_ids
        self.security_policy_names = security_policy_names
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_policy_ids is not None:
            result['SecurityPolicyIds'] = self.security_policy_ids
        if self.security_policy_names is not None:
            result['SecurityPolicyNames'] = self.security_policy_names
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityPolicyIds') is not None:
            self.security_policy_ids = m.get('SecurityPolicyIds')
        if m.get('SecurityPolicyNames') is not None:
            self.security_policy_names = m.get('SecurityPolicyNames')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListSecurityPolicyRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListSecurityPolicyResponseBodySecurityPoliciesRelatedListeners(TeaModel):
    def __init__(
        self,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
    ):
        # The ID of the listener.
        self.listener_id = listener_id
        # The listening port.
        self.listener_port = listener_port
        # The listening protocol. Valid value: **TCPSSL**.
        self.listener_protocol = listener_protocol
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class ListSecurityPolicyResponseBodySecurityPoliciesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag keys. You can specify up to 10 tag keys.
        # 
        # The tag key can be at most 64 characters in length, and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        self.key = key
        # The tag values. You can specify up to 10 tag values.
        # 
        # It can be at most 128 characters in length, and cannot contain `http://` or `https://`. It must not start with `aliyun` or `acs:`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListSecurityPolicyResponseBodySecurityPolicies(TeaModel):
    def __init__(
        self,
        ciphers: str = None,
        region_id: str = None,
        related_listeners: List[ListSecurityPolicyResponseBodySecurityPoliciesRelatedListeners] = None,
        resource_group_id: str = None,
        security_policy_id: str = None,
        security_policy_name: str = None,
        security_policy_status: str = None,
        tags: List[ListSecurityPolicyResponseBodySecurityPoliciesTags] = None,
        tls_version: str = None,
    ):
        # The supported cipher suites, which are determined by the TLS protocol version. You can specify at most 32 cipher suites.
        # 
        # TLS 1.0 and TLS 1.1 support the following cipher suites:
        # 
        # *   **ECDHE-ECDSA-AES128-SHA**\
        # *   **ECDHE-ECDSA-AES256-SHA**\
        # *   **ECDHE-RSA-AES128-SHA**\
        # *   **ECDHE-RSA-AES256-SHA**\
        # *   **AES128-SHA**\
        # *   **AES256-SHA**\
        # *   **DES-CBC3-SHA**\
        # 
        # TLS 1.2 supports the following cipher suites:
        # 
        # *   **ECDHE-ECDSA-AES128-SHA**\
        # *   **ECDHE-ECDSA-AES256-SHA**\
        # *   **ECDHE-RSA-AES128-SHA**\
        # *   **ECDHE-RSA-AES256-SHA**\
        # *   **AES128-SHA**\
        # *   **AES256-SHA**\
        # *   **DES-CBC3-SHA**\
        # *   **ECDHE-ECDSA-AES128-GCM-SHA256**\
        # *   **ECDHE-ECDSA-AES256-GCM-SHA384**\
        # *   **ECDHE-ECDSA-AES128-SHA256**\
        # *   **ECDHE-ECDSA-AES256-SHA384**\
        # *   **ECDHE-RSA-AES128-GCM-SHA256**\
        # *   **ECDHE-RSA-AES256-GCM-SHA384**\
        # *   **ECDHE-RSA-AES128-SHA256**\
        # *   **ECDHE-RSA-AES256-SHA384**\
        # *   **AES128-GCM-SHA256**\
        # *   **AES256-GCM-SHA384**\
        # *   **AES128-SHA256**\
        # *   **AES256-SHA256**\
        # 
        # TLS 1.3 supports the following cipher suites:
        # 
        # *   **TLS_AES\_128\_GCM_SHA256**\
        # *   **TLS_AES\_256\_GCM_SHA384**\
        # *   **TLS_CHACHA20\_POLY1305\_SHA256**\
        # *   **TLS_AES\_128\_CCM_SHA256**\
        # *   **TLS_AES\_128\_CCM\_8\_SHA256**\
        self.ciphers = ciphers
        # The ID of the region where the NLB instance is deployed.
        self.region_id = region_id
        # The listeners that are associated with the NLB instance.
        self.related_listeners = related_listeners
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id
        # The name of the TLS security policy.
        self.security_policy_name = security_policy_name
        # The status of the TLS security policy. Valid values:
        # 
        # *   **Configuring**: The security policy is being configured.
        # *   **Available**: The security policy is available.
        self.security_policy_status = security_policy_status
        # The tags that are added to the NLB instance.
        self.tags = tags
        # The supported versions of the TLS protocol. Valid values: **TLSv1.0**, **TLSv1.1**, **TLSv1.2**, and **TLSv1.3**.
        self.tls_version = tls_version

    def validate(self):
        if self.related_listeners:
            for k in self.related_listeners:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k in self.related_listeners:
                result['RelatedListeners'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        if self.security_policy_status is not None:
            result['SecurityPolicyStatus'] = self.security_policy_status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tls_version is not None:
            result['TlsVersion'] = self.tls_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k in m.get('RelatedListeners'):
                temp_model = ListSecurityPolicyResponseBodySecurityPoliciesRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        if m.get('SecurityPolicyStatus') is not None:
            self.security_policy_status = m.get('SecurityPolicyStatus')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListSecurityPolicyResponseBodySecurityPoliciesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TlsVersion') is not None:
            self.tls_version = m.get('TlsVersion')
        return self


class ListSecurityPolicyResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        security_policies: List[ListSecurityPolicyResponseBodySecurityPolicies] = None,
        total_count: int = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # A list of TLS security policies.
        self.security_policies = security_policies
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.security_policies:
            for k in self.security_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityPolicies'] = []
        if self.security_policies is not None:
            for k in self.security_policies:
                result['SecurityPolicies'].append(k.to_map() if k else None)
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
        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k in m.get('SecurityPolicies'):
                temp_model = ListSecurityPolicyResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSecurityPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSecurityPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSecurityPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServerGroupServersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        server_group_id: str = None,
        server_ids: List[str] = None,
        server_ips: List[str] = None,
    ):
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The ID of the server group.
        self.server_group_id = server_group_id
        self.server_ids = server_ids
        self.server_ips = server_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_ids is not None:
            result['ServerIds'] = self.server_ids
        if self.server_ips is not None:
            result['ServerIps'] = self.server_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerIds') is not None:
            self.server_ids = m.get('ServerIds')
        if m.get('ServerIps') is not None:
            self.server_ips = m.get('ServerIps')
        return self


class ListServerGroupServersResponseBodyServers(TeaModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        server_group_id: str = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        status: str = None,
        weight: int = None,
        zone_id: str = None,
    ):
        # The description of the backend server.
        self.description = description
        # The port used by the backend server. Valid values: **1** to **65535**.
        self.port = port
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The ID of the server.
        self.server_id = server_id
        # The IP address of the backend server.
        self.server_ip = server_ip
        # The type of the backend server. Valid values:
        # 
        # *   **Ecs**: an Elastic Compute Service (ECS) instance
        # *   **Eni**: an elastic network interface (ENI)
        # *   **Eci**: an elastic container instance
        # *   **Ip**: an IP address
        self.server_type = server_type
        # Indicates the status of the backend server. Valid values:
        # 
        # *   **Adding**: The backend server is being added.
        # *   **Available**: The backend server is added.
        # *   **Configuring**: The backend server is being configured.
        # *   **Removing**: The backend server is being removed.
        self.status = status
        # The weight of the backend server.
        self.weight = weight
        # The zone ID of the server.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.status is not None:
            result['Status'] = self.status
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListServerGroupServersResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        servers: List[ListServerGroupServersResponseBodyServers] = None,
        total_count: int = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # A list of backend servers.
        self.servers = servers
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
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
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = ListServerGroupServersResponseBodyServers()
                self.servers.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServerGroupServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServerGroupServersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServerGroupServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServerGroupsRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify up to 10 tag keys.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key
        # The tag value. You can specify up to 10 tag values.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListServerGroupsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        server_group_ids: List[str] = None,
        server_group_names: List[str] = None,
        server_group_type: str = None,
        tag: List[ListServerGroupsRequestTag] = None,
        vpc_id: str = None,
    ):
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If this is your first query and no next queries are to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the value to the value of NextToken that is returned from the last call.
        self.next_token = next_token
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the server group belongs.
        self.resource_group_id = resource_group_id
        self.server_group_ids = server_group_ids
        self.server_group_names = server_group_names
        # The type of server group. Valid values:
        # 
        # *   **Instance** : allows you to add servers of the **Ecs**, **Ens**, and **Eci** types.
        # *   **Ip**: allows you to add servers by specifying IP addresses.
        self.server_group_type = server_group_type
        self.tag = tag
        # The ID of the virtual private cloud (VPC) to which the server group belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.server_group_ids is not None:
            result['ServerGroupIds'] = self.server_group_ids
        if self.server_group_names is not None:
            result['ServerGroupNames'] = self.server_group_names
        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServerGroupIds') is not None:
            self.server_group_ids = m.get('ServerGroupIds')
        if m.get('ServerGroupNames') is not None:
            self.server_group_names = m.get('ServerGroupNames')
        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServerGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListServerGroupsResponseBodyServerGroupsHealthCheck(TeaModel):
    def __init__(
        self,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_enabled: bool = None,
        health_check_http_code: List[str] = None,
        health_check_interval: int = None,
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
        # The maximum timeout period of a health check. Unit: seconds.
        # 
        # Valid values: **1** to **300**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$SERVER_IP**: the private IP address of a backend server.
        # *   **domain**: a specified domain name. The domain name must be 1 to 80 characters in length, and can contain lowercase letters, digits, hyphens (-), and periods (.).
        # 
        # >  This parameter takes effect only if **HealthCheckType** is set to **HTTP**.
        self.health_check_domain = health_check_domain
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.health_check_enabled = health_check_enabled
        # The HTTP status codes returned for health checks. Multiple HTTP status codes are separated by commas (,).
        # 
        # Valid values: **http\_2xx**, **http\_3xx**, **http\_4xx**, and **http\_5xx**.
        # 
        # >  This parameter takes effect only if **HealthCheckType** is set to **HTTP**.
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Unit: seconds.
        # 
        # Valid values: **5** to **50**.
        self.health_check_interval = health_check_interval
        # The protocol that is used for health checks. Valid values: **TCP** and **HTTP**.
        self.health_check_type = health_check_type
        # The path to which health check requests are sent.
        # 
        # >  This parameter takes effect only if **HealthCheckType** is set to **HTTP**.
        self.health_check_url = health_check_url
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The HTTP method that is used for health checks. Valid values: **GET** and **HEAD**.
        # 
        # >  This parameter takes effect only if **HealthCheckType** is set to **HTTP**.
        self.http_check_method = http_check_method
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
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
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
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


class ListServerGroupsResponseBodyServerGroupsTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListServerGroupsResponseBodyServerGroups(TeaModel):
    def __init__(
        self,
        address_ipversion: str = None,
        ali_uid: int = None,
        any_port_enabled: bool = None,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
        health_check: ListServerGroupsResponseBodyServerGroupsHealthCheck = None,
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
        tags: List[ListServerGroupsResponseBodyServerGroupsTags] = None,
        vpc_id: str = None,
    ):
        # The protocol version. Valid values:
        # 
        # *   **ipv4**: IPv4
        # *   **DualStack**: dual stack
        self.address_ipversion = address_ipversion
        # The UID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # Indicates whether the feature of forwarding requests to all ports is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.any_port_enabled = any_port_enabled
        # Indicates whether connection draining is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.connection_drain_enabled = connection_drain_enabled
        # The timeout period of connection draining. Unit: seconds.
        # 
        # Valid values: **10** to **900**.
        self.connection_drain_timeout = connection_drain_timeout
        # The configurations of health checks.
        self.health_check = health_check
        # Indicates whether client IP preservation is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        # 
        # >  Note: If **AddressIPVersion** is set to **ipv4**, the default value is **true**. If **AddressIPVersion** is set to **ipv6**, the only valid value is **false**. **true** will be supported in later version.
        self.preserve_client_ip_enabled = preserve_client_ip_enabled
        # The protocol used to forward requests to the backend servers. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.protocol = protocol
        # The ID of the region where the NLB instance is deployed.
        self.region_id = region_id
        # The NLB instances.
        self.related_load_balancer_ids = related_load_balancer_ids
        # The ID of the resource group to which the server group belongs.
        self.resource_group_id = resource_group_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **Wrr**: Backend servers with higher weights receive more requests than backend servers with lower weights.
        # *   **rr**: Requests are forwarded to the backend servers in sequence. sch: Requests are forwarded to the backend servers based on source IP address hashing.
        # *   **sch**: Requests from the same source IP address are forwarded to the same backend server.
        # *   **tch**: Four-element hashing, which specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are forwarded to the same backend server.
        # *   **qch**: QUIC ID hashing. Requests that contain the same QUIC ID are forwarded to the same backend server.
        self.scheduler = scheduler
        # The number of server groups associated with the NLB instances.
        self.server_count = server_count
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The name of the server group.
        self.server_group_name = server_group_name
        # The status of the server group. Valid values:
        # 
        # *   **Creating**: The server group is being created.
        # *   **Available**: The server group is available.
        # *   **Configuring**: The server group is being configured.
        self.server_group_status = server_group_status
        # The type of server group. Valid values:
        # 
        # *   **Instance** : allows you to add servers of the **Ecs**, **Ens**, and **Eci** types.
        # *   **Ip**: allows you to add servers by specifying IP addresses.
        self.server_group_type = server_group_type
        # The tags that are added to the NLB instance.
        self.tags = tags
        # The ID of the VPC to which the server group belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.health_check:
            self.health_check.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
            temp_model = ListServerGroupsResponseBodyServerGroupsHealthCheck()
            self.health_check = temp_model.from_map(m['HealthCheck'])
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
            for k in m.get('Tags'):
                temp_model = ListServerGroupsResponseBodyServerGroupsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListServerGroupsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        server_groups: List[ListServerGroupsResponseBodyServerGroups] = None,
        total_count: int = None,
    ):
        # The number of entries returned per page. Valid values: **1** to **100**.
        self.max_results = max_results
        # The token that determines the start point of the query. Valid values:
        # 
        # *   If **NextToken** is empty, it indicates that no subsequent query is to be sent.
        # *   If a value of **NextToken** is returned, the value is the token used for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The server groups.
        self.server_groups = server_groups
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.server_groups:
            for k in self.server_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServerGroups'] = []
        if self.server_groups is not None:
            for k in self.server_groups:
                result['ServerGroups'].append(k.to_map() if k else None)
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
            for k in m.get('ServerGroups'):
                temp_model = ListServerGroupsResponseBodyServerGroups()
                self.server_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServerGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServerGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemSecurityPolicyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListSystemSecurityPolicyResponseBodySecurityPolicies(TeaModel):
    def __init__(
        self,
        ciphers: str = None,
        security_policy_id: str = None,
        security_policy_name: str = None,
        tls_version: str = None,
    ):
        self.ciphers = ciphers
        self.security_policy_id = security_policy_id
        self.security_policy_name = security_policy_name
        self.tls_version = tls_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        if self.tls_version is not None:
            result['TlsVersion'] = self.tls_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        if m.get('TlsVersion') is not None:
            self.tls_version = m.get('TlsVersion')
        return self


class ListSystemSecurityPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_policies: List[ListSystemSecurityPolicyResponseBodySecurityPolicies] = None,
    ):
        self.request_id = request_id
        self.security_policies = security_policies

    def validate(self):
        if self.security_policies:
            for k in self.security_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityPolicies'] = []
        if self.security_policies is not None:
            for k in self.security_policies:
                result['SecurityPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k in m.get('SecurityPolicies'):
                temp_model = ListSystemSecurityPolicyResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k))
        return self


class ListSystemSecurityPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSystemSecurityPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSystemSecurityPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.page = page
        self.page_size = page_size
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        category: str = None,
        region_no: str = None,
        resource_id: str = None,
        resource_type: str = None,
        scope: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.ali_uid = ali_uid
        self.category = category
        self.region_no = region_no
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.scope = scope
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.category is not None:
            result['Category'] = self.category
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources
        self.total_count = total_count

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
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
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoadBalancerJoinSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
        security_group_ids: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The value of **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to check the request without performing the operation. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system checks the required parameters, request syntax, and limits. If the request fails the check, an error code is returned based on the cause of the failure. If the request passes the check, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance to be associated with the security group.
        self.load_balancer_id = load_balancer_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class LoadBalancerJoinSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LoadBalancerJoinSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LoadBalancerJoinSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LoadBalancerJoinSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoadBalancerLeaveSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
        security_group_ids: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The value of **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to check the request without performing the operation. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system checks the required parameters, request syntax, and limits. If the request fails the check, an error code is returned based on the cause of the failure. If the request passes the check, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class LoadBalancerLeaveSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LoadBalancerLeaveSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LoadBalancerLeaveSecurityGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LoadBalancerLeaveSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.new_resource_group_id = new_resource_group_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class MoveResourceGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
    ):
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        data: MoveResourceGroupResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = MoveResourceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveServersFromServerGroupRequestServers(TeaModel):
    def __init__(
        self,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
    ):
        # The port used by the backend server. Valid values: **1** to **65535**.
        self.port = port
        # The ID of the server.
        # 
        # *   If the server group type is **Instance**, set the ServerId parameter to the ID of an Elastic Compute Service (ECS) instance, an elastic network interface (ENI), or an elastic container instance. These backend servers are specified by **Ecs**, **Eni**, or **Eci**.
        # *   If the server group type is **Ip**, set the ServerId parameter to an IP address.
        self.server_id = server_id
        # The IP address of the server. If the server group type is **Ip**, set the ServerId parameter to an IP address.
        self.server_ip = server_ip
        # The type of the backend server. Valid values:
        # 
        # *   **Ecs**: an ECS instance
        # *   **Eni**: an ENI
        # *   **Eci**: an elastic container instance
        # *   **Ip**: an IP address
        self.server_type = server_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        return self


class RemoveServersFromServerGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        server_group_id: str = None,
        servers: List[RemoveServersFromServerGroupRequestServers] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not remove the backend servers. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the server group.
        self.server_group_id = server_group_id
        self.servers = servers

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = RemoveServersFromServerGroupRequestServers()
                self.servers.append(temp_model.from_map(k))
        return self


class RemoveServersFromServerGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        server_group_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the server group.
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class RemoveServersFromServerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveServersFromServerGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveServersFromServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartListenerRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not enable the listener. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the listener.
        self.listener_id = listener_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopListenerRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can only contain ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the listener.
        self.listener_id = listener_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopListenerResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopListenerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopListenerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can add up to 20 tags in each call.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can add up to 20 tags in each call.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The value of **RequestId** is different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed. This is the default value.
        self.dry_run = dry_run
        # The region ID of the resource.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource. You can specify up to 50 resource IDs in each call.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   **loadbalancer**: a Network Load Balancer (NLB) instance
        # *   **securitypolicy**: a security policy
        # *   **servergroup**: a server group
        self.resource_type = resource_type
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the specified resource. Valid values:
        # 
        # *   **true**: removes all tags from the specified resource.
        # *   **false**: does not remove all tags from the specified resource. This is the default value.
        self.all = all
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The value of **RequestId** is different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed. This is the default value.
        self.dry_run = dry_run
        # The region ID of the resource.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource. You can specify up to 50 resource IDs in each call.
        self.resource_id = resource_id
        # The type of the resource from which you want to remove tags. Valid values:
        # 
        # *   **loadbalancer**: a Network Load Balancer (NLB) instance
        # *   **securitypolicy**: a security policy
        # *   **servergroup**: a server group
        self.resource_type = resource_type
        # The key of the tag that you want to remove. You can remove up to 20 tags in each call.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateListenerAttributeRequest(TeaModel):
    def __init__(
        self,
        alpn_enabled: bool = None,
        alpn_policy: str = None,
        ca_certificate_ids: List[str] = None,
        ca_enabled: bool = None,
        certificate_ids: List[str] = None,
        client_token: str = None,
        cps: int = None,
        dry_run: bool = None,
        idle_timeout: int = None,
        listener_description: str = None,
        listener_id: str = None,
        mss: int = None,
        proxy_protocol_enabled: bool = None,
        region_id: str = None,
        sec_sensor_enabled: bool = None,
        security_policy_id: str = None,
        server_group_id: str = None,
    ):
        # Specifies whether to enable Application-Layer Protocol Negotiation (ALPN). Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.alpn_enabled = alpn_enabled
        # The ALPN policy.
        self.alpn_policy = alpn_policy
        self.ca_certificate_ids = ca_certificate_ids
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.ca_enabled = ca_enabled
        self.certificate_ids = certificate_ids
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **0** to **1000000**. **0** specifies that the number of connections is unlimited.
        self.cps = cps
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not update the configurations of the listener. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1** to **900**.
        self.idle_timeout = idle_timeout
        # Enter a name for the listener.
        # 
        # The description must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.listener_description = listener_description
        # The ID of the listener.
        self.listener_id = listener_id
        # The size of the largest TCP segment. Unit: bytes. Valid values: **0** to **1500**. **0** specifies that the maximum segment size remains unchanged. This parameter is supported only by listeners that use SSL over TCP.
        self.mss = mss
        # Specifies whether to use the Proxy protocol to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.proxy_protocol_enabled = proxy_protocol_enabled
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # Specifies whether to enable fine-grained monitoring. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sec_sensor_enabled = sec_sensor_enabled
        # The ID of the security policy.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id
        # The ID of the server group.
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled
        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy
        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.mss is not None:
            result['Mss'] = self.mss
        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')
        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')
        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Mss') is not None:
            self.mss = m.get('Mss')
        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateListenerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateListenerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateListenerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerAddressTypeConfigRequestZoneMappings(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        eip_type: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the elastic IP address (EIP).
        self.allocation_id = allocation_id
        # The type of the EIP. Valid values:
        # 
        # *   **Common**: EIP
        # *   **Anycast**: Anycast EIP
        # 
        # >  Only NLB instances in the China (Hong Kong) region can be associated with Anycast EIPs. This parameter is required if you set the **AddressType** parameter to **Internet**.
        self.eip_type = eip_type
        # The ID of the vSwitch in the zone. You can specify only one vSwitch (subnet) in each zone of an NLB instance.
        self.v_switch_id = v_switch_id
        # The ID of the zone of the NLB instance.
        # 
        # You can call the [DescribeZones](~~443890~~) operation to query the most recent zone list.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.eip_type is not None:
            result['EipType'] = self.eip_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('EipType') is not None:
            self.eip_type = m.get('EipType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateLoadBalancerAddressTypeConfigRequest(TeaModel):
    def __init__(
        self,
        address_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
        zone_mappings: List[UpdateLoadBalancerAddressTypeConfigRequestZoneMappings] = None,
    ):
        # The new network type. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. Therefore, the NLB instance can be accessed over the virtual private cloud (VPC) where the NLB instance is deployed.
        self.address_type = address_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among all requests. The token can only contain ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically sets **ClientToken** to the value of **RequestId**. **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to check the request without performing the operation. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system checks the required parameters, request syntax, and limits. If the request fails the check, an error message is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = UpdateLoadBalancerAddressTypeConfigRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class UpdateLoadBalancerAddressTypeConfigResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerAddressTypeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLoadBalancerAddressTypeConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLoadBalancerAddressTypeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        cps: int = None,
        cross_zone_enabled: bool = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **1** to **1000000**.
        self.cps = cps
        # Specifies whether to enable cross-zone load balancing for the NLB instance. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.cross_zone_enabled = cross_zone_enabled
        # Specifies whether only to precheck this request. Valid values:
        # 
        # *   **true**: prechecks the request but does not modify the name or status of the NLB instance. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The name of the NLB instance.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The name must start with a letter.
        self.load_balancer_name = load_balancer_name
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.cross_zone_enabled is not None:
            result['CrossZoneEnabled'] = self.cross_zone_enabled
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateLoadBalancerAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLoadBalancerAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLoadBalancerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerProtectionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        deletion_protection_enabled: bool = None,
        deletion_protection_reason: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        modification_protection_reason: str = None,
        modification_protection_status: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.deletion_protection_enabled = deletion_protection_enabled
        self.deletion_protection_reason = deletion_protection_reason
        self.dry_run = dry_run
        self.load_balancer_id = load_balancer_id
        self.modification_protection_reason = modification_protection_reason
        self.modification_protection_status = modification_protection_status
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deletion_protection_enabled is not None:
            result['DeletionProtectionEnabled'] = self.deletion_protection_enabled
        if self.deletion_protection_reason is not None:
            result['DeletionProtectionReason'] = self.deletion_protection_reason
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason
        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeletionProtectionEnabled') is not None:
            self.deletion_protection_enabled = m.get('DeletionProtectionEnabled')
        if m.get('DeletionProtectionReason') is not None:
            self.deletion_protection_reason = m.get('DeletionProtectionReason')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')
        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateLoadBalancerProtectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLoadBalancerProtectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLoadBalancerProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerZonesRequestZoneMappings(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        eip_type: str = None,
        private_ipv_4address: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the elastic IP address (EIP) or Anycast EIP.
        self.allocation_id = allocation_id
        # The type of the EIP. Valid values:
        # 
        # *   **Common**: EIP
        # *   **Anycast**: Anycast EIP
        # 
        # >  Only NLB instances in the China (Hong Kong) region can be associated with Anycast EIPs. This parameter is required if you set the **AddressType** parameter to **Internet**.
        self.eip_type = eip_type
        # The private IP addresses.
        self.private_ipv_4address = private_ipv_4address
        # The ID of the vSwitch in the zone. By default, each zone contains one vSwitch and one subnet.
        self.v_switch_id = v_switch_id
        # The ID of the zone. You can call the [DescribeZones](~~443890~~) operation to query the zones.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.eip_type is not None:
            result['EipType'] = self.eip_type
        if self.private_ipv_4address is not None:
            result['PrivateIPv4Address'] = self.private_ipv_4address
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('EipType') is not None:
            self.eip_type = m.get('EipType')
        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateLoadBalancerZonesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        region_id: str = None,
        zone_mappings: List[UpdateLoadBalancerZonesRequestZoneMappings] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among all requests. The token can only contain ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically sets **ClientToken** to the value of **RequestId**. **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to check the request without performing the operation. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system checks the required parameters, request syntax, and limits. If the request fails the check, an error message is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # *   **false**: sends the request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed. This is the default value.
        self.dry_run = dry_run
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = UpdateLoadBalancerZonesRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class UpdateLoadBalancerZonesResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLoadBalancerZonesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLoadBalancerZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecurityPolicyAttributeRequest(TeaModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        security_policy_id: str = None,
        security_policy_name: str = None,
        tls_versions: List[str] = None,
    ):
        self.ciphers = ciphers
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not modify the configurations of the security policy. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id
        # The name of the security policy.
        # 
        # The name must be 1 to 200 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        self.security_policy_name = security_policy_name
        self.tls_versions = tls_versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        if self.tls_versions is not None:
            result['TlsVersions'] = self.tls_versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        if m.get('TlsVersions') is not None:
            self.tls_versions = m.get('TlsVersions')
        return self


class UpdateSecurityPolicyAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        security_policy_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        return self


class UpdateSecurityPolicyAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSecurityPolicyAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSecurityPolicyAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServerGroupAttributeRequestHealthCheckConfig(TeaModel):
    def __init__(
        self,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_enabled: bool = None,
        health_check_http_code: List[str] = None,
        health_check_interval: int = None,
        health_check_type: str = None,
        health_check_url: str = None,
        healthy_threshold: int = None,
        http_check_method: str = None,
        unhealthy_threshold: int = None,
    ):
        # The backend port that is used for health checks. Valid values: **0** to **65535**. If you set the value to **0**, the ports of backend servers are used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The maximum timeout period of a health check response. Unit: seconds. Valid values: **1** to **300**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$SERVER_IP**: the private IP address of a backend server.
        # *   **domain**: a specific domain name. The domain name must be 1 to 80 characters in length and can contain lowercase letters, digits, hyphens (-), and periods (.).
        # 
        # >  This parameter takes effect only when you set **HealthCheckType** to **HTTP**.
        self.health_check_domain = health_check_domain
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **true**: enables the health check feature.
        # *   **false**: disables the health check feature.
        self.health_check_enabled = health_check_enabled
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Unit: seconds.
        # 
        # Valid values: **5** to **50**.
        self.health_check_interval = health_check_interval
        # The protocol that is used for health checks. Valid values: **TCP** and **HTTP**.
        self.health_check_type = health_check_type
        # The path to which health check requests are sent.
        # 
        # The path must be 1 to 80 characters in length, and can contain only letters, digits, and the following special characters: `- / . % ? # & =`. The path can also contain the following extended characters: `_ ; ~ ! ( ) * [ ] @ $ ^ : \" , +`. The path must start with a forward slash (/).
        # 
        # >  This parameter takes effect only when you set **HealthCheckType** to **HTTP**.
        self.health_check_url = health_check_url
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from **fail** to **success**. Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The HTTP method that is used for health checks. Valid values: **GET** and **HEAD**.
        # 
        # >  This parameter takes effect only when you set **HealthCheckType** to **HTTP**.
        self.http_check_method = http_check_method
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from **success** to **fail**. Valid values: **2** to **10**.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
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
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
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


class UpdateServerGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
        dry_run: bool = None,
        health_check_config: UpdateServerGroupAttributeRequestHealthCheckConfig = None,
        preserve_client_ip_enabled: bool = None,
        region_id: str = None,
        scheduler: str = None,
        server_group_id: str = None,
        server_group_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically sets **ClientToken** to the value of **RequestId**. **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to enable connection draining. Valid values:
        # 
        # *   **true**: enables connection draining.
        # *   **false**: disables connection draining.
        self.connection_drain_enabled = connection_drain_enabled
        # The timeout period of connection draining. Unit: seconds. Valid values: **10** to **900**.
        self.connection_drain_timeout = connection_drain_timeout
        # Specifies whether to only precheck the request. Valid values:
        # 
        # *   **true**: checks the request without performing the UpdateServerGroupAttribute operation. The system checks the required parameters, request syntax, and limits. If the request fails the check, an error message is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the check, a 2xx HTTP status code is returned and the UpdateServerGroupAttribute operation is performed.
        self.dry_run = dry_run
        self.health_check_config = health_check_config
        # Specifies whether to enable client IP preservation. Valid values:
        # 
        # *   **true**: enables client IP preservation.
        # *   **false**: disables client IP preservation.
        self.preserve_client_ip_enabled = preserve_client_ip_enabled
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the available regions.
        self.region_id = region_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **Wrr**: Backend servers with higher weights receive more requests than backend servers with lower weights.
        # *   **rr**: Requests are forwarded to backend servers in sequence.
        # *   **sch**: Requests from the same source IP address are forwarded to the same backend server.
        # *   **tch**: Four-element hashing is used. This value specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are forwarded to the same backend server.
        # *   **qch**: Requests that contain the same QUIC ID are forwarded to the same backend server.
        self.scheduler = scheduler
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The new name of the server group.
        # 
        # The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The name must start with a letter.
        self.server_group_name = server_group_name

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_drain_enabled is not None:
            result['ConnectionDrainEnabled'] = self.connection_drain_enabled
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()
        if self.preserve_client_ip_enabled is not None:
            result['PreserveClientIpEnabled'] = self.preserve_client_ip_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionDrainEnabled') is not None:
            self.connection_drain_enabled = m.get('ConnectionDrainEnabled')
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('HealthCheckConfig') is not None:
            temp_model = UpdateServerGroupAttributeRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['HealthCheckConfig'])
        if m.get('PreserveClientIpEnabled') is not None:
            self.preserve_client_ip_enabled = m.get('PreserveClientIpEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')
        return self


class UpdateServerGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        server_group_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the server group.
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateServerGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServerGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServerGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServerGroupServersAttributeRequestServers(TeaModel):
    def __init__(
        self,
        description: str = None,
        port: int = None,
        server_id: str = None,
        server_ip: str = None,
        server_type: str = None,
        weight: int = None,
    ):
        # The description of the backend server.
        # 
        # The description must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.description = description
        # The port used by the backend server. Valid values: **1** to **65535**. You can specify at most 40 backend servers in each call.
        # 
        # >  The value of this parameter cannot be modified.
        self.port = port
        # The ID of the backend server. You can specify at most 40 backend servers in each call.
        # 
        # *   If the server group type is **Instance**, set the ServerId parameter to the ID of an Elastic Compute Service (ECS) instance, an elastic network interface (ENI), or an elastic container instance. These backend servers are specified by **Ecs**, **Eni**, or **Eci**.
        # *   If the server group type is **Ip**, set the ServerId parameter to an IP address.
        self.server_id = server_id
        # The IP address of the server. If the server group type is **Ip**, you must specify an IP address.
        # 
        # >  You can specify at most 40 backend servers in each call.
        self.server_ip = server_ip
        # The type of the backend server. Valid values:
        # 
        # *   **Ecs**: an ECS instance
        # *   **Eni**: an ENI
        # *   **Eci**: an elastic container instance
        # *   **Ip**: an IP address
        # 
        # >  You can specify at most 40 backend servers in each call.
        self.server_type = server_type
        # The weight of the backend server. Valid values: **0** to **100**. Default value: **100**. If the weight of a backend server is set to **0**, no requests are forwarded to the backend server.
        # 
        # >  You can specify at most 40 backend servers in each call.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateServerGroupServersAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        server_group_id: str = None,
        servers: List[UpdateServerGroupServersAttributeRequestServers] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that the value is unique among different requests. The token can only contain ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically sets **ClientToken** to the value of **RequestId**. **RequestId** of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the Network Load Balancer (NLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the server group.
        self.server_group_id = server_group_id
        self.servers = servers

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = UpdateServerGroupServersAttributeRequestServers()
                self.servers.append(temp_model.from_map(k))
        return self


class UpdateServerGroupServersAttributeResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
        server_group_id: str = None,
    ):
        # The ID of the asynchronous task.
        self.job_id = job_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the server group.
        self.server_group_id = server_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateServerGroupServersAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServerGroupServersAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServerGroupServersAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


