# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, Dict, Any
except ImportError:
    pass


class AddVmAppToMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, service_name=None, ips=None, ports=None, labels=None,
                 annotations=None, service_account=None, force=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace      # type: str
        self.service_name = service_name  # type: str
        self.ips = ips                  # type: str
        self.ports = ports              # type: str
        self.labels = labels            # type: str
        self.annotations = annotations  # type: str
        self.service_account = service_account  # type: str
        self.force = force              # type: bool

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.service_name, 'service_name')
        self.validate_required(self.ips, 'ips')
        self.validate_required(self.ports, 'ports')
        self.validate_required(self.labels, 'labels')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('Namespace') is not None:
            self.namespace = map.get('Namespace')
        if map.get('ServiceName') is not None:
            self.service_name = map.get('ServiceName')
        if map.get('Ips') is not None:
            self.ips = map.get('Ips')
        if map.get('Ports') is not None:
            self.ports = map.get('Ports')
        if map.get('Labels') is not None:
            self.labels = map.get('Labels')
        if map.get('Annotations') is not None:
            self.annotations = map.get('Annotations')
        if map.get('ServiceAccount') is not None:
            self.service_account = map.get('ServiceAccount')
        if map.get('Force') is not None:
            self.force = map.get('Force')
        return self


class AddVmAppToMeshResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            self.data = map.get('Data')
        return self


class GetVmAppMeshInfoRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class GetVmAppMeshInfoResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            self.data = map.get('Data')
        return self


class GetVmMetaRequest(TeaModel):
    def __init__(self, service_mesh_id=None, trust_domain=None, namespace=None, service_account=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.trust_domain = trust_domain  # type: str
        self.namespace = namespace      # type: str
        self.service_account = service_account  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.trust_domain is not None:
            result['TrustDomain'] = self.trust_domain
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_account is not None:
            result['ServiceAccount'] = self.service_account
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('TrustDomain') is not None:
            self.trust_domain = map.get('TrustDomain')
        if map.get('Namespace') is not None:
            self.namespace = map.get('Namespace')
        if map.get('ServiceAccount') is not None:
            self.service_account = map.get('ServiceAccount')
        return self


class GetVmMetaResponse(TeaModel):
    def __init__(self, request_id=None, vm_meta_info=None):
        self.request_id = request_id    # type: str
        self.vm_meta_info = vm_meta_info  # type: GetVmMetaResponseVmMetaInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vm_meta_info, 'vm_meta_info')
        if self.vm_meta_info:
            self.vm_meta_info.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vm_meta_info is not None:
            result['VmMetaInfo'] = self.vm_meta_info.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('VmMetaInfo') is not None:
            temp_model = GetVmMetaResponseVmMetaInfo()
            self.vm_meta_info = temp_model.from_map(map['VmMetaInfo'])
        return self


class GetVmMetaResponseVmMetaInfo(TeaModel):
    def __init__(self, root_cert_path=None, root_cert_content=None, key_path=None, key_content=None,
                 cert_chain_path=None, cert_chain_content=None, envoy_env_path=None, envoy_env_content=None, hosts_path=None,
                 hosts_content=None, token_path=None, token_content=None):
        self.root_cert_path = root_cert_path  # type: str
        self.root_cert_content = root_cert_content  # type: str
        self.key_path = key_path        # type: str
        self.key_content = key_content  # type: str
        self.cert_chain_path = cert_chain_path  # type: str
        self.cert_chain_content = cert_chain_content  # type: str
        self.envoy_env_path = envoy_env_path  # type: str
        self.envoy_env_content = envoy_env_content  # type: str
        self.hosts_path = hosts_path    # type: str
        self.hosts_content = hosts_content  # type: str
        self.token_path = token_path    # type: str
        self.token_content = token_content  # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RootCertPath') is not None:
            self.root_cert_path = map.get('RootCertPath')
        if map.get('RootCertContent') is not None:
            self.root_cert_content = map.get('RootCertContent')
        if map.get('KeyPath') is not None:
            self.key_path = map.get('KeyPath')
        if map.get('KeyContent') is not None:
            self.key_content = map.get('KeyContent')
        if map.get('CertChainPath') is not None:
            self.cert_chain_path = map.get('CertChainPath')
        if map.get('CertChainContent') is not None:
            self.cert_chain_content = map.get('CertChainContent')
        if map.get('EnvoyEnvPath') is not None:
            self.envoy_env_path = map.get('EnvoyEnvPath')
        if map.get('EnvoyEnvContent') is not None:
            self.envoy_env_content = map.get('EnvoyEnvContent')
        if map.get('HostsPath') is not None:
            self.hosts_path = map.get('HostsPath')
        if map.get('HostsContent') is not None:
            self.hosts_content = map.get('HostsContent')
        if map.get('TokenPath') is not None:
            self.token_path = map.get('TokenPath')
        if map.get('TokenContent') is not None:
            self.token_content = map.get('TokenContent')
        return self


class RemoveVmAppFromMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, service_name=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace      # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.service_name, 'service_name')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('Namespace') is not None:
            self.namespace = map.get('Namespace')
        if map.get('ServiceName') is not None:
            self.service_name = map.get('ServiceName')
        return self


class RemoveVmAppFromMeshResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            self.data = map.get('Data')
        return self


class GetRegisteredServiceEndpointsRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, name=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace      # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('Namespace') is not None:
            self.namespace = map.get('Namespace')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        return self


class GetRegisteredServiceEndpointsResponse(TeaModel):
    def __init__(self, request_id=None, service_endpoints=None):
        self.request_id = request_id    # type: str
        self.service_endpoints = service_endpoints  # type: List[GetRegisteredServiceEndpointsResponseServiceEndpoints]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.service_endpoints, 'service_endpoints')
        if self.service_endpoints:
            for k in self.service_endpoints:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceEndpoints'] = []
        if self.service_endpoints is not None:
            for k in self.service_endpoints:
                result['ServiceEndpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.service_endpoints = []
        if map.get('ServiceEndpoints') is not None:
            for k in map.get('ServiceEndpoints'):
                temp_model = GetRegisteredServiceEndpointsResponseServiceEndpoints()
                self.service_endpoints.append(temp_model.from_map(k))
        return self


class GetRegisteredServiceEndpointsResponseServiceEndpoints(TeaModel):
    def __init__(self, address=None, cluster_id=None):
        self.address = address          # type: str
        self.cluster_id = cluster_id    # type: str

    def validate(self):
        self.validate_required(self.address, 'address')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = {}
        if self.address is not None:
            result['Address'] = self.address
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, map={}):
        if map.get('Address') is not None:
            self.address = map.get('Address')
        if map.get('ClusterId') is not None:
            self.cluster_id = map.get('ClusterId')
        return self


class GetServiceMeshSlbRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class GetServiceMeshSlbResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: List[GetServiceMeshSlbResponseData]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = GetServiceMeshSlbResponseData()
                self.data.append(temp_model.from_map(k))
        return self


class GetServiceMeshSlbResponseData(TeaModel):
    def __init__(self, load_balancer_id=None, status=None, server_health_status=None):
        self.load_balancer_id = load_balancer_id  # type: str
        self.status = status            # type: str
        self.server_health_status = server_health_status  # type: str

    def validate(self):
        self.validate_required(self.load_balancer_id, 'load_balancer_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.server_health_status, 'server_health_status')

    def to_map(self):
        result = {}
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.status is not None:
            result['Status'] = self.status
        if self.server_health_status is not None:
            result['ServerHealthStatus'] = self.server_health_status
        return result

    def from_map(self, map={}):
        if map.get('LoadBalancerId') is not None:
            self.load_balancer_id = map.get('LoadBalancerId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('ServerHealthStatus') is not None:
            self.server_health_status = map.get('ServerHealthStatus')
        return self


class GetRegisteredServicesRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace      # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('Namespace') is not None:
            self.namespace = map.get('Namespace')
        return self


class GetRegisteredServicesResponse(TeaModel):
    def __init__(self, request_id=None, services=None):
        self.request_id = request_id    # type: str
        self.services = services        # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.services, 'services')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.services is not None:
            result['Services'] = self.services
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Services') is not None:
            self.services = map.get('Services')
        return self


class GetDiagnosisRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class GetDiagnosisResponse(TeaModel):
    def __init__(self, request_id=None, result=None, run_at=None):
        self.request_id = request_id    # type: str
        self.result = result            # type: str
        self.run_at = run_at            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result, 'result')
        self.validate_required(self.run_at, 'run_at')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.run_at is not None:
            result['RunAt'] = self.run_at
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Result') is not None:
            self.result = map.get('Result')
        if map.get('RunAt') is not None:
            self.run_at = map.get('RunAt')
        return self


class GetRegisteredServiceNamespacesRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class GetRegisteredServiceNamespacesResponse(TeaModel):
    def __init__(self, request_id=None, namespaces=None):
        self.request_id = request_id    # type: str
        self.namespaces = namespaces    # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.namespaces, 'namespaces')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Namespaces') is not None:
            self.namespaces = map.get('Namespaces')
        return self


class RunDiagnosisRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class RunDiagnosisResponse(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id    # type: str
        self.result = result            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result, 'result')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Result') is not None:
            self.result = map.get('Result')
        return self


class RemoveClusterFromServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, cluster_id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.cluster_id = cluster_id    # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('ClusterId') is not None:
            self.cluster_id = map.get('ClusterId')
        return self


class RemoveClusterFromServiceMeshResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        return self


class AddClusterIntoServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, cluster_id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.cluster_id = cluster_id    # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('ClusterId') is not None:
            self.cluster_id = map.get('ClusterId')
        return self


class AddClusterIntoServiceMeshResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Code') is not None:
            self.code = map.get('Code')
        if map.get('Message') is not None:
            self.message = map.get('Message')
        return self


class UpdateIstioInjectionConfigRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, enable_istio_injection=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace      # type: str
        self.enable_istio_injection = enable_istio_injection  # type: bool

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.enable_istio_injection, 'enable_istio_injection')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.enable_istio_injection is not None:
            result['EnableIstioInjection'] = self.enable_istio_injection
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('Namespace') is not None:
            self.namespace = map.get('Namespace')
        if map.get('EnableIstioInjection') is not None:
            self.enable_istio_injection = map.get('EnableIstioInjection')
        return self


class UpdateIstioInjectionConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DescribeGuestClusterAccessLogDashboardsRequest(TeaModel):
    def __init__(self, k_8s_cluster_id=None):
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str

    def validate(self):
        self.validate_required(self.k_8s_cluster_id, 'k_8s_cluster_id')

    def to_map(self):
        result = {}
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, map={}):
        if map.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = map.get('K8sClusterId')
        return self


