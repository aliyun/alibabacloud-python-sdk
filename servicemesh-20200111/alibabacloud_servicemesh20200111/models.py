# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class GetServiceRegistrySourceRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetServiceRegistrySourceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.status = status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result, 'result')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetServiceRegistrySourceRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        config: Dict[str, Any] = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.config = config

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.config, 'config')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class SetServiceRegistrySourceShrinkRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        config_shrink: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.config_shrink = config_shrink

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.config_shrink, 'config_shrink')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')
        return self


class SetServiceRegistrySourceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result, 'result')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetAutoInjectionLabelSyncStatusRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetAutoInjectionLabelSyncStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
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


class AddVmAppToMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        namespace: str = None,
        service_name: str = None,
        ips: str = None,
        ports: str = None,
        labels: str = None,
        annotations: str = None,
        service_account: str = None,
        force: bool = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.namespace = namespace
        self.service_name = service_name
        self.ips = ips
        self.ports = ports
        self.labels = labels
        self.annotations = annotations
        self.service_account = service_account
        self.force = force

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.service_name, 'service_name')
        self.validate_required(self.ips, 'ips')
        self.validate_required(self.ports, 'ports')
        self.validate_required(self.labels, 'labels')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.service_account is not None:
            result['ServiceAccount'] = self.service_account
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ServiceAccount') is not None:
            self.service_account = m.get('ServiceAccount')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class AddVmAppToMeshResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetVmAppMeshInfoRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetVmAppMeshInfoResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetVmMetaRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        trust_domain: str = None,
        namespace: str = None,
        service_account: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.trust_domain = trust_domain
        self.namespace = namespace
        self.service_account = service_account

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.trust_domain is not None:
            result['TrustDomain'] = self.trust_domain
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_account is not None:
            result['ServiceAccount'] = self.service_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('TrustDomain') is not None:
            self.trust_domain = m.get('TrustDomain')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceAccount') is not None:
            self.service_account = m.get('ServiceAccount')
        return self


class GetVmMetaResponseVmMetaInfo(TeaModel):
    def __init__(
        self,
        root_cert_path: str = None,
        root_cert_content: str = None,
        key_path: str = None,
        key_content: str = None,
        cert_chain_path: str = None,
        cert_chain_content: str = None,
        envoy_env_path: str = None,
        envoy_env_content: str = None,
        hosts_path: str = None,
        hosts_content: str = None,
        token_path: str = None,
        token_content: str = None,
    ):
        self.root_cert_path = root_cert_path
        self.root_cert_content = root_cert_content
        self.key_path = key_path
        self.key_content = key_content
        self.cert_chain_path = cert_chain_path
        self.cert_chain_content = cert_chain_content
        self.envoy_env_path = envoy_env_path
        self.envoy_env_content = envoy_env_content
        self.hosts_path = hosts_path
        self.hosts_content = hosts_content
        self.token_path = token_path
        self.token_content = token_content

    def validate(self):
        self.validate_required(self.root_cert_path, 'root_cert_path')
        self.validate_required(self.root_cert_content, 'root_cert_content')
        self.validate_required(self.key_path, 'key_path')
        self.validate_required(self.key_content, 'key_content')
        self.validate_required(self.cert_chain_path, 'cert_chain_path')
        self.validate_required(self.cert_chain_content, 'cert_chain_content')
        self.validate_required(self.envoy_env_path, 'envoy_env_path')
        self.validate_required(self.envoy_env_content, 'envoy_env_content')
        self.validate_required(self.hosts_path, 'hosts_path')
        self.validate_required(self.hosts_content, 'hosts_content')
        self.validate_required(self.token_path, 'token_path')
        self.validate_required(self.token_content, 'token_content')

    def to_map(self):
        result = dict()
        if self.root_cert_path is not None:
            result['RootCertPath'] = self.root_cert_path
        if self.root_cert_content is not None:
            result['RootCertContent'] = self.root_cert_content
        if self.key_path is not None:
            result['KeyPath'] = self.key_path
        if self.key_content is not None:
            result['KeyContent'] = self.key_content
        if self.cert_chain_path is not None:
            result['CertChainPath'] = self.cert_chain_path
        if self.cert_chain_content is not None:
            result['CertChainContent'] = self.cert_chain_content
        if self.envoy_env_path is not None:
            result['EnvoyEnvPath'] = self.envoy_env_path
        if self.envoy_env_content is not None:
            result['EnvoyEnvContent'] = self.envoy_env_content
        if self.hosts_path is not None:
            result['HostsPath'] = self.hosts_path
        if self.hosts_content is not None:
            result['HostsContent'] = self.hosts_content
        if self.token_path is not None:
            result['TokenPath'] = self.token_path
        if self.token_content is not None:
            result['TokenContent'] = self.token_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RootCertPath') is not None:
            self.root_cert_path = m.get('RootCertPath')
        if m.get('RootCertContent') is not None:
            self.root_cert_content = m.get('RootCertContent')
        if m.get('KeyPath') is not None:
            self.key_path = m.get('KeyPath')
        if m.get('KeyContent') is not None:
            self.key_content = m.get('KeyContent')
        if m.get('CertChainPath') is not None:
            self.cert_chain_path = m.get('CertChainPath')
        if m.get('CertChainContent') is not None:
            self.cert_chain_content = m.get('CertChainContent')
        if m.get('EnvoyEnvPath') is not None:
            self.envoy_env_path = m.get('EnvoyEnvPath')
        if m.get('EnvoyEnvContent') is not None:
            self.envoy_env_content = m.get('EnvoyEnvContent')
        if m.get('HostsPath') is not None:
            self.hosts_path = m.get('HostsPath')
        if m.get('HostsContent') is not None:
            self.hosts_content = m.get('HostsContent')
        if m.get('TokenPath') is not None:
            self.token_path = m.get('TokenPath')
        if m.get('TokenContent') is not None:
            self.token_content = m.get('TokenContent')
        return self


class GetVmMetaResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vm_meta_info: GetVmMetaResponseVmMetaInfo = None,
    ):
        self.request_id = request_id
        self.vm_meta_info = vm_meta_info

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vm_meta_info, 'vm_meta_info')
        if self.vm_meta_info:
            self.vm_meta_info.validate()

    def to_map(self):
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
            temp_model = GetVmMetaResponseVmMetaInfo()
            self.vm_meta_info = temp_model.from_map(m['VmMetaInfo'])
        return self


class RemoveVmAppFromMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        namespace: str = None,
        service_name: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.namespace = namespace
        self.service_name = service_name

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.service_name, 'service_name')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class RemoveVmAppFromMeshResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetRegisteredServiceEndpointsRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        namespace: str = None,
        name: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.namespace = namespace
        self.name = name

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetRegisteredServiceEndpointsResponseServiceEndpoints(TeaModel):
    def __init__(
        self,
        address: str = None,
        cluster_id: str = None,
    ):
        self.address = address
        self.cluster_id = cluster_id

    def validate(self):
        self.validate_required(self.address, 'address')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
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


class GetRegisteredServiceEndpointsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_endpoints: List[GetRegisteredServiceEndpointsResponseServiceEndpoints] = None,
    ):
        self.request_id = request_id
        self.service_endpoints = service_endpoints

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.service_endpoints, 'service_endpoints')
        if self.service_endpoints:
            for k in self.service_endpoints:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceEndpoints'] = []
        if self.service_endpoints is not None:
            for k in self.service_endpoints:
                result['ServiceEndpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_endpoints = []
        if m.get('ServiceEndpoints') is not None:
            for k in m.get('ServiceEndpoints'):
                temp_model = GetRegisteredServiceEndpointsResponseServiceEndpoints()
                self.service_endpoints.append(temp_model.from_map(k))
        return self


class GetServiceMeshSlbRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetServiceMeshSlbResponseData(TeaModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        status: str = None,
        server_health_status: str = None,
    ):
        self.load_balancer_id = load_balancer_id
        self.status = status
        self.server_health_status = server_health_status

    def validate(self):
        self.validate_required(self.load_balancer_id, 'load_balancer_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.server_health_status, 'server_health_status')

    def to_map(self):
        result = dict()
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.status is not None:
            result['Status'] = self.status
        if self.server_health_status is not None:
            result['ServerHealthStatus'] = self.server_health_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ServerHealthStatus') is not None:
            self.server_health_status = m.get('ServerHealthStatus')
        return self


class GetServiceMeshSlbResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetServiceMeshSlbResponseData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetServiceMeshSlbResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetRegisteredServicesRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        namespace: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class GetRegisteredServicesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        services: List[str] = None,
    ):
        self.request_id = request_id
        self.services = services

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.services, 'services')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.services is not None:
            result['Services'] = self.services
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Services') is not None:
            self.services = m.get('Services')
        return self


class GetDiagnosisRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetDiagnosisResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        run_at: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.run_at = run_at
        self.status = status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result, 'result')
        self.validate_required(self.run_at, 'run_at')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.run_at is not None:
            result['RunAt'] = self.run_at
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RunAt') is not None:
            self.run_at = m.get('RunAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetRegisteredServiceNamespacesRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetRegisteredServiceNamespacesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        namespaces: List[str] = None,
    ):
        self.request_id = request_id
        self.namespaces = namespaces

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.namespaces, 'namespaces')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')
        return self


class RunDiagnosisRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class RunDiagnosisResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result, 'result')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RemoveClusterFromServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        cluster_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.cluster_id = cluster_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class RemoveClusterFromServiceMeshResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddClusterIntoServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        cluster_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.cluster_id = cluster_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class AddClusterIntoServiceMeshResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateIstioInjectionConfigRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        namespace: str = None,
        enable_istio_injection: bool = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.namespace = namespace
        self.enable_istio_injection = enable_istio_injection

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.enable_istio_injection, 'enable_istio_injection')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.enable_istio_injection is not None:
            result['EnableIstioInjection'] = self.enable_istio_injection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('EnableIstioInjection') is not None:
            self.enable_istio_injection = m.get('EnableIstioInjection')
        return self


class UpdateIstioInjectionConfigResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeGuestClusterAccessLogDashboardsRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
    ):
        self.k_8s_cluster_id = k_8s_cluster_id

    def validate(self):
        self.validate_required(self.k_8s_cluster_id, 'k_8s_cluster_id')

    def to_map(self):
        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        return self


class DescribeGuestClusterAccessLogDashboardsResponseDashboards(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        self.validate_required(self.title, 'title')
        self.validate_required(self.url, 'url')

    def to_map(self):
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


class DescribeGuestClusterAccessLogDashboardsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        k_8s_cluster_id: str = None,
        dashboards: List[DescribeGuestClusterAccessLogDashboardsResponseDashboards] = None,
    ):
        self.request_id = request_id
        self.k_8s_cluster_id = k_8s_cluster_id
        self.dashboards = dashboards

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.k_8s_cluster_id, 'k_8s_cluster_id')
        self.validate_required(self.dashboards, 'dashboards')
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k in m.get('Dashboards'):
                temp_model = DescribeGuestClusterAccessLogDashboardsResponseDashboards()
                self.dashboards.append(temp_model.from_map(k))
        return self


class DescribeClusterPrometheusRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        k_8s_cluster_id: str = None,
        k_8s_cluster_region_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.k_8s_cluster_id = k_8s_cluster_id
        self.k_8s_cluster_region_id = k_8s_cluster_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.k_8s_cluster_region_id is not None:
            result['K8sClusterRegionId'] = self.k_8s_cluster_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('K8sClusterRegionId') is not None:
            self.k_8s_cluster_region_id = m.get('K8sClusterRegionId')
        return self


class DescribeClusterPrometheusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prometheus: str = None,
    ):
        self.request_id = request_id
        self.prometheus = prometheus

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.prometheus, 'prometheus')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Prometheus') is not None:
            self.prometheus = m.get('Prometheus')
        return self


class DescribeClusterGrafanaRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        k_8s_cluster_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.k_8s_cluster_id = k_8s_cluster_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.k_8s_cluster_id, 'k_8s_cluster_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        return self


class DescribeClusterGrafanaResponseDashboards(TeaModel):
    def __init__(
        self,
        url: str = None,
        title: str = None,
    ):
        self.url = url
        self.title = title

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.title, 'title')

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeClusterGrafanaResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dashboards: List[DescribeClusterGrafanaResponseDashboards] = None,
    ):
        self.request_id = request_id
        self.dashboards = dashboards

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dashboards, 'dashboards')
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k in m.get('Dashboards'):
                temp_model = DescribeClusterGrafanaResponseDashboards()
                self.dashboards.append(temp_model.from_map(k))
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
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeCensResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        clusters: List[str] = None,
    ):
        self.request_id = request_id
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.clusters, 'clusters')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        return self


class DescribeClustersInServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeClustersInServiceMeshResponseClustersAccessLogDashboards(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        self.validate_required(self.title, 'title')
        self.validate_required(self.url, 'url')

    def to_map(self):
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


class DescribeClustersInServiceMeshResponseClusters(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        creation_time: str = None,
        error_message: str = None,
        name: str = None,
        region_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
        vpc_id: str = None,
        sg_id: str = None,
        cluster_domain: str = None,
        access_log_dashboards: List[DescribeClustersInServiceMeshResponseClustersAccessLogDashboards] = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.creation_time = creation_time
        self.error_message = error_message
        self.name = name
        self.region_id = region_id
        self.state = state
        self.update_time = update_time
        self.version = version
        self.vpc_id = vpc_id
        self.sg_id = sg_id
        self.cluster_domain = cluster_domain
        self.access_log_dashboards = access_log_dashboards

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.cluster_type, 'cluster_type')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.name, 'name')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.state, 'state')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.version, 'version')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.sg_id, 'sg_id')
        self.validate_required(self.cluster_domain, 'cluster_domain')
        self.validate_required(self.access_log_dashboards, 'access_log_dashboards')
        if self.access_log_dashboards:
            for k in self.access_log_dashboards:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        result['AccessLogDashboards'] = []
        if self.access_log_dashboards is not None:
            for k in self.access_log_dashboards:
                result['AccessLogDashboards'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        self.access_log_dashboards = []
        if m.get('AccessLogDashboards') is not None:
            for k in m.get('AccessLogDashboards'):
                temp_model = DescribeClustersInServiceMeshResponseClustersAccessLogDashboards()
                self.access_log_dashboards.append(temp_model.from_map(k))
        return self


class DescribeClustersInServiceMeshResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        clusters: List[DescribeClustersInServiceMeshResponseClusters] = None,
    ):
        self.request_id = request_id
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeClustersInServiceMeshResponseClusters()
                self.clusters.append(temp_model.from_map(k))
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
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeIngressGatewaysResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ingress_gateways: List[Dict[str, Any]] = None,
    ):
        self.request_id = request_id
        self.ingress_gateways = ingress_gateways

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ingress_gateways, 'ingress_gateways')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ingress_gateways is not None:
            result['IngressGateways'] = self.ingress_gateways
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IngressGateways') is not None:
            self.ingress_gateways = m.get('IngressGateways')
        return self


class DescribeUpgradeVersionRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeUpgradeVersionResponseVersion(TeaModel):
    def __init__(
        self,
        istio_version: str = None,
        istio_operator_version: str = None,
        kubernetes_version: str = None,
    ):
        self.istio_version = istio_version
        self.istio_operator_version = istio_operator_version
        self.kubernetes_version = kubernetes_version

    def validate(self):
        self.validate_required(self.istio_version, 'istio_version')
        self.validate_required(self.istio_operator_version, 'istio_operator_version')
        self.validate_required(self.kubernetes_version, 'kubernetes_version')

    def to_map(self):
        result = dict()
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.istio_operator_version is not None:
            result['IstioOperatorVersion'] = self.istio_operator_version
        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('IstioOperatorVersion') is not None:
            self.istio_operator_version = m.get('IstioOperatorVersion')
        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')
        return self


class DescribeUpgradeVersionResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version: DescribeUpgradeVersionResponseVersion = None,
    ):
        self.request_id = request_id
        self.version = version

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.version, 'version')
        if self.version:
            self.version.validate()

    def to_map(self):
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
            temp_model = DescribeUpgradeVersionResponseVersion()
            self.version = temp_model.from_map(m['Version'])
        return self


class UpdateMeshFeatureRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        tracing: bool = None,
        trace_sampling: float = None,
        locality_load_balancing: bool = None,
        telemetry: bool = None,
        open_agent_policy: bool = None,
        opalog_level: str = None,
        oparequest_cpu: str = None,
        oparequest_memory: str = None,
        opalimit_cpu: str = None,
        opalimit_memory: str = None,
        enable_audit: bool = None,
        audit_project: str = None,
        cluster_domain: str = None,
        customized_zipkin: bool = None,
        outbound_traffic_policy: str = None,
        proxy_request_cpu: str = None,
        proxy_request_memory: str = None,
        proxy_limit_cpu: str = None,
        proxy_limit_memory: str = None,
        include_ipranges: str = None,
        enable_namespaces_by_default: bool = None,
        auto_injection_policy_enabled: bool = None,
        sidecar_injector_request_cpu: str = None,
        sidecar_injector_request_memory: str = None,
        sidecar_injector_limit_cpu: str = None,
        sidecar_injector_limit_memory: str = None,
        sidecar_injector_webhook_as_yaml: str = None,
        cni_enabled: bool = None,
        cni_exclude_namespaces: str = None,
        opa_enabled: bool = None,
        http_10enabled: bool = None,
        kiali_enabled: bool = None,
        customized_prometheus: bool = None,
        prometheus_url: str = None,
        access_log_enabled: bool = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.tracing = tracing
        self.trace_sampling = trace_sampling
        self.locality_load_balancing = locality_load_balancing
        self.telemetry = telemetry
        self.open_agent_policy = open_agent_policy
        self.opalog_level = opalog_level
        self.oparequest_cpu = oparequest_cpu
        self.oparequest_memory = oparequest_memory
        self.opalimit_cpu = opalimit_cpu
        self.opalimit_memory = opalimit_memory
        self.enable_audit = enable_audit
        self.audit_project = audit_project
        self.cluster_domain = cluster_domain
        self.customized_zipkin = customized_zipkin
        self.outbound_traffic_policy = outbound_traffic_policy
        self.proxy_request_cpu = proxy_request_cpu
        self.proxy_request_memory = proxy_request_memory
        self.proxy_limit_cpu = proxy_limit_cpu
        self.proxy_limit_memory = proxy_limit_memory
        self.include_ipranges = include_ipranges
        self.enable_namespaces_by_default = enable_namespaces_by_default
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.sidecar_injector_request_cpu = sidecar_injector_request_cpu
        self.sidecar_injector_request_memory = sidecar_injector_request_memory
        self.sidecar_injector_limit_cpu = sidecar_injector_limit_cpu
        self.sidecar_injector_limit_memory = sidecar_injector_limit_memory
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml
        self.cni_enabled = cni_enabled
        self.cni_exclude_namespaces = cni_exclude_namespaces
        self.opa_enabled = opa_enabled
        self.http_10enabled = http_10enabled
        self.kiali_enabled = kiali_enabled
        self.customized_prometheus = customized_prometheus
        self.prometheus_url = prometheus_url
        self.access_log_enabled = access_log_enabled

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.locality_load_balancing is not None:
            result['LocalityLoadBalancing'] = self.locality_load_balancing
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.open_agent_policy is not None:
            result['OpenAgentPolicy'] = self.open_agent_policy
        if self.opalog_level is not None:
            result['OPALogLevel'] = self.opalog_level
        if self.oparequest_cpu is not None:
            result['OPARequestCPU'] = self.oparequest_cpu
        if self.oparequest_memory is not None:
            result['OPARequestMemory'] = self.oparequest_memory
        if self.opalimit_cpu is not None:
            result['OPALimitCPU'] = self.opalimit_cpu
        if self.opalimit_memory is not None:
            result['OPALimitMemory'] = self.opalimit_memory
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.proxy_request_cpu is not None:
            result['ProxyRequestCPU'] = self.proxy_request_cpu
        if self.proxy_request_memory is not None:
            result['ProxyRequestMemory'] = self.proxy_request_memory
        if self.proxy_limit_cpu is not None:
            result['ProxyLimitCPU'] = self.proxy_limit_cpu
        if self.proxy_limit_memory is not None:
            result['ProxyLimitMemory'] = self.proxy_limit_memory
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.sidecar_injector_request_cpu is not None:
            result['SidecarInjectorRequestCPU'] = self.sidecar_injector_request_cpu
        if self.sidecar_injector_request_memory is not None:
            result['SidecarInjectorRequestMemory'] = self.sidecar_injector_request_memory
        if self.sidecar_injector_limit_cpu is not None:
            result['SidecarInjectorLimitCPU'] = self.sidecar_injector_limit_cpu
        if self.sidecar_injector_limit_memory is not None:
            result['SidecarInjectorLimitMemory'] = self.sidecar_injector_limit_memory
        if self.sidecar_injector_webhook_as_yaml is not None:
            result['SidecarInjectorWebhookAsYaml'] = self.sidecar_injector_webhook_as_yaml
        if self.cni_enabled is not None:
            result['CniEnabled'] = self.cni_enabled
        if self.cni_exclude_namespaces is not None:
            result['CniExcludeNamespaces'] = self.cni_exclude_namespaces
        if self.opa_enabled is not None:
            result['OpaEnabled'] = self.opa_enabled
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.kiali_enabled is not None:
            result['KialiEnabled'] = self.kiali_enabled
        if self.customized_prometheus is not None:
            result['CustomizedPrometheus'] = self.customized_prometheus
        if self.prometheus_url is not None:
            result['PrometheusUrl'] = self.prometheus_url
        if self.access_log_enabled is not None:
            result['AccessLogEnabled'] = self.access_log_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('LocalityLoadBalancing') is not None:
            self.locality_load_balancing = m.get('LocalityLoadBalancing')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('OpenAgentPolicy') is not None:
            self.open_agent_policy = m.get('OpenAgentPolicy')
        if m.get('OPALogLevel') is not None:
            self.opalog_level = m.get('OPALogLevel')
        if m.get('OPARequestCPU') is not None:
            self.oparequest_cpu = m.get('OPARequestCPU')
        if m.get('OPARequestMemory') is not None:
            self.oparequest_memory = m.get('OPARequestMemory')
        if m.get('OPALimitCPU') is not None:
            self.opalimit_cpu = m.get('OPALimitCPU')
        if m.get('OPALimitMemory') is not None:
            self.opalimit_memory = m.get('OPALimitMemory')
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('ProxyRequestCPU') is not None:
            self.proxy_request_cpu = m.get('ProxyRequestCPU')
        if m.get('ProxyRequestMemory') is not None:
            self.proxy_request_memory = m.get('ProxyRequestMemory')
        if m.get('ProxyLimitCPU') is not None:
            self.proxy_limit_cpu = m.get('ProxyLimitCPU')
        if m.get('ProxyLimitMemory') is not None:
            self.proxy_limit_memory = m.get('ProxyLimitMemory')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('SidecarInjectorRequestCPU') is not None:
            self.sidecar_injector_request_cpu = m.get('SidecarInjectorRequestCPU')
        if m.get('SidecarInjectorRequestMemory') is not None:
            self.sidecar_injector_request_memory = m.get('SidecarInjectorRequestMemory')
        if m.get('SidecarInjectorLimitCPU') is not None:
            self.sidecar_injector_limit_cpu = m.get('SidecarInjectorLimitCPU')
        if m.get('SidecarInjectorLimitMemory') is not None:
            self.sidecar_injector_limit_memory = m.get('SidecarInjectorLimitMemory')
        if m.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = m.get('SidecarInjectorWebhookAsYaml')
        if m.get('CniEnabled') is not None:
            self.cni_enabled = m.get('CniEnabled')
        if m.get('CniExcludeNamespaces') is not None:
            self.cni_exclude_namespaces = m.get('CniExcludeNamespaces')
        if m.get('OpaEnabled') is not None:
            self.opa_enabled = m.get('OpaEnabled')
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('KialiEnabled') is not None:
            self.kiali_enabled = m.get('KialiEnabled')
        if m.get('CustomizedPrometheus') is not None:
            self.customized_prometheus = m.get('CustomizedPrometheus')
        if m.get('PrometheusUrl') is not None:
            self.prometheus_url = m.get('PrometheusUrl')
        if m.get('AccessLogEnabled') is not None:
            self.access_log_enabled = m.get('AccessLogEnabled')
        return self


class UpdateMeshFeatureResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeMeshVersionRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpgradeMeshVersionResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceMeshesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DescribeServiceMeshesResponseServiceMeshesEndpoints(TeaModel):
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
        self.validate_required(self.intranet_api_server_endpoint, 'intranet_api_server_endpoint')
        self.validate_required(self.intranet_pilot_endpoint, 'intranet_pilot_endpoint')
        self.validate_required(self.public_api_server_endpoint, 'public_api_server_endpoint')
        self.validate_required(self.public_pilot_endpoint, 'public_pilot_endpoint')
        self.validate_required(self.reverse_tunnel_endpoint, 'reverse_tunnel_endpoint')

    def to_map(self):
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


class DescribeServiceMeshesResponseServiceMeshesServiceMeshInfo(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        error_message: str = None,
        name: str = None,
        region_id: str = None,
        service_mesh_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
    ):
        self.creation_time = creation_time
        self.error_message = error_message
        self.name = name
        self.region_id = region_id
        self.service_mesh_id = service_mesh_id
        self.state = state
        self.update_time = update_time
        self.version = version

    def validate(self):
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.name, 'name')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.state, 'state')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.name is not None:
            result['Name'] = self.name
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


