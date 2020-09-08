# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddVmAppToMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, service_name=None, ips=None, ports=None, labels=None,
                 annotations=None, service_account=None, force=None):
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
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['Namespace'] = self.namespace
        result['ServiceName'] = self.service_name
        result['Ips'] = self.ips
        result['Ports'] = self.ports
        result['Labels'] = self.labels
        result['Annotations'] = self.annotations
        result['ServiceAccount'] = self.service_account
        result['Force'] = self.force
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.namespace = map.get('Namespace')
        self.service_name = map.get('ServiceName')
        self.ips = map.get('Ips')
        self.ports = map.get('Ports')
        self.labels = map.get('Labels')
        self.annotations = map.get('Annotations')
        self.service_account = map.get('ServiceAccount')
        self.force = map.get('Force')
        return self


class AddVmAppToMeshResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class GetVmAppMeshInfoRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class GetVmAppMeshInfoResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class GetVmMetaRequest(TeaModel):
    def __init__(self, service_mesh_id=None, trust_domain=None, namespace=None, service_account=None):
        self.service_mesh_id = service_mesh_id
        self.trust_domain = trust_domain
        self.namespace = namespace
        self.service_account = service_account

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['TrustDomain'] = self.trust_domain
        result['Namespace'] = self.namespace
        result['ServiceAccount'] = self.service_account
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.trust_domain = map.get('TrustDomain')
        self.namespace = map.get('Namespace')
        self.service_account = map.get('ServiceAccount')
        return self


class GetVmMetaResponse(TeaModel):
    def __init__(self, request_id=None, vm_meta_info=None):
        self.request_id = request_id
        self.vm_meta_info = vm_meta_info  # type: GetVmMetaResponseVmMetaInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.vm_meta_info, 'vm_meta_info')
        if self.vm_meta_info:
            self.vm_meta_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.vm_meta_info is not None:
            result['VmMetaInfo'] = self.vm_meta_info.to_map()
        else:
            result['VmMetaInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('VmMetaInfo') is not None:
            temp_model = GetVmMetaResponseVmMetaInfo()
            self.vm_meta_info = temp_model.from_map(map['VmMetaInfo'])
        else:
            self.vm_meta_info = None
        return self


class GetVmMetaResponseVmMetaInfo(TeaModel):
    def __init__(self, root_cert_path=None, root_cert_content=None, key_path=None, key_content=None,
                 cert_chain_path=None, cert_chain_content=None, envoy_env_path=None, envoy_env_content=None, hosts_path=None,
                 hosts_content=None):
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

    def to_map(self):
        result = {}
        result['RootCertPath'] = self.root_cert_path
        result['RootCertContent'] = self.root_cert_content
        result['KeyPath'] = self.key_path
        result['KeyContent'] = self.key_content
        result['CertChainPath'] = self.cert_chain_path
        result['CertChainContent'] = self.cert_chain_content
        result['EnvoyEnvPath'] = self.envoy_env_path
        result['EnvoyEnvContent'] = self.envoy_env_content
        result['HostsPath'] = self.hosts_path
        result['HostsContent'] = self.hosts_content
        return result

    def from_map(self, map={}):
        self.root_cert_path = map.get('RootCertPath')
        self.root_cert_content = map.get('RootCertContent')
        self.key_path = map.get('KeyPath')
        self.key_content = map.get('KeyContent')
        self.cert_chain_path = map.get('CertChainPath')
        self.cert_chain_content = map.get('CertChainContent')
        self.envoy_env_path = map.get('EnvoyEnvPath')
        self.envoy_env_content = map.get('EnvoyEnvContent')
        self.hosts_path = map.get('HostsPath')
        self.hosts_content = map.get('HostsContent')
        return self


class RemoveVmAppFromMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, service_name=None):
        self.service_mesh_id = service_mesh_id
        self.namespace = namespace
        self.service_name = service_name

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.service_name, 'service_name')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['Namespace'] = self.namespace
        result['ServiceName'] = self.service_name
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.namespace = map.get('Namespace')
        self.service_name = map.get('ServiceName')
        return self


class RemoveVmAppFromMeshResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id
        self.data = data

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.data = map.get('Data')
        return self


class GetRegisteredServiceEndpointsRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, name=None):
        self.service_mesh_id = service_mesh_id
        self.namespace = namespace
        self.name = name

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['Namespace'] = self.namespace
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.namespace = map.get('Namespace')
        self.name = map.get('Name')
        return self


class GetRegisteredServiceEndpointsResponse(TeaModel):
    def __init__(self, request_id=None, service_endpoints=None):
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
        result = {}
        result['RequestId'] = self.request_id
        result['ServiceEndpoints'] = []
        if self.service_endpoints is not None:
            for k in self.service_endpoints:
                result['ServiceEndpoints'].append(k.to_map() if k else None)
        else:
            result['ServiceEndpoints'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.service_endpoints = []
        if map.get('ServiceEndpoints') is not None:
            for k in map.get('ServiceEndpoints'):
                temp_model = GetRegisteredServiceEndpointsResponseServiceEndpoints()
                self.service_endpoints.append(temp_model.from_map(k))
        else:
            self.service_endpoints = None
        return self


class GetRegisteredServiceEndpointsResponseServiceEndpoints(TeaModel):
    def __init__(self, address=None, cluster_id=None):
        self.address = address
        self.cluster_id = cluster_id

    def validate(self):
        self.validate_required(self.address, 'address')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = {}
        result['Address'] = self.address
        result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, map={}):
        self.address = map.get('Address')
        self.cluster_id = map.get('ClusterId')
        return self


class GetServiceMeshSlbRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class GetServiceMeshSlbResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
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
        result = {}
        result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = GetServiceMeshSlbResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class GetServiceMeshSlbResponseData(TeaModel):
    def __init__(self, load_balancer_id=None, status=None, server_health_status=None):
        self.load_balancer_id = load_balancer_id
        self.status = status
        self.server_health_status = server_health_status

    def validate(self):
        self.validate_required(self.load_balancer_id, 'load_balancer_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.server_health_status, 'server_health_status')

    def to_map(self):
        result = {}
        result['LoadBalancerId'] = self.load_balancer_id
        result['Status'] = self.status
        result['ServerHealthStatus'] = self.server_health_status
        return result

    def from_map(self, map={}):
        self.load_balancer_id = map.get('LoadBalancerId')
        self.status = map.get('Status')
        self.server_health_status = map.get('ServerHealthStatus')
        return self


class GetRegisteredServicesRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None):
        self.service_mesh_id = service_mesh_id
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['Namespace'] = self.namespace
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.namespace = map.get('Namespace')
        return self


class GetRegisteredServicesResponse(TeaModel):
    def __init__(self, request_id=None, services=None):
        self.request_id = request_id
        self.services = services

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.services, 'services')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Services'] = self.services
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.services = map.get('Services')
        return self


class GetDiagnosisRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class GetDiagnosisResponse(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id
        self.result = result

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result, 'result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Result'] = self.result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.result = map.get('Result')
        return self


class GetRegisteredServiceNamespacesRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class GetRegisteredServiceNamespacesResponse(TeaModel):
    def __init__(self, request_id=None, namespaces=None):
        self.request_id = request_id
        self.namespaces = namespaces

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.namespaces, 'namespaces')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Namespaces'] = self.namespaces
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.namespaces = map.get('Namespaces')
        return self


class RunDiagnosisRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class RunDiagnosisResponse(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id
        self.result = result

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.result, 'result')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Result'] = self.result
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.result = map.get('Result')
        return self


class RemoveClusterFromServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, cluster_id=None):
        self.service_mesh_id = service_mesh_id
        self.cluster_id = cluster_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.cluster_id = map.get('ClusterId')
        return self


class RemoveClusterFromServiceMeshResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        return self


class AddClusterIntoServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, cluster_id=None):
        self.service_mesh_id = service_mesh_id
        self.cluster_id = cluster_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.cluster_id = map.get('ClusterId')
        return self


class AddClusterIntoServiceMeshResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        return self


class UpdateIstioInjectionConfigRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, enable_istio_injection=None):
        self.service_mesh_id = service_mesh_id
        self.namespace = namespace
        self.enable_istio_injection = enable_istio_injection

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.enable_istio_injection, 'enable_istio_injection')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['Namespace'] = self.namespace
        result['EnableIstioInjection'] = self.enable_istio_injection
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.namespace = map.get('Namespace')
        self.enable_istio_injection = map.get('EnableIstioInjection')
        return self


class UpdateIstioInjectionConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeGuestClusterAccessLogDashboardsRequest(TeaModel):
    def __init__(self, k_8s_cluster_id=None):
        self.k_8s_cluster_id = k_8s_cluster_id

    def validate(self):
        self.validate_required(self.k_8s_cluster_id, 'k_8s_cluster_id')

    def to_map(self):
        result = {}
        result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, map={}):
        self.k_8s_cluster_id = map.get('K8sClusterId')
        return self


class DescribeGuestClusterAccessLogDashboardsResponse(TeaModel):
    def __init__(self, request_id=None, k_8s_cluster_id=None, dashboards=None):
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
        result = {}
        result['RequestId'] = self.request_id
        result['K8sClusterId'] = self.k_8s_cluster_id
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        else:
            result['Dashboards'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.k_8s_cluster_id = map.get('K8sClusterId')
        self.dashboards = []
        if map.get('Dashboards') is not None:
            for k in map.get('Dashboards'):
                temp_model = DescribeGuestClusterAccessLogDashboardsResponseDashboards()
                self.dashboards.append(temp_model.from_map(k))
        else:
            self.dashboards = None
        return self


class DescribeGuestClusterAccessLogDashboardsResponseDashboards(TeaModel):
    def __init__(self, title=None, url=None):
        self.title = title
        self.url = url

    def validate(self):
        self.validate_required(self.title, 'title')
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        result['Title'] = self.title
        result['Url'] = self.url
        return result

    def from_map(self, map={}):
        self.title = map.get('Title')
        self.url = map.get('Url')
        return self


class DescribeClusterPrometheusRequest(TeaModel):
    def __init__(self, service_mesh_id=None, k_8s_cluster_id=None, k_8s_cluster_region_id=None):
        self.service_mesh_id = service_mesh_id
        self.k_8s_cluster_id = k_8s_cluster_id
        self.k_8s_cluster_region_id = k_8s_cluster_region_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['K8sClusterId'] = self.k_8s_cluster_id
        result['K8sClusterRegionId'] = self.k_8s_cluster_region_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.k_8s_cluster_id = map.get('K8sClusterId')
        self.k_8s_cluster_region_id = map.get('K8sClusterRegionId')
        return self


class DescribeClusterPrometheusResponse(TeaModel):
    def __init__(self, request_id=None, prometheus=None):
        self.request_id = request_id
        self.prometheus = prometheus

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.prometheus, 'prometheus')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Prometheus'] = self.prometheus
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.prometheus = map.get('Prometheus')
        return self


