# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddClusterIntoServiceMeshRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        service_mesh_id: str = None,
    ):
        self.cluster_id = cluster_id
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
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
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
        body: AddClusterIntoServiceMeshResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.ecs_id = ecs_id
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
        # Id of the request
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
        body: AddVMIntoServiceMeshResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.body = body
        self.istio_gateway_name = istio_gateway_name
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
        body: CreateASMGatewayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.cert = cert
        self.istio_gateway_name = istio_gateway_name
        self.key = key
        self.secret_name = secret_name
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


class CreateGatewaySecretResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_create_record: Dict[str, SecretCreateRecordValue] = None,
    ):
        self.request_id = request_id
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
        body: CreateGatewaySecretResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.credential = credential
        self.force_https = force_https
        self.hosts = hosts
        self.istio_gateway_name = istio_gateway_name
        self.limit = limit
        self.namespace = namespace
        self.number = number
        self.port_name = port_name
        self.protocol = protocol
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
        body: CreateIstioGatewayDomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.name = name
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
        self.http_status = http_status
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
        self.fixed_delay = fixed_delay
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
        self.abort = abort
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
        self.authority = authority
        self.redirect_code = redirect_code
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
        self.host = host
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
        self.attempts = attempts
        self.per_try_timeout = per_try_timeout
        self.retry_on = retry_on
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
        self.authority = authority
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
        self.delegate = delegate
        self.fault = fault
        self.httpredirect = httpredirect
        self.mirror = mirror
        self.mirror_percentage = mirror_percentage
        self.retries = retries
        self.rewrite = rewrite
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
        self.matching_content = matching_content
        self.matching_mode = matching_mode
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
        self.snihosts = snihosts
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
        self.matching_content = matching_content
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
        self.headers = headers
        self.ports = ports
        self.tlsmatch_attributes = tlsmatch_attributes
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


class CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestination(TeaModel):
    def __init__(
        self,
        host: str = None,
        subset: str = None,
    ):
        self.host = host
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


class CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinations(TeaModel):
    def __init__(
        self,
        destination: CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestination = None,
        weight: int = None,
    ):
        self.destination = destination
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
        httpadvanced_options: CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptions = None,
        match_request: CreateIstioGatewayRoutesRequestGatewayRouteMatchRequest = None,
        namespace: str = None,
        route_destinations: List[CreateIstioGatewayRoutesRequestGatewayRouteRouteDestinations] = None,
        route_name: str = None,
        route_type: str = None,
    ):
        self.httpadvanced_options = httpadvanced_options
        self.match_request = match_request
        self.namespace = namespace
        self.route_destinations = route_destinations
        self.route_name = route_name
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
        if self.httpadvanced_options is not None:
            result['HTTPAdvancedOptions'] = self.httpadvanced_options.to_map()
        if self.match_request is not None:
            result['MatchRequest'] = self.match_request.to_map()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
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
        if m.get('HTTPAdvancedOptions') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptions()
            self.httpadvanced_options = temp_model.from_map(m['HTTPAdvancedOptions'])
        if m.get('MatchRequest') is not None:
            temp_model = CreateIstioGatewayRoutesRequestGatewayRouteMatchRequest()
            self.match_request = temp_model.from_map(m['MatchRequest'])
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
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
        self.description = description
        self.gateway_route = gateway_route
        self.istio_gateway_name = istio_gateway_name
        self.priority = priority
        self.service_mesh_id = service_mesh_id
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
        self.description = description
        self.gateway_route_shrink = gateway_route_shrink
        self.istio_gateway_name = istio_gateway_name
        self.priority = priority
        self.service_mesh_id = service_mesh_id
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
        body: CreateIstioGatewayRoutesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        filter_gateway_cluster_config: bool = None,
        gateway_apienabled: bool = None,
        global_rate_limit_enabled: bool = None,
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
        v_switches: str = None,
        vpc_id: str = None,
        web_assembly_filter_enabled: bool = None,
    ):
        self.access_log_enabled = access_log_enabled
        self.access_log_file = access_log_file
        self.access_log_format = access_log_format
        self.access_log_project = access_log_project
        self.access_log_service_enabled = access_log_service_enabled
        self.access_log_service_host = access_log_service_host
        self.access_log_service_port = access_log_service_port
        self.api_server_load_balancer_spec = api_server_load_balancer_spec
        self.api_server_public_eip = api_server_public_eip
        self.audit_project = audit_project
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.craggregation_enabled = craggregation_enabled
        self.charge_type = charge_type
        self.cluster_spec = cluster_spec
        self.config_source_enabled = config_source_enabled
        self.config_source_nacos_id = config_source_nacos_id
        self.control_plane_log_enabled = control_plane_log_enabled
        self.control_plane_log_project = control_plane_log_project
        self.customized_prometheus = customized_prometheus
        self.customized_zipkin = customized_zipkin
        self.dnsproxying_enabled = dnsproxying_enabled
        self.dubbo_filter_enabled = dubbo_filter_enabled
        self.edition = edition
        self.enable_audit = enable_audit
        self.enable_crhistory = enable_crhistory
        self.enable_sdsserver = enable_sdsserver
        self.exclude_ipranges = exclude_ipranges
        self.exclude_inbound_ports = exclude_inbound_ports
        self.exclude_outbound_ports = exclude_outbound_ports
        self.filter_gateway_cluster_config = filter_gateway_cluster_config
        self.gateway_apienabled = gateway_apienabled
        self.global_rate_limit_enabled = global_rate_limit_enabled
        self.include_ipranges = include_ipranges
        self.istio_version = istio_version
        self.kiali_enabled = kiali_enabled
        self.locality_lbconf = locality_lbconf
        self.locality_load_balancing = locality_load_balancing
        self.mseenabled = mseenabled
        self.multi_buffer_enabled = multi_buffer_enabled
        self.multi_buffer_poll_delay = multi_buffer_poll_delay
        self.mysql_filter_enabled = mysql_filter_enabled
        self.name = name
        self.opalimit_cpu = opalimit_cpu
        self.opalimit_memory = opalimit_memory
        self.opalog_level = opalog_level
        self.oparequest_cpu = oparequest_cpu
        self.oparequest_memory = oparequest_memory
        self.opa_enabled = opa_enabled
        self.open_agent_policy = open_agent_policy
        self.period = period
        self.pilot_load_balancer_spec = pilot_load_balancer_spec
        self.prometheus_url = prometheus_url
        self.proxy_limit_cpu = proxy_limit_cpu
        self.proxy_limit_memory = proxy_limit_memory
        self.proxy_request_cpu = proxy_request_cpu
        self.proxy_request_memory = proxy_request_memory
        self.redis_filter_enabled = redis_filter_enabled
        self.region_id = region_id
        self.telemetry = telemetry
        self.thrift_filter_enabled = thrift_filter_enabled
        self.trace_sampling = trace_sampling
        self.tracing = tracing
        self.v_switches = v_switches
        self.vpc_id = vpc_id
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
        if self.filter_gateway_cluster_config is not None:
            result['FilterGatewayClusterConfig'] = self.filter_gateway_cluster_config
        if self.gateway_apienabled is not None:
            result['GatewayAPIEnabled'] = self.gateway_apienabled
        if self.global_rate_limit_enabled is not None:
            result['GlobalRateLimitEnabled'] = self.global_rate_limit_enabled
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
        if m.get('FilterGatewayClusterConfig') is not None:
            self.filter_gateway_cluster_config = m.get('FilterGatewayClusterConfig')
        if m.get('GatewayAPIEnabled') is not None:
            self.gateway_apienabled = m.get('GatewayAPIEnabled')
        if m.get('GlobalRateLimitEnabled') is not None:
            self.global_rate_limit_enabled = m.get('GlobalRateLimitEnabled')
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
        self.request_id = request_id
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
        body: CreateServiceMeshResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayRouteRequest(TeaModel):
    def __init__(
        self,
        istio_gateway_name: str = None,
        route_name: str = None,
        service_mesh_id: str = None,
    ):
        self.istio_gateway_name = istio_gateway_name
        self.route_name = route_name
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
        body: DeleteGatewayRouteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.istio_gateway_name = istio_gateway_name
        self.secret_name = secret_name
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


class DeleteGatewaySecretResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_delete_record: Dict[str, SecretDeleteRecordValue] = None,
    ):
        self.request_id = request_id
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
        body: DeleteGatewaySecretResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.hosts = hosts
        self.istio_gateway_name = istio_gateway_name
        self.limit = limit
        self.namespace = namespace
        self.port_name = port_name
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
        body: DeleteIstioGatewayDomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.force = force
        self.retain_resources = retain_resources
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
        body: DeleteServiceMeshResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeASMGatewayImportedServicesRequest(TeaModel):
    def __init__(
        self,
        asmgateway_name: str = None,
        service_mesh_id: str = None,
        service_namespace: str = None,
    ):
        self.asmgateway_name = asmgateway_name
        self.service_mesh_id = service_mesh_id
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
        self.service_name = service_name
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
        self.imported_services = imported_services
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
        body: DescribeASMGatewayImportedServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeASMGatewayImportedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAhasProRequest(TeaModel):
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


class DescribeAhasProResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
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


class DescribeAhasProResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAhasProResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAhasProResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCCMVersionRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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


