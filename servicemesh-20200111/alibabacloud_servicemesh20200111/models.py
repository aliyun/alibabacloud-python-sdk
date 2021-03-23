# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class RunDiagnosisRequest(TeaModel):
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


class RunDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

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


class RunDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunDiagnosisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RunDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

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


class DescribeClusterGrafanaResponseBodyDashboards(TeaModel):
    def __init__(
        self,
        url: str = None,
        title: str = None,
    ):
        self.url = url
        self.title = title

    def validate(self):
        pass

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


class DescribeClusterGrafanaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dashboards: List[DescribeClusterGrafanaResponseBodyDashboards] = None,
    ):
        self.request_id = request_id
        self.dashboards = dashboards

    def validate(self):
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
                temp_model = DescribeClusterGrafanaResponseBodyDashboards()
                self.dashboards.append(temp_model.from_map(k))
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


class DescribeGuestClusterAccessLogDashboardsRequest(TeaModel):
    def __init__(
        self,
        k_8s_cluster_id: str = None,
    ):
        self.k_8s_cluster_id = k_8s_cluster_id

    def validate(self):
        pass

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


class DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards(TeaModel):
    def __init__(
        self,
        url: str = None,
        title: str = None,
    ):
        self.url = url
        self.title = title

    def validate(self):
        pass

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


class DescribeGuestClusterAccessLogDashboardsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dashboards: List[DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards] = None,
        k_8s_cluster_id: str = None,
    ):
        self.request_id = request_id
        self.dashboards = dashboards
        self.k_8s_cluster_id = k_8s_cluster_id

    def validate(self):
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
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k in m.get('Dashboards'):
                temp_model = DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards()
                self.dashboards.append(temp_model.from_map(k))
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
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