class DescribeGuestClusterAccessLogDashboardsResponse(TeaModel):
    def __init__(self, request_id=None, k_8s_cluster_id=None, dashboards=None):
        self.request_id = request_id    # type: str
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str
        self.dashboards = dashboards    # type: List[DescribeGuestClusterAccessLogDashboardsResponseDashboards]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.k_8s_cluster_id, 'k_8s_cluster_id')
        self.validate_required(self.dashboards, 'dashboards')
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = map.get('K8sClusterId')
        self.dashboards = []
        if map.get('Dashboards') is not None:
            for k in map.get('Dashboards'):
                temp_model = DescribeGuestClusterAccessLogDashboardsResponseDashboards()
                self.dashboards.append(temp_model.from_map(k))
        return self


class DescribeGuestClusterAccessLogDashboardsResponseDashboards(TeaModel):
    def __init__(self, title=None, url=None):
        self.title = title              # type: str
        self.url = url                  # type: str

    def validate(self):
        self.validate_required(self.title, 'title')
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, map={}):
        if map.get('Title') is not None:
            self.title = map.get('Title')
        if map.get('Url') is not None:
            self.url = map.get('Url')
        return self


class DescribeClusterPrometheusRequest(TeaModel):
    def __init__(self, service_mesh_id=None, k_8s_cluster_id=None, k_8s_cluster_region_id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str
        self.k_8s_cluster_region_id = k_8s_cluster_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.k_8s_cluster_region_id is not None:
            result['K8sClusterRegionId'] = self.k_8s_cluster_region_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = map.get('K8sClusterId')
        if map.get('K8sClusterRegionId') is not None:
            self.k_8s_cluster_region_id = map.get('K8sClusterRegionId')
        return self


class DescribeClusterPrometheusResponse(TeaModel):
    def __init__(self, request_id=None, prometheus=None):
        self.request_id = request_id    # type: str
        self.prometheus = prometheus    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.prometheus, 'prometheus')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Prometheus') is not None:
            self.prometheus = map.get('Prometheus')
        return self


class DescribeClusterGrafanaRequest(TeaModel):
    def __init__(self, service_mesh_id=None, k_8s_cluster_id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.k_8s_cluster_id, 'k_8s_cluster_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = map.get('K8sClusterId')
        return self


class DescribeClusterGrafanaResponse(TeaModel):
    def __init__(self, request_id=None, dashboards=None):
        self.request_id = request_id    # type: str
        self.dashboards = dashboards    # type: List[DescribeClusterGrafanaResponseDashboards]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dashboards, 'dashboards')
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.dashboards = []
        if map.get('Dashboards') is not None:
            for k in map.get('Dashboards'):
                temp_model = DescribeClusterGrafanaResponseDashboards()
                self.dashboards.append(temp_model.from_map(k))
        return self


class DescribeClusterGrafanaResponseDashboards(TeaModel):
    def __init__(self, url=None, title=None):
        self.url = url                  # type: str
        self.title = title              # type: str

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.title, 'title')

    def to_map(self):
        result = {}
        if self.url is not None:
            result['Url'] = self.url
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, map={}):
        if map.get('Url') is not None:
            self.url = map.get('Url')
        if map.get('Title') is not None:
            self.title = map.get('Title')
        return self


class DescribeCensRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DescribeCensResponse(TeaModel):
    def __init__(self, request_id=None, clusters=None):
        self.request_id = request_id    # type: str
        self.clusters = clusters        # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.clusters, 'clusters')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Clusters') is not None:
            self.clusters = map.get('Clusters')
        return self


class DescribeClustersInServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DescribeClustersInServiceMeshResponse(TeaModel):
    def __init__(self, request_id=None, clusters=None):
        self.request_id = request_id    # type: str
        self.clusters = clusters        # type: List[DescribeClustersInServiceMeshResponseClusters]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.clusters = []
        if map.get('Clusters') is not None:
            for k in map.get('Clusters'):
                temp_model = DescribeClustersInServiceMeshResponseClusters()
                self.clusters.append(temp_model.from_map(k))
        return self


class DescribeClustersInServiceMeshResponseClusters(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, creation_time=None, error_message=None, name=None,
                 region_id=None, state=None, update_time=None, version=None, vpc_id=None, sg_id=None, cluster_domain=None):
        self.cluster_id = cluster_id    # type: str
        self.cluster_type = cluster_type  # type: str
        self.creation_time = creation_time  # type: str
        self.error_message = error_message  # type: str
        self.name = name                # type: str
        self.region_id = region_id      # type: str
        self.state = state              # type: str
        self.update_time = update_time  # type: str
        self.version = version          # type: str
        self.vpc_id = vpc_id            # type: str
        self.sg_id = sg_id              # type: str
        self.cluster_domain = cluster_domain  # type: str

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

    def to_map(self):
        result = {}
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
        return result

    def from_map(self, map={}):
        if map.get('ClusterId') is not None:
            self.cluster_id = map.get('ClusterId')
        if map.get('ClusterType') is not None:
            self.cluster_type = map.get('ClusterType')
        if map.get('CreationTime') is not None:
            self.creation_time = map.get('CreationTime')
        if map.get('ErrorMessage') is not None:
            self.error_message = map.get('ErrorMessage')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('State') is not None:
            self.state = map.get('State')
        if map.get('UpdateTime') is not None:
            self.update_time = map.get('UpdateTime')
        if map.get('Version') is not None:
            self.version = map.get('Version')
        if map.get('VpcId') is not None:
            self.vpc_id = map.get('VpcId')
        if map.get('SgId') is not None:
            self.sg_id = map.get('SgId')
        if map.get('ClusterDomain') is not None:
            self.cluster_domain = map.get('ClusterDomain')
        return self


class DescribeIngressGatewaysRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DescribeIngressGatewaysResponse(TeaModel):
    def __init__(self, request_id=None, ingress_gateways=None):
        self.request_id = request_id    # type: str
        self.ingress_gateways = ingress_gateways  # type: List[Dict[str, Any]]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ingress_gateways, 'ingress_gateways')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ingress_gateways is not None:
            result['IngressGateways'] = self.ingress_gateways
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('IngressGateways') is not None:
            self.ingress_gateways = map.get('IngressGateways')
        return self


class DescribeUpgradeVersionRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DescribeUpgradeVersionResponse(TeaModel):
    def __init__(self, request_id=None, version=None):
        self.request_id = request_id    # type: str
        self.version = version          # type: DescribeUpgradeVersionResponseVersion

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.version, 'version')
        if self.version:
            self.version.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Version') is not None:
            temp_model = DescribeUpgradeVersionResponseVersion()
            self.version = temp_model.from_map(map['Version'])
        return self


class DescribeUpgradeVersionResponseVersion(TeaModel):
    def __init__(self, istio_version=None, istio_operator_version=None, kubernetes_version=None):
        self.istio_version = istio_version  # type: str
        self.istio_operator_version = istio_operator_version  # type: str
        self.kubernetes_version = kubernetes_version  # type: str

    def validate(self):
        self.validate_required(self.istio_version, 'istio_version')
        self.validate_required(self.istio_operator_version, 'istio_operator_version')
        self.validate_required(self.kubernetes_version, 'kubernetes_version')

    def to_map(self):
        result = {}
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.istio_operator_version is not None:
            result['IstioOperatorVersion'] = self.istio_operator_version
        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version
        return result

    def from_map(self, map={}):
        if map.get('IstioVersion') is not None:
            self.istio_version = map.get('IstioVersion')
        if map.get('IstioOperatorVersion') is not None:
            self.istio_operator_version = map.get('IstioOperatorVersion')
        if map.get('KubernetesVersion') is not None:
            self.kubernetes_version = map.get('KubernetesVersion')
        return self