class DescribeCCMVersionResponseBody(TeaModel):
    def __init__(
        self,
        ccmversions: Dict[str, CCMVersionsValue] = None,
        request_id: str = None,
    ):
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
        body: DescribeCCMVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCCMVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCensRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        self.clusters = clusters
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
        body: DescribeCensResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.k_8s_cluster_id = k_8s_cluster_id
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
        self.title = title
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
        self.dashboards = dashboards
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
        body: DescribeClusterGrafanaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.k_8s_cluster_id = k_8s_cluster_id
        self.k_8s_cluster_region_id = k_8s_cluster_region_id
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
        self.prometheus = prometheus
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
        body: DescribeClusterPrometheusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeClusterPrometheusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersInServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        self.title = title
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
        self.access_log_dashboards = access_log_dashboards
        self.cluster_domain = cluster_domain
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.creation_time = creation_time
        self.error_message = error_message
        self.logtail_installed_state = logtail_installed_state
        self.name = name
        self.region_id = region_id
        self.sg_id = sg_id
        self.state = state
        self.update_time = update_time
        self.version = version
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
        self.clusters = clusters
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
        body: DescribeClustersInServiceMeshResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.istio_version = istio_version
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
        self.chinese_name = chinese_name
        self.english_name = english_name
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
        self.request_id = request_id
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
        body: DescribeCrTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCrTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewaySecretDetailsRequest(TeaModel):
    def __init__(
        self,
        istio_gateway_name: str = None,
        service_mesh_id: str = None,
    ):
        self.istio_gateway_name = istio_gateway_name
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
        self.expired_time = expired_time
        self.gateway_name = gateway_name
        self.issue_time = issue_time
        self.message = message
        self.sni = sni
        self.secret_name = secret_name
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
        self.gateway_secret_details = gateway_secret_details
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
        body: DescribeGatewaySecretDetailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGatewaySecretDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGuestClusterAccessLogDashboardsRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
    ):
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
        self.title = title
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
        self.dashboards = dashboards
        self.k_8s_cluster_id = k_8s_cluster_id
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
        body: DescribeGuestClusterAccessLogDashboardsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGuestClusterAccessLogDashboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGuestClusterNamespacesRequest(TeaModel):
    def __init__(
        self,
        guest_cluster_id: str = None,
        service_mesh_id: str = None,
    ):
        self.guest_cluster_id = guest_cluster_id
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
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestClusterID') is not None:
            self.guest_cluster_id = m.get('GuestClusterID')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeGuestClusterNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        ns_list: List[str] = None,
        request_id: str = None,
    ):
        self.ns_list = ns_list
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ns_list is not None:
            result['NsList'] = self.ns_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NsList') is not None:
            self.ns_list = m.get('NsList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGuestClusterNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGuestClusterNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.guest_cluster_id = guest_cluster_id
        self.namespace = namespace
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
        self.pod_list = pod_list
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
        body: DescribeGuestClusterPodsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.asmgateway_name = asmgateway_name
        self.service_mesh_id = service_mesh_id
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
        self.name = name
        self.node_port = node_port
        self.port = port
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
        self.cluster_ids = cluster_ids
        self.labels = labels
        self.namespace = namespace
        self.ports = ports
        self.service_name = service_name
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
        self.details = details
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
        body: DescribeImportedServicesDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeImportedServicesDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIngressGatewaysRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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


class DescribeIngressGatewaysResponseBody(TeaModel):
    def __init__(
        self,
        ingress_gateways: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.ingress_gateways = ingress_gateways
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_gateways is not None:
            result['IngressGateways'] = self.ingress_gateways
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressGateways') is not None:
            self.ingress_gateways = m.get('IngressGateways')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIngressGatewaysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIngressGatewaysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIngressGatewaysResponseBody()
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
        self.istio_gateway_name = istio_gateway_name
        self.limit = limit
        self.namespace = namespace
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
        namespace: str = None,
        port_name: str = None,
        protocol: str = None,
    ):
        self.credential_name = credential_name
        self.detail = detail
        self.domains = domains
        self.namespace = namespace
        self.port_name = port_name
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
        self.gateway_secret_details = gateway_secret_details
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
        body: DescribeIstioGatewayDomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.istio_gateway_name = istio_gateway_name
        self.route_name = route_name
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
        self.name = name
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
        self.http_status = http_status
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
        self.exponential_delay = exponential_delay
        self.fixed_delay = fixed_delay
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
        self.abort = abort
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
        self.authority = authority
        self.redirect_code = redirect_code
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
        self.host = host
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
        self.attempts = attempts
        self.per_try_timeout = per_try_timeout
        self.retry_on = retry_on
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
        self.authority = authority
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
        self.delegate = delegate
        self.fault = fault
        self.httpredirect = httpredirect
        self.mirror = mirror
        self.mirror_percentage = mirror_percentage
        self.retries = retries
        self.rewrite = rewrite
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
        self.matching_content = matching_content
        self.matching_mode = matching_mode
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
        self.snihosts = snihosts
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
        self.matching_content = matching_content
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
        self.headers = headers
        self.ports = ports
        self.tlsmatch_attributes = tlsmatch_attributes
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
        self.host = host
        self.port = port
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
        self.add = add
        self.remove = remove
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
        self.add = add
        self.remove = remove
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
        self.request = request
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
        self.destination = destination
        self.headers = headers
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
        httpadvanced_options: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptions = None,
        match_request: DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequest = None,
        route_destinations: List[DescribeIstioGatewayRouteDetailResponseBodyRouteDetailRouteDestinations] = None,
        route_name: str = None,
        route_type: str = None,
    ):
        self.httpadvanced_options = httpadvanced_options
        self.match_request = match_request
        self.route_destinations = route_destinations
        self.route_name = route_name
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
        if self.httpadvanced_options is not None:
            result['HTTPAdvancedOptions'] = self.httpadvanced_options.to_map()
        if self.match_request is not None:
            result['MatchRequest'] = self.match_request.to_map()
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
        if m.get('HTTPAdvancedOptions') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailHTTPAdvancedOptions()
            self.httpadvanced_options = temp_model.from_map(m['HTTPAdvancedOptions'])
        if m.get('MatchRequest') is not None:
            temp_model = DescribeIstioGatewayRouteDetailResponseBodyRouteDetailMatchRequest()
            self.match_request = temp_model.from_map(m['MatchRequest'])
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
        self.description = description
        self.namespace = namespace
        self.priority = priority
        self.request_id = request_id
        self.route_detail = route_detail
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
        body: DescribeIstioGatewayRouteDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.istio_gateway_name = istio_gateway_name
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
        namespace: str = None,
        priority: int = None,
        route_name: str = None,
        route_path: str = None,
        status: int = None,
    ):
        self.asmgateway_name = asmgateway_name
        self.description = description
        self.namespace = namespace
        self.priority = priority
        self.route_name = route_name
        self.route_path = route_path
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
        self.management_routes = management_routes
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
        body: DescribeIstioGatewayRoutesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIstioGatewayRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeManagedServicesRequest(TeaModel):
    def __init__(
        self,
        guest_cluster: str = None,
        limit: int = None,
        marker: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        self.guest_cluster = guest_cluster
        self.limit = limit
        self.marker = marker
        self.namespace = namespace
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
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestCluster') is not None:
            self.guest_cluster = m.get('GuestCluster')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeManagedServicesResponseBodyManagedServiceInfoDeploymentInstances(TeaModel):
    def __init__(
        self,
        ready_replicas: int = None,
        replicas: int = None,
        version: str = None,
    ):
        self.ready_replicas = ready_replicas
        self.replicas = replicas
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ready_replicas is not None:
            result['ReadyReplicas'] = self.ready_replicas
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadyReplicas') is not None:
            self.ready_replicas = m.get('ReadyReplicas')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeManagedServicesResponseBodyManagedServiceInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deployment_instances: List[DescribeManagedServicesResponseBodyManagedServiceInfoDeploymentInstances] = None,
        message: str = None,
        selector: Dict[str, str] = None,
        service_name: str = None,
        sidecar_inject_status: str = None,
    ):
        self.create_time = create_time
        self.deployment_instances = deployment_instances
        self.message = message
        self.selector = selector
        self.service_name = service_name
        self.sidecar_inject_status = sidecar_inject_status

    def validate(self):
        if self.deployment_instances:
            for k in self.deployment_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DeploymentInstances'] = []
        if self.deployment_instances is not None:
            for k in self.deployment_instances:
                result['DeploymentInstances'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.selector is not None:
            result['Selector'] = self.selector
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.sidecar_inject_status is not None:
            result['SidecarInjectStatus'] = self.sidecar_inject_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.deployment_instances = []
        if m.get('DeploymentInstances') is not None:
            for k in m.get('DeploymentInstances'):
                temp_model = DescribeManagedServicesResponseBodyManagedServiceInfoDeploymentInstances()
                self.deployment_instances.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Selector') is not None:
            self.selector = m.get('Selector')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SidecarInjectStatus') is not None:
            self.sidecar_inject_status = m.get('SidecarInjectStatus')
        return self


class DescribeManagedServicesResponseBody(TeaModel):
    def __init__(
        self,
        managed_service_info: List[DescribeManagedServicesResponseBodyManagedServiceInfo] = None,
        mark: str = None,
        request_id: str = None,
    ):
        self.managed_service_info = managed_service_info
        self.mark = mark
        self.request_id = request_id

    def validate(self):
        if self.managed_service_info:
            for k in self.managed_service_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ManagedServiceInfo'] = []
        if self.managed_service_info is not None:
            for k in self.managed_service_info:
                result['ManagedServiceInfo'].append(k.to_map() if k else None)
        if self.mark is not None:
            result['Mark'] = self.mark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.managed_service_info = []
        if m.get('ManagedServiceInfo') is not None:
            for k in m.get('ManagedServiceInfo'):
                temp_model = DescribeManagedServicesResponseBodyManagedServiceInfo()
                self.managed_service_info.append(temp_model.from_map(k))
        if m.get('Mark') is not None:
            self.mark = m.get('Mark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeManagedServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeManagedServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeManagedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceScopeSidecarConfigRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        service_mesh_id: str = None,
    ):
        self.namespace = namespace
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


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceLimit(TeaModel):
    def __init__(
        self,
        resource_cpulimit: str = None,
        resource_memory_limit: str = None,
    ):
        self.resource_cpulimit = resource_cpulimit
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
        self.resource_cpurequest = resource_cpurequest
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
        self.resource_cpulimit = resource_cpulimit
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
        self.resource_cpurequest = resource_cpurequest
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


class DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatches(TeaModel):
    def __init__(
        self,
        exclude_inbound_ports: str = None,
        exclude_outbound_ipranges: str = None,
        exclude_outbound_ports: str = None,
        include_inbound_ports: str = None,
        include_outbound_ipranges: str = None,
        include_outbound_ports: str = None,
        istio_dnsproxy_enabled: bool = None,
        lifecycle_str: str = None,
        sidecar_proxy_init_resource_limit: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceLimit = None,
        sidecar_proxy_init_resource_request: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyInitResourceRequest = None,
        sidecar_proxy_resource_limit: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceLimit = None,
        sidecar_proxy_resource_request: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatchesSidecarProxyResourceRequest = None,
        termination_drain_duration: str = None,
    ):
        self.exclude_inbound_ports = exclude_inbound_ports
        self.exclude_outbound_ipranges = exclude_outbound_ipranges
        self.exclude_outbound_ports = exclude_outbound_ports
        self.include_inbound_ports = include_inbound_ports
        self.include_outbound_ipranges = include_outbound_ipranges
        self.include_outbound_ports = include_outbound_ports
        self.istio_dnsproxy_enabled = istio_dnsproxy_enabled
        self.lifecycle_str = lifecycle_str
        self.sidecar_proxy_init_resource_limit = sidecar_proxy_init_resource_limit
        self.sidecar_proxy_init_resource_request = sidecar_proxy_init_resource_request
        self.sidecar_proxy_resource_limit = sidecar_proxy_resource_limit
        self.sidecar_proxy_resource_request = sidecar_proxy_resource_request
        self.termination_drain_duration = termination_drain_duration

    def validate(self):
        if self.sidecar_proxy_init_resource_limit:
            self.sidecar_proxy_init_resource_limit.validate()
        if self.sidecar_proxy_init_resource_request:
            self.sidecar_proxy_init_resource_request.validate()
        if self.sidecar_proxy_resource_limit:
            self.sidecar_proxy_resource_limit.validate()
        if self.sidecar_proxy_resource_request:
            self.sidecar_proxy_resource_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ipranges is not None:
            result['ExcludeOutboundIPRanges'] = self.exclude_outbound_ipranges
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.include_inbound_ports is not None:
            result['IncludeInboundPorts'] = self.include_inbound_ports
        if self.include_outbound_ipranges is not None:
            result['IncludeOutboundIPRanges'] = self.include_outbound_ipranges
        if self.include_outbound_ports is not None:
            result['IncludeOutboundPorts'] = self.include_outbound_ports
        if self.istio_dnsproxy_enabled is not None:
            result['IstioDNSProxyEnabled'] = self.istio_dnsproxy_enabled
        if self.lifecycle_str is not None:
            result['LifecycleStr'] = self.lifecycle_str
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundIPRanges') is not None:
            self.exclude_outbound_ipranges = m.get('ExcludeOutboundIPRanges')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('IncludeInboundPorts') is not None:
            self.include_inbound_ports = m.get('IncludeInboundPorts')
        if m.get('IncludeOutboundIPRanges') is not None:
            self.include_outbound_ipranges = m.get('IncludeOutboundIPRanges')
        if m.get('IncludeOutboundPorts') is not None:
            self.include_outbound_ports = m.get('IncludeOutboundPorts')
        if m.get('IstioDNSProxyEnabled') is not None:
            self.istio_dnsproxy_enabled = m.get('IstioDNSProxyEnabled')
        if m.get('LifecycleStr') is not None:
            self.lifecycle_str = m.get('LifecycleStr')
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
        return self


class DescribeNamespaceScopeSidecarConfigResponseBody(TeaModel):
    def __init__(
        self,
        config_patches: DescribeNamespaceScopeSidecarConfigResponseBodyConfigPatches = None,
        request_id: str = None,
    ):
        self.config_patches = config_patches
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
        body: DescribeNamespaceScopeSidecarConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeNamespaceScopeSidecarConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodesInstanceTypeRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        multi_buffer_enabled: bool = None,
        node_type: str = None,
    ):
        self.multi_buffer_enabled = multi_buffer_enabled
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.multi_buffer_enabled is not None:
            result['MultiBufferEnabled'] = self.multi_buffer_enabled
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MultiBufferEnabled') is not None:
            self.multi_buffer_enabled = m.get('MultiBufferEnabled')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class DescribeNodesInstanceTypeResponseBody(TeaModel):
    def __init__(
        self,
        instance_types: List[DescribeNodesInstanceTypeResponseBodyInstanceTypes] = None,
        request_id: str = None,
    ):
        self.instance_types = instance_types
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
        body: DescribeNodesInstanceTypeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.k_8s_cluster_id = k_8s_cluster_id
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
        self.load_balancer_id = load_balancer_id
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
        self.request_id = request_id
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
        body: DescribeReusableSlbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeReusableSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceAccessDetailRequest(TeaModel):
    def __init__(
        self,
        guest_cluster: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
        service_name: str = None,
    ):
        self.guest_cluster = guest_cluster
        self.namespace = namespace
        self.service_mesh_id = service_mesh_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster is not None:
            result['GuestCluster'] = self.guest_cluster
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestCluster') is not None:
            self.guest_cluster = m.get('GuestCluster')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeServiceAccessDetailResponseBodyAccessDetail(TeaModel):
    def __init__(
        self,
        cluster_ip: str = None,
        name: str = None,
        ports: str = None,
        type: str = None,
    ):
        self.cluster_ip = cluster_ip
        self.name = name
        self.ports = ports
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_ip is not None:
            result['ClusterIP'] = self.cluster_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterIP') is not None:
            self.cluster_ip = m.get('ClusterIP')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeServiceAccessDetailResponseBody(TeaModel):
    def __init__(
        self,
        access_detail: DescribeServiceAccessDetailResponseBodyAccessDetail = None,
        request_id: str = None,
    ):
        self.access_detail = access_detail
        self.request_id = request_id

    def validate(self):
        if self.access_detail:
            self.access_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_detail is not None:
            result['AccessDetail'] = self.access_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDetail') is not None:
            temp_model = DescribeServiceAccessDetailResponseBodyAccessDetail()
            self.access_detail = temp_model.from_map(m['AccessDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceAccessDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceAccessDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServiceAccessDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceManagedResourceRequest(TeaModel):
    def __init__(
        self,
        guest_cluster: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
        service_name: str = None,
    ):
        self.guest_cluster = guest_cluster
        self.namespace = namespace
        self.service_mesh_id = service_mesh_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster is not None:
            result['GuestCluster'] = self.guest_cluster
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestCluster') is not None:
            self.guest_cluster = m.get('GuestCluster')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeServiceManagedResourceResponseBodyManagedResource(TeaModel):
    def __init__(
        self,
        destination_rules: List[str] = None,
        local_rate_limiters: List[str] = None,
        virtual_services: List[str] = None,
    ):
        self.destination_rules = destination_rules
        self.local_rate_limiters = local_rate_limiters
        self.virtual_services = virtual_services

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_rules is not None:
            result['DestinationRules'] = self.destination_rules
        if self.local_rate_limiters is not None:
            result['LocalRateLimiters'] = self.local_rate_limiters
        if self.virtual_services is not None:
            result['VirtualServices'] = self.virtual_services
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRules') is not None:
            self.destination_rules = m.get('DestinationRules')
        if m.get('LocalRateLimiters') is not None:
            self.local_rate_limiters = m.get('LocalRateLimiters')
        if m.get('VirtualServices') is not None:
            self.virtual_services = m.get('VirtualServices')
        return self


class DescribeServiceManagedResourceResponseBody(TeaModel):
    def __init__(
        self,
        managed_resource: DescribeServiceManagedResourceResponseBodyManagedResource = None,
        request_id: str = None,
    ):
        self.managed_resource = managed_resource
        self.request_id = request_id

    def validate(self):
        if self.managed_resource:
            self.managed_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.managed_resource is not None:
            result['ManagedResource'] = self.managed_resource.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedResource') is not None:
            temp_model = DescribeServiceManagedResourceResponseBodyManagedResource()
            self.managed_resource = temp_model.from_map(m['ManagedResource'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceManagedResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceManagedResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServiceManagedResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshAdditionalStatusRequest(TeaModel):
    def __init__(
        self,
        check_mode: str = None,
        service_mesh_id: str = None,
    ):
        self.check_mode = check_mode
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
        pay_type: str = None,
        reused: bool = None,
        slbback_end_server_num_status: str = None,
        slbexist_status: str = None,
    ):
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
        pay_type: str = None,
        reused: bool = None,
        slbback_end_server_num_status: str = None,
        slbexist_status: str = None,
    ):
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
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Reused') is not None:
            self.reused = m.get('Reused')
        if m.get('SLBBackEndServerNumStatus') is not None:
            self.slbback_end_server_num_status = m.get('SLBBackEndServerNumStatus')
        if m.get('SLBExistStatus') is not None:
            self.slbexist_status = m.get('SLBExistStatus')
        return self


class ClusterStatusLogtailStatusRecordValueAccessLogDashboards(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
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


class ClusterStatusLogtailStatusRecordValue(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        logtail_detail_status: str = None,
        access_log_dashboards: List[ClusterStatusLogtailStatusRecordValueAccessLogDashboards] = None,
    ):
        self.cluster_id = cluster_id
        self.logtail_detail_status = logtail_detail_status
        self.access_log_dashboards = access_log_dashboards

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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.logtail_detail_status is not None:
            result['LogtailDetailStatus'] = self.logtail_detail_status
        result['AccessLogDashboards'] = []
        if self.access_log_dashboards is not None:
            for k in self.access_log_dashboards:
                result['AccessLogDashboards'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('LogtailDetailStatus') is not None:
            self.logtail_detail_status = m.get('LogtailDetailStatus')
        self.access_log_dashboards = []
        if m.get('AccessLogDashboards') is not None:
            for k in m.get('AccessLogDashboards'):
                temp_model = ClusterStatusLogtailStatusRecordValueAccessLogDashboards()
                self.access_log_dashboards.append(temp_model.from_map(k))
        return self


class DescribeServiceMeshAdditionalStatusResponseBodyClusterStatus(TeaModel):
    def __init__(
        self,
        access_log_project_status: str = None,
        api_server_eipstatus: str = None,
        api_server_load_balancer_status: DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusApiServerLoadBalancerStatus = None,
        audit_project_status: str = None,
        control_plane_project_status: str = None,
        logtail_status_record: Dict[str, ClusterStatusLogtailStatusRecordValue] = None,
        pilot_load_balancer_status: DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusPilotLoadBalancerStatus = None,
        sg_status: str = None,
    ):
        self.access_log_project_status = access_log_project_status
        self.api_server_eipstatus = api_server_eipstatus
        self.api_server_load_balancer_status = api_server_load_balancer_status
        self.audit_project_status = audit_project_status
        self.control_plane_project_status = control_plane_project_status
        self.logtail_status_record = logtail_status_record
        self.pilot_load_balancer_status = pilot_load_balancer_status
        self.sg_status = sg_status

    def validate(self):
        if self.api_server_load_balancer_status:
            self.api_server_load_balancer_status.validate()
        if self.logtail_status_record:
            for v in self.logtail_status_record.values():
                if v:
                    v.validate()
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
        if self.control_plane_project_status is not None:
            result['ControlPlaneProjectStatus'] = self.control_plane_project_status
        result['LogtailStatusRecord'] = {}
        if self.logtail_status_record is not None:
            for k, v in self.logtail_status_record.items():
                result['LogtailStatusRecord'][k] = v.to_map()
        if self.pilot_load_balancer_status is not None:
            result['PilotLoadBalancerStatus'] = self.pilot_load_balancer_status.to_map()
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
        if m.get('ControlPlaneProjectStatus') is not None:
            self.control_plane_project_status = m.get('ControlPlaneProjectStatus')
        self.logtail_status_record = {}
        if m.get('LogtailStatusRecord') is not None:
            for k, v in m.get('LogtailStatusRecord').items():
                temp_model = ClusterStatusLogtailStatusRecordValue()
                self.logtail_status_record[k] = temp_model.from_map(v)
        if m.get('PilotLoadBalancerStatus') is not None:
            temp_model = DescribeServiceMeshAdditionalStatusResponseBodyClusterStatusPilotLoadBalancerStatus()
            self.pilot_load_balancer_status = temp_model.from_map(m['PilotLoadBalancerStatus'])
        if m.get('SgStatus') is not None:
            self.sg_status = m.get('SgStatus')
        return self


class DescribeServiceMeshAdditionalStatusResponseBody(TeaModel):
    def __init__(
        self,
        cluster_status: DescribeServiceMeshAdditionalStatusResponseBodyClusterStatus = None,
        request_id: str = None,
    ):
        self.cluster_status = cluster_status
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
        body: DescribeServiceMeshAdditionalStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.limit = limit
        self.offset = offset
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
        name: str = None,
        region_id: str = None,
        service_mesh_id: str = None,
        sg_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
        vpc_id: str = None,
    ):
        self.cluster_domain = cluster_domain
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.creation_time = creation_time
        self.error_message = error_message
        self.forbidden_flag = forbidden_flag
        self.name = name
        self.region_id = region_id
        self.service_mesh_id = service_mesh_id
        self.sg_id = sg_id
        self.state = state
        self.update_time = update_time
        self.version = version
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
        request_id: str = None,
    ):
        self.clusters = clusters
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
                temp_model = DescribeServiceMeshClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceMeshClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceMeshClustersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServiceMeshClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshDetailRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        self.intranet_api_server_endpoint = intranet_api_server_endpoint
        self.intranet_pilot_endpoint = intranet_pilot_endpoint
        self.public_api_server_endpoint = public_api_server_endpoint
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
        self.creation_time = creation_time
        self.error_message = error_message
        self.name = name
        self.profile = profile
        self.region_id = region_id
        self.service_mesh_id = service_mesh_id
        self.state = state
        self.update_time = update_time
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
        self.api_server_loadbalancer_id = api_server_loadbalancer_id
        self.api_server_public_eip = api_server_public_eip
        self.pilot_public_eip = pilot_public_eip
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
        self.enabled = enabled
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
        self.audit_project_status = audit_project_status
        self.enabled = enabled
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
        self.enabled = enabled
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
        self.istiod_image_tag = istiod_image_tag
        self.name = name
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


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationIstioCRHistory(TeaModel):
    def __init__(
        self,
        enable_history: bool = None,
    ):
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
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGetHTTPHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGet(TeaModel):
    def __init__(
        self,
        httpheaders: List[DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGetHTTPHeaders] = None,
        host: str = None,
        port: str = None,
        scheme: str = None,
    ):
        self.httpheaders = httpheaders
        self.host = host
        self.port = port
        self.scheme = scheme

    def validate(self):
        if self.httpheaders:
            for k in self.httpheaders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HTTPHeaders'] = []
        if self.httpheaders is not None:
            for k in self.httpheaders:
                result['HTTPHeaders'].append(k.to_map() if k else None)
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.httpheaders = []
        if m.get('HTTPHeaders') is not None:
            for k in m.get('HTTPHeaders'):
                temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGetHTTPHeaders()
                self.httpheaders.append(temp_model.from_map(k))
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartTCPSocket(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStart(TeaModel):
    def __init__(
        self,
        exec: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartExec = None,
        httpget: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGet = None,
        tcpsocket: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartTCPSocket = None,
    ):
        self.exec = exec
        self.httpget = httpget
        self.tcpsocket = tcpsocket

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.httpget:
            self.httpget.validate()
        if self.tcpsocket:
            self.tcpsocket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.httpget is not None:
            result['HTTPGet'] = self.httpget.to_map()
        if self.tcpsocket is not None:
            result['TCPSocket'] = self.tcpsocket.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('HTTPGet') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartHTTPGet()
            self.httpget = temp_model.from_map(m['HTTPGet'])
        if m.get('TCPSocket') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStartTCPSocket()
            self.tcpsocket = temp_model.from_map(m['TCPSocket'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopExec(TeaModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGetHTTPHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGet(TeaModel):
    def __init__(
        self,
        httpheaders: List[DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGetHTTPHeaders] = None,
        host: str = None,
        port: str = None,
        scheme: str = None,
    ):
        self.httpheaders = httpheaders
        self.host = host
        self.port = port
        self.scheme = scheme

    def validate(self):
        if self.httpheaders:
            for k in self.httpheaders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HTTPHeaders'] = []
        if self.httpheaders is not None:
            for k in self.httpheaders:
                result['HTTPHeaders'].append(k.to_map() if k else None)
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.httpheaders = []
        if m.get('HTTPHeaders') is not None:
            for k in m.get('HTTPHeaders'):
                temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGetHTTPHeaders()
                self.httpheaders.append(temp_model.from_map(k))
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopTCPSocket(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: str = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStop(TeaModel):
    def __init__(
        self,
        exec: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopExec = None,
        httpget: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGet = None,
        tcpsocket: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopTCPSocket = None,
    ):
        self.exec = exec
        self.httpget = httpget
        self.tcpsocket = tcpsocket

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.httpget:
            self.httpget.validate()
        if self.tcpsocket:
            self.tcpsocket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()
        if self.httpget is not None:
            result['HTTPGet'] = self.httpget.to_map()
        if self.tcpsocket is not None:
            result['TCPSocket'] = self.tcpsocket.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopExec()
            self.exec = temp_model.from_map(m['Exec'])
        if m.get('HTTPGet') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopHTTPGet()
            self.httpget = temp_model.from_map(m['HTTPGet'])
        if m.get('TCPSocket') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStopTCPSocket()
            self.tcpsocket = temp_model.from_map(m['TCPSocket'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecycle(TeaModel):
    def __init__(
        self,
        post_start: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStart = None,
        pre_stop: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStop = None,
    ):
        self.post_start = post_start
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
            result['PostStart'] = self.post_start.to_map()
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostStart') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePostStart()
            self.post_start = temp_model.from_map(m['PostStart'])
        if m.get('PreStop') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecyclePreStop()
            self.pre_stop = temp_model.from_map(m['PreStop'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationMultiBuffer(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        poll_delay: str = None,
    ):
        self.enabled = enabled
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


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationOPAScopeInjection(TeaModel):
    def __init__(
        self,
        opascope_injected: bool = None,
    ):
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


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationRateLimit(TeaModel):
    def __init__(
        self,
        enable_global_rate_limit: bool = None,
    ):
        self.enable_global_rate_limit = enable_global_rate_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_global_rate_limit is not None:
            result['EnableGlobalRateLimit'] = self.enable_global_rate_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableGlobalRateLimit') is not None:
            self.enable_global_rate_limit = m.get('EnableGlobalRateLimit')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceLimit(TeaModel):
    def __init__(
        self,
        resource_cpulimit: str = None,
        resource_memory_limit: str = None,
    ):
        self.resource_cpulimit = resource_cpulimit
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
        self.resource_cpurequest = resource_cpurequest
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
        craggregation_enabled: bool = None,
        discovery_selectors: List[Dict[str, Any]] = None,
        istio_crhistory: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationIstioCRHistory = None,
        lifecycle: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationLifecycle = None,
        multi_buffer: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationMultiBuffer = None,
        opascope_injection: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationOPAScopeInjection = None,
        rate_limit: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationRateLimit = None,
        sidecar_proxy_init_resource_limit: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceLimit = None,
        sidecar_proxy_init_resource_request: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationSidecarProxyInitResourceRequest = None,
        termination_drain_duration: str = None,
    ):
        self.craggregation_enabled = craggregation_enabled
        self.discovery_selectors = discovery_selectors
        self.istio_crhistory = istio_crhistory
        self.lifecycle = lifecycle
        self.multi_buffer = multi_buffer
        self.opascope_injection = opascope_injection
        self.rate_limit = rate_limit
        self.sidecar_proxy_init_resource_limit = sidecar_proxy_init_resource_limit
        self.sidecar_proxy_init_resource_request = sidecar_proxy_init_resource_request
        self.termination_drain_duration = termination_drain_duration

    def validate(self):
        if self.istio_crhistory:
            self.istio_crhistory.validate()
        if self.lifecycle:
            self.lifecycle.validate()
        if self.multi_buffer:
            self.multi_buffer.validate()
        if self.opascope_injection:
            self.opascope_injection.validate()
        if self.rate_limit:
            self.rate_limit.validate()
        if self.sidecar_proxy_init_resource_limit:
            self.sidecar_proxy_init_resource_limit.validate()
        if self.sidecar_proxy_init_resource_request:
            self.sidecar_proxy_init_resource_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.opascope_injection is not None:
            result['OPAScopeInjection'] = self.opascope_injection.to_map()
        if self.rate_limit is not None:
            result['RateLimit'] = self.rate_limit.to_map()
        if self.sidecar_proxy_init_resource_limit is not None:
            result['SidecarProxyInitResourceLimit'] = self.sidecar_proxy_init_resource_limit.to_map()
        if self.sidecar_proxy_init_resource_request is not None:
            result['SidecarProxyInitResourceRequest'] = self.sidecar_proxy_init_resource_request.to_map()
        if self.termination_drain_duration is not None:
            result['TerminationDrainDuration'] = self.termination_drain_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        if m.get('OPAScopeInjection') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationOPAScopeInjection()
            self.opascope_injection = temp_model.from_map(m['OPAScopeInjection'])
        if m.get('RateLimit') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigExtraConfigurationRateLimit()
            self.rate_limit = temp_model.from_map(m['RateLimit'])
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
        self.enabled = enabled
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
        self.distribute = distribute
        self.enabled = enabled
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
        self.enabled = enabled
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory
        self.log_level = log_level
        self.request_cpu = request_cpu
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
        self.enabled = enabled
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
        self.enable_sdsserver = enable_sdsserver
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
        self.config_source = config_source
        self.feature = feature
        self.http_10enabled = http_10enabled
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
        self.external_url = external_url
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
        self.dubbo_filter_enabled = dubbo_filter_enabled
        self.mysql_filter_enabled = mysql_filter_enabled
        self.redis_filter_enabled = redis_filter_enabled
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
        self.access_log_file = access_log_file
        self.access_log_format = access_log_format
        self.access_log_service_enabled = access_log_service_enabled
        self.access_log_service_host = access_log_service_host
        self.access_log_service_port = access_log_service_port
        self.cluster_domain = cluster_domain
        self.enable_dnsproxying = enable_dnsproxying
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory
        self.request_cpu = request_cpu
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
        self.enabled = enabled
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
        sidecar_injector_webhook_as_yaml: str = None,
    ):
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.enable_namespaces_by_default = enable_namespaces_by_default
        self.init_cniconfiguration = init_cniconfiguration
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory
        self.request_cpu = request_cpu
        self.request_memory = request_memory
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
        if m.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = m.get('SidecarInjectorWebhookAsYaml')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
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
        self.access_log = access_log
        self.audit = audit
        self.control_plane_log_info = control_plane_log_info
        self.customized_zipkin = customized_zipkin
        self.edition = edition
        self.enable_locality_lb = enable_locality_lb
        self.exclude_ipranges = exclude_ipranges
        self.exclude_inbound_ports = exclude_inbound_ports
        self.exclude_outbound_ports = exclude_outbound_ports
        self.extra_configuration = extra_configuration
        self.include_ipranges = include_ipranges
        self.k_8s_new_apis_support = k_8s_new_apis_support
        self.kiali = kiali
        self.locality_lb = locality_lb
        self.mse = mse
        self.opa = opa
        self.outbound_traffic_policy = outbound_traffic_policy
        self.pilot = pilot
        self.prometheus = prometheus
        self.protocol_support = protocol_support
        self.proxy = proxy
        self.sidecar_injector = sidecar_injector
        self.telemetry = telemetry
        self.tracing = tracing
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
        self.security_group_id = security_group_id
        self.v_switches = v_switches
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
        self.load_balancer = load_balancer
        self.mesh_config = mesh_config
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
        service_mesh_info: DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo = None,
        spec: DescribeServiceMeshDetailResponseBodyServiceMeshSpec = None,
    ):
        self.cluster_spec = cluster_spec
        self.clusters = clusters
        self.endpoints = endpoints
        self.service_mesh_info = service_mesh_info
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
        self.request_id = request_id
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
        body: DescribeServiceMeshDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.private_ip_address = private_ip_address
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
        self.kubeconfig = kubeconfig
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
        body: DescribeServiceMeshKubeconfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServiceMeshKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshLogsRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        self.creation_time = creation_time
        self.log = log
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
        self.logs = logs
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
        body: DescribeServiceMeshLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServiceMeshLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshProxyStatusRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        self.cluster_synced = cluster_synced
        self.endpoint_percent = endpoint_percent
        self.endpoint_synced = endpoint_synced
        self.istio_version = istio_version
        self.listener_synced = listener_synced
        self.proxy_id = proxy_id
        self.proxy_version = proxy_version
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
        self.code = code
        self.message = message
        self.proxy_status = proxy_status
        self.request_id = request_id
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
        body: DescribeServiceMeshProxyStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServiceMeshProxyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshServiceLabelRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        service_names: str = None,
        service_namespaces: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.service_names = service_names
        self.service_namespaces = service_namespaces

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.service_names is not None:
            result['ServiceNames'] = self.service_names
        if self.service_namespaces is not None:
            result['ServiceNamespaces'] = self.service_namespaces
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServiceNames') is not None:
            self.service_names = m.get('ServiceNames')
        if m.get('ServiceNamespaces') is not None:
            self.service_namespaces = m.get('ServiceNamespaces')
        return self


class ServiceLabelsValue(TeaModel):
    def __init__(
        self,
        labels: Dict[str, str] = None,
        success: bool = None,
    ):
        self.labels = labels
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeServiceMeshServiceLabelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_labels: Dict[str, ServiceLabelsValue] = None,
    ):
        self.request_id = request_id
        self.service_labels = service_labels

    def validate(self):
        if self.service_labels:
            for v in self.service_labels.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceLabels'] = {}
        if self.service_labels is not None:
            for k, v in self.service_labels.items():
                result['ServiceLabels'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_labels = {}
        if m.get('ServiceLabels') is not None:
            for k, v in m.get('ServiceLabels').items():
                temp_model = ServiceLabelsValue()
                self.service_labels[k] = temp_model.from_map(v)
        return self


class DescribeServiceMeshServiceLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServiceMeshServiceLabelResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServiceMeshServiceLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshUpgradeStatusRequest(TeaModel):
    def __init__(
        self,
        all_istio_gateway_full_names: str = None,
        guest_cluster_ids: str = None,
        service_mesh_id: str = None,
    ):
        self.all_istio_gateway_full_names = all_istio_gateway_full_names
        self.guest_cluster_ids = guest_cluster_ids
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


class DescribeServiceMeshUpgradeStatusResponseBodyUpgradeDetail(TeaModel):
    def __init__(
        self,
        finished_gateways_num: int = None,
        gateway_status_record: Dict[str, UpgradeDetailGatewayStatusRecordValue] = None,
        mesh_status: str = None,
        total_gateways_num: int = None,
    ):
        self.finished_gateways_num = finished_gateways_num
        self.gateway_status_record = gateway_status_record
        self.mesh_status = mesh_status
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
        self.request_id = request_id
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
        body: DescribeServiceMeshUpgradeStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServiceMeshUpgradeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshVMsRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        self.has_tag = has_tag
        self.host_name = host_name
        self.instance_id = instance_id
        self.ip_address = ip_address
        self.region = region
        self.security_group_ids = security_group_ids
        self.service_mesh_id = service_mesh_id
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
        # Id of the request
        self.request_id = request_id
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
        body: DescribeServiceMeshVMsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.intranet_api_server_endpoint = intranet_api_server_endpoint
        self.intranet_pilot_endpoint = intranet_pilot_endpoint
        self.public_api_server_endpoint = public_api_server_endpoint
        self.public_pilot_endpoint = public_pilot_endpoint
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
        self.creation_time = creation_time
        self.error_message = error_message
        self.name = name
        self.profile = profile
        self.region_id = region_id
        self.service_mesh_id = service_mesh_id
        self.state = state
        self.update_time = update_time
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
        self.api_server_loadbalancer_id = api_server_loadbalancer_id
        self.api_server_public_eip = api_server_public_eip
        self.pilot_public_eip = pilot_public_eip
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
        self.http_10enabled = http_10enabled
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
        self.enabled = enabled
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
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.enable_namespaces_by_default = enable_namespaces_by_default
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
        self.mtls = mtls
        self.outbound_traffic_policy = outbound_traffic_policy
        self.pilot = pilot
        self.sidecar_injector = sidecar_injector
        self.strict_mtls = strict_mtls
        self.telemetry = telemetry
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
        self.security_group_id = security_group_id
        self.v_switches = v_switches
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
        self.load_balancer = load_balancer
        self.mesh_config = mesh_config
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
        service_mesh_info: DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo = None,
        spec: DescribeServiceMeshesResponseBodyServiceMeshesSpec = None,
    ):
        self.cluster_spec = cluster_spec
        self.clusters = clusters
        self.endpoints = endpoints
        self.service_mesh_info = service_mesh_info
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
        self.request_id = request_id
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
        body: DescribeServiceMeshesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServiceMeshesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUpgradeVersionRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        self.istio_operator_version = istio_operator_version
        self.istio_version = istio_version
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
        self.request_id = request_id
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
        body: DescribeUpgradeVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUpgradeVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersWithPermissionsRequest(TeaModel):
    def __init__(
        self,
        user_type: str = None,
    ):
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
        self.request_id = request_id
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
        body: DescribeUsersWithPermissionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUsersWithPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVMsInServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        self.has_tag = has_tag
        self.host_name = host_name
        self.instance_id = instance_id
        self.ip_address = ip_address
        self.region = region
        self.security_group_ids = security_group_ids
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
        # Id of the request
        self.request_id = request_id
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
        body: DescribeVMsInServiceMeshResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.region_id = region_id
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
    ):
        self.is_default = is_default
        self.status = status
        self.v_switch_id = v_switch_id
        self.v_switch_name = v_switch_name
        self.vpc_id = vpc_id

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
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # VSwitches
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
        body: DescribeVSwitchesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVersionManagementRequest(TeaModel):
    def __init__(
        self,
        guest_cluster: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
        service_name: str = None,
    ):
        self.guest_cluster = guest_cluster
        self.namespace = namespace
        self.service_mesh_id = service_mesh_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster is not None:
            result['GuestCluster'] = self.guest_cluster
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestCluster') is not None:
            self.guest_cluster = m.get('GuestCluster')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeVersionManagementResponseBodyVersionDetailsPodInstances(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        namespace: str = None,
        node_ip: str = None,
        pod_ip: str = None,
        pod_name: str = None,
    ):
        self.create_time = create_time
        self.namespace = namespace
        self.node_ip = node_ip
        self.pod_ip = pod_ip
        self.pod_name = pod_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.pod_ip is not None:
            result['PodIP'] = self.pod_ip
        if self.pod_name is not None:
            result['PodName'] = self.pod_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PodIP') is not None:
            self.pod_ip = m.get('PodIP')
        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')
        return self


class DescribeVersionManagementResponseBodyVersionDetails(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deployment_name: str = None,
        images: List[str] = None,
        inject: bool = None,
        pod_instances: List[DescribeVersionManagementResponseBodyVersionDetailsPodInstances] = None,
        ready_replicas: int = None,
        replicas: int = None,
        version: str = None,
    ):
        self.create_time = create_time
        self.deployment_name = deployment_name
        self.images = images
        self.inject = inject
        self.pod_instances = pod_instances
        self.ready_replicas = ready_replicas
        self.replicas = replicas
        self.version = version

    def validate(self):
        if self.pod_instances:
            for k in self.pod_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deployment_name is not None:
            result['DeploymentName'] = self.deployment_name
        if self.images is not None:
            result['Images'] = self.images
        if self.inject is not None:
            result['Inject'] = self.inject
        result['PodInstances'] = []
        if self.pod_instances is not None:
            for k in self.pod_instances:
                result['PodInstances'].append(k.to_map() if k else None)
        if self.ready_replicas is not None:
            result['ReadyReplicas'] = self.ready_replicas
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeploymentName') is not None:
            self.deployment_name = m.get('DeploymentName')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('Inject') is not None:
            self.inject = m.get('Inject')
        self.pod_instances = []
        if m.get('PodInstances') is not None:
            for k in m.get('PodInstances'):
                temp_model = DescribeVersionManagementResponseBodyVersionDetailsPodInstances()
                self.pod_instances.append(temp_model.from_map(k))
        if m.get('ReadyReplicas') is not None:
            self.ready_replicas = m.get('ReadyReplicas')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeVersionManagementResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version_details: List[DescribeVersionManagementResponseBodyVersionDetails] = None,
    ):
        self.request_id = request_id
        self.version_details = version_details

    def validate(self):
        if self.version_details:
            for k in self.version_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['VersionDetails'] = []
        if self.version_details is not None:
            for k in self.version_details:
                result['VersionDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.version_details = []
        if m.get('VersionDetails') is not None:
            for k in m.get('VersionDetails'):
                temp_model = DescribeVersionManagementResponseBodyVersionDetails()
                self.version_details.append(temp_model.from_map(k))
        return self


class DescribeVersionManagementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeVersionManagementResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVersionManagementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVersionsResponseBodyVersionInfo(TeaModel):
    def __init__(
        self,
        edition: str = None,
        versions: List[str] = None,
    ):
        self.edition = edition
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
        self.request_id = request_id
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
        body: DescribeVersionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcsRequest(TeaModel):
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


class DescribeVpcsResponseBodyVpcs(TeaModel):
    def __init__(
        self,
        is_default: bool = None,
        status: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.is_default = is_default
        self.status = status
        self.vpc_id = vpc_id
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
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count
        # Vpcs
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
        body: DescribeVpcsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCaCertRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        # base64 encode format
        self.ca_cert = ca_cert
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
        body: GetCaCertResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCaCertResponseBody()
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
        self.cluster_ids = cluster_ids
        self.name = name
        self.namespace = namespace
        self.service_mesh_id = service_mesh_id
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
        self.address = address
        self.hostname = hostname
        self.pod_name = pod_name
        self.ports = ports
        self.region = region
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
        self.endpoints_details = endpoints_details
        self.location = location
        self.namespace = namespace
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
        self.address = address
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
        self.end_point_slice = end_point_slice
        self.request_id = request_id
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
        body: GetRegisteredServiceEndpointsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRegisteredServiceEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisteredServiceNamespacesRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        self.namespaces = namespaces
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
        body: GetRegisteredServiceNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetRegisteredServiceNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVmAppMeshInfoRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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
        self.data = data
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
        body: GetVmAppMeshInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.namespace = namespace
        self.service_account = service_account
        self.service_mesh_id = service_mesh_id
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
        self.envoy_env_content = envoy_env_content
        self.hosts_content = hosts_content
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
        self.request_id = request_id
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
        body: GetVmMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVmMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
        service_mesh_id: str = None,
    ):
        self.k_8s_cluster_id = k_8s_cluster_id
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


class ListDashboardResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class ListDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyServiceMeshNameRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        service_mesh_id: str = None,
    ):
        self.name = name
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
        body: ModifyServiceMeshNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.enable_audit = enable_audit
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
        self.data = data
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
        body: ReActivateAuditResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReActivateAuditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClusterFromServiceMeshRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        service_mesh_id: str = None,
    ):
        self.cluster_id = cluster_id
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
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
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
        body: RemoveClusterFromServiceMeshResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.ecs_id = ecs_id
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
        # Id of the request
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
        body: RemoveVMFromServiceMeshResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.private_ip_address = private_ip_address
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
        self.kubeconfig = kubeconfig
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
        body: RevokeKubeconfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.body = body
        self.istio_gateway_name = istio_gateway_name
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
        body: UpdateASMGatewayResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
        self.asmgateway_name = asmgateway_name
        self.service_mesh_id = service_mesh_id
        self.service_names = service_names
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
        body: UpdateASMGatewayImportedServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateASMGatewayImportedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInjectedProxyConfigRequest(TeaModel):
    def __init__(
        self,
        deployment_names: str = None,
        guest_cluster: str = None,
        limit_cpus: str = None,
        limit_memories: str = None,
        namespace: str = None,
        request_cpus: str = None,
        request_memories: str = None,
        service_mesh_id: str = None,
    ):
        self.deployment_names = deployment_names
        self.guest_cluster = guest_cluster
        self.limit_cpus = limit_cpus
        self.limit_memories = limit_memories
        self.namespace = namespace
        self.request_cpus = request_cpus
        self.request_memories = request_memories
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_names is not None:
            result['DeploymentNames'] = self.deployment_names
        if self.guest_cluster is not None:
            result['GuestCluster'] = self.guest_cluster
        if self.limit_cpus is not None:
            result['LimitCPUs'] = self.limit_cpus
        if self.limit_memories is not None:
            result['LimitMemories'] = self.limit_memories
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.request_cpus is not None:
            result['RequestCPUs'] = self.request_cpus
        if self.request_memories is not None:
            result['RequestMemories'] = self.request_memories
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentNames') is not None:
            self.deployment_names = m.get('DeploymentNames')
        if m.get('GuestCluster') is not None:
            self.guest_cluster = m.get('GuestCluster')
        if m.get('LimitCPUs') is not None:
            self.limit_cpus = m.get('LimitCPUs')
        if m.get('LimitMemories') is not None:
            self.limit_memories = m.get('LimitMemories')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RequestCPUs') is not None:
            self.request_cpus = m.get('RequestCPUs')
        if m.get('RequestMemories') is not None:
            self.request_memories = m.get('RequestMemories')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpdateInjectedProxyConfigResponseBody(TeaModel):
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


class UpdateInjectedProxyConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInjectedProxyConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateInjectedProxyConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptionsDelegate(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
    ):
        self.name = name
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
        self.http_status = http_status
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
        self.fixed_delay = fixed_delay
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
        self.abort = abort
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
        self.authority = authority
        self.redirect_code = redirect_code
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
        self.host = host
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
        self.attempts = attempts
        self.per_try_timeout = per_try_timeout
        self.retry_on = retry_on
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
        self.authority = authority
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
        self.delegate = delegate
        self.fault = fault
        self.httpredirect = httpredirect
        self.mirror = mirror
        self.mirror_percentage = mirror_percentage
        self.retries = retries
        self.rewrite = rewrite
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
        self.matching_content = matching_content
        self.matching_mode = matching_mode
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
        self.snihosts = snihosts
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
        self.matching_content = matching_content
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
        self.headers = headers
        self.ports = ports
        self.tlsmatch_attributes = tlsmatch_attributes
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


class UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestination(TeaModel):
    def __init__(
        self,
        host: str = None,
        subset: str = None,
    ):
        self.host = host
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


class UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinations(TeaModel):
    def __init__(
        self,
        destination: UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinationsDestination = None,
        weight: int = None,
    ):
        self.destination = destination
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
        httpadvanced_options: UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptions = None,
        match_request: UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequest = None,
        namespace: str = None,
        route_destinations: List[UpdateIstioGatewayRoutesRequestGatewayRouteRouteDestinations] = None,
        route_name: str = None,
        route_type: str = None,
    ):
        self.httpadvanced_options = httpadvanced_options
        self.match_request = match_request
        self.namespace = namespace
        self.route_destinations = route_destinations
        self.route_name = route_name
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
        if self.httpadvanced_options is not None:
            result['HTTPAdvancedOptions'] = self.httpadvanced_options.to_map()
        if self.match_request is not None:
            result['MatchRequest'] = self.match_request.to_map()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
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
        if m.get('HTTPAdvancedOptions') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteHTTPAdvancedOptions()
            self.httpadvanced_options = temp_model.from_map(m['HTTPAdvancedOptions'])
        if m.get('MatchRequest') is not None:
            temp_model = UpdateIstioGatewayRoutesRequestGatewayRouteMatchRequest()
            self.match_request = temp_model.from_map(m['MatchRequest'])
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
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
        self.description = description
        self.gateway_route = gateway_route
        self.istio_gateway_name = istio_gateway_name
        self.priority = priority
        self.service_mesh_id = service_mesh_id
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
        self.description = description
        self.gateway_route_shrink = gateway_route_shrink
        self.istio_gateway_name = istio_gateway_name
        self.priority = priority
        self.service_mesh_id = service_mesh_id
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
        body: UpdateIstioGatewayRoutesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateIstioGatewayRoutesResponseBody()
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
        self.description = description
        self.istio_gateway_name = istio_gateway_name
        self.priority = priority
        self.route_name = route_name
        self.service_mesh_id = service_mesh_id
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
        body: UpdateIstioRouteAdditionalStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateIstioRouteAdditionalStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMeshFeatureRequest(TeaModel):
    def __init__(
        self,
        access_log_enabled: bool = None,
        access_log_file: str = None,
        access_log_format: str = None,
        access_log_project: str = None,
        access_log_service_enabled: bool = None,
        access_log_service_host: str = None,
        access_log_service_port: int = None,
        audit_project: str = None,
        auto_injection_policy_enabled: bool = None,
        craggregation_enabled: bool = None,
        canary_upgrade_enabled: bool = None,
        cluster_spec: str = None,
        cni_enabled: bool = None,
        cni_exclude_namespaces: str = None,
        config_source_enabled: bool = None,
        config_source_nacos_id: str = None,
        customized_prometheus: bool = None,
        customized_zipkin: bool = None,
        dnsproxying_enabled: bool = None,
        discovery_selectors: str = None,
        dubbo_filter_enabled: bool = None,
        enable_audit: bool = None,
        enable_crhistory: bool = None,
        enable_namespaces_by_default: bool = None,
        enable_sdsserver: bool = None,
        exclude_ipranges: str = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ports: str = None,
        filter_gateway_cluster_config: bool = None,
        gateway_apienabled: bool = None,
        global_rate_limit_enabled: bool = None,
        http_10enabled: bool = None,
        include_ipranges: str = None,
        include_inbound_ports: str = None,
        kiali_enabled: bool = None,
        lifecycle: str = None,
        locality_lbconf: str = None,
        locality_load_balancing: bool = None,
        mseenabled: bool = None,
        multi_buffer_enabled: bool = None,
        multi_buffer_poll_delay: str = None,
        mysql_filter_enabled: bool = None,
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
        trace_sampling: float = None,
        tracing: bool = None,
        web_assembly_filter_enabled: bool = None,
    ):
        self.access_log_enabled = access_log_enabled
        self.access_log_file = access_log_file
        self.access_log_format = access_log_format
        self.access_log_project = access_log_project
        self.access_log_service_enabled = access_log_service_enabled
        self.access_log_service_host = access_log_service_host
        self.access_log_service_port = access_log_service_port
        self.audit_project = audit_project
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.craggregation_enabled = craggregation_enabled
        self.canary_upgrade_enabled = canary_upgrade_enabled
        self.cluster_spec = cluster_spec
        self.cni_enabled = cni_enabled
        self.cni_exclude_namespaces = cni_exclude_namespaces
        self.config_source_enabled = config_source_enabled
        self.config_source_nacos_id = config_source_nacos_id
        self.customized_prometheus = customized_prometheus
        self.customized_zipkin = customized_zipkin
        self.dnsproxying_enabled = dnsproxying_enabled
        self.discovery_selectors = discovery_selectors
        self.dubbo_filter_enabled = dubbo_filter_enabled
        self.enable_audit = enable_audit
        self.enable_crhistory = enable_crhistory
        self.enable_namespaces_by_default = enable_namespaces_by_default
        self.enable_sdsserver = enable_sdsserver
        self.exclude_ipranges = exclude_ipranges
        self.exclude_inbound_ports = exclude_inbound_ports
        self.exclude_outbound_ports = exclude_outbound_ports
        self.filter_gateway_cluster_config = filter_gateway_cluster_config
        self.gateway_apienabled = gateway_apienabled
        self.global_rate_limit_enabled = global_rate_limit_enabled
        self.http_10enabled = http_10enabled
        self.include_ipranges = include_ipranges
        self.include_inbound_ports = include_inbound_ports
        self.kiali_enabled = kiali_enabled
        self.lifecycle = lifecycle
        self.locality_lbconf = locality_lbconf
        self.locality_load_balancing = locality_load_balancing
        self.mseenabled = mseenabled
        self.multi_buffer_enabled = multi_buffer_enabled
        self.multi_buffer_poll_delay = multi_buffer_poll_delay
        self.mysql_filter_enabled = mysql_filter_enabled
        self.opainjector_cpulimit = opainjector_cpulimit
        self.opainjector_cpurequirement = opainjector_cpurequirement
        self.opainjector_memory_limit = opainjector_memory_limit
        self.opainjector_memory_requirement = opainjector_memory_requirement
        self.opalimit_cpu = opalimit_cpu
        self.opalimit_memory = opalimit_memory
        self.opalog_level = opalog_level
        self.oparequest_cpu = oparequest_cpu
        self.oparequest_memory = oparequest_memory
        self.opascope_injected = opascope_injected
        self.opa_enabled = opa_enabled
        self.open_agent_policy = open_agent_policy
        self.outbound_traffic_policy = outbound_traffic_policy
        self.prometheus_url = prometheus_url
        self.proxy_init_cpuresource_limit = proxy_init_cpuresource_limit
        self.proxy_init_cpuresource_request = proxy_init_cpuresource_request
        self.proxy_init_memory_resource_limit = proxy_init_memory_resource_limit
        self.proxy_init_memory_resource_request = proxy_init_memory_resource_request
        self.proxy_limit_cpu = proxy_limit_cpu
        self.proxy_limit_memory = proxy_limit_memory
        self.proxy_request_cpu = proxy_request_cpu
        self.proxy_request_memory = proxy_request_memory
        self.redis_filter_enabled = redis_filter_enabled
        self.service_mesh_id = service_mesh_id
        self.sidecar_injector_limit_cpu = sidecar_injector_limit_cpu
        self.sidecar_injector_limit_memory = sidecar_injector_limit_memory
        self.sidecar_injector_request_cpu = sidecar_injector_request_cpu
        self.sidecar_injector_request_memory = sidecar_injector_request_memory
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml
        self.telemetry = telemetry
        self.termination_drain_duration = termination_drain_duration
        self.thrift_filter_enabled = thrift_filter_enabled
        self.trace_sampling = trace_sampling
        self.tracing = tracing
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
        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.craggregation_enabled is not None:
            result['CRAggregationEnabled'] = self.craggregation_enabled
        if self.canary_upgrade_enabled is not None:
            result['CanaryUpgradeEnabled'] = self.canary_upgrade_enabled
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.cni_enabled is not None:
            result['CniEnabled'] = self.cni_enabled
        if self.cni_exclude_namespaces is not None:
            result['CniExcludeNamespaces'] = self.cni_exclude_namespaces
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
        if self.discovery_selectors is not None:
            result['DiscoverySelectors'] = self.discovery_selectors
        if self.dubbo_filter_enabled is not None:
            result['DubboFilterEnabled'] = self.dubbo_filter_enabled
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
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
        if self.global_rate_limit_enabled is not None:
            result['GlobalRateLimitEnabled'] = self.global_rate_limit_enabled
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.include_inbound_ports is not None:
            result['IncludeInboundPorts'] = self.include_inbound_ports
        if self.kiali_enabled is not None:
            result['KialiEnabled'] = self.kiali_enabled
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
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
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.tracing is not None:
            result['Tracing'] = self.tracing
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
        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('CRAggregationEnabled') is not None:
            self.craggregation_enabled = m.get('CRAggregationEnabled')
        if m.get('CanaryUpgradeEnabled') is not None:
            self.canary_upgrade_enabled = m.get('CanaryUpgradeEnabled')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('CniEnabled') is not None:
            self.cni_enabled = m.get('CniEnabled')
        if m.get('CniExcludeNamespaces') is not None:
            self.cni_exclude_namespaces = m.get('CniExcludeNamespaces')
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
        if m.get('DiscoverySelectors') is not None:
            self.discovery_selectors = m.get('DiscoverySelectors')
        if m.get('DubboFilterEnabled') is not None:
            self.dubbo_filter_enabled = m.get('DubboFilterEnabled')
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
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
        if m.get('GlobalRateLimitEnabled') is not None:
            self.global_rate_limit_enabled = m.get('GlobalRateLimitEnabled')
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('IncludeInboundPorts') is not None:
            self.include_inbound_ports = m.get('IncludeInboundPorts')
        if m.get('KialiEnabled') is not None:
            self.kiali_enabled = m.get('KialiEnabled')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
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
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('WebAssemblyFilterEnabled') is not None:
            self.web_assembly_filter_enabled = m.get('WebAssemblyFilterEnabled')
        return self


class UpdateMeshFeatureResponseBody(TeaModel):
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


class UpdateMeshFeatureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateMeshFeatureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateMeshFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceScopeSidecarConfigRequest(TeaModel):
    def __init__(
        self,
        exclude_ipranges: str = None,
        exclude_inbound_ports: str = None,
        exclude_outbound_ports: str = None,
        include_ipranges: str = None,
        include_inbound_ports: str = None,
        include_outbound_ports: str = None,
        istio_dnsproxy_enabled: bool = None,
        lifecycle: str = None,
        namespace: str = None,
        proxy_init_cpuresource_limit: str = None,
        proxy_init_cpuresource_request: str = None,
        proxy_init_memory_resource_limit: str = None,
        proxy_init_memory_resource_request: str = None,
        service_mesh_id: str = None,
        sidecar_proxy_cpuresource_limit: str = None,
        sidecar_proxy_cpuresource_request: str = None,
        sidecar_proxy_memory_resource_limit: str = None,
        sidecar_proxy_memory_resource_request: str = None,
        termination_drain_duration: str = None,
    ):
        self.exclude_ipranges = exclude_ipranges
        self.exclude_inbound_ports = exclude_inbound_ports
        self.exclude_outbound_ports = exclude_outbound_ports
        self.include_ipranges = include_ipranges
        self.include_inbound_ports = include_inbound_ports
        self.include_outbound_ports = include_outbound_ports
        self.istio_dnsproxy_enabled = istio_dnsproxy_enabled
        self.lifecycle = lifecycle
        self.namespace = namespace
        self.proxy_init_cpuresource_limit = proxy_init_cpuresource_limit
        self.proxy_init_cpuresource_request = proxy_init_cpuresource_request
        self.proxy_init_memory_resource_limit = proxy_init_memory_resource_limit
        self.proxy_init_memory_resource_request = proxy_init_memory_resource_request
        self.service_mesh_id = service_mesh_id
        self.sidecar_proxy_cpuresource_limit = sidecar_proxy_cpuresource_limit
        self.sidecar_proxy_cpuresource_request = sidecar_proxy_cpuresource_request
        self.sidecar_proxy_memory_resource_limit = sidecar_proxy_memory_resource_limit
        self.sidecar_proxy_memory_resource_request = sidecar_proxy_memory_resource_request
        self.termination_drain_duration = termination_drain_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.include_inbound_ports is not None:
            result['IncludeInboundPorts'] = self.include_inbound_ports
        if self.include_outbound_ports is not None:
            result['IncludeOutboundPorts'] = self.include_outbound_ports
        if self.istio_dnsproxy_enabled is not None:
            result['IstioDNSProxyEnabled'] = self.istio_dnsproxy_enabled
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.proxy_init_cpuresource_limit is not None:
            result['ProxyInitCPUResourceLimit'] = self.proxy_init_cpuresource_limit
        if self.proxy_init_cpuresource_request is not None:
            result['ProxyInitCPUResourceRequest'] = self.proxy_init_cpuresource_request
        if self.proxy_init_memory_resource_limit is not None:
            result['ProxyInitMemoryResourceLimit'] = self.proxy_init_memory_resource_limit
        if self.proxy_init_memory_resource_request is not None:
            result['ProxyInitMemoryResourceRequest'] = self.proxy_init_memory_resource_request
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('IncludeInboundPorts') is not None:
            self.include_inbound_ports = m.get('IncludeInboundPorts')
        if m.get('IncludeOutboundPorts') is not None:
            self.include_outbound_ports = m.get('IncludeOutboundPorts')
        if m.get('IstioDNSProxyEnabled') is not None:
            self.istio_dnsproxy_enabled = m.get('IstioDNSProxyEnabled')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ProxyInitCPUResourceLimit') is not None:
            self.proxy_init_cpuresource_limit = m.get('ProxyInitCPUResourceLimit')
        if m.get('ProxyInitCPUResourceRequest') is not None:
            self.proxy_init_cpuresource_request = m.get('ProxyInitCPUResourceRequest')
        if m.get('ProxyInitMemoryResourceLimit') is not None:
            self.proxy_init_memory_resource_limit = m.get('ProxyInitMemoryResourceLimit')
        if m.get('ProxyInitMemoryResourceRequest') is not None:
            self.proxy_init_memory_resource_request = m.get('ProxyInitMemoryResourceRequest')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
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
        return self


class UpdateNamespaceScopeSidecarConfigResponseBody(TeaModel):
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


class UpdateNamespaceScopeSidecarConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNamespaceScopeSidecarConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateNamespaceScopeSidecarConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceSidecarInjectRequest(TeaModel):
    def __init__(
        self,
        guest_cluster: str = None,
        inject: bool = None,
        limit_cpu: str = None,
        limit_memory: str = None,
        namespace: str = None,
        request_cpu: str = None,
        request_memory: str = None,
        service_mesh_id: str = None,
        service_name: str = None,
    ):
        self.guest_cluster = guest_cluster
        self.inject = inject
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory
        self.namespace = namespace
        self.request_cpu = request_cpu
        self.request_memory = request_memory
        self.service_mesh_id = service_mesh_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster is not None:
            result['GuestCluster'] = self.guest_cluster
        if self.inject is not None:
            result['Inject'] = self.inject
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestCluster') is not None:
            self.guest_cluster = m.get('GuestCluster')
        if m.get('Inject') is not None:
            self.inject = m.get('Inject')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class UpdateServiceSidecarInjectResponseBody(TeaModel):
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


class UpdateServiceSidecarInjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServiceSidecarInjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateServiceSidecarInjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUnlabeledServiceManagedResourceRequest(TeaModel):
    def __init__(
        self,
        guest_cluster: str = None,
        namespace: str = None,
        service_mesh_id: str = None,
        service_name: str = None,
    ):
        self.guest_cluster = guest_cluster
        self.namespace = namespace
        self.service_mesh_id = service_mesh_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guest_cluster is not None:
            result['GuestCluster'] = self.guest_cluster
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GuestCluster') is not None:
            self.guest_cluster = m.get('GuestCluster')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class UpdateUnlabeledServiceManagedResourceResponseBody(TeaModel):
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


class UpdateUnlabeledServiceManagedResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUnlabeledServiceManagedResourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUnlabeledServiceManagedResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMeshEditionPartiallyRequest(TeaModel):
    def __init__(
        self,
        asmgateway_continue: bool = None,
        service_mesh_id: str = None,
        switch_to_pro: bool = None,
        upgrade_gateway_records: str = None,
    ):
        self.asmgateway_continue = asmgateway_continue
        self.service_mesh_id = service_mesh_id
        self.switch_to_pro = switch_to_pro
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
        body: UpgradeMeshEditionPartiallyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeMeshEditionPartiallyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMeshVersionRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
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


class UpgradeMeshVersionResponseBody(TeaModel):
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


class UpgradeMeshVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeMeshVersionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeMeshVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClusterStatusLogtailStatusRecordValueValue(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
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


