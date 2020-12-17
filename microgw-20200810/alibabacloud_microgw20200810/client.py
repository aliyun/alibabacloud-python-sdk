# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_microgw20200810 import models as microgw_20200810_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('microgw', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def find_all_service(self, gateway_id, request):
        """
        findAllService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_all_service_with_options(gateway_id, request, headers, runtime)

    def find_all_service_with_options(self, gateway_id, request, headers, runtime):
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
        return microgw_20200810_models.FindAllServiceResponse().from_map(self.do_roarequest('FindAllService', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/gateway/%s/service' % gateway_id, 'json', req, runtime))

    def create_api(self, gateway_id, request):
        """
        createApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_api_with_options(gateway_id, request, headers, runtime)

    def create_api_with_options(self, gateway_id, request, headers, runtime):
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
        return microgw_20200810_models.CreateApiResponse().from_map(self.do_roarequest('CreateApi', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/gateway/%s/api' % gateway_id, 'json', req, runtime))

    def get_gateway_by_id(self, gateway_id):
        """
        getGatewayById
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_gateway_by_id_with_options(gateway_id, headers, runtime)

    def get_gateway_by_id_with_options(self, gateway_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetGatewayByIdResponse().from_map(self.do_roarequest('GetGatewayById', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/gateway/%s' % gateway_id, 'json', req, runtime))

    def create_policy(self, request):
        """
        createPolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_policy_with_options(request, headers, runtime)

    def create_policy_with_options(self, request, headers, runtime):
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
        return microgw_20200810_models.CreatePolicyResponse().from_map(self.do_roarequest('CreatePolicy', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/policy', 'json', req, runtime))

    def get_service_instance_for_registry_by_service_name(self, gateway_id, registry_id, request):
        """
        getServiceInstanceForRegistryByServiceName
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_instance_for_registry_by_service_name_with_options(gateway_id, registry_id, request, headers, runtime)

    def get_service_instance_for_registry_by_service_name_with_options(self, gateway_id, registry_id, request, headers, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return microgw_20200810_models.GetServiceInstanceForRegistryByServiceNameResponse().from_map(self.do_roarequest('GetServiceInstanceForRegistryByServiceName', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/gateway/%s/registry/{registryId}/service' % gateway_id, 'json', req, runtime))

    def delete_service(self, service_id):
        """
        deleteService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(service_id, headers, runtime)

    def delete_service_with_options(self, service_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteServiceResponse().from_map(self.do_roarequest('DeleteService', '2020-08-10', 'HTTPS', 'DELETE', 'AK', '/v1/service/%s' % service_id, 'json', req, runtime))

    def update_registry(self, registry_id, request):
        """
        UpdateRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_registry_with_options(registry_id, request, headers, runtime)

    def update_registry_with_options(self, registry_id, request, headers, runtime):
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
        return microgw_20200810_models.UpdateRegistryResponse().from_map(self.do_roarequest('UpdateRegistry', '2020-08-10', 'HTTPS', 'PUT', 'AK', '/v1/registry/%s' % registry_id, 'json', req, runtime))

    def create_gateway(self, request):
        """
        createGateway
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_gateway_with_options(request, headers, runtime)

    def create_gateway_with_options(self, request, headers, runtime):
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
        return microgw_20200810_models.CreateGatewayResponse().from_map(self.do_roarequest('CreateGateway', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/gateway', 'json', req, runtime))

    def check_service_health(self, request):
        """
        checkServiceHealth
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_service_health_with_options(request, headers, runtime)

    def check_service_health_with_options(self, request, headers, runtime):
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
        return microgw_20200810_models.CheckServiceHealthResponse().from_map(self.do_roarequest('CheckServiceHealth', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/service/check', 'json', req, runtime))

    def create_policy_to_api(self, api_id, request):
        """
        createPolicyToApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_policy_to_api_with_options(api_id, request, headers, runtime)

    def create_policy_to_api_with_options(self, api_id, request, headers, runtime):
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
        return microgw_20200810_models.CreatePolicyToApiResponse().from_map(self.do_roarequest('CreatePolicyToApi', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/api/%s/policy' % api_id, 'json', req, runtime))

    def detach_policy(self, api_id, policy_id):
        """
        detachPolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.detach_policy_with_options(api_id, policy_id, headers, runtime)

    def detach_policy_with_options(self, api_id, policy_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DetachPolicyResponse().from_map(self.do_roarequest('DetachPolicy', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/api/%s/detach/{policyId}' % api_id, 'json', req, runtime))

    def find_template(self, api_id):
        """
        findTemplate
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_template_with_options(api_id, headers, runtime)

    def find_template_with_options(self, api_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.FindTemplateResponse().from_map(self.do_roarequest('FindTemplate', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/api/%s/policy/template' % api_id, 'json', req, runtime))

    def validate_registry_address(self, gateway_id, request):
        """
        validateRegistryAddress
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_registry_address_with_options(gateway_id, request, headers, runtime)

    def validate_registry_address_with_options(self, gateway_id, request, headers, runtime):
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
        return microgw_20200810_models.ValidateRegistryAddressResponse().from_map(self.do_roarequest('ValidateRegistryAddress', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/gateway/%s/registry/validate' % gateway_id, 'json', req, runtime))

    def get_api_detail(self, api_id):
        """
        getApiDetail
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_api_detail_with_options(api_id, headers, runtime)

    def get_api_detail_with_options(self, api_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetApiDetailResponse().from_map(self.do_roarequest('GetApiDetail', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/api/%s' % api_id, 'json', req, runtime))

    def create_special_route_for_registry(self, gateway_id):
        """
        createSpecialRouteForRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_special_route_for_registry_with_options(gateway_id, headers, runtime)

    def create_special_route_for_registry_with_options(self, gateway_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.CreateSpecialRouteForRegistryResponse().from_map(self.do_roarequest('CreateSpecialRouteForRegistry', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/gateway/%s/registry/special/route' % gateway_id, 'json', req, runtime))

    def publish_api(self, api_id):
        """
        publishApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_api_with_options(api_id, headers, runtime)

    def publish_api_with_options(self, api_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.PublishApiResponse().from_map(self.do_roarequest('PublishApi', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/api/%s/publish' % api_id, 'json', req, runtime))

    def create_gateway_log_etl(self, gateway_id, region_id):
        """
        CreateGatewayLogEtl
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_gateway_log_etl_with_options(gateway_id, region_id, headers, runtime)

    def create_gateway_log_etl_with_options(self, gateway_id, region_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.CreateGatewayLogEtlResponse().from_map(self.do_roarequest('CreateGatewayLogEtl', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/sls/gateway/%s/region/{regionId}' % gateway_id, 'json', req, runtime))

    def find_policies(self, gateway_id, request):
        """
        FindPolicies
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_policies_with_options(gateway_id, request, headers, runtime)

    def find_policies_with_options(self, gateway_id, request, headers, runtime):
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
        return microgw_20200810_models.FindPoliciesResponse().from_map(self.do_roarequest('FindPolicies', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/gateway/%s/policy' % gateway_id, 'json', req, runtime))

    def attach_policy(self, api_id, request):
        """
        attachPolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.attach_policy_with_options(api_id, request, headers, runtime)

    def attach_policy_with_options(self, api_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.data)
        )
        return microgw_20200810_models.AttachPolicyResponse().from_map(self.do_roarequest('AttachPolicy', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/api/%s/attach' % api_id, 'json', req, runtime))

    def find_registry(self, registry_id):
        """
        findRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_registry_with_options(registry_id, headers, runtime)

    def find_registry_with_options(self, registry_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.FindRegistryResponse().from_map(self.do_roarequest('FindRegistry', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/registry/%s' % registry_id, 'json', req, runtime))

    def get_auth_ticket_by_id(self, ticket_id):
        """
        getAuthTicketById
        """
        runtime = util_models.RuntimeOptions()
        headers = microgw_20200810_models.GetAuthTicketByIdHeaders()
        return self.get_auth_ticket_by_id_with_options(ticket_id, headers, runtime)

    def get_auth_ticket_by_id_with_options(self, ticket_id, tmp_header, runtime):
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
        return microgw_20200810_models.GetAuthTicketByIdResponse().from_map(self.do_roarequest('GetAuthTicketById', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/auth/%s' % ticket_id, 'json', req, runtime))

    def create_registry(self, gateway_id, request):
        """
        CreateRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_registry_with_options(gateway_id, request, headers, runtime)

    def create_registry_with_options(self, gateway_id, request, headers, runtime):
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
        return microgw_20200810_models.CreateRegistryResponse().from_map(self.do_roarequest('CreateRegistry', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/registry', 'json', req, runtime))

    def recycle_api(self, api_id):
        """
        recycleApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recycle_api_with_options(api_id, headers, runtime)

    def recycle_api_with_options(self, api_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.RecycleApiResponse().from_map(self.do_roarequest('RecycleApi', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/api/%s/recycle' % api_id, 'json', req, runtime))

    def create_auth_ticket(self, request):
        """
        createAuthTicket
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_auth_ticket_with_options(request, headers, runtime)

    def create_auth_ticket_with_options(self, request, headers, runtime):
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
        if not UtilClient.is_unset(request.valid_duration):
            body['validDuration'] = request.valid_duration
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return microgw_20200810_models.CreateAuthTicketResponse().from_map(self.do_roarequest('CreateAuthTicket', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/auth', 'json', req, runtime))

    def delete_gateway(self, gateway_id):
        """
        deleteGateway
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_gateway_with_options(gateway_id, headers, runtime)

    def delete_gateway_with_options(self, gateway_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteGatewayResponse().from_map(self.do_roarequest('DeleteGateway', '2020-08-10', 'HTTPS', 'DELETE', 'AK', '/v1/gateway/%s' % gateway_id, 'json', req, runtime))

    def find_service(self, service_id):
        """
        findService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_service_with_options(service_id, headers, runtime)

    def find_service_with_options(self, service_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.FindServiceResponse().from_map(self.do_roarequest('FindService', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/service/%s' % service_id, 'json', req, runtime))

    def delete_policy_by_id(self, policy_id):
        """
        DeletePolicyById
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_policy_by_id_with_options(policy_id, headers, runtime)

    def delete_policy_by_id_with_options(self, policy_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeletePolicyByIdResponse().from_map(self.do_roarequest('DeletePolicyById', '2020-08-10', 'HTTPS', 'DELETE', 'AK', '/v1/policy/%s' % policy_id, 'json', req, runtime))

    def delete_api(self, api_id):
        """
        deleteApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_api_with_options(api_id, headers, runtime)

    def delete_api_with_options(self, api_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteApiResponse().from_map(self.do_roarequest('DeleteApi', '2020-08-10', 'HTTPS', 'DELETE', 'AK', '/v1/api/%s' % api_id, 'json', req, runtime))

    def find_auth_tickets(self, request):
        """
        findAuthTickets
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_auth_tickets_with_options(request, headers, runtime)

    def find_auth_tickets_with_options(self, request, headers, runtime):
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
        return microgw_20200810_models.FindAuthTicketsResponse().from_map(self.do_roarequest('FindAuthTickets', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/auth', 'json', req, runtime))

    def update_policy(self, request):
        """
        updatePolicy
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_policy_with_options(request, headers, runtime)

    def update_policy_with_options(self, request, headers, runtime):
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
        return microgw_20200810_models.UpdatePolicyResponse().from_map(self.do_roarequest('UpdatePolicy', '2020-08-10', 'HTTPS', 'PUT', 'AK', '/v1/policy', 'json', req, runtime))

    def update_auth_ticket(self, request):
        """
        updateAuthTicket
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_auth_ticket_with_options(request, headers, runtime)

    def update_auth_ticket_with_options(self, request, headers, runtime):
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
        return microgw_20200810_models.UpdateAuthTicketResponse().from_map(self.do_roarequest('UpdateAuthTicket', '2020-08-10', 'HTTPS', 'PUT', 'AK', '/v1/auth', 'json', req, runtime))

    def install_arms_agent(self, gateway_id):
        """
        installArmsAgent
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.install_arms_agent_with_options(gateway_id, headers, runtime)

    def install_arms_agent_with_options(self, gateway_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.InstallArmsAgentResponse().from_map(self.do_roarequest('InstallArmsAgent', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/gateway/agent/%s' % gateway_id, 'json', req, runtime))

    def delete_auth_ticket(self, ticket_id):
        """
        deleteAuthTicket
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_auth_ticket_with_options(ticket_id, headers, runtime)

    def delete_auth_ticket_with_options(self, ticket_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteAuthTicketResponse().from_map(self.do_roarequest('DeleteAuthTicket', '2020-08-10', 'HTTPS', 'DELETE', 'AK', '/v1/auth/%s' % ticket_id, 'json', req, runtime))

    def get_policy_by_id(self, policy_id):
        """
        GetPolicyById
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_policy_by_id_with_options(policy_id, headers, runtime)

    def get_policy_by_id_with_options(self, policy_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetPolicyByIdResponse().from_map(self.do_roarequest('GetPolicyById', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/policy/%s' % policy_id, 'json', req, runtime))

    def delete_registry(self, registry_id):
        """
        deleteRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_registry_with_options(registry_id, headers, runtime)

    def delete_registry_with_options(self, registry_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.DeleteRegistryResponse().from_map(self.do_roarequest('DeleteRegistry', '2020-08-10', 'HTTPS', 'DELETE', 'AK', '/v1/registry/%s' % registry_id, 'json', req, runtime))

    def get_policy_owned_by_api(self, api_id):
        """
        getPolicyOwnedByApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_policy_owned_by_api_with_options(api_id, headers, runtime)

    def get_policy_owned_by_api_with_options(self, api_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.GetPolicyOwnedByApiResponse().from_map(self.do_roarequest('GetPolicyOwnedByApi', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/api/%s/policy' % api_id, 'json', req, runtime))

    def update_api(self, api_id, request):
        """
        updateApi
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_api_with_options(api_id, request, headers, runtime)

    def update_api_with_options(self, api_id, request, headers, runtime):
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
        return microgw_20200810_models.UpdateApiResponse().from_map(self.do_roarequest('UpdateApi', '2020-08-10', 'HTTPS', 'PUT', 'AK', '/v1/api/%s' % api_id, 'json', req, runtime))

    def create_service(self, gateway_id, request):
        """
        /gateway/{gatewayId}/service
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(gateway_id, request, headers, runtime)

    def create_service_with_options(self, gateway_id, request, headers, runtime):
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
        return microgw_20200810_models.CreateServiceResponse().from_map(self.do_roarequest('CreateService', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/gateway/%s/service' % gateway_id, 'json', req, runtime))

    def save_all_policies(self, api_id, request):
        """
        saveAllPolicies
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_all_policies_with_options(api_id, request, headers, runtime)

    def save_all_policies_with_options(self, api_id, request, headers, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.data)
        )
        return microgw_20200810_models.SaveAllPoliciesResponse().from_map(self.do_roarequest('SaveAllPolicies', '2020-08-10', 'HTTPS', 'POST', 'AK', '/v1/api/%s/policies' % api_id, 'json', req, runtime))

    def update_gateway(self, request):
        """
        updateGateway
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_gateway_with_options(request, headers, runtime)

    def update_gateway_with_options(self, request, headers, runtime):
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
        return microgw_20200810_models.UpdateGatewayResponse().from_map(self.do_roarequest('UpdateGateway', '2020-08-10', 'HTTPS', 'PUT', 'AK', '/v1/gateway', 'json', req, runtime))

    def update_service(self, service_id, request):
        """
        updateService
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_with_options(service_id, request, headers, runtime)

    def update_service_with_options(self, service_id, request, headers, runtime):
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
        return microgw_20200810_models.UpdateServiceResponse().from_map(self.do_roarequest('UpdateService', '2020-08-10', 'HTTPS', 'PUT', 'AK', '/v1/service/%s' % service_id, 'json', req, runtime))

    def find_apis_by_paging(self, gateway_id, request):
        """
        findApisByPaging
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_apis_by_paging_with_options(gateway_id, request, headers, runtime)

    def find_apis_by_paging_with_options(self, gateway_id, request, headers, runtime):
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
        return microgw_20200810_models.FindApisByPagingResponse().from_map(self.do_roarequest('FindApisByPaging', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/gateway/%s/api' % gateway_id, 'json', req, runtime))

    def update_service_ends(self, service_id, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_ends_with_options(service_id, request, headers, runtime)

    def update_service_ends_with_options(self, service_id, request, headers, runtime):
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
        return microgw_20200810_models.UpdateServiceEndsResponse().from_map(self.do_roarequest('UpdateServiceEnds', '2020-08-10', 'HTTPS', 'PUT', 'AK', '/v1/service/%s/serviceends' % service_id, 'json', req, runtime))

    def find_gateways(self, request):
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.find_gateways_with_options(request, headers, runtime)

    def find_gateways_with_options(self, request, headers, runtime):
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
        return microgw_20200810_models.FindGatewaysResponse().from_map(self.do_roarequest('FindGateways', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/gateway', 'json', req, runtime))

    def get_all_registry(self, gateway_id, request):
        """
        getAllRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_all_registry_with_options(gateway_id, request, headers, runtime)

    def get_all_registry_with_options(self, gateway_id, request, headers, runtime):
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
        return microgw_20200810_models.GetAllRegistryResponse().from_map(self.do_roarequest('GetAllRegistry', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/gateway/%s/registry' % gateway_id, 'json', req, runtime))

    def pull_service_info_from_registry(self, registry_id):
        """
        pullServiceInfoFromRegistry
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.pull_service_info_from_registry_with_options(registry_id, headers, runtime)

    def pull_service_info_from_registry_with_options(self, registry_id, headers, runtime):
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return microgw_20200810_models.PullServiceInfoFromRegistryResponse().from_map(self.do_roarequest('PullServiceInfoFromRegistry', '2020-08-10', 'HTTPS', 'GET', 'AK', '/v1/registry/%s/pull' % registry_id, 'json', req, runtime))
