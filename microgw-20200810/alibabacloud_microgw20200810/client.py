# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_microgw20200810 import models as microgw_20200810_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('microgw', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def find_all_service(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindAllServiceRequest,
    ) -> microgw_20200810_models.FindAllServiceResponse:
        """
        findAllService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_all_service_with_options(gateway_id, request, headers, runtime)

    async def find_all_service_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindAllServiceRequest,
    ) -> microgw_20200810_models.FindAllServiceResponse:
        """
        findAllService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.find_all_service_with_options_async(gateway_id, request, headers, runtime)

    def find_all_service_with_options(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindAllServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindAllServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.alias_name):
            query['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.is_health):
            query['isHealth'] = request.is_health
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.FindAllServiceResponse().from_map(
            self.do_roarequest('FindAllService', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}/service', 'json', req, runtime)
        )

    async def find_all_service_with_options_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindAllServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindAllServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.alias_name):
            query['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.source_type):
            query['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.is_health):
            query['isHealth'] = request.is_health
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.FindAllServiceResponse().from_map(
            await self.do_roarequest_async('FindAllService', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}/service', 'json', req, runtime)
        )

    def create_api(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateApiRequest,
    ) -> microgw_20200810_models.CreateApiResponse:
        """
        createApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_api_with_options(gateway_id, request, headers, runtime)

    async def create_api_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateApiRequest,
    ) -> microgw_20200810_models.CreateApiResponse:
        """
        createApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_api_with_options_async(gateway_id, request, headers, runtime)

    def create_api_with_options(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateApiResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.attached_services):
            body['attachedServices'] = request.attached_services
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateApiResponse().from_map(
            self.do_roarequest('CreateApi', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/gateway/{gateway_id}/api', 'json', req, runtime)
        )

    async def create_api_with_options_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateApiResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.attached_services):
            body['attachedServices'] = request.attached_services
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateApiResponse().from_map(
            await self.do_roarequest_async('CreateApi', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/gateway/{gateway_id}/api', 'json', req, runtime)
        )

    def get_gateway_by_id(
        self,
        gateway_id: str,
    ) -> microgw_20200810_models.GetGatewayByIdResponse:
        """
        getGatewayById
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gateway_by_id_with_options(gateway_id, headers, runtime)

    async def get_gateway_by_id_async(
        self,
        gateway_id: str,
    ) -> microgw_20200810_models.GetGatewayByIdResponse:
        """
        getGatewayById
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_gateway_by_id_with_options_async(gateway_id, headers, runtime)

    def get_gateway_by_id_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetGatewayByIdResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetGatewayByIdResponse().from_map(
            self.do_roarequest('GetGatewayById', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}', 'json', req, runtime)
        )

    async def get_gateway_by_id_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetGatewayByIdResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetGatewayByIdResponse().from_map(
            await self.do_roarequest_async('GetGatewayById', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}', 'json', req, runtime)
        )

    def create_policy(
        self,
        request: microgw_20200810_models.CreatePolicyRequest,
    ) -> microgw_20200810_models.CreatePolicyResponse:
        """
        createPolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_policy_with_options(request, headers, runtime)

    async def create_policy_async(
        self,
        request: microgw_20200810_models.CreatePolicyRequest,
    ) -> microgw_20200810_models.CreatePolicyResponse:
        """
        createPolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_policy_with_options_async(request, headers, runtime)

    def create_policy_with_options(
        self,
        request: microgw_20200810_models.CreatePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.policy_group):
            body['policyGroup'] = request.policy_group
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreatePolicyResponse().from_map(
            self.do_roarequest('CreatePolicy', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/policy', 'json', req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        request: microgw_20200810_models.CreatePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreatePolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.policy_group):
            body['policyGroup'] = request.policy_group
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreatePolicyResponse().from_map(
            await self.do_roarequest_async('CreatePolicy', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/policy', 'json', req, runtime)
        )

    def get_service_instance_for_registry_by_service_name(
        self,
        gateway_id: str,
        registry_id: str,
        request: microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameRequest,
    ) -> microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameResponse:
        """
        getServiceInstanceForRegistryByServiceName
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_instance_for_registry_by_service_name_with_options(gateway_id, registry_id, request, headers, runtime)

    async def get_service_instance_for_registry_by_service_name_async(
        self,
        gateway_id: str,
        registry_id: str,
        request: microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameRequest,
    ) -> microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameResponse:
        """
        getServiceInstanceForRegistryByServiceName
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_instance_for_registry_by_service_name_with_options_async(gateway_id, registry_id, request, headers, runtime)

    def get_service_instance_for_registry_by_service_name_with_options(
        self,
        gateway_id: str,
        registry_id: str,
        request: microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameResponse().from_map(
            self.do_roarequest('GetServiceInstanceForRegistryByServiceName', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}/registry/{{registryId}}/service', 'json', req, runtime)
        )

    async def get_service_instance_for_registry_by_service_name_with_options_async(
        self,
        gateway_id: str,
        registry_id: str,
        request: microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameResponse().from_map(
            await self.do_roarequest_async('GetServiceInstanceForRegistryByServiceName', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}/registry/{{registryId}}/service', 'json', req, runtime)
        )

    def delete_service(
        self,
        service_id: str,
    ) -> microgw_20200810_models.DeleteServiceResponse:
        """
        deleteService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(service_id, headers, runtime)

    async def delete_service_async(
        self,
        service_id: str,
    ) -> microgw_20200810_models.DeleteServiceResponse:
        """
        deleteService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(service_id, headers, runtime)

    def delete_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeleteServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteServiceResponse().from_map(
            self.do_roarequest('DeleteService', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/service/{service_id}', 'json', req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeleteServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteServiceResponse().from_map(
            await self.do_roarequest_async('DeleteService', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/service/{service_id}', 'json', req, runtime)
        )

    def update_registry(
        self,
        registry_id: str,
        request: microgw_20200810_models.UpdateRegistryRequest,
    ) -> microgw_20200810_models.UpdateRegistryResponse:
        """
        UpdateRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_registry_with_options(registry_id, request, headers, runtime)

    async def update_registry_async(
        self,
        registry_id: str,
        request: microgw_20200810_models.UpdateRegistryRequest,
    ) -> microgw_20200810_models.UpdateRegistryResponse:
        """
        UpdateRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_registry_with_options_async(registry_id, request, headers, runtime)

    def update_registry_with_options(
        self,
        registry_id: str,
        request: microgw_20200810_models.UpdateRegistryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateRegistryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateRegistryResponse().from_map(
            self.do_roarequest('UpdateRegistry', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/registry/{registry_id}', 'json', req, runtime)
        )

    async def update_registry_with_options_async(
        self,
        registry_id: str,
        request: microgw_20200810_models.UpdateRegistryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateRegistryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateRegistryResponse().from_map(
            await self.do_roarequest_async('UpdateRegistry', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/registry/{registry_id}', 'json', req, runtime)
        )

    def create_gateway(
        self,
        request: microgw_20200810_models.CreateGatewayRequest,
    ) -> microgw_20200810_models.CreateGatewayResponse:
        """
        createGateway
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_gateway_with_options(request, headers, runtime)

    async def create_gateway_async(
        self,
        request: microgw_20200810_models.CreateGatewayRequest,
    ) -> microgw_20200810_models.CreateGatewayResponse:
        """
        createGateway
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_gateway_with_options_async(request, headers, runtime)

    def create_gateway_with_options(
        self,
        request: microgw_20200810_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_create_slb):
            body['autoCreateSlb'] = request.auto_create_slb
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.edas_namespace_id):
            body['edasNamespaceId'] = request.edas_namespace_id
        if not UtilClient.is_unset(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.pod_cidr):
            body['podCidr'] = request.pod_cidr
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.region_name):
            body['regionName'] = request.region_name
        if not UtilClient.is_unset(request.replica):
            body['replica'] = request.replica
        if not UtilClient.is_unset(request.runtime_on):
            body['runtimeOn'] = request.runtime_on
        if not UtilClient.is_unset(request.security_group):
            body['securityGroup'] = request.security_group
        if not UtilClient.is_unset(request.slb):
            body['slb'] = request.slb
        if not UtilClient.is_unset(request.slb_spec):
            body['slbSpec'] = request.slb_spec
        if not UtilClient.is_unset(request.vpc):
            body['vpc'] = request.vpc
        if not UtilClient.is_unset(request.vswitch):
            body['vswitch'] = request.vswitch
        if not UtilClient.is_unset(request.zone):
            body['zone'] = request.zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateGatewayResponse().from_map(
            self.do_roarequest('CreateGateway', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/gateway', 'json', req, runtime)
        )

    async def create_gateway_with_options_async(
        self,
        request: microgw_20200810_models.CreateGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_create_slb):
            body['autoCreateSlb'] = request.auto_create_slb
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.edas_namespace_id):
            body['edasNamespaceId'] = request.edas_namespace_id
        if not UtilClient.is_unset(request.gateway_type):
            body['gatewayType'] = request.gateway_type
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.pod_cidr):
            body['podCidr'] = request.pod_cidr
        if not UtilClient.is_unset(request.region):
            body['region'] = request.region
        if not UtilClient.is_unset(request.region_name):
            body['regionName'] = request.region_name
        if not UtilClient.is_unset(request.replica):
            body['replica'] = request.replica
        if not UtilClient.is_unset(request.runtime_on):
            body['runtimeOn'] = request.runtime_on
        if not UtilClient.is_unset(request.security_group):
            body['securityGroup'] = request.security_group
        if not UtilClient.is_unset(request.slb):
            body['slb'] = request.slb
        if not UtilClient.is_unset(request.slb_spec):
            body['slbSpec'] = request.slb_spec
        if not UtilClient.is_unset(request.vpc):
            body['vpc'] = request.vpc
        if not UtilClient.is_unset(request.vswitch):
            body['vswitch'] = request.vswitch
        if not UtilClient.is_unset(request.zone):
            body['zone'] = request.zone
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateGatewayResponse().from_map(
            await self.do_roarequest_async('CreateGateway', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/gateway', 'json', req, runtime)
        )

    def check_service_health(
        self,
        request: microgw_20200810_models.CheckServiceHealthRequest,
    ) -> microgw_20200810_models.CheckServiceHealthResponse:
        """
        checkServiceHealth
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_service_health_with_options(request, headers, runtime)

    async def check_service_health_async(
        self,
        request: microgw_20200810_models.CheckServiceHealthRequest,
    ) -> microgw_20200810_models.CheckServiceHealthResponse:
        """
        checkServiceHealth
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_service_health_with_options_async(request, headers, runtime)

    def check_service_health_with_options(
        self,
        request: microgw_20200810_models.CheckServiceHealthRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CheckServiceHealthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.operation_ids):
            body['operationIds'] = request.operation_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CheckServiceHealthResponse().from_map(
            self.do_roarequest('CheckServiceHealth', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/service/check', 'json', req, runtime)
        )

    async def check_service_health_with_options_async(
        self,
        request: microgw_20200810_models.CheckServiceHealthRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CheckServiceHealthResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.operation_ids):
            body['operationIds'] = request.operation_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CheckServiceHealthResponse().from_map(
            await self.do_roarequest_async('CheckServiceHealth', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/service/check', 'json', req, runtime)
        )

    def create_policy_to_api(
        self,
        api_id: str,
        request: microgw_20200810_models.CreatePolicyToApiRequest,
    ) -> microgw_20200810_models.CreatePolicyToApiResponse:
        """
        createPolicyToApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_policy_to_api_with_options(api_id, request, headers, runtime)

    async def create_policy_to_api_async(
        self,
        api_id: str,
        request: microgw_20200810_models.CreatePolicyToApiRequest,
    ) -> microgw_20200810_models.CreatePolicyToApiResponse:
        """
        createPolicyToApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_policy_to_api_with_options_async(api_id, request, headers, runtime)

    def create_policy_to_api_with_options(
        self,
        api_id: str,
        request: microgw_20200810_models.CreatePolicyToApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreatePolicyToApiResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creation_date_time):
            body['creationDateTime'] = request.creation_date_time
        if not UtilClient.is_unset(request.direction):
            body['direction'] = request.direction
        if not UtilClient.is_unset(request.policy_alias_name):
            body['policyAliasName'] = request.policy_alias_name
        if not UtilClient.is_unset(request.policy_content):
            body['policyContent'] = request.policy_content
        if not UtilClient.is_unset(request.policy_group):
            body['policyGroup'] = request.policy_group
        if not UtilClient.is_unset(request.policy_id):
            body['policyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            body['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreatePolicyToApiResponse().from_map(
            self.do_roarequest('CreatePolicyToApi', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/api/{api_id}/policy', 'json', req, runtime)
        )

    async def create_policy_to_api_with_options_async(
        self,
        api_id: str,
        request: microgw_20200810_models.CreatePolicyToApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreatePolicyToApiResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.creation_date_time):
            body['creationDateTime'] = request.creation_date_time
        if not UtilClient.is_unset(request.direction):
            body['direction'] = request.direction
        if not UtilClient.is_unset(request.policy_alias_name):
            body['policyAliasName'] = request.policy_alias_name
        if not UtilClient.is_unset(request.policy_content):
            body['policyContent'] = request.policy_content
        if not UtilClient.is_unset(request.policy_group):
            body['policyGroup'] = request.policy_group
        if not UtilClient.is_unset(request.policy_id):
            body['policyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            body['policyName'] = request.policy_name
        if not UtilClient.is_unset(request.priority):
            body['priority'] = request.priority
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreatePolicyToApiResponse().from_map(
            await self.do_roarequest_async('CreatePolicyToApi', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/api/{api_id}/policy', 'json', req, runtime)
        )

    def detach_policy(
        self,
        api_id: str,
        policy_id: str,
    ) -> microgw_20200810_models.DetachPolicyResponse:
        """
        detachPolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.detach_policy_with_options(api_id, policy_id, headers, runtime)

    async def detach_policy_async(
        self,
        api_id: str,
        policy_id: str,
    ) -> microgw_20200810_models.DetachPolicyResponse:
        """
        detachPolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.detach_policy_with_options_async(api_id, policy_id, headers, runtime)

    def detach_policy_with_options(
        self,
        api_id: str,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DetachPolicyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DetachPolicyResponse().from_map(
            self.do_roarequest('DetachPolicy', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/api/{api_id}/detach/{{policyId}}', 'json', req, runtime)
        )

    async def detach_policy_with_options_async(
        self,
        api_id: str,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DetachPolicyResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DetachPolicyResponse().from_map(
            await self.do_roarequest_async('DetachPolicy', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/api/{api_id}/detach/{{policyId}}', 'json', req, runtime)
        )

    def find_template(
        self,
        api_id: str,
    ) -> microgw_20200810_models.FindTemplateResponse:
        """
        findTemplate
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_template_with_options(api_id, headers, runtime)

    async def find_template_async(
        self,
        api_id: str,
    ) -> microgw_20200810_models.FindTemplateResponse:
        """
        findTemplate
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.find_template_with_options_async(api_id, headers, runtime)

    def find_template_with_options(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.FindTemplateResponse().from_map(
            self.do_roarequest('FindTemplate', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/api/{api_id}/policy/template', 'json', req, runtime)
        )

    async def find_template_with_options_async(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindTemplateResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.FindTemplateResponse().from_map(
            await self.do_roarequest_async('FindTemplate', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/api/{api_id}/policy/template', 'json', req, runtime)
        )

    def validate_registry_address(
        self,
        gateway_id: str,
        request: microgw_20200810_models.ValidateRegistryAddressRequest,
    ) -> microgw_20200810_models.ValidateRegistryAddressResponse:
        """
        validateRegistryAddress
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_registry_address_with_options(gateway_id, request, headers, runtime)

    async def validate_registry_address_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.ValidateRegistryAddressRequest,
    ) -> microgw_20200810_models.ValidateRegistryAddressResponse:
        """
        validateRegistryAddress
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_registry_address_with_options_async(gateway_id, request, headers, runtime)

    def validate_registry_address_with_options(
        self,
        gateway_id: str,
        request: microgw_20200810_models.ValidateRegistryAddressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.ValidateRegistryAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.ValidateRegistryAddressResponse().from_map(
            self.do_roarequest('ValidateRegistryAddress', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/gateway/{gateway_id}/registry/validate', 'json', req, runtime)
        )

    async def validate_registry_address_with_options_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.ValidateRegistryAddressRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.ValidateRegistryAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.ValidateRegistryAddressResponse().from_map(
            await self.do_roarequest_async('ValidateRegistryAddress', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/gateway/{gateway_id}/registry/validate', 'json', req, runtime)
        )

    def get_api_detail(
        self,
        api_id: str,
    ) -> microgw_20200810_models.GetApiDetailResponse:
        """
        getApiDetail
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_api_detail_with_options(api_id, headers, runtime)

    async def get_api_detail_async(
        self,
        api_id: str,
    ) -> microgw_20200810_models.GetApiDetailResponse:
        """
        getApiDetail
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_api_detail_with_options_async(api_id, headers, runtime)

    def get_api_detail_with_options(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetApiDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetApiDetailResponse().from_map(
            self.do_roarequest('GetApiDetail', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/api/{api_id}', 'json', req, runtime)
        )

    async def get_api_detail_with_options_async(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetApiDetailResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetApiDetailResponse().from_map(
            await self.do_roarequest_async('GetApiDetail', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/api/{api_id}', 'json', req, runtime)
        )

    def create_special_route_for_registry(
        self,
        gateway_id: str,
    ) -> microgw_20200810_models.CreateSpecialRouteForRegistryResponse:
        """
        createSpecialRouteForRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_special_route_for_registry_with_options(gateway_id, headers, runtime)

    async def create_special_route_for_registry_async(
        self,
        gateway_id: str,
    ) -> microgw_20200810_models.CreateSpecialRouteForRegistryResponse:
        """
        createSpecialRouteForRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_special_route_for_registry_with_options_async(gateway_id, headers, runtime)

    def create_special_route_for_registry_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateSpecialRouteForRegistryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.CreateSpecialRouteForRegistryResponse().from_map(
            self.do_roarequest('CreateSpecialRouteForRegistry', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/gateway/{gateway_id}/registry/special/route', 'json', req, runtime)
        )

    async def create_special_route_for_registry_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateSpecialRouteForRegistryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.CreateSpecialRouteForRegistryResponse().from_map(
            await self.do_roarequest_async('CreateSpecialRouteForRegistry', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/gateway/{gateway_id}/registry/special/route', 'json', req, runtime)
        )

    def publish_api(
        self,
        api_id: str,
    ) -> microgw_20200810_models.PublishApiResponse:
        """
        publishApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_api_with_options(api_id, headers, runtime)

    async def publish_api_async(
        self,
        api_id: str,
    ) -> microgw_20200810_models.PublishApiResponse:
        """
        publishApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_api_with_options_async(api_id, headers, runtime)

    def publish_api_with_options(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.PublishApiResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.PublishApiResponse().from_map(
            self.do_roarequest('PublishApi', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/api/{api_id}/publish', 'json', req, runtime)
        )

    async def publish_api_with_options_async(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.PublishApiResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.PublishApiResponse().from_map(
            await self.do_roarequest_async('PublishApi', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/api/{api_id}/publish', 'json', req, runtime)
        )

    def create_gateway_log_etl(
        self,
        gateway_id: str,
        region_id: str,
    ) -> microgw_20200810_models.CreateGatewayLogEtlResponse:
        """
        CreateGatewayLogEtl
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_gateway_log_etl_with_options(gateway_id, region_id, headers, runtime)

    async def create_gateway_log_etl_async(
        self,
        gateway_id: str,
        region_id: str,
    ) -> microgw_20200810_models.CreateGatewayLogEtlResponse:
        """
        CreateGatewayLogEtl
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_gateway_log_etl_with_options_async(gateway_id, region_id, headers, runtime)

    def create_gateway_log_etl_with_options(
        self,
        gateway_id: str,
        region_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateGatewayLogEtlResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.CreateGatewayLogEtlResponse().from_map(
            self.do_roarequest('CreateGatewayLogEtl', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/sls/gateway/{gateway_id}/region/{{regionId}}', 'json', req, runtime)
        )

    async def create_gateway_log_etl_with_options_async(
        self,
        gateway_id: str,
        region_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateGatewayLogEtlResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.CreateGatewayLogEtlResponse().from_map(
            await self.do_roarequest_async('CreateGatewayLogEtl', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/sls/gateway/{gateway_id}/region/{{regionId}}', 'json', req, runtime)
        )

    def find_policies(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindPoliciesRequest,
    ) -> microgw_20200810_models.FindPoliciesResponse:
        """
        FindPolicies
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_policies_with_options(gateway_id, request, headers, runtime)

    async def find_policies_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindPoliciesRequest,
    ) -> microgw_20200810_models.FindPoliciesResponse:
        """
        FindPolicies
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.find_policies_with_options_async(gateway_id, request, headers, runtime)

    def find_policies_with_options(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.alias_name):
            query['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.FindPoliciesResponse().from_map(
            self.do_roarequest('FindPolicies', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}/policy', 'json', req, runtime)
        )

    async def find_policies_with_options_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.alias_name):
            query['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.group):
            query['group'] = request.group
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.FindPoliciesResponse().from_map(
            await self.do_roarequest_async('FindPolicies', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}/policy', 'json', req, runtime)
        )

    def attach_policy(
        self,
        api_id: str,
        request: microgw_20200810_models.AttachPolicyRequest,
    ) -> microgw_20200810_models.AttachPolicyResponse:
        """
        attachPolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_policy_with_options(api_id, request, headers, runtime)

    async def attach_policy_async(
        self,
        api_id: str,
        request: microgw_20200810_models.AttachPolicyRequest,
    ) -> microgw_20200810_models.AttachPolicyResponse:
        """
        attachPolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.attach_policy_with_options_async(api_id, request, headers, runtime)

    def attach_policy_with_options(
        self,
        api_id: str,
        request: microgw_20200810_models.AttachPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.data)
        )
        return microgw_20200810_models.AttachPolicyResponse().from_map(
            self.do_roarequest('AttachPolicy', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/api/{api_id}/attach', 'json', req, runtime)
        )

    async def attach_policy_with_options_async(
        self,
        api_id: str,
        request: microgw_20200810_models.AttachPolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.AttachPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.data)
        )
        return microgw_20200810_models.AttachPolicyResponse().from_map(
            await self.do_roarequest_async('AttachPolicy', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/api/{api_id}/attach', 'json', req, runtime)
        )

    def find_registry(
        self,
        registry_id: str,
    ) -> microgw_20200810_models.FindRegistryResponse:
        """
        findRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_registry_with_options(registry_id, headers, runtime)

    async def find_registry_async(
        self,
        registry_id: str,
    ) -> microgw_20200810_models.FindRegistryResponse:
        """
        findRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.find_registry_with_options_async(registry_id, headers, runtime)

    def find_registry_with_options(
        self,
        registry_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindRegistryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.FindRegistryResponse().from_map(
            self.do_roarequest('FindRegistry', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/registry/{registry_id}', 'json', req, runtime)
        )

    async def find_registry_with_options_async(
        self,
        registry_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindRegistryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.FindRegistryResponse().from_map(
            await self.do_roarequest_async('FindRegistry', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/registry/{registry_id}', 'json', req, runtime)
        )

    def get_auth_ticket_by_id(
        self,
        ticket_id: str,
    ) -> microgw_20200810_models.GetAuthTicketByIdResponse:
        """
        getAuthTicketById
        """
        runtime = util_models.RuntimeOptions()
        headers = microgw_20200810_models.GetAuthTicketByIdHeaders()
        return self.get_auth_ticket_by_id_with_options(ticket_id, headers, runtime)

    async def get_auth_ticket_by_id_async(
        self,
        ticket_id: str,
    ) -> microgw_20200810_models.GetAuthTicketByIdResponse:
        """
        getAuthTicketById
        """
        runtime = util_models.RuntimeOptions()
        headers = microgw_20200810_models.GetAuthTicketByIdHeaders()
        return await self.get_auth_ticket_by_id_with_options_async(ticket_id, headers, runtime)

    def get_auth_ticket_by_id_with_options(
        self,
        ticket_id: str,
        tmp_header: microgw_20200810_models.GetAuthTicketByIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetAuthTicketByIdResponse:
        headers = microgw_20200810_models.GetAuthTicketByIdShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.cookie):
            headers.cookie_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.cookie, 'cookie', 'json')
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.cookie_shrink):
            real_headers['cookie'] = headers.cookie_shrink
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return microgw_20200810_models.GetAuthTicketByIdResponse().from_map(
            self.do_roarequest('GetAuthTicketById', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/auth/{ticket_id}', 'json', req, runtime)
        )

    async def get_auth_ticket_by_id_with_options_async(
        self,
        ticket_id: str,
        tmp_header: microgw_20200810_models.GetAuthTicketByIdHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetAuthTicketByIdResponse:
        headers = microgw_20200810_models.GetAuthTicketByIdShrinkHeaders()
        OpenApiUtilClient.convert(tmp_header, headers)
        if not UtilClient.is_unset(tmp_header.cookie):
            headers.cookie_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_header.cookie, 'cookie', 'json')
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.cookie_shrink):
            real_headers['cookie'] = headers.cookie_shrink
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        return microgw_20200810_models.GetAuthTicketByIdResponse().from_map(
            await self.do_roarequest_async('GetAuthTicketById', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/auth/{ticket_id}', 'json', req, runtime)
        )

    def create_registry(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateRegistryRequest,
    ) -> microgw_20200810_models.CreateRegistryResponse:
        """
        CreateRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_registry_with_options(gateway_id, request, headers, runtime)

    async def create_registry_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateRegistryRequest,
    ) -> microgw_20200810_models.CreateRegistryResponse:
        """
        CreateRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_registry_with_options_async(gateway_id, request, headers, runtime)

    def create_registry_with_options(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateRegistryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateRegistryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateRegistryResponse().from_map(
            self.do_roarequest('CreateRegistry', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/registry', 'json', req, runtime)
        )

    async def create_registry_with_options_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateRegistryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateRegistryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['address'] = request.address
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateRegistryResponse().from_map(
            await self.do_roarequest_async('CreateRegistry', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/registry', 'json', req, runtime)
        )

    def recycle_api(
        self,
        api_id: str,
    ) -> microgw_20200810_models.RecycleApiResponse:
        """
        recycleApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recycle_api_with_options(api_id, headers, runtime)

    async def recycle_api_async(
        self,
        api_id: str,
    ) -> microgw_20200810_models.RecycleApiResponse:
        """
        recycleApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recycle_api_with_options_async(api_id, headers, runtime)

    def recycle_api_with_options(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.RecycleApiResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.RecycleApiResponse().from_map(
            self.do_roarequest('RecycleApi', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/api/{api_id}/recycle', 'json', req, runtime)
        )

    async def recycle_api_with_options_async(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.RecycleApiResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.RecycleApiResponse().from_map(
            await self.do_roarequest_async('RecycleApi', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/api/{api_id}/recycle', 'json', req, runtime)
        )

    def create_auth_ticket(
        self,
        request: microgw_20200810_models.CreateAuthTicketRequest,
    ) -> microgw_20200810_models.CreateAuthTicketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_auth_ticket_with_options(request, headers, runtime)

    async def create_auth_ticket_async(
        self,
        request: microgw_20200810_models.CreateAuthTicketRequest,
    ) -> microgw_20200810_models.CreateAuthTicketResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_auth_ticket_with_options_async(request, headers, runtime)

    def create_auth_ticket_with_options(
        self,
        request: microgw_20200810_models.CreateAuthTicketRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateAuthTicketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['comment'] = request.comment
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ticket_type):
            body['ticketType'] = request.ticket_type
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.jwt_signature_type_enum):
            body['jwtSignatureTypeEnum'] = request.jwt_signature_type_enum
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateAuthTicketResponse().from_map(
            self.do_roarequest('CreateAuthTicket', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/auth', 'json', req, runtime)
        )

    async def create_auth_ticket_with_options_async(
        self,
        request: microgw_20200810_models.CreateAuthTicketRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateAuthTicketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['comment'] = request.comment
        if not UtilClient.is_unset(request.gateway_id):
            body['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ticket_type):
            body['ticketType'] = request.ticket_type
        if not UtilClient.is_unset(request.duration):
            body['duration'] = request.duration
        if not UtilClient.is_unset(request.jwt_signature_type_enum):
            body['jwtSignatureTypeEnum'] = request.jwt_signature_type_enum
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateAuthTicketResponse().from_map(
            await self.do_roarequest_async('CreateAuthTicket', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/auth', 'json', req, runtime)
        )

    def delete_gateway(
        self,
        gateway_id: str,
    ) -> microgw_20200810_models.DeleteGatewayResponse:
        """
        deleteGateway
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_gateway_with_options(gateway_id, headers, runtime)

    async def delete_gateway_async(
        self,
        gateway_id: str,
    ) -> microgw_20200810_models.DeleteGatewayResponse:
        """
        deleteGateway
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_gateway_with_options_async(gateway_id, headers, runtime)

    def delete_gateway_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeleteGatewayResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteGatewayResponse().from_map(
            self.do_roarequest('DeleteGateway', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/gateway/{gateway_id}', 'json', req, runtime)
        )

    async def delete_gateway_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeleteGatewayResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteGatewayResponse().from_map(
            await self.do_roarequest_async('DeleteGateway', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/gateway/{gateway_id}', 'json', req, runtime)
        )

    def find_service(
        self,
        service_id: str,
    ) -> microgw_20200810_models.FindServiceResponse:
        """
        findService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_service_with_options(service_id, headers, runtime)

    async def find_service_async(
        self,
        service_id: str,
    ) -> microgw_20200810_models.FindServiceResponse:
        """
        findService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.find_service_with_options_async(service_id, headers, runtime)

    def find_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.FindServiceResponse().from_map(
            self.do_roarequest('FindService', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/service/{service_id}', 'json', req, runtime)
        )

    async def find_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.FindServiceResponse().from_map(
            await self.do_roarequest_async('FindService', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/service/{service_id}', 'json', req, runtime)
        )

    def delete_policy_by_id(
        self,
        policy_id: str,
    ) -> microgw_20200810_models.DeletePolicyByIdResponse:
        """
        DeletePolicyById
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_policy_by_id_with_options(policy_id, headers, runtime)

    async def delete_policy_by_id_async(
        self,
        policy_id: str,
    ) -> microgw_20200810_models.DeletePolicyByIdResponse:
        """
        DeletePolicyById
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_policy_by_id_with_options_async(policy_id, headers, runtime)

    def delete_policy_by_id_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeletePolicyByIdResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeletePolicyByIdResponse().from_map(
            self.do_roarequest('DeletePolicyById', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/policy/{policy_id}', 'json', req, runtime)
        )

    async def delete_policy_by_id_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeletePolicyByIdResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeletePolicyByIdResponse().from_map(
            await self.do_roarequest_async('DeletePolicyById', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/policy/{policy_id}', 'json', req, runtime)
        )

    def delete_api(
        self,
        api_id: str,
    ) -> microgw_20200810_models.DeleteApiResponse:
        """
        deleteApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_api_with_options(api_id, headers, runtime)

    async def delete_api_async(
        self,
        api_id: str,
    ) -> microgw_20200810_models.DeleteApiResponse:
        """
        deleteApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_api_with_options_async(api_id, headers, runtime)

    def delete_api_with_options(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeleteApiResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteApiResponse().from_map(
            self.do_roarequest('DeleteApi', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/api/{api_id}', 'json', req, runtime)
        )

    async def delete_api_with_options_async(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeleteApiResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteApiResponse().from_map(
            await self.do_roarequest_async('DeleteApi', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/api/{api_id}', 'json', req, runtime)
        )

    def find_auth_tickets(
        self,
        request: microgw_20200810_models.FindAuthTicketsRequest,
    ) -> microgw_20200810_models.FindAuthTicketsResponse:
        """
        findAuthTickets
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_auth_tickets_with_options(request, headers, runtime)

    async def find_auth_tickets_async(
        self,
        request: microgw_20200810_models.FindAuthTicketsRequest,
    ) -> microgw_20200810_models.FindAuthTicketsResponse:
        """
        findAuthTickets
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.find_auth_tickets_with_options_async(request, headers, runtime)

    def find_auth_tickets_with_options(
        self,
        request: microgw_20200810_models.FindAuthTicketsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindAuthTicketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.FindAuthTicketsResponse().from_map(
            self.do_roarequest('FindAuthTickets', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/auth', 'json', req, runtime)
        )

    async def find_auth_tickets_with_options_async(
        self,
        request: microgw_20200810_models.FindAuthTicketsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindAuthTicketsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_id):
            query['gatewayId'] = request.gateway_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.FindAuthTicketsResponse().from_map(
            await self.do_roarequest_async('FindAuthTickets', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/auth', 'json', req, runtime)
        )

    def update_policy(
        self,
        request: microgw_20200810_models.UpdatePolicyRequest,
    ) -> microgw_20200810_models.UpdatePolicyResponse:
        """
        updatePolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_policy_with_options(request, headers, runtime)

    async def update_policy_async(
        self,
        request: microgw_20200810_models.UpdatePolicyRequest,
    ) -> microgw_20200810_models.UpdatePolicyResponse:
        """
        updatePolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_policy_with_options_async(request, headers, runtime)

    def update_policy_with_options(
        self,
        request: microgw_20200810_models.UpdatePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdatePolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.policy_group):
            body['policyGroup'] = request.policy_group
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdatePolicyResponse().from_map(
            self.do_roarequest('UpdatePolicy', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/policy', 'json', req, runtime)
        )

    async def update_policy_with_options_async(
        self,
        request: microgw_20200810_models.UpdatePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdatePolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.policy_group):
            body['policyGroup'] = request.policy_group
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdatePolicyResponse().from_map(
            await self.do_roarequest_async('UpdatePolicy', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/policy', 'json', req, runtime)
        )

    def update_auth_ticket(
        self,
        request: microgw_20200810_models.UpdateAuthTicketRequest,
    ) -> microgw_20200810_models.UpdateAuthTicketResponse:
        """
        updateAuthTicket
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_auth_ticket_with_options(request, headers, runtime)

    async def update_auth_ticket_async(
        self,
        request: microgw_20200810_models.UpdateAuthTicketRequest,
    ) -> microgw_20200810_models.UpdateAuthTicketResponse:
        """
        updateAuthTicket
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_auth_ticket_with_options_async(request, headers, runtime)

    def update_auth_ticket_with_options(
        self,
        request: microgw_20200810_models.UpdateAuthTicketRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateAuthTicketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['comment'] = request.comment
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateAuthTicketResponse().from_map(
            self.do_roarequest('UpdateAuthTicket', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/auth', 'json', req, runtime)
        )

    async def update_auth_ticket_with_options_async(
        self,
        request: microgw_20200810_models.UpdateAuthTicketRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateAuthTicketResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['comment'] = request.comment
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateAuthTicketResponse().from_map(
            await self.do_roarequest_async('UpdateAuthTicket', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/auth', 'json', req, runtime)
        )

    def install_arms_agent(
        self,
        gateway_id: str,
    ) -> microgw_20200810_models.InstallArmsAgentResponse:
        """
        installArmsAgent
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_arms_agent_with_options(gateway_id, headers, runtime)

    async def install_arms_agent_async(
        self,
        gateway_id: str,
    ) -> microgw_20200810_models.InstallArmsAgentResponse:
        """
        installArmsAgent
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.install_arms_agent_with_options_async(gateway_id, headers, runtime)

    def install_arms_agent_with_options(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.InstallArmsAgentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.InstallArmsAgentResponse().from_map(
            self.do_roarequest('InstallArmsAgent', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/agent/{gateway_id}', 'json', req, runtime)
        )

    async def install_arms_agent_with_options_async(
        self,
        gateway_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.InstallArmsAgentResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.InstallArmsAgentResponse().from_map(
            await self.do_roarequest_async('InstallArmsAgent', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/agent/{gateway_id}', 'json', req, runtime)
        )

    def delete_auth_ticket(
        self,
        ticket_id: str,
    ) -> microgw_20200810_models.DeleteAuthTicketResponse:
        """
        deleteAuthTicket
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_auth_ticket_with_options(ticket_id, headers, runtime)

    async def delete_auth_ticket_async(
        self,
        ticket_id: str,
    ) -> microgw_20200810_models.DeleteAuthTicketResponse:
        """
        deleteAuthTicket
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_auth_ticket_with_options_async(ticket_id, headers, runtime)

    def delete_auth_ticket_with_options(
        self,
        ticket_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeleteAuthTicketResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteAuthTicketResponse().from_map(
            self.do_roarequest('DeleteAuthTicket', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/auth/{ticket_id}', 'json', req, runtime)
        )

    async def delete_auth_ticket_with_options_async(
        self,
        ticket_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeleteAuthTicketResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteAuthTicketResponse().from_map(
            await self.do_roarequest_async('DeleteAuthTicket', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/auth/{ticket_id}', 'json', req, runtime)
        )

    def get_policy_by_id(
        self,
        policy_id: str,
    ) -> microgw_20200810_models.GetPolicyByIdResponse:
        """
        GetPolicyById
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_policy_by_id_with_options(policy_id, headers, runtime)

    async def get_policy_by_id_async(
        self,
        policy_id: str,
    ) -> microgw_20200810_models.GetPolicyByIdResponse:
        """
        GetPolicyById
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_policy_by_id_with_options_async(policy_id, headers, runtime)

    def get_policy_by_id_with_options(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetPolicyByIdResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetPolicyByIdResponse().from_map(
            self.do_roarequest('GetPolicyById', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/policy/{policy_id}', 'json', req, runtime)
        )

    async def get_policy_by_id_with_options_async(
        self,
        policy_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetPolicyByIdResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetPolicyByIdResponse().from_map(
            await self.do_roarequest_async('GetPolicyById', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/policy/{policy_id}', 'json', req, runtime)
        )

    def delete_registry(
        self,
        registry_id: str,
    ) -> microgw_20200810_models.DeleteRegistryResponse:
        """
        deleteRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_registry_with_options(registry_id, headers, runtime)

    async def delete_registry_async(
        self,
        registry_id: str,
    ) -> microgw_20200810_models.DeleteRegistryResponse:
        """
        deleteRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_registry_with_options_async(registry_id, headers, runtime)

    def delete_registry_with_options(
        self,
        registry_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeleteRegistryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteRegistryResponse().from_map(
            self.do_roarequest('DeleteRegistry', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/registry/{registry_id}', 'json', req, runtime)
        )

    async def delete_registry_with_options_async(
        self,
        registry_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.DeleteRegistryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteRegistryResponse().from_map(
            await self.do_roarequest_async('DeleteRegistry', '2020-08-10', 'HTTPS', 'DELETE', 'AK', f'/v1/registry/{registry_id}', 'json', req, runtime)
        )

    def get_policy_owned_by_api(
        self,
        api_id: str,
    ) -> microgw_20200810_models.GetPolicyOwnedByApiResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_policy_owned_by_api_with_options(api_id, headers, runtime)

    async def get_policy_owned_by_api_async(
        self,
        api_id: str,
    ) -> microgw_20200810_models.GetPolicyOwnedByApiResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_policy_owned_by_api_with_options_async(api_id, headers, runtime)

    def get_policy_owned_by_api_with_options(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetPolicyOwnedByApiResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetPolicyOwnedByApiResponse().from_map(
            self.do_roarequest('GetPolicyOwnedByApi', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/api/{api_id}/policy', 'json', req, runtime)
        )

    async def get_policy_owned_by_api_with_options_async(
        self,
        api_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetPolicyOwnedByApiResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetPolicyOwnedByApiResponse().from_map(
            await self.do_roarequest_async('GetPolicyOwnedByApi', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/api/{api_id}/policy', 'json', req, runtime)
        )

    def update_api(
        self,
        api_id: str,
        request: microgw_20200810_models.UpdateApiRequest,
    ) -> microgw_20200810_models.UpdateApiResponse:
        """
        updateApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_api_with_options(api_id, request, headers, runtime)

    async def update_api_async(
        self,
        api_id: str,
        request: microgw_20200810_models.UpdateApiRequest,
    ) -> microgw_20200810_models.UpdateApiResponse:
        """
        updateApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_api_with_options_async(api_id, request, headers, runtime)

    def update_api_with_options(
        self,
        api_id: str,
        request: microgw_20200810_models.UpdateApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateApiResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.attached_services):
            body['attachedServices'] = request.attached_services
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.creation_date_time):
            body['creationDateTime'] = request.creation_date_time
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ownered_policies):
            body['owneredPolicies'] = request.ownered_policies
        if not UtilClient.is_unset(request.published_gateway):
            body['publishedGateway'] = request.published_gateway
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.update_date_time):
            body['updateDateTime'] = request.update_date_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateApiResponse().from_map(
            self.do_roarequest('UpdateApi', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/api/{api_id}', 'json', req, runtime)
        )

    async def update_api_with_options_async(
        self,
        api_id: str,
        request: microgw_20200810_models.UpdateApiRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateApiResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.attached_services):
            body['attachedServices'] = request.attached_services
        if not UtilClient.is_unset(request.base_path):
            body['basePath'] = request.base_path
        if not UtilClient.is_unset(request.creation_date_time):
            body['creationDateTime'] = request.creation_date_time
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ownered_policies):
            body['owneredPolicies'] = request.ownered_policies
        if not UtilClient.is_unset(request.published_gateway):
            body['publishedGateway'] = request.published_gateway
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.update_date_time):
            body['updateDateTime'] = request.update_date_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateApiResponse().from_map(
            await self.do_roarequest_async('UpdateApi', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/api/{api_id}', 'json', req, runtime)
        )

    def create_service(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateServiceRequest,
    ) -> microgw_20200810_models.CreateServiceResponse:
        """
        /gateway/{gatewayId}/service
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(gateway_id, request, headers, runtime)

    async def create_service_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateServiceRequest,
    ) -> microgw_20200810_models.CreateServiceResponse:
        """
        /gateway/{gatewayId}/service
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(gateway_id, request, headers, runtime)

    def create_service_with_options(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.is_auto_refresh):
            body['isAutoRefresh'] = request.is_auto_refresh
        if not UtilClient.is_unset(request.meta_info):
            body['metaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.registry_id):
            body['registryId'] = request.registry_id
        if not UtilClient.is_unset(request.service_ends):
            body['serviceEnds'] = request.service_ends
        if not UtilClient.is_unset(request.service_name_in_registry):
            body['serviceNameInRegistry'] = request.service_name_in_registry
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateServiceResponse().from_map(
            self.do_roarequest('CreateService', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/gateway/{gateway_id}/service', 'json', req, runtime)
        )

    async def create_service_with_options_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.is_auto_refresh):
            body['isAutoRefresh'] = request.is_auto_refresh
        if not UtilClient.is_unset(request.meta_info):
            body['metaInfo'] = request.meta_info
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.registry_id):
            body['registryId'] = request.registry_id
        if not UtilClient.is_unset(request.service_ends):
            body['serviceEnds'] = request.service_ends
        if not UtilClient.is_unset(request.service_name_in_registry):
            body['serviceNameInRegistry'] = request.service_name_in_registry
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateServiceResponse().from_map(
            await self.do_roarequest_async('CreateService', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/gateway/{gateway_id}/service', 'json', req, runtime)
        )

    def save_all_policies(
        self,
        api_id: str,
        request: microgw_20200810_models.SaveAllPoliciesRequest,
    ) -> microgw_20200810_models.SaveAllPoliciesResponse:
        """
        saveAllPolicies
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_all_policies_with_options(api_id, request, headers, runtime)

    async def save_all_policies_async(
        self,
        api_id: str,
        request: microgw_20200810_models.SaveAllPoliciesRequest,
    ) -> microgw_20200810_models.SaveAllPoliciesResponse:
        """
        saveAllPolicies
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_all_policies_with_options_async(api_id, request, headers, runtime)

    def save_all_policies_with_options(
        self,
        api_id: str,
        request: microgw_20200810_models.SaveAllPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.SaveAllPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.data)
        )
        return microgw_20200810_models.SaveAllPoliciesResponse().from_map(
            self.do_roarequest('SaveAllPolicies', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/api/{api_id}/policies', 'json', req, runtime)
        )

    async def save_all_policies_with_options_async(
        self,
        api_id: str,
        request: microgw_20200810_models.SaveAllPoliciesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.SaveAllPoliciesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.data)
        )
        return microgw_20200810_models.SaveAllPoliciesResponse().from_map(
            await self.do_roarequest_async('SaveAllPolicies', '2020-08-10', 'HTTPS', 'POST', 'AK', f'/v1/api/{api_id}/policies', 'json', req, runtime)
        )

    def update_gateway(
        self,
        request: microgw_20200810_models.UpdateGatewayRequest,
    ) -> microgw_20200810_models.UpdateGatewayResponse:
        """
        updateGateway
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_gateway_with_options(request, headers, runtime)

    async def update_gateway_async(
        self,
        request: microgw_20200810_models.UpdateGatewayRequest,
    ) -> microgw_20200810_models.UpdateGatewayResponse:
        """
        updateGateway
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_gateway_with_options_async(request, headers, runtime)

    def update_gateway_with_options(
        self,
        request: microgw_20200810_models.UpdateGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.replica):
            body['replica'] = request.replica
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateGatewayResponse().from_map(
            self.do_roarequest('UpdateGateway', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/gateway', 'json', req, runtime)
        )

    async def update_gateway_with_options_async(
        self,
        request: microgw_20200810_models.UpdateGatewayRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateGatewayResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.replica):
            body['replica'] = request.replica
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateGatewayResponse().from_map(
            await self.do_roarequest_async('UpdateGateway', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/gateway', 'json', req, runtime)
        )

    def update_service(
        self,
        service_id: str,
        request: microgw_20200810_models.UpdateServiceRequest,
    ) -> microgw_20200810_models.UpdateServiceResponse:
        """
        updateService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_with_options(service_id, request, headers, runtime)

    async def update_service_async(
        self,
        service_id: str,
        request: microgw_20200810_models.UpdateServiceRequest,
    ) -> microgw_20200810_models.UpdateServiceResponse:
        """
        updateService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_with_options_async(service_id, request, headers, runtime)

    def update_service_with_options(
        self,
        service_id: str,
        request: microgw_20200810_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.creation_date_time):
            body['creationDateTime'] = request.creation_date_time
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.is_auto_refresh):
            body['isAutoRefresh'] = request.is_auto_refresh
        if not UtilClient.is_unset(request.is_health):
            body['isHealth'] = request.is_health
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.registry_id):
            body['registryId'] = request.registry_id
        if not UtilClient.is_unset(request.service_ends):
            body['serviceEnds'] = request.service_ends
        if not UtilClient.is_unset(request.service_name_in_registry):
            body['serviceNameInRegistry'] = request.service_name_in_registry
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.update_date_time):
            body['updateDateTime'] = request.update_date_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateServiceResponse().from_map(
            self.do_roarequest('UpdateService', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/service/{service_id}', 'json', req, runtime)
        )

    async def update_service_with_options_async(
        self,
        service_id: str,
        request: microgw_20200810_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['aliasName'] = request.alias_name
        if not UtilClient.is_unset(request.creation_date_time):
            body['creationDateTime'] = request.creation_date_time
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.is_auto_refresh):
            body['isAutoRefresh'] = request.is_auto_refresh
        if not UtilClient.is_unset(request.is_health):
            body['isHealth'] = request.is_health
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.registry_id):
            body['registryId'] = request.registry_id
        if not UtilClient.is_unset(request.service_ends):
            body['serviceEnds'] = request.service_ends
        if not UtilClient.is_unset(request.service_name_in_registry):
            body['serviceNameInRegistry'] = request.service_name_in_registry
        if not UtilClient.is_unset(request.source_type):
            body['sourceType'] = request.source_type
        if not UtilClient.is_unset(request.update_date_time):
            body['updateDateTime'] = request.update_date_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateServiceResponse().from_map(
            await self.do_roarequest_async('UpdateService', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/service/{service_id}', 'json', req, runtime)
        )

    def find_apis_by_paging(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindApisByPagingRequest,
    ) -> microgw_20200810_models.FindApisByPagingResponse:
        """
        findApisByPaging
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_apis_by_paging_with_options(gateway_id, request, headers, runtime)

    async def find_apis_by_paging_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindApisByPagingRequest,
    ) -> microgw_20200810_models.FindApisByPagingResponse:
        """
        findApisByPaging
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.find_apis_by_paging_with_options_async(gateway_id, request, headers, runtime)

    def find_apis_by_paging_with_options(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindApisByPagingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindApisByPagingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.alias_name):
            query['aliasName'] = request.alias_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.FindApisByPagingResponse().from_map(
            self.do_roarequest('FindApisByPaging', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}/api', 'json', req, runtime)
        )

    async def find_apis_by_paging_with_options_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.FindApisByPagingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindApisByPagingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.alias_name):
            query['aliasName'] = request.alias_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.FindApisByPagingResponse().from_map(
            await self.do_roarequest_async('FindApisByPaging', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}/api', 'json', req, runtime)
        )

    def update_service_ends(
        self,
        service_id: str,
        request: microgw_20200810_models.UpdateServiceEndsRequest,
    ) -> microgw_20200810_models.UpdateServiceEndsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_ends_with_options(service_id, request, headers, runtime)

    async def update_service_ends_async(
        self,
        service_id: str,
        request: microgw_20200810_models.UpdateServiceEndsRequest,
    ) -> microgw_20200810_models.UpdateServiceEndsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_ends_with_options_async(service_id, request, headers, runtime)

    def update_service_ends_with_options(
        self,
        service_id: str,
        request: microgw_20200810_models.UpdateServiceEndsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateServiceEndsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.service_nodes):
            body['serviceNodes'] = request.service_nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateServiceEndsResponse().from_map(
            self.do_roarequest('UpdateServiceEnds', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/service/{service_id}/serviceends', 'json', req, runtime)
        )

    async def update_service_ends_with_options_async(
        self,
        service_id: str,
        request: microgw_20200810_models.UpdateServiceEndsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.UpdateServiceEndsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['id'] = request.id
        if not UtilClient.is_unset(request.service_nodes):
            body['serviceNodes'] = request.service_nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.UpdateServiceEndsResponse().from_map(
            await self.do_roarequest_async('UpdateServiceEnds', '2020-08-10', 'HTTPS', 'PUT', 'AK', f'/v1/service/{service_id}/serviceends', 'json', req, runtime)
        )

    def find_gateways(
        self,
        request: microgw_20200810_models.FindGatewaysRequest,
    ) -> microgw_20200810_models.FindGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_gateways_with_options(request, headers, runtime)

    async def find_gateways_async(
        self,
        request: microgw_20200810_models.FindGatewaysRequest,
    ) -> microgw_20200810_models.FindGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.find_gateways_with_options_async(request, headers, runtime)

    def find_gateways_with_options(
        self,
        request: microgw_20200810_models.FindGatewaysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindGatewaysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['gatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.gateway_types):
            query['gatewayTypes'] = request.gateway_types
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.FindGatewaysResponse().from_map(
            self.do_roarequest('FindGateways', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway', 'json', req, runtime)
        )

    async def find_gateways_with_options_async(
        self,
        request: microgw_20200810_models.FindGatewaysRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.FindGatewaysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gateway_unique_id):
            query['gatewayUniqueId'] = request.gateway_unique_id
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.gateway_types):
            query['gatewayTypes'] = request.gateway_types
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.FindGatewaysResponse().from_map(
            await self.do_roarequest_async('FindGateways', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway', 'json', req, runtime)
        )

    def get_all_registry(
        self,
        gateway_id: str,
        request: microgw_20200810_models.GetAllRegistryRequest,
    ) -> microgw_20200810_models.GetAllRegistryResponse:
        """
        getAllRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_all_registry_with_options(gateway_id, request, headers, runtime)

    async def get_all_registry_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.GetAllRegistryRequest,
    ) -> microgw_20200810_models.GetAllRegistryResponse:
        """
        getAllRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_all_registry_with_options_async(gateway_id, request, headers, runtime)

    def get_all_registry_with_options(
        self,
        gateway_id: str,
        request: microgw_20200810_models.GetAllRegistryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetAllRegistryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.group_by):
            query['groupBy'] = request.group_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.GetAllRegistryResponse().from_map(
            self.do_roarequest('GetAllRegistry', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}/registry', 'json', req, runtime)
        )

    async def get_all_registry_with_options_async(
        self,
        gateway_id: str,
        request: microgw_20200810_models.GetAllRegistryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.GetAllRegistryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        if not UtilClient.is_unset(request.group_by):
            query['groupBy'] = request.group_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.GetAllRegistryResponse().from_map(
            await self.do_roarequest_async('GetAllRegistry', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/gateway/{gateway_id}/registry', 'json', req, runtime)
        )

    def pull_service_info_from_registry(
        self,
        registry_id: str,
    ) -> microgw_20200810_models.PullServiceInfoFromRegistryResponse:
        """
        pullServiceInfoFromRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pull_service_info_from_registry_with_options(registry_id, headers, runtime)

    async def pull_service_info_from_registry_async(
        self,
        registry_id: str,
    ) -> microgw_20200810_models.PullServiceInfoFromRegistryResponse:
        """
        pullServiceInfoFromRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.pull_service_info_from_registry_with_options_async(registry_id, headers, runtime)

    def pull_service_info_from_registry_with_options(
        self,
        registry_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.PullServiceInfoFromRegistryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.PullServiceInfoFromRegistryResponse().from_map(
            self.do_roarequest('PullServiceInfoFromRegistry', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/registry/{registry_id}/pull', 'json', req, runtime)
        )

    async def pull_service_info_from_registry_with_options_async(
        self,
        registry_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> microgw_20200810_models.PullServiceInfoFromRegistryResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.PullServiceInfoFromRegistryResponse().from_map(
            await self.do_roarequest_async('PullServiceInfoFromRegistry', '2020-08-10', 'HTTPS', 'GET', 'AK', f'/v1/registry/{registry_id}/pull', 'json', req, runtime)
        )
