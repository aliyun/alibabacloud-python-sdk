# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_servicemesh20200111 import models as servicemesh_20200111_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('servicemesh', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_cluster_into_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        """
        @summary Adds a cluster to an ASM instance.
        
        @param request: AddClusterIntoServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddClusterIntoServiceMeshResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.discovery_only):
            body['DiscoveryOnly'] = request.discovery_only
        if not UtilClient.is_unset(request.ignore_namespace_check):
            body['IgnoreNamespaceCheck'] = request.ignore_namespace_check
        if not UtilClient.is_unset(request.kubeconfig):
            body['Kubeconfig'] = request.kubeconfig
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddClusterIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddClusterIntoServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cluster_into_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        """
        @summary Adds a cluster to an ASM instance.
        
        @param request: AddClusterIntoServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddClusterIntoServiceMeshResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.discovery_only):
            body['DiscoveryOnly'] = request.discovery_only
        if not UtilClient.is_unset(request.ignore_namespace_check):
            body['IgnoreNamespaceCheck'] = request.ignore_namespace_check
        if not UtilClient.is_unset(request.kubeconfig):
            body['Kubeconfig'] = request.kubeconfig
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddClusterIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddClusterIntoServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cluster_into_service_mesh(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        """
        @summary Adds a cluster to an ASM instance.
        
        @param request: AddClusterIntoServiceMeshRequest
        @return: AddClusterIntoServiceMeshResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_cluster_into_service_mesh_with_options(request, runtime)

    async def add_cluster_into_service_mesh_async(
        self,
        request: servicemesh_20200111_models.AddClusterIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddClusterIntoServiceMeshResponse:
        """
        @summary Adds a cluster to an ASM instance.
        
        @param request: AddClusterIntoServiceMeshRequest
        @return: AddClusterIntoServiceMeshResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_cluster_into_service_mesh_with_options_async(request, runtime)

    def add_vminto_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        """
        @deprecated OpenAPI AddVMIntoServiceMesh is deprecated
        
        @summary Adds a virtual machine (VM) to a Service Mesh (ASM) instance.
        
        @param request: AddVMIntoServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddVMIntoServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVMIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddVMIntoServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_vminto_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        """
        @deprecated OpenAPI AddVMIntoServiceMesh is deprecated
        
        @summary Adds a virtual machine (VM) to a Service Mesh (ASM) instance.
        
        @param request: AddVMIntoServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddVMIntoServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVMIntoServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddVMIntoServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_vminto_service_mesh(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        """
        @deprecated OpenAPI AddVMIntoServiceMesh is deprecated
        
        @summary Adds a virtual machine (VM) to a Service Mesh (ASM) instance.
        
        @param request: AddVMIntoServiceMeshRequest
        @return: AddVMIntoServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.add_vminto_service_mesh_with_options(request, runtime)

    async def add_vminto_service_mesh_async(
        self,
        request: servicemesh_20200111_models.AddVMIntoServiceMeshRequest,
    ) -> servicemesh_20200111_models.AddVMIntoServiceMeshResponse:
        """
        @deprecated OpenAPI AddVMIntoServiceMesh is deprecated
        
        @summary Adds a virtual machine (VM) to a Service Mesh (ASM) instance.
        
        @param request: AddVMIntoServiceMeshRequest
        @return: AddVMIntoServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_vminto_service_mesh_with_options_async(request, runtime)

    def create_asmgateway_with_options(
        self,
        request: servicemesh_20200111_models.CreateASMGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateASMGatewayResponse:
        """
        @summary Creates a Service Mesh (ASM) gateway.
        
        @param request: CreateASMGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateASMGatewayResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateASMGateway',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateASMGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_asmgateway_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateASMGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateASMGatewayResponse:
        """
        @summary Creates a Service Mesh (ASM) gateway.
        
        @param request: CreateASMGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateASMGatewayResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateASMGateway',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateASMGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_asmgateway(
        self,
        request: servicemesh_20200111_models.CreateASMGatewayRequest,
    ) -> servicemesh_20200111_models.CreateASMGatewayResponse:
        """
        @summary Creates a Service Mesh (ASM) gateway.
        
        @param request: CreateASMGatewayRequest
        @return: CreateASMGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_asmgateway_with_options(request, runtime)

    async def create_asmgateway_async(
        self,
        request: servicemesh_20200111_models.CreateASMGatewayRequest,
    ) -> servicemesh_20200111_models.CreateASMGatewayResponse:
        """
        @summary Creates a Service Mesh (ASM) gateway.
        
        @param request: CreateASMGatewayRequest
        @return: CreateASMGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_asmgateway_with_options_async(request, runtime)

    def create_gateway_secret_with_options(
        self,
        request: servicemesh_20200111_models.CreateGatewaySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateGatewaySecretResponse:
        """
        @summary Creates a secret for a Service Mesh (ASM) gateway.
        
        @param request: CreateGatewaySecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewaySecretResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert):
            body['Cert'] = request.cert
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.secret_name):
            body['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewaySecret',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateGatewaySecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gateway_secret_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateGatewaySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateGatewaySecretResponse:
        """
        @summary Creates a secret for a Service Mesh (ASM) gateway.
        
        @param request: CreateGatewaySecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGatewaySecretResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cert):
            body['Cert'] = request.cert
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.secret_name):
            body['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGatewaySecret',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateGatewaySecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gateway_secret(
        self,
        request: servicemesh_20200111_models.CreateGatewaySecretRequest,
    ) -> servicemesh_20200111_models.CreateGatewaySecretResponse:
        """
        @summary Creates a secret for a Service Mesh (ASM) gateway.
        
        @param request: CreateGatewaySecretRequest
        @return: CreateGatewaySecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_gateway_secret_with_options(request, runtime)

    async def create_gateway_secret_async(
        self,
        request: servicemesh_20200111_models.CreateGatewaySecretRequest,
    ) -> servicemesh_20200111_models.CreateGatewaySecretResponse:
        """
        @summary Creates a secret for a Service Mesh (ASM) gateway.
        
        @param request: CreateGatewaySecretRequest
        @return: CreateGatewaySecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_gateway_secret_with_options_async(request, runtime)

    def create_istio_gateway_domains_with_options(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateIstioGatewayDomainsResponse:
        """
        @summary Adds domain names for a Service Mesh (ASM) gateway.
        
        @param request: CreateIstioGatewayDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIstioGatewayDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.credential):
            body['Credential'] = request.credential
        if not UtilClient.is_unset(request.force_https):
            body['ForceHttps'] = request.force_https
        if not UtilClient.is_unset(request.hosts):
            body['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.number):
            body['Number'] = request.number
        if not UtilClient.is_unset(request.port_name):
            body['PortName'] = request.port_name
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateIstioGatewayDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_istio_gateway_domains_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateIstioGatewayDomainsResponse:
        """
        @summary Adds domain names for a Service Mesh (ASM) gateway.
        
        @param request: CreateIstioGatewayDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIstioGatewayDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.credential):
            body['Credential'] = request.credential
        if not UtilClient.is_unset(request.force_https):
            body['ForceHttps'] = request.force_https
        if not UtilClient.is_unset(request.hosts):
            body['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.number):
            body['Number'] = request.number
        if not UtilClient.is_unset(request.port_name):
            body['PortName'] = request.port_name
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateIstioGatewayDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_istio_gateway_domains(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.CreateIstioGatewayDomainsResponse:
        """
        @summary Adds domain names for a Service Mesh (ASM) gateway.
        
        @param request: CreateIstioGatewayDomainsRequest
        @return: CreateIstioGatewayDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_istio_gateway_domains_with_options(request, runtime)

    async def create_istio_gateway_domains_async(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.CreateIstioGatewayDomainsResponse:
        """
        @summary Adds domain names for a Service Mesh (ASM) gateway.
        
        @param request: CreateIstioGatewayDomainsRequest
        @return: CreateIstioGatewayDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_istio_gateway_domains_with_options_async(request, runtime)

    def create_istio_gateway_routes_with_options(
        self,
        tmp_req: servicemesh_20200111_models.CreateIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateIstioGatewayRoutesResponse:
        """
        @summary Creates a routing rule for a Service Mesh (ASM) gateway.
        
        @param tmp_req: CreateIstioGatewayRoutesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIstioGatewayRoutesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.CreateIstioGatewayRoutesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_route):
            request.gateway_route_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_route, 'GatewayRoute', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_route_shrink):
            body['GatewayRoute'] = request.gateway_route_shrink
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateIstioGatewayRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_istio_gateway_routes_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.CreateIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateIstioGatewayRoutesResponse:
        """
        @summary Creates a routing rule for a Service Mesh (ASM) gateway.
        
        @param tmp_req: CreateIstioGatewayRoutesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIstioGatewayRoutesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.CreateIstioGatewayRoutesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_route):
            request.gateway_route_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_route, 'GatewayRoute', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_route_shrink):
            body['GatewayRoute'] = request.gateway_route_shrink
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateIstioGatewayRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_istio_gateway_routes(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.CreateIstioGatewayRoutesResponse:
        """
        @summary Creates a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: CreateIstioGatewayRoutesRequest
        @return: CreateIstioGatewayRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_istio_gateway_routes_with_options(request, runtime)

    async def create_istio_gateway_routes_async(
        self,
        request: servicemesh_20200111_models.CreateIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.CreateIstioGatewayRoutesResponse:
        """
        @summary Creates a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: CreateIstioGatewayRoutesRequest
        @return: CreateIstioGatewayRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_istio_gateway_routes_with_options_async(request, runtime)

    def create_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        """
        @summary Creates a Service Mesh (ASM) instance.
        
        @param request: CreateServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceMeshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.api_server_load_balancer_spec):
            body['ApiServerLoadBalancerSpec'] = request.api_server_load_balancer_spec
        if not UtilClient.is_unset(request.api_server_public_eip):
            body['ApiServerPublicEip'] = request.api_server_public_eip
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.cert_chain):
            body['CertChain'] = request.cert_chain
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cluster_domain):
            body['ClusterDomain'] = request.cluster_domain
        if not UtilClient.is_unset(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.control_plane_log_enabled):
            body['ControlPlaneLogEnabled'] = request.control_plane_log_enabled
        if not UtilClient.is_unset(request.control_plane_log_project):
            body['ControlPlaneLogProject'] = request.control_plane_log_project
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.edition):
            body['Edition'] = request.edition
        if not UtilClient.is_unset(request.enable_acmg):
            body['EnableACMG'] = request.enable_acmg
        if not UtilClient.is_unset(request.enable_ambient):
            body['EnableAmbient'] = request.enable_ambient
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.existing_ca_cert):
            body['ExistingCaCert'] = request.existing_ca_cert
        if not UtilClient.is_unset(request.existing_ca_key):
            body['ExistingCaKey'] = request.existing_ca_key
        if not UtilClient.is_unset(request.existing_ca_type):
            body['ExistingCaType'] = request.existing_ca_type
        if not UtilClient.is_unset(request.existing_root_ca_cert):
            body['ExistingRootCaCert'] = request.existing_root_ca_cert
        if not UtilClient.is_unset(request.existing_root_ca_key):
            body['ExistingRootCaKey'] = request.existing_root_ca_key
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.guest_cluster):
            body['GuestCluster'] = request.guest_cluster
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.multi_buffer_enabled):
            body['MultiBufferEnabled'] = request.multi_buffer_enabled
        if not UtilClient.is_unset(request.multi_buffer_poll_delay):
            body['MultiBufferPollDelay'] = request.multi_buffer_poll_delay
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.pilot_load_balancer_spec):
            body['PilotLoadBalancerSpec'] = request.pilot_load_balancer_spec
        if not UtilClient.is_unset(request.playground_scene):
            body['PlaygroundScene'] = request.playground_scene
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.use_existing_ca):
            body['UseExistingCA'] = request.use_existing_ca
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        """
        @summary Creates a Service Mesh (ASM) instance.
        
        @param request: CreateServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceMeshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.api_server_load_balancer_spec):
            body['ApiServerLoadBalancerSpec'] = request.api_server_load_balancer_spec
        if not UtilClient.is_unset(request.api_server_public_eip):
            body['ApiServerPublicEip'] = request.api_server_public_eip
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.auto_renew):
            body['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            body['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.cert_chain):
            body['CertChain'] = request.cert_chain
        if not UtilClient.is_unset(request.charge_type):
            body['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.cluster_domain):
            body['ClusterDomain'] = request.cluster_domain
        if not UtilClient.is_unset(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.control_plane_log_enabled):
            body['ControlPlaneLogEnabled'] = request.control_plane_log_enabled
        if not UtilClient.is_unset(request.control_plane_log_project):
            body['ControlPlaneLogProject'] = request.control_plane_log_project
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.edition):
            body['Edition'] = request.edition
        if not UtilClient.is_unset(request.enable_acmg):
            body['EnableACMG'] = request.enable_acmg
        if not UtilClient.is_unset(request.enable_ambient):
            body['EnableAmbient'] = request.enable_ambient
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.existing_ca_cert):
            body['ExistingCaCert'] = request.existing_ca_cert
        if not UtilClient.is_unset(request.existing_ca_key):
            body['ExistingCaKey'] = request.existing_ca_key
        if not UtilClient.is_unset(request.existing_ca_type):
            body['ExistingCaType'] = request.existing_ca_type
        if not UtilClient.is_unset(request.existing_root_ca_cert):
            body['ExistingRootCaCert'] = request.existing_root_ca_cert
        if not UtilClient.is_unset(request.existing_root_ca_key):
            body['ExistingRootCaKey'] = request.existing_root_ca_key
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.guest_cluster):
            body['GuestCluster'] = request.guest_cluster
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.multi_buffer_enabled):
            body['MultiBufferEnabled'] = request.multi_buffer_enabled
        if not UtilClient.is_unset(request.multi_buffer_poll_delay):
            body['MultiBufferPollDelay'] = request.multi_buffer_poll_delay
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.period):
            body['Period'] = request.period
        if not UtilClient.is_unset(request.pilot_load_balancer_spec):
            body['PilotLoadBalancerSpec'] = request.pilot_load_balancer_spec
        if not UtilClient.is_unset(request.playground_scene):
            body['PlaygroundScene'] = request.playground_scene
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.use_existing_ca):
            body['UseExistingCA'] = request.use_existing_ca
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_mesh(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        """
        @summary Creates a Service Mesh (ASM) instance.
        
        @param request: CreateServiceMeshRequest
        @return: CreateServiceMeshResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_mesh_with_options(request, runtime)

    async def create_service_mesh_async(
        self,
        request: servicemesh_20200111_models.CreateServiceMeshRequest,
    ) -> servicemesh_20200111_models.CreateServiceMeshResponse:
        """
        @summary Creates a Service Mesh (ASM) instance.
        
        @param request: CreateServiceMeshRequest
        @return: CreateServiceMeshResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_mesh_with_options_async(request, runtime)

    def create_swim_lane_with_options(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateSwimLaneResponse:
        """
        @summary Creates a lane.
        
        @param request: CreateSwimLaneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSwimLaneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.label_selector_key):
            body['LabelSelectorKey'] = request.label_selector_key
        if not UtilClient.is_unset(request.label_selector_value):
            body['LabelSelectorValue'] = request.label_selector_value
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateSwimLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_swim_lane_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateSwimLaneResponse:
        """
        @summary Creates a lane.
        
        @param request: CreateSwimLaneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSwimLaneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.label_selector_key):
            body['LabelSelectorKey'] = request.label_selector_key
        if not UtilClient.is_unset(request.label_selector_value):
            body['LabelSelectorValue'] = request.label_selector_value
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateSwimLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_swim_lane(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneRequest,
    ) -> servicemesh_20200111_models.CreateSwimLaneResponse:
        """
        @summary Creates a lane.
        
        @param request: CreateSwimLaneRequest
        @return: CreateSwimLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_swim_lane_with_options(request, runtime)

    async def create_swim_lane_async(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneRequest,
    ) -> servicemesh_20200111_models.CreateSwimLaneResponse:
        """
        @summary Creates a lane.
        
        @param request: CreateSwimLaneRequest
        @return: CreateSwimLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_swim_lane_with_options_async(request, runtime)

    def create_swim_lane_group_with_options(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateSwimLaneGroupResponse:
        """
        @summary Creates a lane group.
        
        @param request: CreateSwimLaneGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSwimLaneGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ingress_gateway_name):
            body['IngressGatewayName'] = request.ingress_gateway_name
        if not UtilClient.is_unset(request.ingress_gateway_namespace):
            body['IngressGatewayNamespace'] = request.ingress_gateway_namespace
        if not UtilClient.is_unset(request.ingress_type):
            body['IngressType'] = request.ingress_type
        if not UtilClient.is_unset(request.is_permissive):
            body['IsPermissive'] = request.is_permissive
        if not UtilClient.is_unset(request.route_header):
            body['RouteHeader'] = request.route_header
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.trace_header):
            body['TraceHeader'] = request.trace_header
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateSwimLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_swim_lane_group_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateSwimLaneGroupResponse:
        """
        @summary Creates a lane group.
        
        @param request: CreateSwimLaneGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSwimLaneGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ingress_gateway_name):
            body['IngressGatewayName'] = request.ingress_gateway_name
        if not UtilClient.is_unset(request.ingress_gateway_namespace):
            body['IngressGatewayNamespace'] = request.ingress_gateway_namespace
        if not UtilClient.is_unset(request.ingress_type):
            body['IngressType'] = request.ingress_type
        if not UtilClient.is_unset(request.is_permissive):
            body['IsPermissive'] = request.is_permissive
        if not UtilClient.is_unset(request.route_header):
            body['RouteHeader'] = request.route_header
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.trace_header):
            body['TraceHeader'] = request.trace_header
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateSwimLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_swim_lane_group(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.CreateSwimLaneGroupResponse:
        """
        @summary Creates a lane group.
        
        @param request: CreateSwimLaneGroupRequest
        @return: CreateSwimLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_swim_lane_group_with_options(request, runtime)

    async def create_swim_lane_group_async(
        self,
        request: servicemesh_20200111_models.CreateSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.CreateSwimLaneGroupResponse:
        """
        @summary Creates a lane group.
        
        @param request: CreateSwimLaneGroupRequest
        @return: CreateSwimLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_swim_lane_group_with_options_async(request, runtime)

    def create_waypoint_with_options(
        self,
        request: servicemesh_20200111_models.CreateWaypointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateWaypointResponse:
        """
        @summary 创建Waypoint
        
        @param request: CreateWaypointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWaypointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hpaenabled):
            body['HPAEnabled'] = request.hpaenabled
        if not UtilClient.is_unset(request.hpamax_replicas):
            body['HPAMaxReplicas'] = request.hpamax_replicas
        if not UtilClient.is_unset(request.hpamin_replicas):
            body['HPAMinReplicas'] = request.hpamin_replicas
        if not UtilClient.is_unset(request.hpatarget_cpu):
            body['HPATargetCPU'] = request.hpatarget_cpu
        if not UtilClient.is_unset(request.hpatarget_memory):
            body['HPATargetMemory'] = request.hpatarget_memory
        if not UtilClient.is_unset(request.limit_cpu):
            body['LimitCPU'] = request.limit_cpu
        if not UtilClient.is_unset(request.limit_memory):
            body['LimitMemory'] = request.limit_memory
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.prefer_eci):
            body['PreferECI'] = request.prefer_eci
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.request_cpu):
            body['RequestCPU'] = request.request_cpu
        if not UtilClient.is_unset(request.request_memory):
            body['RequestMemory'] = request.request_memory
        if not UtilClient.is_unset(request.service_account):
            body['ServiceAccount'] = request.service_account
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWaypoint',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateWaypointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_waypoint_with_options_async(
        self,
        request: servicemesh_20200111_models.CreateWaypointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.CreateWaypointResponse:
        """
        @summary 创建Waypoint
        
        @param request: CreateWaypointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWaypointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hpaenabled):
            body['HPAEnabled'] = request.hpaenabled
        if not UtilClient.is_unset(request.hpamax_replicas):
            body['HPAMaxReplicas'] = request.hpamax_replicas
        if not UtilClient.is_unset(request.hpamin_replicas):
            body['HPAMinReplicas'] = request.hpamin_replicas
        if not UtilClient.is_unset(request.hpatarget_cpu):
            body['HPATargetCPU'] = request.hpatarget_cpu
        if not UtilClient.is_unset(request.hpatarget_memory):
            body['HPATargetMemory'] = request.hpatarget_memory
        if not UtilClient.is_unset(request.limit_cpu):
            body['LimitCPU'] = request.limit_cpu
        if not UtilClient.is_unset(request.limit_memory):
            body['LimitMemory'] = request.limit_memory
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.prefer_eci):
            body['PreferECI'] = request.prefer_eci
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.request_cpu):
            body['RequestCPU'] = request.request_cpu
        if not UtilClient.is_unset(request.request_memory):
            body['RequestMemory'] = request.request_memory
        if not UtilClient.is_unset(request.service_account):
            body['ServiceAccount'] = request.service_account
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWaypoint',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateWaypointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_waypoint(
        self,
        request: servicemesh_20200111_models.CreateWaypointRequest,
    ) -> servicemesh_20200111_models.CreateWaypointResponse:
        """
        @summary 创建Waypoint
        
        @param request: CreateWaypointRequest
        @return: CreateWaypointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_waypoint_with_options(request, runtime)

    async def create_waypoint_async(
        self,
        request: servicemesh_20200111_models.CreateWaypointRequest,
    ) -> servicemesh_20200111_models.CreateWaypointResponse:
        """
        @summary 创建Waypoint
        
        @param request: CreateWaypointRequest
        @return: CreateWaypointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_waypoint_with_options_async(request, runtime)

    def delete_gateway_route_with_options(
        self,
        request: servicemesh_20200111_models.DeleteGatewayRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteGatewayRouteResponse:
        """
        @summary Deletes a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: DeleteGatewayRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.route_name):
            body['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGatewayRoute',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteGatewayRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_route_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteGatewayRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteGatewayRouteResponse:
        """
        @summary Deletes a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: DeleteGatewayRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewayRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.route_name):
            body['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGatewayRoute',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteGatewayRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_route(
        self,
        request: servicemesh_20200111_models.DeleteGatewayRouteRequest,
    ) -> servicemesh_20200111_models.DeleteGatewayRouteResponse:
        """
        @summary Deletes a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: DeleteGatewayRouteRequest
        @return: DeleteGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_route_with_options(request, runtime)

    async def delete_gateway_route_async(
        self,
        request: servicemesh_20200111_models.DeleteGatewayRouteRequest,
    ) -> servicemesh_20200111_models.DeleteGatewayRouteResponse:
        """
        @summary Deletes a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: DeleteGatewayRouteRequest
        @return: DeleteGatewayRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_route_with_options_async(request, runtime)

    def delete_gateway_secret_with_options(
        self,
        request: servicemesh_20200111_models.DeleteGatewaySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteGatewaySecretResponse:
        """
        @summary Deletes a secret for a Service Mesh (ASM) gateway.
        
        @param request: DeleteGatewaySecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewaySecretResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.secret_name):
            body['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGatewaySecret',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteGatewaySecretResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gateway_secret_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteGatewaySecretRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteGatewaySecretResponse:
        """
        @summary Deletes a secret for a Service Mesh (ASM) gateway.
        
        @param request: DeleteGatewaySecretRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGatewaySecretResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.secret_name):
            body['SecretName'] = request.secret_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGatewaySecret',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteGatewaySecretResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gateway_secret(
        self,
        request: servicemesh_20200111_models.DeleteGatewaySecretRequest,
    ) -> servicemesh_20200111_models.DeleteGatewaySecretResponse:
        """
        @summary Deletes a secret for a Service Mesh (ASM) gateway.
        
        @param request: DeleteGatewaySecretRequest
        @return: DeleteGatewaySecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_gateway_secret_with_options(request, runtime)

    async def delete_gateway_secret_async(
        self,
        request: servicemesh_20200111_models.DeleteGatewaySecretRequest,
    ) -> servicemesh_20200111_models.DeleteGatewaySecretResponse:
        """
        @summary Deletes a secret for a Service Mesh (ASM) gateway.
        
        @param request: DeleteGatewaySecretRequest
        @return: DeleteGatewaySecretResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_gateway_secret_with_options_async(request, runtime)

    def delete_istio_gateway_domains_with_options(
        self,
        request: servicemesh_20200111_models.DeleteIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse:
        """
        @summary Deletes one or more domain names for a Service Mesh (ASM) gateway.
        
        @param request: DeleteIstioGatewayDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIstioGatewayDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hosts):
            body['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.port_name):
            body['PortName'] = request.port_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_istio_gateway_domains_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse:
        """
        @summary Deletes one or more domain names for a Service Mesh (ASM) gateway.
        
        @param request: DeleteIstioGatewayDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIstioGatewayDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hosts):
            body['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.port_name):
            body['PortName'] = request.port_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_istio_gateway_domains(
        self,
        request: servicemesh_20200111_models.DeleteIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse:
        """
        @summary Deletes one or more domain names for a Service Mesh (ASM) gateway.
        
        @param request: DeleteIstioGatewayDomainsRequest
        @return: DeleteIstioGatewayDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_istio_gateway_domains_with_options(request, runtime)

    async def delete_istio_gateway_domains_async(
        self,
        request: servicemesh_20200111_models.DeleteIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.DeleteIstioGatewayDomainsResponse:
        """
        @summary Deletes one or more domain names for a Service Mesh (ASM) gateway.
        
        @param request: DeleteIstioGatewayDomainsRequest
        @return: DeleteIstioGatewayDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_istio_gateway_domains_with_options_async(request, runtime)

    def delete_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        """
        @summary Deletes a Service Mesh (ASM) instance.
        
        @param request: DeleteServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceMeshResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.retain_resources):
            body['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        """
        @summary Deletes a Service Mesh (ASM) instance.
        
        @param request: DeleteServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceMeshResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force):
            body['Force'] = request.force
        if not UtilClient.is_unset(request.retain_resources):
            body['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_mesh(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        """
        @summary Deletes a Service Mesh (ASM) instance.
        
        @param request: DeleteServiceMeshRequest
        @return: DeleteServiceMeshResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_service_mesh_with_options(request, runtime)

    async def delete_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DeleteServiceMeshRequest,
    ) -> servicemesh_20200111_models.DeleteServiceMeshResponse:
        """
        @summary Deletes a Service Mesh (ASM) instance.
        
        @param request: DeleteServiceMeshRequest
        @return: DeleteServiceMeshResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_mesh_with_options_async(request, runtime)

    def delete_swim_lane_with_options(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteSwimLaneResponse:
        """
        @summary Deletes a lane.
        
        @param request: DeleteSwimLaneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSwimLaneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteSwimLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_swim_lane_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteSwimLaneResponse:
        """
        @summary Deletes a lane.
        
        @param request: DeleteSwimLaneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSwimLaneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteSwimLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_swim_lane(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneRequest,
    ) -> servicemesh_20200111_models.DeleteSwimLaneResponse:
        """
        @summary Deletes a lane.
        
        @param request: DeleteSwimLaneRequest
        @return: DeleteSwimLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_swim_lane_with_options(request, runtime)

    async def delete_swim_lane_async(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneRequest,
    ) -> servicemesh_20200111_models.DeleteSwimLaneResponse:
        """
        @summary Deletes a lane.
        
        @param request: DeleteSwimLaneRequest
        @return: DeleteSwimLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_swim_lane_with_options_async(request, runtime)

    def delete_swim_lane_group_with_options(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteSwimLaneGroupResponse:
        """
        @summary Deletes a lane group. If a lane group is deleted, the lanes in the group and the traffic routing rules attached to the lanes are deleted.
        
        @param request: DeleteSwimLaneGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSwimLaneGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteSwimLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_swim_lane_group_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteSwimLaneGroupResponse:
        """
        @summary Deletes a lane group. If a lane group is deleted, the lanes in the group and the traffic routing rules attached to the lanes are deleted.
        
        @param request: DeleteSwimLaneGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSwimLaneGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteSwimLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_swim_lane_group(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.DeleteSwimLaneGroupResponse:
        """
        @summary Deletes a lane group. If a lane group is deleted, the lanes in the group and the traffic routing rules attached to the lanes are deleted.
        
        @param request: DeleteSwimLaneGroupRequest
        @return: DeleteSwimLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_swim_lane_group_with_options(request, runtime)

    async def delete_swim_lane_group_async(
        self,
        request: servicemesh_20200111_models.DeleteSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.DeleteSwimLaneGroupResponse:
        """
        @summary Deletes a lane group. If a lane group is deleted, the lanes in the group and the traffic routing rules attached to the lanes are deleted.
        
        @param request: DeleteSwimLaneGroupRequest
        @return: DeleteSwimLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_swim_lane_group_with_options_async(request, runtime)

    def delete_waypoint_with_options(
        self,
        request: servicemesh_20200111_models.DeleteWaypointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteWaypointResponse:
        """
        @summary 删除Waypoint资源
        
        @param request: DeleteWaypointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWaypointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWaypoint',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteWaypointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_waypoint_with_options_async(
        self,
        request: servicemesh_20200111_models.DeleteWaypointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DeleteWaypointResponse:
        """
        @summary 删除Waypoint资源
        
        @param request: DeleteWaypointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWaypointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWaypoint',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteWaypointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_waypoint(
        self,
        request: servicemesh_20200111_models.DeleteWaypointRequest,
    ) -> servicemesh_20200111_models.DeleteWaypointResponse:
        """
        @summary 删除Waypoint资源
        
        @param request: DeleteWaypointRequest
        @return: DeleteWaypointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_waypoint_with_options(request, runtime)

    async def delete_waypoint_async(
        self,
        request: servicemesh_20200111_models.DeleteWaypointRequest,
    ) -> servicemesh_20200111_models.DeleteWaypointResponse:
        """
        @summary 删除Waypoint资源
        
        @param request: DeleteWaypointRequest
        @return: DeleteWaypointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_waypoint_with_options_async(request, runtime)

    def describe_asmgateway_imported_services_with_options(
        self,
        request: servicemesh_20200111_models.DescribeASMGatewayImportedServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse:
        """
        @summary Queries the information about imported services on a Service Mesh (ASM) gateway.
        
        @param request: DescribeASMGatewayImportedServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeASMGatewayImportedServicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeASMGatewayImportedServices',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_asmgateway_imported_services_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeASMGatewayImportedServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse:
        """
        @summary Queries the information about imported services on a Service Mesh (ASM) gateway.
        
        @param request: DescribeASMGatewayImportedServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeASMGatewayImportedServicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeASMGatewayImportedServices',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_asmgateway_imported_services(
        self,
        request: servicemesh_20200111_models.DescribeASMGatewayImportedServicesRequest,
    ) -> servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse:
        """
        @summary Queries the information about imported services on a Service Mesh (ASM) gateway.
        
        @param request: DescribeASMGatewayImportedServicesRequest
        @return: DescribeASMGatewayImportedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_asmgateway_imported_services_with_options(request, runtime)

    async def describe_asmgateway_imported_services_async(
        self,
        request: servicemesh_20200111_models.DescribeASMGatewayImportedServicesRequest,
    ) -> servicemesh_20200111_models.DescribeASMGatewayImportedServicesResponse:
        """
        @summary Queries the information about imported services on a Service Mesh (ASM) gateway.
        
        @param request: DescribeASMGatewayImportedServicesRequest
        @return: DescribeASMGatewayImportedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_asmgateway_imported_services_with_options_async(request, runtime)

    def describe_ccmversion_with_options(
        self,
        request: servicemesh_20200111_models.DescribeCCMVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCCMVersionResponse:
        """
        @summary Queries the versions of the Cloud Controller Manager (CCM) component.
        
        @param request: DescribeCCMVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCCMVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCCMVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCCMVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ccmversion_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeCCMVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCCMVersionResponse:
        """
        @summary Queries the versions of the Cloud Controller Manager (CCM) component.
        
        @param request: DescribeCCMVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCCMVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCCMVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCCMVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ccmversion(
        self,
        request: servicemesh_20200111_models.DescribeCCMVersionRequest,
    ) -> servicemesh_20200111_models.DescribeCCMVersionResponse:
        """
        @summary Queries the versions of the Cloud Controller Manager (CCM) component.
        
        @param request: DescribeCCMVersionRequest
        @return: DescribeCCMVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ccmversion_with_options(request, runtime)

    async def describe_ccmversion_async(
        self,
        request: servicemesh_20200111_models.DescribeCCMVersionRequest,
    ) -> servicemesh_20200111_models.DescribeCCMVersionResponse:
        """
        @summary Queries the versions of the Cloud Controller Manager (CCM) component.
        
        @param request: DescribeCCMVersionRequest
        @return: DescribeCCMVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ccmversion_with_options_async(request, runtime)

    def describe_cens_with_options(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        """
        @summary Queries the network connectivity between clusters that are deployed across virtual private clouds (VPCs) in a Service Mesh (ASM) instance.
        
        @param request: DescribeCensRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCensResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCensResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cens_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        """
        @summary Queries the network connectivity between clusters that are deployed across virtual private clouds (VPCs) in a Service Mesh (ASM) instance.
        
        @param request: DescribeCensRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCensResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCens',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cens(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        """
        @summary Queries the network connectivity between clusters that are deployed across virtual private clouds (VPCs) in a Service Mesh (ASM) instance.
        
        @param request: DescribeCensRequest
        @return: DescribeCensResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    async def describe_cens_async(
        self,
        request: servicemesh_20200111_models.DescribeCensRequest,
    ) -> servicemesh_20200111_models.DescribeCensResponse:
        """
        @summary Queries the network connectivity between clusters that are deployed across virtual private clouds (VPCs) in a Service Mesh (ASM) instance.
        
        @param request: DescribeCensRequest
        @return: DescribeCensResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cens_with_options_async(request, runtime)

    def describe_cluster_grafana_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        """
        @summary Queries the information about Grafana dashboards of a cluster in a Service Mesh (ASM) instance.
        
        @param request: DescribeClusterGrafanaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterGrafanaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.re_add_prometheus_integration):
            query['ReAddPrometheusIntegration'] = request.re_add_prometheus_integration
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterGrafana',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_grafana_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        """
        @summary Queries the information about Grafana dashboards of a cluster in a Service Mesh (ASM) instance.
        
        @param request: DescribeClusterGrafanaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterGrafanaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.re_add_prometheus_integration):
            query['ReAddPrometheusIntegration'] = request.re_add_prometheus_integration
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterGrafana',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterGrafanaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_grafana(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        """
        @summary Queries the information about Grafana dashboards of a cluster in a Service Mesh (ASM) instance.
        
        @param request: DescribeClusterGrafanaRequest
        @return: DescribeClusterGrafanaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_grafana_with_options(request, runtime)

    async def describe_cluster_grafana_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterGrafanaRequest,
    ) -> servicemesh_20200111_models.DescribeClusterGrafanaResponse:
        """
        @summary Queries the information about Grafana dashboards of a cluster in a Service Mesh (ASM) instance.
        
        @param request: DescribeClusterGrafanaRequest
        @return: DescribeClusterGrafanaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_grafana_with_options_async(request, runtime)

    def describe_cluster_prometheus_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        """
        @summary Queries the public endpoint of the Prometheus service that is used to monitor a cluster in an Alibaba Cloud Service Mesh (ASM) instance.
        
        @param request: DescribeClusterPrometheusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterPrometheusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.k_8s_cluster_region_id):
            query['K8sClusterRegionId'] = request.k_8s_cluster_region_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterPrometheus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterPrometheusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_prometheus_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        """
        @summary Queries the public endpoint of the Prometheus service that is used to monitor a cluster in an Alibaba Cloud Service Mesh (ASM) instance.
        
        @param request: DescribeClusterPrometheusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterPrometheusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            query['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.k_8s_cluster_region_id):
            query['K8sClusterRegionId'] = request.k_8s_cluster_region_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterPrometheus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterPrometheusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_prometheus(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        """
        @summary Queries the public endpoint of the Prometheus service that is used to monitor a cluster in an Alibaba Cloud Service Mesh (ASM) instance.
        
        @param request: DescribeClusterPrometheusRequest
        @return: DescribeClusterPrometheusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_prometheus_with_options(request, runtime)

    async def describe_cluster_prometheus_async(
        self,
        request: servicemesh_20200111_models.DescribeClusterPrometheusRequest,
    ) -> servicemesh_20200111_models.DescribeClusterPrometheusResponse:
        """
        @summary Queries the public endpoint of the Prometheus service that is used to monitor a cluster in an Alibaba Cloud Service Mesh (ASM) instance.
        
        @param request: DescribeClusterPrometheusRequest
        @return: DescribeClusterPrometheusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_prometheus_with_options_async(request, runtime)

    def describe_clusters_in_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        """
        @summary Queries the information about clusters in a Service Mesh (ASM) instance.
        
        @param request: DescribeClustersInServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClustersInServiceMeshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClustersInServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_clusters_in_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        """
        @summary Queries the information about clusters in a Service Mesh (ASM) instance.
        
        @param request: DescribeClustersInServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClustersInServiceMeshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClustersInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClustersInServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clusters_in_service_mesh(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        """
        @summary Queries the information about clusters in a Service Mesh (ASM) instance.
        
        @param request: DescribeClustersInServiceMeshRequest
        @return: DescribeClustersInServiceMeshResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_in_service_mesh_with_options(request, runtime)

    async def describe_clusters_in_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DescribeClustersInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeClustersInServiceMeshResponse:
        """
        @summary Queries the information about clusters in a Service Mesh (ASM) instance.
        
        @param request: DescribeClustersInServiceMeshRequest
        @return: DescribeClustersInServiceMeshResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_clusters_in_service_mesh_with_options_async(request, runtime)

    def describe_cr_templates_with_options(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        """
        @summary Queries the common YAML templates of Istio resources used by Service Mesh (ASM) instances.
        
        @param request: DescribeCrTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCrTemplatesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kind):
            body['Kind'] = request.kind
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCrTemplates',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCrTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cr_templates_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        """
        @summary Queries the common YAML templates of Istio resources used by Service Mesh (ASM) instances.
        
        @param request: DescribeCrTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCrTemplatesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_version):
            body['IstioVersion'] = request.istio_version
        if not UtilClient.is_unset(request.kind):
            body['Kind'] = request.kind
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCrTemplates',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCrTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cr_templates(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        """
        @summary Queries the common YAML templates of Istio resources used by Service Mesh (ASM) instances.
        
        @param request: DescribeCrTemplatesRequest
        @return: DescribeCrTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cr_templates_with_options(request, runtime)

    async def describe_cr_templates_async(
        self,
        request: servicemesh_20200111_models.DescribeCrTemplatesRequest,
    ) -> servicemesh_20200111_models.DescribeCrTemplatesResponse:
        """
        @summary Queries the common YAML templates of Istio resources used by Service Mesh (ASM) instances.
        
        @param request: DescribeCrTemplatesRequest
        @return: DescribeCrTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cr_templates_with_options_async(request, runtime)

    def describe_eip_resources_with_options(
        self,
        request: servicemesh_20200111_models.DescribeEipResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeEipResourcesResponse:
        """
        @summary DescribeEipResources
        
        @param request: DescribeEipResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEipResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEipResources',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeEipResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eip_resources_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeEipResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeEipResourcesResponse:
        """
        @summary DescribeEipResources
        
        @param request: DescribeEipResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEipResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEipResources',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeEipResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eip_resources(
        self,
        request: servicemesh_20200111_models.DescribeEipResourcesRequest,
    ) -> servicemesh_20200111_models.DescribeEipResourcesResponse:
        """
        @summary DescribeEipResources
        
        @param request: DescribeEipResourcesRequest
        @return: DescribeEipResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_resources_with_options(request, runtime)

    async def describe_eip_resources_async(
        self,
        request: servicemesh_20200111_models.DescribeEipResourcesRequest,
    ) -> servicemesh_20200111_models.DescribeEipResourcesResponse:
        """
        @summary DescribeEipResources
        
        @param request: DescribeEipResourcesRequest
        @return: DescribeEipResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_eip_resources_with_options_async(request, runtime)

    def describe_gateway_secret_details_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGatewaySecretDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse:
        """
        @summary Queries the detailed information about a secret of a Service Mesh (ASM) gateway.
        
        @param request: DescribeGatewaySecretDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGatewaySecretDetailsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGatewaySecretDetails',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gateway_secret_details_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGatewaySecretDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse:
        """
        @summary Queries the detailed information about a secret of a Service Mesh (ASM) gateway.
        
        @param request: DescribeGatewaySecretDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGatewaySecretDetailsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGatewaySecretDetails',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gateway_secret_details(
        self,
        request: servicemesh_20200111_models.DescribeGatewaySecretDetailsRequest,
    ) -> servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse:
        """
        @summary Queries the detailed information about a secret of a Service Mesh (ASM) gateway.
        
        @param request: DescribeGatewaySecretDetailsRequest
        @return: DescribeGatewaySecretDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_gateway_secret_details_with_options(request, runtime)

    async def describe_gateway_secret_details_async(
        self,
        request: servicemesh_20200111_models.DescribeGatewaySecretDetailsRequest,
    ) -> servicemesh_20200111_models.DescribeGatewaySecretDetailsResponse:
        """
        @summary Queries the detailed information about a secret of a Service Mesh (ASM) gateway.
        
        @param request: DescribeGatewaySecretDetailsRequest
        @return: DescribeGatewaySecretDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_gateway_secret_details_with_options_async(request, runtime)

    def describe_guest_cluster_access_log_dashboards_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        """
        @summary Queries the access log dashboards of a cluster on the data plane.
        
        @param request: DescribeGuestClusterAccessLogDashboardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGuestClusterAccessLogDashboardsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterAccessLogDashboards',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_guest_cluster_access_log_dashboards_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        """
        @summary Queries the access log dashboards of a cluster on the data plane.
        
        @param request: DescribeGuestClusterAccessLogDashboardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGuestClusterAccessLogDashboardsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterAccessLogDashboards',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_guest_cluster_access_log_dashboards(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        """
        @summary Queries the access log dashboards of a cluster on the data plane.
        
        @param request: DescribeGuestClusterAccessLogDashboardsRequest
        @return: DescribeGuestClusterAccessLogDashboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_access_log_dashboards_with_options(request, runtime)

    async def describe_guest_cluster_access_log_dashboards_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse:
        """
        @summary Queries the access log dashboards of a cluster on the data plane.
        
        @param request: DescribeGuestClusterAccessLogDashboardsRequest
        @return: DescribeGuestClusterAccessLogDashboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_guest_cluster_access_log_dashboards_with_options_async(request, runtime)

    def describe_guest_cluster_namespaces_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        """
        @summary Queries a list of the namespaces of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: DescribeGuestClusterNamespacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGuestClusterNamespacesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.show_ns_labels):
            body['ShowNsLabels'] = request.show_ns_labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_guest_cluster_namespaces_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        """
        @summary Queries a list of the namespaces of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: DescribeGuestClusterNamespacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGuestClusterNamespacesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.show_ns_labels):
            body['ShowNsLabels'] = request.show_ns_labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_guest_cluster_namespaces(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        """
        @summary Queries a list of the namespaces of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: DescribeGuestClusterNamespacesRequest
        @return: DescribeGuestClusterNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_namespaces_with_options(request, runtime)

    async def describe_guest_cluster_namespaces_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterNamespacesRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterNamespacesResponse:
        """
        @summary Queries a list of the namespaces of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: DescribeGuestClusterNamespacesRequest
        @return: DescribeGuestClusterNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_guest_cluster_namespaces_with_options_async(request, runtime)

    def describe_guest_cluster_pods_with_options(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        """
        @summary Queries a list of the pods in a specified namespace of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: DescribeGuestClusterPodsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGuestClusterPodsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterPods',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterPodsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_guest_cluster_pods_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        """
        @summary Queries a list of the pods in a specified namespace of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: DescribeGuestClusterPodsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeGuestClusterPodsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterID'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeGuestClusterPods',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterPodsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_guest_cluster_pods(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        """
        @summary Queries a list of the pods in a specified namespace of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: DescribeGuestClusterPodsRequest
        @return: DescribeGuestClusterPodsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_pods_with_options(request, runtime)

    async def describe_guest_cluster_pods_async(
        self,
        request: servicemesh_20200111_models.DescribeGuestClusterPodsRequest,
    ) -> servicemesh_20200111_models.DescribeGuestClusterPodsResponse:
        """
        @summary Queries a list of the pods in a specified namespace of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: DescribeGuestClusterPodsRequest
        @return: DescribeGuestClusterPodsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_guest_cluster_pods_with_options_async(request, runtime)

    def describe_imported_services_detail_with_options(
        self,
        request: servicemesh_20200111_models.DescribeImportedServicesDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeImportedServicesDetailResponse:
        """
        @summary Queries the details of the imported services on a Service Mesh (ASM) gateway.
        
        @param request: DescribeImportedServicesDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImportedServicesDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImportedServicesDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeImportedServicesDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_imported_services_detail_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeImportedServicesDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeImportedServicesDetailResponse:
        """
        @summary Queries the details of the imported services on a Service Mesh (ASM) gateway.
        
        @param request: DescribeImportedServicesDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeImportedServicesDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeImportedServicesDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeImportedServicesDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_imported_services_detail(
        self,
        request: servicemesh_20200111_models.DescribeImportedServicesDetailRequest,
    ) -> servicemesh_20200111_models.DescribeImportedServicesDetailResponse:
        """
        @summary Queries the details of the imported services on a Service Mesh (ASM) gateway.
        
        @param request: DescribeImportedServicesDetailRequest
        @return: DescribeImportedServicesDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_imported_services_detail_with_options(request, runtime)

    async def describe_imported_services_detail_async(
        self,
        request: servicemesh_20200111_models.DescribeImportedServicesDetailRequest,
    ) -> servicemesh_20200111_models.DescribeImportedServicesDetailResponse:
        """
        @summary Queries the details of the imported services on a Service Mesh (ASM) gateway.
        
        @param request: DescribeImportedServicesDetailRequest
        @return: DescribeImportedServicesDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_imported_services_detail_with_options_async(request, runtime)

    def describe_istio_gateway_domains_with_options(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse:
        """
        @summary Queries a list of the domain names that are exposed by a Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIstioGatewayDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_istio_gateway_domains_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayDomainsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse:
        """
        @summary Queries a list of the domain names that are exposed by a Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayDomainsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIstioGatewayDomainsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayDomains',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_istio_gateway_domains(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse:
        """
        @summary Queries a list of the domain names that are exposed by a Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayDomainsRequest
        @return: DescribeIstioGatewayDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_istio_gateway_domains_with_options(request, runtime)

    async def describe_istio_gateway_domains_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayDomainsRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayDomainsResponse:
        """
        @summary Queries a list of the domain names that are exposed by a Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayDomainsRequest
        @return: DescribeIstioGatewayDomainsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_istio_gateway_domains_with_options_async(request, runtime)

    def describe_istio_gateway_route_detail_with_options(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRouteDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse:
        """
        @summary Queries the detailed information about a routing rule of an Alibaba Cloud Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayRouteDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIstioGatewayRouteDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.route_name):
            body['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayRouteDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_istio_gateway_route_detail_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRouteDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse:
        """
        @summary Queries the detailed information about a routing rule of an Alibaba Cloud Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayRouteDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIstioGatewayRouteDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.route_name):
            body['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayRouteDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_istio_gateway_route_detail(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRouteDetailRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse:
        """
        @summary Queries the detailed information about a routing rule of an Alibaba Cloud Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayRouteDetailRequest
        @return: DescribeIstioGatewayRouteDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_istio_gateway_route_detail_with_options(request, runtime)

    async def describe_istio_gateway_route_detail_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRouteDetailRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRouteDetailResponse:
        """
        @summary Queries the detailed information about a routing rule of an Alibaba Cloud Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayRouteDetailRequest
        @return: DescribeIstioGatewayRouteDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_istio_gateway_route_detail_with_options_async(request, runtime)

    def describe_istio_gateway_routes_with_options(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse:
        """
        @summary Queries the routing rules for a Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayRoutesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIstioGatewayRoutesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_istio_gateway_routes_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse:
        """
        @summary Queries the routing rules for a Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayRoutesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIstioGatewayRoutesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_istio_gateway_routes(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse:
        """
        @summary Queries the routing rules for a Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayRoutesRequest
        @return: DescribeIstioGatewayRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_istio_gateway_routes_with_options(request, runtime)

    async def describe_istio_gateway_routes_async(
        self,
        request: servicemesh_20200111_models.DescribeIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.DescribeIstioGatewayRoutesResponse:
        """
        @summary Queries the routing rules for a Service Mesh (ASM) gateway.
        
        @param request: DescribeIstioGatewayRoutesRequest
        @return: DescribeIstioGatewayRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_istio_gateway_routes_with_options_async(request, runtime)

    def describe_mesh_multi_cluster_network_with_options(
        self,
        request: servicemesh_20200111_models.DescribeMeshMultiClusterNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeMeshMultiClusterNetworkResponse:
        """
        @summary 获取ASM网格网络分区设置
        
        @param request: DescribeMeshMultiClusterNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMeshMultiClusterNetworkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMeshMultiClusterNetwork',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeMeshMultiClusterNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mesh_multi_cluster_network_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeMeshMultiClusterNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeMeshMultiClusterNetworkResponse:
        """
        @summary 获取ASM网格网络分区设置
        
        @param request: DescribeMeshMultiClusterNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMeshMultiClusterNetworkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeMeshMultiClusterNetwork',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeMeshMultiClusterNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mesh_multi_cluster_network(
        self,
        request: servicemesh_20200111_models.DescribeMeshMultiClusterNetworkRequest,
    ) -> servicemesh_20200111_models.DescribeMeshMultiClusterNetworkResponse:
        """
        @summary 获取ASM网格网络分区设置
        
        @param request: DescribeMeshMultiClusterNetworkRequest
        @return: DescribeMeshMultiClusterNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_mesh_multi_cluster_network_with_options(request, runtime)

    async def describe_mesh_multi_cluster_network_async(
        self,
        request: servicemesh_20200111_models.DescribeMeshMultiClusterNetworkRequest,
    ) -> servicemesh_20200111_models.DescribeMeshMultiClusterNetworkResponse:
        """
        @summary 获取ASM网格网络分区设置
        
        @param request: DescribeMeshMultiClusterNetworkRequest
        @return: DescribeMeshMultiClusterNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_mesh_multi_cluster_network_with_options_async(request, runtime)

    def describe_metadata_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeMetadataResponse:
        """
        @summary Queries basic information about a Service Mesh (ASM) instance.
        
        @param request: DescribeMetadataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetadataResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMetadata',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metadata_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeMetadataResponse:
        """
        @summary Queries basic information about a Service Mesh (ASM) instance.
        
        @param request: DescribeMetadataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMetadataResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeMetadata',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metadata(self) -> servicemesh_20200111_models.DescribeMetadataResponse:
        """
        @summary Queries basic information about a Service Mesh (ASM) instance.
        
        @return: DescribeMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_metadata_with_options(runtime)

    async def describe_metadata_async(self) -> servicemesh_20200111_models.DescribeMetadataResponse:
        """
        @summary Queries basic information about a Service Mesh (ASM) instance.
        
        @return: DescribeMetadataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_metadata_with_options_async(runtime)

    def describe_namespace_scope_sidecar_config_with_options(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        """
        @summary Queries the configurations of sidecar proxies at the namespace level.
        
        @param request: DescribeNamespaceScopeSidecarConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespaceScopeSidecarConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_namespace_scope_sidecar_config_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        """
        @summary Queries the configurations of sidecar proxies at the namespace level.
        
        @param request: DescribeNamespaceScopeSidecarConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNamespaceScopeSidecarConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_namespace_scope_sidecar_config(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        """
        @summary Queries the configurations of sidecar proxies at the namespace level.
        
        @param request: DescribeNamespaceScopeSidecarConfigRequest
        @return: DescribeNamespaceScopeSidecarConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_namespace_scope_sidecar_config_with_options(request, runtime)

    async def describe_namespace_scope_sidecar_config_async(
        self,
        request: servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.DescribeNamespaceScopeSidecarConfigResponse:
        """
        @summary Queries the configurations of sidecar proxies at the namespace level.
        
        @param request: DescribeNamespaceScopeSidecarConfigRequest
        @return: DescribeNamespaceScopeSidecarConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_namespace_scope_sidecar_config_with_options_async(request, runtime)

    def describe_nodes_instance_type_with_options(
        self,
        request: servicemesh_20200111_models.DescribeNodesInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeNodesInstanceTypeResponse:
        """
        @summary Queries the instance types of nodes on the data plane and whether the instance types support Multi-Buffer acceleration.
        
        @param request: DescribeNodesInstanceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodesInstanceTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodesInstanceType',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeNodesInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nodes_instance_type_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeNodesInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeNodesInstanceTypeResponse:
        """
        @summary Queries the instance types of nodes on the data plane and whether the instance types support Multi-Buffer acceleration.
        
        @param request: DescribeNodesInstanceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodesInstanceTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodesInstanceType',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeNodesInstanceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nodes_instance_type(
        self,
        request: servicemesh_20200111_models.DescribeNodesInstanceTypeRequest,
    ) -> servicemesh_20200111_models.DescribeNodesInstanceTypeResponse:
        """
        @summary Queries the instance types of nodes on the data plane and whether the instance types support Multi-Buffer acceleration.
        
        @param request: DescribeNodesInstanceTypeRequest
        @return: DescribeNodesInstanceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_nodes_instance_type_with_options(request, runtime)

    async def describe_nodes_instance_type_async(
        self,
        request: servicemesh_20200111_models.DescribeNodesInstanceTypeRequest,
    ) -> servicemesh_20200111_models.DescribeNodesInstanceTypeResponse:
        """
        @summary Queries the instance types of nodes on the data plane and whether the instance types support Multi-Buffer acceleration.
        
        @param request: DescribeNodesInstanceTypeRequest
        @return: DescribeNodesInstanceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_nodes_instance_type_with_options_async(request, runtime)

    def describe_reusable_slb_with_options(
        self,
        request: servicemesh_20200111_models.DescribeReusableSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeReusableSlbResponse:
        """
        @summary Queries the Server Load Balancer (SLB) instances that can be reused.
        
        @param request: DescribeReusableSlbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeReusableSlbResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.lb_type):
            body['LbType'] = request.lb_type
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeReusableSlb',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeReusableSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_reusable_slb_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeReusableSlbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeReusableSlbResponse:
        """
        @summary Queries the Server Load Balancer (SLB) instances that can be reused.
        
        @param request: DescribeReusableSlbRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeReusableSlbResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.lb_type):
            body['LbType'] = request.lb_type
        if not UtilClient.is_unset(request.network_type):
            body['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeReusableSlb',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeReusableSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_reusable_slb(
        self,
        request: servicemesh_20200111_models.DescribeReusableSlbRequest,
    ) -> servicemesh_20200111_models.DescribeReusableSlbResponse:
        """
        @summary Queries the Server Load Balancer (SLB) instances that can be reused.
        
        @param request: DescribeReusableSlbRequest
        @return: DescribeReusableSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_reusable_slb_with_options(request, runtime)

    async def describe_reusable_slb_async(
        self,
        request: servicemesh_20200111_models.DescribeReusableSlbRequest,
    ) -> servicemesh_20200111_models.DescribeReusableSlbResponse:
        """
        @summary Queries the Server Load Balancer (SLB) instances that can be reused.
        
        @param request: DescribeReusableSlbRequest
        @return: DescribeReusableSlbResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_reusable_slb_with_options_async(request, runtime)

    def describe_service_mesh_additional_status_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse:
        """
        @summary Queries the check results of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshAdditionalStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshAdditionalStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_mode):
            body['CheckMode'] = request.check_mode
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshAdditionalStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_additional_status_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse:
        """
        @summary Queries the check results of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshAdditionalStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshAdditionalStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_mode):
            body['CheckMode'] = request.check_mode
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshAdditionalStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_additional_status(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse:
        """
        @summary Queries the check results of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshAdditionalStatusRequest
        @return: DescribeServiceMeshAdditionalStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_additional_status_with_options(request, runtime)

    async def describe_service_mesh_additional_status_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshAdditionalStatusResponse:
        """
        @summary Queries the check results of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshAdditionalStatusRequest
        @return: DescribeServiceMeshAdditionalStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_additional_status_with_options_async(request, runtime)

    def describe_service_mesh_clusters_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshClustersResponse:
        """
        @summary Queries the clusters that can be added to a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshClusters',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_clusters_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshClustersResponse:
        """
        @summary Queries the clusters that can be added to a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshClusters',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_clusters(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshClustersRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshClustersResponse:
        """
        @summary Queries the clusters that can be added to a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshClustersRequest
        @return: DescribeServiceMeshClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_clusters_with_options(request, runtime)

    async def describe_service_mesh_clusters_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshClustersRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshClustersResponse:
        """
        @summary Queries the clusters that can be added to a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshClustersRequest
        @return: DescribeServiceMeshClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_clusters_with_options_async(request, runtime)

    def describe_service_mesh_detail_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        """
        @summary Queries the details of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_detail_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        """
        @summary Queries the details of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_detail(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        """
        @summary Queries the details of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshDetailRequest
        @return: DescribeServiceMeshDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_detail_with_options(request, runtime)

    async def describe_service_mesh_detail_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshDetailRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshDetailResponse:
        """
        @summary Queries the details of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshDetailRequest
        @return: DescribeServiceMeshDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_detail_with_options_async(request, runtime)

    def describe_service_mesh_kubeconfig_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        """
        @summary Queries the content of the kubeconfig file of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshKubeconfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshKubeconfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_kubeconfig_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        """
        @summary Queries the content of the kubeconfig file of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshKubeconfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshKubeconfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_kubeconfig(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        """
        @summary Queries the content of the kubeconfig file of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshKubeconfigRequest
        @return: DescribeServiceMeshKubeconfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_kubeconfig_with_options(request, runtime)

    async def describe_service_mesh_kubeconfig_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshKubeconfigRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse:
        """
        @summary Queries the content of the kubeconfig file of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshKubeconfigRequest
        @return: DescribeServiceMeshKubeconfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_kubeconfig_with_options_async(request, runtime)

    def describe_service_mesh_logs_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshLogsResponse:
        """
        @summary Queries the logs of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshLogsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshLogs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_logs_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshLogsResponse:
        """
        @summary Queries the logs of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshLogsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshLogs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_logs(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshLogsRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshLogsResponse:
        """
        @summary Queries the logs of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshLogsRequest
        @return: DescribeServiceMeshLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_logs_with_options(request, runtime)

    async def describe_service_mesh_logs_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshLogsRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshLogsResponse:
        """
        @summary Queries the logs of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshLogsRequest
        @return: DescribeServiceMeshLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_logs_with_options_async(request, runtime)

    def describe_service_mesh_proxy_status_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshProxyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse:
        """
        @summary Queries the status of proxies on the data plane of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshProxyStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshProxyStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshProxyStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_proxy_status_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshProxyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse:
        """
        @summary Queries the status of proxies on the data plane of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshProxyStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshProxyStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshProxyStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_proxy_status(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshProxyStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse:
        """
        @summary Queries the status of proxies on the data plane of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshProxyStatusRequest
        @return: DescribeServiceMeshProxyStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_proxy_status_with_options(request, runtime)

    async def describe_service_mesh_proxy_status_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshProxyStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshProxyStatusResponse:
        """
        @summary Queries the status of proxies on the data plane of a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshProxyStatusRequest
        @return: DescribeServiceMeshProxyStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_proxy_status_with_options_async(request, runtime)

    def describe_service_mesh_upgrade_status_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        """
        @summary Queries the upgrade details of a Service Mesh (ASM) instance and its ingress gateways.
        
        @param request: DescribeServiceMeshUpgradeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshUpgradeStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.all_istio_gateway_full_names):
            body['AllIstioGatewayFullNames'] = request.all_istio_gateway_full_names
        if not UtilClient.is_unset(request.guest_cluster_ids):
            body['GuestClusterIds'] = request.guest_cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshUpgradeStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_upgrade_status_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        """
        @summary Queries the upgrade details of a Service Mesh (ASM) instance and its ingress gateways.
        
        @param request: DescribeServiceMeshUpgradeStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshUpgradeStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        body = {}
        if not UtilClient.is_unset(request.all_istio_gateway_full_names):
            body['AllIstioGatewayFullNames'] = request.all_istio_gateway_full_names
        if not UtilClient.is_unset(request.guest_cluster_ids):
            body['GuestClusterIds'] = request.guest_cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshUpgradeStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_upgrade_status(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        """
        @summary Queries the upgrade details of a Service Mesh (ASM) instance and its ingress gateways.
        
        @param request: DescribeServiceMeshUpgradeStatusRequest
        @return: DescribeServiceMeshUpgradeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_upgrade_status_with_options(request, runtime)

    async def describe_service_mesh_upgrade_status_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshUpgradeStatusResponse:
        """
        @summary Queries the upgrade details of a Service Mesh (ASM) instance and its ingress gateways.
        
        @param request: DescribeServiceMeshUpgradeStatusRequest
        @return: DescribeServiceMeshUpgradeStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_upgrade_status_with_options_async(request, runtime)

    def describe_service_mesh_vms_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        """
        @deprecated OpenAPI DescribeServiceMeshVMs is deprecated
        
        @summary Queries the Elastic Compute Service (ECS) instances that reside in the same virtual private cloud (VPC) as a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshVMsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshVMsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshVMs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshVMsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_mesh_vms_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        """
        @deprecated OpenAPI DescribeServiceMeshVMs is deprecated
        
        @summary Queries the Elastic Compute Service (ECS) instances that reside in the same virtual private cloud (VPC) as a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshVMsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshVMsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshVMs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshVMsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_mesh_vms(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        """
        @deprecated OpenAPI DescribeServiceMeshVMs is deprecated
        
        @summary Queries the Elastic Compute Service (ECS) instances that reside in the same virtual private cloud (VPC) as a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshVMsRequest
        @return: DescribeServiceMeshVMsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_vms_with_options(request, runtime)

    async def describe_service_mesh_vms_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshVMsRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshVMsResponse:
        """
        @deprecated OpenAPI DescribeServiceMeshVMs is deprecated
        
        @summary Queries the Elastic Compute Service (ECS) instances that reside in the same virtual private cloud (VPC) as a Service Mesh (ASM) instance.
        
        @param request: DescribeServiceMeshVMsRequest
        @return: DescribeServiceMeshVMsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_mesh_vms_with_options_async(request, runtime)

    def describe_service_meshes_with_options(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        """
        @summary Queries ASM instances.
        
        @param request: DescribeServiceMeshesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_meshes_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        """
        @summary Queries ASM instances.
        
        @param request: DescribeServiceMeshesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeServiceMeshesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceMeshes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_meshes(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshesRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        """
        @summary Queries ASM instances.
        
        @param request: DescribeServiceMeshesRequest
        @return: DescribeServiceMeshesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_service_meshes_with_options(request, runtime)

    async def describe_service_meshes_async(
        self,
        request: servicemesh_20200111_models.DescribeServiceMeshesRequest,
    ) -> servicemesh_20200111_models.DescribeServiceMeshesResponse:
        """
        @summary Queries ASM instances.
        
        @param request: DescribeServiceMeshesRequest
        @return: DescribeServiceMeshesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_meshes_with_options_async(request, runtime)

    def describe_upgrade_version_with_options(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        """
        @summary Queries the update status of a Service Mesh (ASM) instance.
        
        @param request: DescribeUpgradeVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUpgradeVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpgradeVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUpgradeVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_upgrade_version_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        """
        @summary Queries the update status of a Service Mesh (ASM) instance.
        
        @param request: DescribeUpgradeVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUpgradeVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpgradeVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUpgradeVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_upgrade_version(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        """
        @summary Queries the update status of a Service Mesh (ASM) instance.
        
        @param request: DescribeUpgradeVersionRequest
        @return: DescribeUpgradeVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_upgrade_version_with_options(request, runtime)

    async def describe_upgrade_version_async(
        self,
        request: servicemesh_20200111_models.DescribeUpgradeVersionRequest,
    ) -> servicemesh_20200111_models.DescribeUpgradeVersionResponse:
        """
        @summary Queries the update status of a Service Mesh (ASM) instance.
        
        @param request: DescribeUpgradeVersionRequest
        @return: DescribeUpgradeVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_upgrade_version_with_options_async(request, runtime)

    def describe_user_permissions_with_options(
        self,
        request: servicemesh_20200111_models.DescribeUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUserPermissionsResponse:
        """
        @summary Obtains role-based access control (RBAC) permissions.
        
        @param request: DescribeUserPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserPermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sub_account_user_id):
            body['SubAccountUserId'] = request.sub_account_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUserPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_permissions_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUserPermissionsResponse:
        """
        @summary Obtains role-based access control (RBAC) permissions.
        
        @param request: DescribeUserPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserPermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.sub_account_user_id):
            body['SubAccountUserId'] = request.sub_account_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUserPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_permissions(
        self,
        request: servicemesh_20200111_models.DescribeUserPermissionsRequest,
    ) -> servicemesh_20200111_models.DescribeUserPermissionsResponse:
        """
        @summary Obtains role-based access control (RBAC) permissions.
        
        @param request: DescribeUserPermissionsRequest
        @return: DescribeUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_permissions_with_options(request, runtime)

    async def describe_user_permissions_async(
        self,
        request: servicemesh_20200111_models.DescribeUserPermissionsRequest,
    ) -> servicemesh_20200111_models.DescribeUserPermissionsResponse:
        """
        @summary Obtains role-based access control (RBAC) permissions.
        
        @param request: DescribeUserPermissionsRequest
        @return: DescribeUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_permissions_with_options_async(request, runtime)

    def describe_users_with_permissions_with_options(
        self,
        request: servicemesh_20200111_models.DescribeUsersWithPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUsersWithPermissionsResponse:
        """
        @summary Queries the IDs of all RAM users or RAM roles to which a Role-based Access Control (RBAC) role is assigned.
        
        @param request: DescribeUsersWithPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsersWithPermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUsersWithPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUsersWithPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_users_with_permissions_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeUsersWithPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeUsersWithPermissionsResponse:
        """
        @summary Queries the IDs of all RAM users or RAM roles to which a Role-based Access Control (RBAC) role is assigned.
        
        @param request: DescribeUsersWithPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUsersWithPermissionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUsersWithPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUsersWithPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_users_with_permissions(
        self,
        request: servicemesh_20200111_models.DescribeUsersWithPermissionsRequest,
    ) -> servicemesh_20200111_models.DescribeUsersWithPermissionsResponse:
        """
        @summary Queries the IDs of all RAM users or RAM roles to which a Role-based Access Control (RBAC) role is assigned.
        
        @param request: DescribeUsersWithPermissionsRequest
        @return: DescribeUsersWithPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_users_with_permissions_with_options(request, runtime)

    async def describe_users_with_permissions_async(
        self,
        request: servicemesh_20200111_models.DescribeUsersWithPermissionsRequest,
    ) -> servicemesh_20200111_models.DescribeUsersWithPermissionsResponse:
        """
        @summary Queries the IDs of all RAM users or RAM roles to which a Role-based Access Control (RBAC) role is assigned.
        
        @param request: DescribeUsersWithPermissionsRequest
        @return: DescribeUsersWithPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_users_with_permissions_with_options_async(request, runtime)

    def describe_vms_in_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        """
        @deprecated OpenAPI DescribeVMsInServiceMesh is deprecated
        
        @summary Queries the virtual machines (VMs) that are added to a Service Mesh (ASM) instance.
        
        @param request: DescribeVMsInServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVMsInServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVMsInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVMsInServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vms_in_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        """
        @deprecated OpenAPI DescribeVMsInServiceMesh is deprecated
        
        @summary Queries the virtual machines (VMs) that are added to a Service Mesh (ASM) instance.
        
        @param request: DescribeVMsInServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVMsInServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVMsInServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVMsInServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vms_in_service_mesh(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        """
        @deprecated OpenAPI DescribeVMsInServiceMesh is deprecated
        
        @summary Queries the virtual machines (VMs) that are added to a Service Mesh (ASM) instance.
        
        @param request: DescribeVMsInServiceMeshRequest
        @return: DescribeVMsInServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vms_in_service_mesh_with_options(request, runtime)

    async def describe_vms_in_service_mesh_async(
        self,
        request: servicemesh_20200111_models.DescribeVMsInServiceMeshRequest,
    ) -> servicemesh_20200111_models.DescribeVMsInServiceMeshResponse:
        """
        @deprecated OpenAPI DescribeVMsInServiceMesh is deprecated
        
        @summary Queries the virtual machines (VMs) that are added to a Service Mesh (ASM) instance.
        
        @param request: DescribeVMsInServiceMeshRequest
        @return: DescribeVMsInServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vms_in_service_mesh_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        """
        @summary Queries a list of vSwitches that are deployed in a specified virtual private cloud (VPC) in a region.
        
        @param request: DescribeVSwitchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVSwitchesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        """
        @summary Queries a list of vSwitches that are deployed in a specified virtual private cloud (VPC) in a region.
        
        @param request: DescribeVSwitchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVSwitchesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVSwitches',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitches(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        """
        @summary Queries a list of vSwitches that are deployed in a specified virtual private cloud (VPC) in a region.
        
        @param request: DescribeVSwitchesRequest
        @return: DescribeVSwitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: servicemesh_20200111_models.DescribeVSwitchesRequest,
    ) -> servicemesh_20200111_models.DescribeVSwitchesResponse:
        """
        @summary Queries a list of vSwitches that are deployed in a specified virtual private cloud (VPC) in a region.
        
        @param request: DescribeVSwitchesRequest
        @return: DescribeVSwitchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_versions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVersionsResponse:
        """
        @summary Queries available Service Mesh (ASM) versions when you create an ASM instance.
        
        @param request: DescribeVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVersionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVersions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_versions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVersionsResponse:
        """
        @summary Queries available Service Mesh (ASM) versions when you create an ASM instance.
        
        @param request: DescribeVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVersionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeVersions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_versions(self) -> servicemesh_20200111_models.DescribeVersionsResponse:
        """
        @summary Queries available Service Mesh (ASM) versions when you create an ASM instance.
        
        @return: DescribeVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_versions_with_options(runtime)

    async def describe_versions_async(self) -> servicemesh_20200111_models.DescribeVersionsResponse:
        """
        @summary Queries available Service Mesh (ASM) versions when you create an ASM instance.
        
        @return: DescribeVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_versions_with_options_async(runtime)

    def describe_vpcs_with_options(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        """
        @summary Queries the virtual private clouds (VPCs) that are available in a specified region.
        
        @param request: DescribeVpcsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpcs_with_options_async(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        """
        @summary Queries the virtual private clouds (VPCs) that are available in a specified region.
        
        @param request: DescribeVpcsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVpcsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVpcs',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpcs(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        """
        @summary Queries the virtual private clouds (VPCs) that are available in a specified region.
        
        @param request: DescribeVpcsRequest
        @return: DescribeVpcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    async def describe_vpcs_async(
        self,
        request: servicemesh_20200111_models.DescribeVpcsRequest,
    ) -> servicemesh_20200111_models.DescribeVpcsResponse:
        """
        @summary Queries the virtual private clouds (VPCs) that are available in a specified region.
        
        @param request: DescribeVpcsRequest
        @return: DescribeVpcsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpcs_with_options_async(request, runtime)

    def get_ca_cert_with_options(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        """
        @summary Obtains a certificate issued by a certificate authority (CA).
        
        @param request: GetCaCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCaCertResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCaCert',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetCaCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ca_cert_with_options_async(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        """
        @summary Obtains a certificate issued by a certificate authority (CA).
        
        @param request: GetCaCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCaCertResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCaCert',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetCaCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ca_cert(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        """
        @summary Obtains a certificate issued by a certificate authority (CA).
        
        @param request: GetCaCertRequest
        @return: GetCaCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ca_cert_with_options(request, runtime)

    async def get_ca_cert_async(
        self,
        request: servicemesh_20200111_models.GetCaCertRequest,
    ) -> servicemesh_20200111_models.GetCaCertResponse:
        """
        @summary Obtains a certificate issued by a certificate authority (CA).
        
        @param request: GetCaCertRequest
        @return: GetCaCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ca_cert_with_options_async(request, runtime)

    def get_deployment_by_selector_with_options(
        self,
        tmp_req: servicemesh_20200111_models.GetDeploymentBySelectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetDeploymentBySelectorResponse:
        """
        @summary Queries a list of workloads specified by a label selector.
        
        @param tmp_req: GetDeploymentBySelectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentBySelectorResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.GetDeploymentBySelectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'LabelSelector', 'json')
        body = {}
        if not UtilClient.is_unset(request.guest_cluster):
            body['GuestCluster'] = request.guest_cluster
        if not UtilClient.is_unset(request.label_selector_shrink):
            body['LabelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.mark):
            body['Mark'] = request.mark
        if not UtilClient.is_unset(request.name_space):
            body['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeploymentBySelector',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetDeploymentBySelectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_by_selector_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.GetDeploymentBySelectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetDeploymentBySelectorResponse:
        """
        @summary Queries a list of workloads specified by a label selector.
        
        @param tmp_req: GetDeploymentBySelectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeploymentBySelectorResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.GetDeploymentBySelectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_selector):
            request.label_selector_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_selector, 'LabelSelector', 'json')
        body = {}
        if not UtilClient.is_unset(request.guest_cluster):
            body['GuestCluster'] = request.guest_cluster
        if not UtilClient.is_unset(request.label_selector_shrink):
            body['LabelSelector'] = request.label_selector_shrink
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.mark):
            body['Mark'] = request.mark
        if not UtilClient.is_unset(request.name_space):
            body['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeploymentBySelector',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetDeploymentBySelectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment_by_selector(
        self,
        request: servicemesh_20200111_models.GetDeploymentBySelectorRequest,
    ) -> servicemesh_20200111_models.GetDeploymentBySelectorResponse:
        """
        @summary Queries a list of workloads specified by a label selector.
        
        @param request: GetDeploymentBySelectorRequest
        @return: GetDeploymentBySelectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_deployment_by_selector_with_options(request, runtime)

    async def get_deployment_by_selector_async(
        self,
        request: servicemesh_20200111_models.GetDeploymentBySelectorRequest,
    ) -> servicemesh_20200111_models.GetDeploymentBySelectorResponse:
        """
        @summary Queries a list of workloads specified by a label selector.
        
        @param request: GetDeploymentBySelectorRequest
        @return: GetDeploymentBySelectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_deployment_by_selector_with_options_async(request, runtime)

    def get_grafana_dashboard_url_with_options(
        self,
        request: servicemesh_20200111_models.GetGrafanaDashboardUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetGrafanaDashboardUrlResponse:
        """
        @summary Queries the Grafana dashboard URL from Application Real-Time Monitoring Service (ARMS).
        
        @param request: GetGrafanaDashboardUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGrafanaDashboardUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGrafanaDashboardUrl',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetGrafanaDashboardUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_grafana_dashboard_url_with_options_async(
        self,
        request: servicemesh_20200111_models.GetGrafanaDashboardUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetGrafanaDashboardUrlResponse:
        """
        @summary Queries the Grafana dashboard URL from Application Real-Time Monitoring Service (ARMS).
        
        @param request: GetGrafanaDashboardUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGrafanaDashboardUrlResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetGrafanaDashboardUrl',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetGrafanaDashboardUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_grafana_dashboard_url(
        self,
        request: servicemesh_20200111_models.GetGrafanaDashboardUrlRequest,
    ) -> servicemesh_20200111_models.GetGrafanaDashboardUrlResponse:
        """
        @summary Queries the Grafana dashboard URL from Application Real-Time Monitoring Service (ARMS).
        
        @param request: GetGrafanaDashboardUrlRequest
        @return: GetGrafanaDashboardUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_grafana_dashboard_url_with_options(request, runtime)

    async def get_grafana_dashboard_url_async(
        self,
        request: servicemesh_20200111_models.GetGrafanaDashboardUrlRequest,
    ) -> servicemesh_20200111_models.GetGrafanaDashboardUrlResponse:
        """
        @summary Queries the Grafana dashboard URL from Application Real-Time Monitoring Service (ARMS).
        
        @param request: GetGrafanaDashboardUrlRequest
        @return: GetGrafanaDashboardUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_grafana_dashboard_url_with_options_async(request, runtime)

    def get_registered_service_endpoints_with_options(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        """
        @summary 描述ServiceEndpoints信息
        
        @param request: GetRegisteredServiceEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegisteredServiceEndpointsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_ids):
            body['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceEndpoints',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registered_service_endpoints_with_options_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        """
        @summary 描述ServiceEndpoints信息
        
        @param request: GetRegisteredServiceEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegisteredServiceEndpointsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_ids):
            body['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceEndpoints',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registered_service_endpoints(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        """
        @summary 描述ServiceEndpoints信息
        
        @param request: GetRegisteredServiceEndpointsRequest
        @return: GetRegisteredServiceEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_registered_service_endpoints_with_options(request, runtime)

    async def get_registered_service_endpoints_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceEndpointsRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse:
        """
        @summary 描述ServiceEndpoints信息
        
        @param request: GetRegisteredServiceEndpointsRequest
        @return: GetRegisteredServiceEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_registered_service_endpoints_with_options_async(request, runtime)

    def get_registered_service_namespaces_with_options(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        """
        @param request: GetRegisteredServiceNamespacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegisteredServiceNamespacesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registered_service_namespaces_with_options_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        """
        @param request: GetRegisteredServiceNamespacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegisteredServiceNamespacesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRegisteredServiceNamespaces',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registered_service_namespaces(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        """
        @param request: GetRegisteredServiceNamespacesRequest
        @return: GetRegisteredServiceNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_registered_service_namespaces_with_options(request, runtime)

    async def get_registered_service_namespaces_async(
        self,
        request: servicemesh_20200111_models.GetRegisteredServiceNamespacesRequest,
    ) -> servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse:
        """
        @param request: GetRegisteredServiceNamespacesRequest
        @return: GetRegisteredServiceNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_registered_service_namespaces_with_options_async(request, runtime)

    def get_swim_lane_detail_with_options(
        self,
        request: servicemesh_20200111_models.GetSwimLaneDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneDetailResponse:
        """
        @summary Queries detailed information about a lane.
        
        @param request: GetSwimLaneDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSwimLaneDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_swim_lane_detail_with_options_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneDetailResponse:
        """
        @summary Queries detailed information about a lane.
        
        @param request: GetSwimLaneDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSwimLaneDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneDetail',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_swim_lane_detail(
        self,
        request: servicemesh_20200111_models.GetSwimLaneDetailRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneDetailResponse:
        """
        @summary Queries detailed information about a lane.
        
        @param request: GetSwimLaneDetailRequest
        @return: GetSwimLaneDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_swim_lane_detail_with_options(request, runtime)

    async def get_swim_lane_detail_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneDetailRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneDetailResponse:
        """
        @summary Queries detailed information about a lane.
        
        @param request: GetSwimLaneDetailRequest
        @return: GetSwimLaneDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_swim_lane_detail_with_options_async(request, runtime)

    def get_swim_lane_group_list_with_options(
        self,
        request: servicemesh_20200111_models.GetSwimLaneGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneGroupListResponse:
        """
        @summary Queries a list of all lane groups in an Alibaba Cloud Service Mesh (ASM) instance.
        
        @param request: GetSwimLaneGroupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSwimLaneGroupListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneGroupList',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_swim_lane_group_list_with_options_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneGroupListResponse:
        """
        @summary Queries a list of all lane groups in an Alibaba Cloud Service Mesh (ASM) instance.
        
        @param request: GetSwimLaneGroupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSwimLaneGroupListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneGroupList',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_swim_lane_group_list(
        self,
        request: servicemesh_20200111_models.GetSwimLaneGroupListRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneGroupListResponse:
        """
        @summary Queries a list of all lane groups in an Alibaba Cloud Service Mesh (ASM) instance.
        
        @param request: GetSwimLaneGroupListRequest
        @return: GetSwimLaneGroupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_swim_lane_group_list_with_options(request, runtime)

    async def get_swim_lane_group_list_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneGroupListRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneGroupListResponse:
        """
        @summary Queries a list of all lane groups in an Alibaba Cloud Service Mesh (ASM) instance.
        
        @param request: GetSwimLaneGroupListRequest
        @return: GetSwimLaneGroupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_swim_lane_group_list_with_options_async(request, runtime)

    def get_swim_lane_list_with_options(
        self,
        request: servicemesh_20200111_models.GetSwimLaneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneListResponse:
        """
        @summary Queries a list of all the lanes in a lane group.
        
        @param request: GetSwimLaneListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSwimLaneListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneList',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_swim_lane_list_with_options_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetSwimLaneListResponse:
        """
        @summary Queries a list of all the lanes in a lane group.
        
        @param request: GetSwimLaneListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSwimLaneListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwimLaneList',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSwimLaneListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_swim_lane_list(
        self,
        request: servicemesh_20200111_models.GetSwimLaneListRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneListResponse:
        """
        @summary Queries a list of all the lanes in a lane group.
        
        @param request: GetSwimLaneListRequest
        @return: GetSwimLaneListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_swim_lane_list_with_options(request, runtime)

    async def get_swim_lane_list_async(
        self,
        request: servicemesh_20200111_models.GetSwimLaneListRequest,
    ) -> servicemesh_20200111_models.GetSwimLaneListResponse:
        """
        @summary Queries a list of all the lanes in a lane group.
        
        @param request: GetSwimLaneListRequest
        @return: GetSwimLaneListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_swim_lane_list_with_options_async(request, runtime)

    def get_vm_app_mesh_info_with_options(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        """
        @deprecated OpenAPI GetVmAppMeshInfo is deprecated
        
        @summary Queries the information about VMs that are added to a Service Mesh (ASM) instance.
        
        @param request: GetVmAppMeshInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVmAppMeshInfoResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmAppMeshInfo',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmAppMeshInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vm_app_mesh_info_with_options_async(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        """
        @deprecated OpenAPI GetVmAppMeshInfo is deprecated
        
        @summary Queries the information about VMs that are added to a Service Mesh (ASM) instance.
        
        @param request: GetVmAppMeshInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVmAppMeshInfoResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmAppMeshInfo',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmAppMeshInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vm_app_mesh_info(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        """
        @deprecated OpenAPI GetVmAppMeshInfo is deprecated
        
        @summary Queries the information about VMs that are added to a Service Mesh (ASM) instance.
        
        @param request: GetVmAppMeshInfoRequest
        @return: GetVmAppMeshInfoResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vm_app_mesh_info_with_options(request, runtime)

    async def get_vm_app_mesh_info_async(
        self,
        request: servicemesh_20200111_models.GetVmAppMeshInfoRequest,
    ) -> servicemesh_20200111_models.GetVmAppMeshInfoResponse:
        """
        @deprecated OpenAPI GetVmAppMeshInfo is deprecated
        
        @summary Queries the information about VMs that are added to a Service Mesh (ASM) instance.
        
        @param request: GetVmAppMeshInfoRequest
        @return: GetVmAppMeshInfoResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vm_app_mesh_info_with_options_async(request, runtime)

    def get_vm_meta_with_options(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        """
        @deprecated OpenAPI GetVmMeta is deprecated
        
        @summary Queries the metadata that is required to add a non-containerized application to a Service Mesh (ASM) instance.
        
        @param request: GetVmMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVmMetaResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmMeta',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vm_meta_with_options_async(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        """
        @deprecated OpenAPI GetVmMeta is deprecated
        
        @summary Queries the metadata that is required to add a non-containerized application to a Service Mesh (ASM) instance.
        
        @param request: GetVmMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVmMetaResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVmMeta',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vm_meta(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        """
        @deprecated OpenAPI GetVmMeta is deprecated
        
        @summary Queries the metadata that is required to add a non-containerized application to a Service Mesh (ASM) instance.
        
        @param request: GetVmMetaRequest
        @return: GetVmMetaResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vm_meta_with_options(request, runtime)

    async def get_vm_meta_async(
        self,
        request: servicemesh_20200111_models.GetVmMetaRequest,
    ) -> servicemesh_20200111_models.GetVmMetaResponse:
        """
        @deprecated OpenAPI GetVmMeta is deprecated
        
        @summary Queries the metadata that is required to add a non-containerized application to a Service Mesh (ASM) instance.
        
        @param request: GetVmMetaRequest
        @return: GetVmMetaResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vm_meta_with_options_async(request, runtime)

    def grant_user_permissions_with_options(
        self,
        tmp_req: servicemesh_20200111_models.GrantUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GrantUserPermissionsResponse:
        """
        @summary Grants permissions to a Resource Access Management (RAM) user.
        
        @param tmp_req: GrantUserPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantUserPermissionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.GrantUserPermissionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_account_user_ids):
            request.sub_account_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_account_user_ids, 'SubAccountUserIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.permissions):
            body['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.sub_account_user_id):
            body['SubAccountUserId'] = request.sub_account_user_id
        if not UtilClient.is_unset(request.sub_account_user_ids_shrink):
            body['SubAccountUserIds'] = request.sub_account_user_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantUserPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GrantUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_user_permissions_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.GrantUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.GrantUserPermissionsResponse:
        """
        @summary Grants permissions to a Resource Access Management (RAM) user.
        
        @param tmp_req: GrantUserPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantUserPermissionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.GrantUserPermissionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_account_user_ids):
            request.sub_account_user_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_account_user_ids, 'SubAccountUserIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.permissions):
            body['Permissions'] = request.permissions
        if not UtilClient.is_unset(request.sub_account_user_id):
            body['SubAccountUserId'] = request.sub_account_user_id
        if not UtilClient.is_unset(request.sub_account_user_ids_shrink):
            body['SubAccountUserIds'] = request.sub_account_user_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantUserPermissions',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GrantUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_user_permissions(
        self,
        request: servicemesh_20200111_models.GrantUserPermissionsRequest,
    ) -> servicemesh_20200111_models.GrantUserPermissionsResponse:
        """
        @summary Grants permissions to a Resource Access Management (RAM) user.
        
        @param request: GrantUserPermissionsRequest
        @return: GrantUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_user_permissions_with_options(request, runtime)

    async def grant_user_permissions_async(
        self,
        request: servicemesh_20200111_models.GrantUserPermissionsRequest,
    ) -> servicemesh_20200111_models.GrantUserPermissionsResponse:
        """
        @summary Grants permissions to a Resource Access Management (RAM) user.
        
        @param request: GrantUserPermissionsRequest
        @return: GrantUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.grant_user_permissions_with_options_async(request, runtime)

    def list_service_accounts_with_options(
        self,
        request: servicemesh_20200111_models.ListServiceAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ListServiceAccountsResponse:
        """
        @summary 列举所有服务账号
        
        @param request: ListServiceAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceAccountsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceAccounts',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListServiceAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_accounts_with_options_async(
        self,
        request: servicemesh_20200111_models.ListServiceAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ListServiceAccountsResponse:
        """
        @summary 列举所有服务账号
        
        @param request: ListServiceAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceAccountsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceAccounts',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListServiceAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_accounts(
        self,
        request: servicemesh_20200111_models.ListServiceAccountsRequest,
    ) -> servicemesh_20200111_models.ListServiceAccountsResponse:
        """
        @summary 列举所有服务账号
        
        @param request: ListServiceAccountsRequest
        @return: ListServiceAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_accounts_with_options(request, runtime)

    async def list_service_accounts_async(
        self,
        request: servicemesh_20200111_models.ListServiceAccountsRequest,
    ) -> servicemesh_20200111_models.ListServiceAccountsResponse:
        """
        @summary 列举所有服务账号
        
        @param request: ListServiceAccountsRequest
        @return: ListServiceAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_accounts_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: servicemesh_20200111_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ListTagResourcesResponse:
        """
        @summary Queries user tags on a Service Mesh (ASM) instance.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: servicemesh_20200111_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ListTagResourcesResponse:
        """
        @summary Queries user tags on a Service Mesh (ASM) instance.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: servicemesh_20200111_models.ListTagResourcesRequest,
    ) -> servicemesh_20200111_models.ListTagResourcesResponse:
        """
        @summary Queries user tags on a Service Mesh (ASM) instance.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: servicemesh_20200111_models.ListTagResourcesRequest,
    ) -> servicemesh_20200111_models.ListTagResourcesResponse:
        """
        @summary Queries user tags on a Service Mesh (ASM) instance.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_waypoints_with_options(
        self,
        request: servicemesh_20200111_models.ListWaypointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ListWaypointsResponse:
        """
        @summary Queries the configurations of all waypoint proxies in a namespace of a cluster on the data plane.
        
        @param request: ListWaypointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWaypointsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.continue_):
            body['Continue'] = request.continue_
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWaypoints',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListWaypointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waypoints_with_options_async(
        self,
        request: servicemesh_20200111_models.ListWaypointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ListWaypointsResponse:
        """
        @summary Queries the configurations of all waypoint proxies in a namespace of a cluster on the data plane.
        
        @param request: ListWaypointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWaypointsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.continue_):
            body['Continue'] = request.continue_
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWaypoints',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListWaypointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waypoints(
        self,
        request: servicemesh_20200111_models.ListWaypointsRequest,
    ) -> servicemesh_20200111_models.ListWaypointsResponse:
        """
        @summary Queries the configurations of all waypoint proxies in a namespace of a cluster on the data plane.
        
        @param request: ListWaypointsRequest
        @return: ListWaypointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_waypoints_with_options(request, runtime)

    async def list_waypoints_async(
        self,
        request: servicemesh_20200111_models.ListWaypointsRequest,
    ) -> servicemesh_20200111_models.ListWaypointsResponse:
        """
        @summary Queries the configurations of all waypoint proxies in a namespace of a cluster on the data plane.
        
        @param request: ListWaypointsRequest
        @return: ListWaypointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_waypoints_with_options_async(request, runtime)

    def modify_api_server_eip_resource_with_options(
        self,
        request: servicemesh_20200111_models.ModifyApiServerEipResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyApiServerEipResourceResponse:
        """
        @summary ModifyApiServerEipResource
        
        @param request: ModifyApiServerEipResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyApiServerEipResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['ApiServerEipId'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApiServerEipResource',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyApiServerEipResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_api_server_eip_resource_with_options_async(
        self,
        request: servicemesh_20200111_models.ModifyApiServerEipResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyApiServerEipResourceResponse:
        """
        @summary ModifyApiServerEipResource
        
        @param request: ModifyApiServerEipResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyApiServerEipResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_server_eip_id):
            body['ApiServerEipId'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyApiServerEipResource',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyApiServerEipResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_api_server_eip_resource(
        self,
        request: servicemesh_20200111_models.ModifyApiServerEipResourceRequest,
    ) -> servicemesh_20200111_models.ModifyApiServerEipResourceResponse:
        """
        @summary ModifyApiServerEipResource
        
        @param request: ModifyApiServerEipResourceRequest
        @return: ModifyApiServerEipResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_api_server_eip_resource_with_options(request, runtime)

    async def modify_api_server_eip_resource_async(
        self,
        request: servicemesh_20200111_models.ModifyApiServerEipResourceRequest,
    ) -> servicemesh_20200111_models.ModifyApiServerEipResourceResponse:
        """
        @summary ModifyApiServerEipResource
        
        @param request: ModifyApiServerEipResourceRequest
        @return: ModifyApiServerEipResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_api_server_eip_resource_with_options_async(request, runtime)

    def modify_pilot_eip_resource_with_options(
        self,
        request: servicemesh_20200111_models.ModifyPilotEipResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyPilotEipResourceResponse:
        """
        @summary ModifyPilotEipResource
        
        @param request: ModifyPilotEipResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPilotEipResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.eip_id):
            body['EipId'] = request.eip_id
        if not UtilClient.is_unset(request.is_canary):
            body['IsCanary'] = request.is_canary
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPilotEipResource',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyPilotEipResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_pilot_eip_resource_with_options_async(
        self,
        request: servicemesh_20200111_models.ModifyPilotEipResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyPilotEipResourceResponse:
        """
        @summary ModifyPilotEipResource
        
        @param request: ModifyPilotEipResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPilotEipResourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.eip_id):
            body['EipId'] = request.eip_id
        if not UtilClient.is_unset(request.is_canary):
            body['IsCanary'] = request.is_canary
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPilotEipResource',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyPilotEipResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_pilot_eip_resource(
        self,
        request: servicemesh_20200111_models.ModifyPilotEipResourceRequest,
    ) -> servicemesh_20200111_models.ModifyPilotEipResourceResponse:
        """
        @summary ModifyPilotEipResource
        
        @param request: ModifyPilotEipResourceRequest
        @return: ModifyPilotEipResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_pilot_eip_resource_with_options(request, runtime)

    async def modify_pilot_eip_resource_async(
        self,
        request: servicemesh_20200111_models.ModifyPilotEipResourceRequest,
    ) -> servicemesh_20200111_models.ModifyPilotEipResourceResponse:
        """
        @summary ModifyPilotEipResource
        
        @param request: ModifyPilotEipResourceRequest
        @return: ModifyPilotEipResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_pilot_eip_resource_with_options_async(request, runtime)

    def modify_service_mesh_name_with_options(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        """
        @summary Modifies the name of a Service Mesh (ASM) instance.
        
        @param request: ModifyServiceMeshNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyServiceMeshNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyServiceMeshName',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyServiceMeshNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_service_mesh_name_with_options_async(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        """
        @summary Modifies the name of a Service Mesh (ASM) instance.
        
        @param request: ModifyServiceMeshNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyServiceMeshNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyServiceMeshName',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyServiceMeshNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_service_mesh_name(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        """
        @summary Modifies the name of a Service Mesh (ASM) instance.
        
        @param request: ModifyServiceMeshNameRequest
        @return: ModifyServiceMeshNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_service_mesh_name_with_options(request, runtime)

    async def modify_service_mesh_name_async(
        self,
        request: servicemesh_20200111_models.ModifyServiceMeshNameRequest,
    ) -> servicemesh_20200111_models.ModifyServiceMeshNameResponse:
        """
        @summary Modifies the name of a Service Mesh (ASM) instance.
        
        @param request: ModifyServiceMeshNameRequest
        @return: ModifyServiceMeshNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_service_mesh_name_with_options_async(request, runtime)

    def re_activate_audit_with_options(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        """
        @summary Recreates a project that is used to store audit logs. After mesh audit is enabled, if you delete the log project that stores audit logs by mistake, you can recreate a project for storing audit logs.
        
        @description Before you call this operation, make sure that you understand the billing methods of Simple Log Service. For more information, visit the [pricing page](https://www.alibabacloud.com/zh/pricing-calculator?_p_lc=1\\&spm=a2796.7960336.3034855210.1.44e6b91aaSp2M7#/commodity/vm_intl).
        
        @param request: ReActivateAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReActivateAuditResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReActivateAudit',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ReActivateAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def re_activate_audit_with_options_async(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        """
        @summary Recreates a project that is used to store audit logs. After mesh audit is enabled, if you delete the log project that stores audit logs by mistake, you can recreate a project for storing audit logs.
        
        @description Before you call this operation, make sure that you understand the billing methods of Simple Log Service. For more information, visit the [pricing page](https://www.alibabacloud.com/zh/pricing-calculator?_p_lc=1\\&spm=a2796.7960336.3034855210.1.44e6b91aaSp2M7#/commodity/vm_intl).
        
        @param request: ReActivateAuditRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReActivateAuditResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReActivateAudit',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ReActivateAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def re_activate_audit(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        """
        @summary Recreates a project that is used to store audit logs. After mesh audit is enabled, if you delete the log project that stores audit logs by mistake, you can recreate a project for storing audit logs.
        
        @description Before you call this operation, make sure that you understand the billing methods of Simple Log Service. For more information, visit the [pricing page](https://www.alibabacloud.com/zh/pricing-calculator?_p_lc=1\\&spm=a2796.7960336.3034855210.1.44e6b91aaSp2M7#/commodity/vm_intl).
        
        @param request: ReActivateAuditRequest
        @return: ReActivateAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.re_activate_audit_with_options(request, runtime)

    async def re_activate_audit_async(
        self,
        request: servicemesh_20200111_models.ReActivateAuditRequest,
    ) -> servicemesh_20200111_models.ReActivateAuditResponse:
        """
        @summary Recreates a project that is used to store audit logs. After mesh audit is enabled, if you delete the log project that stores audit logs by mistake, you can recreate a project for storing audit logs.
        
        @description Before you call this operation, make sure that you understand the billing methods of Simple Log Service. For more information, visit the [pricing page](https://www.alibabacloud.com/zh/pricing-calculator?_p_lc=1\\&spm=a2796.7960336.3034855210.1.44e6b91aaSp2M7#/commodity/vm_intl).
        
        @param request: ReActivateAuditRequest
        @return: ReActivateAuditResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.re_activate_audit_with_options_async(request, runtime)

    def remove_cluster_from_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        """
        @summary Removes a cluster from a Service Mesh (ASM) instance.
        
        @param request: RemoveClusterFromServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveClusterFromServiceMeshResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.reserve_namespace):
            body['ReserveNamespace'] = request.reserve_namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveClusterFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cluster_from_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        """
        @summary Removes a cluster from a Service Mesh (ASM) instance.
        
        @param request: RemoveClusterFromServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveClusterFromServiceMeshResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.reserve_namespace):
            body['ReserveNamespace'] = request.reserve_namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveClusterFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cluster_from_service_mesh(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        """
        @summary Removes a cluster from a Service Mesh (ASM) instance.
        
        @param request: RemoveClusterFromServiceMeshRequest
        @return: RemoveClusterFromServiceMeshResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_cluster_from_service_mesh_with_options(request, runtime)

    async def remove_cluster_from_service_mesh_async(
        self,
        request: servicemesh_20200111_models.RemoveClusterFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse:
        """
        @summary Removes a cluster from a Service Mesh (ASM) instance.
        
        @param request: RemoveClusterFromServiceMeshRequest
        @return: RemoveClusterFromServiceMeshResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_cluster_from_service_mesh_with_options_async(request, runtime)

    def remove_vmfrom_service_mesh_with_options(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        """
        @deprecated OpenAPI RemoveVMFromServiceMesh is deprecated
        
        @summary Removes a virtual machine (VM) from a Service Mesh (ASM) instance.
        
        @param request: RemoveVMFromServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveVMFromServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVMFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveVMFromServiceMeshResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_vmfrom_service_mesh_with_options_async(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        """
        @deprecated OpenAPI RemoveVMFromServiceMesh is deprecated
        
        @summary Removes a virtual machine (VM) from a Service Mesh (ASM) instance.
        
        @param request: RemoveVMFromServiceMeshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveVMFromServiceMeshResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ecs_id):
            query['EcsId'] = request.ecs_id
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVMFromServiceMesh',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveVMFromServiceMeshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_vmfrom_service_mesh(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        """
        @deprecated OpenAPI RemoveVMFromServiceMesh is deprecated
        
        @summary Removes a virtual machine (VM) from a Service Mesh (ASM) instance.
        
        @param request: RemoveVMFromServiceMeshRequest
        @return: RemoveVMFromServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_vmfrom_service_mesh_with_options(request, runtime)

    async def remove_vmfrom_service_mesh_async(
        self,
        request: servicemesh_20200111_models.RemoveVMFromServiceMeshRequest,
    ) -> servicemesh_20200111_models.RemoveVMFromServiceMeshResponse:
        """
        @deprecated OpenAPI RemoveVMFromServiceMesh is deprecated
        
        @summary Removes a virtual machine (VM) from a Service Mesh (ASM) instance.
        
        @param request: RemoveVMFromServiceMeshRequest
        @return: RemoveVMFromServiceMeshResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_vmfrom_service_mesh_with_options_async(request, runtime)

    def revoke_kubeconfig_with_options(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        """
        @summary Revokes the kubeconfig file of a Service Mesh (ASM) instance and generates a new kubeconfig file.
        
        @param request: RevokeKubeconfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeKubeconfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RevokeKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_kubeconfig_with_options_async(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        """
        @summary Revokes the kubeconfig file of a Service Mesh (ASM) instance and generates a new kubeconfig file.
        
        @param request: RevokeKubeconfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeKubeconfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.private_ip_address):
            body['PrivateIpAddress'] = request.private_ip_address
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeKubeconfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RevokeKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_kubeconfig(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        """
        @summary Revokes the kubeconfig file of a Service Mesh (ASM) instance and generates a new kubeconfig file.
        
        @param request: RevokeKubeconfigRequest
        @return: RevokeKubeconfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_kubeconfig_with_options(request, runtime)

    async def revoke_kubeconfig_async(
        self,
        request: servicemesh_20200111_models.RevokeKubeconfigRequest,
    ) -> servicemesh_20200111_models.RevokeKubeconfigResponse:
        """
        @summary Revokes the kubeconfig file of a Service Mesh (ASM) instance and generates a new kubeconfig file.
        
        @param request: RevokeKubeconfigRequest
        @return: RevokeKubeconfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_kubeconfig_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: servicemesh_20200111_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.TagResourcesResponse:
        """
        @summary Adds or modifies user tags on a resource.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: servicemesh_20200111_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.TagResourcesResponse:
        """
        @summary Adds or modifies user tags on a resource.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: servicemesh_20200111_models.TagResourcesRequest,
    ) -> servicemesh_20200111_models.TagResourcesResponse:
        """
        @summary Adds or modifies user tags on a resource.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: servicemesh_20200111_models.TagResourcesRequest,
    ) -> servicemesh_20200111_models.TagResourcesResponse:
        """
        @summary Adds or modifies user tags on a resource.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: servicemesh_20200111_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UntagResourcesResponse:
        """
        @summary Deletes user tags on a Service Mesh (ASM) instance.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: servicemesh_20200111_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UntagResourcesResponse:
        """
        @summary Deletes user tags on a Service Mesh (ASM) instance.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: servicemesh_20200111_models.UntagResourcesRequest,
    ) -> servicemesh_20200111_models.UntagResourcesResponse:
        """
        @summary Deletes user tags on a Service Mesh (ASM) instance.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: servicemesh_20200111_models.UntagResourcesRequest,
    ) -> servicemesh_20200111_models.UntagResourcesResponse:
        """
        @summary Deletes user tags on a Service Mesh (ASM) instance.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_asmgateway_with_options(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMGatewayResponse:
        """
        @summary Updates a Service Mesh (ASM) gateway.
        
        @param request: UpdateASMGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateASMGatewayResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMGateway',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asmgateway_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMGatewayResponse:
        """
        @summary Updates a Service Mesh (ASM) gateway.
        
        @param request: UpdateASMGatewayRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateASMGatewayResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMGateway',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_asmgateway(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayRequest,
    ) -> servicemesh_20200111_models.UpdateASMGatewayResponse:
        """
        @summary Updates a Service Mesh (ASM) gateway.
        
        @param request: UpdateASMGatewayRequest
        @return: UpdateASMGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_asmgateway_with_options(request, runtime)

    async def update_asmgateway_async(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayRequest,
    ) -> servicemesh_20200111_models.UpdateASMGatewayResponse:
        """
        @summary Updates a Service Mesh (ASM) gateway.
        
        @param request: UpdateASMGatewayRequest
        @return: UpdateASMGatewayResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_asmgateway_with_options_async(request, runtime)

    def update_asmgateway_imported_services_with_options(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayImportedServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse:
        """
        @summary Updates imported services on a Service Mesh (ASM) gateway to import or delete upstream services associated with the gateway.
        
        @param request: UpdateASMGatewayImportedServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateASMGatewayImportedServicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_names):
            body['ServiceNames'] = request.service_names
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMGatewayImportedServices',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asmgateway_imported_services_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayImportedServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse:
        """
        @summary Updates imported services on a Service Mesh (ASM) gateway to import or delete upstream services associated with the gateway.
        
        @param request: UpdateASMGatewayImportedServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateASMGatewayImportedServicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_name):
            body['ASMGatewayName'] = request.asmgateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.service_names):
            body['ServiceNames'] = request.service_names
        if not UtilClient.is_unset(request.service_namespace):
            body['ServiceNamespace'] = request.service_namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMGatewayImportedServices',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_asmgateway_imported_services(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayImportedServicesRequest,
    ) -> servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse:
        """
        @summary Updates imported services on a Service Mesh (ASM) gateway to import or delete upstream services associated with the gateway.
        
        @param request: UpdateASMGatewayImportedServicesRequest
        @return: UpdateASMGatewayImportedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_asmgateway_imported_services_with_options(request, runtime)

    async def update_asmgateway_imported_services_async(
        self,
        request: servicemesh_20200111_models.UpdateASMGatewayImportedServicesRequest,
    ) -> servicemesh_20200111_models.UpdateASMGatewayImportedServicesResponse:
        """
        @summary Updates imported services on a Service Mesh (ASM) gateway to import or delete upstream services associated with the gateway.
        
        @param request: UpdateASMGatewayImportedServicesRequest
        @return: UpdateASMGatewayImportedServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_asmgateway_imported_services_with_options_async(request, runtime)

    def update_asmnamespace_from_guest_cluster_with_options(
        self,
        request: servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse:
        """
        @summary Synchronizes namespaces of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: UpdateASMNamespaceFromGuestClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateASMNamespaceFromGuestClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMNamespaceFromGuestCluster',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asmnamespace_from_guest_cluster_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse:
        """
        @summary Synchronizes namespaces of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: UpdateASMNamespaceFromGuestClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateASMNamespaceFromGuestClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.k_8s_cluster_id):
            body['K8sClusterId'] = request.k_8s_cluster_id
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateASMNamespaceFromGuestCluster',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_asmnamespace_from_guest_cluster(
        self,
        request: servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterRequest,
    ) -> servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse:
        """
        @summary Synchronizes namespaces of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: UpdateASMNamespaceFromGuestClusterRequest
        @return: UpdateASMNamespaceFromGuestClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_asmnamespace_from_guest_cluster_with_options(request, runtime)

    async def update_asmnamespace_from_guest_cluster_async(
        self,
        request: servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterRequest,
    ) -> servicemesh_20200111_models.UpdateASMNamespaceFromGuestClusterResponse:
        """
        @summary Synchronizes namespaces of a Kubernetes cluster that is added to a Service Mesh (ASM) instance.
        
        @param request: UpdateASMNamespaceFromGuestClusterRequest
        @return: UpdateASMNamespaceFromGuestClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_asmnamespace_from_guest_cluster_with_options_async(request, runtime)

    def update_control_plane_log_config_with_options(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse:
        """
        @summary Modifies the configuration for collecting control plane logs.
        
        @param request: UpdateControlPlaneLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateControlPlaneLogConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.log_ttlin_day):
            body['LogTTLInDay'] = request.log_ttlin_day
        if not UtilClient.is_unset(request.project):
            body['Project'] = request.project
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateControlPlaneLogConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_control_plane_log_config_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse:
        """
        @summary Modifies the configuration for collecting control plane logs.
        
        @param request: UpdateControlPlaneLogConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateControlPlaneLogConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.log_ttlin_day):
            body['LogTTLInDay'] = request.log_ttlin_day
        if not UtilClient.is_unset(request.project):
            body['Project'] = request.project
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateControlPlaneLogConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_control_plane_log_config(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogConfigRequest,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse:
        """
        @summary Modifies the configuration for collecting control plane logs.
        
        @param request: UpdateControlPlaneLogConfigRequest
        @return: UpdateControlPlaneLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_control_plane_log_config_with_options(request, runtime)

    async def update_control_plane_log_config_async(
        self,
        request: servicemesh_20200111_models.UpdateControlPlaneLogConfigRequest,
    ) -> servicemesh_20200111_models.UpdateControlPlaneLogConfigResponse:
        """
        @summary Modifies the configuration for collecting control plane logs.
        
        @param request: UpdateControlPlaneLogConfigRequest
        @return: UpdateControlPlaneLogConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_control_plane_log_config_with_options_async(request, runtime)

    def update_guest_cluster_config_with_options(
        self,
        request: servicemesh_20200111_models.UpdateGuestClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateGuestClusterConfigResponse:
        """
        @summary 更新Guest Cluster配置
        
        @param request: UpdateGuestClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGuestClusterConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterId'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.smcenabled):
            body['SMCEnabled'] = request.smcenabled
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGuestClusterConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateGuestClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_guest_cluster_config_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateGuestClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateGuestClusterConfigResponse:
        """
        @summary 更新Guest Cluster配置
        
        @param request: UpdateGuestClusterConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGuestClusterConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.guest_cluster_id):
            body['GuestClusterId'] = request.guest_cluster_id
        if not UtilClient.is_unset(request.smcenabled):
            body['SMCEnabled'] = request.smcenabled
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGuestClusterConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateGuestClusterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_guest_cluster_config(
        self,
        request: servicemesh_20200111_models.UpdateGuestClusterConfigRequest,
    ) -> servicemesh_20200111_models.UpdateGuestClusterConfigResponse:
        """
        @summary 更新Guest Cluster配置
        
        @param request: UpdateGuestClusterConfigRequest
        @return: UpdateGuestClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_guest_cluster_config_with_options(request, runtime)

    async def update_guest_cluster_config_async(
        self,
        request: servicemesh_20200111_models.UpdateGuestClusterConfigRequest,
    ) -> servicemesh_20200111_models.UpdateGuestClusterConfigResponse:
        """
        @summary 更新Guest Cluster配置
        
        @param request: UpdateGuestClusterConfigRequest
        @return: UpdateGuestClusterConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_guest_cluster_config_with_options_async(request, runtime)

    def update_istio_gateway_routes_with_options(
        self,
        tmp_req: servicemesh_20200111_models.UpdateIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse:
        """
        @summary Updates a routing rule for a Service Mesh (ASM) gateway.
        
        @param tmp_req: UpdateIstioGatewayRoutesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIstioGatewayRoutesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.UpdateIstioGatewayRoutesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_route):
            request.gateway_route_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_route, 'GatewayRoute', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_route_shrink):
            body['GatewayRoute'] = request.gateway_route_shrink
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_istio_gateway_routes_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.UpdateIstioGatewayRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse:
        """
        @summary Updates a routing rule for a Service Mesh (ASM) gateway.
        
        @param tmp_req: UpdateIstioGatewayRoutesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIstioGatewayRoutesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.UpdateIstioGatewayRoutesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_route):
            request.gateway_route_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.gateway_route, 'GatewayRoute', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.gateway_route_shrink):
            body['GatewayRoute'] = request.gateway_route_shrink
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioGatewayRoutes',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_istio_gateway_routes(
        self,
        request: servicemesh_20200111_models.UpdateIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse:
        """
        @summary Updates a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: UpdateIstioGatewayRoutesRequest
        @return: UpdateIstioGatewayRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_istio_gateway_routes_with_options(request, runtime)

    async def update_istio_gateway_routes_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioGatewayRoutesRequest,
    ) -> servicemesh_20200111_models.UpdateIstioGatewayRoutesResponse:
        """
        @summary Updates a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: UpdateIstioGatewayRoutesRequest
        @return: UpdateIstioGatewayRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_istio_gateway_routes_with_options_async(request, runtime)

    def update_istio_injection_config_with_options(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        """
        @param request: UpdateIstioInjectionConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIstioInjectionConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_plane_mode):
            body['DataPlaneMode'] = request.data_plane_mode
        if not UtilClient.is_unset(request.enable_istio_injection):
            body['EnableIstioInjection'] = request.enable_istio_injection
        if not UtilClient.is_unset(request.enable_sidecar_set_injection):
            body['EnableSidecarSetInjection'] = request.enable_sidecar_set_injection
        if not UtilClient.is_unset(request.istio_rev):
            body['IstioRev'] = request.istio_rev
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioInjectionConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioInjectionConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_istio_injection_config_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        """
        @param request: UpdateIstioInjectionConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIstioInjectionConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_plane_mode):
            body['DataPlaneMode'] = request.data_plane_mode
        if not UtilClient.is_unset(request.enable_istio_injection):
            body['EnableIstioInjection'] = request.enable_istio_injection
        if not UtilClient.is_unset(request.enable_sidecar_set_injection):
            body['EnableSidecarSetInjection'] = request.enable_sidecar_set_injection
        if not UtilClient.is_unset(request.istio_rev):
            body['IstioRev'] = request.istio_rev
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioInjectionConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioInjectionConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_istio_injection_config(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        """
        @param request: UpdateIstioInjectionConfigRequest
        @return: UpdateIstioInjectionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_istio_injection_config_with_options(request, runtime)

    async def update_istio_injection_config_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioInjectionConfigRequest,
    ) -> servicemesh_20200111_models.UpdateIstioInjectionConfigResponse:
        """
        @param request: UpdateIstioInjectionConfigRequest
        @return: UpdateIstioInjectionConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_istio_injection_config_with_options_async(request, runtime)

    def update_istio_route_additional_status_with_options(
        self,
        request: servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse:
        """
        @summary Updates the information about a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: UpdateIstioRouteAdditionalStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIstioRouteAdditionalStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.route_name):
            query['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioRouteAdditionalStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_istio_route_additional_status_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse:
        """
        @summary Updates the information about a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: UpdateIstioRouteAdditionalStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIstioRouteAdditionalStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.route_name):
            query['RouteName'] = request.route_name
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.istio_gateway_name):
            body['IstioGatewayName'] = request.istio_gateway_name
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIstioRouteAdditionalStatus',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_istio_route_additional_status(
        self,
        request: servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusRequest,
    ) -> servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse:
        """
        @summary Updates the information about a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: UpdateIstioRouteAdditionalStatusRequest
        @return: UpdateIstioRouteAdditionalStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_istio_route_additional_status_with_options(request, runtime)

    async def update_istio_route_additional_status_async(
        self,
        request: servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusRequest,
    ) -> servicemesh_20200111_models.UpdateIstioRouteAdditionalStatusResponse:
        """
        @summary Updates the information about a routing rule for a Service Mesh (ASM) gateway.
        
        @param request: UpdateIstioRouteAdditionalStatusRequest
        @return: UpdateIstioRouteAdditionalStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_istio_route_additional_status_with_options_async(request, runtime)

    def update_mesh_craggregation_with_options(
        self,
        request: servicemesh_20200111_models.UpdateMeshCRAggregationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshCRAggregationResponse:
        """
        @summary Updates the settings of whether to enable the Kubernetes API on the data plane to access Istio resources.
        
        @param request: UpdateMeshCRAggregationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMeshCRAggregationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpulimit):
            body['CPULimit'] = request.cpulimit
        if not UtilClient.is_unset(request.cpurequirement):
            body['CPURequirement'] = request.cpurequirement
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.memory_limit):
            body['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.memory_requirement):
            body['MemoryRequirement'] = request.memory_requirement
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.use_public_api_server):
            body['UsePublicApiServer'] = request.use_public_api_server
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshCRAggregation',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshCRAggregationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mesh_craggregation_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshCRAggregationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshCRAggregationResponse:
        """
        @summary Updates the settings of whether to enable the Kubernetes API on the data plane to access Istio resources.
        
        @param request: UpdateMeshCRAggregationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMeshCRAggregationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cpulimit):
            body['CPULimit'] = request.cpulimit
        if not UtilClient.is_unset(request.cpurequirement):
            body['CPURequirement'] = request.cpurequirement
        if not UtilClient.is_unset(request.enabled):
            body['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.memory_limit):
            body['MemoryLimit'] = request.memory_limit
        if not UtilClient.is_unset(request.memory_requirement):
            body['MemoryRequirement'] = request.memory_requirement
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.use_public_api_server):
            body['UsePublicApiServer'] = request.use_public_api_server
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshCRAggregation',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshCRAggregationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mesh_craggregation(
        self,
        request: servicemesh_20200111_models.UpdateMeshCRAggregationRequest,
    ) -> servicemesh_20200111_models.UpdateMeshCRAggregationResponse:
        """
        @summary Updates the settings of whether to enable the Kubernetes API on the data plane to access Istio resources.
        
        @param request: UpdateMeshCRAggregationRequest
        @return: UpdateMeshCRAggregationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_mesh_craggregation_with_options(request, runtime)

    async def update_mesh_craggregation_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshCRAggregationRequest,
    ) -> servicemesh_20200111_models.UpdateMeshCRAggregationResponse:
        """
        @summary Updates the settings of whether to enable the Kubernetes API on the data plane to access Istio resources.
        
        @param request: UpdateMeshCRAggregationRequest
        @return: UpdateMeshCRAggregationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_mesh_craggregation_with_options_async(request, runtime)

    def update_mesh_feature_with_options(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        """
        @summary Updates the configuration of a Service Mesh (ASM) instance.
        
        @param request: UpdateMeshFeatureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMeshFeatureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_log_gateway_enabled):
            query['AccessLogGatewayEnabled'] = request.access_log_gateway_enabled
        if not UtilClient.is_unset(request.access_log_sidecar_enabled):
            query['AccessLogSidecarEnabled'] = request.access_log_sidecar_enabled
        if not UtilClient.is_unset(request.labels_for_offloaded_workloads):
            query['LabelsForOffloadedWorkloads'] = request.labels_for_offloaded_workloads
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_gateway_lifecycle):
            body['AccessLogGatewayLifecycle'] = request.access_log_gateway_lifecycle
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.access_log_sidecar_lifecycle):
            body['AccessLogSidecarLifecycle'] = request.access_log_sidecar_lifecycle
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.auto_injection_policy_enabled):
            body['AutoInjectionPolicyEnabled'] = request.auto_injection_policy_enabled
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.cert_chain):
            body['CertChain'] = request.cert_chain
        if not UtilClient.is_unset(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cni_enabled):
            body['CniEnabled'] = request.cni_enabled
        if not UtilClient.is_unset(request.cni_exclude_namespaces):
            body['CniExcludeNamespaces'] = request.cni_exclude_namespaces
        if not UtilClient.is_unset(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.default_components_schedule_config):
            body['DefaultComponentsScheduleConfig'] = request.default_components_schedule_config
        if not UtilClient.is_unset(request.discovery_selectors):
            body['DiscoverySelectors'] = request.discovery_selectors
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_auto_diagnosis):
            body['EnableAutoDiagnosis'] = request.enable_auto_diagnosis
        if not UtilClient.is_unset(request.enable_bootstrap_xds_agent):
            body['EnableBootstrapXdsAgent'] = request.enable_bootstrap_xds_agent
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_namespaces_by_default):
            body['EnableNamespacesByDefault'] = request.enable_namespaces_by_default
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.existing_ca_cert):
            body['ExistingCaCert'] = request.existing_ca_cert
        if not UtilClient.is_unset(request.existing_ca_key):
            body['ExistingCaKey'] = request.existing_ca_key
        if not UtilClient.is_unset(request.existing_root_ca_cert):
            body['ExistingRootCaCert'] = request.existing_root_ca_cert
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.hold_application_until_proxy_starts):
            body['HoldApplicationUntilProxyStarts'] = request.hold_application_until_proxy_starts
        if not UtilClient.is_unset(request.http_10enabled):
            body['Http10Enabled'] = request.http_10enabled
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.include_outbound_ports):
            body['IncludeOutboundPorts'] = request.include_outbound_ports
        if not UtilClient.is_unset(request.integrate_kiali):
            body['IntegrateKiali'] = request.integrate_kiali
        if not UtilClient.is_unset(request.interception_mode):
            body['InterceptionMode'] = request.interception_mode
        if not UtilClient.is_unset(request.kiali_arms_auth_tokens):
            body['KialiArmsAuthTokens'] = request.kiali_arms_auth_tokens
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.kiali_service_annotations):
            body['KialiServiceAnnotations'] = request.kiali_service_annotations
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.log_level):
            body['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.multi_buffer_enabled):
            body['MultiBufferEnabled'] = request.multi_buffer_enabled
        if not UtilClient.is_unset(request.multi_buffer_poll_delay):
            body['MultiBufferPollDelay'] = request.multi_buffer_poll_delay
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.nfdenabled):
            body['NFDEnabled'] = request.nfdenabled
        if not UtilClient.is_unset(request.nfdlabel_pruned):
            body['NFDLabelPruned'] = request.nfdlabel_pruned
        if not UtilClient.is_unset(request.opainjector_cpulimit):
            body['OPAInjectorCPULimit'] = request.opainjector_cpulimit
        if not UtilClient.is_unset(request.opainjector_cpurequirement):
            body['OPAInjectorCPURequirement'] = request.opainjector_cpurequirement
        if not UtilClient.is_unset(request.opainjector_memory_limit):
            body['OPAInjectorMemoryLimit'] = request.opainjector_memory_limit
        if not UtilClient.is_unset(request.opainjector_memory_requirement):
            body['OPAInjectorMemoryRequirement'] = request.opainjector_memory_requirement
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opascope_injected):
            body['OPAScopeInjected'] = request.opascope_injected
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.outbound_traffic_policy):
            body['OutboundTrafficPolicy'] = request.outbound_traffic_policy
        if not UtilClient.is_unset(request.pilot_enable_quic_listeners):
            body['PilotEnableQuicListeners'] = request.pilot_enable_quic_listeners
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.proxy_stats_matcher):
            body['ProxyStatsMatcher'] = request.proxy_stats_matcher
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.smcenabled):
            body['SMCEnabled'] = request.smcenabled
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_injector_limit_cpu):
            body['SidecarInjectorLimitCPU'] = request.sidecar_injector_limit_cpu
        if not UtilClient.is_unset(request.sidecar_injector_limit_memory):
            body['SidecarInjectorLimitMemory'] = request.sidecar_injector_limit_memory
        if not UtilClient.is_unset(request.sidecar_injector_request_cpu):
            body['SidecarInjectorRequestCPU'] = request.sidecar_injector_request_cpu
        if not UtilClient.is_unset(request.sidecar_injector_request_memory):
            body['SidecarInjectorRequestMemory'] = request.sidecar_injector_request_memory
        if not UtilClient.is_unset(request.sidecar_injector_webhook_as_yaml):
            body['SidecarInjectorWebhookAsYaml'] = request.sidecar_injector_webhook_as_yaml
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_custom_tags):
            body['TraceCustomTags'] = request.trace_custom_tags
        if not UtilClient.is_unset(request.trace_max_path_tag_length):
            body['TraceMaxPathTagLength'] = request.trace_max_path_tag_length
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_limit_cpu):
            body['TracingOnExtZipkinLimitCPU'] = request.tracing_on_ext_zipkin_limit_cpu
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_limit_memory):
            body['TracingOnExtZipkinLimitMemory'] = request.tracing_on_ext_zipkin_limit_memory
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_replica_count):
            body['TracingOnExtZipkinReplicaCount'] = request.tracing_on_ext_zipkin_replica_count
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_request_cpu):
            body['TracingOnExtZipkinRequestCPU'] = request.tracing_on_ext_zipkin_request_cpu
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_request_memory):
            body['TracingOnExtZipkinRequestMemory'] = request.tracing_on_ext_zipkin_request_memory
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshFeature',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mesh_feature_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        """
        @summary Updates the configuration of a Service Mesh (ASM) instance.
        
        @param request: UpdateMeshFeatureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMeshFeatureResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_log_gateway_enabled):
            query['AccessLogGatewayEnabled'] = request.access_log_gateway_enabled
        if not UtilClient.is_unset(request.access_log_sidecar_enabled):
            query['AccessLogSidecarEnabled'] = request.access_log_sidecar_enabled
        if not UtilClient.is_unset(request.labels_for_offloaded_workloads):
            query['LabelsForOffloadedWorkloads'] = request.labels_for_offloaded_workloads
        body = {}
        if not UtilClient.is_unset(request.access_log_enabled):
            body['AccessLogEnabled'] = request.access_log_enabled
        if not UtilClient.is_unset(request.access_log_file):
            body['AccessLogFile'] = request.access_log_file
        if not UtilClient.is_unset(request.access_log_format):
            body['AccessLogFormat'] = request.access_log_format
        if not UtilClient.is_unset(request.access_log_gateway_lifecycle):
            body['AccessLogGatewayLifecycle'] = request.access_log_gateway_lifecycle
        if not UtilClient.is_unset(request.access_log_project):
            body['AccessLogProject'] = request.access_log_project
        if not UtilClient.is_unset(request.access_log_service_enabled):
            body['AccessLogServiceEnabled'] = request.access_log_service_enabled
        if not UtilClient.is_unset(request.access_log_service_host):
            body['AccessLogServiceHost'] = request.access_log_service_host
        if not UtilClient.is_unset(request.access_log_service_port):
            body['AccessLogServicePort'] = request.access_log_service_port
        if not UtilClient.is_unset(request.access_log_sidecar_lifecycle):
            body['AccessLogSidecarLifecycle'] = request.access_log_sidecar_lifecycle
        if not UtilClient.is_unset(request.audit_project):
            body['AuditProject'] = request.audit_project
        if not UtilClient.is_unset(request.auto_injection_policy_enabled):
            body['AutoInjectionPolicyEnabled'] = request.auto_injection_policy_enabled
        if not UtilClient.is_unset(request.craggregation_enabled):
            body['CRAggregationEnabled'] = request.craggregation_enabled
        if not UtilClient.is_unset(request.cert_chain):
            body['CertChain'] = request.cert_chain
        if not UtilClient.is_unset(request.cluster_spec):
            body['ClusterSpec'] = request.cluster_spec
        if not UtilClient.is_unset(request.cni_enabled):
            body['CniEnabled'] = request.cni_enabled
        if not UtilClient.is_unset(request.cni_exclude_namespaces):
            body['CniExcludeNamespaces'] = request.cni_exclude_namespaces
        if not UtilClient.is_unset(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.config_source_enabled):
            body['ConfigSourceEnabled'] = request.config_source_enabled
        if not UtilClient.is_unset(request.config_source_nacos_id):
            body['ConfigSourceNacosID'] = request.config_source_nacos_id
        if not UtilClient.is_unset(request.customized_prometheus):
            body['CustomizedPrometheus'] = request.customized_prometheus
        if not UtilClient.is_unset(request.customized_zipkin):
            body['CustomizedZipkin'] = request.customized_zipkin
        if not UtilClient.is_unset(request.dnsproxying_enabled):
            body['DNSProxyingEnabled'] = request.dnsproxying_enabled
        if not UtilClient.is_unset(request.default_components_schedule_config):
            body['DefaultComponentsScheduleConfig'] = request.default_components_schedule_config
        if not UtilClient.is_unset(request.discovery_selectors):
            body['DiscoverySelectors'] = request.discovery_selectors
        if not UtilClient.is_unset(request.dubbo_filter_enabled):
            body['DubboFilterEnabled'] = request.dubbo_filter_enabled
        if not UtilClient.is_unset(request.enable_audit):
            body['EnableAudit'] = request.enable_audit
        if not UtilClient.is_unset(request.enable_auto_diagnosis):
            body['EnableAutoDiagnosis'] = request.enable_auto_diagnosis
        if not UtilClient.is_unset(request.enable_bootstrap_xds_agent):
            body['EnableBootstrapXdsAgent'] = request.enable_bootstrap_xds_agent
        if not UtilClient.is_unset(request.enable_crhistory):
            body['EnableCRHistory'] = request.enable_crhistory
        if not UtilClient.is_unset(request.enable_namespaces_by_default):
            body['EnableNamespacesByDefault'] = request.enable_namespaces_by_default
        if not UtilClient.is_unset(request.enable_sdsserver):
            body['EnableSDSServer'] = request.enable_sdsserver
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.existing_ca_cert):
            body['ExistingCaCert'] = request.existing_ca_cert
        if not UtilClient.is_unset(request.existing_ca_key):
            body['ExistingCaKey'] = request.existing_ca_key
        if not UtilClient.is_unset(request.existing_root_ca_cert):
            body['ExistingRootCaCert'] = request.existing_root_ca_cert
        if not UtilClient.is_unset(request.filter_gateway_cluster_config):
            body['FilterGatewayClusterConfig'] = request.filter_gateway_cluster_config
        if not UtilClient.is_unset(request.gateway_apienabled):
            body['GatewayAPIEnabled'] = request.gateway_apienabled
        if not UtilClient.is_unset(request.hold_application_until_proxy_starts):
            body['HoldApplicationUntilProxyStarts'] = request.hold_application_until_proxy_starts
        if not UtilClient.is_unset(request.http_10enabled):
            body['Http10Enabled'] = request.http_10enabled
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.include_outbound_ports):
            body['IncludeOutboundPorts'] = request.include_outbound_ports
        if not UtilClient.is_unset(request.integrate_kiali):
            body['IntegrateKiali'] = request.integrate_kiali
        if not UtilClient.is_unset(request.interception_mode):
            body['InterceptionMode'] = request.interception_mode
        if not UtilClient.is_unset(request.kiali_arms_auth_tokens):
            body['KialiArmsAuthTokens'] = request.kiali_arms_auth_tokens
        if not UtilClient.is_unset(request.kiali_enabled):
            body['KialiEnabled'] = request.kiali_enabled
        if not UtilClient.is_unset(request.kiali_service_annotations):
            body['KialiServiceAnnotations'] = request.kiali_service_annotations
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.locality_lbconf):
            body['LocalityLBConf'] = request.locality_lbconf
        if not UtilClient.is_unset(request.locality_load_balancing):
            body['LocalityLoadBalancing'] = request.locality_load_balancing
        if not UtilClient.is_unset(request.log_level):
            body['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.mseenabled):
            body['MSEEnabled'] = request.mseenabled
        if not UtilClient.is_unset(request.multi_buffer_enabled):
            body['MultiBufferEnabled'] = request.multi_buffer_enabled
        if not UtilClient.is_unset(request.multi_buffer_poll_delay):
            body['MultiBufferPollDelay'] = request.multi_buffer_poll_delay
        if not UtilClient.is_unset(request.mysql_filter_enabled):
            body['MysqlFilterEnabled'] = request.mysql_filter_enabled
        if not UtilClient.is_unset(request.nfdenabled):
            body['NFDEnabled'] = request.nfdenabled
        if not UtilClient.is_unset(request.nfdlabel_pruned):
            body['NFDLabelPruned'] = request.nfdlabel_pruned
        if not UtilClient.is_unset(request.opainjector_cpulimit):
            body['OPAInjectorCPULimit'] = request.opainjector_cpulimit
        if not UtilClient.is_unset(request.opainjector_cpurequirement):
            body['OPAInjectorCPURequirement'] = request.opainjector_cpurequirement
        if not UtilClient.is_unset(request.opainjector_memory_limit):
            body['OPAInjectorMemoryLimit'] = request.opainjector_memory_limit
        if not UtilClient.is_unset(request.opainjector_memory_requirement):
            body['OPAInjectorMemoryRequirement'] = request.opainjector_memory_requirement
        if not UtilClient.is_unset(request.opalimit_cpu):
            body['OPALimitCPU'] = request.opalimit_cpu
        if not UtilClient.is_unset(request.opalimit_memory):
            body['OPALimitMemory'] = request.opalimit_memory
        if not UtilClient.is_unset(request.opalog_level):
            body['OPALogLevel'] = request.opalog_level
        if not UtilClient.is_unset(request.oparequest_cpu):
            body['OPARequestCPU'] = request.oparequest_cpu
        if not UtilClient.is_unset(request.oparequest_memory):
            body['OPARequestMemory'] = request.oparequest_memory
        if not UtilClient.is_unset(request.opascope_injected):
            body['OPAScopeInjected'] = request.opascope_injected
        if not UtilClient.is_unset(request.opa_enabled):
            body['OpaEnabled'] = request.opa_enabled
        if not UtilClient.is_unset(request.open_agent_policy):
            body['OpenAgentPolicy'] = request.open_agent_policy
        if not UtilClient.is_unset(request.outbound_traffic_policy):
            body['OutboundTrafficPolicy'] = request.outbound_traffic_policy
        if not UtilClient.is_unset(request.pilot_enable_quic_listeners):
            body['PilotEnableQuicListeners'] = request.pilot_enable_quic_listeners
        if not UtilClient.is_unset(request.prometheus_url):
            body['PrometheusUrl'] = request.prometheus_url
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.proxy_limit_cpu):
            body['ProxyLimitCPU'] = request.proxy_limit_cpu
        if not UtilClient.is_unset(request.proxy_limit_memory):
            body['ProxyLimitMemory'] = request.proxy_limit_memory
        if not UtilClient.is_unset(request.proxy_request_cpu):
            body['ProxyRequestCPU'] = request.proxy_request_cpu
        if not UtilClient.is_unset(request.proxy_request_memory):
            body['ProxyRequestMemory'] = request.proxy_request_memory
        if not UtilClient.is_unset(request.proxy_stats_matcher):
            body['ProxyStatsMatcher'] = request.proxy_stats_matcher
        if not UtilClient.is_unset(request.redis_filter_enabled):
            body['RedisFilterEnabled'] = request.redis_filter_enabled
        if not UtilClient.is_unset(request.smcenabled):
            body['SMCEnabled'] = request.smcenabled
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_injector_limit_cpu):
            body['SidecarInjectorLimitCPU'] = request.sidecar_injector_limit_cpu
        if not UtilClient.is_unset(request.sidecar_injector_limit_memory):
            body['SidecarInjectorLimitMemory'] = request.sidecar_injector_limit_memory
        if not UtilClient.is_unset(request.sidecar_injector_request_cpu):
            body['SidecarInjectorRequestCPU'] = request.sidecar_injector_request_cpu
        if not UtilClient.is_unset(request.sidecar_injector_request_memory):
            body['SidecarInjectorRequestMemory'] = request.sidecar_injector_request_memory
        if not UtilClient.is_unset(request.sidecar_injector_webhook_as_yaml):
            body['SidecarInjectorWebhookAsYaml'] = request.sidecar_injector_webhook_as_yaml
        if not UtilClient.is_unset(request.telemetry):
            body['Telemetry'] = request.telemetry
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        if not UtilClient.is_unset(request.thrift_filter_enabled):
            body['ThriftFilterEnabled'] = request.thrift_filter_enabled
        if not UtilClient.is_unset(request.trace_custom_tags):
            body['TraceCustomTags'] = request.trace_custom_tags
        if not UtilClient.is_unset(request.trace_max_path_tag_length):
            body['TraceMaxPathTagLength'] = request.trace_max_path_tag_length
        if not UtilClient.is_unset(request.trace_sampling):
            body['TraceSampling'] = request.trace_sampling
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_limit_cpu):
            body['TracingOnExtZipkinLimitCPU'] = request.tracing_on_ext_zipkin_limit_cpu
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_limit_memory):
            body['TracingOnExtZipkinLimitMemory'] = request.tracing_on_ext_zipkin_limit_memory
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_replica_count):
            body['TracingOnExtZipkinReplicaCount'] = request.tracing_on_ext_zipkin_replica_count
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_request_cpu):
            body['TracingOnExtZipkinRequestCPU'] = request.tracing_on_ext_zipkin_request_cpu
        if not UtilClient.is_unset(request.tracing_on_ext_zipkin_request_memory):
            body['TracingOnExtZipkinRequestMemory'] = request.tracing_on_ext_zipkin_request_memory
        if not UtilClient.is_unset(request.web_assembly_filter_enabled):
            body['WebAssemblyFilterEnabled'] = request.web_assembly_filter_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshFeature',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mesh_feature(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        """
        @summary Updates the configuration of a Service Mesh (ASM) instance.
        
        @param request: UpdateMeshFeatureRequest
        @return: UpdateMeshFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_mesh_feature_with_options(request, runtime)

    async def update_mesh_feature_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshFeatureRequest,
    ) -> servicemesh_20200111_models.UpdateMeshFeatureResponse:
        """
        @summary Updates the configuration of a Service Mesh (ASM) instance.
        
        @param request: UpdateMeshFeatureRequest
        @return: UpdateMeshFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_mesh_feature_with_options_async(request, runtime)

    def update_mesh_multi_cluster_network_with_options(
        self,
        tmp_req: servicemesh_20200111_models.UpdateMeshMultiClusterNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshMultiClusterNetworkResponse:
        """
        @summary Updates the network configurations of multiple Kubernetes clusters in a Service Mesh (ASM) instance.
        
        @param tmp_req: UpdateMeshMultiClusterNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMeshMultiClusterNetworkResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.UpdateMeshMultiClusterNetworkShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.multi_cluster_networks):
            request.multi_cluster_networks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.multi_cluster_networks, 'MultiClusterNetworks', 'json')
        body = {}
        if not UtilClient.is_unset(request.multi_cluster_networks_shrink):
            body['MultiClusterNetworks'] = request.multi_cluster_networks_shrink
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshMultiClusterNetwork',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshMultiClusterNetworkResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mesh_multi_cluster_network_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.UpdateMeshMultiClusterNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateMeshMultiClusterNetworkResponse:
        """
        @summary Updates the network configurations of multiple Kubernetes clusters in a Service Mesh (ASM) instance.
        
        @param tmp_req: UpdateMeshMultiClusterNetworkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateMeshMultiClusterNetworkResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.UpdateMeshMultiClusterNetworkShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.multi_cluster_networks):
            request.multi_cluster_networks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.multi_cluster_networks, 'MultiClusterNetworks', 'json')
        body = {}
        if not UtilClient.is_unset(request.multi_cluster_networks_shrink):
            body['MultiClusterNetworks'] = request.multi_cluster_networks_shrink
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMeshMultiClusterNetwork',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshMultiClusterNetworkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mesh_multi_cluster_network(
        self,
        request: servicemesh_20200111_models.UpdateMeshMultiClusterNetworkRequest,
    ) -> servicemesh_20200111_models.UpdateMeshMultiClusterNetworkResponse:
        """
        @summary Updates the network configurations of multiple Kubernetes clusters in a Service Mesh (ASM) instance.
        
        @param request: UpdateMeshMultiClusterNetworkRequest
        @return: UpdateMeshMultiClusterNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_mesh_multi_cluster_network_with_options(request, runtime)

    async def update_mesh_multi_cluster_network_async(
        self,
        request: servicemesh_20200111_models.UpdateMeshMultiClusterNetworkRequest,
    ) -> servicemesh_20200111_models.UpdateMeshMultiClusterNetworkResponse:
        """
        @summary Updates the network configurations of multiple Kubernetes clusters in a Service Mesh (ASM) instance.
        
        @param request: UpdateMeshMultiClusterNetworkRequest
        @return: UpdateMeshMultiClusterNetworkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_mesh_multi_cluster_network_with_options_async(request, runtime)

    def update_namespace_scope_sidecar_config_with_options(
        self,
        tmp_req: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        """
        @summary Updates the configurations of sidecar proxies at the namespace level.
        
        @param tmp_req: UpdateNamespaceScopeSidecarConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNamespaceScopeSidecarConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scaled_sidecar_resource):
            request.scaled_sidecar_resource_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scaled_sidecar_resource, 'ScaledSidecarResource', 'json')
        body = {}
        if not UtilClient.is_unset(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.enable_core_dump):
            body['EnableCoreDump'] = request.enable_core_dump
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.hold_application_until_proxy_starts):
            body['HoldApplicationUntilProxyStarts'] = request.hold_application_until_proxy_starts
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.include_outbound_ports):
            body['IncludeOutboundPorts'] = request.include_outbound_ports
        if not UtilClient.is_unset(request.interception_mode):
            body['InterceptionMode'] = request.interception_mode
        if not UtilClient.is_unset(request.istio_dnsproxy_enabled):
            body['IstioDNSProxyEnabled'] = request.istio_dnsproxy_enabled
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.log_level):
            body['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.post_start):
            body['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            body['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.privileged):
            body['Privileged'] = request.privileged
        if not UtilClient.is_unset(request.proxy_init_ack_slo_cpuresource_limit):
            body['ProxyInitAckSloCPUResourceLimit'] = request.proxy_init_ack_slo_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_ack_slo_cpuresource_request):
            body['ProxyInitAckSloCPUResourceRequest'] = request.proxy_init_ack_slo_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_ack_slo_memory_resource_limit):
            body['ProxyInitAckSloMemoryResourceLimit'] = request.proxy_init_ack_slo_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_ack_slo_memory_resource_request):
            body['ProxyInitAckSloMemoryResourceRequest'] = request.proxy_init_ack_slo_memory_resource_request
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.proxy_metadata):
            body['ProxyMetadata'] = request.proxy_metadata
        if not UtilClient.is_unset(request.proxy_stats_matcher):
            body['ProxyStatsMatcher'] = request.proxy_stats_matcher
        if not UtilClient.is_unset(request.readiness_failure_threshold):
            body['ReadinessFailureThreshold'] = request.readiness_failure_threshold
        if not UtilClient.is_unset(request.readiness_initial_delay_seconds):
            body['ReadinessInitialDelaySeconds'] = request.readiness_initial_delay_seconds
        if not UtilClient.is_unset(request.readiness_period_seconds):
            body['ReadinessPeriodSeconds'] = request.readiness_period_seconds
        if not UtilClient.is_unset(request.runtime_values):
            body['RuntimeValues'] = request.runtime_values
        if not UtilClient.is_unset(request.smcenabled):
            body['SMCEnabled'] = request.smcenabled
        if not UtilClient.is_unset(request.scaled_sidecar_resource_shrink):
            body['ScaledSidecarResource'] = request.scaled_sidecar_resource_shrink
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_cpuresource_limit):
            body['SidecarProxyAckSloCPUResourceLimit'] = request.sidecar_proxy_ack_slo_cpuresource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_cpuresource_request):
            body['SidecarProxyAckSloCPUResourceRequest'] = request.sidecar_proxy_ack_slo_cpuresource_request
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_memory_resource_limit):
            body['SidecarProxyAckSloMemoryResourceLimit'] = request.sidecar_proxy_ack_slo_memory_resource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_memory_resource_request):
            body['SidecarProxyAckSloMemoryResourceRequest'] = request.sidecar_proxy_ack_slo_memory_resource_request
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_limit):
            body['SidecarProxyCPUResourceLimit'] = request.sidecar_proxy_cpuresource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_request):
            body['SidecarProxyCPUResourceRequest'] = request.sidecar_proxy_cpuresource_request
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_limit):
            body['SidecarProxyMemoryResourceLimit'] = request.sidecar_proxy_memory_resource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_request):
            body['SidecarProxyMemoryResourceRequest'] = request.sidecar_proxy_memory_resource_request
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_scope_sidecar_config_with_options_async(
        self,
        tmp_req: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        """
        @summary Updates the configurations of sidecar proxies at the namespace level.
        
        @param tmp_req: UpdateNamespaceScopeSidecarConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNamespaceScopeSidecarConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scaled_sidecar_resource):
            request.scaled_sidecar_resource_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scaled_sidecar_resource, 'ScaledSidecarResource', 'json')
        body = {}
        if not UtilClient.is_unset(request.concurrency):
            body['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.enable_core_dump):
            body['EnableCoreDump'] = request.enable_core_dump
        if not UtilClient.is_unset(request.exclude_ipranges):
            body['ExcludeIPRanges'] = request.exclude_ipranges
        if not UtilClient.is_unset(request.exclude_inbound_ports):
            body['ExcludeInboundPorts'] = request.exclude_inbound_ports
        if not UtilClient.is_unset(request.exclude_outbound_ports):
            body['ExcludeOutboundPorts'] = request.exclude_outbound_ports
        if not UtilClient.is_unset(request.hold_application_until_proxy_starts):
            body['HoldApplicationUntilProxyStarts'] = request.hold_application_until_proxy_starts
        if not UtilClient.is_unset(request.include_ipranges):
            body['IncludeIPRanges'] = request.include_ipranges
        if not UtilClient.is_unset(request.include_inbound_ports):
            body['IncludeInboundPorts'] = request.include_inbound_ports
        if not UtilClient.is_unset(request.include_outbound_ports):
            body['IncludeOutboundPorts'] = request.include_outbound_ports
        if not UtilClient.is_unset(request.interception_mode):
            body['InterceptionMode'] = request.interception_mode
        if not UtilClient.is_unset(request.istio_dnsproxy_enabled):
            body['IstioDNSProxyEnabled'] = request.istio_dnsproxy_enabled
        if not UtilClient.is_unset(request.lifecycle):
            body['Lifecycle'] = request.lifecycle
        if not UtilClient.is_unset(request.log_level):
            body['LogLevel'] = request.log_level
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.post_start):
            body['PostStart'] = request.post_start
        if not UtilClient.is_unset(request.pre_stop):
            body['PreStop'] = request.pre_stop
        if not UtilClient.is_unset(request.privileged):
            body['Privileged'] = request.privileged
        if not UtilClient.is_unset(request.proxy_init_ack_slo_cpuresource_limit):
            body['ProxyInitAckSloCPUResourceLimit'] = request.proxy_init_ack_slo_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_ack_slo_cpuresource_request):
            body['ProxyInitAckSloCPUResourceRequest'] = request.proxy_init_ack_slo_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_ack_slo_memory_resource_limit):
            body['ProxyInitAckSloMemoryResourceLimit'] = request.proxy_init_ack_slo_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_ack_slo_memory_resource_request):
            body['ProxyInitAckSloMemoryResourceRequest'] = request.proxy_init_ack_slo_memory_resource_request
        if not UtilClient.is_unset(request.proxy_init_cpuresource_limit):
            body['ProxyInitCPUResourceLimit'] = request.proxy_init_cpuresource_limit
        if not UtilClient.is_unset(request.proxy_init_cpuresource_request):
            body['ProxyInitCPUResourceRequest'] = request.proxy_init_cpuresource_request
        if not UtilClient.is_unset(request.proxy_init_memory_resource_limit):
            body['ProxyInitMemoryResourceLimit'] = request.proxy_init_memory_resource_limit
        if not UtilClient.is_unset(request.proxy_init_memory_resource_request):
            body['ProxyInitMemoryResourceRequest'] = request.proxy_init_memory_resource_request
        if not UtilClient.is_unset(request.proxy_metadata):
            body['ProxyMetadata'] = request.proxy_metadata
        if not UtilClient.is_unset(request.proxy_stats_matcher):
            body['ProxyStatsMatcher'] = request.proxy_stats_matcher
        if not UtilClient.is_unset(request.readiness_failure_threshold):
            body['ReadinessFailureThreshold'] = request.readiness_failure_threshold
        if not UtilClient.is_unset(request.readiness_initial_delay_seconds):
            body['ReadinessInitialDelaySeconds'] = request.readiness_initial_delay_seconds
        if not UtilClient.is_unset(request.readiness_period_seconds):
            body['ReadinessPeriodSeconds'] = request.readiness_period_seconds
        if not UtilClient.is_unset(request.runtime_values):
            body['RuntimeValues'] = request.runtime_values
        if not UtilClient.is_unset(request.smcenabled):
            body['SMCEnabled'] = request.smcenabled
        if not UtilClient.is_unset(request.scaled_sidecar_resource_shrink):
            body['ScaledSidecarResource'] = request.scaled_sidecar_resource_shrink
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_cpuresource_limit):
            body['SidecarProxyAckSloCPUResourceLimit'] = request.sidecar_proxy_ack_slo_cpuresource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_cpuresource_request):
            body['SidecarProxyAckSloCPUResourceRequest'] = request.sidecar_proxy_ack_slo_cpuresource_request
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_memory_resource_limit):
            body['SidecarProxyAckSloMemoryResourceLimit'] = request.sidecar_proxy_ack_slo_memory_resource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_ack_slo_memory_resource_request):
            body['SidecarProxyAckSloMemoryResourceRequest'] = request.sidecar_proxy_ack_slo_memory_resource_request
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_limit):
            body['SidecarProxyCPUResourceLimit'] = request.sidecar_proxy_cpuresource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_cpuresource_request):
            body['SidecarProxyCPUResourceRequest'] = request.sidecar_proxy_cpuresource_request
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_limit):
            body['SidecarProxyMemoryResourceLimit'] = request.sidecar_proxy_memory_resource_limit
        if not UtilClient.is_unset(request.sidecar_proxy_memory_resource_request):
            body['SidecarProxyMemoryResourceRequest'] = request.sidecar_proxy_memory_resource_request
        if not UtilClient.is_unset(request.termination_drain_duration):
            body['TerminationDrainDuration'] = request.termination_drain_duration
        if not UtilClient.is_unset(request.tracing):
            body['Tracing'] = request.tracing
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNamespaceScopeSidecarConfig',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace_scope_sidecar_config(
        self,
        request: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        """
        @summary Updates the configurations of sidecar proxies at the namespace level.
        
        @param request: UpdateNamespaceScopeSidecarConfigRequest
        @return: UpdateNamespaceScopeSidecarConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_namespace_scope_sidecar_config_with_options(request, runtime)

    async def update_namespace_scope_sidecar_config_async(
        self,
        request: servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigRequest,
    ) -> servicemesh_20200111_models.UpdateNamespaceScopeSidecarConfigResponse:
        """
        @summary Updates the configurations of sidecar proxies at the namespace level.
        
        @param request: UpdateNamespaceScopeSidecarConfigRequest
        @return: UpdateNamespaceScopeSidecarConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_namespace_scope_sidecar_config_with_options_async(request, runtime)

    def update_swim_lane_with_options(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateSwimLaneResponse:
        """
        @summary Updates the information about a lane.
        
        @param request: UpdateSwimLaneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSwimLaneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.label_selector_key):
            body['LabelSelectorKey'] = request.label_selector_key
        if not UtilClient.is_unset(request.label_selector_value):
            body['LabelSelectorValue'] = request.label_selector_value
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateSwimLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_swim_lane_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateSwimLaneResponse:
        """
        @summary Updates the information about a lane.
        
        @param request: UpdateSwimLaneRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSwimLaneResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.label_selector_key):
            body['LabelSelectorKey'] = request.label_selector_key
        if not UtilClient.is_unset(request.label_selector_value):
            body['LabelSelectorValue'] = request.label_selector_value
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.swim_lane_name):
            body['SwimLaneName'] = request.swim_lane_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSwimLane',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateSwimLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_swim_lane(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneRequest,
    ) -> servicemesh_20200111_models.UpdateSwimLaneResponse:
        """
        @summary Updates the information about a lane.
        
        @param request: UpdateSwimLaneRequest
        @return: UpdateSwimLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_swim_lane_with_options(request, runtime)

    async def update_swim_lane_async(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneRequest,
    ) -> servicemesh_20200111_models.UpdateSwimLaneResponse:
        """
        @summary Updates the information about a lane.
        
        @param request: UpdateSwimLaneRequest
        @return: UpdateSwimLaneResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_swim_lane_with_options_async(request, runtime)

    def update_swim_lane_group_with_options(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateSwimLaneGroupResponse:
        """
        @summary Updates the information of a lane group.
        
        @param request: UpdateSwimLaneGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSwimLaneGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fallback_target):
            body['FallbackTarget'] = request.fallback_target
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ingress_routing_strategy):
            body['IngressRoutingStrategy'] = request.ingress_routing_strategy
        if not UtilClient.is_unset(request.service_level_fallback_target):
            body['ServiceLevelFallbackTarget'] = request.service_level_fallback_target
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.weighted_ingress_rule):
            body['WeightedIngressRule'] = request.weighted_ingress_rule
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateSwimLaneGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_swim_lane_group_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateSwimLaneGroupResponse:
        """
        @summary Updates the information of a lane group.
        
        @param request: UpdateSwimLaneGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSwimLaneGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fallback_target):
            body['FallbackTarget'] = request.fallback_target
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.ingress_routing_strategy):
            body['IngressRoutingStrategy'] = request.ingress_routing_strategy
        if not UtilClient.is_unset(request.service_level_fallback_target):
            body['ServiceLevelFallbackTarget'] = request.service_level_fallback_target
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.services_list):
            body['ServicesList'] = request.services_list
        if not UtilClient.is_unset(request.weighted_ingress_rule):
            body['WeightedIngressRule'] = request.weighted_ingress_rule
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSwimLaneGroup',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateSwimLaneGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_swim_lane_group(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.UpdateSwimLaneGroupResponse:
        """
        @summary Updates the information of a lane group.
        
        @param request: UpdateSwimLaneGroupRequest
        @return: UpdateSwimLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_swim_lane_group_with_options(request, runtime)

    async def update_swim_lane_group_async(
        self,
        request: servicemesh_20200111_models.UpdateSwimLaneGroupRequest,
    ) -> servicemesh_20200111_models.UpdateSwimLaneGroupResponse:
        """
        @summary Updates the information of a lane group.
        
        @param request: UpdateSwimLaneGroupRequest
        @return: UpdateSwimLaneGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_swim_lane_group_with_options_async(request, runtime)

    def update_waypoint_with_options(
        self,
        request: servicemesh_20200111_models.UpdateWaypointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateWaypointResponse:
        """
        @summary 更新Waypoint
        
        @param request: UpdateWaypointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWaypointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hpaenabled):
            body['HPAEnabled'] = request.hpaenabled
        if not UtilClient.is_unset(request.hpamax_replicas):
            body['HPAMaxReplicas'] = request.hpamax_replicas
        if not UtilClient.is_unset(request.hpamin_replicas):
            body['HPAMinReplicas'] = request.hpamin_replicas
        if not UtilClient.is_unset(request.hpatarget_cpu):
            body['HPATargetCPU'] = request.hpatarget_cpu
        if not UtilClient.is_unset(request.hpatarget_memory):
            body['HPATargetMemory'] = request.hpatarget_memory
        if not UtilClient.is_unset(request.limit_cpu):
            body['LimitCPU'] = request.limit_cpu
        if not UtilClient.is_unset(request.limit_memory):
            body['LimitMemory'] = request.limit_memory
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.prefer_eci):
            body['PreferECI'] = request.prefer_eci
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.request_cpu):
            body['RequestCPU'] = request.request_cpu
        if not UtilClient.is_unset(request.request_memory):
            body['RequestMemory'] = request.request_memory
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWaypoint',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateWaypointResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_waypoint_with_options_async(
        self,
        request: servicemesh_20200111_models.UpdateWaypointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpdateWaypointResponse:
        """
        @summary 更新Waypoint
        
        @param request: UpdateWaypointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWaypointResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.hpaenabled):
            body['HPAEnabled'] = request.hpaenabled
        if not UtilClient.is_unset(request.hpamax_replicas):
            body['HPAMaxReplicas'] = request.hpamax_replicas
        if not UtilClient.is_unset(request.hpamin_replicas):
            body['HPAMinReplicas'] = request.hpamin_replicas
        if not UtilClient.is_unset(request.hpatarget_cpu):
            body['HPATargetCPU'] = request.hpatarget_cpu
        if not UtilClient.is_unset(request.hpatarget_memory):
            body['HPATargetMemory'] = request.hpatarget_memory
        if not UtilClient.is_unset(request.limit_cpu):
            body['LimitCPU'] = request.limit_cpu
        if not UtilClient.is_unset(request.limit_memory):
            body['LimitMemory'] = request.limit_memory
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.prefer_eci):
            body['PreferECI'] = request.prefer_eci
        if not UtilClient.is_unset(request.replicas):
            body['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.request_cpu):
            body['RequestCPU'] = request.request_cpu
        if not UtilClient.is_unset(request.request_memory):
            body['RequestMemory'] = request.request_memory
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWaypoint',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateWaypointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_waypoint(
        self,
        request: servicemesh_20200111_models.UpdateWaypointRequest,
    ) -> servicemesh_20200111_models.UpdateWaypointResponse:
        """
        @summary 更新Waypoint
        
        @param request: UpdateWaypointRequest
        @return: UpdateWaypointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_waypoint_with_options(request, runtime)

    async def update_waypoint_async(
        self,
        request: servicemesh_20200111_models.UpdateWaypointRequest,
    ) -> servicemesh_20200111_models.UpdateWaypointResponse:
        """
        @summary 更新Waypoint
        
        @param request: UpdateWaypointRequest
        @return: UpdateWaypointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_waypoint_with_options_async(request, runtime)

    def upgrade_mesh_edition_partially_with_options(
        self,
        request: servicemesh_20200111_models.UpgradeMeshEditionPartiallyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse:
        """
        @summary Upgrades a Service Mesh (ASM) instance to Professional Edition that is commercially released.
        
        @param request: UpgradeMeshEditionPartiallyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMeshEditionPartiallyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_continue):
            body['ASMGatewayContinue'] = request.asmgateway_continue
        if not UtilClient.is_unset(request.expected_version):
            body['ExpectedVersion'] = request.expected_version
        if not UtilClient.is_unset(request.pre_check):
            body['PreCheck'] = request.pre_check
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.switch_to_pro):
            body['SwitchToPro'] = request.switch_to_pro
        if not UtilClient.is_unset(request.upgrade_gateway_records):
            body['UpgradeGatewayRecords'] = request.upgrade_gateway_records
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeMeshEditionPartially',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_mesh_edition_partially_with_options_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshEditionPartiallyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse:
        """
        @summary Upgrades a Service Mesh (ASM) instance to Professional Edition that is commercially released.
        
        @param request: UpgradeMeshEditionPartiallyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMeshEditionPartiallyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.asmgateway_continue):
            body['ASMGatewayContinue'] = request.asmgateway_continue
        if not UtilClient.is_unset(request.expected_version):
            body['ExpectedVersion'] = request.expected_version
        if not UtilClient.is_unset(request.pre_check):
            body['PreCheck'] = request.pre_check
        if not UtilClient.is_unset(request.service_mesh_id):
            body['ServiceMeshId'] = request.service_mesh_id
        if not UtilClient.is_unset(request.switch_to_pro):
            body['SwitchToPro'] = request.switch_to_pro
        if not UtilClient.is_unset(request.upgrade_gateway_records):
            body['UpgradeGatewayRecords'] = request.upgrade_gateway_records
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpgradeMeshEditionPartially',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_mesh_edition_partially(
        self,
        request: servicemesh_20200111_models.UpgradeMeshEditionPartiallyRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse:
        """
        @summary Upgrades a Service Mesh (ASM) instance to Professional Edition that is commercially released.
        
        @param request: UpgradeMeshEditionPartiallyRequest
        @return: UpgradeMeshEditionPartiallyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_mesh_edition_partially_with_options(request, runtime)

    async def upgrade_mesh_edition_partially_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshEditionPartiallyRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshEditionPartiallyResponse:
        """
        @summary Upgrades a Service Mesh (ASM) instance to Professional Edition that is commercially released.
        
        @param request: UpgradeMeshEditionPartiallyRequest
        @return: UpgradeMeshEditionPartiallyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_mesh_edition_partially_with_options_async(request, runtime)

    def upgrade_mesh_version_with_options(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        """
        @summary Updates the version of a Service Mesh (ASM) instance.
        
        @param request: UpgradeMeshVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMeshVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pre_check):
            query['PreCheck'] = request.pre_check
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMeshVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_mesh_version_with_options_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        """
        @summary Updates the version of a Service Mesh (ASM) instance.
        
        @param request: UpgradeMeshVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMeshVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pre_check):
            query['PreCheck'] = request.pre_check
        if not UtilClient.is_unset(request.service_mesh_id):
            query['ServiceMeshId'] = request.service_mesh_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMeshVersion',
            version='2020-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_mesh_version(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        """
        @summary Updates the version of a Service Mesh (ASM) instance.
        
        @param request: UpgradeMeshVersionRequest
        @return: UpgradeMeshVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_mesh_version_with_options(request, runtime)

    async def upgrade_mesh_version_async(
        self,
        request: servicemesh_20200111_models.UpgradeMeshVersionRequest,
    ) -> servicemesh_20200111_models.UpgradeMeshVersionResponse:
        """
        @summary Updates the version of a Service Mesh (ASM) instance.
        
        @param request: UpgradeMeshVersionRequest
        @return: UpgradeMeshVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_mesh_version_with_options_async(request, runtime)