class UpdateMeshFeatureRequest(TeaModel):
    def __init__(self, service_mesh_id=None, tracing=None, trace_sampling=None, locality_load_balancing=None,
                 telemetry=None, open_agent_policy=None, opalog_level=None, oparequest_cpu=None, oparequest_memory=None,
                 opalimit_cpu=None, opalimit_memory=None, enable_audit=None, audit_project=None, cluster_domain=None,
                 customized_zipkin=None, outbound_traffic_policy=None, proxy_request_cpu=None, proxy_request_memory=None,
                 proxy_limit_cpu=None, proxy_limit_memory=None, include_ipranges=None, enable_namespaces_by_default=None,
                 auto_injection_policy_enabled=None, sidecar_injector_request_cpu=None, sidecar_injector_request_memory=None,
                 sidecar_injector_limit_cpu=None, sidecar_injector_limit_memory=None, sidecar_injector_webhook_as_yaml=None,
                 cni_enabled=None, cni_exclude_namespaces=None, opa_enabled=None, http_10enabled=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.tracing = tracing          # type: bool
        self.trace_sampling = trace_sampling  # type: float
        self.locality_load_balancing = locality_load_balancing  # type: bool
        self.telemetry = telemetry      # type: bool
        self.open_agent_policy = open_agent_policy  # type: bool
        self.opalog_level = opalog_level  # type: str
        self.oparequest_cpu = oparequest_cpu  # type: str
        self.oparequest_memory = oparequest_memory  # type: str
        self.opalimit_cpu = opalimit_cpu  # type: str
        self.opalimit_memory = opalimit_memory  # type: str
        self.enable_audit = enable_audit  # type: bool
        self.audit_project = audit_project  # type: str
        self.cluster_domain = cluster_domain  # type: str
        self.customized_zipkin = customized_zipkin  # type: bool
        self.outbound_traffic_policy = outbound_traffic_policy  # type: str
        self.proxy_request_cpu = proxy_request_cpu  # type: str
        self.proxy_request_memory = proxy_request_memory  # type: str
        self.proxy_limit_cpu = proxy_limit_cpu  # type: str
        self.proxy_limit_memory = proxy_limit_memory  # type: str
        self.include_ipranges = include_ipranges  # type: str
        self.enable_namespaces_by_default = enable_namespaces_by_default  # type: bool
        self.auto_injection_policy_enabled = auto_injection_policy_enabled  # type: bool
        self.sidecar_injector_request_cpu = sidecar_injector_request_cpu  # type: str
        self.sidecar_injector_request_memory = sidecar_injector_request_memory  # type: str
        self.sidecar_injector_limit_cpu = sidecar_injector_limit_cpu  # type: str
        self.sidecar_injector_limit_memory = sidecar_injector_limit_memory  # type: str
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml  # type: str
        self.cni_enabled = cni_enabled  # type: bool
        self.cni_exclude_namespaces = cni_exclude_namespaces  # type: str
        self.opa_enabled = opa_enabled  # type: bool
        self.http_10enabled = http_10enabled  # type: bool

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
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
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('Tracing') is not None:
            self.tracing = map.get('Tracing')
        if map.get('TraceSampling') is not None:
            self.trace_sampling = map.get('TraceSampling')
        if map.get('LocalityLoadBalancing') is not None:
            self.locality_load_balancing = map.get('LocalityLoadBalancing')
        if map.get('Telemetry') is not None:
            self.telemetry = map.get('Telemetry')
        if map.get('OpenAgentPolicy') is not None:
            self.open_agent_policy = map.get('OpenAgentPolicy')
        if map.get('OPALogLevel') is not None:
            self.opalog_level = map.get('OPALogLevel')
        if map.get('OPARequestCPU') is not None:
            self.oparequest_cpu = map.get('OPARequestCPU')
        if map.get('OPARequestMemory') is not None:
            self.oparequest_memory = map.get('OPARequestMemory')
        if map.get('OPALimitCPU') is not None:
            self.opalimit_cpu = map.get('OPALimitCPU')
        if map.get('OPALimitMemory') is not None:
            self.opalimit_memory = map.get('OPALimitMemory')
        if map.get('EnableAudit') is not None:
            self.enable_audit = map.get('EnableAudit')
        if map.get('AuditProject') is not None:
            self.audit_project = map.get('AuditProject')
        if map.get('ClusterDomain') is not None:
            self.cluster_domain = map.get('ClusterDomain')
        if map.get('CustomizedZipkin') is not None:
            self.customized_zipkin = map.get('CustomizedZipkin')
        if map.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = map.get('OutboundTrafficPolicy')
        if map.get('ProxyRequestCPU') is not None:
            self.proxy_request_cpu = map.get('ProxyRequestCPU')
        if map.get('ProxyRequestMemory') is not None:
            self.proxy_request_memory = map.get('ProxyRequestMemory')
        if map.get('ProxyLimitCPU') is not None:
            self.proxy_limit_cpu = map.get('ProxyLimitCPU')
        if map.get('ProxyLimitMemory') is not None:
            self.proxy_limit_memory = map.get('ProxyLimitMemory')
        if map.get('IncludeIPRanges') is not None:
            self.include_ipranges = map.get('IncludeIPRanges')
        if map.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = map.get('EnableNamespacesByDefault')
        if map.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = map.get('AutoInjectionPolicyEnabled')
        if map.get('SidecarInjectorRequestCPU') is not None:
            self.sidecar_injector_request_cpu = map.get('SidecarInjectorRequestCPU')
        if map.get('SidecarInjectorRequestMemory') is not None:
            self.sidecar_injector_request_memory = map.get('SidecarInjectorRequestMemory')
        if map.get('SidecarInjectorLimitCPU') is not None:
            self.sidecar_injector_limit_cpu = map.get('SidecarInjectorLimitCPU')
        if map.get('SidecarInjectorLimitMemory') is not None:
            self.sidecar_injector_limit_memory = map.get('SidecarInjectorLimitMemory')
        if map.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = map.get('SidecarInjectorWebhookAsYaml')
        if map.get('CniEnabled') is not None:
            self.cni_enabled = map.get('CniEnabled')
        if map.get('CniExcludeNamespaces') is not None:
            self.cni_exclude_namespaces = map.get('CniExcludeNamespaces')
        if map.get('OpaEnabled') is not None:
            self.opa_enabled = map.get('OpaEnabled')
        if map.get('Http10Enabled') is not None:
            self.http_10enabled = map.get('Http10Enabled')
        return self


class UpdateMeshFeatureResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class UpgradeMeshVersionRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class UpgradeMeshVersionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DescribeServiceMeshesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DescribeServiceMeshesResponse(TeaModel):
    def __init__(self, request_id=None, service_meshes=None):
        self.request_id = request_id    # type: str
        self.service_meshes = service_meshes  # type: List[DescribeServiceMeshesResponseServiceMeshes]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.service_meshes, 'service_meshes')
        if self.service_meshes:
            for k in self.service_meshes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceMeshes'] = []
        if self.service_meshes is not None:
            for k in self.service_meshes:
                result['ServiceMeshes'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.service_meshes = []
        if map.get('ServiceMeshes') is not None:
            for k in map.get('ServiceMeshes'):
                temp_model = DescribeServiceMeshesResponseServiceMeshes()
                self.service_meshes.append(temp_model.from_map(k))
        return self


class DescribeServiceMeshesResponseServiceMeshesEndpoints(TeaModel):
    def __init__(self, intranet_api_server_endpoint=None, intranet_pilot_endpoint=None,
                 public_api_server_endpoint=None, public_pilot_endpoint=None, reverse_tunnel_endpoint=None):
        self.intranet_api_server_endpoint = intranet_api_server_endpoint  # type: str
        self.intranet_pilot_endpoint = intranet_pilot_endpoint  # type: str
        self.public_api_server_endpoint = public_api_server_endpoint  # type: str
        self.public_pilot_endpoint = public_pilot_endpoint  # type: str
        self.reverse_tunnel_endpoint = reverse_tunnel_endpoint  # type: str

    def validate(self):
        self.validate_required(self.intranet_api_server_endpoint, 'intranet_api_server_endpoint')
        self.validate_required(self.intranet_pilot_endpoint, 'intranet_pilot_endpoint')
        self.validate_required(self.public_api_server_endpoint, 'public_api_server_endpoint')
        self.validate_required(self.public_pilot_endpoint, 'public_pilot_endpoint')
        self.validate_required(self.reverse_tunnel_endpoint, 'reverse_tunnel_endpoint')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = map.get('IntranetApiServerEndpoint')
        if map.get('IntranetPilotEndpoint') is not None:
            self.intranet_pilot_endpoint = map.get('IntranetPilotEndpoint')
        if map.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = map.get('PublicApiServerEndpoint')
        if map.get('PublicPilotEndpoint') is not None:
            self.public_pilot_endpoint = map.get('PublicPilotEndpoint')
        if map.get('ReverseTunnelEndpoint') is not None:
            self.reverse_tunnel_endpoint = map.get('ReverseTunnelEndpoint')
        return self


class DescribeServiceMeshesResponseServiceMeshesServiceMeshInfo(TeaModel):
    def __init__(self, creation_time=None, error_message=None, name=None, region_id=None, service_mesh_id=None,
                 state=None, update_time=None, version=None):
        self.creation_time = creation_time  # type: str
        self.error_message = error_message  # type: str
        self.name = name                # type: str
        self.region_id = region_id      # type: str
        self.service_mesh_id = service_mesh_id  # type: str
        self.state = state              # type: str
        self.update_time = update_time  # type: str
        self.version = version          # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('CreationTime') is not None:
            self.creation_time = map.get('CreationTime')
        if map.get('ErrorMessage') is not None:
            self.error_message = map.get('ErrorMessage')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('State') is not None:
            self.state = map.get('State')
        if map.get('UpdateTime') is not None:
            self.update_time = map.get('UpdateTime')
        if map.get('Version') is not None:
            self.version = map.get('Version')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecLoadBalancer(TeaModel):
    def __init__(self, api_server_loadbalancer_id=None, api_server_public_eip=None, pilot_public_eip=None,
                 pilot_public_loadbalancer_id=None):
        self.api_server_loadbalancer_id = api_server_loadbalancer_id  # type: str
        self.api_server_public_eip = api_server_public_eip  # type: bool
        self.pilot_public_eip = pilot_public_eip  # type: bool
        self.pilot_public_loadbalancer_id = pilot_public_loadbalancer_id  # type: str

    def validate(self):
        self.validate_required(self.api_server_loadbalancer_id, 'api_server_loadbalancer_id')
        self.validate_required(self.api_server_public_eip, 'api_server_public_eip')
        self.validate_required(self.pilot_public_eip, 'pilot_public_eip')
        self.validate_required(self.pilot_public_loadbalancer_id, 'pilot_public_loadbalancer_id')

    def to_map(self):
        result = {}
        if self.api_server_loadbalancer_id is not None:
            result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.pilot_public_loadbalancer_id is not None:
            result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        return result

    def from_map(self, map={}):
        if map.get('ApiServerLoadbalancerId') is not None:
            self.api_server_loadbalancer_id = map.get('ApiServerLoadbalancerId')
        if map.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = map.get('ApiServerPublicEip')
        if map.get('PilotPublicEip') is not None:
            self.pilot_public_eip = map.get('PilotPublicEip')
        if map.get('PilotPublicLoadbalancerId') is not None:
            self.pilot_public_loadbalancer_id = map.get('PilotPublicLoadbalancerId')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigPilot(TeaModel):
    def __init__(self, trace_sampling=None, http_10enabled=None):
        self.trace_sampling = trace_sampling  # type: float
        self.http_10enabled = http_10enabled  # type: bool

    def validate(self):
        self.validate_required(self.trace_sampling, 'trace_sampling')
        self.validate_required(self.http_10enabled, 'http_10enabled')

    def to_map(self):
        result = {}
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        return result

    def from_map(self, map={}):
        if map.get('TraceSampling') is not None:
            self.trace_sampling = map.get('TraceSampling')
        if map.get('Http10Enabled') is not None:
            self.http_10enabled = map.get('Http10Enabled')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(self, enabled=None, exclude_namespaces=None):
        self.enabled = enabled          # type: bool
        self.exclude_namespaces = exclude_namespaces  # type: str

    def validate(self):
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.exclude_namespaces, 'exclude_namespaces')

    def to_map(self):
        result = {}
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.exclude_namespaces is not None:
            result['ExcludeNamespaces'] = self.exclude_namespaces
        return result

    def from_map(self, map={}):
        if map.get('Enabled') is not None:
            self.enabled = map.get('Enabled')
        if map.get('ExcludeNamespaces') is not None:
            self.exclude_namespaces = map.get('ExcludeNamespaces')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(self, enable_namespaces_by_default=None, auto_injection_policy_enabled=None,
                 init_cniconfiguration=None):
        self.enable_namespaces_by_default = enable_namespaces_by_default  # type: bool
        self.auto_injection_policy_enabled = auto_injection_policy_enabled  # type: bool
        self.init_cniconfiguration = init_cniconfiguration  # type: DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration

    def validate(self):
        self.validate_required(self.enable_namespaces_by_default, 'enable_namespaces_by_default')
        self.validate_required(self.auto_injection_policy_enabled, 'auto_injection_policy_enabled')
        self.validate_required(self.init_cniconfiguration, 'init_cniconfiguration')
        if self.init_cniconfiguration:
            self.init_cniconfiguration.validate()

    def to_map(self):
        result = {}
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.init_cniconfiguration is not None:
            result['InitCNIConfiguration'] = self.init_cniconfiguration.to_map()
        return result

    def from_map(self, map={}):
        if map.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = map.get('EnableNamespacesByDefault')
        if map.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = map.get('AutoInjectionPolicyEnabled')
        if map.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(map['InitCNIConfiguration'])
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecMeshConfig(TeaModel):
    def __init__(self, mtls=None, outbound_traffic_policy=None, strict_mtls=None, tracing=None, telemetry=None,
                 pilot=None, sidecar_injector=None):
        self.mtls = mtls                # type: bool
        self.outbound_traffic_policy = outbound_traffic_policy  # type: str
        self.strict_mtls = strict_mtls  # type: bool
        self.tracing = tracing          # type: bool
        self.telemetry = telemetry      # type: bool
        self.pilot = pilot              # type: DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigPilot
        self.sidecar_injector = sidecar_injector  # type: DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjector

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('Mtls') is not None:
            self.mtls = map.get('Mtls')
        if map.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = map.get('OutboundTrafficPolicy')
        if map.get('StrictMtls') is not None:
            self.strict_mtls = map.get('StrictMtls')
        if map.get('Tracing') is not None:
            self.tracing = map.get('Tracing')
        if map.get('Telemetry') is not None:
            self.telemetry = map.get('Telemetry')
        if map.get('Pilot') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(map['Pilot'])
        if map.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(map['SidecarInjector'])
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecNetwork(TeaModel):
    def __init__(self, security_group_id=None, vpc_id=None, v_switches=None):
        self.security_group_id = security_group_id  # type: str
        self.vpc_id = vpc_id            # type: str
        self.v_switches = v_switches    # type: List[str]

    def validate(self):
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switches, 'v_switches')

    def to_map(self):
        result = {}
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        return result

    def from_map(self, map={}):
        if map.get('SecurityGroupId') is not None:
            self.security_group_id = map.get('SecurityGroupId')
        if map.get('VpcId') is not None:
            self.vpc_id = map.get('VpcId')
        if map.get('VSwitches') is not None:
            self.v_switches = map.get('VSwitches')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpec(TeaModel):
    def __init__(self, load_balancer=None, mesh_config=None, network=None):
        self.load_balancer = load_balancer  # type: DescribeServiceMeshesResponseServiceMeshesSpecLoadBalancer
        self.mesh_config = mesh_config  # type: DescribeServiceMeshesResponseServiceMeshesSpecMeshConfig
        self.network = network          # type: DescribeServiceMeshesResponseServiceMeshesSpecNetwork

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
        result = {}
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, map={}):
        if map.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(map['LoadBalancer'])
        if map.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecMeshConfig()
            self.mesh_config = temp_model.from_map(map['MeshConfig'])
        if map.get('Network') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecNetwork()
            self.network = temp_model.from_map(map['Network'])
        return self


