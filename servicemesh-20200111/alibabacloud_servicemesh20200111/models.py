# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class SecretCreateRecordValue(TeaModel):
    def __init__(
        self,
        state: str = None,
        cluster_id: str = None,
        message: str = None,
    ):
        self.state = state
        self.cluster_id = cluster_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SecretDeleteRecordValue(TeaModel):
    def __init__(
        self,
        state: str = None,
        cluster_id: str = None,
        message: str = None,
    ):
        self.state = state
        self.cluster_id = cluster_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CCMVersionsValue(TeaModel):
    def __init__(
        self,
        query_state: str = None,
        version: str = None,
        slbgraceful_drain_support: bool = None,
        cluster_id: str = None,
        message: str = None,
    ):
        self.query_state = query_state
        self.version = version
        self.slbgraceful_drain_support = slbgraceful_drain_support
        self.cluster_id = cluster_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_state is not None:
            result['QueryState'] = self.query_state
        if self.version is not None:
            result['Version'] = self.version
        if self.slbgraceful_drain_support is not None:
            result['SLBGracefulDrainSupport'] = self.slbgraceful_drain_support
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryState') is not None:
            self.query_state = m.get('QueryState')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('SLBGracefulDrainSupport') is not None:
            self.slbgraceful_drain_support = m.get('SLBGracefulDrainSupport')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpgradeDetailGatewayStatusRecordValue(TeaModel):
    def __init__(
        self,
        status: str = None,
        message: str = None,
        version: str = None,
    ):
        self.status = status
        self.message = message
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.message is not None:
            result['Message'] = self.message
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class AddClusterIntoServiceMeshRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_namespace_check: bool = None,
        service_mesh_id: str = None,
    ):
        self.cluster_id = cluster_id
        # 添加集群时不检查目标集群是否存在istio-system namespace，一般用于自建istio 迁移ASM 场景
        self.ignore_namespace_check = ignore_namespace_check
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_namespace_check is not None:
            result['IgnoreNamespaceCheck'] = self.ignore_namespace_check
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreNamespaceCheck') is not None:
            self.ignore_namespace_check = m.get('IgnoreNamespaceCheck')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class AddClusterIntoServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddClusterIntoServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddClusterIntoServiceMeshResponseBody = None,
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
            temp_model = AddClusterIntoServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVMIntoServiceMeshRequest(TeaModel):
    def __init__(
        self,
        ecs_id: str = None,
        service_mesh_id: str = None,
    ):
        # The ID of the VM.
        self.ecs_id = ecs_id
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class AddVMIntoServiceMeshResponseBody(TeaModel):
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


class AddVMIntoServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddVMIntoServiceMeshResponseBody = None,
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
            temp_model = AddVMIntoServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateASMGatewayRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        istio_gateway_name: str = None,
        service_mesh_id: str = None,
    ):
        # The YAML content that is used to create the ASM gateway.
        self.body = body
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class CreateASMGatewayResponseBody(TeaModel):
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


class CreateASMGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateASMGatewayResponseBody = None,
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
            temp_model = CreateASMGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewaySecretRequest(TeaModel):
    def __init__(
        self,
        cert: str = None,
        istio_gateway_name: str = None,
        key: str = None,
        secret_name: str = None,
        service_mesh_id: str = None,
    ):
        # The content of the certificate.
        self.cert = cert
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The private key of the certificate.
        self.key = key
        # The name of the secret.
        self.secret_name = secret_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.key is not None:
            result['Key'] = self.key
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class CreateGatewaySecretResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_create_record: Dict[str, SecretCreateRecordValue] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The record of creating the secret.
        self.secret_create_record = secret_create_record

    def validate(self):
        if self.secret_create_record:
            for v in self.secret_create_record.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecretCreateRecord'] = {}
        if self.secret_create_record is not None:
            for k, v in self.secret_create_record.items():
                result['SecretCreateRecord'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.secret_create_record = {}
        if m.get('SecretCreateRecord') is not None:
            for k, v in m.get('SecretCreateRecord').items():
                temp_model = SecretCreateRecordValue()
                self.secret_create_record[k] = temp_model.from_map(v)
        return self


class CreateGatewaySecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewaySecretResponseBody = None,
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
            temp_model = CreateGatewaySecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIstioGatewayDomainsRequest(TeaModel):
    def __init__(
        self,
        credential: str = None,
        force_https: bool = None,
        hosts: str = None,
        istio_gateway_name: str = None,
        limit: str = None,
        namespace: str = None,
        number: int = None,
        port_name: str = None,
        protocol: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the secret that contains the Transport Layer Security (TLS) certificate and certificate authority (CA) certificate.
        self.credential = credential
        # Specifies whether to forcibly use TLS to protect connection security.
        # 
        # *   `true`: forcibly uses TLS to protect connection security.
        # *   `false`: does not forcibly use TLS to protect connection security.
        self.force_https = force_https
        # The domain names of the one or more hosts that are exposed by the ASM gateway. Separate multiple domain names with commas (,).
        self.hosts = hosts
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The maximum number of ASM gateways to query.
        self.limit = limit
        # The name of the namespace.
        self.namespace = namespace
        # The port that is provided by the ASM gateway.
        self.number = number
        # The name of the port.
        self.port_name = port_name
        # The type of the protocol. Valid values: `HTTP`, `HTTPS`, `GRPC`, `HTTP2`, `MONGO`, `TCP`, and `TLS`.
        self.protocol = protocol
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential is not None:
            result['Credential'] = self.credential
        if self.force_https is not None:
            result['ForceHttps'] = self.force_https
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.number is not None:
            result['Number'] = self.number
        if self.port_name is not None:
            result['PortName'] = self.port_name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Credential') is not None:
            self.credential = m.get('Credential')
        if m.get('ForceHttps') is not None:
            self.force_https = m.get('ForceHttps')
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class CreateIstioGatewayDomainsResponseBody(TeaModel):
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


class CreateIstioGatewayDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIstioGatewayDomainsResponseBody = None,
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
            temp_model = CreateIstioGatewayDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsDelegate(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
    ):
        # The name of the virtual service.
        self.name = name
        # The namespace to which the virtual service belongs.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbortPercentage(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The percentage of requests that are aborted with the specified error code, which is expressed as a decimal.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbort(TeaModel):
    def __init__(
        self,
        http_status: int = None,
        percentage: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbortPercentage = None,
    ):
        # The HTTP status code.
        self.http_status = http_status
        # The percentage of requests that are aborted with the specified error code.
        self.percentage = percentage

    def validate(self):
        if self.percentage:
            self.percentage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status is not None:
            result['HttpStatus'] = self.http_status
        if self.percentage is not None:
            result['Percentage'] = self.percentage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')
        if m.get('Percentage') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbortPercentage()
            self.percentage = temp_model.from_map(m['Percentage'])
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelayPercentage(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The percentage of requests to which the delay fault is injected, which is expressed as a decimal.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelay(TeaModel):
    def __init__(
        self,
        fixed_delay: str = None,
        percentage: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelayPercentage = None,
    ):
        # The fixed duration for request delay.
        self.fixed_delay = fixed_delay
        # The percentage of requests to which the delay fault is injected.
        self.percentage = percentage

    def validate(self):
        if self.percentage:
            self.percentage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fixed_delay is not None:
            result['FixedDelay'] = self.fixed_delay
        if self.percentage is not None:
            result['Percentage'] = self.percentage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedDelay') is not None:
            self.fixed_delay = m.get('FixedDelay')
        if m.get('Percentage') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelayPercentage()
            self.percentage = temp_model.from_map(m['Percentage'])
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFault(TeaModel):
    def __init__(
        self,
        abort: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbort = None,
        delay: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelay = None,
    ):
        # The configurations for aborting requests with specified error codes.
        self.abort = abort
        # The duration to delay a request.
        self.delay = delay

    def validate(self):
        if self.abort:
            self.abort.validate()
        if self.delay:
            self.delay.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abort is not None:
            result['Abort'] = self.abort.to_map()
        if self.delay is not None:
            result['Delay'] = self.delay.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abort') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbort()
            self.abort = temp_model.from_map(m['Abort'])
        if m.get('Delay') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelay()
            self.delay = temp_model.from_map(m['Delay'])
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsHTTPRedirect(TeaModel):
    def __init__(
        self,
        authority: str = None,
        redirect_code: int = None,
        uri: str = None,
    ):
        # The value to be used to overwrite the value of the Authority or Host header during redirection.``
        self.authority = authority
        # The HTTP status code to be used to indicate URL redirection. Default value: 301.
        self.redirect_code = redirect_code
        # The value to be used to overwrite the URL path during redirection.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.redirect_code is not None:
            result['RedirectCode'] = self.redirect_code
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('RedirectCode') is not None:
            self.redirect_code = m.get('RedirectCode')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirror(TeaModel):
    def __init__(
        self,
        host: str = None,
        subset: str = None,
    ):
        # The name of the service defined in the service registry.
        self.host = host
        # The name of the service subset.
        self.subset = subset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.subset is not None:
            result['Subset'] = self.subset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Subset') is not None:
            self.subset = m.get('Subset')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirrorPercentage(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The percentage of requests that are mirrored to another destination except for the original destination, which is expressed as a decimal.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetriesRetryRemoteLocalities(TeaModel):
    def __init__(
        self,
        value: bool = None,
    ):
        # Specifies whether to allow retries to other localities. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetries(TeaModel):
    def __init__(
        self,
        attempts: int = None,
        per_try_timeout: str = None,
        retry_on: str = None,
        retry_remote_localities: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetriesRetryRemoteLocalities = None,
    ):
        # The number of retries allowed for a request.
        self.attempts = attempts
        # The timeout period for each retry. Example: `5s`.
        self.per_try_timeout = per_try_timeout
        # The condition for retries. Example: `connect-failure,refused-stream,503`.
        self.retry_on = retry_on
        # Specifies whether to allow retries to other localities.
        self.retry_remote_localities = retry_remote_localities

    def validate(self):
        if self.retry_remote_localities:
            self.retry_remote_localities.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempts is not None:
            result['Attempts'] = self.attempts
        if self.per_try_timeout is not None:
            result['PerTryTimeout'] = self.per_try_timeout
        if self.retry_on is not None:
            result['RetryOn'] = self.retry_on
        if self.retry_remote_localities is not None:
            result['RetryRemoteLocalities'] = self.retry_remote_localities.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attempts') is not None:
            self.attempts = m.get('Attempts')
        if m.get('PerTryTimeout') is not None:
            self.per_try_timeout = m.get('PerTryTimeout')
        if m.get('RetryOn') is not None:
            self.retry_on = m.get('RetryOn')
        if m.get('RetryRemoteLocalities') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetriesRetryRemoteLocalities()
            self.retry_remote_localities = temp_model.from_map(m['RetryRemoteLocalities'])
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRewrite(TeaModel):
    def __init__(
        self,
        authority: str = None,
        uri: str = None,
    ):
        # The value to be used to overwrite the value of the Authority or Host header.
        self.authority = authority
        # The value to be used to overwrite the path or prefix of the URI.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptions(TeaModel):
    def __init__(
        self,
        delegate: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsDelegate = None,
        fault: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFault = None,
        httpredirect: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsHTTPRedirect = None,
        mirror: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirror = None,
        mirror_percentage: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirrorPercentage = None,
        retries: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetries = None,
        rewrite: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRewrite = None,
        timeout: str = None,
    ):
        # The virtual service that defines traffic routing.
        self.delegate = delegate
        # The configurations of fault injection.
        self.fault = fault
        # The HTTP redirect rule.
        self.httpredirect = httpredirect
        # The configurations for mirroring HTTP traffic to another destination in addition to forwarding requests to the specified destination.
        self.mirror = mirror
        # The percentage of requests that are mirrored to another destination except for the original destination.
        self.mirror_percentage = mirror_percentage
        # The configurations of retries for failed requests.
        self.retries = retries
        # The configurations for rewriting the virtual service.
        self.rewrite = rewrite
        # The timeout period for requests.
        self.timeout = timeout

    def validate(self):
        if self.delegate:
            self.delegate.validate()
        if self.fault:
            self.fault.validate()
        if self.httpredirect:
            self.httpredirect.validate()
        if self.mirror:
            self.mirror.validate()
        if self.mirror_percentage:
            self.mirror_percentage.validate()
        if self.retries:
            self.retries.validate()
        if self.rewrite:
            self.rewrite.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delegate is not None:
            result['Delegate'] = self.delegate.to_map()
        if self.fault is not None:
            result['Fault'] = self.fault.to_map()
        if self.httpredirect is not None:
            result['HTTPRedirect'] = self.httpredirect.to_map()
        if self.mirror is not None:
            result['Mirror'] = self.mirror.to_map()
        if self.mirror_percentage is not None:
            result['MirrorPercentage'] = self.mirror_percentage.to_map()
        if self.retries is not None:
            result['Retries'] = self.retries.to_map()
        if self.rewrite is not None:
            result['Rewrite'] = self.rewrite.to_map()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delegate') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsDelegate()
            self.delegate = temp_model.from_map(m['Delegate'])
        if m.get('Fault') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFault()
            self.fault = temp_model.from_map(m['Fault'])
        if m.get('HTTPRedirect') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsHTTPRedirect()
            self.httpredirect = temp_model.from_map(m['HTTPRedirect'])
        if m.get('Mirror') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirror()
            self.mirror = temp_model.from_map(m['Mirror'])
        if m.get('MirrorPercentage') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirrorPercentage()
            self.mirror_percentage = temp_model.from_map(m['MirrorPercentage'])
        if m.get('Retries') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetries()
            self.retries = temp_model.from_map(m['Retries'])
        if m.get('Rewrite') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRewrite()
            self.rewrite = temp_model.from_map(m['Rewrite'])
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteMatchRequestHeaders(TeaModel):
    def __init__(
        self,
        matching_content: str = None,
        matching_mode: str = None,
        name: str = None,
    ):
        # The header value to be matched.
        self.matching_content = matching_content
        # The matching mode for the header value. Valid values:
        # 
        # *   `exact`: exact match
        # *   `prefix`: match by prefix
        # *   `regex`: match by regular expression
        self.matching_mode = matching_mode
        # The header key to be matched.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.matching_content is not None:
            result['MatchingContent'] = self.matching_content
        if self.matching_mode is not None:
            result['MatchingMode'] = self.matching_mode
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchingContent') is not None:
            self.matching_content = m.get('MatchingContent')
        if m.get('MatchingMode') is not None:
            self.matching_mode = m.get('MatchingMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteMatchRequestTLSMatchAttributes(TeaModel):
    def __init__(
        self,
        snihosts: List[str] = None,
        tlsport: int = None,
    ):
        # The Server Name Indication (SNI) values to be matched.
        self.snihosts = snihosts
        # The TLS port.
        self.tlsport = tlsport

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snihosts is not None:
            result['SNIHosts'] = self.snihosts
        if self.tlsport is not None:
            result['TLSPort'] = self.tlsport
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SNIHosts') is not None:
            self.snihosts = m.get('SNIHosts')
        if m.get('TLSPort') is not None:
            self.tlsport = m.get('TLSPort')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteMatchRequestURI(TeaModel):
    def __init__(
        self,
        matching_content: str = None,
        matching_mode: str = None,
    ):
        # The content to be matched.
        self.matching_content = matching_content
        # The matching mode for the routing rule. Valid values:
        # 
        # *   `exact`: exact match
        # *   `prefix`: match by prefix
        # *   `regex`: match by regular expression
        self.matching_mode = matching_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.matching_content is not None:
            result['MatchingContent'] = self.matching_content
        if self.matching_mode is not None:
            result['MatchingMode'] = self.matching_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchingContent') is not None:
            self.matching_content = m.get('MatchingContent')
        if m.get('MatchingMode') is not None:
            self.matching_mode = m.get('MatchingMode')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteMatchRequest(TeaModel):
    def __init__(
        self,
        headers: List[CreateIstioGatewayRoutesRequestGatewayRouteMatchRequestHeaders] = None,
        ports: List[int] = None,
        tlsmatch_attributes: List[CreateIstioGatewayRoutesRequestGatewayRouteMatchRequestTLSMatchAttributes] = None,
        uri: CreateIstioGatewayRoutesRequestGatewayRouteMatchRequestURI = None,
    ):
        # The request headers to be matched.
        self.headers = headers
        # The ports of destination services for Layer 4 weighted routing.
        self.ports = ports
        # The matching rule for Transport Layer Security (TLS) traffic.
        self.tlsmatch_attributes = tlsmatch_attributes
        # The matching rule for URIs.
        self.uri = uri

    def validate(self):
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()
        if self.tlsmatch_attributes:
            for k in self.tlsmatch_attributes:
                if k:
                    k.validate()
        if self.uri:
            self.uri.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Headers'] = []
        if self.headers is not None:
            for k in self.headers:
                result['Headers'].append(k.to_map() if k else None)
        if self.ports is not None:
            result['Ports'] = self.ports
        result['TLSMatchAttributes'] = []
        if self.tlsmatch_attributes is not None:
            for k in self.tlsmatch_attributes:
                result['TLSMatchAttributes'].append(k.to_map() if k else None)
        if self.uri is not None:
            result['URI'] = self.uri.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('Headers') is not None:
            for k in m.get('Headers'):
                temp_model = CreateIstioGatewayRoutesRequestGatewayRouteMatchRequestHeaders()
                self.headers.append(temp_model.from_map(k))
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        self.tlsmatch_attributes = []
        if m.get('TLSMatchAttributes') is not None:
            for k in m.get('TLSMatchAttributes'):
                temp_model = CreateIstioGatewayRoutesRequestGatewayRouteMatchRequestTLSMatchAttributes()
                self.tlsmatch_attributes.append(temp_model.from_map(k))
        if m.get('URI') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteMatchRequestURI()
            self.uri = temp_model.from_map(m['URI'])
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestinationPort(TeaModel):
    def __init__(
        self,
        number: int = None,
    ):
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestination(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestinationPort = None,
        subset: str = None,
    ):
        # The name of the service defined in the service registry.
        self.host = host
        self.port = port
        # The name of the service subset.
        self.subset = subset

    def validate(self):
        if self.port:
            self.port.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port.to_map()
        if self.subset is not None:
            result['Subset'] = self.subset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestinationPort()
            self.port = temp_model.from_map(m['Port'])
        if m.get('Subset') is not None:
            self.subset = m.get('Subset')
        return self


class CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinations(TeaModel):
    def __init__(
        self,
        destination: CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestination = None,
        weight: int = None,
    ):
        # The unique endpoint of the destination service to which the specified requests are sent.
        self.destination = destination
        # The weight of the service subset.
        self.weight = weight

    def validate(self):
        if self.destination:
            self.destination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination.to_map()
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestination()
            self.destination = temp_model.from_map(m['Destination'])
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreateIstioGatewayRoutesRequestGatewayRoute(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        httpadvanced_options: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptions = None,
        match_request: CreateIstioGatewayRoutesRequestGatewayRouteMatchRequest = None,
        namespace: str = None,
        raw_vsroute: Any = None,
        route_destinations: List[CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinations] = None,
        route_name: str = None,
        route_type: str = None,
    ):
        self.domains = domains
        # The advanced settings for routing HTTP traffic.
        self.httpadvanced_options = httpadvanced_options
        # The matching rules for traffic routing.
        self.match_request = match_request
        # The name of the namespace.
        self.namespace = namespace
        self.raw_vsroute = raw_vsroute
        # The endpoints of destination services for Layer 4 weighted routing.
        self.route_destinations = route_destinations
        # The name of the routing rule.
        self.route_name = route_name
        # The type of the traffic to be routed. Valid values: `HTTP`, `TLS`, and `TCP`.
        self.route_type = route_type

    def validate(self):
        if self.httpadvanced_options:
            self.httpadvanced_options.validate()
        if self.match_request:
            self.match_request.validate()
        if self.route_destinations:
            for k in self.route_destinations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.httpadvanced_options is not None:
            result['HTTPAdvancedOptions'] = self.httpadvanced_options.to_map()
        if self.match_request is not None:
            result['MatchRequest'] = self.match_request.to_map()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.raw_vsroute is not None:
            result['RawVSRoute'] = self.raw_vsroute
        result['RouteDestinations'] = []
        if self.route_destinations is not None:
            for k in self.route_destinations:
                result['RouteDestinations'].append(k.to_map() if k else None)
        if self.route_name is not None:
            result['RouteName'] = self.route_name
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('HTTPAdvancedOptions') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptions()
            self.httpadvanced_options = temp_model.from_map(m['HTTPAdvancedOptions'])
        if m.get('MatchRequest') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteMatchRequest()
            self.match_request = temp_model.from_map(m['MatchRequest'])
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RawVSRoute') is not None:
            self.raw_vsroute = m.get('RawVSRoute')
        self.route_destinations = []
        if m.get('RouteDestinations') is not None:
            for k in m.get('RouteDestinations'):
                temp_model = CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinations()
                self.route_destinations.append(temp_model.from_map(k))
        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        return self


class CreateIstioGatewayRoutesRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        gateway_route: CreateIstioGatewayRoutesRequestGatewayRoute = None,
        istio_gateway_name: str = None,
        priority: int = None,
        service_mesh_id: str = None,
        status: int = None,
    ):
        # The description of the routing rule.
        self.description = description
        # The information about the routing rule to be created for the ASM gateway.
        self.gateway_route = gateway_route
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The priority of the routing rule. The value of this parameter is an integer. A smaller value indicates a higher priority.
        self.priority = priority
        # The ASM instance ID.
        self.service_mesh_id = service_mesh_id
        # The status of the routing rule. Valid values:
        # 
        # *   `0`: The routing rule is valid.
        # *   `1`: The routing rule is invalid.
        # *   `2`: An error occurs during the creation or update of the routing rule.
        self.status = status

    def validate(self):
        if self.gateway_route:
            self.gateway_route.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gateway_route is not None:
            result['GatewayRoute'] = self.gateway_route.to_map()
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GatewayRoute') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRoute()
            self.gateway_route = temp_model.from_map(m['GatewayRoute'])
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateIstioGatewayRoutesShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        gateway_route_shrink: str = None,
        istio_gateway_name: str = None,
        priority: int = None,
        service_mesh_id: str = None,
        status: int = None,
    ):
        # The description of the routing rule.
        self.description = description
        # The information about the routing rule to be created for the ASM gateway.
        self.gateway_route_shrink = gateway_route_shrink
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The priority of the routing rule. The value of this parameter is an integer. A smaller value indicates a higher priority.
        self.priority = priority
        # The ASM instance ID.
        self.service_mesh_id = service_mesh_id
        # The status of the routing rule. Valid values:
        # 
        # *   `0`: The routing rule is valid.
        # *   `1`: The routing rule is invalid.
        # *   `2`: An error occurs during the creation or update of the routing rule.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gateway_route_shrink is not None:
            result['GatewayRoute'] = self.gateway_route_shrink
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GatewayRoute') is not None:
            self.gateway_route_shrink = m.get('GatewayRoute')
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateIstioGatewayRoutesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class CreateIstioGatewayRoutesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIstioGatewayRoutesResponseBody = None,
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
            temp_model = CreateIstioGatewayRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceMeshRequest(TeaModel):
    def __init__(
        self,
        access_log_enabled: bool = None,
        access_log_file: str = None,
        access_log_format: str = None,
        access_log_project: str = None,
        access_log_service_enabled: bool = None,
        access_log_service_host: str = None,
        access_log_service_port: int = None,
        api_server_load_balancer_spec: str = None,
        api_server_public_eip: bool = None,
        audit_project: str = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        craggregation_enabled: bool = None,
        charge_type: str = None,
        cluster_spec: str = None,
        config_source_enabled: bool = None,
        config_source_nacos_id: str = None,
        control_plane_log_enabled: bool = None,
        control_plane_log_project: str = None,
        customized_prometheus: bool = None,
        customized_zipkin: bool = None,
        dnsproxying_enabled: bool = None,
        dubbo_filter_enabled: bool = None,
        edition: str = None,
        enable_audit: bool = None,
        enable_crhistory: bool = None,
        enable_sdsserver: bool = None,
        exclude_ipranges: str = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ports: str = None,
        existing_ca_cert: str = None,
        existing_ca_key: str = None,
        existing_ca_type: str = None,
        existing_root_ca_cert: str = None,
        existing_root_ca_key: str = None,
        filter_gateway_cluster_config: bool = None,
        gateway_apienabled: bool = None,
        include_ipranges: str = None,
        istio_version: str = None,
        kiali_enabled: bool = None,
        locality_lbconf: str = None,
        locality_load_balancing: bool = None,
        mseenabled: bool = None,
        multi_buffer_enabled: bool = None,
        multi_buffer_poll_delay: str = None,
        mysql_filter_enabled: bool = None,
        name: str = None,
        opalimit_cpu: str = None,
        opalimit_memory: str = None,
        opalog_level: str = None,
        oparequest_cpu: str = None,
        oparequest_memory: str = None,
        opa_enabled: bool = None,
        open_agent_policy: bool = None,
        period: int = None,
        pilot_load_balancer_spec: str = None,
        prometheus_url: str = None,
        proxy_limit_cpu: str = None,
        proxy_limit_memory: str = None,
        proxy_request_cpu: str = None,
        proxy_request_memory: str = None,
        redis_filter_enabled: bool = None,
        region_id: str = None,
        telemetry: bool = None,
        thrift_filter_enabled: bool = None,
        trace_sampling: float = None,
        tracing: bool = None,
        use_existing_ca: bool = None,
        v_switches: str = None,
        vpc_id: str = None,
        web_assembly_filter_enabled: bool = None,
    ):
        # Specifies whether to enable access log collection. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.access_log_enabled = access_log_enabled
        # Specifies whether to enable access log collection. Valid values:
        # 
        # *   "": disables access log collection.
        # *   `/dev/stdout`: enables access log collection. Access logs are written to /dev/stdout.
        self.access_log_file = access_log_file
        # Custom fields of access logs. To set this parameter, you must enable access log collection. Otherwise, you cannot set this parameter. The value must be a JSON string. The following key values must be contained: authority_for, bytes_received, bytes_sent, downstream_local_address, downstream_remote_address, duration, istio_policy_status, method, path, protocol, requested_server_name, response_code, response_flags, route_name, start_time, trace_id, upstream_cluster, upstream_host, upstream_local_address, upstream_service_time, upstream_transport_failure_reason, user_agent, and x_forwarded_for.
        self.access_log_format = access_log_format
        # The SLS project from which access logs are collected.
        self.access_log_project = access_log_project
        # Specifies whether to enable gRPC Access Log Service (ALS) of Envoy. gRPC is short for Google Remote Procedure Call. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.access_log_service_enabled = access_log_service_enabled
        # The endpoint of Envoy\"s gRPC ALS.
        self.access_log_service_host = access_log_service_host
        # The port of Envoy\"s gRPC ALS.
        self.access_log_service_port = access_log_service_port
        # The type of the SLB instance that is bound to Istio Pilot. Valid values: `slb.s1.small`, `slb.s2.small`, `slb.s2.medium`, `slb.s3.small`, `slb.s3.medium`, and `slb.s3.large`.
        self.api_server_load_balancer_spec = api_server_load_balancer_spec
        # Specifies whether to expose the API server to the Internet. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        # 
        # > If you set this parameter to `false`, the API server cannot be accessed over the Internet.
        self.api_server_public_eip = api_server_public_eip
        # The name of the Log Service project that is used for mesh audit.
        # 
        # Default value: mesh-log-{ASM instance ID}.
        self.audit_project = audit_project
        # Specifies whether to enable auto-renewal for the SLB instance if the SLB instance uses the subscription billing method. Valid values:
        # 
        # - true
        # 
        # - false
        self.auto_renew = auto_renew
        # The auto-renewal period of the SLB instance. This parameter is valid only if the `ChargeType` parameter is set to `PrePay`. If the original subscription period of the SLB instance is less than one year, the value of this parameter indicates the number of months for auto-renewal. If the original subscription period of the SLB instance is more than one year, the value of this parameter indicates the number of years for auto-renewal.
        self.auto_renew_period = auto_renew_period
        # Specifies whether to allow the Kubernetes API of clusters on the data plane to access Istio resources. The version of the ASM instance must be V1.9.7.93 or later. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.craggregation_enabled = craggregation_enabled
        # The billing method of the SLB instance. Valid values:
        # *   `PayOnDemand`: pay-as-you-go.
        # *   `PrePay`: subscription.
        self.charge_type = charge_type
        # The edition of the ASM instance. Valid values:
        # 
        # - `standard`: Standard Edition
        # 
        # - `enterprise`: Enterprise Edition
        # 
        # - `ultimate`: Ultimate Edition
        self.cluster_spec = cluster_spec
        # Specifies whether to enable the external service registry. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.config_source_enabled = config_source_enabled
        # The instance ID of the Nacos registry.
        self.config_source_nacos_id = config_source_nacos_id
        # Specifies whether to enable the collection of control plane logs. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.control_plane_log_enabled = control_plane_log_enabled
        # The name of the Log Service project that is used to collect the logs of the control plane.
        self.control_plane_log_project = control_plane_log_project
        # Specifies whether to use a custom Prometheus instance. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.customized_prometheus = customized_prometheus
        # Specifies whether to use a self-managed Zipkin system to collect tracing data. Valid values:
        # 
        # *   `true`: uses a self-managed Zipkin system to collect tracing data.
        # *   `false`: uses Alibaba Cloud Tracing Analysis to collect tracing data.
        # 
        # Default value: `false`.
        self.customized_zipkin = customized_zipkin
        # Specifies whether to enable the DNS proxy feature. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.dnsproxying_enabled = dnsproxying_enabled
        # Specifies whether to enable Dubbo Filter. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.dubbo_filter_enabled = dubbo_filter_enabled
        # The edition of the ASM instance.
        self.edition = edition
        # Specifies whether to enable the mesh audit feature. To enable this feature, make sure that you have activated [Log Service](https://sls.console.aliyun.com/). Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.enable_audit = enable_audit
        # Specifies whether to enable the rollback feature for Istio resources. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.enable_crhistory = enable_crhistory
        # Specifies whether to enable Secret Discovery Service (SDS). Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.enable_sdsserver = enable_sdsserver
        # The IP ranges in CIDR form to be excluded from redirection to the sidecar proxy in the ASM instance.
        self.exclude_ipranges = exclude_ipranges
        # The inbound ports to be excluded from redirection to the sidecar proxy in the ASM instance. Separate multiple port numbers with commas (,).
        self.exclude_inbound_ports = exclude_inbound_ports
        # The outbound ports to be excluded from redirection to the sidecar proxy in the ASM instance. Separate multiple port numbers with commas (,).
        self.exclude_outbound_ports = exclude_outbound_ports
        # The existing CA certificate, which is encoded in Base64. This parameter is used in scenarios where you migrate open source Istio to ASM. It specifies the content of the ca-cert.pem file in the istio-ca-secret secret. The secret is in the istio-system namespace of the Kubernetes cluster where the open source Istio is installed.
        self.existing_ca_cert = existing_ca_cert
        # The existing CA key, which is encoded in Base64. This parameter is used in scenarios where you migrate open source Istio to ASM. It specifies the content of the ca-key.pem file in the istio-ca-secret secret. The secret is in the istio-system namespace of the Kubernetes cluster where the open source Istio is installed.
        self.existing_ca_key = existing_ca_key
        # The type of the existing CA certificate. Valid values:
        # 
        # *   1: Self-signed certificate generated by istiod. The certificate corresponds to the secret named istio-ca-secret in the istio-system namespace. If you use this type of certificate, you must set the `ExistingCaCert` and `ExsitingCaKey` parameters.
        # *   2: Administrator-specified certificate. For more information, see [plugin ca cert](https://istio.io/latest/docs/tasks/security/cert-management/plugin-ca-cert/). In most cases, the certificate corresponds to the secret named cacerts in the istio-system namespace. If you use this type of certificate, you must set the `ExisingRootCaCert` and `ExisingRootCaKey` parameters.
        self.existing_ca_type = existing_ca_type
        # The existing root certificate, which is encoded in Base64.
        self.existing_root_ca_cert = existing_root_ca_cert
        # The private key that corresponds to the root certificate, which is encoded in Base64.
        self.existing_root_ca_key = existing_root_ca_key
        # Specifies whether to enable gateway configuration filtering. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.filter_gateway_cluster_config = filter_gateway_cluster_config
        # Specifies whether to enable Gateway API. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.gateway_apienabled = gateway_apienabled
        # The IP ranges in CIDR form for which traffic is to be redirected to the sidecar proxy in the ASM instance.
        self.include_ipranges = include_ipranges
        # The Istio version of the ASM instance.
        self.istio_version = istio_version
        # Specifies whether to enable the mesh topology feature. To enable this feature, make sure that you have enabled Prometheus monitoring. If Prometheus monitoring is disabled, you must set this parameter to `false`.`` Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.kiali_enabled = kiali_enabled
        # The configurations for the access to the nearest instance.
        self.locality_lbconf = locality_lbconf
        # Specifies whether to route traffic to the nearest instance. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.locality_load_balancing = locality_load_balancing
        # Specifies whether to enable Microservices Engine (MSE). Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.mseenabled = mseenabled
        # Specifies whether to enable MultiBuffer-based Transport Layer Security (TLS) acceleration. Valid values:
        # 
        # - `true`
        # 
        # - `false`
        # 
        # 
        # Default value: `true`
        self.multi_buffer_enabled = multi_buffer_enabled
        # The pull-request latency. Default value: 30. Unit: seconds.
        self.multi_buffer_poll_delay = multi_buffer_poll_delay
        # Specifies whether to enable MySQL Filter. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.mysql_filter_enabled = mysql_filter_enabled
        # The name of the ASM instance.
        self.name = name
        # The maximum number of CPU cores that are available to the OPA container.
        self.opalimit_cpu = opalimit_cpu
        # The maximum size of the memory that is available to the OPA container. You can specify the parameter value in the standard quantity representation form used by Kubernetes. 1 Mi equals 1,024 KB.
        self.opalimit_memory = opalimit_memory
        # The log level of the OPA container.
        self.opalog_level = opalog_level
        # The minimum number of CPU cores that are required by the OPA container. You can specify the parameter value in the standard representation form of CPUs in Kubernetes. For example, if you set the value to 1, one CPU core is required.
        self.oparequest_cpu = oparequest_cpu
        # The minimum size of the memory that is required by the OPA container. You can specify the parameter value in the standard quantity representation form used by Kubernetes. 1 Mi equals 1,024 KB.
        self.oparequest_memory = oparequest_memory
        # Specifies whether to enable the OPA plug-in. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.opa_enabled = opa_enabled
        # Specifies whether to install the Open Policy Agent (OPA) plug-in. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.open_agent_policy = open_agent_policy
        # The subscription period of the SLB instance. Unit: month. This parameter is valid only if the ChargeType parameter is set to PrePay. For example, if the subscription period is one year, set this parameter to 12.
        self.period = period
        # The type of the SLB instance that is bound to Istio Pilot. Valid values: `slb.s1.small`, `slb.s2.small`, `slb.s2.medium`, `slb.s3.small`, `slb.s3.medium`, and `slb.s3.large`.
        self.pilot_load_balancer_spec = pilot_load_balancer_spec
        # The endpoint of the custom Prometheus instance.
        self.prometheus_url = prometheus_url
        # The maximum number of CPU cores that are available to the proxy container.
        self.proxy_limit_cpu = proxy_limit_cpu
        # The maximum size of the memory that is available to the proxy container.
        self.proxy_limit_memory = proxy_limit_memory
        # The minimum number of CPU cores that are required by the proxy container.
        self.proxy_request_cpu = proxy_request_cpu
        # The minimum size of the memory that is required by the proxy container.
        self.proxy_request_memory = proxy_request_memory
        # Specifies whether to enable Redis Filter. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.redis_filter_enabled = redis_filter_enabled
        # The ID of the region in which the ASM instance resides.
        self.region_id = region_id
        # Specifies whether to enable Prometheus monitoring. We recommend that you use Prometheus Service of [Application Real-Time Monitoring Service (ARMS)](https://arms.console.aliyun.com/). Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.telemetry = telemetry
        # Specifies whether to enable Thrift Filter. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.thrift_filter_enabled = thrift_filter_enabled
        # The sampling percentage of Tracing Analysis.
        self.trace_sampling = trace_sampling
        # Specifies whether to enable the Tracing Analysis feature. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.tracing = tracing
        # Specifies whether to use an existing CA certificate and private key.
        self.use_existing_ca = use_existing_ca
        # The ID of the vSwitch to which the ASM instance is connected.
        self.v_switches = v_switches
        # The ID of the virtual private cloud (VPC) in which the ASM instance resides.
        self.vpc_id = vpc_id
        # Specifies whether to enable WebAssembly Filter. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.web_assembly_filter_enabled = web_assembly_filter_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_enabled is not None:
            result['AccessLogEnabled'] = self.access_log_enabled
        if self.access_log_file is not None:
            result['AccessLogFile'] = self.access_log_file
        if self.access_log_format is not None:
            result['AccessLogFormat'] = self.access_log_format
        if self.access_log_project is not None:
            result['AccessLogProject'] = self.access_log_project
        if self.access_log_service_enabled is not None:
            result['AccessLogServiceEnabled'] = self.access_log_service_enabled
        if self.access_log_service_host is not None:
            result['AccessLogServiceHost'] = self.access_log_service_host
        if self.access_log_service_port is not None:
            result['AccessLogServicePort'] = self.access_log_service_port
        if self.api_server_load_balancer_spec is not None:
            result['ApiServerLoadBalancerSpec'] = self.api_server_load_balancer_spec
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.craggregation_enabled is not None:
            result['CRAggregationEnabled'] = self.craggregation_enabled
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.config_source_enabled is not None:
            result['ConfigSourceEnabled'] = self.config_source_enabled
        if self.config_source_nacos_id is not None:
            result['ConfigSourceNacosID'] = self.config_source_nacos_id
        if self.control_plane_log_enabled is not None:
            result['ControlPlaneLogEnabled'] = self.control_plane_log_enabled
        if self.control_plane_log_project is not None:
            result['ControlPlaneLogProject'] = self.control_plane_log_project
        if self.customized_prometheus is not None:
            result['CustomizedPrometheus'] = self.customized_prometheus
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.dnsproxying_enabled is not None:
            result['DNSProxyingEnabled'] = self.dnsproxying_enabled
        if self.dubbo_filter_enabled is not None:
            result['DubboFilterEnabled'] = self.dubbo_filter_enabled
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.enable_crhistory is not None:
            result['EnableCRHistory'] = self.enable_crhistory
        if self.enable_sdsserver is not None:
            result['EnableSDSServer'] = self.enable_sdsserver
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.existing_ca_cert is not None:
            result['ExistingCaCert'] = self.existing_ca_cert
        if self.existing_ca_key is not None:
            result['ExistingCaKey'] = self.existing_ca_key
        if self.existing_ca_type is not None:
            result['ExistingCaType'] = self.existing_ca_type
        if self.existing_root_ca_cert is not None:
            result['ExistingRootCaCert'] = self.existing_root_ca_cert
        if self.existing_root_ca_key is not None:
            result['ExistingRootCaKey'] = self.existing_root_ca_key
        if self.filter_gateway_cluster_config is not None:
            result['FilterGatewayClusterConfig'] = self.filter_gateway_cluster_config
        if self.gateway_apienabled is not None:
            result['GatewayAPIEnabled'] = self.gateway_apienabled
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.kiali_enabled is not None:
            result['KialiEnabled'] = self.kiali_enabled
        if self.locality_lbconf is not None:
            result['LocalityLBConf'] = self.locality_lbconf
        if self.locality_load_balancing is not None:
            result['LocalityLoadBalancing'] = self.locality_load_balancing
        if self.mseenabled is not None:
            result['MSEEnabled'] = self.mseenabled
        if self.multi_buffer_enabled is not None:
            result['MultiBufferEnabled'] = self.multi_buffer_enabled
        if self.multi_buffer_poll_delay is not None:
            result['MultiBufferPollDelay'] = self.multi_buffer_poll_delay
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.opalimit_cpu is not None:
            result['OPALimitCPU'] = self.opalimit_cpu
        if self.opalimit_memory is not None:
            result['OPALimitMemory'] = self.opalimit_memory
        if self.opalog_level is not None:
            result['OPALogLevel'] = self.opalog_level
        if self.oparequest_cpu is not None:
            result['OPARequestCPU'] = self.oparequest_cpu
        if self.oparequest_memory is not None:
            result['OPARequestMemory'] = self.oparequest_memory
        if self.opa_enabled is not None:
            result['OpaEnabled'] = self.opa_enabled
        if self.open_agent_policy is not None:
            result['OpenAgentPolicy'] = self.open_agent_policy
        if self.period is not None:
            result['Period'] = self.period
        if self.pilot_load_balancer_spec is not None:
            result['PilotLoadBalancerSpec'] = self.pilot_load_balancer_spec
        if self.prometheus_url is not None:
            result['PrometheusUrl'] = self.prometheus_url
        if self.proxy_limit_cpu is not None:
            result['ProxyLimitCPU'] = self.proxy_limit_cpu
        if self.proxy_limit_memory is not None:
            result['ProxyLimitMemory'] = self.proxy_limit_memory
        if self.proxy_request_cpu is not None:
            result['ProxyRequestCPU'] = self.proxy_request_cpu
        if self.proxy_request_memory is not None:
            result['ProxyRequestMemory'] = self.proxy_request_memory
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.use_existing_ca is not None:
            result['UseExistingCA'] = self.use_existing_ca
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.web_assembly_filter_enabled is not None:
            result['WebAssemblyFilterEnabled'] = self.web_assembly_filter_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogEnabled') is not None:
            self.access_log_enabled = m.get('AccessLogEnabled')
        if m.get('AccessLogFile') is not None:
            self.access_log_file = m.get('AccessLogFile')
        if m.get('AccessLogFormat') is not None:
            self.access_log_format = m.get('AccessLogFormat')
        if m.get('AccessLogProject') is not None:
            self.access_log_project = m.get('AccessLogProject')
        if m.get('AccessLogServiceEnabled') is not None:
            self.access_log_service_enabled = m.get('AccessLogServiceEnabled')
        if m.get('AccessLogServiceHost') is not None:
            self.access_log_service_host = m.get('AccessLogServiceHost')
        if m.get('AccessLogServicePort') is not None:
            self.access_log_service_port = m.get('AccessLogServicePort')
        if m.get('ApiServerLoadBalancerSpec') is not None:
            self.api_server_load_balancer_spec = m.get('ApiServerLoadBalancerSpec')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('CRAggregationEnabled') is not None:
            self.craggregation_enabled = m.get('CRAggregationEnabled')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('ConfigSourceEnabled') is not None:
            self.config_source_enabled = m.get('ConfigSourceEnabled')
        if m.get('ConfigSourceNacosID') is not None:
            self.config_source_nacos_id = m.get('ConfigSourceNacosID')
        if m.get('ControlPlaneLogEnabled') is not None:
            self.control_plane_log_enabled = m.get('ControlPlaneLogEnabled')
        if m.get('ControlPlaneLogProject') is not None:
            self.control_plane_log_project = m.get('ControlPlaneLogProject')
        if m.get('CustomizedPrometheus') is not None:
            self.customized_prometheus = m.get('CustomizedPrometheus')
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('DNSProxyingEnabled') is not None:
            self.dnsproxying_enabled = m.get('DNSProxyingEnabled')
        if m.get('DubboFilterEnabled') is not None:
            self.dubbo_filter_enabled = m.get('DubboFilterEnabled')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('EnableCRHistory') is not None:
            self.enable_crhistory = m.get('EnableCRHistory')
        if m.get('EnableSDSServer') is not None:
            self.enable_sdsserver = m.get('EnableSDSServer')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('ExistingCaCert') is not None:
            self.existing_ca_cert = m.get('ExistingCaCert')
        if m.get('ExistingCaKey') is not None:
            self.existing_ca_key = m.get('ExistingCaKey')
        if m.get('ExistingCaType') is not None:
            self.existing_ca_type = m.get('ExistingCaType')
        if m.get('ExistingRootCaCert') is not None:
            self.existing_root_ca_cert = m.get('ExistingRootCaCert')
        if m.get('ExistingRootCaKey') is not None:
            self.existing_root_ca_key = m.get('ExistingRootCaKey')
        if m.get('FilterGatewayClusterConfig') is not None:
            self.filter_gateway_cluster_config = m.get('FilterGatewayClusterConfig')
        if m.get('GatewayAPIEnabled') is not None:
            self.gateway_apienabled = m.get('GatewayAPIEnabled')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('KialiEnabled') is not None:
            self.kiali_enabled = m.get('KialiEnabled')
        if m.get('LocalityLBConf') is not None:
            self.locality_lbconf = m.get('LocalityLBConf')
        if m.get('LocalityLoadBalancing') is not None:
            self.locality_load_balancing = m.get('LocalityLoadBalancing')
        if m.get('MSEEnabled') is not None:
            self.mseenabled = m.get('MSEEnabled')
        if m.get('MultiBufferEnabled') is not None:
            self.multi_buffer_enabled = m.get('MultiBufferEnabled')
        if m.get('MultiBufferPollDelay') is not None:
            self.multi_buffer_poll_delay = m.get('MultiBufferPollDelay')
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OPALimitCPU') is not None:
            self.opalimit_cpu = m.get('OPALimitCPU')
        if m.get('OPALimitMemory') is not None:
            self.opalimit_memory = m.get('OPALimitMemory')
        if m.get('OPALogLevel') is not None:
            self.opalog_level = m.get('OPALogLevel')
        if m.get('OPARequestCPU') is not None:
            self.oparequest_cpu = m.get('OPARequestCPU')
        if m.get('OPARequestMemory') is not None:
            self.oparequest_memory = m.get('OPARequestMemory')
        if m.get('OpaEnabled') is not None:
            self.opa_enabled = m.get('OpaEnabled')
        if m.get('OpenAgentPolicy') is not None:
            self.open_agent_policy = m.get('OpenAgentPolicy')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PilotLoadBalancerSpec') is not None:
            self.pilot_load_balancer_spec = m.get('PilotLoadBalancerSpec')
        if m.get('PrometheusUrl') is not None:
            self.prometheus_url = m.get('PrometheusUrl')
        if m.get('ProxyLimitCPU') is not None:
            self.proxy_limit_cpu = m.get('ProxyLimitCPU')
        if m.get('ProxyLimitMemory') is not None:
            self.proxy_limit_memory = m.get('ProxyLimitMemory')
        if m.get('ProxyRequestCPU') is not None:
            self.proxy_request_cpu = m.get('ProxyRequestCPU')
        if m.get('ProxyRequestMemory') is not None:
            self.proxy_request_memory = m.get('ProxyRequestMemory')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('UseExistingCA') is not None:
            self.use_existing_ca = m.get('UseExistingCA')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WebAssemblyFilterEnabled') is not None:
            self.web_assembly_filter_enabled = m.get('WebAssemblyFilterEnabled')
        return self


class CreateServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_mesh_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class CreateServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceMeshResponseBody = None,
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
            temp_model = CreateServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSwimLaneRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        label_selector_key: str = None,
        label_selector_value: str = None,
        service_mesh_id: str = None,
        services_list: str = None,
        swim_lane_name: str = None,
    ):
        # The name of the lane group.
        self.group_name = group_name
        # The label key of the associated service workload. Set the value to `ASM_TRAFFIC_TAG`.
        self.label_selector_key = label_selector_key
        # The label value of the associated service workload.``
        self.label_selector_value = label_selector_value
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The list of services associated with the lane. The value is a JSON array. The format of a single service is `$Cluster name /$Cluster ID/$Namespace/$Service name`.
        self.services_list = services_list
        # The name of the lane.
        self.swim_lane_name = swim_lane_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.label_selector_key is not None:
            result['LabelSelectorKey'] = self.label_selector_key
        if self.label_selector_value is not None:
            result['LabelSelectorValue'] = self.label_selector_value
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.services_list is not None:
            result['ServicesList'] = self.services_list
        if self.swim_lane_name is not None:
            result['SwimLaneName'] = self.swim_lane_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('LabelSelectorKey') is not None:
            self.label_selector_key = m.get('LabelSelectorKey')
        if m.get('LabelSelectorValue') is not None:
            self.label_selector_value = m.get('LabelSelectorValue')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServicesList') is not None:
            self.services_list = m.get('ServicesList')
        if m.get('SwimLaneName') is not None:
            self.swim_lane_name = m.get('SwimLaneName')
        return self


class CreateSwimLaneResponseBody(TeaModel):
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


class CreateSwimLaneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSwimLaneResponseBody = None,
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
            temp_model = CreateSwimLaneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSwimLaneGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ingress_gateway_name: str = None,
        ingress_type: str = None,
        service_mesh_id: str = None,
        services_list: str = None,
    ):
        # The name of the lane group.
        self.group_name = group_name
        # The name of the ingress gateway.
        self.ingress_gateway_name = ingress_gateway_name
        # The type of the gateway for ingress traffic. Only ASM ingress gateways are supported.
        self.ingress_type = ingress_type
        # The ID of the Alibaba Cloud Service Mesh (ASM) instance.
        self.service_mesh_id = service_mesh_id
        # A list of services associated with the lane group. The value is a JSON array. The format of a service is `$Cluster name/$Cluster ID/$Namespace/$Service name`.
        self.services_list = services_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ingress_gateway_name is not None:
            result['IngressGatewayName'] = self.ingress_gateway_name
        if self.ingress_type is not None:
            result['IngressType'] = self.ingress_type
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.services_list is not None:
            result['ServicesList'] = self.services_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IngressGatewayName') is not None:
            self.ingress_gateway_name = m.get('IngressGatewayName')
        if m.get('IngressType') is not None:
            self.ingress_type = m.get('IngressType')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServicesList') is not None:
            self.services_list = m.get('ServicesList')
        return self


class CreateSwimLaneGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class CreateSwimLaneGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSwimLaneGroupResponseBody = None,
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
            temp_model = CreateSwimLaneGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayRouteRequest(TeaModel):
    def __init__(
        self,
        istio_gateway_name: str = None,
        route_name: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The name of the routing rule.
        self.route_name = route_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.route_name is not None:
            result['RouteName'] = self.route_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DeleteGatewayRouteResponseBody(TeaModel):
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


class DeleteGatewayRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayRouteResponseBody = None,
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
            temp_model = DeleteGatewayRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewaySecretRequest(TeaModel):
    def __init__(
        self,
        istio_gateway_name: str = None,
        secret_name: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The name of the secret.
        self.secret_name = secret_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DeleteGatewaySecretResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_delete_record: Dict[str, SecretDeleteRecordValue] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The record of deleting the secret.
        self.secret_delete_record = secret_delete_record

    def validate(self):
        if self.secret_delete_record:
            for v in self.secret_delete_record.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecretDeleteRecord'] = {}
        if self.secret_delete_record is not None:
            for k, v in self.secret_delete_record.items():
                result['SecretDeleteRecord'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.secret_delete_record = {}
        if m.get('SecretDeleteRecord') is not None:
            for k, v in m.get('SecretDeleteRecord').items():
                temp_model = SecretDeleteRecordValue()
                self.secret_delete_record[k] = temp_model.from_map(v)
        return self


class DeleteGatewaySecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewaySecretResponseBody = None,
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
            temp_model = DeleteGatewaySecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIstioGatewayDomainsRequest(TeaModel):
    def __init__(
        self,
        hosts: str = None,
        istio_gateway_name: str = None,
        limit: str = None,
        namespace: str = None,
        port_name: str = None,
        service_mesh_id: str = None,
    ):
        # The domain names of the one or more hosts that are exposed by the ASM gateway. Separate multiple domain names with commas (,).
        self.hosts = hosts
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The maximum number of ASM gateways to query.
        self.limit = limit
        # The namespace in which the ASM gateway resides.
        self.namespace = namespace
        # The name of the port.
        self.port_name = port_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.port_name is not None:
            result['PortName'] = self.port_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DeleteIstioGatewayDomainsResponseBody(TeaModel):
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


class DeleteIstioGatewayDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIstioGatewayDomainsResponseBody = None,
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
            temp_model = DeleteIstioGatewayDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceMeshRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        retain_resources: str = None,
        service_mesh_id: str = None,
    ):
        # Specifies whether to forcibly delete the ASM instance. Valid values:
        # 
        # *   `true`: forcibly deletes the ASM instance.
        # *   `false`: does not forcibly delete the ASM instance.
        # 
        # Default value: false.
        self.force = force
        # A JSON string that can be parsed into a string array. You can use this JSON string to specify the IDs of the resource instances that need to be retained when the ASM instance is deleted.
        self.retain_resources = retain_resources
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.retain_resources is not None:
            result['RetainResources'] = self.retain_resources
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('RetainResources') is not None:
            self.retain_resources = m.get('RetainResources')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DeleteServiceMeshResponseBody(TeaModel):
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


class DeleteServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceMeshResponseBody = None,
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
            temp_model = DeleteServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSwimLaneRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        service_mesh_id: str = None,
        swim_lane_name: str = None,
    ):
        # The name of the lane group.
        self.group_name = group_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The name of the lane.
        self.swim_lane_name = swim_lane_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.swim_lane_name is not None:
            result['SwimLaneName'] = self.swim_lane_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('SwimLaneName') is not None:
            self.swim_lane_name = m.get('SwimLaneName')
        return self


class DeleteSwimLaneResponseBody(TeaModel):
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


class DeleteSwimLaneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSwimLaneResponseBody = None,
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
            temp_model = DeleteSwimLaneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSwimLaneGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the lane group.
        self.group_name = group_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DeleteSwimLaneGroupResponseBody(TeaModel):
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


class DeleteSwimLaneGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSwimLaneGroupResponseBody = None,
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
            temp_model = DeleteSwimLaneGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeASMGatewayImportedServicesRequest(TeaModel):
    def __init__(
        self,
        asmgateway_name: str = None,
        service_mesh_id: str = None,
        service_namespace: str = None,
    ):
        # The name of the ASM gateway.
        self.asmgateway_name = asmgateway_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The namespace in which the service resides.
        self.service_namespace = service_namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asmgateway_name is not None:
            result['ASMGatewayName'] = self.asmgateway_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.service_namespace is not None:
            result['ServiceNamespace'] = self.service_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ASMGatewayName') is not None:
            self.asmgateway_name = m.get('ASMGatewayName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServiceNamespace') is not None:
            self.service_namespace = m.get('ServiceNamespace')
        return self


class DescribeASMGatewayImportedServicesResponseBodyImportedServices(TeaModel):
    def __init__(
        self,
        service_name: str = None,
        service_namespace: str = None,
    ):
        # The name of the service.
        self.service_name = service_name
        # The namespace in which the service resides.
        self.service_namespace = service_namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_namespace is not None:
            result['ServiceNamespace'] = self.service_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceNamespace') is not None:
            self.service_namespace = m.get('ServiceNamespace')
        return self


class DescribeASMGatewayImportedServicesResponseBody(TeaModel):
    def __init__(
        self,
        imported_services: List[DescribeASMGatewayImportedServicesResponseBodyImportedServices] = None,
        request_id: str = None,
    ):
        # The imported services.
        self.imported_services = imported_services
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.imported_services:
            for k in self.imported_services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImportedServices'] = []
        if self.imported_services is not None:
            for k in self.imported_services:
                result['ImportedServices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.imported_services = []
        if m.get('ImportedServices') is not None:
            for k in m.get('ImportedServices'):
                temp_model = DescribeASMGatewayImportedServicesResponseBodyImportedServices()
                self.imported_services.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeASMGatewayImportedServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeASMGatewayImportedServicesResponseBody = None,
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
            temp_model = DescribeASMGatewayImportedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCCMVersionRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The versions of the CCM component in all clusters on the data plane.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeCCMVersionResponseBody(TeaModel):
    def __init__(
        self,
        ccmversions: Dict[str, CCMVersionsValue] = None,
        request_id: str = None,
    ):
        # The ID of the request.
        self.ccmversions = ccmversions
        self.request_id = request_id

    def validate(self):
        if self.ccmversions:
            for v in self.ccmversions.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CCMVersions'] = {}
        if self.ccmversions is not None:
            for k, v in self.ccmversions.items():
                result['CCMVersions'][k] = v.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ccmversions = {}
        if m.get('CCMVersions') is not None:
            for k, v in m.get('CCMVersions').items():
                temp_model = CCMVersionsValue()
                self.ccmversions[k] = temp_model.from_map(v)
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCCMVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCCMVersionResponseBody = None,
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
            temp_model = DescribeCCMVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCensRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeCensResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[str] = None,
        request_id: str = None,
    ):
        # The IDs of the queried Kubernetes clusters.
        self.clusters = clusters
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCensResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCensResponseBody = None,
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
            temp_model = DescribeCensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterGrafanaRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
        service_mesh_id: str = None,
    ):
        # The ID of the cluster on the data plane.
        self.k_8s_cluster_id = k_8s_cluster_id
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeClusterGrafanaResponseBodyDashboards(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        # The title of the Grafana dashboard.
        self.title = title
        # The endpoint of the Grafana dashboard.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeClusterGrafanaResponseBody(TeaModel):
    def __init__(
        self,
        dashboards: List[DescribeClusterGrafanaResponseBodyDashboards] = None,
        request_id: str = None,
    ):
        # The information of Grafana dashboards.
        self.dashboards = dashboards
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k in m.get('Dashboards'):
                temp_model = DescribeClusterGrafanaResponseBodyDashboards()
                self.dashboards.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterGrafanaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterGrafanaResponseBody = None,
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
            temp_model = DescribeClusterGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterPrometheusRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
        k_8s_cluster_region_id: str = None,
        service_mesh_id: str = None,
    ):
        # The ID of the cluster on the data plane.
        self.k_8s_cluster_id = k_8s_cluster_id
        # The ID of the region where the cluster on the data plane resides.
        self.k_8s_cluster_region_id = k_8s_cluster_region_id
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.k_8s_cluster_region_id is not None:
            result['K8sClusterRegionId'] = self.k_8s_cluster_region_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('K8sClusterRegionId') is not None:
            self.k_8s_cluster_region_id = m.get('K8sClusterRegionId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeClusterPrometheusResponseBody(TeaModel):
    def __init__(
        self,
        prometheus: str = None,
        request_id: str = None,
    ):
        # The public endpoint of the Prometheus service that is used to monitor a cluster in the ASM instance.
        self.prometheus = prometheus
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prometheus') is not None:
            self.prometheus = m.get('Prometheus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterPrometheusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterPrometheusResponseBody = None,
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
            temp_model = DescribeClusterPrometheusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersInServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        # The name of the dashboard for access logs.
        self.title = title
        # The URL of the dashboard for access logs.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeClustersInServiceMeshResponseBodyClusters(TeaModel):
    def __init__(
        self,
        access_log_dashboards: List[DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards] = None,
        cluster_domain: str = None,
        cluster_id: str = None,
        cluster_type: str = None,
        creation_time: str = None,
        error_message: str = None,
        logtail_installed_state: str = None,
        name: str = None,
        region_id: str = None,
        sg_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
        vpc_id: str = None,
    ):
        # The configurations of access log collection.
        self.access_log_dashboards = access_log_dashboards
        # The domain of the cluster.
        self.cluster_domain = cluster_domain
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The type of the cluster.
        self.cluster_type = cluster_type
        # The point in time when the cluster was created.
        self.creation_time = creation_time
        # The error message that is returned when the call failed.
        self.error_message = error_message
        # Indicates whether the Logtail component is installed in the cluster. Valid values:
        # 
        # *   `logtail_installed`: The Logtail component is installed.
        # 
        # \-`logtail_uninstalled`: The Logtail component is not installed.
        # 
        # *   `logtail_state_get_error`: The Logtail component fails to be installed.
        self.logtail_installed_state = logtail_installed_state
        # The name of the cluster.
        self.name = name
        # The ID of the region in which the cluster resides.
        self.region_id = region_id
        # The ID of the security group.
        self.sg_id = sg_id
        # The status of the cluster.
        self.state = state
        # The point in time when the cluster was last modified.
        self.update_time = update_time
        # The version number of the cluster.
        self.version = version
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        if self.access_log_dashboards:
            for k in self.access_log_dashboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessLogDashboards'] = []
        if self.access_log_dashboards is not None:
            for k in self.access_log_dashboards:
                result['AccessLogDashboards'].append(k.to_map() if k else None)
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.logtail_installed_state is not None:
            result['LogtailInstalledState'] = self.logtail_installed_state
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_log_dashboards = []
        if m.get('AccessLogDashboards') is not None:
            for k in m.get('AccessLogDashboards'):
                temp_model = DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards()
                self.access_log_dashboards.append(temp_model.from_map(k))
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('LogtailInstalledState') is not None:
            self.logtail_installed_state = m.get('LogtailInstalledState')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeClustersInServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[DescribeClustersInServiceMeshResponseBodyClusters] = None,
        request_id: str = None,
    ):
        # The clusters in the ASM instance.
        self.clusters = clusters
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeClustersInServiceMeshResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClustersInServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClustersInServiceMeshResponseBody = None,
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
            temp_model = DescribeClustersInServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCrTemplatesRequest(TeaModel):
    def __init__(
        self,
        istio_version: str = None,
        kind: str = None,
    ):
        # The Istio version used in ASM.
        self.istio_version = istio_version
        # The type of Istio resource whose common YAML templates you want to query. Valid values:
        # 
        # *   AuthorizationPolicy
        # *   RequestAuthentication
        # *   PeerAuthentication
        # *   WorkloadGroup
        # *   WorkloadEntry
        # *   Sidecar
        # *   EnvoyFilter
        # *   ServiceEntry
        # *   Gateway
        # *   DestinationRule
        # *   VirtualService
        self.kind = kind

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.kind is not None:
            result['Kind'] = self.kind
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('Kind') is not None:
            self.kind = m.get('Kind')
        return self


class DescribeCrTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        chinese_name: str = None,
        english_name: str = None,
        yaml: str = None,
    ):
        # The Chinese name of the YAML template.
        self.chinese_name = chinese_name
        # The English name of the YAML template.
        self.english_name = english_name
        # The content in the YAML template.
        self.yaml = yaml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chinese_name is not None:
            result['ChineseName'] = self.chinese_name
        if self.english_name is not None:
            result['EnglishName'] = self.english_name
        if self.yaml is not None:
            result['Yaml'] = self.yaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChineseName') is not None:
            self.chinese_name = m.get('ChineseName')
        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')
        if m.get('Yaml') is not None:
            self.yaml = m.get('Yaml')
        return self


class DescribeCrTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        templates: List[DescribeCrTemplatesResponseBodyTemplates] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The common YAML templates for the specified type of Istio resource.
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = DescribeCrTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class DescribeCrTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCrTemplatesResponseBody = None,
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
            temp_model = DescribeCrTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEipResourcesRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        service_mesh_id: str = None,
    ):
        # The number of the page to return. Default value: 1.
        self.page_num = page_num
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeEipResourcesResponseBodyEipList(TeaModel):
    def __init__(
        self,
        allocation_id: str = None,
        instance_type: str = None,
        ip_address: str = None,
        status: str = None,
    ):
        # The ID of the EIP.
        self.allocation_id = allocation_id
        # The type of the resource that is associated with the EIP. Valid values:
        # 
        # *   `EcsInstance`: an ECS instance in a VPC
        # *   `SlbInstance`: a Server Load Balancer (SLB) instance in a VPC
        # *   `Nat`: a NAT gateway
        # *   `HaVip`: a high-availability virtual IP address (HAVIP)
        # *   `NetworkInterface`: a secondary elastic network interface (ENI)
        # 
        # Default value: `EcsInstance`.
        self.instance_type = instance_type
        # The IP address of the EIP.
        self.ip_address = ip_address
        # The status of the EIP. Valid values:
        # 
        # *   `Associating`: The EIP is being associated with a resource.
        # *   `Unassociating`: The EIP is being disassociated from a resource.
        # *   `InUse`: The EIP is associated with a resource.
        # *   `Available`: The EIP is available.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeEipResourcesResponseBodyPageResult(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEipResourcesResponseBody(TeaModel):
    def __init__(
        self,
        eip_list: List[DescribeEipResourcesResponseBodyEipList] = None,
        page_result: DescribeEipResourcesResponseBodyPageResult = None,
        request_id: str = None,
    ):
        # The EIPs.
        self.eip_list = eip_list
        # The pagination information.
        self.page_result = page_result
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.eip_list:
            for k in self.eip_list:
                if k:
                    k.validate()
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EipList'] = []
        if self.eip_list is not None:
            for k in self.eip_list:
                result['EipList'].append(k.to_map() if k else None)
        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_list = []
        if m.get('EipList') is not None:
            for k in m.get('EipList'):
                temp_model = DescribeEipResourcesResponseBodyEipList()
                self.eip_list.append(temp_model.from_map(k))
        if m.get('PageResult') is not None:
            temp_model = DescribeEipResourcesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m['PageResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEipResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEipResourcesResponseBody = None,
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
            temp_model = DescribeEipResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewaySecretDetailsRequest(TeaModel):
    def __init__(
        self,
        istio_gateway_name: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeGatewaySecretDetailsResponseBodyGatewaySecretDetails(TeaModel):
    def __init__(
        self,
        expired_time: str = None,
        gateway_name: str = None,
        issue_time: str = None,
        message: str = None,
        sni: str = None,
        secret_name: str = None,
        state: str = None,
    ):
        # The time when the certificate expires.
        self.expired_time = expired_time
        # The name of the gateway.
        self.gateway_name = gateway_name
        # The time when the certificate was issued.
        self.issue_time = issue_time
        # *   An error message is returned if the status of the gateway is abnormal. Examples: `tls.crt not exist`, `tls.key not exist`, and `secret type must be kubernetes.io/tls`.
        # *   An empty value is returned if the status of the gateway is normal.
        self.message = message
        # The Server Name Indication (SNI) value that indicates the hostname of the service.
        self.sni = sni
        # The name of the secret.
        self.secret_name = secret_name
        # The status of the certificate. Valid values:
        # 
        # *   `normal`
        # *   `abnormal`
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.issue_time is not None:
            result['IssueTime'] = self.issue_time
        if self.message is not None:
            result['Message'] = self.message
        if self.sni is not None:
            result['SNI'] = self.sni
        if self.secret_name is not None:
            result['SecretName'] = self.secret_name
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('IssueTime') is not None:
            self.issue_time = m.get('IssueTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SNI') is not None:
            self.sni = m.get('SNI')
        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeGatewaySecretDetailsResponseBody(TeaModel):
    def __init__(
        self,
        gateway_secret_details: List[DescribeGatewaySecretDetailsResponseBodyGatewaySecretDetails] = None,
        request_id: str = None,
    ):
        # The detailed information about the secret of the ASM gateway.
        self.gateway_secret_details = gateway_secret_details
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.gateway_secret_details:
            for k in self.gateway_secret_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GatewaySecretDetails'] = []
        if self.gateway_secret_details is not None:
            for k in self.gateway_secret_details:
                result['GatewaySecretDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway_secret_details = []
        if m.get('GatewaySecretDetails') is not None:
            for k in m.get('GatewaySecretDetails'):
                temp_model = DescribeGatewaySecretDetailsResponseBodyGatewaySecretDetails()
                self.gateway_secret_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGatewaySecretDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewaySecretDetailsResponseBody = None,
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
            temp_model = DescribeGatewaySecretDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGuestClusterAccessLogDashboardsRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
    ):
        # The ID of the cluster on the data plane.
        self.k_8s_cluster_id = k_8s_cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        return self


class DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        # The title of the report.
        self.title = title
        # The URL of the report.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeGuestClusterAccessLogDashboardsResponseBody(TeaModel):
    def __init__(
        self,
        dashboards: List[DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards] = None,
        k_8s_cluster_id: str = None,
        request_id: str = None,
    ):
        # The access log reports of a cluster on the data plane.
        self.dashboards = dashboards
        # The ID of the cluster on the data plane.
        self.k_8s_cluster_id = k_8s_cluster_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k in m.get('Dashboards'):
                temp_model = DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards()
                self.dashboards.append(temp_model.from_map(k))
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGuestClusterAccessLogDashboardsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGuestClusterAccessLogDashboardsResponseBody = None,
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
            temp_model = DescribeGuestClusterAccessLogDashboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGuestClusterNamespacesRequest(TeaModel):
    def __init__(
        self,
        guest_cluster_id: str = None,
        service_mesh_id: str = None,
        show_ns_labels: bool = None,
    ):
        # The ID of the Kubernetes cluster that is added to the ASM instance.
        self.guest_cluster_id = guest_cluster_id
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # Specifies whether to return the labels of the namespaces.
        self.show_ns_labels = show_ns_labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster_id is not None:
            result['GuestClusterID'] = self.guest_cluster_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.show_ns_labels is not None:
            result['ShowNsLabels'] = self.show_ns_labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestClusterID') is not None:
            self.guest_cluster_id = m.get('GuestClusterID')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ShowNsLabels') is not None:
            self.show_ns_labels = m.get('ShowNsLabels')
        return self


class DescribeGuestClusterNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        ns_labels: Dict[str, Any] = None,
        ns_list: List[str] = None,
        request_id: str = None,
    ):
        # The labels of the namespaces. Labels are returned only when the `ShowNsLabels` parameter is set to `true`.
        self.ns_labels = ns_labels
        # The names of the namespaces.
        self.ns_list = ns_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ns_labels is not None:
            result['NsLabels'] = self.ns_labels
        if self.ns_list is not None:
            result['NsList'] = self.ns_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NsLabels') is not None:
            self.ns_labels = m.get('NsLabels')
        if m.get('NsList') is not None:
            self.ns_list = m.get('NsList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGuestClusterNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGuestClusterNamespacesResponseBody = None,
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
            temp_model = DescribeGuestClusterNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGuestClusterPodsRequest(TeaModel):
    def __init__(
        self,
        guest_cluster_id: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        # The ID of the Kubernetes cluster that is added to the ASM instance.
        self.guest_cluster_id = guest_cluster_id
        # The name of the namespace.
        self.namespace = namespace
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster_id is not None:
            result['GuestClusterID'] = self.guest_cluster_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestClusterID') is not None:
            self.guest_cluster_id = m.get('GuestClusterID')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeGuestClusterPodsResponseBody(TeaModel):
    def __init__(
        self,
        pod_list: List[str] = None,
        request_id: str = None,
    ):
        # The names of the queried pods.
        self.pod_list = pod_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pod_list is not None:
            result['PodList'] = self.pod_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PodList') is not None:
            self.pod_list = m.get('PodList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGuestClusterPodsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGuestClusterPodsResponseBody = None,
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
            temp_model = DescribeGuestClusterPodsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImportedServicesDetailRequest(TeaModel):
    def __init__(
        self,
        asmgateway_name: str = None,
        service_mesh_id: str = None,
        service_namespace: str = None,
    ):
        # The name of the service.
        self.asmgateway_name = asmgateway_name
        # The details of the services.
        self.service_mesh_id = service_mesh_id
        # The namespace in which the service resides.
        self.service_namespace = service_namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asmgateway_name is not None:
            result['ASMGatewayName'] = self.asmgateway_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.service_namespace is not None:
            result['ServiceNamespace'] = self.service_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ASMGatewayName') is not None:
            self.asmgateway_name = m.get('ASMGatewayName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServiceNamespace') is not None:
            self.service_namespace = m.get('ServiceNamespace')
        return self


class DescribeImportedServicesDetailResponseBodyDetailsPorts(TeaModel):
    def __init__(
        self,
        name: str = None,
        node_port: int = None,
        port: int = None,
        protocol: str = None,
        target_port: int = None,
    ):
        # The container port.
        self.name = name
        self.node_port = node_port
        self.port = port
        # The node port.
        self.protocol = protocol
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.node_port is not None:
            result['NodePort'] = self.node_port
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodePort') is not None:
            self.node_port = m.get('NodePort')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class DescribeImportedServicesDetailResponseBodyDetails(TeaModel):
    def __init__(
        self,
        cluster_ids: List[str] = None,
        labels: Dict[str, str] = None,
        namespace: str = None,
        ports: List[DescribeImportedServicesDetailResponseBodyDetailsPorts] = None,
        service_name: str = None,
        service_type: str = None,
    ):
        # The name of the port.
        self.cluster_ids = cluster_ids
        # The ports declared for the service.
        self.labels = labels
        # Kubernetes
        self.namespace = namespace
        # The port number.
        self.ports = ports
        # The type of the service.
        self.service_name = service_name
        # The protocol of the port.
        self.service_type = service_type

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeImportedServicesDetailResponseBodyDetailsPorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class DescribeImportedServicesDetailResponseBody(TeaModel):
    def __init__(
        self,
        details: List[DescribeImportedServicesDetailResponseBodyDetails] = None,
        request_id: str = None,
    ):
        # The IDs of the clusters to which the service belongs.
        self.details = details
        # The labels of the service.
        self.request_id = request_id

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = DescribeImportedServicesDetailResponseBodyDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImportedServicesDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImportedServicesDetailResponseBody = None,
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
            temp_model = DescribeImportedServicesDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIstioGatewayDomainsRequest(TeaModel):
    def __init__(
        self,
        istio_gateway_name: str = None,
        limit: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The maximum number of ASM gateways to query.
        self.limit = limit
        # The namespace in which the ASM gateway resides.
        self.namespace = namespace
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeIstioGatewayDomainsResponseBodyGatewaySecretDetails(TeaModel):
    def __init__(
        self,
        credential_name: str = None,
        detail: str = None,
        domains: List[str] = None,
        gateway_crname: str = None,
        namespace: str = None,
        port_name: str = None,
        protocol: str = None,
    ):
        # The name of the secret that contains the Transport Layer Security (TLS) certificate and certificate authority (CA) certificate.
        self.credential_name = credential_name
        # The details of the domain name in the JSON format.
        self.detail = detail
        # The domain name.
        self.domains = domains
        self.gateway_crname = gateway_crname
        # The namespace in which the ASM gateway resides.
        self.namespace = namespace
        # The name of the port.
        self.port_name = port_name
        # The type of the protocol. Valid values: `HTTP`, `HTTPS`, `GRPC`, `HTTP2`, `MONGO`, `TCP`, and `TLS`.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_name is not None:
            result['CredentialName'] = self.credential_name
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.gateway_crname is not None:
            result['GatewayCRName'] = self.gateway_crname
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.port_name is not None:
            result['PortName'] = self.port_name
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialName') is not None:
            self.credential_name = m.get('CredentialName')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('GatewayCRName') is not None:
            self.gateway_crname = m.get('GatewayCRName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeIstioGatewayDomainsResponseBody(TeaModel):
    def __init__(
        self,
        gateway_secret_details: List[DescribeIstioGatewayDomainsResponseBodyGatewaySecretDetails] = None,
        request_id: str = None,
    ):
        # The domain names that are exposed by the ASM gateway.
        self.gateway_secret_details = gateway_secret_details
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.gateway_secret_details:
            for k in self.gateway_secret_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GatewaySecretDetails'] = []
        if self.gateway_secret_details is not None:
            for k in self.gateway_secret_details:
                result['GatewaySecretDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway_secret_details = []
        if m.get('GatewaySecretDetails') is not None:
            for k in m.get('GatewaySecretDetails'):
                temp_model = DescribeIstioGatewayDomainsResponseBodyGatewaySecretDetails()
                self.gateway_secret_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIstioGatewayDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIstioGatewayDomainsResponseBody = None,
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
            temp_model = DescribeIstioGatewayDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIstioGatewayRouteDetailRequest(TeaModel):
    def __init__(
        self,
        istio_gateway_name: str = None,
        route_name: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The name of the routing rule.
        self.route_name = route_name
        # The ASM instance ID.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.route_name is not None:
            result['RouteName'] = self.route_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsDelegate(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
    ):
        # The name of the virtual service.
        self.name = name
        # The namespace to which the virtual service belongs.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultAbortPercentage(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The percentage of requests that are mirrored to another destination except for the original destination, which is expressed as a decimal.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultAbort(TeaModel):
    def __init__(
        self,
        http_status: int = None,
        percentage: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultAbortPercentage = None,
    ):
        # The HTTP status code.
        self.http_status = http_status
        # The percentage of requests that are aborted with the specified error code.
        self.percentage = percentage

    def validate(self):
        if self.percentage:
            self.percentage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status is not None:
            result['HttpStatus'] = self.http_status
        if self.percentage is not None:
            result['Percentage'] = self.percentage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')
        if m.get('Percentage') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultAbortPercentage()
            self.percentage = temp_model.from_map(m['Percentage'])
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultDelayPercentage(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The percentage of requests that are aborted with the specified error code, which is expressed as a decimal.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultDelay(TeaModel):
    def __init__(
        self,
        exponential_delay: str = None,
        fixed_delay: str = None,
        percentage: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultDelayPercentage = None,
    ):
        # The duration for request delay is expressed as 2 raised to the power of x. You must specify the value of x.
        self.exponential_delay = exponential_delay
        # The fixed duration for request delay.
        self.fixed_delay = fixed_delay
        # The percentage of requests to which the delay fault is injected.
        self.percentage = percentage

    def validate(self):
        if self.percentage:
            self.percentage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exponential_delay is not None:
            result['ExponentialDelay'] = self.exponential_delay
        if self.fixed_delay is not None:
            result['FixedDelay'] = self.fixed_delay
        if self.percentage is not None:
            result['Percentage'] = self.percentage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExponentialDelay') is not None:
            self.exponential_delay = m.get('ExponentialDelay')
        if m.get('FixedDelay') is not None:
            self.fixed_delay = m.get('FixedDelay')
        if m.get('Percentage') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultDelayPercentage()
            self.percentage = temp_model.from_map(m['Percentage'])
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFault(TeaModel):
    def __init__(
        self,
        abort: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultAbort = None,
        delay: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultDelay = None,
    ):
        # The configurations for aborting requests with specified error codes.
        self.abort = abort
        # The duration to delay a request.
        self.delay = delay

    def validate(self):
        if self.abort:
            self.abort.validate()
        if self.delay:
            self.delay.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abort is not None:
            result['Abort'] = self.abort.to_map()
        if self.delay is not None:
            result['Delay'] = self.delay.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abort') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultAbort()
            self.abort = temp_model.from_map(m['Abort'])
        if m.get('Delay') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFaultDelay()
            self.delay = temp_model.from_map(m['Delay'])
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsHTTPRedirect(TeaModel):
    def __init__(
        self,
        authority: str = None,
        redirect_code: int = None,
        uri: str = None,
    ):
        # The value to be used to overwrite the value of the Authority or Host header during redirection.
        self.authority = authority
        # The HTTP status code to be used to indicate URL redirection. Default value: 301.
        self.redirect_code = redirect_code
        # The value to be used to overwrite the URL path during redirection.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.redirect_code is not None:
            result['RedirectCode'] = self.redirect_code
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('RedirectCode') is not None:
            self.redirect_code = m.get('RedirectCode')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsMirror(TeaModel):
    def __init__(
        self,
        host: str = None,
        subset: str = None,
    ):
        # The name of the service defined in the service registry.
        self.host = host
        # The name of the service subset.
        self.subset = subset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.subset is not None:
            result['Subset'] = self.subset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Subset') is not None:
            self.subset = m.get('Subset')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsMirrorPercentage(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The percentage of requests that are aborted with the specified error code, which is expressed as a decimal.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsRetriesRetryRemoteLocalities(TeaModel):
    def __init__(
        self,
        value: bool = None,
    ):
        # Specifies whether to allow retries to other localities. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsRetries(TeaModel):
    def __init__(
        self,
        attempts: int = None,
        per_try_timeout: str = None,
        retry_on: str = None,
        retry_remote_localities: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsRetriesRetryRemoteLocalities = None,
    ):
        # The number of retries that are allowed for a request.
        self.attempts = attempts
        # The timeout period for each retry.
        self.per_try_timeout = per_try_timeout
        # The condition for retries. Example: `connect-failure,refused-stream,503`.
        self.retry_on = retry_on
        # Specifies whether to allow retries to other localities.
        self.retry_remote_localities = retry_remote_localities

    def validate(self):
        if self.retry_remote_localities:
            self.retry_remote_localities.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempts is not None:
            result['Attempts'] = self.attempts
        if self.per_try_timeout is not None:
            result['PerTryTimeout'] = self.per_try_timeout
        if self.retry_on is not None:
            result['RetryOn'] = self.retry_on
        if self.retry_remote_localities is not None:
            result['RetryRemoteLocalities'] = self.retry_remote_localities.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attempts') is not None:
            self.attempts = m.get('Attempts')
        if m.get('PerTryTimeout') is not None:
            self.per_try_timeout = m.get('PerTryTimeout')
        if m.get('RetryOn') is not None:
            self.retry_on = m.get('RetryOn')
        if m.get('RetryRemoteLocalities') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsRetriesRetryRemoteLocalities()
            self.retry_remote_localities = temp_model.from_map(m['RetryRemoteLocalities'])
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsRewrite(TeaModel):
    def __init__(
        self,
        authority: str = None,
        uri: str = None,
    ):
        # The value to be used to overwrite the value of the Authority or Host header.
        self.authority = authority
        # The value to be used to overwrite the path or prefix of the URI.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptions(TeaModel):
    def __init__(
        self,
        delegate: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsDelegate = None,
        fault: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFault = None,
        httpredirect: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsHTTPRedirect = None,
        mirror: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsMirror = None,
        mirror_percentage: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsMirrorPercentage = None,
        retries: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsRetries = None,
        rewrite: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsRewrite = None,
        timeout: str = None,
    ):
        # The virtual service that defines traffic routing.
        self.delegate = delegate
        # The configurations of fault injection.
        self.fault = fault
        # The HTTP redirection rule.
        self.httpredirect = httpredirect
        # The configurations for mirroring HTTP traffic to another destination in addition to forwarding requests to the specified destination.
        self.mirror = mirror
        # The percentage of requests that are aborted with the specified error code.
        self.mirror_percentage = mirror_percentage
        # The configurations of retries for failed requests.
        self.retries = retries
        # The configurations for rewriting the virtual service.
        self.rewrite = rewrite
        # The timeout period for requests.
        self.timeout = timeout

    def validate(self):
        if self.delegate:
            self.delegate.validate()
        if self.fault:
            self.fault.validate()
        if self.httpredirect:
            self.httpredirect.validate()
        if self.mirror:
            self.mirror.validate()
        if self.mirror_percentage:
            self.mirror_percentage.validate()
        if self.retries:
            self.retries.validate()
        if self.rewrite:
            self.rewrite.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delegate is not None:
            result['Delegate'] = self.delegate.to_map()
        if self.fault is not None:
            result['Fault'] = self.fault.to_map()
        if self.httpredirect is not None:
            result['HTTPRedirect'] = self.httpredirect.to_map()
        if self.mirror is not None:
            result['Mirror'] = self.mirror.to_map()
        if self.mirror_percentage is not None:
            result['MirrorPercentage'] = self.mirror_percentage.to_map()
        if self.retries is not None:
            result['Retries'] = self.retries.to_map()
        if self.rewrite is not None:
            result['Rewrite'] = self.rewrite.to_map()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delegate') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsDelegate()
            self.delegate = temp_model.from_map(m['Delegate'])
        if m.get('Fault') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsFault()
            self.fault = temp_model.from_map(m['Fault'])
        if m.get('HTTPRedirect') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsHTTPRedirect()
            self.httpredirect = temp_model.from_map(m['HTTPRedirect'])
        if m.get('Mirror') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsMirror()
            self.mirror = temp_model.from_map(m['Mirror'])
        if m.get('MirrorPercentage') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsMirrorPercentage()
            self.mirror_percentage = temp_model.from_map(m['MirrorPercentage'])
        if m.get('Retries') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsRetries()
            self.retries = temp_model.from_map(m['Retries'])
        if m.get('Rewrite') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptionsRewrite()
            self.rewrite = temp_model.from_map(m['Rewrite'])
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequestHeaders(TeaModel):
    def __init__(
        self,
        matching_content: str = None,
        matching_mode: str = None,
        name: str = None,
    ):
        # The header value to be matched.
        self.matching_content = matching_content
        # The matching mode for the header value. Valid values:
        # 
        # *   `exact`: exact match
        # *   `prefix`: match by prefix
        # *   `regex`: match by regular expression
        self.matching_mode = matching_mode
        # The header key to be matched.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.matching_content is not None:
            result['MatchingContent'] = self.matching_content
        if self.matching_mode is not None:
            result['MatchingMode'] = self.matching_mode
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchingContent') is not None:
            self.matching_content = m.get('MatchingContent')
        if m.get('MatchingMode') is not None:
            self.matching_mode = m.get('MatchingMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequestTLSMatchAttributes(TeaModel):
    def __init__(
        self,
        snihosts: List[str] = None,
        tlsport: int = None,
    ):
        # The Server Name Indication (SNI) values to be matched.
        self.snihosts = snihosts
        # The TLS port.
        self.tlsport = tlsport

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snihosts is not None:
            result['SNIHosts'] = self.snihosts
        if self.tlsport is not None:
            result['TLSPort'] = self.tlsport
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SNIHosts') is not None:
            self.snihosts = m.get('SNIHosts')
        if m.get('TLSPort') is not None:
            self.tlsport = m.get('TLSPort')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequestURI(TeaModel):
    def __init__(
        self,
        matching_content: str = None,
        matching_mode: str = None,
    ):
        # The content to be matched.
        self.matching_content = matching_content
        # The matching mode. Valid values:
        # 
        # *   `exact`: exact match
        # *   `prefix`: match by prefix
        # *   `regex`: match by regular expression
        self.matching_mode = matching_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.matching_content is not None:
            result['MatchingContent'] = self.matching_content
        if self.matching_mode is not None:
            result['MatchingMode'] = self.matching_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchingContent') is not None:
            self.matching_content = m.get('MatchingContent')
        if m.get('MatchingMode') is not None:
            self.matching_mode = m.get('MatchingMode')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequest(TeaModel):
    def __init__(
        self,
        headers: List[DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequestHeaders] = None,
        ports: List[int] = None,
        tlsmatch_attributes: List[DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequestTLSMatchAttributes] = None,
        uri: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequestURI = None,
    ):
        # The request headers to be matched.
        self.headers = headers
        # The ports.
        self.ports = ports
        # The matching rules for Transport Layer Security (TLS) traffic.
        self.tlsmatch_attributes = tlsmatch_attributes
        # The matching rule for URIs.
        self.uri = uri

    def validate(self):
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()
        if self.tlsmatch_attributes:
            for k in self.tlsmatch_attributes:
                if k:
                    k.validate()
        if self.uri:
            self.uri.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Headers'] = []
        if self.headers is not None:
            for k in self.headers:
                result['Headers'].append(k.to_map() if k else None)
        if self.ports is not None:
            result['Ports'] = self.ports
        result['TLSMatchAttributes'] = []
        if self.tlsmatch_attributes is not None:
            for k in self.tlsmatch_attributes:
                result['TLSMatchAttributes'].append(k.to_map() if k else None)
        if self.uri is not None:
            result['URI'] = self.uri.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('Headers') is not None:
            for k in m.get('Headers'):
                temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequestHeaders()
                self.headers.append(temp_model.from_map(k))
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        self.tlsmatch_attributes = []
        if m.get('TLSMatchAttributes') is not None:
            for k in m.get('TLSMatchAttributes'):
                temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequestTLSMatchAttributes()
                self.tlsmatch_attributes.append(temp_model.from_map(k))
        if m.get('URI') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequestURI()
            self.uri = temp_model.from_map(m['URI'])
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsDestinationPort(TeaModel):
    def __init__(
        self,
        number: int = None,
    ):
        # The ports of the specified hosts to which the traffic is routed.
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsDestination(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsDestinationPort = None,
        subset: str = None,
    ):
        # The name of the service defined in the service registry.
        self.host = host
        # The ports.
        self.port = port
        # The name of the service subset.
        self.subset = subset

    def validate(self):
        if self.port:
            self.port.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port.to_map()
        if self.subset is not None:
            result['Subset'] = self.subset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsDestinationPort()
            self.port = temp_model.from_map(m['Port'])
        if m.get('Subset') is not None:
            self.subset = m.get('Subset')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsHeadersRequest(TeaModel):
    def __init__(
        self,
        add: Dict[str, Any] = None,
        remove: List[str] = None,
        set: Dict[str, str] = None,
    ):
        # The values to be added to the header key.
        self.add = add
        # The header value to be deleted.
        self.remove = remove
        # The header key to be used to overwrite the original header key.
        self.set = set

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        if self.remove is not None:
            result['Remove'] = self.remove
        if self.set is not None:
            result['Set'] = self.set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        if m.get('Remove') is not None:
            self.remove = m.get('Remove')
        if m.get('Set') is not None:
            self.set = m.get('Set')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsHeadersResponse(TeaModel):
    def __init__(
        self,
        add: Dict[str, Any] = None,
        remove: List[str] = None,
        set: Dict[str, Any] = None,
    ):
        # The values to be added to the header key.
        self.add = add
        # The header value to be deleted.
        self.remove = remove
        # The header key to be used to overwrite the original header key.
        self.set = set

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add is not None:
            result['Add'] = self.add
        if self.remove is not None:
            result['Remove'] = self.remove
        if self.set is not None:
            result['Set'] = self.set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Add') is not None:
            self.add = m.get('Add')
        if m.get('Remove') is not None:
            self.remove = m.get('Remove')
        if m.get('Set') is not None:
            self.set = m.get('Set')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsHeaders(TeaModel):
    def __init__(
        self,
        request: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsHeadersRequest = None,
        response: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsHeadersResponse = None,
    ):
        # The request header to be matched.
        self.request = request
        # The processing of the headers of the response that is to be returned.
        self.response = response

    def validate(self):
        if self.request:
            self.request.validate()
        if self.response:
            self.response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        if self.response is not None:
            result['Response'] = self.response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsHeadersRequest()
            self.request = temp_model.from_map(m['Request'])
        if m.get('Response') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsHeadersResponse()
            self.response = temp_model.from_map(m['Response'])
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinations(TeaModel):
    def __init__(
        self,
        destination: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsDestination = None,
        headers: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsHeaders = None,
        weight: int = None,
    ):
        # The unique endpoint of the destination service to which the specified requests are sent.
        self.destination = destination
        # The request headers to be matched.
        self.headers = headers
        # The traffic weight. Valid values: 1 to 100.
        self.weight = weight

    def validate(self):
        if self.destination:
            self.destination.validate()
        if self.headers:
            self.headers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination.to_map()
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsDestination()
            self.destination = temp_model.from_map(m['Destination'])
        if m.get('Headers') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinationsHeaders()
            self.headers = temp_model.from_map(m['Headers'])
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class DescribeIstioGatewayRouteDetailResponseBodyRouteDetail(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        httpadvanced_options: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptions = None,
        has_unsafe_features: bool = None,
        match_request: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequest = None,
        raw_vsroute: str = None,
        route_destinations: List[DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinations] = None,
        route_name: str = None,
        route_type: str = None,
    ):
        self.domains = domains
        # The advanced settings for routing HTTP traffic.
        self.httpadvanced_options = httpadvanced_options
        self.has_unsafe_features = has_unsafe_features
        # The matching rules for traffic routing.
        self.match_request = match_request
        self.raw_vsroute = raw_vsroute
        # The endpoints of destination services for Layer 4 weighted routing.
        self.route_destinations = route_destinations
        # The name of the routing rule.
        self.route_name = route_name
        # The type of the traffic to be routed. Valid values: `HTTP`, `TLS`, and `TCP`.
        self.route_type = route_type

    def validate(self):
        if self.httpadvanced_options:
            self.httpadvanced_options.validate()
        if self.match_request:
            self.match_request.validate()
        if self.route_destinations:
            for k in self.route_destinations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.httpadvanced_options is not None:
            result['HTTPAdvancedOptions'] = self.httpadvanced_options.to_map()
        if self.has_unsafe_features is not None:
            result['HasUnsafeFeatures'] = self.has_unsafe_features
        if self.match_request is not None:
            result['MatchRequest'] = self.match_request.to_map()
        if self.raw_vsroute is not None:
            result['RawVSRoute'] = self.raw_vsroute
        result['RouteDestinations'] = []
        if self.route_destinations is not None:
            for k in self.route_destinations:
                result['RouteDestinations'].append(k.to_map() if k else None)
        if self.route_name is not None:
            result['RouteName'] = self.route_name
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('HTTPAdvancedOptions') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptions()
            self.httpadvanced_options = temp_model.from_map(m['HTTPAdvancedOptions'])
        if m.get('HasUnsafeFeatures') is not None:
            self.has_unsafe_features = m.get('HasUnsafeFeatures')
        if m.get('MatchRequest') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequest()
            self.match_request = temp_model.from_map(m['MatchRequest'])
        if m.get('RawVSRoute') is not None:
            self.raw_vsroute = m.get('RawVSRoute')
        self.route_destinations = []
        if m.get('RouteDestinations') is not None:
            for k in m.get('RouteDestinations'):
                temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinations()
                self.route_destinations.append(temp_model.from_map(k))
        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        return self


class DescribeIstioGatewayRouteDetailResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        namespace: str = None,
        priority: int = None,
        request_id: str = None,
        route_detail: DescribeIstioGatewayRouteDetailResponseBodyRouteDetail = None,
        status: int = None,
    ):
        # The description of the routing rule.
        self.description = description
        # The namespace.
        self.namespace = namespace
        # The priority of the routing rule. The value of this parameter is an integer. A smaller value indicates a higher priority.
        self.priority = priority
        # The request ID.
        self.request_id = request_id
        # The detailed information about the routing rule.
        self.route_detail = route_detail
        # The status of the routing rule. Valid values:
        # 
        # *   `0`: The routing rule is valid.
        # *   `1`: The routing rule is invalid.
        # *   `2`: An error occurs during the creation or update of the routing rule.
        self.status = status

    def validate(self):
        if self.route_detail:
            self.route_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route_detail is not None:
            result['RouteDetail'] = self.route_detail.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RouteDetail') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetail()
            self.route_detail = temp_model.from_map(m['RouteDetail'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeIstioGatewayRouteDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIstioGatewayRouteDetailResponseBody = None,
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
            temp_model = DescribeIstioGatewayRouteDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIstioGatewayRoutesRequest(TeaModel):
    def __init__(
        self,
        istio_gateway_name: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The ASM instance ID.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeIstioGatewayRoutesResponseBodyManagementRoutes(TeaModel):
    def __init__(
        self,
        asmgateway_name: str = None,
        description: str = None,
        destination_host: List[str] = None,
        destination_sub_set: List[str] = None,
        namespace: str = None,
        priority: int = None,
        route_name: str = None,
        route_path: str = None,
        status: int = None,
    ):
        # The name of the ASM gateway.
        self.asmgateway_name = asmgateway_name
        # The description of the routing rule.
        self.description = description
        self.destination_host = destination_host
        self.destination_sub_set = destination_sub_set
        # The namespace.
        self.namespace = namespace
        # The priority of the routing rule. The value of this parameter is an integer. A smaller value indicates a higher priority.
        self.priority = priority
        # The name of the routing rule.
        self.route_name = route_name
        # The path that is used to match request URLs.
        self.route_path = route_path
        # The status of the routing rule. Valid values:
        # 
        # *   `0`: The routing rule is valid.
        # *   `1`: The routing rule is invalid.
        # *   `2`: An error occurs during the creation or update of the routing rule.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asmgateway_name is not None:
            result['ASMGatewayName'] = self.asmgateway_name
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_host is not None:
            result['DestinationHost'] = self.destination_host
        if self.destination_sub_set is not None:
            result['DestinationSubSet'] = self.destination_sub_set
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.route_name is not None:
            result['RouteName'] = self.route_name
        if self.route_path is not None:
            result['RoutePath'] = self.route_path
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ASMGatewayName') is not None:
            self.asmgateway_name = m.get('ASMGatewayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationHost') is not None:
            self.destination_host = m.get('DestinationHost')
        if m.get('DestinationSubSet') is not None:
            self.destination_sub_set = m.get('DestinationSubSet')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')
        if m.get('RoutePath') is not None:
            self.route_path = m.get('RoutePath')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeIstioGatewayRoutesResponseBody(TeaModel):
    def __init__(
        self,
        management_routes: List[DescribeIstioGatewayRoutesResponseBodyManagementRoutes] = None,
        request_id: str = None,
    ):
        # The routing rules.
        self.management_routes = management_routes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.management_routes:
            for k in self.management_routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ManagementRoutes'] = []
        if self.management_routes is not None:
            for k in self.management_routes:
                result['ManagementRoutes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.management_routes = []
        if m.get('ManagementRoutes') is not None:
            for k in m.get('ManagementRoutes'):
                temp_model = DescribeIstioGatewayRoutesResponseBodyManagementRoutes()
                self.management_routes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIstioGatewayRoutesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIstioGatewayRoutesResponseBody = None,
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
            temp_model = DescribeIstioGatewayRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMetadataResponseBodyMetaDataProEdition(TeaModel):
    def __init__(
        self,
        current_version: str = None,
        version_crds: List[Dict[str, Any]] = None,
        version_registry: List[Dict[str, Any]] = None,
        versions: List[str] = None,
    ):
        # The current version.
        self.current_version = current_version
        # The CRDs of the versions.
        self.version_crds = version_crds
        # The ASM version and the corresponding Istio version.
        self.version_registry = version_registry
        # The supported versions.
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.version_crds is not None:
            result['VersionCrds'] = self.version_crds
        if self.version_registry is not None:
            result['VersionRegistry'] = self.version_registry
        if self.versions is not None:
            result['Versions'] = self.versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('VersionCrds') is not None:
            self.version_crds = m.get('VersionCrds')
        if m.get('VersionRegistry') is not None:
            self.version_registry = m.get('VersionRegistry')
        if m.get('Versions') is not None:
            self.versions = m.get('Versions')
        return self


class DescribeMetadataResponseBodyMetaData(TeaModel):
    def __init__(
        self,
        current_version: str = None,
        pro_edition: DescribeMetadataResponseBodyMetaDataProEdition = None,
        regions: List[str] = None,
        version_crds: List[Dict[str, Any]] = None,
        version_registry: List[Dict[str, Any]] = None,
        versions: List[str] = None,
    ):
        # The current version.
        self.current_version = current_version
        # The version information about ASM of a commercial edition.
        self.pro_edition = pro_edition
        # The regions where ASM instances can be created.
        self.regions = regions
        # The Custom Resource Definitions (CRDs) of the versions.
        self.version_crds = version_crds
        # The ASM version and the corresponding Istio version.
        self.version_registry = version_registry
        # The supported versions.
        self.versions = versions

    def validate(self):
        if self.pro_edition:
            self.pro_edition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.pro_edition is not None:
            result['ProEdition'] = self.pro_edition.to_map()
        if self.regions is not None:
            result['Regions'] = self.regions
        if self.version_crds is not None:
            result['VersionCrds'] = self.version_crds
        if self.version_registry is not None:
            result['VersionRegistry'] = self.version_registry
        if self.versions is not None:
            result['Versions'] = self.versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('ProEdition') is not None:
            temp_model = DescribeMetadataResponseBodyMetaDataProEdition()
            self.pro_edition = temp_model.from_map(m['ProEdition'])
        if m.get('Regions') is not None:
            self.regions = m.get('Regions')
        if m.get('VersionCrds') is not None:
            self.version_crds = m.get('VersionCrds')
        if m.get('VersionRegistry') is not None:
            self.version_registry = m.get('VersionRegistry')
        if m.get('Versions') is not None:
            self.versions = m.get('Versions')
        return self


class DescribeMetadataResponseBody(TeaModel):
    def __init__(
        self,
        meta_data: DescribeMetadataResponseBodyMetaData = None,
        request_id: str = None,
    ):
        # The metadata of ASM, which contains basic information about ASM.
        self.meta_data = meta_data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaData') is not None:
            temp_model = DescribeMetadataResponseBodyMetaData()
            self.meta_data = temp_model.from_map(m['MetaData'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMetadataResponseBody = None,
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
            temp_model = DescribeMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceScopeSidecarConfigRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        # The namespace.
        self.namespace = namespace
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesProxyStatsMatcher(TeaModel):
    def __init__(
        self,
        inclusion_prefixes: List[str] = None,
        inclusion_regexps: List[str] = None,
        inclusion_suffixes: List[str] = None,
    ):
        # The prefixes of the custom Envoy statistics that are reported by the sidecar proxy.
        self.inclusion_prefixes = inclusion_prefixes
        # The regular expressions for specifying the custom Envoy statistics that are reported by the sidecar proxy.
        self.inclusion_regexps = inclusion_regexps
        # The suffixes of the custom Envoy statistics that are reported by the sidecar proxy.
        self.inclusion_suffixes = inclusion_suffixes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inclusion_prefixes is not None:
            result['InclusionPrefixes'] = self.inclusion_prefixes
        if self.inclusion_regexps is not None:
            result['InclusionRegexps'] = self.inclusion_regexps
        if self.inclusion_suffixes is not None:
            result['InclusionSuffixes'] = self.inclusion_suffixes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InclusionPrefixes') is not None:
            self.inclusion_prefixes = m.get('InclusionPrefixes')
        if m.get('InclusionRegexps') is not None:
            self.inclusion_regexps = m.get('InclusionRegexps')
        if m.get('InclusionSuffixes') is not None:
            self.inclusion_suffixes = m.get('InclusionSuffixes')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyAckSloResource(TeaModel):
    def __init__(
        self,
        limits: Dict[str, str] = None,
        requests: Dict[str, str] = None,
    ):
        self.limits = limits
        self.requests = requests

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limits is not None:
            result['Limits'] = self.limits
        if self.requests is not None:
            result['Requests'] = self.requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limits') is not None:
            self.limits = m.get('Limits')
        if m.get('Requests') is not None:
            self.requests = m.get('Requests')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitAckSloResource(TeaModel):
    def __init__(
        self,
        limits: Dict[str, str] = None,
        requests: Dict[str, str] = None,
    ):
        self.limits = limits
        self.requests = requests

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limits is not None:
            result['Limits'] = self.limits
        if self.requests is not None:
            result['Requests'] = self.requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limits') is not None:
            self.limits = m.get('Limits')
        if m.get('Requests') is not None:
            self.requests = m.get('Requests')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceLimit(TeaModel):
    def __init__(
        self,
        resource_cpulimit: str = None,
        resource_memory_limit: str = None,
    ):
        # The maximum number of CPU cores.
        self.resource_cpulimit = resource_cpulimit
        # The maximum size of the memory.
        self.resource_memory_limit = resource_memory_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpulimit is not None:
            result['ResourceCPULimit'] = self.resource_cpulimit
        if self.resource_memory_limit is not None:
            result['ResourceMemoryLimit'] = self.resource_memory_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPULimit') is not None:
            self.resource_cpulimit = m.get('ResourceCPULimit')
        if m.get('ResourceMemoryLimit') is not None:
            self.resource_memory_limit = m.get('ResourceMemoryLimit')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceRequest(TeaModel):
    def __init__(
        self,
        resource_cpurequest: str = None,
        resource_memory_request: str = None,
    ):
        # The minimum number of CPU cores.
        self.resource_cpurequest = resource_cpurequest
        # The minimum size of the memory.
        self.resource_memory_request = resource_memory_request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpurequest is not None:
            result['ResourceCPURequest'] = self.resource_cpurequest
        if self.resource_memory_request is not None:
            result['ResourceMemoryRequest'] = self.resource_memory_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPURequest') is not None:
            self.resource_cpurequest = m.get('ResourceCPURequest')
        if m.get('ResourceMemoryRequest') is not None:
            self.resource_memory_request = m.get('ResourceMemoryRequest')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceLimit(TeaModel):
    def __init__(
        self,
        resource_cpulimit: str = None,
        resource_memory_limit: str = None,
    ):
        # The maximum number of CPU cores.
        self.resource_cpulimit = resource_cpulimit
        # The maximum size of the memory.
        self.resource_memory_limit = resource_memory_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpulimit is not None:
            result['ResourceCPULimit'] = self.resource_cpulimit
        if self.resource_memory_limit is not None:
            result['ResourceMemoryLimit'] = self.resource_memory_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPULimit') is not None:
            self.resource_cpulimit = m.get('ResourceCPULimit')
        if m.get('ResourceMemoryLimit') is not None:
            self.resource_memory_limit = m.get('ResourceMemoryLimit')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceRequest(TeaModel):
    def __init__(
        self,
        resource_cpurequest: str = None,
        resource_memory_request: str = None,
    ):
        # The minimum number of CPU cores.
        self.resource_cpurequest = resource_cpurequest
        # The minimum size of the memory.
        self.resource_memory_request = resource_memory_request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpurequest is not None:
            result['ResourceCPURequest'] = self.resource_cpurequest
        if self.resource_memory_request is not None:
            result['ResourceMemoryRequest'] = self.resource_memory_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPURequest') is not None:
            self.resource_cpurequest = m.get('ResourceCPURequest')
        if m.get('ResourceMemoryRequest') is not None:
            self.resource_memory_request = m.get('ResourceMemoryRequest')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesTracing(TeaModel):
    def __init__(
        self,
        custom_tags: Dict[str, Any] = None,
        max_path_tag_length: int = None,
        sampling: float = None,
    ):
        # The custom tags added to reported spans. The key of a tag is of the string type. The value of a tag is in the JSON format. A custom tag can belong to one of the following types:
        # 
        # *   `literal`: The tag value is a fixed value in the JSON format. This tag must contain the `value` field that specifies a literal. Example: `{"value":"test"}`.
        # *   `header`: The tag value is a request header in the JSON format. This tag must contain the `name` field and the `defaultValue` field. The name field indicates the name of the request header. The defaultValue field indicates the default value that is used when no request header is available. Example: `{"name":"test","defaultValue":"test"}`.
        # *   `environment`: The tag value is an environment variable in the JSON format. This tag must contain the `name` field and the `defaultValue` field. The name field indicates the name of the environment variable. The defaultValue field indicates the environment variable that is used when no environment variable is available. Example: `{"name":"test","defaultValue":"test"}`.
        self.custom_tags = custom_tags
        # The maximum tag length.
        self.max_path_tag_length = max_path_tag_length
        # The sampling rate.
        self.sampling = sampling

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_tags is not None:
            result['CustomTags'] = self.custom_tags
        if self.max_path_tag_length is not None:
            result['MaxPathTagLength'] = self.max_path_tag_length
        if self.sampling is not None:
            result['Sampling'] = self.sampling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTags') is not None:
            self.custom_tags = m.get('CustomTags')
        if m.get('MaxPathTagLength') is not None:
            self.max_path_tag_length = m.get('MaxPathTagLength')
        if m.get('Sampling') is not None:
            self.sampling = m.get('Sampling')
        return self


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatches(TeaModel):
    def __init__(
        self,
        concurrency: int = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ipranges: str = None,
        exclude_outbound_ports: str = None,
        hold_application_until_proxy_starts: bool = None,
        include_inbound_ports: str = None,
        include_outbound_ipranges: str = None,
        include_outbound_ports: str = None,
        interception_mode: str = None,
        istio_dnsproxy_enabled: bool = None,
        lifecycle_str: str = None,
        log_level: str = None,
        proxy_metadata: Dict[str, str] = None,
        proxy_stats_matcher: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesProxyStatsMatcher = None,
        sidecar_proxy_ack_slo_resource: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyAckSloResource = None,
        sidecar_proxy_init_ack_slo_resource: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitAckSloResource = None,
        sidecar_proxy_init_resource_limit: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceLimit = None,
        sidecar_proxy_init_resource_request: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceRequest = None,
        sidecar_proxy_resource_limit: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceLimit = None,
        sidecar_proxy_resource_request: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceRequest = None,
        termination_drain_duration: str = None,
        tracing: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesTracing = None,
    ):
        # The number of worker threads to run in the istio-proxy container.
        self.concurrency = concurrency
        # The inbound ports to be excluded from redirection to the sidecar proxy in the ASM instance.
        self.exclude_inbound_ports = exclude_inbound_ports
        # The outbound IP ranges in CIDR form to be excluded from redirection to the sidecar proxy in the ASM instance.
        self.exclude_outbound_ipranges = exclude_outbound_ipranges
        # The outbound ports to be excluded from redirection to the sidecar proxy in the ASM instance.
        self.exclude_outbound_ports = exclude_outbound_ports
        # Indicates whether applications can be started only after the istio-proxy container starts. Valid values:
        # 
        # *   `true`
        # *   false
        self.hold_application_until_proxy_starts = hold_application_until_proxy_starts
        # The inbound ports for which traffic is to be redirected to the sidecar proxy in the ASM instance.
        self.include_inbound_ports = include_inbound_ports
        # The outbound IP ranges in CIDR form for which traffic is to be redirected to the sidecar proxy in the ASM instance.
        self.include_outbound_ipranges = include_outbound_ipranges
        # The outbound ports for which traffic is to be redirected to the sidecar proxy in the ASM instance.
        self.include_outbound_ports = include_outbound_ports
        # The mode in which the sidecar proxy intercepts inbound traffic. Valid values:
        # 
        # *   `REDIRECT` (default): In this mode, source IP addresses are lost during traffic redirection to the sidecar proxy.
        # *   `TPROXY`: In this mode, both the source and destination IP addresses and ports are preserved.
        self.interception_mode = interception_mode
        # Indicates whether the Domain Name System (DNS) proxy feature is enabled. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.istio_dnsproxy_enabled = istio_dnsproxy_enabled
        # The JSON string that describes the lifecycle of the sidecar proxy.
        self.lifecycle_str = lifecycle_str
        # The log level. Valid values: `info`, `debug`, `trace`, and `error`.
        self.log_level = log_level
        self.proxy_metadata = proxy_metadata
        # The custom Envoy statistics that are reported by the sidecar proxy.
        self.proxy_stats_matcher = proxy_stats_matcher
        self.sidecar_proxy_ack_slo_resource = sidecar_proxy_ack_slo_resource
        self.sidecar_proxy_init_ack_slo_resource = sidecar_proxy_init_ack_slo_resource
        # The maximum size of resources that are available to the istio-init container in the pod into which the sidecar proxy is injected. The istio-init container is used in this topic.
        self.sidecar_proxy_init_resource_limit = sidecar_proxy_init_resource_limit
        # The minimum size of resources that are required by the istio-init container.
        self.sidecar_proxy_init_resource_request = sidecar_proxy_init_resource_request
        # The maximum size of resources that are available to the sidecar proxy container.
        self.sidecar_proxy_resource_limit = sidecar_proxy_resource_limit
        # The minimum size of resources that are required by the sidecar proxy container.
        self.sidecar_proxy_resource_request = sidecar_proxy_resource_request
        # The maximum period of time allowed for connections to complete on sidecar proxy shutdown.
        self.termination_drain_duration = termination_drain_duration
        # The custom configurations of Tracing Analysis.
        self.tracing = tracing

    def validate(self):
        if self.proxy_stats_matcher:
            self.proxy_stats_matcher.validate()
        if self.sidecar_proxy_ack_slo_resource:
            self.sidecar_proxy_ack_slo_resource.validate()
        if self.sidecar_proxy_init_ack_slo_resource:
            self.sidecar_proxy_init_ack_slo_resource.validate()
        if self.sidecar_proxy_init_resource_limit:
            self.sidecar_proxy_init_resource_limit.validate()
        if self.sidecar_proxy_init_resource_request:
            self.sidecar_proxy_init_resource_request.validate()
        if self.sidecar_proxy_resource_limit:
            self.sidecar_proxy_resource_limit.validate()
        if self.sidecar_proxy_resource_request:
            self.sidecar_proxy_resource_request.validate()
        if self.tracing:
            self.tracing.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ipranges is not None:
            result['ExcludeOutboundIPRanges'] = self.exclude_outbound_ipranges
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.hold_application_until_proxy_starts is not None:
            result['HoldApplicationUntilProxyStarts'] = self.hold_application_until_proxy_starts
        if self.include_inbound_ports is not None:
            result['IncludeInboundPorts'] = self.include_inbound_ports
        if self.include_outbound_ipranges is not None:
            result['IncludeOutboundIPRanges'] = self.include_outbound_ipranges
        if self.include_outbound_ports is not None:
            result['IncludeOutboundPorts'] = self.include_outbound_ports
        if self.interception_mode is not None:
            result['InterceptionMode'] = self.interception_mode
        if self.istio_dnsproxy_enabled is not None:
            result['IstioDNSProxyEnabled'] = self.istio_dnsproxy_enabled
        if self.lifecycle_str is not None:
            result['LifecycleStr'] = self.lifecycle_str
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.proxy_metadata is not None:
            result['ProxyMetadata'] = self.proxy_metadata
        if self.proxy_stats_matcher is not None:
            result['ProxyStatsMatcher'] = self.proxy_stats_matcher.to_map()
        if self.sidecar_proxy_ack_slo_resource is not None:
            result['SidecarProxyAckSloResource'] = self.sidecar_proxy_ack_slo_resource.to_map()
        if self.sidecar_proxy_init_ack_slo_resource is not None:
            result['SidecarProxyInitAckSloResource'] = self.sidecar_proxy_init_ack_slo_resource.to_map()
        if self.sidecar_proxy_init_resource_limit is not None:
            result['SidecarProxyInitResourceLimit'] = self.sidecar_proxy_init_resource_limit.to_map()
        if self.sidecar_proxy_init_resource_request is not None:
            result['SidecarProxyInitResourceRequest'] = self.sidecar_proxy_init_resource_request.to_map()
        if self.sidecar_proxy_resource_limit is not None:
            result['SidecarProxyResourceLimit'] = self.sidecar_proxy_resource_limit.to_map()
        if self.sidecar_proxy_resource_request is not None:
            result['SidecarProxyResourceRequest'] = self.sidecar_proxy_resource_request.to_map()
        if self.termination_drain_duration is not None:
            result['TerminationDrainDuration'] = self.termination_drain_duration
        if self.tracing is not None:
            result['Tracing'] = self.tracing.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundIPRanges') is not None:
            self.exclude_outbound_ipranges = m.get('ExcludeOutboundIPRanges')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('HoldApplicationUntilProxyStarts') is not None:
            self.hold_application_until_proxy_starts = m.get('HoldApplicationUntilProxyStarts')
        if m.get('IncludeInboundPorts') is not None:
            self.include_inbound_ports = m.get('IncludeInboundPorts')
        if m.get('IncludeOutboundIPRanges') is not None:
            self.include_outbound_ipranges = m.get('IncludeOutboundIPRanges')
        if m.get('IncludeOutboundPorts') is not None:
            self.include_outbound_ports = m.get('IncludeOutboundPorts')
        if m.get('InterceptionMode') is not None:
            self.interception_mode = m.get('InterceptionMode')
        if m.get('IstioDNSProxyEnabled') is not None:
            self.istio_dnsproxy_enabled = m.get('IstioDNSProxyEnabled')
        if m.get('LifecycleStr') is not None:
            self.lifecycle_str = m.get('LifecycleStr')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('ProxyMetadata') is not None:
            self.proxy_metadata = m.get('ProxyMetadata')
        if m.get('ProxyStatsMatcher') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesProxyStatsMatcher()
            self.proxy_stats_matcher = temp_model.from_map(m['ProxyStatsMatcher'])
        if m.get('SidecarProxyAckSloResource') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyAckSloResource()
            self.sidecar_proxy_ack_slo_resource = temp_model.from_map(m['SidecarProxyAckSloResource'])
        if m.get('SidecarProxyInitAckSloResource') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitAckSloResource()
            self.sidecar_proxy_init_ack_slo_resource = temp_model.from_map(m['SidecarProxyInitAckSloResource'])
        if m.get('SidecarProxyInitResourceLimit') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceLimit()
            self.sidecar_proxy_init_resource_limit = temp_model.from_map(m['SidecarProxyInitResourceLimit'])
        if m.get('SidecarProxyInitResourceRequest') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceRequest()
            self.sidecar_proxy_init_resource_request = temp_model.from_map(m['SidecarProxyInitResourceRequest'])
        if m.get('SidecarProxyResourceLimit') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceLimit()
            self.sidecar_proxy_resource_limit = temp_model.from_map(m['SidecarProxyResourceLimit'])
        if m.get('SidecarProxyResourceRequest') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceRequest()
            self.sidecar_proxy_resource_request = temp_model.from_map(m['SidecarProxyResourceRequest'])
        if m.get('TerminationDrainDuration') is not None:
            self.termination_drain_duration = m.get('TerminationDrainDuration')
        if m.get('Tracing') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesTracing()
            self.tracing = temp_model.from_map(m['Tracing'])
        return self


class DescribeNamespaceScopeSidecarConfigResponseBody(TeaModel):
    def __init__(
        self,
        config_patches: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatches = None,
        request_id: str = None,
    ):
        # The namespace-level sidecar proxy configurations.
        self.config_patches = config_patches
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.config_patches:
            self.config_patches.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_patches is not None:
            result['ConfigPatches'] = self.config_patches.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigPatches') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatches()
            self.config_patches = temp_model.from_map(m['ConfigPatches'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNamespaceScopeSidecarConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNamespaceScopeSidecarConfigResponseBody = None,
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
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodesInstanceTypeRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the Alibaba Cloud Service Mesh (ASM) instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeNodesInstanceTypeResponseBodyInstanceTypes(TeaModel):
    def __init__(
        self,
        key: str = None,
        multi_buffer_enabled: bool = None,
        node_type: str = None,
        value: str = None,
    ):
        self.key = key
        # Indicates whether the instance type supports Multi-Buffer acceleration. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.multi_buffer_enabled = multi_buffer_enabled
        # The instance type of the node.
        self.node_type = node_type
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
        if self.multi_buffer_enabled is not None:
            result['MultiBufferEnabled'] = self.multi_buffer_enabled
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MultiBufferEnabled') is not None:
            self.multi_buffer_enabled = m.get('MultiBufferEnabled')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeNodesInstanceTypeResponseBody(TeaModel):
    def __init__(
        self,
        instance_types: List[DescribeNodesInstanceTypeResponseBodyInstanceTypes] = None,
        request_id: str = None,
    ):
        # The instance types of the nodes.
        self.instance_types = instance_types
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_types:
            for k in self.instance_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceTypes'] = []
        if self.instance_types is not None:
            for k in self.instance_types:
                result['InstanceTypes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_types = []
        if m.get('InstanceTypes') is not None:
            for k in m.get('InstanceTypes'):
                temp_model = DescribeNodesInstanceTypeResponseBodyInstanceTypes()
                self.instance_types.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNodesInstanceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNodesInstanceTypeResponseBody = None,
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
            temp_model = DescribeNodesInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeReusableSlbRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
        network_type: str = None,
    ):
        # The ID of the Kubernetes cluster on the data plane.
        self.k_8s_cluster_id = k_8s_cluster_id
        # The network type of the SLB instance. Valid values:
        # 
        # *   `intranet`
        # *   `internet`
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        return self


class DescribeReusableSlbResponseBodyReusableSlbList(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
    ):
        # The ID of the SLB instance.
        self.load_balancer_id = load_balancer_id
        # The name of the SLB instance.
        self.load_balancer_name = load_balancer_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        return self


class DescribeReusableSlbResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        reusable_slb_list: List[DescribeReusableSlbResponseBodyReusableSlbList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The list of SLB instances that can be reused.
        self.reusable_slb_list = reusable_slb_list

    def validate(self):
        if self.reusable_slb_list:
            for k in self.reusable_slb_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ReusableSlbList'] = []
        if self.reusable_slb_list is not None:
            for k in self.reusable_slb_list:
                result['ReusableSlbList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.reusable_slb_list = []
        if m.get('ReusableSlbList') is not None:
            for k in m.get('ReusableSlbList'):
                temp_model = DescribeReusableSlbResponseBodyReusableSlbList()
                self.reusable_slb_list.append(temp_model.from_map(k))
        return self


class DescribeReusableSlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeReusableSlbResponseBody = None,
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
            temp_model = DescribeReusableSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshAdditionalStatusRequest(TeaModel):
    def __init__(
        self,
        check_mode: str = None,
        service_mesh_id: str = None,
    ):
        # The check mode of the ASM instance. Valid values:
        # 
        # *   `normal`: checks the Server Load Balancer (SLB) instances created for exposing the API server and Istio Pilot, audit logs, and installation of Logtail for clusters on the data plane.
        # *   `full`: checks control plane logs, access logs, security groups, and the elastic IP addresses (EIPs) of the API server in addition to the check items in normal mode.
        self.check_mode = check_mode
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_mode is not None:
            result['CheckMode'] = self.check_mode
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckMode') is not None:
            self.check_mode = m.get('CheckMode')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusApiServerLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        locked: bool = None,
        pay_type: str = None,
        reused: bool = None,
        slbback_end_server_num_status: str = None,
        slbexist_status: str = None,
    ):
        # Indicates whether the SLB instance is locked. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.locked = locked
        # The billing method of the SLB instance. Valid values:
        # 
        # *   `PrePay`: subscription
        # *   `PayOnDemand`: pay-as-you-go
        self.pay_type = pay_type
        # Indicates whether the SLB instance is reused. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.reused = reused
        # The check result of the number of the backend servers of the SLB instance created for exposing Istio Pilot. Valid values:
        # 
        # *   `too_much`: An excessive number of backend servers are created.
        # *   `num_exact`: A proper number of backend servers are created.
        # *   `too_little`: The number of backend servers falls short.
        self.slbback_end_server_num_status = slbback_end_server_num_status
        # The check result of the SLB instance. Valid values:
        # 
        # *   `exist`: The SLB instance exists.
        # *   `not_exist`: The SLB instance does not exist.
        # *   `conflict`: Conflicts are detected.
        # *   `failed`: The check fails.
        # *   `time_out`: The check times out.
        self.slbexist_status = slbexist_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.reused is not None:
            result['Reused'] = self.reused
        if self.slbback_end_server_num_status is not None:
            result['SLBBackEndServerNumStatus'] = self.slbback_end_server_num_status
        if self.slbexist_status is not None:
            result['SLBExistStatus'] = self.slbexist_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Reused') is not None:
            self.reused = m.get('Reused')
        if m.get('SLBBackEndServerNumStatus') is not None:
            self.slbback_end_server_num_status = m.get('SLBBackEndServerNumStatus')
        if m.get('SLBExistStatus') is not None:
            self.slbexist_status = m.get('SLBExistStatus')
        return self


class DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusCanaryPilotLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        locked: bool = None,
        pay_type: str = None,
        reused: bool = None,
        slbback_end_server_num_status: str = None,
        slbexist_status: str = None,
    ):
        self.locked = locked
        self.pay_type = pay_type
        self.reused = reused
        self.slbback_end_server_num_status = slbback_end_server_num_status
        self.slbexist_status = slbexist_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.reused is not None:
            result['Reused'] = self.reused
        if self.slbback_end_server_num_status is not None:
            result['SLBBackEndServerNumStatus'] = self.slbback_end_server_num_status
        if self.slbexist_status is not None:
            result['SLBExistStatus'] = self.slbexist_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Reused') is not None:
            self.reused = m.get('Reused')
        if m.get('SLBBackEndServerNumStatus') is not None:
            self.slbback_end_server_num_status = m.get('SLBBackEndServerNumStatus')
        if m.get('SLBExistStatus') is not None:
            self.slbexist_status = m.get('SLBExistStatus')
        return self


class DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusPilotLoadBalancerStatus(TeaModel):
    def __init__(
        self,
        locked: bool = None,
        pay_type: str = None,
        reused: bool = None,
        slbback_end_server_num_status: str = None,
        slbexist_status: str = None,
    ):
        # Indicates whether the SLB instance is locked. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.locked = locked
        # The billing method of the SLB instance. Valid values:
        # 
        # *   `PrePay`: subscription
        # *   `PayOnDemand`: pay-as-you-go
        self.pay_type = pay_type
        # Indicates whether the SLB instance is reused. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.reused = reused
        # The check result of the number of the backend servers of the SLB instance created for exposing Istio Pilot. Valid values:
        # 
        # *   `too_much`: An excessive number of backend servers are created.
        # *   `num_exact`: A proper number of backend servers are created.
        # *   `too_little`: The number of backend servers falls short.
        self.slbback_end_server_num_status = slbback_end_server_num_status
        # The check result of the SLB instance. Valid values:
        # 
        # *   `exist`: The SLB instance exists.
        # *   `not_exist`: The SLB instance does not exist.
        # *   `conflict`: Conflicts are detected.
        # *   `failed`: The check fails.
        # *   `time_out`: The check times out.
        self.slbexist_status = slbexist_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locked is not None:
            result['Locked'] = self.locked
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.reused is not None:
            result['Reused'] = self.reused
        if self.slbback_end_server_num_status is not None:
            result['SLBBackEndServerNumStatus'] = self.slbback_end_server_num_status
        if self.slbexist_status is not None:
            result['SLBExistStatus'] = self.slbexist_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Reused') is not None:
            self.reused = m.get('Reused')
        if m.get('SLBBackEndServerNumStatus') is not None:
            self.slbback_end_server_num_status = m.get('SLBBackEndServerNumStatus')
        if m.get('SLBExistStatus') is not None:
            self.slbexist_status = m.get('SLBExistStatus')
        return self


class DescribeServiceMeshAdditionalStatusResponseBodyClusterStatus(TeaModel):
    def __init__(
        self,
        access_log_project_status: str = None,
        api_server_eipstatus: str = None,
        api_server_load_balancer_status: DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusApiServerLoadBalancerStatus = None,
        audit_project_status: str = None,
        canary_pilot_load_balancer_status: DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusCanaryPilotLoadBalancerStatus = None,
        control_plane_project_status: str = None,
        logtail_status_record: Dict[str, Any] = None,
        pilot_load_balancer_status: DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusPilotLoadBalancerStatus = None,
        ramapplication_status: str = None,
        sg_status: str = None,
    ):
        # Indicates whether access logs exist. Valid values:
        # 
        # *   `exist`: Access logs exist.
        # *   `not_exist`: Access logs do not exist.
        # *   `failed`: The check fails.
        # *   `time_out`: The check times out.
        self.access_log_project_status = access_log_project_status
        # The check result of the EIP associated with the API server. Valid values:
        # 
        # *   `exist`: The EIP exists.
        # *   `not_exist`: The EIP does not exist.
        # *   `failed`: The check fails.
        # *   `time_out`: The check times out.
        # *   `not_in_use`: The EIP is not associated with the API Server.
        # *   `locked`: The EIP is locked.
        self.api_server_eipstatus = api_server_eipstatus
        # The check results of the SLB instance created for exposing the API server.
        self.api_server_load_balancer_status = api_server_load_balancer_status
        # Indicates whether audit logs exist. Valid values:
        # 
        # *   `exist`
        # *   `not exist`
        self.audit_project_status = audit_project_status
        self.canary_pilot_load_balancer_status = canary_pilot_load_balancer_status
        # Indicates whether control plane logs exist. Valid values:
        # 
        # *   `exist`: Control plane logs exist.
        # *   `not_exist`: Control plane logs do not exist.
        # *   `failed`: The check fails.
        # *   `time_out`: The check times out.
        self.control_plane_project_status = control_plane_project_status
        # Indicates whether Logtail is installed in clusters on the data plane.
        self.logtail_status_record = logtail_status_record
        # The check results of the SLB instance created for exposing Istio Pilot.
        self.pilot_load_balancer_status = pilot_load_balancer_status
        self.ramapplication_status = ramapplication_status
        # Indicates whether the security group is reused. Valid values:
        # 
        # *   `reused`: The security group is reused.
        # *   `not_reused`: The security group is not reused.
        # *   `failed`: The check fails.
        # *   `time_out`: The check times out.
        self.sg_status = sg_status

    def validate(self):
        if self.api_server_load_balancer_status:
            self.api_server_load_balancer_status.validate()
        if self.canary_pilot_load_balancer_status:
            self.canary_pilot_load_balancer_status.validate()
        if self.pilot_load_balancer_status:
            self.pilot_load_balancer_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_project_status is not None:
            result['AccessLogProjectStatus'] = self.access_log_project_status
        if self.api_server_eipstatus is not None:
            result['ApiServerEIPStatus'] = self.api_server_eipstatus
        if self.api_server_load_balancer_status is not None:
            result['ApiServerLoadBalancerStatus'] = self.api_server_load_balancer_status.to_map()
        if self.audit_project_status is not None:
            result['AuditProjectStatus'] = self.audit_project_status
        if self.canary_pilot_load_balancer_status is not None:
            result['CanaryPilotLoadBalancerStatus'] = self.canary_pilot_load_balancer_status.to_map()
        if self.control_plane_project_status is not None:
            result['ControlPlaneProjectStatus'] = self.control_plane_project_status
        if self.logtail_status_record is not None:
            result['LogtailStatusRecord'] = self.logtail_status_record
        if self.pilot_load_balancer_status is not None:
            result['PilotLoadBalancerStatus'] = self.pilot_load_balancer_status.to_map()
        if self.ramapplication_status is not None:
            result['RAMApplicationStatus'] = self.ramapplication_status
        if self.sg_status is not None:
            result['SgStatus'] = self.sg_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogProjectStatus') is not None:
            self.access_log_project_status = m.get('AccessLogProjectStatus')
        if m.get('ApiServerEIPStatus') is not None:
            self.api_server_eipstatus = m.get('ApiServerEIPStatus')
        if m.get('ApiServerLoadBalancerStatus') is not None:
            temp_model = DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusApiServerLoadBalancerStatus()
            self.api_server_load_balancer_status = temp_model.from_map(m['ApiServerLoadBalancerStatus'])
        if m.get('AuditProjectStatus') is not None:
            self.audit_project_status = m.get('AuditProjectStatus')
        if m.get('CanaryPilotLoadBalancerStatus') is not None:
            temp_model = DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusCanaryPilotLoadBalancerStatus()
            self.canary_pilot_load_balancer_status = temp_model.from_map(m['CanaryPilotLoadBalancerStatus'])
        if m.get('ControlPlaneProjectStatus') is not None:
            self.control_plane_project_status = m.get('ControlPlaneProjectStatus')
        if m.get('LogtailStatusRecord') is not None:
            self.logtail_status_record = m.get('LogtailStatusRecord')
        if m.get('PilotLoadBalancerStatus') is not None:
            temp_model = DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusPilotLoadBalancerStatus()
            self.pilot_load_balancer_status = temp_model.from_map(m['PilotLoadBalancerStatus'])
        if m.get('RAMApplicationStatus') is not None:
            self.ramapplication_status = m.get('RAMApplicationStatus')
        if m.get('SgStatus') is not None:
            self.sg_status = m.get('SgStatus')
        return self


class DescribeServiceMeshAdditionalStatusResponseBody(TeaModel):
    def __init__(
        self,
        cluster_status: DescribeServiceMeshAdditionalStatusResponseBodyClusterStatus = None,
        request_id: str = None,
    ):
        # The status of the cluster.
        self.cluster_status = cluster_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cluster_status:
            self.cluster_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterStatus') is not None:
            temp_model = DescribeServiceMeshAdditionalStatusResponseBodyClusterStatus()
            self.cluster_status = temp_model.from_map(m['ClusterStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceMeshAdditionalStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceMeshAdditionalStatusResponseBody = None,
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
            temp_model = DescribeServiceMeshAdditionalStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshClustersRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        offset: int = None,
        service_mesh_id: str = None,
    ):
        # The maximum number of clusters in a cluster list.
        self.limit = limit
        # The position where the query starts.
        self.offset = offset
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_domain: str = None,
        cluster_id: str = None,
        cluster_type: str = None,
        creation_time: str = None,
        error_message: str = None,
        forbidden_flag: int = None,
        forbidden_info: str = None,
        name: str = None,
        region_id: str = None,
        service_mesh_id: str = None,
        sg_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
        vpc_id: str = None,
    ):
        # The domain name of the cluster.
        self.cluster_domain = cluster_domain
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster type.
        self.cluster_type = cluster_type
        # The time when the cluster was created.
        self.creation_time = creation_time
        # The error message about the cluster.
        self.error_message = error_message
        # Indicates that the cluster is available or the reason why the cluster cannot be added to the ASM instance. Valid values:
        # 
        # *   `0`: The cluster can be added to the ASM instance.
        # *   `1`: The cluster cannot be added to the ASM instance because you do not have administrator permissions on the cluster.
        # *   `2`: The cluster cannot be added to the ASM instance because the cluster and the ASM instance reside in different VPCs between which no private connections are built.
        # *   `3`: The CIDR block of the cluster conflicts with that of the ASM instance.
        # *   `4`: The cluster has a namespace that is named istio system.
        self.forbidden_flag = forbidden_flag
        self.forbidden_info = forbidden_info
        # The name of the cluster.
        self.name = name
        # The ID of the region in which the cluster resides.
        self.region_id = region_id
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The ID of the security group.
        self.sg_id = sg_id
        # The state of the cluster. Valid values:
        # 
        # *   `running`: The cluster is running.
        # *   `starting`: The cluster is starting.
        # *   `stopping`: The cluster is being stopped.
        # *   `stopped`: The cluster is stopped.
        # *   `failed`: The cluster fails to be run.
        self.state = state
        # The time when the cluster was last modified.
        self.update_time = update_time
        # The version number of the cluster.
        self.version = version
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.forbidden_flag is not None:
            result['ForbiddenFlag'] = self.forbidden_flag
        if self.forbidden_info is not None:
            result['ForbiddenInfo'] = self.forbidden_info
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ForbiddenFlag') is not None:
            self.forbidden_flag = m.get('ForbiddenFlag')
        if m.get('ForbiddenInfo') is not None:
            self.forbidden_info = m.get('ForbiddenInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeServiceMeshClustersResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[DescribeServiceMeshClustersResponseBodyClusters] = None,
        number_of_clusters: int = None,
        request_id: str = None,
    ):
        # The queried clusters.
        self.clusters = clusters
        self.number_of_clusters = number_of_clusters
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.number_of_clusters is not None:
            result['NumberOfClusters'] = self.number_of_clusters
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeServiceMeshClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('NumberOfClusters') is not None:
            self.number_of_clusters = m.get('NumberOfClusters')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceMeshClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceMeshClustersResponseBody = None,
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
            temp_model = DescribeServiceMeshClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshDetailRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints(TeaModel):
    def __init__(
        self,
        intranet_api_server_endpoint: str = None,
        intranet_pilot_endpoint: str = None,
        public_api_server_endpoint: str = None,
        public_pilot_endpoint: str = None,
    ):
        # The endpoint that is used to access the API server from the internal network.
        self.intranet_api_server_endpoint = intranet_api_server_endpoint
        # The endpoint that is used to access Istio Pilot from the internal network.
        self.intranet_pilot_endpoint = intranet_pilot_endpoint
        # The endpoint that is used to expose the API server to the Internet.
        self.public_api_server_endpoint = public_api_server_endpoint
        # The endpoint that is used to expose Istio Pilot to the Internet.
        self.public_pilot_endpoint = public_pilot_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.intranet_pilot_endpoint is not None:
            result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        if self.public_pilot_endpoint is not None:
            result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('IntranetPilotEndpoint') is not None:
            self.intranet_pilot_endpoint = m.get('IntranetPilotEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        if m.get('PublicPilotEndpoint') is not None:
            self.public_pilot_endpoint = m.get('PublicPilotEndpoint')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        error_message: str = None,
        name: str = None,
        profile: str = None,
        region_id: str = None,
        service_mesh_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
    ):
        # The time when the ASM instance was created.
        self.creation_time = creation_time
        # The error message that is returned when the call failed.
        self.error_message = error_message
        # The name of the ASM instance.
        self.name = name
        # The edition of the ASM instance. Valid values:
        # 
        # *   `Default`: Standard Edition
        # *   `Pro`: Professional Edition
        self.profile = profile
        # The ID of the region in which the ASM instance resides.
        self.region_id = region_id
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The status of the ASM instance.
        self.state = state
        # The time when the ASM instance was last modified.
        self.update_time = update_time
        # The version of the ASM instance.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer(TeaModel):
    def __init__(
        self,
        api_server_loadbalancer_id: str = None,
        api_server_public_eip: bool = None,
        pilot_public_eip: bool = None,
        pilot_public_loadbalancer_id: str = None,
    ):
        # The ID of the SLB instance that is used when the API server is exposed to the Internet.
        self.api_server_loadbalancer_id = api_server_loadbalancer_id
        # Indicates whether the API server is exposed to the Internet. Valid values:
        # 
        # *   `true`: The API server is exposed to the Internet.
        # *   `false`: The API server is not exposed to the Internet.
        self.api_server_public_eip = api_server_public_eip
        # Indicates whether Istio Pilot is exposed to the Internet. Valid values:
        # 
        # *   `true`: Istio Pilot is exposed to the Internet.
        # *   `false`: Istio Pilot is not exposed to the Internet.
        self.pilot_public_eip = pilot_public_eip
        # The ID of the Server Load Balancer (SLB) instance that is used when Istio Pilot is exposed to the Internet.
        self.pilot_public_loadbalancer_id = pilot_public_loadbalancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_loadbalancer_id is not None:
            result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.pilot_public_loadbalancer_id is not None:
            result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiServerLoadbalancerId') is not None:
            self.api_server_loadbalancer_id = m.get('ApiServerLoadbalancerId')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('PilotPublicEip') is not None:
            self.pilot_public_eip = m.get('PilotPublicEip')
        if m.get('PilotPublicLoadbalancerId') is not None:
            self.pilot_public_loadbalancer_id = m.get('PilotPublicLoadbalancerId')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        project: str = None,
    ):
        # Indicates whether access log collection is enabled. Valid values:
        # 
        # *   `true`: Access log collection is enabled.
        # *   `false`: Access log collection is disabled.
        self.enabled = enabled
        # The name of the Log Service project that stores access logs.
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit(TeaModel):
    def __init__(
        self,
        audit_project_status: str = None,
        enabled: bool = None,
        project: str = None,
    ):
        # Indicates whether an audit project exists in the ASM instance. Valid values:
        # 
        # *   `audit_project_exist`: An audit project exists.
        # *   `audit_project_not_exist`: No audit project exists.
        self.audit_project_status = audit_project_status
        # Indicates whether mesh audit is enabled. Valid values:
        # 
        # *   `true`: Mesh audit is enabled.
        # *   `false`: Mesh audit is disabled.
        self.enabled = enabled
        # The name of the Log Service project that is used for mesh audit.
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_project_status is not None:
            result['AuditProjectStatus'] = self.audit_project_status
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditProjectStatus') is not None:
            self.audit_project_status = m.get('AuditProjectStatus')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigControlPlaneLogInfo(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        project: str = None,
    ):
        # Indicates whether the collection of control-plane logs is enabled. Valid values:
        # 
        # *   `true`: The collection of control-plane logs is enabled.
        # *   `false`: The collection of control-plane logs is disabled.
        self.enabled = enabled
        # The name of the Log Service project that stores control-plane logs.
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigEdition(TeaModel):
    def __init__(
        self,
        istiod_image_tag: str = None,
        name: str = None,
        proxy_image_tag: str = None,
    ):
        # The version of the Istiod image.
        self.istiod_image_tag = istiod_image_tag
        # The name of the edition.
        self.name = name
        # The version of the Istio Proxy image.
        self.proxy_image_tag = proxy_image_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istiod_image_tag is not None:
            result['IstiodImageTag'] = self.istiod_image_tag
        if self.name is not None:
            result['Name'] = self.name
        if self.proxy_image_tag is not None:
            result['ProxyImageTag'] = self.proxy_image_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstiodImageTag') is not None:
            self.istiod_image_tag = m.get('IstiodImageTag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProxyImageTag') is not None:
            self.proxy_image_tag = m.get('ProxyImageTag')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAccessLogExtraConf(TeaModel):
    def __init__(
        self,
        gateway_lifecycle: int = None,
        sidecar_lifecycle: int = None,
    ):
        # The retention period for the access logs of the ingress gateway. Unit: day. The logs are collected by using the Log Service. For example, a value of 30 indicates that the logs are retained for 30 days.
        self.gateway_lifecycle = gateway_lifecycle
        # The retention period for the access logs of sidecar proxies. Unit: day. The logs are collected by using the Log Service. For example, a value of 30 indicates that the logs are retained for 30 days.
        self.sidecar_lifecycle = sidecar_lifecycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_lifecycle is not None:
            result['GatewayLifecycle'] = self.gateway_lifecycle
        if self.sidecar_lifecycle is not None:
            result['SidecarLifecycle'] = self.sidecar_lifecycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayLifecycle') is not None:
            self.gateway_lifecycle = m.get('GatewayLifecycle')
        if m.get('SidecarLifecycle') is not None:
            self.sidecar_lifecycle = m.get('SidecarLifecycle')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfigurationEgressHpaCpu(TeaModel):
    def __init__(
        self,
        target_average_utilization: int = None,
    ):
        # The expected CPU utilization when HPA is enabled. Valid values: 1 to 100. If the CPU utilization exceeds this value, the number of pod replicas increases. If the CPU utilization is less than this value, the number of pod replicas decreases.
        self.target_average_utilization = target_average_utilization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_average_utilization is not None:
            result['TargetAverageUtilization'] = self.target_average_utilization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetAverageUtilization') is not None:
            self.target_average_utilization = m.get('TargetAverageUtilization')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfigurationEgressHpaMemory(TeaModel):
    def __init__(
        self,
        target_average_utilization: int = None,
    ):
        # The expected memory usage when HPA is enabled. Valid values: 1 to 100. If the memory usage exceeds this value, the number of pod replicas increases. If the memory usage is less than this value, the number of pod replicas decreases.
        self.target_average_utilization = target_average_utilization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_average_utilization is not None:
            result['TargetAverageUtilization'] = self.target_average_utilization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetAverageUtilization') is not None:
            self.target_average_utilization = m.get('TargetAverageUtilization')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfigurationEgressResources(TeaModel):
    def __init__(
        self,
        limits: Dict[str, Any] = None,
        requests: Dict[str, Any] = None,
    ):
        # The resources that are available to the egress gateway.
        self.limits = limits
        # The resources that are requested by the egress gateway.
        self.requests = requests

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limits is not None:
            result['Limits'] = self.limits
        if self.requests is not None:
            result['Requests'] = self.requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limits') is not None:
            self.limits = m.get('Limits')
        if m.get('Requests') is not None:
            self.requests = m.get('Requests')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfiguration(TeaModel):
    def __init__(
        self,
        egress_autoscale_enabled: bool = None,
        egress_hpa_cpu: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfigurationEgressHpaCpu = None,
        egress_hpa_memory: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfigurationEgressHpaMemory = None,
        egress_max_replica: int = None,
        egress_min_replica: int = None,
        egress_replica_count: int = None,
        egress_resources: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfigurationEgressResources = None,
        enabled: bool = None,
    ):
        # Indicates whether Horizontal Pod Autoscaling (HPA) is enabled for the egress gateway.
        self.egress_autoscale_enabled = egress_autoscale_enabled
        # The CPU resource configurations of the egress gateway when HPA is enabled.
        self.egress_hpa_cpu = egress_hpa_cpu
        # The memory resource configurations of the egress gateway when HPA is enabled.
        self.egress_hpa_memory = egress_hpa_memory
        # The maximum number of egress gateway pod replicas when HPA is enabled.
        self.egress_max_replica = egress_max_replica
        # The minimum number of egress gateway pod replicas when HPA is enabled.
        self.egress_min_replica = egress_min_replica
        # The number of the egress gateway pod replicas.
        self.egress_replica_count = egress_replica_count
        # The resource configurations of the egress gateway that is used by adaptive xDS optimization.
        self.egress_resources = egress_resources
        # Indicates whether adaptive xDS optimization is enabled.
        self.enabled = enabled

    def validate(self):
        if self.egress_hpa_cpu:
            self.egress_hpa_cpu.validate()
        if self.egress_hpa_memory:
            self.egress_hpa_memory.validate()
        if self.egress_resources:
            self.egress_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.egress_autoscale_enabled is not None:
            result['EgressAutoscaleEnabled'] = self.egress_autoscale_enabled
        if self.egress_hpa_cpu is not None:
            result['EgressHpaCpu'] = self.egress_hpa_cpu.to_map()
        if self.egress_hpa_memory is not None:
            result['EgressHpaMemory'] = self.egress_hpa_memory.to_map()
        if self.egress_max_replica is not None:
            result['EgressMaxReplica'] = self.egress_max_replica
        if self.egress_min_replica is not None:
            result['EgressMinReplica'] = self.egress_min_replica
        if self.egress_replica_count is not None:
            result['EgressReplicaCount'] = self.egress_replica_count
        if self.egress_resources is not None:
            result['EgressResources'] = self.egress_resources.to_map()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressAutoscaleEnabled') is not None:
            self.egress_autoscale_enabled = m.get('EgressAutoscaleEnabled')
        if m.get('EgressHpaCpu') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfigurationEgressHpaCpu()
            self.egress_hpa_cpu = temp_model.from_map(m['EgressHpaCpu'])
        if m.get('EgressHpaMemory') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfigurationEgressHpaMemory()
            self.egress_hpa_memory = temp_model.from_map(m['EgressHpaMemory'])
        if m.get('EgressMaxReplica') is not None:
            self.egress_max_replica = m.get('EgressMaxReplica')
        if m.get('EgressMinReplica') is not None:
            self.egress_min_replica = m.get('EgressMinReplica')
        if m.get('EgressReplicaCount') is not None:
            self.egress_replica_count = m.get('EgressReplicaCount')
        if m.get('EgressResources') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfigurationEgressResources()
            self.egress_resources = temp_model.from_map(m['EgressResources'])
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAutoDiagnosis(TeaModel):
    def __init__(
        self,
        auto_diagnosis_enabled: bool = None,
    ):
        # Indicates whether automatic diagnosis is enabled for the ASM instance. If you enable this feature, the ASM instance is automatically diagnosed five minutes after you modify an Istio resource.
        self.auto_diagnosis_enabled = auto_diagnosis_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_diagnosis_enabled is not None:
            result['AutoDiagnosisEnabled'] = self.auto_diagnosis_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDiagnosisEnabled') is not None:
            self.auto_diagnosis_enabled = m.get('AutoDiagnosisEnabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationCRAggregationConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Indicates whether Istio resources can be accessed by using the Kubernetes API on the data plane.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationIstioCRHistory(TeaModel):
    def __init__(
        self,
        enable_history: bool = None,
    ):
        # Indicates whether the rollback feature for Istio resources is enabled. Valid values:
        # 
        # *   `true`: The rollback feature for Istio resources is enabled.
        # *   `false`: The rollback feature for Istio resources is disabled.
        self.enable_history = enable_history

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_history is not None:
            result['EnableHistory'] = self.enable_history
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableHistory') is not None:
            self.enable_history = m.get('EnableHistory')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        # The executed command.
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHttpGetHttpHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the HTTP request header.
        self.name = name
        # The value of the HTTP request header field.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHttpGet(TeaModel):
    def __init__(
        self,
        host: str = None,
        http_headers: List[DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHttpGetHttpHeaders] = None,
        port: str = None,
        scheme: str = None,
    ):
        # The URL of the request.
        self.host = host
        # The HTTP request headers.
        self.http_headers = http_headers
        # The port number of the request.
        self.port = port
        # The request method. Valid values: `http` and `https`.
        self.scheme = scheme

    def validate(self):
        if self.http_headers:
            for k in self.http_headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        result['httpHeaders'] = []
        if self.http_headers is not None:
            for k in self.http_headers:
                result['httpHeaders'].append(k.to_map() if k else None)
        if self.port is not None:
            result['port'] = self.port
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        self.http_headers = []
        if m.get('httpHeaders') is not None:
            for k in m.get('httpHeaders'):
                temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHttpGetHttpHeaders()
                self.http_headers.append(temp_model.from_map(k))
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartTcpSocket(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        # The URL of the TCP socket request.
        self.host = host
        # The port number of the TCP socket request.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStart(TeaModel):
    def __init__(
        self,
        exec: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartExec = None,
        http_get: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHttpGet = None,
        tcp_socket: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartTcpSocket = None,
    ):
        # The post-start script.
        self.exec = exec
        # The HTTP GET request that is sent before the instance stops.
        self.http_get = http_get
        # The TCP socket request that is sent.
        self.tcp_socket = tcp_socket

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['exec'] = self.exec.to_map()
        if self.http_get is not None:
            result['httpGet'] = self.http_get.to_map()
        if self.tcp_socket is not None:
            result['tcpSocket'] = self.tcp_socket.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exec') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartExec()
            self.exec = temp_model.from_map(m['exec'])
        if m.get('httpGet') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHttpGet()
            self.http_get = temp_model.from_map(m['httpGet'])
        if m.get('tcpSocket') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartTcpSocket()
            self.tcp_socket = temp_model.from_map(m['tcpSocket'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        # The executed command.
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('command') is not None:
            self.command = m.get('command')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHttpGetHttpHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the HTTP request header.
        self.name = name
        # The value of the HTTP request header field.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHttpGet(TeaModel):
    def __init__(
        self,
        host: str = None,
        http_headers: List[DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHttpGetHttpHeaders] = None,
        port: str = None,
        scheme: str = None,
    ):
        # The URL of the request.
        self.host = host
        # The HTTP request headers.
        self.http_headers = http_headers
        # The port number of the request.
        self.port = port
        # The request method. Valid values: `http` and `https`.
        self.scheme = scheme

    def validate(self):
        if self.http_headers:
            for k in self.http_headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        result['httpHeaders'] = []
        if self.http_headers is not None:
            for k in self.http_headers:
                result['httpHeaders'].append(k.to_map() if k else None)
        if self.port is not None:
            result['port'] = self.port
        if self.scheme is not None:
            result['scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        self.http_headers = []
        if m.get('httpHeaders') is not None:
            for k in m.get('httpHeaders'):
                temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHttpGetHttpHeaders()
                self.http_headers.append(temp_model.from_map(k))
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopTcpSocket(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        # The URL of the request.
        self.host = host
        # The port number of the request.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['host'] = self.host
        if self.port is not None:
            result['port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('port') is not None:
            self.port = m.get('port')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStop(TeaModel):
    def __init__(
        self,
        exec: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopExec = None,
        http_get: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHttpGet = None,
        tcp_socket: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopTcpSocket = None,
    ):
        # The pre-close script.
        self.exec = exec
        # The HTTP GET request that is sent before the instance stops.
        self.http_get = http_get
        # The TCP socket request that is sent.
        self.tcp_socket = tcp_socket

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['exec'] = self.exec.to_map()
        if self.http_get is not None:
            result['httpGet'] = self.http_get.to_map()
        if self.tcp_socket is not None:
            result['tcpSocket'] = self.tcp_socket.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exec') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopExec()
            self.exec = temp_model.from_map(m['exec'])
        if m.get('httpGet') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHttpGet()
            self.http_get = temp_model.from_map(m['httpGet'])
        if m.get('tcpSocket') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopTcpSocket()
            self.tcp_socket = temp_model.from_map(m['tcpSocket'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecycle(TeaModel):
    def __init__(
        self,
        post_start: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStart = None,
        pre_stop: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStop = None,
    ):
        # The post-start parameters.
        self.post_start = post_start
        # The pre-close parameters.
        self.pre_stop = pre_stop

    def validate(self):
        if self.post_start:
            self.post_start.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.post_start is not None:
            result['postStart'] = self.post_start.to_map()
        if self.pre_stop is not None:
            result['preStop'] = self.pre_stop.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('postStart') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStart()
            self.post_start = temp_model.from_map(m['postStart'])
        if m.get('preStop') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStop()
            self.pre_stop = temp_model.from_map(m['preStop'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationMultiBuffer(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        poll_delay: str = None,
    ):
        # Indicates whether MulitiBuffer-based TLS acceleration is enabled. Valid values:
        # 
        # *   `true`: MulitiBuffer-based TLS acceleration is enabled.
        # *   `false`: MulitiBuffer-based TLS acceleration is disabled.
        self.enabled = enabled
        # The pull-request latency.
        self.poll_delay = poll_delay

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.poll_delay is not None:
            result['PollDelay'] = self.poll_delay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PollDelay') is not None:
            self.poll_delay = m.get('PollDelay')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationNFDConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        nfdlabel_pruned: bool = None,
    ):
        # Indicates whether NFD is enabled.
        self.enabled = enabled
        # Indicates whether feature labels on nodes are cleared when NFD is disabled.
        self.nfdlabel_pruned = nfdlabel_pruned

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.nfdlabel_pruned is not None:
            result['NFDLabelPruned'] = self.nfdlabel_pruned
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('NFDLabelPruned') is not None:
            self.nfdlabel_pruned = m.get('NFDLabelPruned')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationOPAScopeInjection(TeaModel):
    def __init__(
        self,
        opascope_injected: bool = None,
    ):
        # Indicates whether the feature of controlling the OPA injection scope is enabled. Valid values:
        # 
        # *   `true`: The feature is enabled.
        # *   `false`: The feature is disabled.
        self.opascope_injected = opascope_injected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.opascope_injected is not None:
            result['OPAScopeInjected'] = self.opascope_injected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OPAScopeInjected') is not None:
            self.opascope_injected = m.get('OPAScopeInjected')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceLimit(TeaModel):
    def __init__(
        self,
        resource_cpulimit: str = None,
        resource_memory_limit: str = None,
    ):
        # The maximum number of CPU cores that are available to the istio-init container.
        self.resource_cpulimit = resource_cpulimit
        # The maximum size of the memory that is available to the istio-init container.
        self.resource_memory_limit = resource_memory_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpulimit is not None:
            result['ResourceCPULimit'] = self.resource_cpulimit
        if self.resource_memory_limit is not None:
            result['ResourceMemoryLimit'] = self.resource_memory_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPULimit') is not None:
            self.resource_cpulimit = m.get('ResourceCPULimit')
        if m.get('ResourceMemoryLimit') is not None:
            self.resource_memory_limit = m.get('ResourceMemoryLimit')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceRequest(TeaModel):
    def __init__(
        self,
        resource_cpurequest: str = None,
        resource_memory_request: str = None,
    ):
        # The number of CPU cores that are requested by the istio-init container.
        self.resource_cpurequest = resource_cpurequest
        # The size of the memory that is requested by the istio-init container.
        self.resource_memory_request = resource_memory_request

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_cpurequest is not None:
            result['ResourceCPURequest'] = self.resource_cpurequest
        if self.resource_memory_request is not None:
            result['ResourceMemoryRequest'] = self.resource_memory_request
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCPURequest') is not None:
            self.resource_cpurequest = m.get('ResourceCPURequest')
        if m.get('ResourceMemoryRequest') is not None:
            self.resource_memory_request = m.get('ResourceMemoryRequest')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfiguration(TeaModel):
    def __init__(
        self,
        access_log_extra_conf: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAccessLogExtraConf = None,
        adaptive_xds_configuration: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfiguration = None,
        auto_diagnosis: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAutoDiagnosis = None,
        craggregation_configuration: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationCRAggregationConfiguration = None,
        craggregation_enabled: bool = None,
        discovery_selectors: List[Dict[str, Any]] = None,
        istio_crhistory: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationIstioCRHistory = None,
        lifecycle: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecycle = None,
        multi_buffer: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationMultiBuffer = None,
        nfdconfiguration: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationNFDConfiguration = None,
        opascope_injection: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationOPAScopeInjection = None,
        sidecar_proxy_init_resource_limit: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceLimit = None,
        sidecar_proxy_init_resource_request: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceRequest = None,
        termination_drain_duration: str = None,
    ):
        # The configurations of additional features for access log collection
        self.access_log_extra_conf = access_log_extra_conf
        # The configurations of adaptive xDS optimization.
        self.adaptive_xds_configuration = adaptive_xds_configuration
        # The configurations of automatic diagnosis for the ASM instance.
        self.auto_diagnosis = auto_diagnosis
        # Access to Istio resources by using the Kubernetes API on the data plane.
        self.craggregation_configuration = craggregation_configuration
        # Indicates whether the Kubernetes API of clusters on the data plane can be used to access Istio resources. Valid values:
        # 
        # *   `true`: The Kubernetes API of clusters on the data plane can be used to access Istio resources.
        # *   `false`: The Kubernetes API of clusters on the data plane cannot be used to access Istio resources.
        self.craggregation_enabled = craggregation_enabled
        # The label selectors used to specify namespaces on the data plane. The control plane discovers and process only application services in the specified namespaces.
        self.discovery_selectors = discovery_selectors
        # The configurations of the rollback feature for Istio resources.
        self.istio_crhistory = istio_crhistory
        # The lifecycle of Istio Proxy.
        self.lifecycle = lifecycle
        # The information about Transport Layer Security (TLS) acceleration based on MulitiBuffer.
        self.multi_buffer = multi_buffer
        # The configurations of Node Feature Discovery (NFD).
        self.nfdconfiguration = nfdconfiguration
        # The configurations of the feature of controlling the OPA injection scope.
        self.opascope_injection = opascope_injection
        # The resource limits on the istio-init container.
        self.sidecar_proxy_init_resource_limit = sidecar_proxy_init_resource_limit
        # The resources that are requested by the istio-init container.
        self.sidecar_proxy_init_resource_request = sidecar_proxy_init_resource_request
        # The maximum period of time that Istio Proxy waits for a request to end.
        self.termination_drain_duration = termination_drain_duration

    def validate(self):
        if self.access_log_extra_conf:
            self.access_log_extra_conf.validate()
        if self.adaptive_xds_configuration:
            self.adaptive_xds_configuration.validate()
        if self.auto_diagnosis:
            self.auto_diagnosis.validate()
        if self.craggregation_configuration:
            self.craggregation_configuration.validate()
        if self.istio_crhistory:
            self.istio_crhistory.validate()
        if self.lifecycle:
            self.lifecycle.validate()
        if self.multi_buffer:
            self.multi_buffer.validate()
        if self.nfdconfiguration:
            self.nfdconfiguration.validate()
        if self.opascope_injection:
            self.opascope_injection.validate()
        if self.sidecar_proxy_init_resource_limit:
            self.sidecar_proxy_init_resource_limit.validate()
        if self.sidecar_proxy_init_resource_request:
            self.sidecar_proxy_init_resource_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_extra_conf is not None:
            result['AccessLogExtraConf'] = self.access_log_extra_conf.to_map()
        if self.adaptive_xds_configuration is not None:
            result['AdaptiveXdsConfiguration'] = self.adaptive_xds_configuration.to_map()
        if self.auto_diagnosis is not None:
            result['AutoDiagnosis'] = self.auto_diagnosis.to_map()
        if self.craggregation_configuration is not None:
            result['CRAggregationConfiguration'] = self.craggregation_configuration.to_map()
        if self.craggregation_enabled is not None:
            result['CRAggregationEnabled'] = self.craggregation_enabled
        if self.discovery_selectors is not None:
            result['DiscoverySelectors'] = self.discovery_selectors
        if self.istio_crhistory is not None:
            result['IstioCRHistory'] = self.istio_crhistory.to_map()
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle.to_map()
        if self.multi_buffer is not None:
            result['MultiBuffer'] = self.multi_buffer.to_map()
        if self.nfdconfiguration is not None:
            result['NFDConfiguration'] = self.nfdconfiguration.to_map()
        if self.opascope_injection is not None:
            result['OPAScopeInjection'] = self.opascope_injection.to_map()
        if self.sidecar_proxy_init_resource_limit is not None:
            result['SidecarProxyInitResourceLimit'] = self.sidecar_proxy_init_resource_limit.to_map()
        if self.sidecar_proxy_init_resource_request is not None:
            result['SidecarProxyInitResourceRequest'] = self.sidecar_proxy_init_resource_request.to_map()
        if self.termination_drain_duration is not None:
            result['TerminationDrainDuration'] = self.termination_drain_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogExtraConf') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAccessLogExtraConf()
            self.access_log_extra_conf = temp_model.from_map(m['AccessLogExtraConf'])
        if m.get('AdaptiveXdsConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAdaptiveXdsConfiguration()
            self.adaptive_xds_configuration = temp_model.from_map(m['AdaptiveXdsConfiguration'])
        if m.get('AutoDiagnosis') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationAutoDiagnosis()
            self.auto_diagnosis = temp_model.from_map(m['AutoDiagnosis'])
        if m.get('CRAggregationConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationCRAggregationConfiguration()
            self.craggregation_configuration = temp_model.from_map(m['CRAggregationConfiguration'])
        if m.get('CRAggregationEnabled') is not None:
            self.craggregation_enabled = m.get('CRAggregationEnabled')
        if m.get('DiscoverySelectors') is not None:
            self.discovery_selectors = m.get('DiscoverySelectors')
        if m.get('IstioCRHistory') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationIstioCRHistory()
            self.istio_crhistory = temp_model.from_map(m['IstioCRHistory'])
        if m.get('Lifecycle') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecycle()
            self.lifecycle = temp_model.from_map(m['Lifecycle'])
        if m.get('MultiBuffer') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationMultiBuffer()
            self.multi_buffer = temp_model.from_map(m['MultiBuffer'])
        if m.get('NFDConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationNFDConfiguration()
            self.nfdconfiguration = temp_model.from_map(m['NFDConfiguration'])
        if m.get('OPAScopeInjection') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationOPAScopeInjection()
            self.opascope_injection = temp_model.from_map(m['OPAScopeInjection'])
        if m.get('SidecarProxyInitResourceLimit') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceLimit()
            self.sidecar_proxy_init_resource_limit = temp_model.from_map(m['SidecarProxyInitResourceLimit'])
        if m.get('SidecarProxyInitResourceRequest') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceRequest()
            self.sidecar_proxy_init_resource_request = temp_model.from_map(m['SidecarProxyInitResourceRequest'])
        if m.get('TerminationDrainDuration') is not None:
            self.termination_drain_duration = m.get('TerminationDrainDuration')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigK8sNewAPIsSupport(TeaModel):
    def __init__(
        self,
        gateway_apienabled: bool = None,
    ):
        # Indicates whether Gateway API is enabled. Valid values:
        # 
        # *   `true`: Gateway API is enabled.
        # *   `false`: Gateway API is disabled.
        self.gateway_apienabled = gateway_apienabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_apienabled is not None:
            result['GatewayAPIEnabled'] = self.gateway_apienabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayAPIEnabled') is not None:
            self.gateway_apienabled = m.get('GatewayAPIEnabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        url: str = None,
    ):
        # Indicates whether mesh topology is enabled. Mesh topology can be enabled only when Prometheus monitoring is enabled. If Prometheus monitoring is disabled, you must set this parameter to `false`. Valid values:
        # 
        # *   `true`: Mesh topology is enabled.
        # *   `false`: Mesh topology is disabled.
        self.enabled = enabled
        # The endpoint of the mesh topology service.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigLocalityLB(TeaModel):
    def __init__(
        self,
        distribute: Dict[str, Any] = None,
        enabled: bool = None,
        failover: Dict[str, Any] = None,
    ):
        # The configurations of cross-region traffic distribution.
        # 
        # >  Only one of `Failover` and Distribute parameters can be set. If you set the `Distribute` parameter, you cannot set the Failover parameter.
        self.distribute = distribute
        # Indicates whether cross-region load balancing is enabled. Valid values:
        # 
        # *   `true`: Cross-region load balancing is enabled.
        # *   `false`: Cross-region load balancing is disabled.
        self.enabled = enabled
        # The configurations of cross-region failover.
        # 
        # >  Only one of Failover and `Distribute` parameters can be set. If you set the `Failover` parameter, you cannot set the `Distribute` parameter.
        self.failover = failover

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distribute is not None:
            result['Distribute'] = self.distribute
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.failover is not None:
            result['Failover'] = self.failover
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Distribute') is not None:
            self.distribute = m.get('Distribute')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Failover') is not None:
            self.failover = m.get('Failover')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Indicates whether MSE is enabled. Valid values:
        # 
        # - `true`: MSE is enabled.
        # - `false`: MSE is disabled.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        limit_cpu: str = None,
        limit_memory: str = None,
        log_level: str = None,
        request_cpu: str = None,
        request_memory: str = None,
    ):
        # Indicates whether the OPA plug-in is installed. Valid values:
        # 
        # *   `true`: The OPA plug-in is installed.
        # *   `false`: The OPA plug-in is not installed.
        self.enabled = enabled
        # The maximum number of CPU cores that are available to the OPA proxy container.
        self.limit_cpu = limit_cpu
        # The maximum size of the memory that is available to the OPA proxy container.
        self.limit_memory = limit_memory
        # The level of the logs to be generated for OPA.
        self.log_level = log_level
        # The number of CPU cores that are requested by the OPA proxy container.
        self.request_cpu = request_cpu
        # The size of the memory that is requested by the OPA proxy container.
        self.request_memory = request_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotConfigSource(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        nacos_id: str = None,
    ):
        # Indicates whether communication is allowed between external services and services in the mesh. Valid values:
        # 
        # *   `true`: The communication is allowed.
        # *   `false`: The communication is not allowed.
        self.enabled = enabled
        # The ID of the Nacos instance that provides external service information.
        self.nacos_id = nacos_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.nacos_id is not None:
            result['NacosID'] = self.nacos_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('NacosID') is not None:
            self.nacos_id = m.get('NacosID')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotFeature(TeaModel):
    def __init__(
        self,
        enable_sdsserver: bool = None,
        filter_gateway_cluster_config: bool = None,
    ):
        # Indicates whether Secret Discovery Service (SDS) is enabled. Valid values:
        # 
        # *   `true`: SDS is enabled.
        # *   `false`: SDS is disabled.
        self.enable_sdsserver = enable_sdsserver
        # Indicates whether gateway configuration filtering is enabled. Valid values:
        # 
        # *   `true`: Gateway configuration filtering is enabled.
        # *   `false`: Gateway configuration filtering is disabled.
        self.filter_gateway_cluster_config = filter_gateway_cluster_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_sdsserver is not None:
            result['EnableSDSServer'] = self.enable_sdsserver
        if self.filter_gateway_cluster_config is not None:
            result['FilterGatewayClusterConfig'] = self.filter_gateway_cluster_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSDSServer') is not None:
            self.enable_sdsserver = m.get('EnableSDSServer')
        if m.get('FilterGatewayClusterConfig') is not None:
            self.filter_gateway_cluster_config = m.get('FilterGatewayClusterConfig')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot(TeaModel):
    def __init__(
        self,
        config_source: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotConfigSource = None,
        feature: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotFeature = None,
        http_10enabled: bool = None,
        trace_sampling: float = None,
    ):
        # The configurations of communication between external services and services in the mesh.
        self.config_source = config_source
        # The configurations of Pilot features.
        self.feature = feature
        # Indicates whether HTTP/1.0 is supported. Valid values:
        # 
        # *   `true`: HTTP/1.0 is supported.
        # *   `false`: HTTP/1.0 is not supported.
        self.http_10enabled = http_10enabled
        # The sampling percentage of tracing analysis.
        self.trace_sampling = trace_sampling

    def validate(self):
        if self.config_source:
            self.config_source.validate()
        if self.feature:
            self.feature.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_source is not None:
            result['ConfigSource'] = self.config_source.to_map()
        if self.feature is not None:
            result['Feature'] = self.feature.to_map()
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSource') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotConfigSource()
            self.config_source = temp_model.from_map(m['ConfigSource'])
        if m.get('Feature') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotFeature()
            self.feature = temp_model.from_map(m['Feature'])
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus(TeaModel):
    def __init__(
        self,
        external_url: str = None,
        use_external: bool = None,
    ):
        # The endpoint of Prometheus monitoring. If you use a custom Prometheus instance, this parameter is populated by the system.
        self.external_url = external_url
        # Indicates whether a custom Prometheus instance is used. Valid values:
        # 
        # *   `true`: A custom Prometheus instance is used.
        # *   `false`: No custom Prometheus instance is used.
        self.use_external = use_external

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.use_external is not None:
            result['UseExternal'] = self.use_external
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('UseExternal') is not None:
            self.use_external = m.get('UseExternal')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport(TeaModel):
    def __init__(
        self,
        dubbo_filter_enabled: bool = None,
        mysql_filter_enabled: bool = None,
        redis_filter_enabled: bool = None,
        thrift_filter_enabled: bool = None,
    ):
        # Indicates whether Dubbo Filter is enabled. Valid values:
        # 
        # *   `true`: Dubbo Filter is enabled.
        # *   `false`: Dubbo Filter is disabled.
        self.dubbo_filter_enabled = dubbo_filter_enabled
        # Indicates whether MySQL Filter is enabled. Valid values:
        # 
        # *   `true`: MySQL Filter is enabled.
        # *   `false`: MySQL Filter is disabled.
        self.mysql_filter_enabled = mysql_filter_enabled
        # Indicates whether Redis Filter is enabled. Valid values:
        # 
        # *   `true`: Redis Filter is enabled.
        # *   `false`: Redis Filter is disabled.
        self.redis_filter_enabled = redis_filter_enabled
        # Indicates whether Thrift Filter is enabled. Valid values:
        # 
        # *   `true`: Thrift Filter is enabled.
        # *   `false`: Thrift Filter is disabled.
        self.thrift_filter_enabled = thrift_filter_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dubbo_filter_enabled is not None:
            result['DubboFilterEnabled'] = self.dubbo_filter_enabled
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DubboFilterEnabled') is not None:
            self.dubbo_filter_enabled = m.get('DubboFilterEnabled')
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy(TeaModel):
    def __init__(
        self,
        access_log_file: str = None,
        access_log_format: str = None,
        access_log_service_enabled: bool = None,
        access_log_service_host: str = None,
        access_log_service_port: int = None,
        cluster_domain: str = None,
        enable_dnsproxying: bool = None,
        limit_cpu: str = None,
        limit_memory: str = None,
        request_cpu: str = None,
        request_memory: str = None,
    ):
        # The path to the file that stores the access logs of sidecar proxies.
        self.access_log_file = access_log_file
        # The format of the access logs of sidecar proxies.
        self.access_log_format = access_log_format
        # Indicates whether gRPC Access Log Service (ALS) for Envoy is enabled. Valid values:
        # 
        # *   `true`: gRPC ALS for Envoy is enabled.
        # *   `false`: gRPC ALS for Envoy is disabled.
        self.access_log_service_enabled = access_log_service_enabled
        # The endpoint of gRPC ALS for Envoy.
        self.access_log_service_host = access_log_service_host
        # The port of gRPC ALS for Envoy.
        self.access_log_service_port = access_log_service_port
        # The trusted domain.
        self.cluster_domain = cluster_domain
        # Indicates whether the Domain Name System (DNS) proxy feature is enabled. Valid values: Valid values:
        # 
        # *   `true`: The DNS proxy feature is enabled.
        # *   `false`: The DNS proxy feature is disabled.
        self.enable_dnsproxying = enable_dnsproxying
        # The maximum number of CPU cores.
        self.limit_cpu = limit_cpu
        # The maximum size of the memory.
        self.limit_memory = limit_memory
        # The number of CPU cores that are requested.
        self.request_cpu = request_cpu
        # The size of the memory that is requested.
        self.request_memory = request_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_file is not None:
            result['AccessLogFile'] = self.access_log_file
        if self.access_log_format is not None:
            result['AccessLogFormat'] = self.access_log_format
        if self.access_log_service_enabled is not None:
            result['AccessLogServiceEnabled'] = self.access_log_service_enabled
        if self.access_log_service_host is not None:
            result['AccessLogServiceHost'] = self.access_log_service_host
        if self.access_log_service_port is not None:
            result['AccessLogServicePort'] = self.access_log_service_port
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.enable_dnsproxying is not None:
            result['EnableDNSProxying'] = self.enable_dnsproxying
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogFile') is not None:
            self.access_log_file = m.get('AccessLogFile')
        if m.get('AccessLogFormat') is not None:
            self.access_log_format = m.get('AccessLogFormat')
        if m.get('AccessLogServiceEnabled') is not None:
            self.access_log_service_enabled = m.get('AccessLogServiceEnabled')
        if m.get('AccessLogServiceHost') is not None:
            self.access_log_service_host = m.get('AccessLogServiceHost')
        if m.get('AccessLogServicePort') is not None:
            self.access_log_service_port = m.get('AccessLogServicePort')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('EnableDNSProxying') is not None:
            self.enable_dnsproxying = m.get('EnableDNSProxying')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        exclude_namespaces: str = None,
    ):
        # Indicates whether the CNI plug-in is enabled. Valid values:
        # 
        # *   `true`: The CNI plug-in is enabled.
        # *   `false`: The CNI plug-in is disabled.
        self.enabled = enabled
        # The namespaces to exclude. The CNI plug-in ignores pods in the excluded namespaces.
        self.exclude_namespaces = exclude_namespaces

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.exclude_namespaces is not None:
            result['ExcludeNamespaces'] = self.exclude_namespaces
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExcludeNamespaces') is not None:
            self.exclude_namespaces = m.get('ExcludeNamespaces')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(
        self,
        auto_injection_policy_enabled: bool = None,
        enable_namespaces_by_default: bool = None,
        init_cniconfiguration: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration = None,
        limit_cpu: str = None,
        limit_memory: str = None,
        request_cpu: str = None,
        request_memory: str = None,
        sidecar_injector_num: int = None,
        sidecar_injector_webhook_as_yaml: str = None,
    ):
        # Indicates whether automatic sidecar injection can be enabled by using pod annotations. Valid values:
        # 
        # *   `true`: Automatic sidecar injection can be enabled by using pod annotations.
        # *   `false`: Automatic sidecar injection cannot be enabled by using pod annotations.
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        # Indicates whether automatic sidecar injection is enabled for all namespaces. Valid values:
        # 
        # *   `true`: Automatic sidecar injection is enabled for all namespaces.
        # *   `false`: Automatic sidecar injection is not enabled for all namespaces.
        self.enable_namespaces_by_default = enable_namespaces_by_default
        # The configurations of Container Network Interface (CNI).
        self.init_cniconfiguration = init_cniconfiguration
        # The maximum number of CPU cores that are available to the sidecar injector pod.
        self.limit_cpu = limit_cpu
        # The maximum size of the memory that is available to the sidecar injector pod.
        self.limit_memory = limit_memory
        # The number of CPU cores that are requested by the sidecar injector pod.
        self.request_cpu = request_cpu
        # The size of the memory that is requested by the sidecar injector pod.
        self.request_memory = request_memory
        # The number of component replicas that are used for sidecar injection. Default value: `1`.
        self.sidecar_injector_num = sidecar_injector_num
        # Other configurations of automatic sidecar injection, in the YAML format. For more information, see [Enable automatic sidecar injection by using multiple methods](~~186136~~).
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml

    def validate(self):
        if self.init_cniconfiguration:
            self.init_cniconfiguration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.init_cniconfiguration is not None:
            result['InitCNIConfiguration'] = self.init_cniconfiguration.to_map()
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.sidecar_injector_num is not None:
            result['SidecarInjectorNum'] = self.sidecar_injector_num
        if self.sidecar_injector_webhook_as_yaml is not None:
            result['SidecarInjectorWebhookAsYaml'] = self.sidecar_injector_webhook_as_yaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(m['InitCNIConfiguration'])
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('SidecarInjectorNum') is not None:
            self.sidecar_injector_num = m.get('SidecarInjectorNum')
        if m.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = m.get('SidecarInjectorWebhookAsYaml')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Indicates whether WebAssembly Filter is enabled. Valid values:
        # 
        # *   `true`:WebAssembly Filter is enabled.
        # *   `false`: WebAssembly Filter is disabled.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig(TeaModel):
    def __init__(
        self,
        access_log: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog = None,
        audit: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit = None,
        control_plane_log_info: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigControlPlaneLogInfo = None,
        customized_zipkin: bool = None,
        edition: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigEdition = None,
        enable_locality_lb: bool = None,
        exclude_ipranges: str = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ports: str = None,
        extra_configuration: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfiguration = None,
        include_ipranges: str = None,
        k_8s_new_apis_support: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigK8sNewAPIsSupport = None,
        kiali: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali = None,
        locality_lb: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigLocalityLB = None,
        mse: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE = None,
        opa: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA = None,
        outbound_traffic_policy: str = None,
        pilot: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot = None,
        prometheus: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus = None,
        protocol_support: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport = None,
        proxy: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy = None,
        sidecar_injector: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector = None,
        telemetry: bool = None,
        tracing: bool = None,
        web_assembly_filter_deployment: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment = None,
    ):
        # The configurations of access log collection.
        self.access_log = access_log
        # The information about mesh audit.
        self.audit = audit
        # The configurations of control-plane log collection.
        self.control_plane_log_info = control_plane_log_info
        # Indicates whether a custom Zipkin system is used. Valid values:
        # 
        # *   `true`: A custom Zipkin system is used.
        # *   `false`: No custom Zipkin system is used.
        self.customized_zipkin = customized_zipkin
        # The information about the edition.
        self.edition = edition
        # Indicates whether the feature that routes traffic to the nearest instance is enabled. Valid values:
        # 
        # *   `true`: The feature is enabled.
        # *   `false`: The feature is disabled.
        self.enable_locality_lb = enable_locality_lb
        # The IP ranges in CIDR form to be excluded from redirection to sidecar proxies in the ASM instance.
        self.exclude_ipranges = exclude_ipranges
        # The inbound ports to be excluded from redirection to sidecar proxies in the ASM instance.
        self.exclude_inbound_ports = exclude_inbound_ports
        # The outbound ports to be excluded from redirection to sidecar proxies in the ASM instance.
        self.exclude_outbound_ports = exclude_outbound_ports
        # The configurations of additional features for the ASM instance.
        self.extra_configuration = extra_configuration
        # The IP ranges in CIDR form to redirect to the sidecar proxies in the ASM instance.
        self.include_ipranges = include_ipranges
        # The information about the Kubernetes API.
        self.k_8s_new_apis_support = k_8s_new_apis_support
        # The configurations of mesh topology.
        self.kiali = kiali
        # The configurations of cross-region load balancing.
        self.locality_lb = locality_lb
        # The configurations of Microservices Engine (MSE).
        self.mse = mse
        # The information about the Open Policy Agent (OPA) plug-in.
        self.opa = opa
        # The outbound traffic policy. Valid values:
        # 
        # *   `ALLOW_ANY`: Outbound traffic to all external services is allowed.
        # *   `REGISTRY_ONLY`: Outbound traffic is allowed to only external services that are defined in the service registry of the ASM instance.
        self.outbound_traffic_policy = outbound_traffic_policy
        # The Pilot configurations.
        self.pilot = pilot
        # The configurations of Prometheus monitoring.
        self.prometheus = prometheus
        # The configurations of protocol support.
        self.protocol_support = protocol_support
        # The proxy configurations.
        self.proxy = proxy
        # The configurations of the sidecar injector.
        self.sidecar_injector = sidecar_injector
        # Indicates whether Prometheus monitoring is enabled. We recommend that you use [Prometheus Service of Application Real-Time Monitoring Service (ARMS)](https://arms.console.aliyun.com/). Valid values:
        # 
        # *   `true`: Prometheus monitoring is enabled.
        # *   `false`: Prometheus monitoring is disabled.
        self.telemetry = telemetry
        # Indicates whether tracing analysis is enabled. This feature can be enabled only after [Tracing Analysis](https://tracing-analysis.console.aliyun.com/) is activated. Valid values:
        # 
        # *   `true`: Tracing analysis is enabled.
        # *   `false`: Tracing analysis is disabled.
        self.tracing = tracing
        # The configurations of WebAssembly Filter.
        self.web_assembly_filter_deployment = web_assembly_filter_deployment

    def validate(self):
        if self.access_log:
            self.access_log.validate()
        if self.audit:
            self.audit.validate()
        if self.control_plane_log_info:
            self.control_plane_log_info.validate()
        if self.edition:
            self.edition.validate()
        if self.extra_configuration:
            self.extra_configuration.validate()
        if self.k_8s_new_apis_support:
            self.k_8s_new_apis_support.validate()
        if self.kiali:
            self.kiali.validate()
        if self.locality_lb:
            self.locality_lb.validate()
        if self.mse:
            self.mse.validate()
        if self.opa:
            self.opa.validate()
        if self.pilot:
            self.pilot.validate()
        if self.prometheus:
            self.prometheus.validate()
        if self.protocol_support:
            self.protocol_support.validate()
        if self.proxy:
            self.proxy.validate()
        if self.sidecar_injector:
            self.sidecar_injector.validate()
        if self.web_assembly_filter_deployment:
            self.web_assembly_filter_deployment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log is not None:
            result['AccessLog'] = self.access_log.to_map()
        if self.audit is not None:
            result['Audit'] = self.audit.to_map()
        if self.control_plane_log_info is not None:
            result['ControlPlaneLogInfo'] = self.control_plane_log_info.to_map()
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.edition is not None:
            result['Edition'] = self.edition.to_map()
        if self.enable_locality_lb is not None:
            result['EnableLocalityLB'] = self.enable_locality_lb
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.extra_configuration is not None:
            result['ExtraConfiguration'] = self.extra_configuration.to_map()
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.k_8s_new_apis_support is not None:
            result['K8sNewAPIsSupport'] = self.k_8s_new_apis_support.to_map()
        if self.kiali is not None:
            result['Kiali'] = self.kiali.to_map()
        if self.locality_lb is not None:
            result['LocalityLB'] = self.locality_lb.to_map()
        if self.mse is not None:
            result['MSE'] = self.mse.to_map()
        if self.opa is not None:
            result['OPA'] = self.opa.to_map()
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus.to_map()
        if self.protocol_support is not None:
            result['ProtocolSupport'] = self.protocol_support.to_map()
        if self.proxy is not None:
            result['Proxy'] = self.proxy.to_map()
        if self.sidecar_injector is not None:
            result['SidecarInjector'] = self.sidecar_injector.to_map()
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.web_assembly_filter_deployment is not None:
            result['WebAssemblyFilterDeployment'] = self.web_assembly_filter_deployment.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLog') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog()
            self.access_log = temp_model.from_map(m['AccessLog'])
        if m.get('Audit') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit()
            self.audit = temp_model.from_map(m['Audit'])
        if m.get('ControlPlaneLogInfo') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigControlPlaneLogInfo()
            self.control_plane_log_info = temp_model.from_map(m['ControlPlaneLogInfo'])
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('Edition') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigEdition()
            self.edition = temp_model.from_map(m['Edition'])
        if m.get('EnableLocalityLB') is not None:
            self.enable_locality_lb = m.get('EnableLocalityLB')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('ExtraConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfiguration()
            self.extra_configuration = temp_model.from_map(m['ExtraConfiguration'])
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('K8sNewAPIsSupport') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigK8sNewAPIsSupport()
            self.k_8s_new_apis_support = temp_model.from_map(m['K8sNewAPIsSupport'])
        if m.get('Kiali') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali()
            self.kiali = temp_model.from_map(m['Kiali'])
        if m.get('LocalityLB') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigLocalityLB()
            self.locality_lb = temp_model.from_map(m['LocalityLB'])
        if m.get('MSE') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE()
            self.mse = temp_model.from_map(m['MSE'])
        if m.get('OPA') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA()
            self.opa = temp_model.from_map(m['OPA'])
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('Pilot') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(m['Pilot'])
        if m.get('Prometheus') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus()
            self.prometheus = temp_model.from_map(m['Prometheus'])
        if m.get('ProtocolSupport') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport()
            self.protocol_support = temp_model.from_map(m['ProtocolSupport'])
        if m.get('Proxy') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy()
            self.proxy = temp_model.from_map(m['Proxy'])
        if m.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(m['SidecarInjector'])
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('WebAssemblyFilterDeployment') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment()
            self.web_assembly_filter_deployment = temp_model.from_map(m['WebAssemblyFilterDeployment'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switches: List[str] = None,
        vpc_id: str = None,
    ):
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The ID of the vSwitch.
        self.v_switches = v_switches
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpec(TeaModel):
    def __init__(
        self,
        load_balancer: DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer = None,
        mesh_config: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig = None,
        network: DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork = None,
    ):
        # The information about load balancing.
        self.load_balancer = load_balancer
        # The configurations of the ASM instance.
        self.mesh_config = mesh_config
        # The network configurations of the ASM instance.
        self.network = network

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()
        if self.mesh_config:
            self.mesh_config.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(m['LoadBalancer'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        if m.get('Network') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMesh(TeaModel):
    def __init__(
        self,
        cluster_spec: str = None,
        clusters: List[str] = None,
        endpoints: DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints = None,
        owner_id: str = None,
        owner_type: str = None,
        service_mesh_info: DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo = None,
        spec: DescribeServiceMeshDetailResponseBodyServiceMeshSpec = None,
    ):
        # The specification of the ASM instance. Valid values:
        # 
        # - `standard`: Standard Edition
        # - `enterprise`: Enterprise Edition
        # - `ultimate`: Ultimate Edition
        self.cluster_spec = cluster_spec
        # The list of clusters.
        self.clusters = clusters
        # The endpoints of the ASM instance.
        self.endpoints = endpoints
        # The ID of the Alibaba Cloud service instance for which the ASM instance is created.
        self.owner_id = owner_id
        # The Alibaba Cloud service for which the ASM instance is created. Valid values:
        # 
        # - `ackone`: The ASM instance is created for Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        # - An empty value indicates that the ASM instance is created by the user.
        self.owner_type = owner_type
        # The basic information about the ASM instance.
        self.service_mesh_info = service_mesh_info
        # The specifications of the ASM instance.
        self.spec = spec

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()
        if self.service_mesh_info:
            self.service_mesh_info.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        if m.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(m['ServiceMeshInfo'])
        if m.get('Spec') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class DescribeServiceMeshDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_mesh: DescribeServiceMeshDetailResponseBodyServiceMesh = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the ASM instance.
        self.service_mesh = service_mesh

    def validate(self):
        if self.service_mesh:
            self.service_mesh.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_mesh is not None:
            result['ServiceMesh'] = self.service_mesh.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceMesh') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMesh()
            self.service_mesh = temp_model.from_map(m['ServiceMesh'])
        return self


class DescribeServiceMeshDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceMeshDetailResponseBody = None,
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
            temp_model = DescribeServiceMeshDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshKubeconfigRequest(TeaModel):
    def __init__(
        self,
        private_ip_address: bool = None,
        service_mesh_id: str = None,
    ):
        # Specifies whether to query the kubeconfig file that is used for Internet access or internal network access.
        self.private_ip_address = private_ip_address
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshKubeconfigResponseBody(TeaModel):
    def __init__(
        self,
        kubeconfig: str = None,
        request_id: str = None,
    ):
        # The content of the kubeconfig file of the cluster.
        self.kubeconfig = kubeconfig
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubeconfig is not None:
            result['Kubeconfig'] = self.kubeconfig
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Kubeconfig') is not None:
            self.kubeconfig = m.get('Kubeconfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceMeshKubeconfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceMeshKubeconfigResponseBody = None,
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
            temp_model = DescribeServiceMeshKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshLogsRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshLogsResponseBodyLogs(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        log: str = None,
        service_mesh_id: str = None,
    ):
        # The point in time when the logs were generated.
        self.creation_time = creation_time
        # The content of the logs.
        self.log = log
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.log is not None:
            result['Log'] = self.log
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Log') is not None:
            self.log = m.get('Log')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshLogsResponseBody(TeaModel):
    def __init__(
        self,
        logs: List[DescribeServiceMeshLogsResponseBodyLogs] = None,
        request_id: str = None,
    ):
        # The details of the logs.
        self.logs = logs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeServiceMeshLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceMeshLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceMeshLogsResponseBody = None,
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
            temp_model = DescribeServiceMeshLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshProxyStatusRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshProxyStatusResponseBodyProxyStatus(TeaModel):
    def __init__(
        self,
        cluster_synced: str = None,
        endpoint_percent: str = None,
        endpoint_synced: str = None,
        istio_version: str = None,
        listener_synced: str = None,
        proxy_id: str = None,
        proxy_version: str = None,
        route_synced: str = None,
    ):
        # The update status of the proxy. Valid values:
        # 
        # *   `SYNCED`: The status of the proxy is updated.
        # *   `NOT SENT`: The status of the proxy is not updated.
        # *   `STALE (Never Acknowledged)`: Istiod has sent multiple requests to the Envoy proxy to update the status of the proxy but receives no response.
        # *   `STALE`: Istiod has sent a request to the Envoy proxy to update the status of the proxy but receives no response.
        self.cluster_synced = cluster_synced
        # The percentage of the updated endpoints.
        self.endpoint_percent = endpoint_percent
        # The update status of the endpoint. Valid values:
        # 
        # *   `SYNCED`: The status of the endpoint is updated.
        # *   `NOT SENT`: The status of the endpoint is not updated.
        # *   `STALE (Never Acknowledged)`: Istiod has sent multiple requests to the Envoy proxy to update the status of the endpoint but receives no response.
        # *   `STALE`: Istiod has sent a request to the Envoy proxy to update the status of the endpoint but receives no response.
        self.endpoint_synced = endpoint_synced
        # The version of Istiod.
        self.istio_version = istio_version
        # The update status of the listener. Valid values:
        # 
        # *   `SYNCED`: The status of the listener is updated.
        # *   `NOT SENT`: The status of the listener is not updated.
        # *   `STALE (Never Acknowledged)`: Istiod has sent multiple requests to the Envoy proxy to update the status of the listener but receives no response.
        # *   `STALE`: Istiod has sent a request to the Envoy proxy to update the status of the listener but receives no response.
        self.listener_synced = listener_synced
        # The ID of the proxy on the data plane.
        self.proxy_id = proxy_id
        # The version number of the proxy on the data plane.
        self.proxy_version = proxy_version
        # The update status of the route. Valid values:
        # 
        # *   `SYNCED`: The status of the route is updated.
        # *   `NOT SENT`: The status of the route is not updated.
        # *   `STALE (Never Acknowledged)`: Istiod has sent multiple requests to the Envoy proxy to update the status of the route but receives no response.
        # *   `STALE`: Istiod has sent a request to the Envoy proxy to update the status of the route but receives no response.
        self.route_synced = route_synced

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_synced is not None:
            result['ClusterSynced'] = self.cluster_synced
        if self.endpoint_percent is not None:
            result['EndpointPercent'] = self.endpoint_percent
        if self.endpoint_synced is not None:
            result['EndpointSynced'] = self.endpoint_synced
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.listener_synced is not None:
            result['ListenerSynced'] = self.listener_synced
        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id
        if self.proxy_version is not None:
            result['ProxyVersion'] = self.proxy_version
        if self.route_synced is not None:
            result['RouteSynced'] = self.route_synced
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterSynced') is not None:
            self.cluster_synced = m.get('ClusterSynced')
        if m.get('EndpointPercent') is not None:
            self.endpoint_percent = m.get('EndpointPercent')
        if m.get('EndpointSynced') is not None:
            self.endpoint_synced = m.get('EndpointSynced')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('ListenerSynced') is not None:
            self.listener_synced = m.get('ListenerSynced')
        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')
        if m.get('ProxyVersion') is not None:
            self.proxy_version = m.get('ProxyVersion')
        if m.get('RouteSynced') is not None:
            self.route_synced = m.get('RouteSynced')
        return self


class DescribeServiceMeshProxyStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        proxy_status: List[DescribeServiceMeshProxyStatusResponseBodyProxyStatus] = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code. Valid values:
        # 
        # `200`: The status code returned because the operation is successful.
        # 
        # *   `403`: The status code returned because you are not authorized to perform this operation.
        # *   `503`: The status code returned because a backend server error occurs.
        self.code = code
        # The returned message.
        self.message = message
        # The information about the status of the proxies on the data plane.
        self.proxy_status = proxy_status
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.proxy_status:
            for k in self.proxy_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['ProxyStatus'] = []
        if self.proxy_status is not None:
            for k in self.proxy_status:
                result['ProxyStatus'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.proxy_status = []
        if m.get('ProxyStatus') is not None:
            for k in m.get('ProxyStatus'):
                temp_model = DescribeServiceMeshProxyStatusResponseBodyProxyStatus()
                self.proxy_status.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeServiceMeshProxyStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceMeshProxyStatusResponseBody = None,
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
            temp_model = DescribeServiceMeshProxyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshUpgradeStatusRequest(TeaModel):
    def __init__(
        self,
        all_istio_gateway_full_names: str = None,
        guest_cluster_ids: str = None,
        service_mesh_id: str = None,
    ):
        # The ID of the request.
        self.all_istio_gateway_full_names = all_istio_gateway_full_names
        # The fully qualified names of ingress gateways in the ASM instance. Separate multiple names with commas (,).
        self.guest_cluster_ids = guest_cluster_ids
        # The IDs of the clusters on the data plane of the ASM instance. Separate multiple clusters with commas (,).
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_istio_gateway_full_names is not None:
            result['AllIstioGatewayFullNames'] = self.all_istio_gateway_full_names
        if self.guest_cluster_ids is not None:
            result['GuestClusterIds'] = self.guest_cluster_ids
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllIstioGatewayFullNames') is not None:
            self.all_istio_gateway_full_names = m.get('AllIstioGatewayFullNames')
        if m.get('GuestClusterIds') is not None:
            self.guest_cluster_ids = m.get('GuestClusterIds')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshUpgradeStatusResponseBodyUpgradeDetail(TeaModel):
    def __init__(
        self,
        finished_gateways_num: int = None,
        gateway_status_record: Dict[str, UpgradeDetailGatewayStatusRecordValue] = None,
        mesh_status: str = None,
        total_gateways_num: int = None,
    ):
        # The status of the ASM instance. Valid values:
        # 
        # *   running: The instance is running.
        # *   `upgrading`: The instance is being upgraded.
        # *   `upgrading_failed`: The upgrade of the instance fails.
        self.finished_gateways_num = finished_gateways_num
        self.gateway_status_record = gateway_status_record
        # The total number of ingress gateways in the ASM instance.
        self.mesh_status = mesh_status
        # The information about the status of the ingress gateways.
        self.total_gateways_num = total_gateways_num

    def validate(self):
        if self.gateway_status_record:
            for v in self.gateway_status_record.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finished_gateways_num is not None:
            result['FinishedGatewaysNum'] = self.finished_gateways_num
        result['GatewayStatusRecord'] = {}
        if self.gateway_status_record is not None:
            for k, v in self.gateway_status_record.items():
                result['GatewayStatusRecord'][k] = v.to_map()
        if self.mesh_status is not None:
            result['MeshStatus'] = self.mesh_status
        if self.total_gateways_num is not None:
            result['TotalGatewaysNum'] = self.total_gateways_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishedGatewaysNum') is not None:
            self.finished_gateways_num = m.get('FinishedGatewaysNum')
        self.gateway_status_record = {}
        if m.get('GatewayStatusRecord') is not None:
            for k, v in m.get('GatewayStatusRecord').items():
                temp_model = UpgradeDetailGatewayStatusRecordValue()
                self.gateway_status_record[k] = temp_model.from_map(v)
        if m.get('MeshStatus') is not None:
            self.mesh_status = m.get('MeshStatus')
        if m.get('TotalGatewaysNum') is not None:
            self.total_gateways_num = m.get('TotalGatewaysNum')
        return self


class DescribeServiceMeshUpgradeStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        upgrade_detail: DescribeServiceMeshUpgradeStatusResponseBodyUpgradeDetail = None,
    ):
        # The upgrade results.
        self.request_id = request_id
        # The number of ingress gateways that are upgraded.
        self.upgrade_detail = upgrade_detail

    def validate(self):
        if self.upgrade_detail:
            self.upgrade_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upgrade_detail is not None:
            result['UpgradeDetail'] = self.upgrade_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpgradeDetail') is not None:
            temp_model = DescribeServiceMeshUpgradeStatusResponseBodyUpgradeDetail()
            self.upgrade_detail = temp_model.from_map(m['UpgradeDetail'])
        return self


class DescribeServiceMeshUpgradeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceMeshUpgradeStatusResponseBody = None,
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
            temp_model = DescribeServiceMeshUpgradeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshVMsRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshVMsResponseBodyVMs(TeaModel):
    def __init__(
        self,
        has_tag: bool = None,
        host_name: str = None,
        instance_id: str = None,
        ip_address: str = None,
        region: str = None,
        security_group_ids: str = None,
        service_mesh_id: str = None,
        status: str = None,
    ):
        # Indicates whether the ECS instance has labels.
        self.has_tag = has_tag
        # The hostname of the ECS instance.
        self.host_name = host_name
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The IP address of the ECS instance.
        self.ip_address = ip_address
        # The ID of the region.
        self.region = region
        # The security group to which the ECS instance belongs.
        self.security_group_ids = security_group_ids
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The state of the ECS instance.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_tag is not None:
            result['HasTag'] = self.has_tag
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.region is not None:
            result['Region'] = self.region
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasTag') is not None:
            self.has_tag = m.get('HasTag')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeServiceMeshVMsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vms: List[DescribeServiceMeshVMsResponseBodyVMs] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ECS instances that reside in the same VPC as the ASM instance.
        self.vms = vms

    def validate(self):
        if self.vms:
            for k in self.vms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VMs'] = []
        if self.vms is not None:
            for k in self.vms:
                result['VMs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.vms = []
        if m.get('VMs') is not None:
            for k in m.get('VMs'):
                temp_model = DescribeServiceMeshVMsResponseBodyVMs()
                self.vms.append(temp_model.from_map(k))
        return self


class DescribeServiceMeshVMsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceMeshVMsResponseBody = None,
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
            temp_model = DescribeServiceMeshVMsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesEndpoints(TeaModel):
    def __init__(
        self,
        intranet_api_server_endpoint: str = None,
        intranet_pilot_endpoint: str = None,
        public_api_server_endpoint: str = None,
        public_pilot_endpoint: str = None,
        reverse_tunnel_endpoint: str = None,
    ):
        # The endpoint that is used to access the API server from the internal network.
        self.intranet_api_server_endpoint = intranet_api_server_endpoint
        # The endpoint that is used to access Istio Pilot from the internal network.
        self.intranet_pilot_endpoint = intranet_pilot_endpoint
        # The endpoint that is used to expose the API server to the Internet.
        self.public_api_server_endpoint = public_api_server_endpoint
        # The endpoint that is used to expose Istio Pilot to the Internet.
        self.public_pilot_endpoint = public_pilot_endpoint
        # The endpoint of the reverse tunnel.
        self.reverse_tunnel_endpoint = reverse_tunnel_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.intranet_pilot_endpoint is not None:
            result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        if self.public_pilot_endpoint is not None:
            result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        if self.reverse_tunnel_endpoint is not None:
            result['ReverseTunnelEndpoint'] = self.reverse_tunnel_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('IntranetPilotEndpoint') is not None:
            self.intranet_pilot_endpoint = m.get('IntranetPilotEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        if m.get('PublicPilotEndpoint') is not None:
            self.public_pilot_endpoint = m.get('PublicPilotEndpoint')
        if m.get('ReverseTunnelEndpoint') is not None:
            self.reverse_tunnel_endpoint = m.get('ReverseTunnelEndpoint')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        error_message: str = None,
        name: str = None,
        profile: str = None,
        region_id: str = None,
        service_mesh_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
    ):
        # The point in time when the ASM instance was created.
        self.creation_time = creation_time
        # The error message that is returned when the call failed.
        self.error_message = error_message
        # The name of the ASM instance.
        self.name = name
        # The edition of the ASM instance before ASM is available for commercial use. Valid values:
        # 
        # *   `Pro`: Professional Edition
        # *   `Default`: Standard Edition
        self.profile = profile
        # The ID of the region in which the ASM instance resides.
        self.region_id = region_id
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The status of the ASM instance.
        self.state = state
        # The point in time when the ASM instance was last modified.
        self.update_time = update_time
        # The version number of the ASM instance.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer(TeaModel):
    def __init__(
        self,
        api_server_loadbalancer_id: str = None,
        api_server_public_eip: bool = None,
        pilot_public_eip: bool = None,
        pilot_public_loadbalancer_id: str = None,
    ):
        # The ID of the SLB instance that is used when the API server is exposed to the Internet.
        self.api_server_loadbalancer_id = api_server_loadbalancer_id
        # Indicates whether the API Server is exposed to the Internet. Valid values:
        # 
        # *   `true`: The API server is exposed to the Internet.
        # *   `false`: The API server is not exposed to the Internet.
        self.api_server_public_eip = api_server_public_eip
        # Indicates whether Istio Pilot is exposed to the Internet. Valid values:
        # 
        # *   `true`: Istio Pilot is exposed to the Internet.
        # *   `false`: Istio Pilot is not exposed to the Internet.
        self.pilot_public_eip = pilot_public_eip
        # The ID of the Server Load Balancer (SLB) instance that is used when Istio Pilot is exposed to the Internet.
        self.pilot_public_loadbalancer_id = pilot_public_loadbalancer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_loadbalancer_id is not None:
            result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.pilot_public_loadbalancer_id is not None:
            result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiServerLoadbalancerId') is not None:
            self.api_server_loadbalancer_id = m.get('ApiServerLoadbalancerId')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('PilotPublicEip') is not None:
            self.pilot_public_eip = m.get('PilotPublicEip')
        if m.get('PilotPublicLoadbalancerId') is not None:
            self.pilot_public_loadbalancer_id = m.get('PilotPublicLoadbalancerId')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot(TeaModel):
    def __init__(
        self,
        http_10enabled: bool = None,
        trace_sampling: float = None,
    ):
        # Indicates whether the support for HTTP 1.0 is enabled. Valid values:
        # 
        # *   `true`: The support for HTTP 1.0 is enabled.
        # *   `false`: The support for HTTP 1.0 is disabled.
        self.http_10enabled = http_10enabled
        # The sampling percentage of tracing.
        self.trace_sampling = trace_sampling

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        exclude_namespaces: str = None,
    ):
        # Indicates whether elevated privileges are required for the istio-init container when you perform traffic redirection for the istio-proxy container. Valid values:
        # 
        # *   `true`: Elevated privileges are required for the istio-init container.
        # *   `false`: Elevated privileges are not required for the istio-init container.
        self.enabled = enabled
        # The namespace for which sidecar injection is disabled.
        self.exclude_namespaces = exclude_namespaces

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.exclude_namespaces is not None:
            result['ExcludeNamespaces'] = self.exclude_namespaces
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExcludeNamespaces') is not None:
            self.exclude_namespaces = m.get('ExcludeNamespaces')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(
        self,
        auto_injection_policy_enabled: bool = None,
        enable_namespaces_by_default: bool = None,
        init_cniconfiguration: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration = None,
    ):
        # Indicates whether automatic sidecar injection is enabled by using annotations.
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        # Indicates whether automatic sidecar injection is enabled for all namespaces. Valid values:
        # 
        # *   `true`: Automatic sidecar injection is enabled for all namespaces.
        # *   `false`: Automatic sidecar injection is disabled for all namespaces.
        self.enable_namespaces_by_default = enable_namespaces_by_default
        # The initial configurations of Container Network Interface (CNI).
        self.init_cniconfiguration = init_cniconfiguration

    def validate(self):
        if self.init_cniconfiguration:
            self.init_cniconfiguration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.init_cniconfiguration is not None:
            result['InitCNIConfiguration'] = self.init_cniconfiguration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(m['InitCNIConfiguration'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig(TeaModel):
    def __init__(
        self,
        mtls: bool = None,
        outbound_traffic_policy: str = None,
        pilot: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot = None,
        sidecar_injector: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector = None,
        strict_mtls: bool = None,
        telemetry: bool = None,
        tracing: bool = None,
    ):
        # Indicates whether the feature of routing traffic to the nearest instance is enabled. Valid values:
        # 
        # *   `true`: The feature is enabled.
        # *   `false`: The feature is disabled.
        self.mtls = mtls
        # The outbound traffic policy. Valid values:
        # 
        # *   `ALLOW_ANY`: Outbound traffic to an external service is allowed.
        # *   `REGISTRY_ONLY`: Outbound traffic is allowed to only external services that are defined in the service registry of the ASM instance.
        self.outbound_traffic_policy = outbound_traffic_policy
        # The configurations of the control plane.
        self.pilot = pilot
        # The configurations of sidecar injection.
        self.sidecar_injector = sidecar_injector
        # Indicates whether mutual Transport Layer Security (mTLS) is strictly enforced.
        self.strict_mtls = strict_mtls
        # Indicates whether Prometheus monitoring is enabled. We recommend that you use Prometheus Service of Application Real-Time Monitoring Service (ARMS). Valid values:
        # 
        # *   `true`: Prometheus monitoring is enabled.
        # *   `false`: Prometheus monitoring is disabled.
        self.telemetry = telemetry
        # Indicates whether the tracing feature is enabled. This feature can be enabled only after Tracing Analysis is activated. Valid values:
        # 
        # *   `true`: The tracing feature is enabled.
        # *   `false`: The tracing feature is disabled.
        self.tracing = tracing

    def validate(self):
        if self.pilot:
            self.pilot.validate()
        if self.sidecar_injector:
            self.sidecar_injector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mtls is not None:
            result['Mtls'] = self.mtls
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        if self.sidecar_injector is not None:
            result['SidecarInjector'] = self.sidecar_injector.to_map()
        if self.strict_mtls is not None:
            result['StrictMtls'] = self.strict_mtls
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mtls') is not None:
            self.mtls = m.get('Mtls')
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('Pilot') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(m['Pilot'])
        if m.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(m['SidecarInjector'])
        if m.get('StrictMtls') is not None:
            self.strict_mtls = m.get('StrictMtls')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switches: List[str] = None,
        vpc_id: str = None,
    ):
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The IDs of vSwitches.
        self.v_switches = v_switches
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpec(TeaModel):
    def __init__(
        self,
        load_balancer: DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer = None,
        mesh_config: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig = None,
        network: DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork = None,
    ):
        # The information about load balancing.
        self.load_balancer = load_balancer
        # The configurations of the ASM instance.
        self.mesh_config = mesh_config
        # The network configurations of the ASM instance.
        self.network = network

    def validate(self):
        if self.load_balancer:
            self.load_balancer.validate()
        if self.mesh_config:
            self.mesh_config.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(m['LoadBalancer'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        if m.get('Network') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshes(TeaModel):
    def __init__(
        self,
        cluster_spec: str = None,
        clusters: List[str] = None,
        endpoints: DescribeServiceMeshesResponseBodyServiceMeshesEndpoints = None,
        owner_id: str = None,
        owner_type: str = None,
        service_mesh_info: DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo = None,
        spec: DescribeServiceMeshesResponseBodyServiceMeshesSpec = None,
    ):
        # The edition of the ASM instance. Valid values:
        # 
        # - `standard`: Standard Edition
        # - `enterprise`: Enterprise Edition
        # - `ultimate`: Ultimate Edition
        self.cluster_spec = cluster_spec
        # The information about the clusters.
        self.clusters = clusters
        # All endpoints of the ASM instance.
        self.endpoints = endpoints
        # The ID of the Alibaba Cloud service instance for which the ASM instance is created.
        self.owner_id = owner_id
        # The Alibaba Cloud service for which the ASM instance is created. Valid values:
        # 
        # - `ackone`: The ASM instance is created for Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        # - An empty value indicates that the ASM instance is created by the user.
        self.owner_type = owner_type
        # The basic information about the ASM instance.
        self.service_mesh_info = service_mesh_info
        # The specifications of the ASM instance.
        self.spec = spec

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()
        if self.service_mesh_info:
            self.service_mesh_info.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        if m.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(m['ServiceMeshInfo'])
        if m.get('Spec') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class DescribeServiceMeshesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_meshes: List[DescribeServiceMeshesResponseBodyServiceMeshes] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the ASM instances.
        self.service_meshes = service_meshes

    def validate(self):
        if self.service_meshes:
            for k in self.service_meshes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceMeshes'] = []
        if self.service_meshes is not None:
            for k in self.service_meshes:
                result['ServiceMeshes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_meshes = []
        if m.get('ServiceMeshes') is not None:
            for k in m.get('ServiceMeshes'):
                temp_model = DescribeServiceMeshesResponseBodyServiceMeshes()
                self.service_meshes.append(temp_model.from_map(k))
        return self


class DescribeServiceMeshesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceMeshesResponseBody = None,
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
            temp_model = DescribeServiceMeshesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUpgradeVersionRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeUpgradeVersionResponseBodyVersion(TeaModel):
    def __init__(
        self,
        istio_operator_version: str = None,
        istio_version: str = None,
        kubernetes_version: str = None,
    ):
        # The version of the ASM instance.
        self.istio_operator_version = istio_operator_version
        # The Istio version.
        self.istio_version = istio_version
        # The Kubernetes version.
        self.kubernetes_version = kubernetes_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.istio_operator_version is not None:
            result['IstioOperatorVersion'] = self.istio_operator_version
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioOperatorVersion') is not None:
            self.istio_operator_version = m.get('IstioOperatorVersion')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')
        return self


class DescribeUpgradeVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version: DescribeUpgradeVersionResponseBodyVersion = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The version information.
        self.version = version

    def validate(self):
        if self.version:
            self.version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            temp_model = DescribeUpgradeVersionResponseBodyVersion()
            self.version = temp_model.from_map(m['Version'])
        return self


class DescribeUpgradeVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUpgradeVersionResponseBody = None,
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
            temp_model = DescribeUpgradeVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserPermissionsRequest(TeaModel):
    def __init__(
        self,
        sub_account_user_id: str = None,
    ):
        # The ID of the RAM user or RAM role.
        self.sub_account_user_id = sub_account_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_account_user_id is not None:
            result['SubAccountUserId'] = self.sub_account_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubAccountUserId') is not None:
            self.sub_account_user_id = m.get('SubAccountUserId')
        return self


class DescribeUserPermissionsResponseBodyPermissions(TeaModel):
    def __init__(
        self,
        is_ram_role: str = None,
        parent_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        role_name: str = None,
        role_type: str = None,
    ):
        # The entity to which the permissions are granted. A value of `true` indicates that the permissions are granted to a RAM user. A value of `false` indicates that the permissions are granted to a RAM role.
        self.is_ram_role = is_ram_role
        # This parameter is required by the system. The return value is fixed to `0`.
        self.parent_id = parent_id
        # The ID of the ASM instance.
        self.resource_id = resource_id
        # This parameter is required by the system. The return value is fixed to `cluster`.
        self.resource_type = resource_type
        # The name of the permissions. Valid values:
        # 
        # *   `istio-admin`: the permissions of Alibaba Cloud Service Mesh (ASM) administrators.
        # *   `istio-ops`: the permissions of ASM restricted users.
        # *   `istio-readonly`: the read-only permissions.
        self.role_name = role_name
        # This parameter is required by the system. The return value is fixed to `custom`.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_ram_role is not None:
            result['IsRamRole'] = self.is_ram_role
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.role_type is not None:
            result['RoleType'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsRamRole') is not None:
            self.is_ram_role = m.get('IsRamRole')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')
        return self


class DescribeUserPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        permissions: List[DescribeUserPermissionsResponseBodyPermissions] = None,
        request_id: str = None,
    ):
        # The permissions that are granted to an entity.
        self.permissions = permissions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = DescribeUserPermissionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserPermissionsResponseBody = None,
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
            temp_model = DescribeUserPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersWithPermissionsRequest(TeaModel):
    def __init__(
        self,
        user_type: str = None,
    ):
        # Specifies whether to query the IDs of all RAM users or RAM roles to which an RBAC role is assigned. Valid values:
        # 
        # *   `SubUser`: Query the IDs of all RAM users to which an RBAC role is assigned.
        # *   `RamRole`: Query the IDs of all RAM roles to which an RBAC role is assigned.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeUsersWithPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        uids: List[str] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The IDs of the RAM users or RAM roles to which an RBAC role is assigned.
        self.uids = uids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uids is not None:
            result['UIDs'] = self.uids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UIDs') is not None:
            self.uids = m.get('UIDs')
        return self


class DescribeUsersWithPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsersWithPermissionsResponseBody = None,
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
            temp_model = DescribeUsersWithPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVMsInServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeVMsInServiceMeshResponseBodyVMs(TeaModel):
    def __init__(
        self,
        has_tag: bool = None,
        host_name: str = None,
        instance_id: str = None,
        ip_address: str = None,
        region: str = None,
        security_group_ids: str = None,
        status: str = None,
    ):
        # Indicates whether the VM has labels.
        self.has_tag = has_tag
        # The host name of the VM.
        self.host_name = host_name
        # The ID of the VM.
        self.instance_id = instance_id
        # The IP address of the VM.
        self.ip_address = ip_address
        # The region ID.
        self.region = region
        # The security group to which the VM belongs.
        self.security_group_ids = security_group_ids
        # The status of the VM.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_tag is not None:
            result['HasTag'] = self.has_tag
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.region is not None:
            result['Region'] = self.region
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasTag') is not None:
            self.has_tag = m.get('HasTag')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeVMsInServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vms: List[DescribeVMsInServiceMeshResponseBodyVMs] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The VMs that are added to the ASM instance.
        self.vms = vms

    def validate(self):
        if self.vms:
            for k in self.vms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VMs'] = []
        if self.vms is not None:
            for k in self.vms:
                result['VMs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.vms = []
        if m.get('VMs') is not None:
            for k in m.get('VMs'):
                temp_model = DescribeVMsInServiceMeshResponseBodyVMs()
                self.vms.append(temp_model.from_map(k))
        return self


class DescribeVMsInServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVMsInServiceMeshResponseBody = None,
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
            temp_model = DescribeVMsInServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVSwitchesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVSwitchesResponseBodyVSwitches(TeaModel):
    def __init__(
        self,
        is_default: bool = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Indicates whether the vSwitch is the default vSwitch. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.is_default = is_default
        # The state of the vSwitch. Valid values:
        # 
        # *   `Pending`: The vSwitch is being configured.
        # *   `Available`: The vSwitch is available.
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The name of the vSwitch.
        self.v_switch_name = v_switch_name
        # The ID of the VPC to which the vSwitch belongs.
        self.vpc_id = vpc_id
        # 交换机所属的可用区。
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeVSwitchesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        v_switches: List[DescribeVSwitchesResponseBodyVSwitches] = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of vSwitches that are deployed in the VPC in the region. This parameter is optional and is not returned by default.
        self.total_count = total_count
        # The available vSwitches.
        self.v_switches = v_switches

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = DescribeVSwitchesResponseBodyVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVSwitchesResponseBody = None,
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
            temp_model = DescribeVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVersionsResponseBodyVersionInfo(TeaModel):
    def __init__(
        self,
        edition: str = None,
        versions: List[str] = None,
    ):
        # The edition of the ASM instance. Valid values:
        # 
        # *   `Default`: Standard Edition
        # *   `Pro`: Professional Edition that is commercially released
        self.edition = edition
        # The ASM versions available for the ASM instance of the current edition.
        self.versions = versions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.versions is not None:
            result['Versions'] = self.versions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Versions') is not None:
            self.versions = m.get('Versions')
        return self


class DescribeVersionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version_info: List[DescribeVersionsResponseBodyVersionInfo] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The available ASM versions.
        self.version_info = version_info

    def validate(self):
        if self.version_info:
            for k in self.version_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VersionInfo'] = []
        if self.version_info is not None:
            for k in self.version_info:
                result['VersionInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.version_info = []
        if m.get('VersionInfo') is not None:
            for k in m.get('VersionInfo'):
                temp_model = DescribeVersionsResponseBodyVersionInfo()
                self.version_info.append(temp_model.from_map(k))
        return self


class DescribeVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVersionsResponseBody = None,
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
            temp_model = DescribeVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
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


class DescribeVpcsResponseBodyVpcs(TeaModel):
    def __init__(
        self,
        is_default: bool = None,
        status: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # Indicates whether the VPC is the default VPC in the specified region. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.is_default = is_default
        # The status of the VPC. Valid values:
        # 
        # *   `Pending`: The VPC is being configured.
        # *   `Available`: The VPC is available for use.
        self.status = status
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeVpcsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        vpcs: List[DescribeVpcsResponseBodyVpcs] = None,
    ):
        # The maximum number of entries returned on a single page.
        self.max_results = max_results
        # The token that marks the end of the current returned page. If this parameter is empty, it indicates that you have retrieved all the data.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned. By default, this parameter is not returned.
        self.total_count = total_count
        # The list of VPCs that are available in the specified region.
        self.vpcs = vpcs

    def validate(self):
        if self.vpcs:
            for k in self.vpcs:
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Vpcs'] = []
        if self.vpcs is not None:
            for k in self.vpcs:
                result['Vpcs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k in m.get('Vpcs'):
                temp_model = DescribeVpcsResponseBodyVpcs()
                self.vpcs.append(temp_model.from_map(k))
        return self


class DescribeVpcsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVpcsResponseBody = None,
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
            temp_model = DescribeVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCaCertRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the Alibaba Cloud Service Mesh (ASM) instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetCaCertResponseBody(TeaModel):
    def __init__(
        self,
        ca_cert: str = None,
        request_id: str = None,
    ):
        # The Base64-encoded content of the CA certificate.
        self.ca_cert = ca_cert
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_cert is not None:
            result['CaCert'] = self.ca_cert
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCert') is not None:
            self.ca_cert = m.get('CaCert')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCaCertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCaCertResponseBody = None,
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
            temp_model = GetCaCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeploymentBySelectorRequest(TeaModel):
    def __init__(
        self,
        guest_cluster: str = None,
        label_selector: Dict[str, str] = None,
        limit: int = None,
        mark: str = None,
        name_space: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the cluster.
        self.guest_cluster = guest_cluster
        # The label selector information.
        self.label_selector = label_selector
        # The maximum number of returned data entries.
        self.limit = limit
        # The marker of data queried last time.
        self.mark = mark
        # The namespace.
        self.name_space = name_space
        # The ID of the Alibaba Cloud Service Mesh (ASM) instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster is not None:
            result['GuestCluster'] = self.guest_cluster
        if self.label_selector is not None:
            result['LabelSelector'] = self.label_selector
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.mark is not None:
            result['Mark'] = self.mark
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestCluster') is not None:
            self.guest_cluster = m.get('GuestCluster')
        if m.get('LabelSelector') is not None:
            self.label_selector = m.get('LabelSelector')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Mark') is not None:
            self.mark = m.get('Mark')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetDeploymentBySelectorShrinkRequest(TeaModel):
    def __init__(
        self,
        guest_cluster: str = None,
        label_selector_shrink: str = None,
        limit: int = None,
        mark: str = None,
        name_space: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the cluster.
        self.guest_cluster = guest_cluster
        # The label selector information.
        self.label_selector_shrink = label_selector_shrink
        # The maximum number of returned data entries.
        self.limit = limit
        # The marker of data queried last time.
        self.mark = mark
        # The namespace.
        self.name_space = name_space
        # The ID of the Alibaba Cloud Service Mesh (ASM) instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster is not None:
            result['GuestCluster'] = self.guest_cluster
        if self.label_selector_shrink is not None:
            result['LabelSelector'] = self.label_selector_shrink
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.mark is not None:
            result['Mark'] = self.mark
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestCluster') is not None:
            self.guest_cluster = m.get('GuestCluster')
        if m.get('LabelSelector') is not None:
            self.label_selector_shrink = m.get('LabelSelector')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Mark') is not None:
            self.mark = m.get('Mark')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetDeploymentBySelectorResponseBody(TeaModel):
    def __init__(
        self,
        deployment_name_list: List[bytes] = None,
        mark: str = None,
        request_id: str = None,
    ):
        # The queried workloads.
        self.deployment_name_list = deployment_name_list
        # The end-of-data marker.
        self.mark = mark
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_name_list is not None:
            result['DeploymentNameList'] = self.deployment_name_list
        if self.mark is not None:
            result['Mark'] = self.mark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentNameList') is not None:
            self.deployment_name_list = m.get('DeploymentNameList')
        if m.get('Mark') is not None:
            self.mark = m.get('Mark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeploymentBySelectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeploymentBySelectorResponseBody = None,
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
            temp_model = GetDeploymentBySelectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGrafanaDashboardUrlRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
        service_mesh_id: str = None,
        title: str = None,
    ):
        # The ID of the Container Service for Kubernetes (ACK) or serverless Kubernetes (ASK) cluster.
        self.k_8s_cluster_id = k_8s_cluster_id
        # The ID of the Alibaba Cloud Service Mesh (ASM) instance.
        self.service_mesh_id = service_mesh_id
        # The name of the dashboard.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetGrafanaDashboardUrlResponseBodyDashboards(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        # The name of the dashboard.
        self.title = title
        # The URL of the dashboard.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetGrafanaDashboardUrlResponseBody(TeaModel):
    def __init__(
        self,
        dashboards: List[GetGrafanaDashboardUrlResponseBodyDashboards] = None,
        request_id: str = None,
    ):
        # The information about the dashboard.
        self.dashboards = dashboards
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k in m.get('Dashboards'):
                temp_model = GetGrafanaDashboardUrlResponseBodyDashboards()
                self.dashboards.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGrafanaDashboardUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGrafanaDashboardUrlResponseBody = None,
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
            temp_model = GetGrafanaDashboardUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisteredServiceEndpointsRequest(TeaModel):
    def __init__(
        self,
        cluster_ids: str = None,
        name: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
        service_type: str = None,
    ):
        # The name of the registered service.
        self.cluster_ids = cluster_ids
        # The type of the registered service. Valid values:
        # 
        # *   `ServiceEntry`: indicates that the service is registered by creating a service entry.
        # *   `Kubernetes`: indicates that the service is registered on a Kubernetes cluster on the data plane.
        self.name = name
        # The IDs of clusters in the ASM instance. Separate multiple cluster IDs with commas (,).
        self.namespace = namespace
        # The name of the namespace.
        self.service_mesh_id = service_mesh_id
        # The endpoints of the registered service.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class GetRegisteredServiceEndpointsResponseBodyEndPointSliceEndpointsDetails(TeaModel):
    def __init__(
        self,
        address: str = None,
        hostname: str = None,
        pod_name: str = None,
        ports: List[int] = None,
        region: str = None,
        sidecar_injected: bool = None,
    ):
        # The port of the registered service.
        self.address = address
        # The ID of the region in which the registered service resides.
        self.hostname = hostname
        # The IP address of the registered service.
        self.pod_name = pod_name
        # The host name of the registered service.
        self.ports = ports
        # Indicates whether sidecar proxies are injected. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.region = region
        # The ID of the request.
        self.sidecar_injected = sidecar_injected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.region is not None:
            result['Region'] = self.region
        if self.sidecar_injected is not None:
            result['SidecarInjected'] = self.sidecar_injected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SidecarInjected') is not None:
            self.sidecar_injected = m.get('SidecarInjected')
        return self


class GetRegisteredServiceEndpointsResponseBodyEndPointSlice(TeaModel):
    def __init__(
        self,
        endpoints_details: List[GetRegisteredServiceEndpointsResponseBodyEndPointSliceEndpointsDetails] = None,
        location: str = None,
        namespace: str = None,
        service_name: str = None,
    ):
        # The name of the pod.
        self.endpoints_details = endpoints_details
        # The details of the endpoint of the registered service.
        self.location = location
        # The location of the registered service. Valid values:
        # 
        # *   `MESH_INTERNAL`: The service is deployed inside the ASM instance.
        # *   `MESH_EXTERNAL`: The service is deployed outside the ASM instance.
        self.namespace = namespace
        # The name of the namespace.
        self.service_name = service_name

    def validate(self):
        if self.endpoints_details:
            for k in self.endpoints_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EndpointsDetails'] = []
        if self.endpoints_details is not None:
            for k in self.endpoints_details:
                result['EndpointsDetails'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoints_details = []
        if m.get('EndpointsDetails') is not None:
            for k in m.get('EndpointsDetails'):
                temp_model = GetRegisteredServiceEndpointsResponseBodyEndPointSliceEndpointsDetails()
                self.endpoints_details.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GetRegisteredServiceEndpointsResponseBodyServiceEndpoints(TeaModel):
    def __init__(
        self,
        address: str = None,
        cluster_id: str = None,
    ):
        # The ID of the cluster on the data plane.
        self.address = address
        # The details of the endpoints of the registered service.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetRegisteredServiceEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        end_point_slice: GetRegisteredServiceEndpointsResponseBodyEndPointSlice = None,
        request_id: str = None,
        service_endpoints: List[GetRegisteredServiceEndpointsResponseBodyServiceEndpoints] = None,
    ):
        # The name of the registered service.
        self.end_point_slice = end_point_slice
        self.request_id = request_id
        # The IP address of the registered service.
        self.service_endpoints = service_endpoints

    def validate(self):
        if self.end_point_slice:
            self.end_point_slice.validate()
        if self.service_endpoints:
            for k in self.service_endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_point_slice is not None:
            result['EndPointSlice'] = self.end_point_slice.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceEndpoints'] = []
        if self.service_endpoints is not None:
            for k in self.service_endpoints:
                result['ServiceEndpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndPointSlice') is not None:
            temp_model = GetRegisteredServiceEndpointsResponseBodyEndPointSlice()
            self.end_point_slice = temp_model.from_map(m['EndPointSlice'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_endpoints = []
        if m.get('ServiceEndpoints') is not None:
            for k in m.get('ServiceEndpoints'):
                temp_model = GetRegisteredServiceEndpointsResponseBodyServiceEndpoints()
                self.service_endpoints.append(temp_model.from_map(k))
        return self


class GetRegisteredServiceEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRegisteredServiceEndpointsResponseBody = None,
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
            temp_model = GetRegisteredServiceEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisteredServiceNamespacesRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetRegisteredServiceNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        namespaces: List[str] = None,
        request_id: str = None,
    ):
        # The names of the queried namespaces.
        self.namespaces = namespaces
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRegisteredServiceNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRegisteredServiceNamespacesResponseBody = None,
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
            temp_model = GetRegisteredServiceNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSwimLaneDetailRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        service_mesh_id: str = None,
        swim_lane_name: str = None,
    ):
        # The name of the lane group.
        self.group_name = group_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The name of the lane.
        self.swim_lane_name = swim_lane_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.swim_lane_name is not None:
            result['SwimLaneName'] = self.swim_lane_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('SwimLaneName') is not None:
            self.swim_lane_name = m.get('SwimLaneName')
        return self


class GetSwimLaneDetailResponseBody(TeaModel):
    def __init__(
        self,
        ingress_rule: str = None,
        ingress_service: str = None,
        label_selector_key: str = None,
        label_selector_value: str = None,
        request_id: str = None,
        services_list: str = None,
    ):
        # The traffic routing rule that routes traffic to the lane by using the ingress gateway. The traffic routing rule contains one or more custom routes.
        self.ingress_rule = ingress_rule
        # This parameter is deprecated.
        self.ingress_service = ingress_service
        # Fixed value: **ASM_TRAFFIC_TAG**.
        self.label_selector_key = label_selector_key
        # The value of ASM_TRAFFIC_TAG.
        self.label_selector_value = label_selector_value
        # The ID of the request.
        self.request_id = request_id
        # A list of services associated with the lane.
        self.services_list = services_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_rule is not None:
            result['IngressRule'] = self.ingress_rule
        if self.ingress_service is not None:
            result['IngressService'] = self.ingress_service
        if self.label_selector_key is not None:
            result['LabelSelectorKey'] = self.label_selector_key
        if self.label_selector_value is not None:
            result['LabelSelectorValue'] = self.label_selector_value
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.services_list is not None:
            result['ServicesList'] = self.services_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressRule') is not None:
            self.ingress_rule = m.get('IngressRule')
        if m.get('IngressService') is not None:
            self.ingress_service = m.get('IngressService')
        if m.get('LabelSelectorKey') is not None:
            self.label_selector_key = m.get('LabelSelectorKey')
        if m.get('LabelSelectorValue') is not None:
            self.label_selector_value = m.get('LabelSelectorValue')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServicesList') is not None:
            self.services_list = m.get('ServicesList')
        return self


class GetSwimLaneDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSwimLaneDetailResponseBody = None,
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
            temp_model = GetSwimLaneDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSwimLaneGroupListRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ASM instance ID.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetSwimLaneGroupListResponseBodySwimLaneGroupList(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ingress_gateway_name: str = None,
        ingress_type: str = None,
        service_list: str = None,
    ):
        # The name of the lane group.
        self.group_name = group_name
        # The name of the ingress gateway.
        self.ingress_gateway_name = ingress_gateway_name
        # The ingress type. Traffic routing rules can be configured only in an ingress gateway.
        self.ingress_type = ingress_type
        # A list of services associated with the lane group.
        self.service_list = service_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ingress_gateway_name is not None:
            result['IngressGatewayName'] = self.ingress_gateway_name
        if self.ingress_type is not None:
            result['IngressType'] = self.ingress_type
        if self.service_list is not None:
            result['ServiceList'] = self.service_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IngressGatewayName') is not None:
            self.ingress_gateway_name = m.get('IngressGatewayName')
        if m.get('IngressType') is not None:
            self.ingress_type = m.get('IngressType')
        if m.get('ServiceList') is not None:
            self.service_list = m.get('ServiceList')
        return self


class GetSwimLaneGroupListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        swim_lane_group_list: List[GetSwimLaneGroupListResponseBodySwimLaneGroupList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the lane groups.
        self.swim_lane_group_list = swim_lane_group_list

    def validate(self):
        if self.swim_lane_group_list:
            for k in self.swim_lane_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SwimLaneGroupList'] = []
        if self.swim_lane_group_list is not None:
            for k in self.swim_lane_group_list:
                result['SwimLaneGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.swim_lane_group_list = []
        if m.get('SwimLaneGroupList') is not None:
            for k in m.get('SwimLaneGroupList'):
                temp_model = GetSwimLaneGroupListResponseBodySwimLaneGroupList()
                self.swim_lane_group_list.append(temp_model.from_map(k))
        return self


class GetSwimLaneGroupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSwimLaneGroupListResponseBody = None,
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
            temp_model = GetSwimLaneGroupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSwimLaneListRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        service_mesh_id: str = None,
    ):
        # The name of the lane group.
        self.group_name = group_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetSwimLaneListResponseBodySwimLaneList(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ingress_rule: str = None,
        ingress_service: str = None,
        label_selector_key: str = None,
        label_selector_value: str = None,
        name: str = None,
        service_list: str = None,
    ):
        # The name of the lane group.
        self.group_name = group_name
        # The traffic routing rule associated with the lane.
        self.ingress_rule = ingress_rule
        # This parameter is deprecated.
        self.ingress_service = ingress_service
        # The label key of the associated service workload. Fixed value: `ASM_TRAFFIC_TAG`.
        self.label_selector_key = label_selector_key
        # The label value of the associated service workload.``
        self.label_selector_value = label_selector_value
        # The name of the lane.
        self.name = name
        # A list of services associated with the lane.
        self.service_list = service_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ingress_rule is not None:
            result['IngressRule'] = self.ingress_rule
        if self.ingress_service is not None:
            result['IngressService'] = self.ingress_service
        if self.label_selector_key is not None:
            result['LabelSelectorKey'] = self.label_selector_key
        if self.label_selector_value is not None:
            result['LabelSelectorValue'] = self.label_selector_value
        if self.name is not None:
            result['Name'] = self.name
        if self.service_list is not None:
            result['ServiceList'] = self.service_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IngressRule') is not None:
            self.ingress_rule = m.get('IngressRule')
        if m.get('IngressService') is not None:
            self.ingress_service = m.get('IngressService')
        if m.get('LabelSelectorKey') is not None:
            self.label_selector_key = m.get('LabelSelectorKey')
        if m.get('LabelSelectorValue') is not None:
            self.label_selector_value = m.get('LabelSelectorValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceList') is not None:
            self.service_list = m.get('ServiceList')
        return self


class GetSwimLaneListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        swim_lane_list: List[GetSwimLaneListResponseBodySwimLaneList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # A list of all the lanes in the lane group.
        self.swim_lane_list = swim_lane_list

    def validate(self):
        if self.swim_lane_list:
            for k in self.swim_lane_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SwimLaneList'] = []
        if self.swim_lane_list is not None:
            for k in self.swim_lane_list:
                result['SwimLaneList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.swim_lane_list = []
        if m.get('SwimLaneList') is not None:
            for k in m.get('SwimLaneList'):
                temp_model = GetSwimLaneListResponseBodySwimLaneList()
                self.swim_lane_list.append(temp_model.from_map(k))
        return self


class GetSwimLaneListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSwimLaneListResponseBody = None,
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
            temp_model = GetSwimLaneListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVmAppMeshInfoRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetVmAppMeshInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The returned information.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVmAppMeshInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVmAppMeshInfoResponseBody = None,
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
            temp_model = GetVmAppMeshInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVmMetaRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        service_account: str = None,
        service_mesh_id: str = None,
        trust_domain: str = None,
    ):
        # The namespace. This parameter is valid only after you set the Namespace and the ServiceAccount parameters.
        self.namespace = namespace
        # The service account. This parameter is valid only after you set the Namespace and the ServiceAccount parameters.
        self.service_account = service_account
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The trusted domain. Default value: cluster.local. This parameter is valid only after you set the Namespace and the ServiceAccount parameters.
        self.trust_domain = trust_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_account is not None:
            result['ServiceAccount'] = self.service_account
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.trust_domain is not None:
            result['TrustDomain'] = self.trust_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceAccount') is not None:
            self.service_account = m.get('ServiceAccount')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('TrustDomain') is not None:
            self.trust_domain = m.get('TrustDomain')
        return self


class GetVmMetaResponseBodyVmMetaInfo(TeaModel):
    def __init__(
        self,
        envoy_env_content: str = None,
        hosts_content: str = None,
        token_content: str = None,
    ):
        # The content of the EnvoyEnv file.
        self.envoy_env_content = envoy_env_content
        # The content of the hosts file.
        self.hosts_content = hosts_content
        # The content of the Token file.
        self.token_content = token_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.envoy_env_content is not None:
            result['EnvoyEnvContent'] = self.envoy_env_content
        if self.hosts_content is not None:
            result['HostsContent'] = self.hosts_content
        if self.token_content is not None:
            result['TokenContent'] = self.token_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvoyEnvContent') is not None:
            self.envoy_env_content = m.get('EnvoyEnvContent')
        if m.get('HostsContent') is not None:
            self.hosts_content = m.get('HostsContent')
        if m.get('TokenContent') is not None:
            self.token_content = m.get('TokenContent')
        return self


class GetVmMetaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vm_meta_info: GetVmMetaResponseBodyVmMetaInfo = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The metadata that is required to add a non-containerized application to the ASM instance.
        self.vm_meta_info = vm_meta_info

    def validate(self):
        if self.vm_meta_info:
            self.vm_meta_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vm_meta_info is not None:
            result['VmMetaInfo'] = self.vm_meta_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VmMetaInfo') is not None:
            temp_model = GetVmMetaResponseBodyVmMetaInfo()
            self.vm_meta_info = temp_model.from_map(m['VmMetaInfo'])
        return self


class GetVmMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVmMetaResponseBody = None,
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
            temp_model = GetVmMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantUserPermissionsRequest(TeaModel):
    def __init__(
        self,
        permissions: str = None,
        sub_account_user_id: str = None,
        sub_account_user_ids: List[str] = None,
    ):
        # The permissions that are granted to an entity. The content is a string that consists of JSON arrays. You must specify all permissions that you want to grant to an entity. You can add or remove permissions by modifying the content. Field definition of the sample code:
        # 
        # *   `IsCustom`: a parameter that is required by the system. Set the value to `true`.
        # *   `Cluster`: the ID of the Alibaba Cloud Service Mesh (ASM) instance.
        # *   `RoleName`: the name of the permissions. Valid values: `istio-admin`, `istio-ops`, and `istio-readonly`. A value of istio-admin indicates the permissions of ASM administrators. A value of istio-ops indicates the permissions of ASM restricted users. A value of istio-readonly indicates the read-only permissions.
        # *   `IsRamRole`: the entity to which you want to grant the permissions. To grant the permissions to a RAM role, set the value to `true`. Otherwise, set the value to `false`.
        self.permissions = permissions
        # The ID of the RAM user or RAM role.
        self.sub_account_user_id = sub_account_user_id
        # The ID list of the RAM user or RAM role.
        self.sub_account_user_ids = sub_account_user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.sub_account_user_id is not None:
            result['SubAccountUserId'] = self.sub_account_user_id
        if self.sub_account_user_ids is not None:
            result['SubAccountUserIds'] = self.sub_account_user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('SubAccountUserId') is not None:
            self.sub_account_user_id = m.get('SubAccountUserId')
        if m.get('SubAccountUserIds') is not None:
            self.sub_account_user_ids = m.get('SubAccountUserIds')
        return self


class GrantUserPermissionsShrinkRequest(TeaModel):
    def __init__(
        self,
        permissions: str = None,
        sub_account_user_id: str = None,
        sub_account_user_ids_shrink: str = None,
    ):
        # The permissions that are granted to an entity. The content is a string that consists of JSON arrays. You must specify all permissions that you want to grant to an entity. You can add or remove permissions by modifying the content. Field definition of the sample code:
        # 
        # *   `IsCustom`: a parameter that is required by the system. Set the value to `true`.
        # *   `Cluster`: the ID of the Alibaba Cloud Service Mesh (ASM) instance.
        # *   `RoleName`: the name of the permissions. Valid values: `istio-admin`, `istio-ops`, and `istio-readonly`. A value of istio-admin indicates the permissions of ASM administrators. A value of istio-ops indicates the permissions of ASM restricted users. A value of istio-readonly indicates the read-only permissions.
        # *   `IsRamRole`: the entity to which you want to grant the permissions. To grant the permissions to a RAM role, set the value to `true`. Otherwise, set the value to `false`.
        self.permissions = permissions
        # The ID of the RAM user or RAM role.
        self.sub_account_user_id = sub_account_user_id
        # The ID list of the RAM user or RAM role.
        self.sub_account_user_ids_shrink = sub_account_user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permissions is not None:
            result['Permissions'] = self.permissions
        if self.sub_account_user_id is not None:
            result['SubAccountUserId'] = self.sub_account_user_id
        if self.sub_account_user_ids_shrink is not None:
            result['SubAccountUserIds'] = self.sub_account_user_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Permissions') is not None:
            self.permissions = m.get('Permissions')
        if m.get('SubAccountUserId') is not None:
            self.sub_account_user_id = m.get('SubAccountUserId')
        if m.get('SubAccountUserIds') is not None:
            self.sub_account_user_ids_shrink = m.get('SubAccountUserIds')
        return self


class GrantUserPermissionsResponseBody(TeaModel):
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


class GrantUserPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GrantUserPermissionsResponseBody = None,
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
            temp_model = GrantUserPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApiServerEipResourceRequest(TeaModel):
    def __init__(
        self,
        api_server_eip_id: str = None,
        operation: str = None,
        service_mesh_id: str = None,
    ):
        # The ID of the EIP.
        self.api_server_eip_id = api_server_eip_id
        # The type of the operation. Valid values:
        # 
        # *   `UnBindEip`: disassociates an EIP from the API server.
        # *   `BindEip`: associates an EIP with the API server.
        self.operation = operation
        # The ID of the Alibaba Cloud Service Mesh (ASM) instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_eip_id is not None:
            result['ApiServerEipId'] = self.api_server_eip_id
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiServerEipId') is not None:
            self.api_server_eip_id = m.get('ApiServerEipId')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class ModifyApiServerEipResourceResponseBody(TeaModel):
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


class ModifyApiServerEipResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyApiServerEipResourceResponseBody = None,
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
            temp_model = ModifyApiServerEipResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyServiceMeshNameRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        service_mesh_id: str = None,
    ):
        # The new name of the ASM instance.
        self.name = name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class ModifyServiceMeshNameResponseBody(TeaModel):
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


class ModifyServiceMeshNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyServiceMeshNameResponseBody = None,
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
            temp_model = ModifyServiceMeshNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReActivateAuditRequest(TeaModel):
    def __init__(
        self,
        enable_audit: bool = None,
        service_mesh_id: str = None,
    ):
        # Specifies whether to recreate a project that is used to store audit logs. Valid values:
        # 
        # *   true: recreates a project.
        # *   false: does not recreate a project.
        self.enable_audit = enable_audit
        # The ID of the Alibaba Cloud Service Mesh (ASM) instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class ReActivateAuditResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The name of the project that is used to store audit logs.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReActivateAuditResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReActivateAuditResponseBody = None,
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
            temp_model = ReActivateAuditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClusterFromServiceMeshRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        reserve_namespace: bool = None,
        service_mesh_id: str = None,
    ):
        self.cluster_id = cluster_id
        # 移除集群时，保留istio-system 命名空间
        self.reserve_namespace = reserve_namespace
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.reserve_namespace is not None:
            result['ReserveNamespace'] = self.reserve_namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ReserveNamespace') is not None:
            self.reserve_namespace = m.get('ReserveNamespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class RemoveClusterFromServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveClusterFromServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveClusterFromServiceMeshResponseBody = None,
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
            temp_model = RemoveClusterFromServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveVMFromServiceMeshRequest(TeaModel):
    def __init__(
        self,
        ecs_id: str = None,
        service_mesh_id: str = None,
    ):
        # The ID of the VM.
        self.ecs_id = ecs_id
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class RemoveVMFromServiceMeshResponseBody(TeaModel):
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


class RemoveVMFromServiceMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveVMFromServiceMeshResponseBody = None,
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
            temp_model = RemoveVMFromServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeKubeconfigRequest(TeaModel):
    def __init__(
        self,
        private_ip_address: bool = None,
        service_mesh_id: str = None,
    ):
        # Specifies whether to return the kubeconfig file for private access.
        # 
        # *   `true`: returns the kubeconfig file for private access.
        # *   `false`: returns the kubeconfig file for public access.
        self.private_ip_address = private_ip_address
        # The ID of the ASM instance for which you want to revoke a kubeconfig file.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class RevokeKubeconfigResponseBody(TeaModel):
    def __init__(
        self,
        kubeconfig: str = None,
        request_id: str = None,
    ):
        # The new kubeconfig file generated.
        self.kubeconfig = kubeconfig
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubeconfig is not None:
            result['Kubeconfig'] = self.kubeconfig
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Kubeconfig') is not None:
            self.kubeconfig = m.get('Kubeconfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RevokeKubeconfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeKubeconfigResponseBody = None,
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
            temp_model = RevokeKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateASMGatewayRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        istio_gateway_name: str = None,
        service_mesh_id: str = None,
    ):
        # The new YAML content of the ASM gateway.
        self.body = body
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpdateASMGatewayResponseBody(TeaModel):
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


class UpdateASMGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateASMGatewayResponseBody = None,
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
            temp_model = UpdateASMGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateASMGatewayImportedServicesRequest(TeaModel):
    def __init__(
        self,
        asmgateway_name: str = None,
        service_mesh_id: str = None,
        service_names: str = None,
        service_namespace: str = None,
    ):
        # The name of the ASM gateway.
        self.asmgateway_name = asmgateway_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The names of the services. Separate multiple service names with commas (,). Example: reviews,sleep.
        self.service_names = service_names
        # The namespace in which the service resides.
        self.service_namespace = service_namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asmgateway_name is not None:
            result['ASMGatewayName'] = self.asmgateway_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.service_names is not None:
            result['ServiceNames'] = self.service_names
        if self.service_namespace is not None:
            result['ServiceNamespace'] = self.service_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ASMGatewayName') is not None:
            self.asmgateway_name = m.get('ASMGatewayName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServiceNames') is not None:
            self.service_names = m.get('ServiceNames')
        if m.get('ServiceNamespace') is not None:
            self.service_namespace = m.get('ServiceNamespace')
        return self


class UpdateASMGatewayImportedServicesResponseBody(TeaModel):
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


class UpdateASMGatewayImportedServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateASMGatewayImportedServicesResponseBody = None,
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
            temp_model = UpdateASMGatewayImportedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateASMNamespaceFromGuestClusterRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
        service_mesh_id: str = None,
    ):
        # The ID of the Kubernetes cluster whose namespace information you want to synchronize to ASM. The Kubernetes cluster is added to the ASM instance that is specified by the ServiceMeshId parameter.
        self.k_8s_cluster_id = k_8s_cluster_id
        # The ASM instance ID.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpdateASMNamespaceFromGuestClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateASMNamespaceFromGuestClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateASMNamespaceFromGuestClusterResponseBody = None,
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
            temp_model = UpdateASMNamespaceFromGuestClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsDelegate(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
    ):
        # The name of the virtual service.
        self.name = name
        # The namespace to which the virtual service belongs.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbortPercentage(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The percentage of requests that are aborted with the specified error code, which is expressed as a decimal.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbort(TeaModel):
    def __init__(
        self,
        http_status: int = None,
        percentage: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbortPercentage = None,
    ):
        # The HTTP status code.
        self.http_status = http_status
        # The percentage of requests that are aborted with the specified error code.
        self.percentage = percentage

    def validate(self):
        if self.percentage:
            self.percentage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status is not None:
            result['HttpStatus'] = self.http_status
        if self.percentage is not None:
            result['Percentage'] = self.percentage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')
        if m.get('Percentage') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbortPercentage()
            self.percentage = temp_model.from_map(m['Percentage'])
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelayPercentage(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The percentage of requests to which the delay fault is injected, which is expressed as a decimal.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelay(TeaModel):
    def __init__(
        self,
        fixed_delay: str = None,
        percentage: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelayPercentage = None,
    ):
        # The fixed duration for request delay.
        self.fixed_delay = fixed_delay
        # The percentage of requests to which the delay fault is injected.
        self.percentage = percentage

    def validate(self):
        if self.percentage:
            self.percentage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fixed_delay is not None:
            result['FixedDelay'] = self.fixed_delay
        if self.percentage is not None:
            result['Percentage'] = self.percentage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedDelay') is not None:
            self.fixed_delay = m.get('FixedDelay')
        if m.get('Percentage') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelayPercentage()
            self.percentage = temp_model.from_map(m['Percentage'])
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFault(TeaModel):
    def __init__(
        self,
        abort: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbort = None,
        delay: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelay = None,
    ):
        # The configurations for aborting requests with specified error codes.
        self.abort = abort
        # The duration to delay a request.
        self.delay = delay

    def validate(self):
        if self.abort:
            self.abort.validate()
        if self.delay:
            self.delay.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abort is not None:
            result['Abort'] = self.abort.to_map()
        if self.delay is not None:
            result['Delay'] = self.delay.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abort') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultAbort()
            self.abort = temp_model.from_map(m['Abort'])
        if m.get('Delay') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFaultDelay()
            self.delay = temp_model.from_map(m['Delay'])
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsHTTPRedirect(TeaModel):
    def __init__(
        self,
        authority: str = None,
        redirect_code: int = None,
        uri: str = None,
    ):
        # The value to be used to overwrite the value of the Authority or Host header during redirection.
        self.authority = authority
        # The HTTP status code to be used to indicate URL redirection. Default value: 301.
        self.redirect_code = redirect_code
        # The value to be used to overwrite the URL path during redirection.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.redirect_code is not None:
            result['RedirectCode'] = self.redirect_code
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('RedirectCode') is not None:
            self.redirect_code = m.get('RedirectCode')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirror(TeaModel):
    def __init__(
        self,
        host: str = None,
        subset: str = None,
    ):
        # The name of the service defined in the service registry.
        self.host = host
        # The name of the service subset.
        self.subset = subset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.subset is not None:
            result['Subset'] = self.subset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Subset') is not None:
            self.subset = m.get('Subset')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirrorPercentage(TeaModel):
    def __init__(
        self,
        value: float = None,
    ):
        # The percentage of requests that are mirrored to another destination except for the original destination, which is expressed as a decimal.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetriesRetryRemoteLocalities(TeaModel):
    def __init__(
        self,
        value: bool = None,
    ):
        # Specifies whether to allow retries to other localities. Valid values:
        # 
        # *   `true`
        # *   `false`
        # 
        # Default value: `false`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetries(TeaModel):
    def __init__(
        self,
        attempts: int = None,
        per_try_timeout: str = None,
        retry_on: str = None,
        retry_remote_localities: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetriesRetryRemoteLocalities = None,
    ):
        # The number of retries allowed for a request.
        self.attempts = attempts
        # The timeout period for each retry.
        self.per_try_timeout = per_try_timeout
        # The condition for retries. Example: `connect-failure,refused-stream,503`.
        self.retry_on = retry_on
        # Specifies whether to allow retries to other localities.
        self.retry_remote_localities = retry_remote_localities

    def validate(self):
        if self.retry_remote_localities:
            self.retry_remote_localities.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempts is not None:
            result['Attempts'] = self.attempts
        if self.per_try_timeout is not None:
            result['PerTryTimeout'] = self.per_try_timeout
        if self.retry_on is not None:
            result['RetryOn'] = self.retry_on
        if self.retry_remote_localities is not None:
            result['RetryRemoteLocalities'] = self.retry_remote_localities.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attempts') is not None:
            self.attempts = m.get('Attempts')
        if m.get('PerTryTimeout') is not None:
            self.per_try_timeout = m.get('PerTryTimeout')
        if m.get('RetryOn') is not None:
            self.retry_on = m.get('RetryOn')
        if m.get('RetryRemoteLocalities') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetriesRetryRemoteLocalities()
            self.retry_remote_localities = temp_model.from_map(m['RetryRemoteLocalities'])
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRewrite(TeaModel):
    def __init__(
        self,
        authority: str = None,
        uri: str = None,
    ):
        # The value to be used to overwrite the value of the Authority or Host header.
        self.authority = authority
        # The value to be used to overwrite the path or prefix of the URI.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptions(TeaModel):
    def __init__(
        self,
        delegate: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsDelegate = None,
        fault: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFault = None,
        httpredirect: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsHTTPRedirect = None,
        mirror: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirror = None,
        mirror_percentage: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirrorPercentage = None,
        retries: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetries = None,
        rewrite: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRewrite = None,
        timeout: str = None,
    ):
        # The virtual service that defines traffic routing.
        self.delegate = delegate
        # The configurations of fault injection.
        self.fault = fault
        # The HTTP redirection rule.
        self.httpredirect = httpredirect
        # The configurations for mirroring HTTP traffic to another destination in addition to forwarding requests to the specified destination.
        self.mirror = mirror
        # The percentage of requests that are mirrored to another destination except for the original destination.
        self.mirror_percentage = mirror_percentage
        # The configurations of retries for failed requests.
        self.retries = retries
        # The configurations for rewriting the virtual service.
        self.rewrite = rewrite
        # The timeout period for requests.
        self.timeout = timeout

    def validate(self):
        if self.delegate:
            self.delegate.validate()
        if self.fault:
            self.fault.validate()
        if self.httpredirect:
            self.httpredirect.validate()
        if self.mirror:
            self.mirror.validate()
        if self.mirror_percentage:
            self.mirror_percentage.validate()
        if self.retries:
            self.retries.validate()
        if self.rewrite:
            self.rewrite.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delegate is not None:
            result['Delegate'] = self.delegate.to_map()
        if self.fault is not None:
            result['Fault'] = self.fault.to_map()
        if self.httpredirect is not None:
            result['HTTPRedirect'] = self.httpredirect.to_map()
        if self.mirror is not None:
            result['Mirror'] = self.mirror.to_map()
        if self.mirror_percentage is not None:
            result['MirrorPercentage'] = self.mirror_percentage.to_map()
        if self.retries is not None:
            result['Retries'] = self.retries.to_map()
        if self.rewrite is not None:
            result['Rewrite'] = self.rewrite.to_map()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delegate') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsDelegate()
            self.delegate = temp_model.from_map(m['Delegate'])
        if m.get('Fault') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsFault()
            self.fault = temp_model.from_map(m['Fault'])
        if m.get('HTTPRedirect') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsHTTPRedirect()
            self.httpredirect = temp_model.from_map(m['HTTPRedirect'])
        if m.get('Mirror') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirror()
            self.mirror = temp_model.from_map(m['Mirror'])
        if m.get('MirrorPercentage') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsMirrorPercentage()
            self.mirror_percentage = temp_model.from_map(m['MirrorPercentage'])
        if m.get('Retries') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRetries()
            self.retries = temp_model.from_map(m['Retries'])
        if m.get('Rewrite') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsRewrite()
            self.rewrite = temp_model.from_map(m['Rewrite'])
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequestHeaders(TeaModel):
    def __init__(
        self,
        matching_content: str = None,
        matching_mode: str = None,
        name: str = None,
    ):
        # The header value to be matched.
        self.matching_content = matching_content
        # The matching mode for the header value. Valid values:
        # 
        # *   `exact`: exact match
        # *   `prefix`: match by prefix
        # *   `regex`: match by regular expression
        self.matching_mode = matching_mode
        # The header key to be matched.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.matching_content is not None:
            result['MatchingContent'] = self.matching_content
        if self.matching_mode is not None:
            result['MatchingMode'] = self.matching_mode
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchingContent') is not None:
            self.matching_content = m.get('MatchingContent')
        if m.get('MatchingMode') is not None:
            self.matching_mode = m.get('MatchingMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequestTLSMatchAttributes(TeaModel):
    def __init__(
        self,
        snihosts: List[str] = None,
        tlsport: int = None,
    ):
        # The Server Name Indication (SNI) values to be matched.
        self.snihosts = snihosts
        # The TLS port.
        self.tlsport = tlsport

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snihosts is not None:
            result['SNIHosts'] = self.snihosts
        if self.tlsport is not None:
            result['TLSPort'] = self.tlsport
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SNIHosts') is not None:
            self.snihosts = m.get('SNIHosts')
        if m.get('TLSPort') is not None:
            self.tlsport = m.get('TLSPort')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequestURI(TeaModel):
    def __init__(
        self,
        matching_content: str = None,
        matching_mode: str = None,
    ):
        # The content to be matched.
        self.matching_content = matching_content
        # The matching mode for the routing rule. Valid values:
        # 
        # *   `exact`: exact match
        # *   `prefix`: match by prefix
        # *   `regex`: match by regular expression
        self.matching_mode = matching_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.matching_content is not None:
            result['MatchingContent'] = self.matching_content
        if self.matching_mode is not None:
            result['MatchingMode'] = self.matching_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchingContent') is not None:
            self.matching_content = m.get('MatchingContent')
        if m.get('MatchingMode') is not None:
            self.matching_mode = m.get('MatchingMode')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequest(TeaModel):
    def __init__(
        self,
        headers: List[UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequestHeaders] = None,
        ports: List[int] = None,
        tlsmatch_attributes: List[UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequestTLSMatchAttributes] = None,
        uri: UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequestURI = None,
    ):
        # The request headers to be matched.
        self.headers = headers
        # The ports.
        self.ports = ports
        # The matching rule for Transport Layer Security (TLS) traffic.
        self.tlsmatch_attributes = tlsmatch_attributes
        # The matching rule for URIs.
        self.uri = uri

    def validate(self):
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()
        if self.tlsmatch_attributes:
            for k in self.tlsmatch_attributes:
                if k:
                    k.validate()
        if self.uri:
            self.uri.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Headers'] = []
        if self.headers is not None:
            for k in self.headers:
                result['Headers'].append(k.to_map() if k else None)
        if self.ports is not None:
            result['Ports'] = self.ports
        result['TLSMatchAttributes'] = []
        if self.tlsmatch_attributes is not None:
            for k in self.tlsmatch_attributes:
                result['TLSMatchAttributes'].append(k.to_map() if k else None)
        if self.uri is not None:
            result['URI'] = self.uri.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.headers = []
        if m.get('Headers') is not None:
            for k in m.get('Headers'):
                temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequestHeaders()
                self.headers.append(temp_model.from_map(k))
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        self.tlsmatch_attributes = []
        if m.get('TLSMatchAttributes') is not None:
            for k in m.get('TLSMatchAttributes'):
                temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequestTLSMatchAttributes()
                self.tlsmatch_attributes.append(temp_model.from_map(k))
        if m.get('URI') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequestURI()
            self.uri = temp_model.from_map(m['URI'])
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestinationPort(TeaModel):
    def __init__(
        self,
        number: int = None,
    ):
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestination(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestinationPort = None,
        subset: str = None,
    ):
        # The name of the service defined in the service registry.
        self.host = host
        self.port = port
        # The name of the service subset.
        self.subset = subset

    def validate(self):
        if self.port:
            self.port.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port.to_map()
        if self.subset is not None:
            result['Subset'] = self.subset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestinationPort()
            self.port = temp_model.from_map(m['Port'])
        if m.get('Subset') is not None:
            self.subset = m.get('Subset')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinations(TeaModel):
    def __init__(
        self,
        destination: UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestination = None,
        weight: int = None,
    ):
        # The unique endpoint of the destination service to which the specified requests are sent.
        self.destination = destination
        # The weight of the service subset.
        self.weight = weight

    def validate(self):
        if self.destination:
            self.destination.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination.to_map()
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestination()
            self.destination = temp_model.from_map(m['Destination'])
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateIstioGatewayRoutesRequestGatewayRoute(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
        httpadvanced_options: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptions = None,
        match_request: UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequest = None,
        namespace: str = None,
        raw_vsroute: Any = None,
        route_destinations: List[UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinations] = None,
        route_name: str = None,
        route_type: str = None,
    ):
        self.domains = domains
        # The advanced settings for routing HTTP traffic.
        self.httpadvanced_options = httpadvanced_options
        # The matching rules for traffic routing.
        self.match_request = match_request
        # The namespace in which the destination service resides.
        self.namespace = namespace
        self.raw_vsroute = raw_vsroute
        # The endpoints of destination services for Layer 4 weighted routing.
        self.route_destinations = route_destinations
        # The name of the routing rule.
        self.route_name = route_name
        # The type of the traffic to be routed. Valid values: `HTTP`, `TLS`, and `TCP`.
        self.route_type = route_type

    def validate(self):
        if self.httpadvanced_options:
            self.httpadvanced_options.validate()
        if self.match_request:
            self.match_request.validate()
        if self.route_destinations:
            for k in self.route_destinations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.httpadvanced_options is not None:
            result['HTTPAdvancedOptions'] = self.httpadvanced_options.to_map()
        if self.match_request is not None:
            result['MatchRequest'] = self.match_request.to_map()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.raw_vsroute is not None:
            result['RawVSRoute'] = self.raw_vsroute
        result['RouteDestinations'] = []
        if self.route_destinations is not None:
            for k in self.route_destinations:
                result['RouteDestinations'].append(k.to_map() if k else None)
        if self.route_name is not None:
            result['RouteName'] = self.route_name
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('HTTPAdvancedOptions') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptions()
            self.httpadvanced_options = temp_model.from_map(m['HTTPAdvancedOptions'])
        if m.get('MatchRequest') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequest()
            self.match_request = temp_model.from_map(m['MatchRequest'])
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RawVSRoute') is not None:
            self.raw_vsroute = m.get('RawVSRoute')
        self.route_destinations = []
        if m.get('RouteDestinations') is not None:
            for k in m.get('RouteDestinations'):
                temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinations()
                self.route_destinations.append(temp_model.from_map(k))
        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        return self


class UpdateIstioGatewayRoutesRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        gateway_route: UpdateIstioGatewayRoutesRequestGatewayRoute = None,
        istio_gateway_name: str = None,
        priority: int = None,
        service_mesh_id: str = None,
        status: int = None,
    ):
        # The description of the routing rule.
        self.description = description
        # The information about the routing rule to be updated for the ASM gateway.
        self.gateway_route = gateway_route
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The priority of the routing rule. The value of this parameter is an integer. A smaller value indicates a higher priority.
        self.priority = priority
        # The ASM instance ID.
        self.service_mesh_id = service_mesh_id
        # The status of the routing rule. Valid values:
        # 
        # *   `0`: The routing rule is valid.
        # *   `1`: The routing rule is invalid.
        # *   `2`: An error occurs during the creation or update of the routing rule.
        self.status = status

    def validate(self):
        if self.gateway_route:
            self.gateway_route.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gateway_route is not None:
            result['GatewayRoute'] = self.gateway_route.to_map()
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GatewayRoute') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRoute()
            self.gateway_route = temp_model.from_map(m['GatewayRoute'])
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateIstioGatewayRoutesShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        gateway_route_shrink: str = None,
        istio_gateway_name: str = None,
        priority: int = None,
        service_mesh_id: str = None,
        status: int = None,
    ):
        # The description of the routing rule.
        self.description = description
        # The information about the routing rule to be updated for the ASM gateway.
        self.gateway_route_shrink = gateway_route_shrink
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The priority of the routing rule. The value of this parameter is an integer. A smaller value indicates a higher priority.
        self.priority = priority
        # The ASM instance ID.
        self.service_mesh_id = service_mesh_id
        # The status of the routing rule. Valid values:
        # 
        # *   `0`: The routing rule is valid.
        # *   `1`: The routing rule is invalid.
        # *   `2`: An error occurs during the creation or update of the routing rule.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.gateway_route_shrink is not None:
            result['GatewayRoute'] = self.gateway_route_shrink
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GatewayRoute') is not None:
            self.gateway_route_shrink = m.get('GatewayRoute')
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateIstioGatewayRoutesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateIstioGatewayRoutesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIstioGatewayRoutesResponseBody = None,
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
            temp_model = UpdateIstioGatewayRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIstioInjectionConfigRequest(TeaModel):
    def __init__(
        self,
        enable_istio_injection: bool = None,
        enable_sidecar_set_injection: bool = None,
        istio_rev: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        # Specifies whether to enable Istio automatic sidecar injection.
        self.enable_istio_injection = enable_istio_injection
        # Specifies whether to enable automatic sidecar injection by using SidecarSet.
        self.enable_sidecar_set_injection = enable_sidecar_set_injection
        self.istio_rev = istio_rev
        # The namespace for which you want to modify the sidecar injection setting.
        self.namespace = namespace
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_istio_injection is not None:
            result['EnableIstioInjection'] = self.enable_istio_injection
        if self.enable_sidecar_set_injection is not None:
            result['EnableSidecarSetInjection'] = self.enable_sidecar_set_injection
        if self.istio_rev is not None:
            result['IstioRev'] = self.istio_rev
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableIstioInjection') is not None:
            self.enable_istio_injection = m.get('EnableIstioInjection')
        if m.get('EnableSidecarSetInjection') is not None:
            self.enable_sidecar_set_injection = m.get('EnableSidecarSetInjection')
        if m.get('IstioRev') is not None:
            self.istio_rev = m.get('IstioRev')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpdateIstioInjectionConfigResponseBody(TeaModel):
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


class UpdateIstioInjectionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIstioInjectionConfigResponseBody = None,
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
            temp_model = UpdateIstioInjectionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIstioRouteAdditionalStatusRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        istio_gateway_name: str = None,
        priority: int = None,
        route_name: str = None,
        service_mesh_id: str = None,
        status: int = None,
    ):
        # The description of the routing rule.
        self.description = description
        # The name of the ASM gateway.
        self.istio_gateway_name = istio_gateway_name
        # The priority of the routing rule. The value of this parameter is an integer. A smaller value indicates a higher priority.
        self.priority = priority
        # The name of the routing rule.
        self.route_name = route_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The status of the routing rule. Valid values:
        # 
        # *   `0`: The routing rule is valid.
        # *   `1`: The routing rule is invalid.
        # *   `2`: An error occurs during the creation or update of the routing rule.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.istio_gateway_name is not None:
            result['IstioGatewayName'] = self.istio_gateway_name
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.route_name is not None:
            result['RouteName'] = self.route_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IstioGatewayName') is not None:
            self.istio_gateway_name = m.get('IstioGatewayName')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateIstioRouteAdditionalStatusResponseBody(TeaModel):
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


class UpdateIstioRouteAdditionalStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateIstioRouteAdditionalStatusResponseBody = None,
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
            temp_model = UpdateIstioRouteAdditionalStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMeshCRAggregationRequest(TeaModel):
    def __init__(
        self,
        cpulimit: str = None,
        cpurequirement: str = None,
        enabled: bool = None,
        memory_limit: str = None,
        memory_requirement: str = None,
        service_mesh_id: str = None,
        use_public_api_server: bool = None,
    ):
        # The maximum number of CPU cores that are available for the components installed in the ACK cluster on the data plane if you enable the Kubernetes API to access Istio resources in the ASM instance. You can specify the parameter value in the standard quantity representation used by Kubernetes.
        self.cpulimit = cpulimit
        # The number of CPU cores that are requested by the components installed in the Container Service for Kubernetes (ACK) cluster on the data plane if you enable the Kubernetes API to access Istio resources in the ASM instance. You can specify the parameter value in the standard quantity representation used by Kubernetes.
        self.cpurequirement = cpurequirement
        # Specifies whether to enable the Kubernetes API on the data plane to access Istio resources in the ASM instance. Valid values:
        # 
        # *   `true`: enables the Kubernetes API to access Istio resources in the ASM instance.
        # *   `false`: does not enable the Kubernetes API to access Istio resources in the ASM instance.
        self.enabled = enabled
        # The maximum size of the memory that is available for the components installed in the ACK cluster on the data plane if you enable the Kubernetes API to access Istio resources in the ASM instance. You can specify the parameter value in the standard quantity representation used by Kubernetes. 1 Mi equals 1,024 KB.
        self.memory_limit = memory_limit
        # The size of the memory that is requested by the components installed in the ACK cluster on the data plane if you enable the Kubernetes API to access Istio resources in the ASM instance. You can specify the parameter value in the standard quantity representation used by Kubernetes. 1 Mi equals 1,024 KB.
        self.memory_requirement = memory_requirement
        # The ID of the Alibaba Cloud Service Mesh (ASM) instance.
        self.service_mesh_id = service_mesh_id
        # Specifies whether the Kubernetes API on the data plane uses the public endpoint of the API server to access Istio resources in the ASM instance. Valid values:
        # 
        # *   `true`: The Kubernetes API on the data plane uses the public endpoint of the API server to access Istio resources in the ASM instance.
        # *   `false`: The Kubernetes API on the data plane uses the private endpoint of the API server to access Istio resources in the ASM instance.
        # 
        # Default value: `false`.
        self.use_public_api_server = use_public_api_server

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpulimit is not None:
            result['CPULimit'] = self.cpulimit
        if self.cpurequirement is not None:
            result['CPURequirement'] = self.cpurequirement
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.memory_requirement is not None:
            result['MemoryRequirement'] = self.memory_requirement
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.use_public_api_server is not None:
            result['UsePublicApiServer'] = self.use_public_api_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPULimit') is not None:
            self.cpulimit = m.get('CPULimit')
        if m.get('CPURequirement') is not None:
            self.cpurequirement = m.get('CPURequirement')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('MemoryRequirement') is not None:
            self.memory_requirement = m.get('MemoryRequirement')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('UsePublicApiServer') is not None:
            self.use_public_api_server = m.get('UsePublicApiServer')
        return self


class UpdateMeshCRAggregationResponseBody(TeaModel):
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


class UpdateMeshCRAggregationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMeshCRAggregationResponseBody = None,
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
            temp_model = UpdateMeshCRAggregationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMeshFeatureRequest(TeaModel):
    def __init__(
        self,
        access_log_enabled: bool = None,
        access_log_file: str = None,
        access_log_format: str = None,
        access_log_gateway_lifecycle: int = None,
        access_log_project: str = None,
        access_log_service_enabled: bool = None,
        access_log_service_host: str = None,
        access_log_service_port: int = None,
        access_log_sidecar_lifecycle: int = None,
        audit_project: str = None,
        auto_injection_policy_enabled: bool = None,
        craggregation_enabled: bool = None,
        cluster_spec: str = None,
        cni_enabled: bool = None,
        cni_exclude_namespaces: str = None,
        concurrency: int = None,
        config_source_enabled: bool = None,
        config_source_nacos_id: str = None,
        customized_prometheus: bool = None,
        customized_zipkin: bool = None,
        dnsproxying_enabled: bool = None,
        default_components_schedule_config: str = None,
        discovery_selectors: str = None,
        dubbo_filter_enabled: bool = None,
        enable_audit: bool = None,
        enable_auto_diagnosis: bool = None,
        enable_bootstrap_xds_agent: bool = None,
        enable_crhistory: bool = None,
        enable_namespaces_by_default: bool = None,
        enable_sdsserver: bool = None,
        exclude_ipranges: str = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ports: str = None,
        filter_gateway_cluster_config: bool = None,
        gateway_apienabled: bool = None,
        hold_application_until_proxy_starts: bool = None,
        http_10enabled: bool = None,
        include_ipranges: str = None,
        include_inbound_ports: str = None,
        include_outbound_ports: str = None,
        integrate_kiali: bool = None,
        interception_mode: str = None,
        kiali_arms_auth_tokens: str = None,
        kiali_enabled: bool = None,
        kiali_service_annotations: str = None,
        lifecycle: str = None,
        locality_lbconf: str = None,
        locality_load_balancing: bool = None,
        log_level: str = None,
        mseenabled: bool = None,
        multi_buffer_enabled: bool = None,
        multi_buffer_poll_delay: str = None,
        mysql_filter_enabled: bool = None,
        nfdenabled: bool = None,
        nfdlabel_pruned: bool = None,
        opainjector_cpulimit: str = None,
        opainjector_cpurequirement: str = None,
        opainjector_memory_limit: str = None,
        opainjector_memory_requirement: str = None,
        opalimit_cpu: str = None,
        opalimit_memory: str = None,
        opalog_level: str = None,
        oparequest_cpu: str = None,
        oparequest_memory: str = None,
        opascope_injected: bool = None,
        opa_enabled: bool = None,
        open_agent_policy: bool = None,
        outbound_traffic_policy: str = None,
        prometheus_url: str = None,
        proxy_init_cpuresource_limit: str = None,
        proxy_init_cpuresource_request: str = None,
        proxy_init_memory_resource_limit: str = None,
        proxy_init_memory_resource_request: str = None,
        proxy_limit_cpu: str = None,
        proxy_limit_memory: str = None,
        proxy_request_cpu: str = None,
        proxy_request_memory: str = None,
        proxy_stats_matcher: str = None,
        redis_filter_enabled: bool = None,
        service_mesh_id: str = None,
        sidecar_injector_limit_cpu: str = None,
        sidecar_injector_limit_memory: str = None,
        sidecar_injector_request_cpu: str = None,
        sidecar_injector_request_memory: str = None,
        sidecar_injector_webhook_as_yaml: str = None,
        telemetry: bool = None,
        termination_drain_duration: str = None,
        thrift_filter_enabled: bool = None,
        trace_custom_tags: str = None,
        trace_max_path_tag_length: str = None,
        trace_sampling: float = None,
        tracing: bool = None,
        tracing_on_ext_zipkin_limit_cpu: str = None,
        tracing_on_ext_zipkin_limit_memory: str = None,
        tracing_on_ext_zipkin_request_cpu: str = None,
        tracing_on_ext_zipkin_request_memory: str = None,
        web_assembly_filter_enabled: bool = None,
    ):
        # Specifies whether to enable access log collection. Valid values:
        # 
        # *   `true`: enables access log collection.
        # *   `false`: disables access log collection.
        # 
        # Default value: `false`.
        self.access_log_enabled = access_log_enabled
        # Specifies whether to enable access logging. Valid values:
        # 
        # *   `""`: disables access logging.
        # *   `/dev/stdout`: enables access logging. Access logs are written to /dev/stdout.
        self.access_log_file = access_log_file
        # The custom format of access logs. To set this parameter, make sure that you have enabled access log collection. The value must be a JSON string. The following key names must be contained: authority_for, bytes_received, bytes_sent, downstream_local_address, downstream_remote_address, duration, istio_policy_status, method, path, protocol, requested_server_name, response_code, response_flags, route_name, start_time, trace_id, upstream_cluster, upstream_host, upstream_local_address, upstream_service_time, upstream_transport_failure_reason, user_agent, and x_forwarded_for.
        self.access_log_format = access_log_format
        # The retention period for the access logs of the sidecar proxy. Unit: day. The logs are collected by using Log Service. For example, `30` indicates 30 days.
        self.access_log_gateway_lifecycle = access_log_gateway_lifecycle
        # The custom project on which the Log Service collects logs.
        self.access_log_project = access_log_project
        # Specifies whether to enable gRPC Access Log Service (ALS) for Envoy. Valid values:
        # 
        # *   `true`: enables gRPC ALS for Envoy.
        # *   `false`: disables gRPC ALS for Envoy.
        # 
        # Default value: `false`.
        self.access_log_service_enabled = access_log_service_enabled
        # The endpoint of gRPC ALS for Envoy.
        self.access_log_service_host = access_log_service_host
        # The port of gRPC ALS for Envoy.
        self.access_log_service_port = access_log_service_port
        # Specifies whether to enable automatic diagnostics for the ASM instance. If you enable this feature, the ASM instance is automatically diagnosed when you modify Istio resources in the ASM instance.
        self.access_log_sidecar_lifecycle = access_log_sidecar_lifecycle
        # The name of the Log Service project that is used for mesh audit.
        # 
        # Default value: `mesh-log-{ASM instance ID}`.
        self.audit_project = audit_project
        # Specifies whether to enable automatic sidecar proxy injection by using pod annotations. Valid values:
        # 
        # *   `true`: enables automatic sidecar proxy injection by using pod annotations.
        # *   `false`: disables automatic sidecar proxy injection by using pod annotations.
        # 
        # Default value: `false`.
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        # Specifies whether to use the Kubernetes API of clusters on the data plane to access Istio resources. To use this feature, the version of the ASM instance must be V1.9.7.93 or later.
        self.craggregation_enabled = craggregation_enabled
        # Specifies whether to enable the feature of controlling the OPA injection scope. Valid values:
        # 
        # *   `true`: enables the feature.
        # *   `false`: disables the feature.
        self.cluster_spec = cluster_spec
        # Specifies whether to enable the Container Network Interface (CNI) plug-in. Valid values:
        # 
        # *   `true`: enables the CNI plug-in.
        # *   `false`: disables the CNI plug-in.
        # 
        # Default value: `false`.
        self.cni_enabled = cni_enabled
        # The namespaces to be excluded for the CNI plug-in.
        self.cni_exclude_namespaces = cni_exclude_namespaces
        # Specifies whether to delay application container startup until the sidecar proxy container is started in a pod.
        self.concurrency = concurrency
        # Specifies whether to enable the external service registry. Valid values:
        # 
        # *   `true`: enables the external service registry.
        # *   `false`: disables the external service registry.
        # 
        # Default value: `false`.
        self.config_source_enabled = config_source_enabled
        # The instance ID of the Nacos registry.
        self.config_source_nacos_id = config_source_nacos_id
        # Specifies whether to use a custom Prometheus instance. Valid values:
        # 
        # *   `true`: uses a custom Prometheus instance.
        # *   `false`: does not use a custom Prometheus instance.
        # 
        # Default value: `false`.
        self.customized_prometheus = customized_prometheus
        # Specifies whether to use a self-managed Zipkin system to collect tracing data. Valid values:
        # 
        # *   `true`: uses a self-managed Zipkin system.
        # *   `false`: does not use a self-managed Zipkin system.
        # 
        # Default value: `false`.
        self.customized_zipkin = customized_zipkin
        # Specifies whether to enable DNS proxy. Valid values:
        # 
        # *   `true`: enables the DNS proxy feature.
        # *   `false`: disables the DNS proxy feature.
        # 
        # Default value: `false`.
        self.dnsproxying_enabled = dnsproxying_enabled
        # Specifies the default scheduling configurations that ASM delivers to components on the data plane. You can configure nodeSelector and tolerations in the JSON format. 
        # 
        # 
        # >* Modifying the value of this parameter is a high-risk operation. The modification will cause all components on the data plane of ASM to restart. Exercise caution before modifying the value of this parameter. 
        # >* The configurations specified by this parameter do not apply to the ASM gateway. You can configure scheduling on the ASM gateway.
        self.default_components_schedule_config = default_components_schedule_config
        # The label selectors used to specify the namespaces of the clusters on the data plane for selective service discovery.
        self.discovery_selectors = discovery_selectors
        # Specifies whether to enable Dubbo Filter. Valid values:
        # 
        # *   `true`: enables Dubbo Filter.
        # *   `false`: disables Dubbo Filter.
        # 
        # Default value: `false`.
        self.dubbo_filter_enabled = dubbo_filter_enabled
        # Specifies whether to enable the mesh audit feature. To enable this feature, make sure that you have activated [Log Service](https://sls.console.aliyun.com/). Valid values:
        # 
        # *   `true`: enables the mesh audit feature.
        # *   `false`: disables the mesh audit feature.
        # 
        # Default value: `false`.
        self.enable_audit = enable_audit
        # The ports for which outbound traffic is redirected to the sidecar proxy.
        self.enable_auto_diagnosis = enable_auto_diagnosis
        # Specifies the authentication token of an ARMS Prometheus instance when the Mesh Topology feature is enabled and ARMS Prometheus is used to collect monitoring metrics. The token is used to allow Mesh Topology to access the ARMS Prometheus instance. The token is in the JSON format. The key in the JSON object is the ID of the cluster on the data plane, and the value is the authentication token of the ARMS Prometheus instance deployed in the cluster.
        self.enable_bootstrap_xds_agent = enable_bootstrap_xds_agent
        # Specifies whether to enable the rollback feature for Istio resources.
        self.enable_crhistory = enable_crhistory
        # Specifies whether to enable automatic sidecar proxy injection for all namespaces. Valid values:
        # 
        # *   `true`: enables automatic sidecar proxy injection for all namespaces.
        # *   `false`: disables automatic sidecar proxy injection for all namespaces.
        # 
        # Default value: `false`.
        self.enable_namespaces_by_default = enable_namespaces_by_default
        # Specifies whether to enable Secret Discovery Service (SDS). Valid values:
        # 
        # *   `true`: enables SDS.
        # *   `false`: disables SDS.
        # 
        # Default value: `false`.
        self.enable_sdsserver = enable_sdsserver
        # The IP addresses of external services to which traffic is not intercepted.
        self.exclude_ipranges = exclude_ipranges
        # The ports for which inbound traffic is not redirected to the sidecar proxy. Separate multiple ports with commas (,).
        self.exclude_inbound_ports = exclude_inbound_ports
        # The ports for which outbound traffic is not redirected to the sidecar proxy. Separate multiple ports with commas (,).
        self.exclude_outbound_ports = exclude_outbound_ports
        # Specifies whether to enable gateway configuration filtering. Valid values:
        # 
        # *   `true`: enables gateway configuration filtering.
        # *   `false`: disables gateway configuration filtering.
        # 
        # Default value: `false`.
        self.filter_gateway_cluster_config = filter_gateway_cluster_config
        # Specifies whether to enable Gateway API. Valid values:
        # 
        # *   `true`: enables Gateway API.
        # *   `false`: disables Gateway API.
        # 
        # Default value: `false`.
        self.gateway_apienabled = gateway_apienabled
        # Other metrics of the sidecar proxy on the data plane.
        self.hold_application_until_proxy_starts = hold_application_until_proxy_starts
        # Specifies whether to support HTTP 1.0. Valid values:
        # 
        # *   `true`: supports HTTP 1.0.
        # *   `false`: does not support HTTP 1.0.
        # 
        # Default value: `false`.
        self.http_10enabled = http_10enabled
        # The IP addresses of external services to which traffic is intercepted.
        self.include_ipranges = include_ipranges
        # The ports for which inbound traffic is redirected to the sidecar proxy.
        self.include_inbound_ports = include_inbound_ports
        # The log level of the sidecar proxy on the data plane. Log levels include `none`, `error`, `warn`, `info`, and `debug`. The levels correspond to different amounts of information reported by the logs. For example, none-level logs report the least information, while debug-level logs report the most information.
        self.include_outbound_ports = include_outbound_ports
        # Specifies whether to enable Node Feature Discovery (NFD).
        self.integrate_kiali = integrate_kiali
        # Specifies whether to load the bootstrap configuration before the sidecar proxy is started.
        self.interception_mode = interception_mode
        # Specifies the default scheduling configurations that ASM delivers to components on the data plane. You can configure `nodeSelector` and tolerations in the JSON format.
        # 
        # > *   Modifying the value of this parameter is a high-risk operation. The modification will cause all components on the data plane of ASM to restart. Exercise caution before modifying the value of this parameter.
        # >*   The configurations specified by this parameter do not apply to the ASM gateway. You can configure gateway-specific scheduling on the ASM gateway.
        self.kiali_arms_auth_tokens = kiali_arms_auth_tokens
        # Specifies whether to enable the Mesh Topology feature. To enable this feature, make sure that you have enabled Prometheus monitoring. If Prometheus monitoring is disabled, the Mesh Topology feature must be disabled. Valid values:````
        # 
        # *   `true`: enables the Mesh Topology feature.
        # *   `false`: disables the Mesh Topology feature.
        # 
        # Default value: `false`.
        self.kiali_enabled = kiali_enabled
        # 当开启网格拓扑且为访问网格拓扑创建CLB时，通过此参数使用Annotation配置不同集群中网格拓扑服务的CLB。
        # 
        # 参数格式为JSON编码的字符串，JSON对象中的键为数据面集群的集群ID，值为数据面集群中网格拓扑服务的Annotation内容。
        # 
        # 有关如何通过注解配置CLB，参考 [通过Annotation配置传统型负载均衡CLB](https://help.aliyun.com/document_detail/86531.html)。
        self.kiali_service_annotations = kiali_service_annotations
        # The lifecycle of the sidecar proxy.
        self.lifecycle = lifecycle
        # The configurations of cross-region load balancing. Valid values:
        # 
        # *   `failover`: the configurations of cross-region failover. Example:
        # 
        # <!---->
        # 
        #     failover: [// Cross-region failover configurations of the struct type. 
        #             {
        #                 // If a service fails in the China (Beijing) region, the traffic is redirected to the same service in the China (Hangzhou) region. 
        #                 from: "cn-beijing", 
        #                 to: "cn-hangzhou",
        #             }
        #         ]
        # 
        # *   `distribute`: the configurations of cross-region traffic distribution. Example:
        # 
        # <!---->
        # 
        #     distribute: [// Cross-region traffic distribution configurations of the struct type. 
        #             {
        #                 // For traffic that is routed to the China (Beijing) region, 70% of the traffic is allocated to the China (Beijing) region and the rest of the traffic is redirected to the China (Hangzhou) region. 
        #                 "from": "cn-beijing",
        #                 "to": {
        #                     "cn-beijing": 70,
        #                     "cn-hangzhou": 30,
        #                 }
        #             }
        #         ]
        self.locality_lbconf = locality_lbconf
        # Specifies whether to enable cross-region load balancing. Valid values:
        # 
        # *   `true`: enables cross-region load balancing.
        # *   `false`: disables cross-region load balancing.
        # 
        # Default value: `false`.
        self.locality_load_balancing = locality_load_balancing
        # The number of worker threads used by the sidecar proxy on the data plane.
        self.log_level = log_level
        # Specifies whether to enable Microservice Engine (MSE). Valid values:
        # 
        # *   `true`: enables MSE.
        # *   `false`: disables MSE.
        # 
        # Default value: `false`.
        self.mseenabled = mseenabled
        # Specifies whether to enable Transport Layer Security (TLS) acceleration based on MultiBuffer.
        self.multi_buffer_enabled = multi_buffer_enabled
        # The pull-request latency. By default, this parameter is left empty.
        self.multi_buffer_poll_delay = multi_buffer_poll_delay
        # Specifies whether to enable MySQL Filter. Valid values:
        # 
        # *   `true`: enables MySQL Filter.
        # *   `false`: disables MySQL Filter.
        # 
        # Default value: `false`.
        self.mysql_filter_enabled = mysql_filter_enabled
        # Specifies whether to clear feature labels on nodes when NFD is disabled.
        # 
        # This parameter is valid only when the `NFDEnabled` parameter is set to `false`.
        self.nfdenabled = nfdenabled
        # The minimum number of CPU cores requested by the proxy service that exports Tracing Analysis data. For example, `1000m` indicates one CPU core.
        self.nfdlabel_pruned = nfdlabel_pruned
        # The maximum size of the memory that is available to the pod that injects OPA proxies into application pods. For example, `1024Mi` indicates 1024 MB.
        self.opainjector_cpulimit = opainjector_cpulimit
        # The minimum size of the memory requested by the pod that injects OPA proxies into application pods. For example, `50 Mi` indicates 50 MB.
        self.opainjector_cpurequirement = opainjector_cpurequirement
        # Specifies whether to create an SLB instance for accessing the ASM mesh topology.
        self.opainjector_memory_limit = opainjector_memory_limit
        # The maximum number of CPU cores that are available to the pod that injects OPA proxies into application pods. For example, `1000m` indicates one CPU core.
        self.opainjector_memory_requirement = opainjector_memory_requirement
        # The maximum number of CPU cores that are available to the OPA proxy container.
        self.opalimit_cpu = opalimit_cpu
        # The maximum size of the memory that is available to the OPA proxy container.
        self.opalimit_memory = opalimit_memory
        # The log level of the OPA proxy container.
        # 
        # *   `info`: outputs all information.
        # *   `debug`: outputs debugging and error information.
        # *   `error`: outputs only error information.
        self.opalog_level = opalog_level
        # The number of CPU cores that are requested by the OPA proxy container.
        self.oparequest_cpu = oparequest_cpu
        # The size of the memory that is requested by the OPA proxy container.
        self.oparequest_memory = oparequest_memory
        # The minimum number of CPU cores requested by the pod that injects OPA proxies into application pods. For example, `1000m` indicates one CPU core.
        self.opascope_injected = opascope_injected
        # Specifies whether to enable the OPA plug-in. Valid values:
        # 
        # *   `true`: enables the OPA plug-in.
        # *   `false`: disables the OPA plug-in.
        # 
        # Default value: `false`.
        self.opa_enabled = opa_enabled
        # Specifies whether to install the Open Policy Agent (OPA) plug-in. Valid values:
        # 
        # *   `true`: installs the OPA plug-in.
        # *   `false`: does not install the OPA plug-in.
        # 
        # Default value: `false`.
        self.open_agent_policy = open_agent_policy
        # The policy for accessing external services. Valid values:
        # 
        # *   `ALLOW_ANY`: allows access to all external services.
        # *   `REGISTRY_ONLY`: allows access to only the external services that are defined in the ServiceEntry of the ASM instance.
        self.outbound_traffic_policy = outbound_traffic_policy
        # The endpoint of Prometheus monitoring. If you use ARMS Prometheus, set this parameter to the endpoint of Prometheus provided by ARMS.
        self.prometheus_url = prometheus_url
        # The maximum number of CPU cores that are available to the istio-init container.
        self.proxy_init_cpuresource_limit = proxy_init_cpuresource_limit
        # The number of CPU cores that are requested by the istio-init container.
        self.proxy_init_cpuresource_request = proxy_init_cpuresource_request
        # The maximum size of the memory that is available to the istio-init container.
        self.proxy_init_memory_resource_limit = proxy_init_memory_resource_limit
        # The size of the memory that is requested by the istio-init container.
        self.proxy_init_memory_resource_request = proxy_init_memory_resource_request
        # The maximum number of CPU cores that are available to the sidecar proxy container.
        self.proxy_limit_cpu = proxy_limit_cpu
        # The maximum size of the memory that is available to the sidecar proxy container.
        self.proxy_limit_memory = proxy_limit_memory
        # The number of CPU cores that are requested by the sidecar proxy container.
        self.proxy_request_cpu = proxy_request_cpu
        # The size of the memory that is requested by the sidecar proxy container.
        self.proxy_request_memory = proxy_request_memory
        # The mode in which the sidecar proxy intercepts inbound traffic. Valid values:
        # 
        # *   `REDIRECT`: The sidecar proxy intercepts inbound traffic in the REDIRECT mode.
        # *   `TPROXY`: The sidecar proxy intercepts inbound traffic in the TPROXY mode.
        self.proxy_stats_matcher = proxy_stats_matcher
        # Specifies whether to enable Redis Filter. Valid values:
        # 
        # *   `true`: enables Redis Filter.
        # *   `false`: disables Redis Filter.
        # 
        # Default value: `false`.
        self.redis_filter_enabled = redis_filter_enabled
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # The maximum number of CPU cores that are available to the pod where a sidecar proxy injector resides.
        self.sidecar_injector_limit_cpu = sidecar_injector_limit_cpu
        # The maximum size of the memory that is available to the pod where a sidecar proxy injector resides.
        self.sidecar_injector_limit_memory = sidecar_injector_limit_memory
        # The number of CPU cores that are requested by the pod where a sidecar proxy injector resides.
        self.sidecar_injector_request_cpu = sidecar_injector_request_cpu
        # The size of the memory that is requested by the pod where a sidecar proxy injector resides.
        self.sidecar_injector_request_memory = sidecar_injector_request_memory
        # Other configurations of automatic sidecar proxy injection, in the YAML format.
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml
        # Specifies whether to enable Prometheus monitoring. We recommend that you enable [ARMS Prometheus](https://arms.console.aliyun.com/). Valid values:
        # 
        # *   `true`: enables Prometheus monitoring.
        # *   `false`: disables Prometheus monitoring.
        # 
        # Default value: `false`.
        self.telemetry = telemetry
        # The maximum period of time that the sidecar proxy waits for requests to be processed before the proxy is stopped. For example, if you want to specify a period of 5 seconds, set this parameter to 5s.
        self.termination_drain_duration = termination_drain_duration
        # Specifies whether to enable Thrift Filter. Valid values:
        # 
        # *   `true`: enables Thrift Filter.
        # *   `false`: disables Thrift Filter.
        # 
        # Default value: `false`.
        self.thrift_filter_enabled = thrift_filter_enabled
        # The custom tag of Tracing Analysis. Specify this parameter in the JSON format.
        # 
        #     {
        #         "name1": CustomTag,
        #         "name2": CustomTag
        #     }
        # 
        # Tag key: literal, header, or environment.
        # 
        #     {
        #         "literal": {
        #             "value": "Fixed value"
        #         }
        #         "header": {
        #             "name": "Header name"
        #             "defaultValue": "Default value that is used if the specified header does not exist"
        #         }
        #         "environment": {
        #             "name": "Environment variable name"
        #             "defaultValue": "Default value that is used if the specified environment variable does not exist"
        #         }
        #     }
        self.trace_custom_tags = trace_custom_tags
        # The maximum length of the request path contained in the HttpUrl span tag. Default value: `256`.
        self.trace_max_path_tag_length = trace_max_path_tag_length
        # The sampling percentage of Tracing Analysis.
        self.trace_sampling = trace_sampling
        # Specifies whether to enable the Tracing Analysis feature. To enable this feature, make sure that you have activated [Tracing Analysis](https://tracing-analysis.console.aliyun.com/). Valid values:
        # 
        # *   `true`: enables the Tracing Analysis feature.
        # *   `false`: disables the Tracing Analysis feature.
        # 
        # Default value: `false`.
        self.tracing = tracing
        # The maximum size of the memory that is available to the proxy service that exports Tracing Analysis data. For example, `1Mi` indicates 1 MB.
        self.tracing_on_ext_zipkin_limit_cpu = tracing_on_ext_zipkin_limit_cpu
        # The retention period for the access logs of the ingress gateway. Unit: day. The logs are collected by using Log Service. For example, `30` indicates 30 days.
        self.tracing_on_ext_zipkin_limit_memory = tracing_on_ext_zipkin_limit_memory
        # The minimum size of the memory requested by the proxy service that exports Tracing Analysis data. For example, `1Mi` indicates 1 MB.
        self.tracing_on_ext_zipkin_request_cpu = tracing_on_ext_zipkin_request_cpu
        # The maximum number of CPU cores that are available to the proxy service that exports Tracing Analysis data. For example, `1000m` indicates one CPU core.
        self.tracing_on_ext_zipkin_request_memory = tracing_on_ext_zipkin_request_memory
        # Specifies whether to enable WebAssembly Filter. Valid values:
        # 
        # *   `true`: enables WebAssembly Filter.
        # *   `false`: disables WebAssembly Filter.
        # 
        # Default value: `false`.
        self.web_assembly_filter_enabled = web_assembly_filter_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_log_enabled is not None:
            result['AccessLogEnabled'] = self.access_log_enabled
        if self.access_log_file is not None:
            result['AccessLogFile'] = self.access_log_file
        if self.access_log_format is not None:
            result['AccessLogFormat'] = self.access_log_format
        if self.access_log_gateway_lifecycle is not None:
            result['AccessLogGatewayLifecycle'] = self.access_log_gateway_lifecycle
        if self.access_log_project is not None:
            result['AccessLogProject'] = self.access_log_project
        if self.access_log_service_enabled is not None:
            result['AccessLogServiceEnabled'] = self.access_log_service_enabled
        if self.access_log_service_host is not None:
            result['AccessLogServiceHost'] = self.access_log_service_host
        if self.access_log_service_port is not None:
            result['AccessLogServicePort'] = self.access_log_service_port
        if self.access_log_sidecar_lifecycle is not None:
            result['AccessLogSidecarLifecycle'] = self.access_log_sidecar_lifecycle
        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.craggregation_enabled is not None:
            result['CRAggregationEnabled'] = self.craggregation_enabled
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.cni_enabled is not None:
            result['CniEnabled'] = self.cni_enabled
        if self.cni_exclude_namespaces is not None:
            result['CniExcludeNamespaces'] = self.cni_exclude_namespaces
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.config_source_enabled is not None:
            result['ConfigSourceEnabled'] = self.config_source_enabled
        if self.config_source_nacos_id is not None:
            result['ConfigSourceNacosID'] = self.config_source_nacos_id
        if self.customized_prometheus is not None:
            result['CustomizedPrometheus'] = self.customized_prometheus
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.dnsproxying_enabled is not None:
            result['DNSProxyingEnabled'] = self.dnsproxying_enabled
        if self.default_components_schedule_config is not None:
            result['DefaultComponentsScheduleConfig'] = self.default_components_schedule_config
        if self.discovery_selectors is not None:
            result['DiscoverySelectors'] = self.discovery_selectors
        if self.dubbo_filter_enabled is not None:
            result['DubboFilterEnabled'] = self.dubbo_filter_enabled
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.enable_auto_diagnosis is not None:
            result['EnableAutoDiagnosis'] = self.enable_auto_diagnosis
        if self.enable_bootstrap_xds_agent is not None:
            result['EnableBootstrapXdsAgent'] = self.enable_bootstrap_xds_agent
        if self.enable_crhistory is not None:
            result['EnableCRHistory'] = self.enable_crhistory
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.enable_sdsserver is not None:
            result['EnableSDSServer'] = self.enable_sdsserver
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.filter_gateway_cluster_config is not None:
            result['FilterGatewayClusterConfig'] = self.filter_gateway_cluster_config
        if self.gateway_apienabled is not None:
            result['GatewayAPIEnabled'] = self.gateway_apienabled
        if self.hold_application_until_proxy_starts is not None:
            result['HoldApplicationUntilProxyStarts'] = self.hold_application_until_proxy_starts
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.include_inbound_ports is not None:
            result['IncludeInboundPorts'] = self.include_inbound_ports
        if self.include_outbound_ports is not None:
            result['IncludeOutboundPorts'] = self.include_outbound_ports
        if self.integrate_kiali is not None:
            result['IntegrateKiali'] = self.integrate_kiali
        if self.interception_mode is not None:
            result['InterceptionMode'] = self.interception_mode
        if self.kiali_arms_auth_tokens is not None:
            result['KialiArmsAuthTokens'] = self.kiali_arms_auth_tokens
        if self.kiali_enabled is not None:
            result['KialiEnabled'] = self.kiali_enabled
        if self.kiali_service_annotations is not None:
            result['KialiServiceAnnotations'] = self.kiali_service_annotations
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.locality_lbconf is not None:
            result['LocalityLBConf'] = self.locality_lbconf
        if self.locality_load_balancing is not None:
            result['LocalityLoadBalancing'] = self.locality_load_balancing
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.mseenabled is not None:
            result['MSEEnabled'] = self.mseenabled
        if self.multi_buffer_enabled is not None:
            result['MultiBufferEnabled'] = self.multi_buffer_enabled
        if self.multi_buffer_poll_delay is not None:
            result['MultiBufferPollDelay'] = self.multi_buffer_poll_delay
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.nfdenabled is not None:
            result['NFDEnabled'] = self.nfdenabled
        if self.nfdlabel_pruned is not None:
            result['NFDLabelPruned'] = self.nfdlabel_pruned
        if self.opainjector_cpulimit is not None:
            result['OPAInjectorCPULimit'] = self.opainjector_cpulimit
        if self.opainjector_cpurequirement is not None:
            result['OPAInjectorCPURequirement'] = self.opainjector_cpurequirement
        if self.opainjector_memory_limit is not None:
            result['OPAInjectorMemoryLimit'] = self.opainjector_memory_limit
        if self.opainjector_memory_requirement is not None:
            result['OPAInjectorMemoryRequirement'] = self.opainjector_memory_requirement
        if self.opalimit_cpu is not None:
            result['OPALimitCPU'] = self.opalimit_cpu
        if self.opalimit_memory is not None:
            result['OPALimitMemory'] = self.opalimit_memory
        if self.opalog_level is not None:
            result['OPALogLevel'] = self.opalog_level
        if self.oparequest_cpu is not None:
            result['OPARequestCPU'] = self.oparequest_cpu
        if self.oparequest_memory is not None:
            result['OPARequestMemory'] = self.oparequest_memory
        if self.opascope_injected is not None:
            result['OPAScopeInjected'] = self.opascope_injected
        if self.opa_enabled is not None:
            result['OpaEnabled'] = self.opa_enabled
        if self.open_agent_policy is not None:
            result['OpenAgentPolicy'] = self.open_agent_policy
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.prometheus_url is not None:
            result['PrometheusUrl'] = self.prometheus_url
        if self.proxy_init_cpuresource_limit is not None:
            result['ProxyInitCPUResourceLimit'] = self.proxy_init_cpuresource_limit
        if self.proxy_init_cpuresource_request is not None:
            result['ProxyInitCPUResourceRequest'] = self.proxy_init_cpuresource_request
        if self.proxy_init_memory_resource_limit is not None:
            result['ProxyInitMemoryResourceLimit'] = self.proxy_init_memory_resource_limit
        if self.proxy_init_memory_resource_request is not None:
            result['ProxyInitMemoryResourceRequest'] = self.proxy_init_memory_resource_request
        if self.proxy_limit_cpu is not None:
            result['ProxyLimitCPU'] = self.proxy_limit_cpu
        if self.proxy_limit_memory is not None:
            result['ProxyLimitMemory'] = self.proxy_limit_memory
        if self.proxy_request_cpu is not None:
            result['ProxyRequestCPU'] = self.proxy_request_cpu
        if self.proxy_request_memory is not None:
            result['ProxyRequestMemory'] = self.proxy_request_memory
        if self.proxy_stats_matcher is not None:
            result['ProxyStatsMatcher'] = self.proxy_stats_matcher
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.sidecar_injector_limit_cpu is not None:
            result['SidecarInjectorLimitCPU'] = self.sidecar_injector_limit_cpu
        if self.sidecar_injector_limit_memory is not None:
            result['SidecarInjectorLimitMemory'] = self.sidecar_injector_limit_memory
        if self.sidecar_injector_request_cpu is not None:
            result['SidecarInjectorRequestCPU'] = self.sidecar_injector_request_cpu
        if self.sidecar_injector_request_memory is not None:
            result['SidecarInjectorRequestMemory'] = self.sidecar_injector_request_memory
        if self.sidecar_injector_webhook_as_yaml is not None:
            result['SidecarInjectorWebhookAsYaml'] = self.sidecar_injector_webhook_as_yaml
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.termination_drain_duration is not None:
            result['TerminationDrainDuration'] = self.termination_drain_duration
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        if self.trace_custom_tags is not None:
            result['TraceCustomTags'] = self.trace_custom_tags
        if self.trace_max_path_tag_length is not None:
            result['TraceMaxPathTagLength'] = self.trace_max_path_tag_length
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.tracing_on_ext_zipkin_limit_cpu is not None:
            result['TracingOnExtZipkinLimitCPU'] = self.tracing_on_ext_zipkin_limit_cpu
        if self.tracing_on_ext_zipkin_limit_memory is not None:
            result['TracingOnExtZipkinLimitMemory'] = self.tracing_on_ext_zipkin_limit_memory
        if self.tracing_on_ext_zipkin_request_cpu is not None:
            result['TracingOnExtZipkinRequestCPU'] = self.tracing_on_ext_zipkin_request_cpu
        if self.tracing_on_ext_zipkin_request_memory is not None:
            result['TracingOnExtZipkinRequestMemory'] = self.tracing_on_ext_zipkin_request_memory
        if self.web_assembly_filter_enabled is not None:
            result['WebAssemblyFilterEnabled'] = self.web_assembly_filter_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLogEnabled') is not None:
            self.access_log_enabled = m.get('AccessLogEnabled')
        if m.get('AccessLogFile') is not None:
            self.access_log_file = m.get('AccessLogFile')
        if m.get('AccessLogFormat') is not None:
            self.access_log_format = m.get('AccessLogFormat')
        if m.get('AccessLogGatewayLifecycle') is not None:
            self.access_log_gateway_lifecycle = m.get('AccessLogGatewayLifecycle')
        if m.get('AccessLogProject') is not None:
            self.access_log_project = m.get('AccessLogProject')
        if m.get('AccessLogServiceEnabled') is not None:
            self.access_log_service_enabled = m.get('AccessLogServiceEnabled')
        if m.get('AccessLogServiceHost') is not None:
            self.access_log_service_host = m.get('AccessLogServiceHost')
        if m.get('AccessLogServicePort') is not None:
            self.access_log_service_port = m.get('AccessLogServicePort')
        if m.get('AccessLogSidecarLifecycle') is not None:
            self.access_log_sidecar_lifecycle = m.get('AccessLogSidecarLifecycle')
        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('CRAggregationEnabled') is not None:
            self.craggregation_enabled = m.get('CRAggregationEnabled')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('CniEnabled') is not None:
            self.cni_enabled = m.get('CniEnabled')
        if m.get('CniExcludeNamespaces') is not None:
            self.cni_exclude_namespaces = m.get('CniExcludeNamespaces')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ConfigSourceEnabled') is not None:
            self.config_source_enabled = m.get('ConfigSourceEnabled')
        if m.get('ConfigSourceNacosID') is not None:
            self.config_source_nacos_id = m.get('ConfigSourceNacosID')
        if m.get('CustomizedPrometheus') is not None:
            self.customized_prometheus = m.get('CustomizedPrometheus')
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('DNSProxyingEnabled') is not None:
            self.dnsproxying_enabled = m.get('DNSProxyingEnabled')
        if m.get('DefaultComponentsScheduleConfig') is not None:
            self.default_components_schedule_config = m.get('DefaultComponentsScheduleConfig')
        if m.get('DiscoverySelectors') is not None:
            self.discovery_selectors = m.get('DiscoverySelectors')
        if m.get('DubboFilterEnabled') is not None:
            self.dubbo_filter_enabled = m.get('DubboFilterEnabled')
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('EnableAutoDiagnosis') is not None:
            self.enable_auto_diagnosis = m.get('EnableAutoDiagnosis')
        if m.get('EnableBootstrapXdsAgent') is not None:
            self.enable_bootstrap_xds_agent = m.get('EnableBootstrapXdsAgent')
        if m.get('EnableCRHistory') is not None:
            self.enable_crhistory = m.get('EnableCRHistory')
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('EnableSDSServer') is not None:
            self.enable_sdsserver = m.get('EnableSDSServer')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('FilterGatewayClusterConfig') is not None:
            self.filter_gateway_cluster_config = m.get('FilterGatewayClusterConfig')
        if m.get('GatewayAPIEnabled') is not None:
            self.gateway_apienabled = m.get('GatewayAPIEnabled')
        if m.get('HoldApplicationUntilProxyStarts') is not None:
            self.hold_application_until_proxy_starts = m.get('HoldApplicationUntilProxyStarts')
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('IncludeInboundPorts') is not None:
            self.include_inbound_ports = m.get('IncludeInboundPorts')
        if m.get('IncludeOutboundPorts') is not None:
            self.include_outbound_ports = m.get('IncludeOutboundPorts')
        if m.get('IntegrateKiali') is not None:
            self.integrate_kiali = m.get('IntegrateKiali')
        if m.get('InterceptionMode') is not None:
            self.interception_mode = m.get('InterceptionMode')
        if m.get('KialiArmsAuthTokens') is not None:
            self.kiali_arms_auth_tokens = m.get('KialiArmsAuthTokens')
        if m.get('KialiEnabled') is not None:
            self.kiali_enabled = m.get('KialiEnabled')
        if m.get('KialiServiceAnnotations') is not None:
            self.kiali_service_annotations = m.get('KialiServiceAnnotations')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('LocalityLBConf') is not None:
            self.locality_lbconf = m.get('LocalityLBConf')
        if m.get('LocalityLoadBalancing') is not None:
            self.locality_load_balancing = m.get('LocalityLoadBalancing')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('MSEEnabled') is not None:
            self.mseenabled = m.get('MSEEnabled')
        if m.get('MultiBufferEnabled') is not None:
            self.multi_buffer_enabled = m.get('MultiBufferEnabled')
        if m.get('MultiBufferPollDelay') is not None:
            self.multi_buffer_poll_delay = m.get('MultiBufferPollDelay')
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('NFDEnabled') is not None:
            self.nfdenabled = m.get('NFDEnabled')
        if m.get('NFDLabelPruned') is not None:
            self.nfdlabel_pruned = m.get('NFDLabelPruned')
        if m.get('OPAInjectorCPULimit') is not None:
            self.opainjector_cpulimit = m.get('OPAInjectorCPULimit')
        if m.get('OPAInjectorCPURequirement') is not None:
            self.opainjector_cpurequirement = m.get('OPAInjectorCPURequirement')
        if m.get('OPAInjectorMemoryLimit') is not None:
            self.opainjector_memory_limit = m.get('OPAInjectorMemoryLimit')
        if m.get('OPAInjectorMemoryRequirement') is not None:
            self.opainjector_memory_requirement = m.get('OPAInjectorMemoryRequirement')
        if m.get('OPALimitCPU') is not None:
            self.opalimit_cpu = m.get('OPALimitCPU')
        if m.get('OPALimitMemory') is not None:
            self.opalimit_memory = m.get('OPALimitMemory')
        if m.get('OPALogLevel') is not None:
            self.opalog_level = m.get('OPALogLevel')
        if m.get('OPARequestCPU') is not None:
            self.oparequest_cpu = m.get('OPARequestCPU')
        if m.get('OPARequestMemory') is not None:
            self.oparequest_memory = m.get('OPARequestMemory')
        if m.get('OPAScopeInjected') is not None:
            self.opascope_injected = m.get('OPAScopeInjected')
        if m.get('OpaEnabled') is not None:
            self.opa_enabled = m.get('OpaEnabled')
        if m.get('OpenAgentPolicy') is not None:
            self.open_agent_policy = m.get('OpenAgentPolicy')
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('PrometheusUrl') is not None:
            self.prometheus_url = m.get('PrometheusUrl')
        if m.get('ProxyInitCPUResourceLimit') is not None:
            self.proxy_init_cpuresource_limit = m.get('ProxyInitCPUResourceLimit')
        if m.get('ProxyInitCPUResourceRequest') is not None:
            self.proxy_init_cpuresource_request = m.get('ProxyInitCPUResourceRequest')
        if m.get('ProxyInitMemoryResourceLimit') is not None:
            self.proxy_init_memory_resource_limit = m.get('ProxyInitMemoryResourceLimit')
        if m.get('ProxyInitMemoryResourceRequest') is not None:
            self.proxy_init_memory_resource_request = m.get('ProxyInitMemoryResourceRequest')
        if m.get('ProxyLimitCPU') is not None:
            self.proxy_limit_cpu = m.get('ProxyLimitCPU')
        if m.get('ProxyLimitMemory') is not None:
            self.proxy_limit_memory = m.get('ProxyLimitMemory')
        if m.get('ProxyRequestCPU') is not None:
            self.proxy_request_cpu = m.get('ProxyRequestCPU')
        if m.get('ProxyRequestMemory') is not None:
            self.proxy_request_memory = m.get('ProxyRequestMemory')
        if m.get('ProxyStatsMatcher') is not None:
            self.proxy_stats_matcher = m.get('ProxyStatsMatcher')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('SidecarInjectorLimitCPU') is not None:
            self.sidecar_injector_limit_cpu = m.get('SidecarInjectorLimitCPU')
        if m.get('SidecarInjectorLimitMemory') is not None:
            self.sidecar_injector_limit_memory = m.get('SidecarInjectorLimitMemory')
        if m.get('SidecarInjectorRequestCPU') is not None:
            self.sidecar_injector_request_cpu = m.get('SidecarInjectorRequestCPU')
        if m.get('SidecarInjectorRequestMemory') is not None:
            self.sidecar_injector_request_memory = m.get('SidecarInjectorRequestMemory')
        if m.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = m.get('SidecarInjectorWebhookAsYaml')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('TerminationDrainDuration') is not None:
            self.termination_drain_duration = m.get('TerminationDrainDuration')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        if m.get('TraceCustomTags') is not None:
            self.trace_custom_tags = m.get('TraceCustomTags')
        if m.get('TraceMaxPathTagLength') is not None:
            self.trace_max_path_tag_length = m.get('TraceMaxPathTagLength')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('TracingOnExtZipkinLimitCPU') is not None:
            self.tracing_on_ext_zipkin_limit_cpu = m.get('TracingOnExtZipkinLimitCPU')
        if m.get('TracingOnExtZipkinLimitMemory') is not None:
            self.tracing_on_ext_zipkin_limit_memory = m.get('TracingOnExtZipkinLimitMemory')
        if m.get('TracingOnExtZipkinRequestCPU') is not None:
            self.tracing_on_ext_zipkin_request_cpu = m.get('TracingOnExtZipkinRequestCPU')
        if m.get('TracingOnExtZipkinRequestMemory') is not None:
            self.tracing_on_ext_zipkin_request_memory = m.get('TracingOnExtZipkinRequestMemory')
        if m.get('WebAssemblyFilterEnabled') is not None:
            self.web_assembly_filter_enabled = m.get('WebAssemblyFilterEnabled')
        return self


class UpdateMeshFeatureResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateMeshFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMeshFeatureResponseBody = None,
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
            temp_model = UpdateMeshFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceScopeSidecarConfigRequest(TeaModel):
    def __init__(
        self,
        concurrency: int = None,
        exclude_ipranges: str = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ports: str = None,
        hold_application_until_proxy_starts: bool = None,
        include_ipranges: str = None,
        include_inbound_ports: str = None,
        include_outbound_ports: str = None,
        interception_mode: str = None,
        istio_dnsproxy_enabled: bool = None,
        lifecycle: str = None,
        log_level: str = None,
        namespace: str = None,
        post_start: str = None,
        pre_stop: str = None,
        proxy_init_ack_slo_cpuresource_limit: str = None,
        proxy_init_ack_slo_cpuresource_request: str = None,
        proxy_init_ack_slo_memory_resource_limit: str = None,
        proxy_init_ack_slo_memory_resource_request: str = None,
        proxy_init_cpuresource_limit: str = None,
        proxy_init_cpuresource_request: str = None,
        proxy_init_memory_resource_limit: str = None,
        proxy_init_memory_resource_request: str = None,
        proxy_metadata: str = None,
        proxy_stats_matcher: str = None,
        service_mesh_id: str = None,
        sidecar_proxy_ack_slo_cpuresource_limit: str = None,
        sidecar_proxy_ack_slo_cpuresource_request: str = None,
        sidecar_proxy_ack_slo_memory_resource_limit: str = None,
        sidecar_proxy_ack_slo_memory_resource_request: str = None,
        sidecar_proxy_cpuresource_limit: str = None,
        sidecar_proxy_cpuresource_request: str = None,
        sidecar_proxy_memory_resource_limit: str = None,
        sidecar_proxy_memory_resource_request: str = None,
        termination_drain_duration: str = None,
        tracing: str = None,
    ):
        # The number of worker threads to run in Istio Proxy.
        self.concurrency = concurrency
        # The range of IP addresses that are allowed to access external services. (`global.proxy.excludelPRanges`)
        self.exclude_ipranges = exclude_ipranges
        # The port that the inbound traffic of the sidecar proxy does not pass through.
        self.exclude_inbound_ports = exclude_inbound_ports
        # The port that the outbound traffic of the sidecar proxy does not pass through.
        self.exclude_outbound_ports = exclude_outbound_ports
        # Specifies whether applications can be started only after Istio Proxy starts. Valid values:
        # 
        # *   `true`: Applications can be started only after Istio Proxy starts.
        # *   `false`: Applications can be started before Istio Proxy starts.
        self.hold_application_until_proxy_starts = hold_application_until_proxy_starts
        # The range of IP addresses that are denied to access external services. (`global.proxy.includelPRanges`)
        self.include_ipranges = include_ipranges
        # The port that the inbound traffic of the sidecar proxy passes through.
        self.include_inbound_ports = include_inbound_ports
        # The port that the outbound traffic of the sidecar proxy passes through.
        self.include_outbound_ports = include_outbound_ports
        # The mode in which the sidecar proxy intercepts inbound traffic. Valid values:
        # 
        # *   `REDIRECT`: The sidecar proxy intercepts inbound traffic in the REDIRECT mode.
        # *   `TPROXY`: The sidecar proxy intercepts inbound traffic in the TPROXY mode.
        self.interception_mode = interception_mode
        # Specifies whether to enable the Domain Name System (DNS) proxy feature. Valid values:
        # 
        # *   `true`: The DNS proxy feature is enabled.
        # *   `false`: The DNS proxy feature is disabled.
        self.istio_dnsproxy_enabled = istio_dnsproxy_enabled
        # The lifecycle of the sidecar proxy.
        self.lifecycle = lifecycle
        # The log level. Valid values: `info`, `debug`, `tracing`, and `error`.
        self.log_level = log_level
        # The namespace for which you want to update the sidecar proxy configurations.
        self.namespace = namespace
        # The post-start parameters of Istio Proxy.
        self.post_start = post_start
        # The pre-close parameters of Istio Proxy.
        self.pre_stop = pre_stop
        self.proxy_init_ack_slo_cpuresource_limit = proxy_init_ack_slo_cpuresource_limit
        self.proxy_init_ack_slo_cpuresource_request = proxy_init_ack_slo_cpuresource_request
        self.proxy_init_ack_slo_memory_resource_limit = proxy_init_ack_slo_memory_resource_limit
        self.proxy_init_ack_slo_memory_resource_request = proxy_init_ack_slo_memory_resource_request
        # The maximum number of CPU cores that are available to the sidecar proxy init container.
        self.proxy_init_cpuresource_limit = proxy_init_cpuresource_limit
        # The minimum number of CPU cores that are requested by the sidecar proxy init container.
        self.proxy_init_cpuresource_request = proxy_init_cpuresource_request
        # The maximum size of memory that is available to the sidecar proxy init container.
        self.proxy_init_memory_resource_limit = proxy_init_memory_resource_limit
        # The minimum size of memory that is requested by the sidecar proxy init container.
        self.proxy_init_memory_resource_request = proxy_init_memory_resource_request
        self.proxy_metadata = proxy_metadata
        # The monitoring metrics for data collected by Envoy proxies. The value is in the JSON format.
        self.proxy_stats_matcher = proxy_stats_matcher
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        self.sidecar_proxy_ack_slo_cpuresource_limit = sidecar_proxy_ack_slo_cpuresource_limit
        self.sidecar_proxy_ack_slo_cpuresource_request = sidecar_proxy_ack_slo_cpuresource_request
        self.sidecar_proxy_ack_slo_memory_resource_limit = sidecar_proxy_ack_slo_memory_resource_limit
        self.sidecar_proxy_ack_slo_memory_resource_request = sidecar_proxy_ack_slo_memory_resource_request
        # The maximum number of CPU cores that are available to the sidecar proxy container.
        self.sidecar_proxy_cpuresource_limit = sidecar_proxy_cpuresource_limit
        # The minimum number of CPU cores that are requested by the sidecar proxy container.
        self.sidecar_proxy_cpuresource_request = sidecar_proxy_cpuresource_request
        # The maximum size of memory that is available to the sidecar proxy container.
        self.sidecar_proxy_memory_resource_limit = sidecar_proxy_memory_resource_limit
        # The minimum size of memory that is requested by the sidecar proxy container.
        self.sidecar_proxy_memory_resource_request = sidecar_proxy_memory_resource_request
        # The maximum period of time that the sidecar proxy waits for a request to end.
        self.termination_drain_duration = termination_drain_duration
        # The custom configurations of Tracing Analysis. The configurations must be serialized into JSON strings. The configurations contain the following parameters:
        # 
        # *   `sampling`: The sampling rate, which is of the DOUBLE type.
        # 
        # *   `custom_tags`: The custom tags added to reported spans, which are of the MAP type. The key of a tag is of the string type. The value of a tag is in the JSON format. A custom tag can belong to one of the following types:
        # 
        #     *   `literal`: The tag value is a fixed value in the JSON format. This tag must contain the `value` field that specifies a literal. Example: `{"value":"test"}`.
        #     *   `header`: The tag value is a request header in the JSON format. This tag must contain the `name` field and `defaultValue` field.The name field indicates the name of the request header. The defaultValue field indicates the default value that is used when no request header is available. Example: `{"name":"test","defaultValue":"test"}`.
        #     *   `environment`: The tag value is an environment variable in the JSON format. This tag must contain the `name` field and `defaultValue` field. The name field indicates the name of the environment variable. The defaultValue field indicates the environment variable that is used when no environment variable is available. Example: `{"name":"test","defaultValue":"test"}`.
        self.tracing = tracing

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.hold_application_until_proxy_starts is not None:
            result['HoldApplicationUntilProxyStarts'] = self.hold_application_until_proxy_starts
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.include_inbound_ports is not None:
            result['IncludeInboundPorts'] = self.include_inbound_ports
        if self.include_outbound_ports is not None:
            result['IncludeOutboundPorts'] = self.include_outbound_ports
        if self.interception_mode is not None:
            result['InterceptionMode'] = self.interception_mode
        if self.istio_dnsproxy_enabled is not None:
            result['IstioDNSProxyEnabled'] = self.istio_dnsproxy_enabled
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.proxy_init_ack_slo_cpuresource_limit is not None:
            result['ProxyInitAckSloCPUResourceLimit'] = self.proxy_init_ack_slo_cpuresource_limit
        if self.proxy_init_ack_slo_cpuresource_request is not None:
            result['ProxyInitAckSloCPUResourceRequest'] = self.proxy_init_ack_slo_cpuresource_request
        if self.proxy_init_ack_slo_memory_resource_limit is not None:
            result['ProxyInitAckSloMemoryResourceLimit'] = self.proxy_init_ack_slo_memory_resource_limit
        if self.proxy_init_ack_slo_memory_resource_request is not None:
            result['ProxyInitAckSloMemoryResourceRequest'] = self.proxy_init_ack_slo_memory_resource_request
        if self.proxy_init_cpuresource_limit is not None:
            result['ProxyInitCPUResourceLimit'] = self.proxy_init_cpuresource_limit
        if self.proxy_init_cpuresource_request is not None:
            result['ProxyInitCPUResourceRequest'] = self.proxy_init_cpuresource_request
        if self.proxy_init_memory_resource_limit is not None:
            result['ProxyInitMemoryResourceLimit'] = self.proxy_init_memory_resource_limit
        if self.proxy_init_memory_resource_request is not None:
            result['ProxyInitMemoryResourceRequest'] = self.proxy_init_memory_resource_request
        if self.proxy_metadata is not None:
            result['ProxyMetadata'] = self.proxy_metadata
        if self.proxy_stats_matcher is not None:
            result['ProxyStatsMatcher'] = self.proxy_stats_matcher
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.sidecar_proxy_ack_slo_cpuresource_limit is not None:
            result['SidecarProxyAckSloCPUResourceLimit'] = self.sidecar_proxy_ack_slo_cpuresource_limit
        if self.sidecar_proxy_ack_slo_cpuresource_request is not None:
            result['SidecarProxyAckSloCPUResourceRequest'] = self.sidecar_proxy_ack_slo_cpuresource_request
        if self.sidecar_proxy_ack_slo_memory_resource_limit is not None:
            result['SidecarProxyAckSloMemoryResourceLimit'] = self.sidecar_proxy_ack_slo_memory_resource_limit
        if self.sidecar_proxy_ack_slo_memory_resource_request is not None:
            result['SidecarProxyAckSloMemoryResourceRequest'] = self.sidecar_proxy_ack_slo_memory_resource_request
        if self.sidecar_proxy_cpuresource_limit is not None:
            result['SidecarProxyCPUResourceLimit'] = self.sidecar_proxy_cpuresource_limit
        if self.sidecar_proxy_cpuresource_request is not None:
            result['SidecarProxyCPUResourceRequest'] = self.sidecar_proxy_cpuresource_request
        if self.sidecar_proxy_memory_resource_limit is not None:
            result['SidecarProxyMemoryResourceLimit'] = self.sidecar_proxy_memory_resource_limit
        if self.sidecar_proxy_memory_resource_request is not None:
            result['SidecarProxyMemoryResourceRequest'] = self.sidecar_proxy_memory_resource_request
        if self.termination_drain_duration is not None:
            result['TerminationDrainDuration'] = self.termination_drain_duration
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('HoldApplicationUntilProxyStarts') is not None:
            self.hold_application_until_proxy_starts = m.get('HoldApplicationUntilProxyStarts')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('IncludeInboundPorts') is not None:
            self.include_inbound_ports = m.get('IncludeInboundPorts')
        if m.get('IncludeOutboundPorts') is not None:
            self.include_outbound_ports = m.get('IncludeOutboundPorts')
        if m.get('InterceptionMode') is not None:
            self.interception_mode = m.get('InterceptionMode')
        if m.get('IstioDNSProxyEnabled') is not None:
            self.istio_dnsproxy_enabled = m.get('IstioDNSProxyEnabled')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('ProxyInitAckSloCPUResourceLimit') is not None:
            self.proxy_init_ack_slo_cpuresource_limit = m.get('ProxyInitAckSloCPUResourceLimit')
        if m.get('ProxyInitAckSloCPUResourceRequest') is not None:
            self.proxy_init_ack_slo_cpuresource_request = m.get('ProxyInitAckSloCPUResourceRequest')
        if m.get('ProxyInitAckSloMemoryResourceLimit') is not None:
            self.proxy_init_ack_slo_memory_resource_limit = m.get('ProxyInitAckSloMemoryResourceLimit')
        if m.get('ProxyInitAckSloMemoryResourceRequest') is not None:
            self.proxy_init_ack_slo_memory_resource_request = m.get('ProxyInitAckSloMemoryResourceRequest')
        if m.get('ProxyInitCPUResourceLimit') is not None:
            self.proxy_init_cpuresource_limit = m.get('ProxyInitCPUResourceLimit')
        if m.get('ProxyInitCPUResourceRequest') is not None:
            self.proxy_init_cpuresource_request = m.get('ProxyInitCPUResourceRequest')
        if m.get('ProxyInitMemoryResourceLimit') is not None:
            self.proxy_init_memory_resource_limit = m.get('ProxyInitMemoryResourceLimit')
        if m.get('ProxyInitMemoryResourceRequest') is not None:
            self.proxy_init_memory_resource_request = m.get('ProxyInitMemoryResourceRequest')
        if m.get('ProxyMetadata') is not None:
            self.proxy_metadata = m.get('ProxyMetadata')
        if m.get('ProxyStatsMatcher') is not None:
            self.proxy_stats_matcher = m.get('ProxyStatsMatcher')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('SidecarProxyAckSloCPUResourceLimit') is not None:
            self.sidecar_proxy_ack_slo_cpuresource_limit = m.get('SidecarProxyAckSloCPUResourceLimit')
        if m.get('SidecarProxyAckSloCPUResourceRequest') is not None:
            self.sidecar_proxy_ack_slo_cpuresource_request = m.get('SidecarProxyAckSloCPUResourceRequest')
        if m.get('SidecarProxyAckSloMemoryResourceLimit') is not None:
            self.sidecar_proxy_ack_slo_memory_resource_limit = m.get('SidecarProxyAckSloMemoryResourceLimit')
        if m.get('SidecarProxyAckSloMemoryResourceRequest') is not None:
            self.sidecar_proxy_ack_slo_memory_resource_request = m.get('SidecarProxyAckSloMemoryResourceRequest')
        if m.get('SidecarProxyCPUResourceLimit') is not None:
            self.sidecar_proxy_cpuresource_limit = m.get('SidecarProxyCPUResourceLimit')
        if m.get('SidecarProxyCPUResourceRequest') is not None:
            self.sidecar_proxy_cpuresource_request = m.get('SidecarProxyCPUResourceRequest')
        if m.get('SidecarProxyMemoryResourceLimit') is not None:
            self.sidecar_proxy_memory_resource_limit = m.get('SidecarProxyMemoryResourceLimit')
        if m.get('SidecarProxyMemoryResourceRequest') is not None:
            self.sidecar_proxy_memory_resource_request = m.get('SidecarProxyMemoryResourceRequest')
        if m.get('TerminationDrainDuration') is not None:
            self.termination_drain_duration = m.get('TerminationDrainDuration')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        return self


class UpdateNamespaceScopeSidecarConfigResponseBody(TeaModel):
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


class UpdateNamespaceScopeSidecarConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNamespaceScopeSidecarConfigResponseBody = None,
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
            temp_model = UpdateNamespaceScopeSidecarConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSwimLaneRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        label_selector_key: str = None,
        label_selector_value: str = None,
        service_mesh_id: str = None,
        services_list: str = None,
        swim_lane_name: str = None,
    ):
        # The name of the lane group.
        self.group_name = group_name
        # The label key of the associated service workload. Set the value to `ASM_TRAFFIC_TAG`.
        self.label_selector_key = label_selector_key
        # The label value of the associated service workload.``
        self.label_selector_value = label_selector_value
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # A list of services associated with the lane.
        self.services_list = services_list
        # The name of the lane.
        self.swim_lane_name = swim_lane_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.label_selector_key is not None:
            result['LabelSelectorKey'] = self.label_selector_key
        if self.label_selector_value is not None:
            result['LabelSelectorValue'] = self.label_selector_value
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.services_list is not None:
            result['ServicesList'] = self.services_list
        if self.swim_lane_name is not None:
            result['SwimLaneName'] = self.swim_lane_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('LabelSelectorKey') is not None:
            self.label_selector_key = m.get('LabelSelectorKey')
        if m.get('LabelSelectorValue') is not None:
            self.label_selector_value = m.get('LabelSelectorValue')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServicesList') is not None:
            self.services_list = m.get('ServicesList')
        if m.get('SwimLaneName') is not None:
            self.swim_lane_name = m.get('SwimLaneName')
        return self


class UpdateSwimLaneResponseBody(TeaModel):
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


class UpdateSwimLaneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSwimLaneResponseBody = None,
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
            temp_model = UpdateSwimLaneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSwimLaneGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        service_mesh_id: str = None,
        services_list: str = None,
    ):
        # The name of the lane group.
        self.group_name = group_name
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id
        # A list of services associated with the lane group.
        self.services_list = services_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.services_list is not None:
            result['ServicesList'] = self.services_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServicesList') is not None:
            self.services_list = m.get('ServicesList')
        return self


class UpdateSwimLaneGroupResponseBody(TeaModel):
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


class UpdateSwimLaneGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSwimLaneGroupResponseBody = None,
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
            temp_model = UpdateSwimLaneGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMeshEditionPartiallyRequest(TeaModel):
    def __init__(
        self,
        asmgateway_continue: bool = None,
        expected_version: str = None,
        pre_check: bool = None,
        service_mesh_id: str = None,
        switch_to_pro: bool = None,
        upgrade_gateway_records: str = None,
    ):
        # Specifies whether to upgrade the ASM gateways for the ASM instance. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.asmgateway_continue = asmgateway_continue
        self.expected_version = expected_version
        # 执行升级检查。如果该值设置为true，则只会执行升级检查，并不会实际升级。
        self.pre_check = pre_check
        # The ASM instance ID.
        self.service_mesh_id = service_mesh_id
        # *   ``
        # *   ``
        self.switch_to_pro = switch_to_pro
        # Specifies the ASM gateways to be upgraded. Separate multiple ASM gateways with commas (,).
        self.upgrade_gateway_records = upgrade_gateway_records

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asmgateway_continue is not None:
            result['ASMGatewayContinue'] = self.asmgateway_continue
        if self.expected_version is not None:
            result['ExpectedVersion'] = self.expected_version
        if self.pre_check is not None:
            result['PreCheck'] = self.pre_check
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.switch_to_pro is not None:
            result['SwitchToPro'] = self.switch_to_pro
        if self.upgrade_gateway_records is not None:
            result['UpgradeGatewayRecords'] = self.upgrade_gateway_records
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ASMGatewayContinue') is not None:
            self.asmgateway_continue = m.get('ASMGatewayContinue')
        if m.get('ExpectedVersion') is not None:
            self.expected_version = m.get('ExpectedVersion')
        if m.get('PreCheck') is not None:
            self.pre_check = m.get('PreCheck')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('SwitchToPro') is not None:
            self.switch_to_pro = m.get('SwitchToPro')
        if m.get('UpgradeGatewayRecords') is not None:
            self.upgrade_gateway_records = m.get('UpgradeGatewayRecords')
        return self


class UpgradeMeshEditionPartiallyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpgradeMeshEditionPartiallyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeMeshEditionPartiallyResponseBody = None,
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
            temp_model = UpgradeMeshEditionPartiallyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMeshVersionRequest(TeaModel):
    def __init__(
        self,
        pre_check: bool = None,
        service_mesh_id: str = None,
    ):
        self.pre_check = pre_check
        # The ID of the ASM instance.
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pre_check is not None:
            result['PreCheck'] = self.pre_check
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreCheck') is not None:
            self.pre_check = m.get('PreCheck')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpgradeMeshVersionResponseBody(TeaModel):
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


class UpgradeMeshVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeMeshVersionResponseBody = None,
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
            temp_model = UpgradeMeshVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