class DescribeServiceMeshesResponseBodyServiceMeshesEndpoints(TeaModel):
    def __init__(
        self,
        intranet_pilot_endpoint: str = None,
        reverse_tunnel_endpoint: str = None,
        public_pilot_endpoint: str = None,
        intranet_api_server_endpoint: str = None,
        public_api_server_endpoint: str = None,
    ):
        self.intranet_pilot_endpoint = intranet_pilot_endpoint
        self.reverse_tunnel_endpoint = reverse_tunnel_endpoint
        self.public_pilot_endpoint = public_pilot_endpoint
        self.intranet_api_server_endpoint = intranet_api_server_endpoint
        self.public_api_server_endpoint = public_api_server_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.intranet_pilot_endpoint is not None:
            result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        if self.reverse_tunnel_endpoint is not None:
            result['ReverseTunnelEndpoint'] = self.reverse_tunnel_endpoint
        if self.public_pilot_endpoint is not None:
            result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetPilotEndpoint') is not None:
            self.intranet_pilot_endpoint = m.get('IntranetPilotEndpoint')
        if m.get('ReverseTunnelEndpoint') is not None:
            self.reverse_tunnel_endpoint = m.get('ReverseTunnelEndpoint')
        if m.get('PublicPilotEndpoint') is not None:
            self.public_pilot_endpoint = m.get('PublicPilotEndpoint')
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo(TeaModel):
    def __init__(
        self,
        profile: str = None,
        creation_time: str = None,
        update_time: str = None,
        error_message: str = None,
        version: str = None,
        state: str = None,
        service_mesh_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.profile = profile
        self.creation_time = creation_time
        self.update_time = update_time
        self.error_message = error_message
        self.version = version
        self.state = state
        self.service_mesh_id = service_mesh_id
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.version is not None:
            result['Version'] = self.version
        if self.state is not None:
            result['State'] = self.state
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        security_group_id: str = None,
        v_switches: List[str] = None,
    ):
        self.vpc_id = vpc_id
        self.security_group_id = security_group_id
        self.v_switches = v_switches

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer(TeaModel):
    def __init__(
        self,
        pilot_public_eip: bool = None,
        pilot_public_loadbalancer_id: str = None,
        api_server_loadbalancer_id: str = None,
        api_server_public_eip: bool = None,
    ):
        self.pilot_public_eip = pilot_public_eip
        self.pilot_public_loadbalancer_id = pilot_public_loadbalancer_id
        self.api_server_loadbalancer_id = api_server_loadbalancer_id
        self.api_server_public_eip = api_server_public_eip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.pilot_public_loadbalancer_id is not None:
            result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        if self.api_server_loadbalancer_id is not None:
            result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PilotPublicEip') is not None:
            self.pilot_public_eip = m.get('PilotPublicEip')
        if m.get('PilotPublicLoadbalancerId') is not None:
            self.pilot_public_loadbalancer_id = m.get('PilotPublicLoadbalancerId')
        if m.get('ApiServerLoadbalancerId') is not None:
            self.api_server_loadbalancer_id = m.get('ApiServerLoadbalancerId')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
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
        exclude_namespaces: str = None,
        enabled: bool = None,
    ):
        self.exclude_namespaces = exclude_namespaces
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.exclude_namespaces is not None:
            result['ExcludeNamespaces'] = self.exclude_namespaces
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeNamespaces') is not None:
            self.exclude_namespaces = m.get('ExcludeNamespaces')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(
        self,
        enable_namespaces_by_default: bool = None,
        auto_injection_policy_enabled: bool = None,
        init_cniconfiguration: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration = None,
    ):
        self.enable_namespaces_by_default = enable_namespaces_by_default
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.init_cniconfiguration = init_cniconfiguration

    def validate(self):
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
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(m['InitCNIConfiguration'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig(TeaModel):
    def __init__(
        self,
        telemetry: bool = None,
        outbound_traffic_policy: str = None,
        tracing: bool = None,
        strict_mtls: bool = None,
        pilot: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot = None,
        mtls: bool = None,
        sidecar_injector: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector = None,
    ):
        self.telemetry = telemetry
        self.outbound_traffic_policy = outbound_traffic_policy
        self.tracing = tracing
        self.strict_mtls = strict_mtls
        self.pilot = pilot
        self.mtls = mtls
        self.sidecar_injector = sidecar_injector

    def validate(self):
        if self.pilot:
            self.pilot.validate()
        if self.sidecar_injector:
            self.sidecar_injector.validate()

    def to_map(self):
        result = dict()
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.strict_mtls is not None:
            result['StrictMtls'] = self.strict_mtls
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        if self.mtls is not None:
            result['Mtls'] = self.mtls
        if self.sidecar_injector is not None:
            result['SidecarInjector'] = self.sidecar_injector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('StrictMtls') is not None:
            self.strict_mtls = m.get('StrictMtls')
        if m.get('Pilot') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(m['Pilot'])
        if m.get('Mtls') is not None:
            self.mtls = m.get('Mtls')
        if m.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(m['SidecarInjector'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpec(TeaModel):
    def __init__(
        self,
        network: DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork = None,
        load_balancer: DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer = None,
        mesh_config: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig = None,
    ):
        self.network = network
        self.load_balancer = load_balancer
        self.mesh_config = mesh_config

    def validate(self):
        if self.network:
            self.network.validate()
        if self.load_balancer:
            self.load_balancer.validate()
        if self.mesh_config:
            self.mesh_config.validate()

    def to_map(self):
        result = dict()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Network') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(m['LoadBalancer'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshes(TeaModel):
    def __init__(
        self,
        endpoints: DescribeServiceMeshesResponseBodyServiceMeshesEndpoints = None,
        service_mesh_info: DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo = None,
        spec: DescribeServiceMeshesResponseBodyServiceMeshesSpec = None,
        clusters: List[str] = None,
    ):
        self.endpoints = endpoints
        self.service_mesh_info = service_mesh_info
        self.spec = spec
        self.clusters = clusters

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()
        if self.service_mesh_info:
            self.service_mesh_info.validate()
        if self.spec:
            self.spec.validate()

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
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(m['ServiceMeshInfo'])
        if m.get('Spec') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
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


class GetDiagnosisRequest(TeaModel):
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


class GetDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        run_at: str = None,
        result: str = None,
    ):
        self.status = status
        self.request_id = request_id
        self.run_at = run_at
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_at is not None:
            result['RunAt'] = self.run_at
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunAt') is not None:
            self.run_at = m.get('RunAt')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDiagnosisResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

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


class GetRegisteredServicesResponseBody(TeaModel):
    def __init__(
        self,
        services: List[str] = None,
        request_id: str = None,
    ):
        self.services = services
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.services is not None:
            result['Services'] = self.services
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Services') is not None:
            self.services = m.get('Services')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRegisteredServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRegisteredServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetRegisteredServicesResponseBody()
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
        request_id: str = None,
        ingress_gateways: List[Dict[str, Any]] = None,
    ):
        self.request_id = request_id
        self.ingress_gateways = ingress_gateways

    def validate(self):
        pass

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


class DescribeServiceMeshDetailRequest(TeaModel):
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


class DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints(TeaModel):
    def __init__(
        self,
        intranet_pilot_endpoint: str = None,
        public_pilot_endpoint: str = None,
        intranet_api_server_endpoint: str = None,
        public_api_server_endpoint: str = None,
    ):
        self.intranet_pilot_endpoint = intranet_pilot_endpoint
        self.public_pilot_endpoint = public_pilot_endpoint
        self.intranet_api_server_endpoint = intranet_api_server_endpoint
        self.public_api_server_endpoint = public_api_server_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.intranet_pilot_endpoint is not None:
            result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        if self.public_pilot_endpoint is not None:
            result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntranetPilotEndpoint') is not None:
            self.intranet_pilot_endpoint = m.get('IntranetPilotEndpoint')
        if m.get('PublicPilotEndpoint') is not None:
            self.public_pilot_endpoint = m.get('PublicPilotEndpoint')
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo(TeaModel):
    def __init__(
        self,
        profile: str = None,
        creation_time: str = None,
        update_time: str = None,
        error_message: str = None,
        version: str = None,
        state: str = None,
        service_mesh_id: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.profile = profile
        self.creation_time = creation_time
        self.update_time = update_time
        self.error_message = error_message
        self.version = version
        self.state = state
        self.service_mesh_id = service_mesh_id
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.version is not None:
            result['Version'] = self.version
        if self.state is not None:
            result['State'] = self.state
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        security_group_id: str = None,
        v_switches: List[str] = None,
    ):
        self.vpc_id = vpc_id
        self.security_group_id = security_group_id
        self.v_switches = v_switches

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer(TeaModel):
    def __init__(
        self,
        pilot_public_eip: bool = None,
        pilot_public_loadbalancer_id: str = None,
        api_server_loadbalancer_id: str = None,
        api_server_public_eip: bool = None,
    ):
        self.pilot_public_eip = pilot_public_eip
        self.pilot_public_loadbalancer_id = pilot_public_loadbalancer_id
        self.api_server_loadbalancer_id = api_server_loadbalancer_id
        self.api_server_public_eip = api_server_public_eip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.pilot_public_loadbalancer_id is not None:
            result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        if self.api_server_loadbalancer_id is not None:
            result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PilotPublicEip') is not None:
            self.pilot_public_eip = m.get('PilotPublicEip')
        if m.get('PilotPublicLoadbalancerId') is not None:
            self.pilot_public_loadbalancer_id = m.get('PilotPublicLoadbalancerId')
        if m.get('ApiServerLoadbalancerId') is not None:
            self.api_server_loadbalancer_id = m.get('ApiServerLoadbalancerId')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA(TeaModel):
    def __init__(
        self,
        request_memory: str = None,
        log_level: str = None,
        enabled: bool = None,
        limit_memory: str = None,
        request_cpu: str = None,
        limit_cpu: str = None,
    ):
        self.request_memory = request_memory
        self.log_level = log_level
        self.enabled = enabled
        self.limit_memory = limit_memory
        self.request_cpu = request_cpu
        self.limit_cpu = limit_cpu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus(TeaModel):
    def __init__(
        self,
        use_external: bool = None,
        external_url: str = None,
    ):
        self.use_external = use_external
        self.external_url = external_url

    def validate(self):
        pass

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


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

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


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot(TeaModel):
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


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

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


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(
        self,
        exclude_namespaces: str = None,
        enabled: bool = None,
    ):
        self.exclude_namespaces = exclude_namespaces
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.exclude_namespaces is not None:
            result['ExcludeNamespaces'] = self.exclude_namespaces
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeNamespaces') is not None:
            self.exclude_namespaces = m.get('ExcludeNamespaces')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(
        self,
        enable_namespaces_by_default: bool = None,
        request_memory: str = None,
        limit_memory: str = None,
        request_cpu: str = None,
        auto_injection_policy_enabled: bool = None,
        limit_cpu: str = None,
        init_cniconfiguration: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration = None,
        sidecar_injector_webhook_as_yaml: str = None,
    ):
        self.enable_namespaces_by_default = enable_namespaces_by_default
        self.request_memory = request_memory
        self.limit_memory = limit_memory
        self.request_cpu = request_cpu
        self.auto_injection_policy_enabled = auto_injection_policy_enabled
        self.limit_cpu = limit_cpu
        self.init_cniconfiguration = init_cniconfiguration
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml

    def validate(self):
        if self.init_cniconfiguration:
            self.init_cniconfiguration.validate()

    def to_map(self):
        result = dict()
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.init_cniconfiguration is not None:
            result['InitCNIConfiguration'] = self.init_cniconfiguration.to_map()
        if self.sidecar_injector_webhook_as_yaml is not None:
            result['SidecarInjectorWebhookAsYaml'] = self.sidecar_injector_webhook_as_yaml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(m['InitCNIConfiguration'])
        if m.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = m.get('SidecarInjectorWebhookAsYaml')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport(TeaModel):
    def __init__(
        self,
        mysql_filter_enabled: bool = None,
        redis_filter_enabled: bool = None,
        thrift_filter_enabled: bool = None,
    ):
        self.mysql_filter_enabled = mysql_filter_enabled
        self.redis_filter_enabled = redis_filter_enabled
        self.thrift_filter_enabled = thrift_filter_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
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


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

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


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit(TeaModel):
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


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy(TeaModel):
    def __init__(
        self,
        request_memory: str = None,
        cluster_domain: str = None,
        limit_memory: str = None,
        request_cpu: str = None,
        enable_dnsproxying: bool = None,
        limit_cpu: str = None,
    ):
        self.request_memory = request_memory
        self.cluster_domain = cluster_domain
        self.limit_memory = limit_memory
        self.request_cpu = request_cpu
        self.enable_dnsproxying = enable_dnsproxying
        self.limit_cpu = limit_cpu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.enable_dnsproxying is not None:
            result['EnableDNSProxying'] = self.enable_dnsproxying
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('EnableDNSProxying') is not None:
            self.enable_dnsproxying = m.get('EnableDNSProxying')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig(TeaModel):
    def __init__(
        self,
        opa: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA = None,
        prometheus: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus = None,
        access_log: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog = None,
        pilot: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot = None,
        mse: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE = None,
        customized_zipkin: bool = None,
        sidecar_injector: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector = None,
        include_ipranges: str = None,
        telemetry: bool = None,
        edition: str = None,
        protocol_support: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport = None,
        outbound_traffic_policy: str = None,
        kiali: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali = None,
        tracing: bool = None,
        web_assembly_filter_deployment: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment = None,
        enable_locality_lb: bool = None,
        audit: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit = None,
        proxy: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy = None,
    ):
        self.opa = opa
        self.prometheus = prometheus
        self.access_log = access_log
        self.pilot = pilot
        self.mse = mse
        self.customized_zipkin = customized_zipkin
        self.sidecar_injector = sidecar_injector
        self.include_ipranges = include_ipranges
        self.telemetry = telemetry
        self.edition = edition
        self.protocol_support = protocol_support
        self.outbound_traffic_policy = outbound_traffic_policy
        self.kiali = kiali
        self.tracing = tracing
        self.web_assembly_filter_deployment = web_assembly_filter_deployment
        self.enable_locality_lb = enable_locality_lb
        self.audit = audit
        self.proxy = proxy

    def validate(self):
        if self.opa:
            self.opa.validate()
        if self.prometheus:
            self.prometheus.validate()
        if self.access_log:
            self.access_log.validate()
        if self.pilot:
            self.pilot.validate()
        if self.mse:
            self.mse.validate()
        if self.sidecar_injector:
            self.sidecar_injector.validate()
        if self.protocol_support:
            self.protocol_support.validate()
        if self.kiali:
            self.kiali.validate()
        if self.web_assembly_filter_deployment:
            self.web_assembly_filter_deployment.validate()
        if self.audit:
            self.audit.validate()
        if self.proxy:
            self.proxy.validate()

    def to_map(self):
        result = dict()
        if self.opa is not None:
            result['OPA'] = self.opa.to_map()
        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus.to_map()
        if self.access_log is not None:
            result['AccessLog'] = self.access_log.to_map()
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        if self.mse is not None:
            result['MSE'] = self.mse.to_map()
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.sidecar_injector is not None:
            result['SidecarInjector'] = self.sidecar_injector.to_map()
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.protocol_support is not None:
            result['ProtocolSupport'] = self.protocol_support.to_map()
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.kiali is not None:
            result['Kiali'] = self.kiali.to_map()
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.web_assembly_filter_deployment is not None:
            result['WebAssemblyFilterDeployment'] = self.web_assembly_filter_deployment.to_map()
        if self.enable_locality_lb is not None:
            result['EnableLocalityLB'] = self.enable_locality_lb
        if self.audit is not None:
            result['Audit'] = self.audit.to_map()
        if self.proxy is not None:
            result['Proxy'] = self.proxy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OPA') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA()
            self.opa = temp_model.from_map(m['OPA'])
        if m.get('Prometheus') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus()
            self.prometheus = temp_model.from_map(m['Prometheus'])
        if m.get('AccessLog') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog()
            self.access_log = temp_model.from_map(m['AccessLog'])
        if m.get('Pilot') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(m['Pilot'])
        if m.get('MSE') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE()
            self.mse = temp_model.from_map(m['MSE'])
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(m['SidecarInjector'])
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('ProtocolSupport') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport()
            self.protocol_support = temp_model.from_map(m['ProtocolSupport'])
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('Kiali') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali()
            self.kiali = temp_model.from_map(m['Kiali'])
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('WebAssemblyFilterDeployment') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment()
            self.web_assembly_filter_deployment = temp_model.from_map(m['WebAssemblyFilterDeployment'])
        if m.get('EnableLocalityLB') is not None:
            self.enable_locality_lb = m.get('EnableLocalityLB')
        if m.get('Audit') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit()
            self.audit = temp_model.from_map(m['Audit'])
        if m.get('Proxy') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy()
            self.proxy = temp_model.from_map(m['Proxy'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpec(TeaModel):
    def __init__(
        self,
        network: DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork = None,
        load_balancer: DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer = None,
        mesh_config: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig = None,
    ):
        self.network = network
        self.load_balancer = load_balancer
        self.mesh_config = mesh_config

    def validate(self):
        if self.network:
            self.network.validate()
        if self.load_balancer:
            self.load_balancer.validate()
        if self.mesh_config:
            self.mesh_config.validate()

    def to_map(self):
        result = dict()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Network') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(m['LoadBalancer'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMesh(TeaModel):
    def __init__(
        self,
        endpoints: DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints = None,
        service_mesh_info: DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo = None,
        spec: DescribeServiceMeshDetailResponseBodyServiceMeshSpec = None,
        clusters: List[str] = None,
    ):
        self.endpoints = endpoints
        self.service_mesh_info = service_mesh_info
        self.spec = spec
        self.clusters = clusters

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()
        if self.service_mesh_info:
            self.service_mesh_info.validate()
        if self.spec:
            self.spec.validate()

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
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(m['ServiceMeshInfo'])
        if m.get('Spec') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
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


class DescribeCensResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        clusters: List[str] = None,
    ):
        self.request_id = request_id
        self.clusters = clusters

    def validate(self):
        pass

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


class DeleteServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        force: bool = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.force = force

    def validate(self):
        pass

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


class DeleteServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

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


class UpgradeMeshVersionRequest(TeaModel):
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


class UpgradeMeshVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

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


class DescribeServiceMeshKubeconfigRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        private_ip_address: bool = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

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


class DescribeServiceMeshKubeconfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        kubeconfig: str = None,
    ):
        self.request_id = request_id
        self.kubeconfig = kubeconfig

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.kubeconfig is not None:
            result['Kubeconfig'] = self.kubeconfig
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Kubeconfig') is not None:
            self.kubeconfig = m.get('Kubeconfig')
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


class GetVmAppMeshInfoRequest(TeaModel):
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


class GetVmAppMeshInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

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


class RemoveClusterFromServiceMeshRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        cluster_id: str = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.cluster_id = cluster_id

    def validate(self):
        pass

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


class RemoveClusterFromServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
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


class SetServiceRegistrySourceRequest(TeaModel):
    def __init__(
        self,
        service_mesh_id: str = None,
        config: Dict[str, Any] = None,
    ):
        self.service_mesh_id = service_mesh_id
        self.config = config

    def validate(self):
        pass

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
        pass

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


class SetServiceRegistrySourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

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


class SetServiceRegistrySourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetServiceRegistrySourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SetServiceRegistrySourceResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

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


class AddClusterIntoServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
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


class GetServiceMeshSlbRequest(TeaModel):
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


class GetServiceMeshSlbResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        server_health_status: str = None,
        load_balancer_id: str = None,
    ):
        self.status = status
        self.server_health_status = server_health_status
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.server_health_status is not None:
            result['ServerHealthStatus'] = self.server_health_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ServerHealthStatus') is not None:
            self.server_health_status = m.get('ServerHealthStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class GetServiceMeshSlbResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[GetServiceMeshSlbResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
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
                temp_model = GetServiceMeshSlbResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetServiceMeshSlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceMeshSlbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetServiceMeshSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

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
        service_endpoints: List[GetRegisteredServiceEndpointsResponseBodyServiceEndpoints] = None,
        request_id: str = None,
    ):
        self.service_endpoints = service_endpoints
        self.request_id = request_id

    def validate(self):
        if self.service_endpoints:
            for k in self.service_endpoints:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ServiceEndpoints'] = []
        if self.service_endpoints is not None:
            for k in self.service_endpoints:
                result['ServiceEndpoints'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_endpoints = []
        if m.get('ServiceEndpoints') is not None:
            for k in m.get('ServiceEndpoints'):
                temp_model = GetRegisteredServiceEndpointsResponseBodyServiceEndpoints()
                self.service_endpoints.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        mseenabled: bool = None,
        redis_filter_enabled: bool = None,
        mysql_filter_enabled: bool = None,
        thrift_filter_enabled: bool = None,
        web_assembly_filter_enabled: bool = None,
        dnsproxying_enabled: bool = None,
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
        self.mseenabled = mseenabled
        self.redis_filter_enabled = redis_filter_enabled
        self.mysql_filter_enabled = mysql_filter_enabled
        self.thrift_filter_enabled = thrift_filter_enabled
        self.web_assembly_filter_enabled = web_assembly_filter_enabled
        self.dnsproxying_enabled = dnsproxying_enabled

    def validate(self):
        pass

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
        if self.mseenabled is not None:
            result['MSEEnabled'] = self.mseenabled
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        if self.web_assembly_filter_enabled is not None:
            result['WebAssemblyFilterEnabled'] = self.web_assembly_filter_enabled
        if self.dnsproxying_enabled is not None:
            result['DNSProxyingEnabled'] = self.dnsproxying_enabled
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
        if m.get('MSEEnabled') is not None:
            self.mseenabled = m.get('MSEEnabled')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        if m.get('WebAssemblyFilterEnabled') is not None:
            self.web_assembly_filter_enabled = m.get('WebAssemblyFilterEnabled')
        if m.get('DNSProxyingEnabled') is not None:
            self.dnsproxying_enabled = m.get('DNSProxyingEnabled')
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
        pass

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


class AddVmAppToMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

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


class AddVmAppToMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddVmAppToMeshResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AddVmAppToMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        redis_filter_enabled: bool = None,
        mysql_filter_enabled: bool = None,
        thrift_filter_enabled: bool = None,
        web_assembly_filter_enabled: bool = None,
        mseenabled: bool = None,
        dnsproxying_enabled: bool = None,
        edition: str = None,
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
        self.redis_filter_enabled = redis_filter_enabled
        self.mysql_filter_enabled = mysql_filter_enabled
        self.thrift_filter_enabled = thrift_filter_enabled
        self.web_assembly_filter_enabled = web_assembly_filter_enabled
        self.mseenabled = mseenabled
        self.dnsproxying_enabled = dnsproxying_enabled
        self.edition = edition

    def validate(self):
        pass

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
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        if self.web_assembly_filter_enabled is not None:
            result['WebAssemblyFilterEnabled'] = self.web_assembly_filter_enabled
        if self.mseenabled is not None:
            result['MSEEnabled'] = self.mseenabled
        if self.dnsproxying_enabled is not None:
            result['DNSProxyingEnabled'] = self.dnsproxying_enabled
        if self.edition is not None:
            result['Edition'] = self.edition
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
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        if m.get('WebAssemblyFilterEnabled') is not None:
            self.web_assembly_filter_enabled = m.get('WebAssemblyFilterEnabled')
        if m.get('MSEEnabled') is not None:
            self.mseenabled = m.get('MSEEnabled')
        if m.get('DNSProxyingEnabled') is not None:
            self.dnsproxying_enabled = m.get('DNSProxyingEnabled')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
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


class GetAutoInjectionLabelSyncStatusRequest(TeaModel):
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


class GetAutoInjectionLabelSyncStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
    ):
        self.status = status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAutoInjectionLabelSyncStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutoInjectionLabelSyncStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetAutoInjectionLabelSyncStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRegistrySourceRequest(TeaModel):
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


class GetServiceRegistrySourceResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        result: str = None,
    ):
        self.status = status
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetServiceRegistrySourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceRegistrySourceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetServiceRegistrySourceResponseBody()
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


class InitializeASMRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

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


class InitializeASMRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitializeASMRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = InitializeASMRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

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


class RemoveVmAppFromMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

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


class RemoveVmAppFromMeshResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveVmAppFromMeshResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = RemoveVmAppFromMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
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


class DescribeClusterPrometheusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prometheus: str = None,
    ):
        self.request_id = request_id
        self.prometheus = prometheus

    def validate(self):
        pass

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
        pass

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


class UpdateIstioInjectionConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

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


class UpdateIstioInjectionConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateIstioInjectionConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateIstioInjectionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

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


class GetVmMetaResponseBodyVmMetaInfo(TeaModel):
    def __init__(
        self,
        token_path: str = None,
        hosts_content: str = None,
        envoy_env_path: str = None,
        token_content: str = None,
        cert_chain_path: str = None,
        root_cert_content: str = None,
        key_content: str = None,
        root_cert_path: str = None,
        cert_chain_content: str = None,
        hosts_path: str = None,
        key_path: str = None,
        envoy_env_content: str = None,
    ):
        self.token_path = token_path
        self.hosts_content = hosts_content
        self.envoy_env_path = envoy_env_path
        self.token_content = token_content
        self.cert_chain_path = cert_chain_path
        self.root_cert_content = root_cert_content
        self.key_content = key_content
        self.root_cert_path = root_cert_path
        self.cert_chain_content = cert_chain_content
        self.hosts_path = hosts_path
        self.key_path = key_path
        self.envoy_env_content = envoy_env_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.token_path is not None:
            result['TokenPath'] = self.token_path
        if self.hosts_content is not None:
            result['HostsContent'] = self.hosts_content
        if self.envoy_env_path is not None:
            result['EnvoyEnvPath'] = self.envoy_env_path
        if self.token_content is not None:
            result['TokenContent'] = self.token_content
        if self.cert_chain_path is not None:
            result['CertChainPath'] = self.cert_chain_path
        if self.root_cert_content is not None:
            result['RootCertContent'] = self.root_cert_content
        if self.key_content is not None:
            result['KeyContent'] = self.key_content
        if self.root_cert_path is not None:
            result['RootCertPath'] = self.root_cert_path
        if self.cert_chain_content is not None:
            result['CertChainContent'] = self.cert_chain_content
        if self.hosts_path is not None:
            result['HostsPath'] = self.hosts_path
        if self.key_path is not None:
            result['KeyPath'] = self.key_path
        if self.envoy_env_content is not None:
            result['EnvoyEnvContent'] = self.envoy_env_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TokenPath') is not None:
            self.token_path = m.get('TokenPath')
        if m.get('HostsContent') is not None:
            self.hosts_content = m.get('HostsContent')
        if m.get('EnvoyEnvPath') is not None:
            self.envoy_env_path = m.get('EnvoyEnvPath')
        if m.get('TokenContent') is not None:
            self.token_content = m.get('TokenContent')
        if m.get('CertChainPath') is not None:
            self.cert_chain_path = m.get('CertChainPath')
        if m.get('RootCertContent') is not None:
            self.root_cert_content = m.get('RootCertContent')
        if m.get('KeyContent') is not None:
            self.key_content = m.get('KeyContent')
        if m.get('RootCertPath') is not None:
            self.root_cert_path = m.get('RootCertPath')
        if m.get('CertChainContent') is not None:
            self.cert_chain_content = m.get('CertChainContent')
        if m.get('HostsPath') is not None:
            self.hosts_path = m.get('HostsPath')
        if m.get('KeyPath') is not None:
            self.key_path = m.get('KeyPath')
        if m.get('EnvoyEnvContent') is not None:
            self.envoy_env_content = m.get('EnvoyEnvContent')
        return self