class DescribeServiceMeshesResponseServiceMeshes(TeaModel):
    def __init__(self, endpoints=None, service_mesh_info=None, spec=None, clusters=None):
        self.endpoints = endpoints      # type: DescribeServiceMeshesResponseServiceMeshesEndpoints
        self.service_mesh_info = service_mesh_info  # type: DescribeServiceMeshesResponseServiceMeshesServiceMeshInfo
        self.spec = spec                # type: DescribeServiceMeshesResponseServiceMeshesSpec
        self.clusters = clusters        # type: List[str]

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
        result = {}
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        return result

    def from_map(self, map={}):
        if map.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesEndpoints()
            self.endpoints = temp_model.from_map(map['Endpoints'])
        if map.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(map['ServiceMeshInfo'])
        if map.get('Spec') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpec()
            self.spec = temp_model.from_map(map['Spec'])
        if map.get('Clusters') is not None:
            self.clusters = map.get('Clusters')
        return self


class DescribeServiceMeshDetailRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DescribeServiceMeshDetailResponse(TeaModel):
    def __init__(self, request_id=None, service_mesh=None):
        self.request_id = request_id    # type: str
        self.service_mesh = service_mesh  # type: DescribeServiceMeshDetailResponseServiceMesh

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.service_mesh, 'service_mesh')
        if self.service_mesh:
            self.service_mesh.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_mesh is not None:
            result['ServiceMesh'] = self.service_mesh.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('ServiceMesh') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMesh()
            self.service_mesh = temp_model.from_map(map['ServiceMesh'])
        return self