class DescribeClusterGrafanaRequest(TeaModel):
    def __init__(self, service_mesh_id=None, k_8s_cluster_id=None):
        self.service_mesh_id = service_mesh_id
        self.k_8s_cluster_id = k_8s_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.k_8s_cluster_id = map.get('K8sClusterId')
        return self


class DescribeClusterGrafanaResponse(TeaModel):
    def __init__(self, request_id=None, dashboards=None):
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
        result = {}
        result['RequestId'] = self.request_id
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        else:
            result['Dashboards'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dashboards = []
        if map.get('Dashboards') is not None:
            for k in map.get('Dashboards'):
                temp_model = DescribeClusterGrafanaResponseDashboards()
                self.dashboards.append(temp_model.from_map(k))
        else:
            self.dashboards = None
        return self


class DescribeClusterGrafanaResponseDashboards(TeaModel):
    def __init__(self, url=None, title=None):
        self.url = url
        self.title = title

    def validate(self):
        self.validate_required(self.url, 'url')
        self.validate_required(self.title, 'title')

    def to_map(self):
        result = {}
        result['Url'] = self.url
        result['Title'] = self.title
        return result

    def from_map(self, map={}):
        self.url = map.get('Url')
        self.title = map.get('Title')
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, map={}):
        self.accept_language = map.get('AcceptLanguage')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, request_id=None, business_locations=None):
        self.request_id = request_id
        self.business_locations = business_locations

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.business_locations, 'business_locations')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BusinessLocations'] = self.business_locations
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.business_locations = map.get('BusinessLocations')
        return self


class DescribeCensRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DescribeCensResponse(TeaModel):
    def __init__(self, request_id=None, clusters=None):
        self.request_id = request_id
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.clusters, 'clusters')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Clusters'] = self.clusters
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.clusters = map.get('Clusters')
        return self


class DescribeClustersInServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DescribeClustersInServiceMeshResponse(TeaModel):
    def __init__(self, request_id=None, clusters=None):
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
        result = {}
        result['RequestId'] = self.request_id
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        else:
            result['Clusters'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.clusters = []
        if map.get('Clusters') is not None:
            for k in map.get('Clusters'):
                temp_model = DescribeClustersInServiceMeshResponseClusters()
                self.clusters.append(temp_model.from_map(k))
        else:
            self.clusters = None
        return self


class DescribeClustersInServiceMeshResponseClusters(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, creation_time=None, error_message=None, name=None,
                 region_id=None, state=None, update_time=None, version=None, vpc_id=None, sg_id=None, cluster_domain=None):
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
        result['ClusterId'] = self.cluster_id
        result['ClusterType'] = self.cluster_type
        result['CreationTime'] = self.creation_time
        result['ErrorMessage'] = self.error_message
        result['Name'] = self.name
        result['RegionId'] = self.region_id
        result['State'] = self.state
        result['UpdateTime'] = self.update_time
        result['Version'] = self.version
        result['VpcId'] = self.vpc_id
        result['SgId'] = self.sg_id
        result['ClusterDomain'] = self.cluster_domain
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        self.cluster_type = map.get('ClusterType')
        self.creation_time = map.get('CreationTime')
        self.error_message = map.get('ErrorMessage')
        self.name = map.get('Name')
        self.region_id = map.get('RegionId')
        self.state = map.get('State')
        self.update_time = map.get('UpdateTime')
        self.version = map.get('Version')
        self.vpc_id = map.get('VpcId')
        self.sg_id = map.get('SgId')
        self.cluster_domain = map.get('ClusterDomain')
        return self


class DescribeIngressGatewaysRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DescribeIngressGatewaysResponse(TeaModel):
    def __init__(self, request_id=None, ingress_gateways=None):
        self.request_id = request_id
        self.ingress_gateways = ingress_gateways

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ingress_gateways, 'ingress_gateways')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['IngressGateways'] = self.ingress_gateways
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ingress_gateways = map.get('IngressGateways')
        return self


class DescribeUpgradeVersionRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DescribeUpgradeVersionResponse(TeaModel):
    def __init__(self, request_id=None, version=None):
        self.request_id = request_id
        self.version = version  # type: DescribeUpgradeVersionResponseVersion

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.version, 'version')
        if self.version:
            self.version.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version.to_map()
        else:
            result['Version'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Version') is not None:
            temp_model = DescribeUpgradeVersionResponseVersion()
            self.version = temp_model.from_map(map['Version'])
        else:
            self.version = None
        return self


class DescribeUpgradeVersionResponseVersion(TeaModel):
    def __init__(self, istio_version=None, istio_operator_version=None, kubernetes_version=None):
        self.istio_version = istio_version
        self.istio_operator_version = istio_operator_version
        self.kubernetes_version = kubernetes_version

    def validate(self):
        self.validate_required(self.istio_version, 'istio_version')
        self.validate_required(self.istio_operator_version, 'istio_operator_version')
        self.validate_required(self.kubernetes_version, 'kubernetes_version')

    def to_map(self):
        result = {}
        result['IstioVersion'] = self.istio_version
        result['IstioOperatorVersion'] = self.istio_operator_version
        result['KubernetesVersion'] = self.kubernetes_version
        return result

    def from_map(self, map={}):
        self.istio_version = map.get('IstioVersion')
        self.istio_operator_version = map.get('IstioOperatorVersion')
        self.kubernetes_version = map.get('KubernetesVersion')
        return self


class UpdateMeshFeatureRequest(TeaModel):
    def __init__(self, service_mesh_id=None, tracing=None, trace_sampling=None, locality_load_balancing=None,
                 telemetry=None, open_agent_policy=None, opalog_level=None, oparequest_cpu=None, oparequest_memory=None,
                 opalimit_cpu=None, opalimit_memory=None, enable_audit=None, audit_project=None, cluster_domain=None,
                 customized_zipkin=None, outbound_traffic_policy=None, proxy_request_cpu=None, proxy_request_memory=None,
                 proxy_limit_cpu=None, proxy_limit_memory=None, include_ipranges=None):
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

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['Tracing'] = self.tracing
        result['TraceSampling'] = self.trace_sampling
        result['LocalityLoadBalancing'] = self.locality_load_balancing
        result['Telemetry'] = self.telemetry
        result['OpenAgentPolicy'] = self.open_agent_policy
        result['OPALogLevel'] = self.opalog_level
        result['OPARequestCPU'] = self.oparequest_cpu
        result['OPARequestMemory'] = self.oparequest_memory
        result['OPALimitCPU'] = self.opalimit_cpu
        result['OPALimitMemory'] = self.opalimit_memory
        result['EnableAudit'] = self.enable_audit
        result['AuditProject'] = self.audit_project
        result['ClusterDomain'] = self.cluster_domain
        result['CustomizedZipkin'] = self.customized_zipkin
        result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        result['ProxyRequestCPU'] = self.proxy_request_cpu
        result['ProxyRequestMemory'] = self.proxy_request_memory
        result['ProxyLimitCPU'] = self.proxy_limit_cpu
        result['ProxyLimitMemory'] = self.proxy_limit_memory
        result['IncludeIPRanges'] = self.include_ipranges
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.tracing = map.get('Tracing')
        self.trace_sampling = map.get('TraceSampling')
        self.locality_load_balancing = map.get('LocalityLoadBalancing')
        self.telemetry = map.get('Telemetry')
        self.open_agent_policy = map.get('OpenAgentPolicy')
        self.opalog_level = map.get('OPALogLevel')
        self.oparequest_cpu = map.get('OPARequestCPU')
        self.oparequest_memory = map.get('OPARequestMemory')
        self.opalimit_cpu = map.get('OPALimitCPU')
        self.opalimit_memory = map.get('OPALimitMemory')
        self.enable_audit = map.get('EnableAudit')
        self.audit_project = map.get('AuditProject')
        self.cluster_domain = map.get('ClusterDomain')
        self.customized_zipkin = map.get('CustomizedZipkin')
        self.outbound_traffic_policy = map.get('OutboundTrafficPolicy')
        self.proxy_request_cpu = map.get('ProxyRequestCPU')
        self.proxy_request_memory = map.get('ProxyRequestMemory')
        self.proxy_limit_cpu = map.get('ProxyLimitCPU')
        self.proxy_limit_memory = map.get('ProxyLimitMemory')
        self.include_ipranges = map.get('IncludeIPRanges')
        return self


class UpdateMeshFeatureResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UpgradeMeshVersionRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class UpgradeMeshVersionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
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
        result = {}
        result['RequestId'] = self.request_id
        result['ServiceMeshes'] = []
        if self.service_meshes is not None:
            for k in self.service_meshes:
                result['ServiceMeshes'].append(k.to_map() if k else None)
        else:
            result['ServiceMeshes'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.service_meshes = []
        if map.get('ServiceMeshes') is not None:
            for k in map.get('ServiceMeshes'):
                temp_model = DescribeServiceMeshesResponseServiceMeshes()
                self.service_meshes.append(temp_model.from_map(k))
        else:
            self.service_meshes = None
        return self


class DescribeServiceMeshesResponseServiceMeshesEndpoints(TeaModel):
    def __init__(self, intranet_api_server_endpoint=None, intranet_pilot_endpoint=None,
                 public_api_server_endpoint=None, public_pilot_endpoint=None, reverse_tunnel_endpoint=None):
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
        result = {}
        result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        result['ReverseTunnelEndpoint'] = self.reverse_tunnel_endpoint
        return result

    def from_map(self, map={}):
        self.intranet_api_server_endpoint = map.get('IntranetApiServerEndpoint')
        self.intranet_pilot_endpoint = map.get('IntranetPilotEndpoint')
        self.public_api_server_endpoint = map.get('PublicApiServerEndpoint')
        self.public_pilot_endpoint = map.get('PublicPilotEndpoint')
        self.reverse_tunnel_endpoint = map.get('ReverseTunnelEndpoint')
        return self


class DescribeServiceMeshesResponseServiceMeshesServiceMeshInfo(TeaModel):
    def __init__(self, creation_time=None, error_message=None, name=None, region_id=None, service_mesh_id=None,
                 state=None, update_time=None, version=None):
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
        result = {}
        result['CreationTime'] = self.creation_time
        result['ErrorMessage'] = self.error_message
        result['Name'] = self.name
        result['RegionId'] = self.region_id
        result['ServiceMeshId'] = self.service_mesh_id
        result['State'] = self.state
        result['UpdateTime'] = self.update_time
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.creation_time = map.get('CreationTime')
        self.error_message = map.get('ErrorMessage')
        self.name = map.get('Name')
        self.region_id = map.get('RegionId')
        self.service_mesh_id = map.get('ServiceMeshId')
        self.state = map.get('State')
        self.update_time = map.get('UpdateTime')
        self.version = map.get('Version')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecLoadBalancer(TeaModel):
    def __init__(self, api_server_loadbalancer_id=None, api_server_public_eip=None, pilot_public_eip=None,
                 pilot_public_loadbalancer_id=None):
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
        result = {}
        result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        result['ApiServerPublicEip'] = self.api_server_public_eip
        result['PilotPublicEip'] = self.pilot_public_eip
        result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        return result

    def from_map(self, map={}):
        self.api_server_loadbalancer_id = map.get('ApiServerLoadbalancerId')
        self.api_server_public_eip = map.get('ApiServerPublicEip')
        self.pilot_public_eip = map.get('PilotPublicEip')
        self.pilot_public_loadbalancer_id = map.get('PilotPublicLoadbalancerId')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecMeshConfig(TeaModel):
    def __init__(self, mtls=None, outbound_traffic_policy=None, strict_mtls=None, tracing=None, telemetry=None):
        self.mtls = mtls
        self.outbound_traffic_policy = outbound_traffic_policy
        self.strict_mtls = strict_mtls
        self.tracing = tracing
        self.telemetry = telemetry

    def validate(self):
        self.validate_required(self.mtls, 'mtls')
        self.validate_required(self.outbound_traffic_policy, 'outbound_traffic_policy')
        self.validate_required(self.strict_mtls, 'strict_mtls')
        self.validate_required(self.tracing, 'tracing')
        self.validate_required(self.telemetry, 'telemetry')

    def to_map(self):
        result = {}
        result['Mtls'] = self.mtls
        result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        result['StrictMtls'] = self.strict_mtls
        result['Tracing'] = self.tracing
        result['Telemetry'] = self.telemetry
        return result

    def from_map(self, map={}):
        self.mtls = map.get('Mtls')
        self.outbound_traffic_policy = map.get('OutboundTrafficPolicy')
        self.strict_mtls = map.get('StrictMtls')
        self.tracing = map.get('Tracing')
        self.telemetry = map.get('Telemetry')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpecNetwork(TeaModel):
    def __init__(self, security_group_id=None, vpc_id=None, v_switches=None):
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
        self.v_switches = v_switches

    def validate(self):
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switches, 'v_switches')

    def to_map(self):
        result = {}
        result['SecurityGroupId'] = self.security_group_id
        result['VpcId'] = self.vpc_id
        result['VSwitches'] = self.v_switches
        return result

    def from_map(self, map={}):
        self.security_group_id = map.get('SecurityGroupId')
        self.vpc_id = map.get('VpcId')
        self.v_switches = map.get('VSwitches')
        return self


class DescribeServiceMeshesResponseServiceMeshesSpec(TeaModel):
    def __init__(self, load_balancer=None, mesh_config=None, network=None):
        self.load_balancer = load_balancer  # type: DescribeServiceMeshesResponseServiceMeshesSpecLoadBalancer
        self.mesh_config = mesh_config  # type: DescribeServiceMeshesResponseServiceMeshesSpecMeshConfig
        self.network = network  # type: DescribeServiceMeshesResponseServiceMeshesSpecNetwork

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
        else:
            result['LoadBalancer'] = None
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        else:
            result['MeshConfig'] = None
        if self.network is not None:
            result['Network'] = self.network.to_map()
        else:
            result['Network'] = None
        return result

    def from_map(self, map={}):
        if map.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(map['LoadBalancer'])
        else:
            self.load_balancer = None
        if map.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecMeshConfig()
            self.mesh_config = temp_model.from_map(map['MeshConfig'])
        else:
            self.mesh_config = None
        if map.get('Network') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpecNetwork()
            self.network = temp_model.from_map(map['Network'])
        else:
            self.network = None
        return self


class DescribeServiceMeshesResponseServiceMeshes(TeaModel):
    def __init__(self, endpoints=None, service_mesh_info=None, spec=None, clusters=None):
        self.endpoints = endpoints  # type: DescribeServiceMeshesResponseServiceMeshesEndpoints
        self.service_mesh_info = service_mesh_info  # type: DescribeServiceMeshesResponseServiceMeshesServiceMeshInfo
        self.spec = spec  # type: DescribeServiceMeshesResponseServiceMeshesSpec
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
        result = {}
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        else:
            result['Endpoints'] = None
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        else:
            result['ServiceMeshInfo'] = None
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        else:
            result['Spec'] = None
        result['Clusters'] = self.clusters
        return result

    def from_map(self, map={}):
        if map.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesEndpoints()
            self.endpoints = temp_model.from_map(map['Endpoints'])
        else:
            self.endpoints = None
        if map.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(map['ServiceMeshInfo'])
        else:
            self.service_mesh_info = None
        if map.get('Spec') is not None:
            temp_model = DescribeServiceMeshesResponseServiceMeshesSpec()
            self.spec = temp_model.from_map(map['Spec'])
        else:
            self.spec = None
        self.clusters = map.get('Clusters')
        return self


class DescribeServiceMeshDetailRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DescribeServiceMeshDetailResponse(TeaModel):
    def __init__(self, request_id=None, service_mesh=None):
        self.request_id = request_id
        self.service_mesh = service_mesh  # type: DescribeServiceMeshDetailResponseServiceMesh

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.service_mesh, 'service_mesh')
        if self.service_mesh:
            self.service_mesh.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.service_mesh is not None:
            result['ServiceMesh'] = self.service_mesh.to_map()
        else:
            result['ServiceMesh'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ServiceMesh') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMesh()
            self.service_mesh = temp_model.from_map(map['ServiceMesh'])
        else:
            self.service_mesh = None
        return self


class DescribeServiceMeshDetailResponseServiceMeshEndpoints(TeaModel):
    def __init__(self, intranet_api_server_endpoint=None, intranet_pilot_endpoint=None,
                 public_api_server_endpoint=None, public_pilot_endpoint=None):
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
        result = {}
        result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        return result

    def from_map(self, map={}):
        self.intranet_api_server_endpoint = map.get('IntranetApiServerEndpoint')
        self.intranet_pilot_endpoint = map.get('IntranetPilotEndpoint')
        self.public_api_server_endpoint = map.get('PublicApiServerEndpoint')
        self.public_pilot_endpoint = map.get('PublicPilotEndpoint')
        return self


class DescribeServiceMeshDetailResponseServiceMeshServiceMeshInfo(TeaModel):
    def __init__(self, creation_time=None, error_message=None, name=None, region_id=None, service_mesh_id=None,
                 state=None, update_time=None, version=None):
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
        result = {}
        result['CreationTime'] = self.creation_time
        result['ErrorMessage'] = self.error_message
        result['Name'] = self.name
        result['RegionId'] = self.region_id
        result['ServiceMeshId'] = self.service_mesh_id
        result['State'] = self.state
        result['UpdateTime'] = self.update_time
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.creation_time = map.get('CreationTime')
        self.error_message = map.get('ErrorMessage')
        self.name = map.get('Name')
        self.region_id = map.get('RegionId')
        self.service_mesh_id = map.get('ServiceMeshId')
        self.state = map.get('State')
        self.update_time = map.get('UpdateTime')
        self.version = map.get('Version')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecLoadBalancer(TeaModel):
    def __init__(self, api_server_loadbalancer_id=None, api_server_public_eip=None, pilot_public_eip=None,
                 pilot_public_loadbalancer_id=None):
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
        result = {}
        result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        result['ApiServerPublicEip'] = self.api_server_public_eip
        result['PilotPublicEip'] = self.pilot_public_eip
        result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        return result

    def from_map(self, map={}):
        self.api_server_loadbalancer_id = map.get('ApiServerLoadbalancerId')
        self.api_server_public_eip = map.get('ApiServerPublicEip')
        self.pilot_public_eip = map.get('PilotPublicEip')
        self.pilot_public_loadbalancer_id = map.get('PilotPublicLoadbalancerId')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPilot(TeaModel):
    def __init__(self, trace_sampling=None):
        self.trace_sampling = trace_sampling

    def validate(self):
        self.validate_required(self.trace_sampling, 'trace_sampling')

    def to_map(self):
        result = {}
        result['TraceSampling'] = self.trace_sampling
        return result

    def from_map(self, map={}):
        self.trace_sampling = map.get('TraceSampling')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigOPA(TeaModel):
    def __init__(self, enabled=None, log_level=None, request_cpu=None, request_memory=None, limit_cpu=None,
                 limit_memory=None):
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
        result = {}
        result['Enabled'] = self.enabled
        result['LogLevel'] = self.log_level
        result['RequestCPU'] = self.request_cpu
        result['RequestMemory'] = self.request_memory
        result['LimitCPU'] = self.limit_cpu
        result['LimitMemory'] = self.limit_memory
        return result

    def from_map(self, map={}):
        self.enabled = map.get('Enabled')
        self.log_level = map.get('LogLevel')
        self.request_cpu = map.get('RequestCPU')
        self.request_memory = map.get('RequestMemory')
        self.limit_cpu = map.get('LimitCPU')
        self.limit_memory = map.get('LimitMemory')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAudit(TeaModel):
    def __init__(self, enabled=None, project=None):
        self.enabled = enabled
        self.project = project

    def validate(self):
        self.validate_required(self.enabled, 'enabled')
        self.validate_required(self.project, 'project')

    def to_map(self):
        result = {}
        result['Enabled'] = self.enabled
        result['Project'] = self.project
        return result

    def from_map(self, map={}):
        self.enabled = map.get('Enabled')
        self.project = map.get('Project')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigProxy(TeaModel):
    def __init__(self, cluster_domain=None, request_cpu=None, request_memory=None, limit_cpu=None,
                 limit_memory=None):
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
        result = {}
        result['ClusterDomain'] = self.cluster_domain
        result['RequestCPU'] = self.request_cpu
        result['RequestMemory'] = self.request_memory
        result['LimitCPU'] = self.limit_cpu
        result['LimitMemory'] = self.limit_memory
        return result

    def from_map(self, map={}):
        self.cluster_domain = map.get('ClusterDomain')
        self.request_cpu = map.get('RequestCPU')
        self.request_memory = map.get('RequestMemory')
        self.limit_cpu = map.get('LimitCPU')
        self.limit_memory = map.get('LimitMemory')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfig(TeaModel):
    def __init__(self, enable_locality_lb=None, telemetry=None, tracing=None, customized_zipkin=None,
                 outbound_traffic_policy=None, include_ipranges=None, pilot=None, opa=None, audit=None, proxy=None):
        self.enable_locality_lb = enable_locality_lb
        self.telemetry = telemetry
        self.tracing = tracing
        self.customized_zipkin = customized_zipkin
        self.outbound_traffic_policy = outbound_traffic_policy
        self.include_ipranges = include_ipranges
        self.pilot = pilot  # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPilot
        self.opa = opa  # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigOPA
        self.audit = audit  # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAudit
        self.proxy = proxy  # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigProxy

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

    def to_map(self):
        result = {}
        result['EnableLocalityLB'] = self.enable_locality_lb
        result['Telemetry'] = self.telemetry
        result['Tracing'] = self.tracing
        result['CustomizedZipkin'] = self.customized_zipkin
        result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        result['IncludeIPRanges'] = self.include_ipranges
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        else:
            result['Pilot'] = None
        if self.opa is not None:
            result['OPA'] = self.opa.to_map()
        else:
            result['OPA'] = None
        if self.audit is not None:
            result['Audit'] = self.audit.to_map()
        else:
            result['Audit'] = None
        if self.proxy is not None:
            result['Proxy'] = self.proxy.to_map()
        else:
            result['Proxy'] = None
        return result

    def from_map(self, map={}):
        self.enable_locality_lb = map.get('EnableLocalityLB')
        self.telemetry = map.get('Telemetry')
        self.tracing = map.get('Tracing')
        self.customized_zipkin = map.get('CustomizedZipkin')
        self.outbound_traffic_policy = map.get('OutboundTrafficPolicy')
        self.include_ipranges = map.get('IncludeIPRanges')
        if map.get('Pilot') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(map['Pilot'])
        else:
            self.pilot = None
        if map.get('OPA') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigOPA()
            self.opa = temp_model.from_map(map['OPA'])
        else:
            self.opa = None
        if map.get('Audit') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigAudit()
            self.audit = temp_model.from_map(map['Audit'])
        else:
            self.audit = None
        if map.get('Proxy') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfigProxy()
            self.proxy = temp_model.from_map(map['Proxy'])
        else:
            self.proxy = None
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpecNetwork(TeaModel):
    def __init__(self, security_group_id=None, vpc_id=None, v_switches=None):
        self.security_group_id = security_group_id
        self.vpc_id = vpc_id
        self.v_switches = v_switches

    def validate(self):
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.v_switches, 'v_switches')

    def to_map(self):
        result = {}
        result['SecurityGroupId'] = self.security_group_id
        result['VpcId'] = self.vpc_id
        result['VSwitches'] = self.v_switches
        return result

    def from_map(self, map={}):
        self.security_group_id = map.get('SecurityGroupId')
        self.vpc_id = map.get('VpcId')
        self.v_switches = map.get('VSwitches')
        return self