class DescribeServiceMeshesResponseServiceMeshesSpecLoadBalancer(TeaModel):
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
        self.validate_required(self.api_server_loadbalancer_id, 'api_server_loadbalancer_id')
        self.validate_required(self.api_server_public_eip, 'api_server_public_eip')
        self.validate_required(self.pilot_public_eip, 'pilot_public_eip')
        self.validate_required(self.pilot_public_loadbalancer_id, 'pilot_public_loadbalancer_id')

    def to_map(self):
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


class DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigPilot(TeaModel):
    def __init__(
        self,
        trace_sampling: float = None,
        http_10enabled: bool = None,
    ):
        self.trace_sampling = trace_sampling
        self.http_10enabled = http_10enabled

    def validate(self):
        self.validate_required(self.trace_sampling, 'trace_sampling')
        self.validate_required(self.http_10enabled, 'http_10enabled')

    def to_map(self):
        result = dict()
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        exclude_namespaces: str = None,
    ):
        self.enabled = enabled
        self.exclude_namespaces = exclude_namespaces

    def validate(self):
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.exclude_namespaces, 'exclude_namespaces')

    def to_map(self):
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


class DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(
        self,
        enable_namespaces_by_default: bool = None,
        auto_injection_policy_enabled: bool = None,
        init_cniconfiguration: DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration = None,
    ):
        self.enable_namespaces_by_default = enable_namespaces_by_default
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.init_cniconfiguration = init_cniconfiguration

    def validate(self):
        self.validate_required(self.enable_namespaces_by_default, 'enable_namespaces_by_default')
        self.validate_required(self.auto_injection_policy_enabled, 'auto_injection_policy_enabled')
        self.validate_required(self.init_cniconfiguration, 'init_cniconfiguration')
        if self.init_cniconfiguration:
            self.init_cniconfiguration.validate()

    def to_map(self):
        result = dict()
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.init_cniconfiguration is not None:
            result['InitCNIConfiguration'] = self.init_cniconfiguration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(m['InitCNIConfiguration'])
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecMeshConfig(TeaModel):
    def __init__(
        self,
        mtls: bool = None,
        outbound_traffic_policy: str = None,
        strict_mtls: bool = None,
        tracing: bool = None,
        telemetry: bool = None,
        pilot: DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigPilot = None,
        sidecar_injector: DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjector = None,
    ):
        self.mtls = mtls
        self.outbound_traffic_policy = outbound_traffic_policy
        self.strict_mtls = strict_mtls
        self.tracing = tracing
        self.telemetry = telemetry
        self.pilot = pilot
        self.sidecar_injector = sidecar_injector

    def validate(self):
        self.validate_required(self.mtls, 'mtls')
        self.validate_required(self.outbound_traffic_policy, 'outbound_traffic_policy')
        self.validate_required(self.strict_mtls, 'strict_mtls')
        self.validate_required(self.tracing, 'tracing')
        self.validate_required(self.telemetry, 'telemetry')
        self.validate_required(self.pilot, 'pilot')
        if self.pilot:
            self.pilot.validate()
        self.validate_required(self.sidecar_injector, 'sidecar_injector')
        if self.sidecar_injector:
            self.sidecar_injector.validate()

    def to_map(self):
        result = dict()
        if self.mtls is not None:
            result['Mtls'] = self.mtls
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.strict_mtls is not None:
            result['StrictMtls'] = self.strict_mtls
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        if self.sidecar_injector is not None:
            result['SidecarInjector'] = self.sidecar_injector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mtls') is not None:
            self.mtls = m.get('Mtls')
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('StrictMtls') is not None:
            self.strict_mtls = m.get('StrictMtls')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('Pilot') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(m['Pilot'])
        if m.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(m['SidecarInjector'])
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecNetwork(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        vpc_id: str = None,
        v_switches: List[str] = None,
    ):
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
        self.v_switches = v_switches

    def validate(self):
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switches, 'v_switches')

    def to_map(self):
        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpec(TeaModel):
    def __init__(
        self,
        load_balancer: DescribeServiceMeshesResponseServiceMeshesSpecLoadBalancer = None,
        mesh_config: DescribeServiceMeshesResponseServiceMeshesSpecMeshConfig = None,
        network: DescribeServiceMeshesResponseServiceMeshesSpecNetwork = None,
    ):
        self.load_balancer = load_balancer
        self.mesh_config = mesh_config
        self.network = network

    def validate(self):
        self.validate_required(self.load_balancer, 'load_balancer')
        if self.load_balancer:
            self.load_balancer.validate()
        self.validate_required(self.mesh_config, 'mesh_config')
        if self.mesh_config:
            self.mesh_config.validate()
        self.validate_required(self.network, 'network')
        if self.network:
            self.network.validate()

    def to_map(self):
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
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(m['LoadBalancer'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        if m.get('Network') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeServiceMeshesResponseServiceMeshes(TeaModel):
    def __init__(
        self,
        endpoints: DescribeServiceMeshesResponseServiceMeshesEndpoints = None,
        service_mesh_info: DescribeServiceMeshesResponseServiceMeshesServiceMeshInfo = None,
        spec: DescribeServiceMeshesResponseServiceMeshesSpec = None,
        clusters: List[str] = None,
    ):
        self.endpoints = endpoints
        self.service_mesh_info = service_mesh_info
        self.spec = spec
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.endpoints, 'endpoints')
        if self.endpoints:
            self.endpoints.validate()
        self.validate_required(self.service_mesh_info, 'service_mesh_info')
        if self.service_mesh_info:
            self.service_mesh_info.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()
        self.validate_required(self.clusters, 'clusters')

    def to_map(self):
        result = dict()
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(m['ServiceMeshInfo'])
        if m.get('Spec') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        return self


class DescribeServiceMeshesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_meshes: List[DescribeServiceMeshesResponseServiceMeshes] = None,
    ):
        self.request_id = request_id
        self.service_meshes = service_meshes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.service_meshes, 'service_meshes')
        if self.service_meshes:
            for k in self.service_meshes:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeServiceMeshesResponseServiceMeshes()
                self.service_meshes.append(temp_model.from_map(k))
        return self


class DescribeServiceMeshDetailRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshDetailResponseServiceMeshEndpoints(TeaModel):
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
        self.validate_required(self.intranet_api_server_endpoint, 'intranet_api_server_endpoint')
        self.validate_required(self.intranet_pilot_endpoint, 'intranet_pilot_endpoint')
        self.validate_required(self.public_api_server_endpoint, 'public_api_server_endpoint')
        self.validate_required(self.public_pilot_endpoint, 'public_pilot_endpoint')

    def to_map(self):
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


class DescribeServiceMeshDetailResponseServiceMeshServiceMeshInfo(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        error_message: str = None,
        name: str = None,
        region_id: str = None,
        service_mesh_id: str = None,
        state: str = None,
        update_time: str = None,
        version: str = None,
    ):
        self.creation_time = creation_time
        self.error_message = error_message
        self.name = name
        self.region_id = region_id
        self.service_mesh_id = service_mesh_id
        self.state = state
        self.update_time = update_time
        self.version = version

    def validate(self):
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.error_message, 'error_message')
        self.validate_required(self.name, 'name')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.state, 'state')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.name is not None:
            result['Name'] = self.name
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


class DescribeServiceMeshDetailResponseServiceMeshSpecLoadBalancer(TeaModel):
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
        self.validate_required(self.api_server_loadbalancer_id, 'api_server_loadbalancer_id')
        self.validate_required(self.api_server_public_eip, 'api_server_public_eip')
        self.validate_required(self.pilot_public_eip, 'pilot_public_eip')
        self.validate_required(self.pilot_public_loadbalancer_id, 'pilot_public_loadbalancer_id')

    def to_map(self):
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


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPilot(TeaModel):
    def __init__(
        self,
        trace_sampling: float = None,
        http_10enabled: bool = None,
    ):
        self.trace_sampling = trace_sampling
        self.http_10enabled = http_10enabled

    def validate(self):
        self.validate_required(self.trace_sampling, 'trace_sampling')
        self.validate_required(self.http_10enabled, 'http_10enabled')

    def to_map(self):
        result = dict()
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigOPA(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        log_level: str = None,
        request_cpu: str = None,
        request_memory: str = None,
        limit_cpu: str = None,
        limit_memory: str = None,
    ):
        self.enabled = enabled
        self.log_level = log_level
        self.request_cpu = request_cpu
        self.request_memory = request_memory
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory

    def validate(self):
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.log_level, 'log_level')
        self.validate_required(self.request_cpu, 'request_cpu')
        self.validate_required(self.request_memory, 'request_memory')
        self.validate_required(self.limit_cpu, 'limit_cpu')
        self.validate_required(self.limit_memory, 'limit_memory')

    def to_map(self):
        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAudit(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        project: str = None,
    ):
        self.enabled = enabled
        self.project = project

    def validate(self):
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.project, 'project')

    def to_map(self):
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


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigProxy(TeaModel):
    def __init__(
        self,
        cluster_domain: str = None,
        request_cpu: str = None,
        request_memory: str = None,
        limit_cpu: str = None,
        limit_memory: str = None,
    ):
        self.cluster_domain = cluster_domain
        self.request_cpu = request_cpu
        self.request_memory = request_memory
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory

    def validate(self):
        self.validate_required(self.cluster_domain, 'cluster_domain')
        self.validate_required(self.request_cpu, 'request_cpu')
        self.validate_required(self.request_memory, 'request_memory')
        self.validate_required(self.limit_cpu, 'limit_cpu')
        self.validate_required(self.limit_memory, 'limit_memory')

    def to_map(self):
        result = dict()
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        exclude_namespaces: str = None,
    ):
        self.enabled = enabled
        self.exclude_namespaces = exclude_namespaces

    def validate(self):
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.exclude_namespaces, 'exclude_namespaces')

    def to_map(self):
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


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(
        self,
        enable_namespaces_by_default: bool = None,
        auto_injection_policy_enabled: bool = None,
        request_cpu: str = None,
        request_memory: str = None,
        limit_cpu: str = None,
        limit_memory: str = None,
        sidecar_injector_webhook_as_yaml: str = None,
        init_cniconfiguration: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration = None,
    ):
        self.enable_namespaces_by_default = enable_namespaces_by_default
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.request_cpu = request_cpu
        self.request_memory = request_memory
        self.limit_cpu = limit_cpu
        self.limit_memory = limit_memory
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml
        self.init_cniconfiguration = init_cniconfiguration

    def validate(self):
        self.validate_required(self.enable_namespaces_by_default, 'enable_namespaces_by_default')
        self.validate_required(self.auto_injection_policy_enabled, 'auto_injection_policy_enabled')
        self.validate_required(self.request_cpu, 'request_cpu')
        self.validate_required(self.request_memory, 'request_memory')
        self.validate_required(self.limit_cpu, 'limit_cpu')
        self.validate_required(self.limit_memory, 'limit_memory')
        self.validate_required(self.sidecar_injector_webhook_as_yaml, 'sidecar_injector_webhook_as_yaml')
        self.validate_required(self.init_cniconfiguration, 'init_cniconfiguration')
        if self.init_cniconfiguration:
            self.init_cniconfiguration.validate()

    def to_map(self):
        result = dict()
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.sidecar_injector_webhook_as_yaml is not None:
            result['SidecarInjectorWebhookAsYaml'] = self.sidecar_injector_webhook_as_yaml
        if self.init_cniconfiguration is not None:
            result['InitCNIConfiguration'] = self.init_cniconfiguration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = m.get('SidecarInjectorWebhookAsYaml')
        if m.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(m['InitCNIConfiguration'])
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigKiali(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        url: str = None,
    ):
        self.enabled = enabled
        self.url = url

    def validate(self):
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.url, 'url')

    def to_map(self):
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


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPrometheus(TeaModel):
    def __init__(
        self,
        use_external: bool = None,
        external_url: str = None,
    ):
        self.use_external = use_external
        self.external_url = external_url

    def validate(self):
        self.validate_required(self.use_external, 'use_external')
        self.validate_required(self.external_url, 'external_url')

    def to_map(self):
        result = dict()
        if self.use_external is not None:
            result['UseExternal'] = self.use_external
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UseExternal') is not None:
            self.use_external = m.get('UseExternal')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAccessLog(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        self.validate_required(self.enabled, 'enabled')

    def to_map(self):
        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfig(TeaModel):
    def __init__(
        self,
        enable_locality_lb: bool = None,
        telemetry: bool = None,
        tracing: bool = None,
        customized_zipkin: bool = None,
        outbound_traffic_policy: str = None,
        include_ipranges: str = None,
        edition: str = None,
        pilot: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPilot = None,
        opa: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigOPA = None,
        audit: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAudit = None,
        proxy: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigProxy = None,
        sidecar_injector: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjector = None,
        kiali: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigKiali = None,
        prometheus: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPrometheus = None,
        access_log: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAccessLog = None,
    ):
        self.enable_locality_lb = enable_locality_lb
        self.telemetry = telemetry
        self.tracing = tracing
        self.customized_zipkin = customized_zipkin
        self.outbound_traffic_policy = outbound_traffic_policy
        self.include_ipranges = include_ipranges
        self.edition = edition
        self.pilot = pilot
        self.opa = opa
        self.audit = audit
        self.proxy = proxy
        self.sidecar_injector = sidecar_injector
        self.kiali = kiali
        self.prometheus = prometheus
        self.access_log = access_log

    def validate(self):
        self.validate_required(self.enable_locality_lb, 'enable_locality_lb')
        self.validate_required(self.telemetry, 'telemetry')
        self.validate_required(self.tracing, 'tracing')
        self.validate_required(self.customized_zipkin, 'customized_zipkin')
        self.validate_required(self.outbound_traffic_policy, 'outbound_traffic_policy')
        self.validate_required(self.include_ipranges, 'include_ipranges')
        self.validate_required(self.edition, 'edition')
        self.validate_required(self.pilot, 'pilot')
        if self.pilot:
            self.pilot.validate()
        self.validate_required(self.opa, 'opa')
        if self.opa:
            self.opa.validate()
        self.validate_required(self.audit, 'audit')
        if self.audit:
            self.audit.validate()
        self.validate_required(self.proxy, 'proxy')
        if self.proxy:
            self.proxy.validate()
        self.validate_required(self.sidecar_injector, 'sidecar_injector')
        if self.sidecar_injector:
            self.sidecar_injector.validate()
        self.validate_required(self.kiali, 'kiali')
        if self.kiali:
            self.kiali.validate()
        self.validate_required(self.prometheus, 'prometheus')
        if self.prometheus:
            self.prometheus.validate()
        self.validate_required(self.access_log, 'access_log')
        if self.access_log:
            self.access_log.validate()

    def to_map(self):
        result = dict()
        if self.enable_locality_lb is not None:
            result['EnableLocalityLB'] = self.enable_locality_lb
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        if self.opa is not None:
            result['OPA'] = self.opa.to_map()
        if self.audit is not None:
            result['Audit'] = self.audit.to_map()
        if self.proxy is not None:
            result['Proxy'] = self.proxy.to_map()
        if self.sidecar_injector is not None:
            result['SidecarInjector'] = self.sidecar_injector.to_map()
        if self.kiali is not None:
            result['Kiali'] = self.kiali.to_map()
        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus.to_map()
        if self.access_log is not None:
            result['AccessLog'] = self.access_log.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableLocalityLB') is not None:
            self.enable_locality_lb = m.get('EnableLocalityLB')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Pilot') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(m['Pilot'])
        if m.get('OPA') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigOPA()
            self.opa = temp_model.from_map(m['OPA'])
        if m.get('Audit') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAudit()
            self.audit = temp_model.from_map(m['Audit'])
        if m.get('Proxy') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigProxy()
            self.proxy = temp_model.from_map(m['Proxy'])
        if m.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(m['SidecarInjector'])
        if m.get('Kiali') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigKiali()
            self.kiali = temp_model.from_map(m['Kiali'])
        if m.get('Prometheus') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPrometheus()
            self.prometheus = temp_model.from_map(m['Prometheus'])
        if m.get('AccessLog') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAccessLog()
            self.access_log = temp_model.from_map(m['AccessLog'])
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecNetwork(TeaModel):
    def __init__(
        self,
        security_group_id: str = None,
        vpc_id: str = None,
        v_switches: List[str] = None,
    ):
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
        self.v_switches = v_switches

    def validate(self):
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switches, 'v_switches')

    def to_map(self):
        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpec(TeaModel):
    def __init__(
        self,
        load_balancer: DescribeServiceMeshDetailResponseServiceMeshSpecLoadBalancer = None,
        mesh_config: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfig = None,
        network: DescribeServiceMeshDetailResponseServiceMeshSpecNetwork = None,
    ):
        self.load_balancer = load_balancer
        self.mesh_config = mesh_config
        self.network = network

    def validate(self):
        self.validate_required(self.load_balancer, 'load_balancer')
        if self.load_balancer:
            self.load_balancer.validate()
        self.validate_required(self.mesh_config, 'mesh_config')
        if self.mesh_config:
            self.mesh_config.validate()
        self.validate_required(self.network, 'network')
        if self.network:
            self.network.validate()

    def to_map(self):
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
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(m['LoadBalancer'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        if m.get('Network') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeServiceMeshDetailResponseServiceMesh(TeaModel):
    def __init__(
        self,
        endpoints: DescribeServiceMeshDetailResponseServiceMeshEndpoints = None,
        service_mesh_info: DescribeServiceMeshDetailResponseServiceMeshServiceMeshInfo = None,
        spec: DescribeServiceMeshDetailResponseServiceMeshSpec = None,
        clusters: List[str] = None,
    ):
        self.endpoints = endpoints
        self.service_mesh_info = service_mesh_info
        self.spec = spec
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.endpoints, 'endpoints')
        if self.endpoints:
            self.endpoints.validate()
        self.validate_required(self.service_mesh_info, 'service_mesh_info')
        if self.service_mesh_info:
            self.service_mesh_info.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()
        self.validate_required(self.clusters, 'clusters')

    def to_map(self):
        result = dict()
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(m['ServiceMeshInfo'])
        if m.get('Spec') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        return self


class DescribeServiceMeshDetailResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_mesh: DescribeServiceMeshDetailResponseServiceMesh = None,
    ):
        self.request_id = request_id
        self.service_mesh = service_mesh

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.service_mesh, 'service_mesh')
        if self.service_mesh:
            self.service_mesh.validate()

    def to_map(self):
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
            temp_model = DescribeServiceMeshDetailResponseServiceMesh()
            self.service_mesh = temp_model.from_map(m['ServiceMesh'])
        return self


class DescribeServiceMeshKubeconfigRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        private_ip_address: bool = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.private_ip_address = private_ip_address

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class DescribeServiceMeshKubeconfigResponse(TeaModel):
    def __init__(
        self,
        kubeconfig: str = None,
        request_id: str = None,
    ):
        self.kubeconfig = kubeconfig
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.kubeconfig, 'kubeconfig')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
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


class CreateServiceMeshRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        istio_version: str = None,
        vpc_id: str = None,
        api_server_public_eip: bool = None,
        pilot_public_eip: bool = None,
        tracing: bool = None,
        name: str = None,
        v_switches: str = None,
        trace_sampling: float = None,
        locality_load_balancing: bool = None,
        telemetry: bool = None,
        open_agent_policy: bool = None,
        opalog_level: str = None,
        oparequest_cpu: str = None,
        oparequest_memory: str = None,
        opalimit_cpu: str = None,
        opalimit_memory: str = None,
        enable_audit: bool = None,
        audit_project: str = None,
        proxy_request_cpu: str = None,
        proxy_request_memory: str = None,
        proxy_limit_cpu: str = None,
        proxy_limit_memory: str = None,
        include_ipranges: str = None,
        exclude_ipranges: str = None,
        exclude_outbound_ports: str = None,
        exclude_inbound_ports: str = None,
        opa_enabled: bool = None,
        kiali_enabled: bool = None,
        access_log_enabled: bool = None,
        customized_prometheus: bool = None,
        prometheus_url: str = None,
    ):
        self.region_id = region_id
        self.istio_version = istio_version
        self.vpc_id = vpc_id
        self.api_server_public_eip = api_server_public_eip
        self.pilot_public_eip = pilot_public_eip
        self.tracing = tracing
        self.name = name
        self.v_switches = v_switches
        self.trace_sampling = trace_sampling
        self.locality_load_balancing = locality_load_balancing
        self.telemetry = telemetry
        self.open_agent_policy = open_agent_policy
        self.opalog_level = opalog_level
        self.oparequest_cpu = oparequest_cpu
        self.oparequest_memory = oparequest_memory
        self.opalimit_cpu = opalimit_cpu
        self.opalimit_memory = opalimit_memory
        self.enable_audit = enable_audit
        self.audit_project = audit_project
        self.proxy_request_cpu = proxy_request_cpu
        self.proxy_request_memory = proxy_request_memory
        self.proxy_limit_cpu = proxy_limit_cpu
        self.proxy_limit_memory = proxy_limit_memory
        self.include_ipranges = include_ipranges
        self.exclude_ipranges = exclude_ipranges
        self.exclude_outbound_ports = exclude_outbound_ports
        self.exclude_inbound_ports = exclude_inbound_ports
        self.opa_enabled = opa_enabled
        self.kiali_enabled = kiali_enabled
        self.access_log_enabled = access_log_enabled
        self.customized_prometheus = customized_prometheus
        self.prometheus_url = prometheus_url

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switches, 'v_switches')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.name is not None:
            result['Name'] = self.name
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.locality_load_balancing is not None:
            result['LocalityLoadBalancing'] = self.locality_load_balancing
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.open_agent_policy is not None:
            result['OpenAgentPolicy'] = self.open_agent_policy
        if self.opalog_level is not None:
            result['OPALogLevel'] = self.opalog_level
        if self.oparequest_cpu is not None:
            result['OPARequestCPU'] = self.oparequest_cpu
        if self.oparequest_memory is not None:
            result['OPARequestMemory'] = self.oparequest_memory
        if self.opalimit_cpu is not None:
            result['OPALimitCPU'] = self.opalimit_cpu
        if self.opalimit_memory is not None:
            result['OPALimitMemory'] = self.opalimit_memory
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project
        if self.proxy_request_cpu is not None:
            result['ProxyRequestCPU'] = self.proxy_request_cpu
        if self.proxy_request_memory is not None:
            result['ProxyRequestMemory'] = self.proxy_request_memory
        if self.proxy_limit_cpu is not None:
            result['ProxyLimitCPU'] = self.proxy_limit_cpu
        if self.proxy_limit_memory is not None:
            result['ProxyLimitMemory'] = self.proxy_limit_memory
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.opa_enabled is not None:
            result['OpaEnabled'] = self.opa_enabled
        if self.kiali_enabled is not None:
            result['KialiEnabled'] = self.kiali_enabled
        if self.access_log_enabled is not None:
            result['AccessLogEnabled'] = self.access_log_enabled
        if self.customized_prometheus is not None:
            result['CustomizedPrometheus'] = self.customized_prometheus
        if self.prometheus_url is not None:
            result['PrometheusUrl'] = self.prometheus_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('PilotPublicEip') is not None:
            self.pilot_public_eip = m.get('PilotPublicEip')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('LocalityLoadBalancing') is not None:
            self.locality_load_balancing = m.get('LocalityLoadBalancing')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('OpenAgentPolicy') is not None:
            self.open_agent_policy = m.get('OpenAgentPolicy')
        if m.get('OPALogLevel') is not None:
            self.opalog_level = m.get('OPALogLevel')
        if m.get('OPARequestCPU') is not None:
            self.oparequest_cpu = m.get('OPARequestCPU')
        if m.get('OPARequestMemory') is not None:
            self.oparequest_memory = m.get('OPARequestMemory')
        if m.get('OPALimitCPU') is not None:
            self.opalimit_cpu = m.get('OPALimitCPU')
        if m.get('OPALimitMemory') is not None:
            self.opalimit_memory = m.get('OPALimitMemory')
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')
        if m.get('ProxyRequestCPU') is not None:
            self.proxy_request_cpu = m.get('ProxyRequestCPU')
        if m.get('ProxyRequestMemory') is not None:
            self.proxy_request_memory = m.get('ProxyRequestMemory')
        if m.get('ProxyLimitCPU') is not None:
            self.proxy_limit_cpu = m.get('ProxyLimitCPU')
        if m.get('ProxyLimitMemory') is not None:
            self.proxy_limit_memory = m.get('ProxyLimitMemory')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('OpaEnabled') is not None:
            self.opa_enabled = m.get('OpaEnabled')
        if m.get('KialiEnabled') is not None:
            self.kiali_enabled = m.get('KialiEnabled')
        if m.get('AccessLogEnabled') is not None:
            self.access_log_enabled = m.get('AccessLogEnabled')
        if m.get('CustomizedPrometheus') is not None:
            self.customized_prometheus = m.get('CustomizedPrometheus')
        if m.get('PrometheusUrl') is not None:
            self.prometheus_url = m.get('PrometheusUrl')
        return self


class CreateServiceMeshResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_mesh_id: str = None,
    ):
        self.request_id = request_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
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


class DeleteServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        force: bool = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.force = force

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class DeleteServiceMeshResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