class DescribeServiceMeshDetailResponseServiceMeshEndpoints(TeaModel):
    def __init__(self, intranet_api_server_endpoint=None, intranet_pilot_endpoint=None,
                 public_api_server_endpoint=None, public_pilot_endpoint=None):
        self.intranet_api_server_endpoint = intranet_api_server_endpoint  # type: str
        self.intranet_pilot_endpoint = intranet_pilot_endpoint  # type: str
        self.public_api_server_endpoint = public_api_server_endpoint  # type: str
        self.public_pilot_endpoint = public_pilot_endpoint  # type: str

    def validate(self):
        self.validate_required(self.intranet_api_server_endpoint, 'intranet_api_server_endpoint')
        self.validate_required(self.intranet_pilot_endpoint, 'intranet_pilot_endpoint')
        self.validate_required(self.public_api_server_endpoint, 'public_api_server_endpoint')
        self.validate_required(self.public_pilot_endpoint, 'public_pilot_endpoint')

    def to_map(self):
        result = {}
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.intranet_pilot_endpoint is not None:
            result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        if self.public_pilot_endpoint is not None:
            result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        return result

    def from_map(self, map={}):
        if map.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = map.get('IntranetApiServerEndpoint')
        if map.get('IntranetPilotEndpoint') is not None:
            self.intranet_pilot_endpoint = map.get('IntranetPilotEndpoint')
        if map.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = map.get('PublicApiServerEndpoint')
        if map.get('PublicPilotEndpoint') is not None:
            self.public_pilot_endpoint = map.get('PublicPilotEndpoint')
        return self