class DescribeServiceMeshDetailResponseServiceMeshSpec(TeaModel):
    def __init__(self, load_balancer=None, mesh_config=None, network=None):
        self.load_balancer = load_balancer  # type: DescribeServiceMeshDetailResponseServiceMeshSpecLoadBalancer
        self.mesh_config = mesh_config  # type: DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfig
        self.network = network  # type: DescribeServiceMeshDetailResponseServiceMeshSpecNetwork

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
        else:
            result['LoadBalancer'] = None
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        else:
            result['MeshConfig'] = None
        if self.network is not None:
            result['Network'] = self.network.to_map()
        else:
            result['Network'] = None
        return result

    def from_map(self, map={}):
        if map.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(map['LoadBalancer'])
        else:
            self.load_balancer = None
        if map.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecMeshConfig()
            self.mesh_config = temp_model.from_map(map['MeshConfig'])
        else:
            self.mesh_config = None
        if map.get('Network') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpecNetwork()
            self.network = temp_model.from_map(map['Network'])
        else:
            self.network = None
        return self


class DescribeServiceMeshDetailResponseServiceMesh(TeaModel):
    def __init__(self, endpoints=None, service_mesh_info=None, spec=None, clusters=None):
        self.endpoints = endpoints  # type: DescribeServiceMeshDetailResponseServiceMeshEndpoints
        self.service_mesh_info = service_mesh_info  # type: DescribeServiceMeshDetailResponseServiceMeshServiceMeshInfo
        self.spec = spec  # type: DescribeServiceMeshDetailResponseServiceMeshSpec
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
        result = {}
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        else:
            result['Endpoints'] = None
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        else:
            result['ServiceMeshInfo'] = None
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        else:
            result['Spec'] = None
        result['Clusters'] = self.clusters
        return result

    def from_map(self, map={}):
        if map.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshEndpoints()
            self.endpoints = temp_model.from_map(map['Endpoints'])
        else:
            self.endpoints = None
        if map.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(map['ServiceMeshInfo'])
        else:
            self.service_mesh_info = None
        if map.get('Spec') is not None:
            temp_model = DescribeServiceMeshDetailResponseServiceMeshSpec()
            self.spec = temp_model.from_map(map['Spec'])
        else:
            self.spec = None
        self.clusters = map.get('Clusters')
        return self