class GetVmMetaResponseBody(TeaModel):
    def __init__(
        self,
        vm_meta_info: GetVmMetaResponseBodyVmMetaInfo = None,
        request_id: str = None,
    ):
        self.vm_meta_info = vm_meta_info
        self.request_id = request_id

    def validate(self):
        if self.vm_meta_info:
            self.vm_meta_info.validate()

    def to_map(self):
        result = dict()
        if self.vm_meta_info is not None:
            result['VmMetaInfo'] = self.vm_meta_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VmMetaInfo') is not None:
            temp_model = GetVmMetaResponseBodyVmMetaInfo()
            self.vm_meta_info = temp_model.from_map(m['VmMetaInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeUpgradeVersionRequest(TeaModel):
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


class DescribeUpgradeVersionResponseBodyVersion(TeaModel):
    def __init__(
        self,
        kubernetes_version: str = None,
        istio_operator_version: str = None,
        istio_version: str = None,
    ):
        self.kubernetes_version = kubernetes_version
        self.istio_operator_version = istio_operator_version
        self.istio_version = istio_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version
        if self.istio_operator_version is not None:
            result['IstioOperatorVersion'] = self.istio_operator_version
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')
        if m.get('IstioOperatorVersion') is not None:
            self.istio_operator_version = m.get('IstioOperatorVersion')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
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


class DescribeClustersInServiceMeshRequest(TeaModel):
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


class DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards(TeaModel):
    def __init__(
        self,
        url: str = None,
        title: str = None,
    ):
        self.url = url
        self.title = title

    def validate(self):
        pass

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


class DescribeClustersInServiceMeshResponseBodyClusters(TeaModel):
    def __init__(
        self,
        sg_id: str = None,
        vpc_id: str = None,
        creation_time: str = None,
        update_time: str = None,
        error_message: str = None,
        state: str = None,
        access_log_dashboards: List[DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards] = None,
        region_id: str = None,
        cluster_domain: str = None,
        version: str = None,
        cluster_type: str = None,
        name: str = None,
        cluster_id: str = None,
    ):
        self.sg_id = sg_id
        self.vpc_id = vpc_id
        self.creation_time = creation_time
        self.update_time = update_time
        self.error_message = error_message
        self.state = state
        self.access_log_dashboards = access_log_dashboards
        self.region_id = region_id
        self.cluster_domain = cluster_domain
        self.version = version
        self.cluster_type = cluster_type
        self.name = name
        self.cluster_id = cluster_id

    def validate(self):
        if self.access_log_dashboards:
            for k in self.access_log_dashboards:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.state is not None:
            result['State'] = self.state
        result['AccessLogDashboards'] = []
        if self.access_log_dashboards is not None:
            for k in self.access_log_dashboards:
                result['AccessLogDashboards'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.version is not None:
            result['Version'] = self.version
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.name is not None:
            result['Name'] = self.name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.access_log_dashboards = []
        if m.get('AccessLogDashboards') is not None:
            for k in m.get('AccessLogDashboards'):
                temp_model = DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards()
                self.access_log_dashboards.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClustersInServiceMeshResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        clusters: List[DescribeClustersInServiceMeshResponseBodyClusters] = None,
    ):
        self.request_id = request_id
        self.clusters = clusters

    def validate(self):
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
                temp_model = DescribeClustersInServiceMeshResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
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