class DescribeServiceMeshDetailResponseServiceMeshServiceMeshInfo(TeaModel):
    def __init__(self, creation_time=None, error_message=None, name=None, region_id=None, service_mesh_id=None,
                 state=None, update_time=None, version=None):
        self.creation_time = creation_time  # type: str
        self.error_message = error_message  # type: str
        self.name = name                # type: str
        self.region_id = region_id      # type: str
        self.service_mesh_id = service_mesh_id  # type: str
        self.state = state              # type: str
        self.update_time = update_time  # type: str
        self.version = version          # type: str

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('CreationTime') is not None:
            self.creation_time = map.get('CreationTime')
        if map.get('ErrorMessage') is not None:
            self.error_message = map.get('ErrorMessage')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('State') is not None:
            self.state = map.get('State')
        if map.get('UpdateTime') is not None:
            self.update_time = map.get('UpdateTime')
        if map.get('Version') is not None:
            self.version = map.get('Version')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecLoadBalancer(TeaModel):
    def __init__(self, api_server_loadbalancer_id=None, api_server_public_eip=None, pilot_public_eip=None,
                 pilot_public_loadbalancer_id=None):
        self.api_server_loadbalancer_id = api_server_loadbalancer_id  # type: str
        self.api_server_public_eip = api_server_public_eip  # type: bool
        self.pilot_public_eip = pilot_public_eip  # type: bool
        self.pilot_public_loadbalancer_id = pilot_public_loadbalancer_id  # type: str

    def validate(self):
        self.validate_required(self.api_server_loadbalancer_id, 'api_server_loadbalancer_id')
        self.validate_required(self.api_server_public_eip, 'api_server_public_eip')
        self.validate_required(self.pilot_public_eip, 'pilot_public_eip')
        self.validate_required(self.pilot_public_loadbalancer_id, 'pilot_public_loadbalancer_id')

    def to_map(self):
        result = {}
        if self.api_server_loadbalancer_id is not None:
            result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.pilot_public_loadbalancer_id is not None:
            result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        return result

    def from_map(self, map={}):
        if map.get('ApiServerLoadbalancerId') is not None:
            self.api_server_loadbalancer_id = map.get('ApiServerLoadbalancerId')
        if map.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = map.get('ApiServerPublicEip')
        if map.get('PilotPublicEip') is not None:
            self.pilot_public_eip = map.get('PilotPublicEip')
        if map.get('PilotPublicLoadbalancerId') is not None:
            self.pilot_public_loadbalancer_id = map.get('PilotPublicLoadbalancerId')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPilot(TeaModel):
    def __init__(self, trace_sampling=None, http_10enabled=None):
        self.trace_sampling = trace_sampling  # type: float
        self.http_10enabled = http_10enabled  # type: bool

    def validate(self):
        self.validate_required(self.trace_sampling, 'trace_sampling')
        self.validate_required(self.http_10enabled, 'http_10enabled')

    def to_map(self):
        result = {}
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        return result

    def from_map(self, map={}):
        if map.get('TraceSampling') is not None:
            self.trace_sampling = map.get('TraceSampling')
        if map.get('Http10Enabled') is not None:
            self.http_10enabled = map.get('Http10Enabled')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigOPA(TeaModel):
    def __init__(self, enabled=None, log_level=None, request_cpu=None, request_memory=None, limit_cpu=None,
                 limit_memory=None):
        self.enabled = enabled          # type: bool
        self.log_level = log_level      # type: str
        self.request_cpu = request_cpu  # type: str
        self.request_memory = request_memory  # type: str
        self.limit_cpu = limit_cpu      # type: str
        self.limit_memory = limit_memory  # type: str

    def validate(self):
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.log_level, 'log_level')
        self.validate_required(self.request_cpu, 'request_cpu')
        self.validate_required(self.request_memory, 'request_memory')
        self.validate_required(self.limit_cpu, 'limit_cpu')
        self.validate_required(self.limit_memory, 'limit_memory')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('Enabled') is not None:
            self.enabled = map.get('Enabled')
        if map.get('LogLevel') is not None:
            self.log_level = map.get('LogLevel')
        if map.get('RequestCPU') is not None:
            self.request_cpu = map.get('RequestCPU')
        if map.get('RequestMemory') is not None:
            self.request_memory = map.get('RequestMemory')
        if map.get('LimitCPU') is not None:
            self.limit_cpu = map.get('LimitCPU')
        if map.get('LimitMemory') is not None:
            self.limit_memory = map.get('LimitMemory')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAudit(TeaModel):
    def __init__(self, enabled=None, project=None):
        self.enabled = enabled          # type: bool
        self.project = project          # type: str

    def validate(self):
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.project, 'project')

    def to_map(self):
        result = {}
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, map={}):
        if map.get('Enabled') is not None:
            self.enabled = map.get('Enabled')
        if map.get('Project') is not None:
            self.project = map.get('Project')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigProxy(TeaModel):
    def __init__(self, cluster_domain=None, request_cpu=None, request_memory=None, limit_cpu=None,
                 limit_memory=None):
        self.cluster_domain = cluster_domain  # type: str
        self.request_cpu = request_cpu  # type: str
        self.request_memory = request_memory  # type: str
        self.limit_cpu = limit_cpu      # type: str
        self.limit_memory = limit_memory  # type: str

    def validate(self):
        self.validate_required(self.cluster_domain, 'cluster_domain')
        self.validate_required(self.request_cpu, 'request_cpu')
        self.validate_required(self.request_memory, 'request_memory')
        self.validate_required(self.limit_cpu, 'limit_cpu')
        self.validate_required(self.limit_memory, 'limit_memory')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ClusterDomain') is not None:
            self.cluster_domain = map.get('ClusterDomain')
        if map.get('RequestCPU') is not None:
            self.request_cpu = map.get('RequestCPU')
        if map.get('RequestMemory') is not None:
            self.request_memory = map.get('RequestMemory')
        if map.get('LimitCPU') is not None:
            self.limit_cpu = map.get('LimitCPU')
        if map.get('LimitMemory') is not None:
            self.limit_memory = map.get('LimitMemory')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(self, enabled=None, exclude_namespaces=None):
        self.enabled = enabled          # type: bool
        self.exclude_namespaces = exclude_namespaces  # type: str

    def validate(self):
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.exclude_namespaces, 'exclude_namespaces')

    def to_map(self):
        result = {}
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.exclude_namespaces is not None:
            result['ExcludeNamespaces'] = self.exclude_namespaces
        return result

    def from_map(self, map={}):
        if map.get('Enabled') is not None:
            self.enabled = map.get('Enabled')
        if map.get('ExcludeNamespaces') is not None:
            self.exclude_namespaces = map.get('ExcludeNamespaces')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(self, enable_namespaces_by_default=None, auto_injection_policy_enabled=None, request_cpu=None,
                 request_memory=None, limit_cpu=None, limit_memory=None, sidecar_injector_webhook_as_yaml=None,
                 init_cniconfiguration=None):
        self.enable_namespaces_by_default = enable_namespaces_by_default  # type: bool
        self.auto_injection_policy_enabled = auto_injection_policy_enabled  # type: bool
        self.request_cpu = request_cpu  # type: str
        self.request_memory = request_memory  # type: str
        self.limit_cpu = limit_cpu      # type: str
        self.limit_memory = limit_memory  # type: str
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml  # type: str
        self.init_cniconfiguration = init_cniconfiguration  # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = map.get('EnableNamespacesByDefault')
        if map.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = map.get('AutoInjectionPolicyEnabled')
        if map.get('RequestCPU') is not None:
            self.request_cpu = map.get('RequestCPU')
        if map.get('RequestMemory') is not None:
            self.request_memory = map.get('RequestMemory')
        if map.get('LimitCPU') is not None:
            self.limit_cpu = map.get('LimitCPU')
        if map.get('LimitMemory') is not None:
            self.limit_memory = map.get('LimitMemory')
        if map.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = map.get('SidecarInjectorWebhookAsYaml')
        if map.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(map['InitCNIConfiguration'])
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfig(TeaModel):
    def __init__(self, enable_locality_lb=None, telemetry=None, tracing=None, customized_zipkin=None,
                 outbound_traffic_policy=None, include_ipranges=None, pilot=None, opa=None, audit=None, proxy=None, sidecar_injector=None):
        self.enable_locality_lb = enable_locality_lb  # type: bool
        self.telemetry = telemetry      # type: bool
        self.tracing = tracing          # type: bool
        self.customized_zipkin = customized_zipkin  # type: bool
        self.outbound_traffic_policy = outbound_traffic_policy  # type: str
        self.include_ipranges = include_ipranges  # type: str
        self.pilot = pilot              # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPilot
        self.opa = opa                  # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigOPA
        self.audit = audit              # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAudit
        self.proxy = proxy              # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigProxy
        self.sidecar_injector = sidecar_injector  # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjector

    def validate(self):
        self.validate_required(self.enable_locality_lb, 'enable_locality_lb')
        self.validate_required(self.telemetry, 'telemetry')
        self.validate_required(self.tracing, 'tracing')
        self.validate_required(self.customized_zipkin, 'customized_zipkin')
        self.validate_required(self.outbound_traffic_policy, 'outbound_traffic_policy')
        self.validate_required(self.include_ipranges, 'include_ipranges')
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

    def to_map(self):
        result = {}
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
        return result

    def from_map(self, map={}):
        if map.get('EnableLocalityLB') is not None:
            self.enable_locality_lb = map.get('EnableLocalityLB')
        if map.get('Telemetry') is not None:
            self.telemetry = map.get('Telemetry')
        if map.get('Tracing') is not None:
            self.tracing = map.get('Tracing')
        if map.get('CustomizedZipkin') is not None:
            self.customized_zipkin = map.get('CustomizedZipkin')
        if map.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = map.get('OutboundTrafficPolicy')
        if map.get('IncludeIPRanges') is not None:
            self.include_ipranges = map.get('IncludeIPRanges')
        if map.get('Pilot') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(map['Pilot'])
        if map.get('OPA') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigOPA()
            self.opa = temp_model.from_map(map['OPA'])
        if map.get('Audit') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAudit()
            self.audit = temp_model.from_map(map['Audit'])
        if map.get('Proxy') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigProxy()
            self.proxy = temp_model.from_map(map['Proxy'])
        if map.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(map['SidecarInjector'])
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecNetwork(TeaModel):
    def __init__(self, security_group_id=None, vpc_id=None, v_switches=None):
        self.security_group_id = security_group_id  # type: str
        self.vpc_id = vpc_id            # type: str
        self.v_switches = v_switches    # type: List[str]

    def validate(self):
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switches, 'v_switches')

    def to_map(self):
        result = {}
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        return result

    def from_map(self, map={}):
        if map.get('SecurityGroupId') is not None:
            self.security_group_id = map.get('SecurityGroupId')
        if map.get('VpcId') is not None:
            self.vpc_id = map.get('VpcId')
        if map.get('VSwitches') is not None:
            self.v_switches = map.get('VSwitches')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpec(TeaModel):
    def __init__(self, load_balancer=None, mesh_config=None, network=None):
        self.load_balancer = load_balancer  # type: DescribeServiceMeshDetailResponseServiceMeshSpecLoadBalancer
        self.mesh_config = mesh_config  # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfig
        self.network = network          # type: DescribeServiceMeshDetailResponseServiceMeshSpecNetwork

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
        result = {}
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, map={}):
        if map.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(map['LoadBalancer'])
        if map.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfig()
            self.mesh_config = temp_model.from_map(map['MeshConfig'])
        if map.get('Network') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecNetwork()
            self.network = temp_model.from_map(map['Network'])
        return self