class DescribeServiceMeshKubeconfigRequest(TeaModel):
    def __init__(self, service_mesh_id=None, private_ip_address=None):
        self.service_mesh_id = service_mesh_id
        self.private_ip_address = private_ip_address

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.private_ip_address = map.get('PrivateIpAddress')
        return self


class DescribeServiceMeshKubeconfigResponse(TeaModel):
    def __init__(self, kubeconfig=None, request_id=None):
        self.kubeconfig = kubeconfig
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.kubeconfig, 'kubeconfig')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Kubeconfig'] = self.kubeconfig
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.kubeconfig = map.get('Kubeconfig')
        self.request_id = map.get('RequestId')
        return self


class CreateServiceMeshRequest(TeaModel):
    def __init__(self, region_id=None, istio_version=None, vpc_id=None, api_server_public_eip=None,
                 pilot_public_eip=None, tracing=None, name=None, v_switches=None, trace_sampling=None, locality_load_balancing=None,
                 telemetry=None, open_agent_policy=None, opalog_level=None, oparequest_cpu=None, oparequest_memory=None,
                 opalimit_cpu=None, opalimit_memory=None, enable_audit=None, audit_project=None, proxy_request_cpu=None,
                 proxy_request_memory=None, proxy_limit_cpu=None, proxy_limit_memory=None, include_ipranges=None, exclude_ipranges=None,
                 exclude_outbound_ports=None, exclude_inbound_ports=None):
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

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.vpc_id, 'vpc_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['IstioVersion'] = self.istio_version
        result['VpcId'] = self.vpc_id
        result['ApiServerPublicEip'] = self.api_server_public_eip
        result['PilotPublicEip'] = self.pilot_public_eip
        result['Tracing'] = self.tracing
        result['Name'] = self.name
        result['VSwitches'] = self.v_switches
        result['TraceSampling'] = self.trace_sampling
        result['LocalityLoadBalancing'] = self.locality_load_balancing
        result['Telemetry'] = self.telemetry
        result['OpenAgentPolicy'] = self.open_agent_policy
        result['OPALogLevel'] = self.opalog_level
        result['OPARequestCPU'] = self.oparequest_cpu
        result['OPARequestMemory'] = self.oparequest_memory
        result['OPALimitCPU'] = self.opalimit_cpu
        result['OPALimitMemory'] = self.opalimit_memory
        result['EnableAudit'] = self.enable_audit
        result['AuditProject'] = self.audit_project
        result['ProxyRequestCPU'] = self.proxy_request_cpu
        result['ProxyRequestMemory'] = self.proxy_request_memory
        result['ProxyLimitCPU'] = self.proxy_limit_cpu
        result['ProxyLimitMemory'] = self.proxy_limit_memory
        result['IncludeIPRanges'] = self.include_ipranges
        result['ExcludeIPRanges'] = self.exclude_ipranges
        result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.istio_version = map.get('IstioVersion')
        self.vpc_id = map.get('VpcId')
        self.api_server_public_eip = map.get('ApiServerPublicEip')
        self.pilot_public_eip = map.get('PilotPublicEip')
        self.tracing = map.get('Tracing')
        self.name = map.get('Name')
        self.v_switches = map.get('VSwitches')
        self.trace_sampling = map.get('TraceSampling')
        self.locality_load_balancing = map.get('LocalityLoadBalancing')
        self.telemetry = map.get('Telemetry')
        self.open_agent_policy = map.get('OpenAgentPolicy')
        self.opalog_level = map.get('OPALogLevel')
        self.oparequest_cpu = map.get('OPARequestCPU')
        self.oparequest_memory = map.get('OPARequestMemory')
        self.opalimit_cpu = map.get('OPALimitCPU')
        self.opalimit_memory = map.get('OPALimitMemory')
        self.enable_audit = map.get('EnableAudit')
        self.audit_project = map.get('AuditProject')
        self.proxy_request_cpu = map.get('ProxyRequestCPU')
        self.proxy_request_memory = map.get('ProxyRequestMemory')
        self.proxy_limit_cpu = map.get('ProxyLimitCPU')
        self.proxy_limit_memory = map.get('ProxyLimitMemory')
        self.include_ipranges = map.get('IncludeIPRanges')
        self.exclude_ipranges = map.get('ExcludeIPRanges')
        self.exclude_outbound_ports = map.get('ExcludeOutboundPorts')
        self.exclude_inbound_ports = map.get('ExcludeInboundPorts')
        return self


class CreateServiceMeshResponse(TeaModel):
    def __init__(self, request_id=None, service_mesh_id=None):
        self.request_id = request_id
        self.service_mesh_id = service_mesh_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.service_mesh_id = map.get('ServiceMeshId')
        return self


class DeleteServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, force=None):
        self.service_mesh_id = service_mesh_id
        self.force = force

    def validate(self):
        self.validate_required(self.service_mesh_id, 'service_mesh_id')

    def to_map(self):
        result = {}
        result['ServiceMeshId'] = self.service_mesh_id
        result['Force'] = self.force
        return result

    def from_map(self, map={}):
        self.service_mesh_id = map.get('ServiceMeshId')
        self.force = map.get('Force')
        return self


class DeleteServiceMeshResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self