class DescribeServiceMeshDetailResponseServiceMesh(TeaModel):
    def __init__(self, endpoints=None, service_mesh_info=None, spec=None, clusters=None):
        self.endpoints = endpoints      # type: DescribeServiceMeshDetailResponseServiceMeshEndpoints
        self.service_mesh_info = service_mesh_info  # type: DescribeServiceMeshDetailResponseServiceMeshServiceMeshInfo
        self.spec = spec                # type: DescribeServiceMeshDetailResponseServiceMeshSpec
        self.clusters = clusters        # type: List[str]

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
        result = {}
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        return result

    def from_map(self, map={}):
        if map.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshEndpoints()
            self.endpoints = temp_model.from_map(map['Endpoints'])
        if map.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(map['ServiceMeshInfo'])
        if map.get('Spec') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpec()
            self.spec = temp_model.from_map(map['Spec'])
        if map.get('Clusters') is not None:
            self.clusters = map.get('Clusters')
        return self


class DescribeServiceMeshKubeconfigRequest(TeaModel):
    def __init__(self, service_mesh_id=None, private_ip_address=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.private_ip_address = private_ip_address  # type: bool

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('PrivateIpAddress') is not None:
            self.private_ip_address = map.get('PrivateIpAddress')
        return self


class DescribeServiceMeshKubeconfigResponse(TeaModel):
    def __init__(self, kubeconfig=None, request_id=None):
        self.kubeconfig = kubeconfig    # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.kubeconfig, 'kubeconfig')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.kubeconfig is not None:
            result['Kubeconfig'] = self.kubeconfig
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Kubeconfig') is not None:
            self.kubeconfig = map.get('Kubeconfig')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class CreateServiceMeshRequest(TeaModel):
    def __init__(self, region_id=None, istio_version=None, vpc_id=None, api_server_public_eip=None,
                 pilot_public_eip=None, tracing=None, name=None, v_switches=None, trace_sampling=None, locality_load_balancing=None,
                 telemetry=None, open_agent_policy=None, opalog_level=None, oparequest_cpu=None, oparequest_memory=None,
                 opalimit_cpu=None, opalimit_memory=None, enable_audit=None, audit_project=None, proxy_request_cpu=None,
                 proxy_request_memory=None, proxy_limit_cpu=None, proxy_limit_memory=None, include_ipranges=None, exclude_ipranges=None,
                 exclude_outbound_ports=None, exclude_inbound_ports=None, opa_enabled=None):
        self.region_id = region_id      # type: str
        self.istio_version = istio_version  # type: str
        self.vpc_id = vpc_id            # type: str
        self.api_server_public_eip = api_server_public_eip  # type: bool
        self.pilot_public_eip = pilot_public_eip  # type: bool
        self.tracing = tracing          # type: bool
        self.name = name                # type: str
        self.v_switches = v_switches    # type: str
        self.trace_sampling = trace_sampling  # type: float
        self.locality_load_balancing = locality_load_balancing  # type: bool
        self.telemetry = telemetry      # type: bool
        self.open_agent_policy = open_agent_policy  # type: bool
        self.opalog_level = opalog_level  # type: str
        self.oparequest_cpu = oparequest_cpu  # type: str
        self.oparequest_memory = oparequest_memory  # type: str
        self.opalimit_cpu = opalimit_cpu  # type: str
        self.opalimit_memory = opalimit_memory  # type: str
        self.enable_audit = enable_audit  # type: bool
        self.audit_project = audit_project  # type: str
        self.proxy_request_cpu = proxy_request_cpu  # type: str
        self.proxy_request_memory = proxy_request_memory  # type: str
        self.proxy_limit_cpu = proxy_limit_cpu  # type: str
        self.proxy_limit_memory = proxy_limit_memory  # type: str
        self.include_ipranges = include_ipranges  # type: str
        self.exclude_ipranges = exclude_ipranges  # type: str
        self.exclude_outbound_ports = exclude_outbound_ports  # type: str
        self.exclude_inbound_ports = exclude_inbound_ports  # type: str
        self.opa_enabled = opa_enabled  # type: bool

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switches, 'v_switches')

    def to_map(self):
        result = {}
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
        return result

    def from_map(self, map={}):
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('IstioVersion') is not None:
            self.istio_version = map.get('IstioVersion')
        if map.get('VpcId') is not None:
            self.vpc_id = map.get('VpcId')
        if map.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = map.get('ApiServerPublicEip')
        if map.get('PilotPublicEip') is not None:
            self.pilot_public_eip = map.get('PilotPublicEip')
        if map.get('Tracing') is not None:
            self.tracing = map.get('Tracing')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('VSwitches') is not None:
            self.v_switches = map.get('VSwitches')
        if map.get('TraceSampling') is not None:
            self.trace_sampling = map.get('TraceSampling')
        if map.get('LocalityLoadBalancing') is not None:
            self.locality_load_balancing = map.get('LocalityLoadBalancing')
        if map.get('Telemetry') is not None:
            self.telemetry = map.get('Telemetry')
        if map.get('OpenAgentPolicy') is not None:
            self.open_agent_policy = map.get('OpenAgentPolicy')
        if map.get('OPALogLevel') is not None:
            self.opalog_level = map.get('OPALogLevel')
        if map.get('OPARequestCPU') is not None:
            self.oparequest_cpu = map.get('OPARequestCPU')
        if map.get('OPARequestMemory') is not None:
            self.oparequest_memory = map.get('OPARequestMemory')
        if map.get('OPALimitCPU') is not None:
            self.opalimit_cpu = map.get('OPALimitCPU')
        if map.get('OPALimitMemory') is not None:
            self.opalimit_memory = map.get('OPALimitMemory')
        if map.get('EnableAudit') is not None:
            self.enable_audit = map.get('EnableAudit')
        if map.get('AuditProject') is not None:
            self.audit_project = map.get('AuditProject')
        if map.get('ProxyRequestCPU') is not None:
            self.proxy_request_cpu = map.get('ProxyRequestCPU')
        if map.get('ProxyRequestMemory') is not None:
            self.proxy_request_memory = map.get('ProxyRequestMemory')
        if map.get('ProxyLimitCPU') is not None:
            self.proxy_limit_cpu = map.get('ProxyLimitCPU')
        if map.get('ProxyLimitMemory') is not None:
            self.proxy_limit_memory = map.get('ProxyLimitMemory')
        if map.get('IncludeIPRanges') is not None:
            self.include_ipranges = map.get('IncludeIPRanges')
        if map.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = map.get('ExcludeIPRanges')
        if map.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = map.get('ExcludeOutboundPorts')
        if map.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = map.get('ExcludeInboundPorts')
        if map.get('OpaEnabled') is not None:
            self.opa_enabled = map.get('OpaEnabled')
        return self


class CreateServiceMeshResponse(TeaModel):
    def __init__(self, request_id=None, service_mesh_id=None):
        self.request_id = request_id    # type: str
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DeleteServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, force=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.force = force              # type: bool

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, map={}):
        if map.get('ServiceMeshId') is not None:
            self.service_mesh_id = map.get('ServiceMeshId')
        if map.get('Force') is not None:
            self.force = map.get('Force')
        return self


class DeleteServiceMeshResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self
