# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_csas20230120 import models as csas_20230120_models
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
        self._endpoint = self.get_endpoint('csas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_application_2connector_with_options(
        self,
        tmp_req: csas_20230120_models.AttachApplication2ConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.AttachApplication2ConnectorResponse:
        """
        @summary 挂载connector的应用
        
        @param tmp_req: AttachApplication2ConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachApplication2ConnectorResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.AttachApplication2ConnectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachApplication2Connector',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.AttachApplication2ConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_application_2connector_with_options_async(
        self,
        tmp_req: csas_20230120_models.AttachApplication2ConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.AttachApplication2ConnectorResponse:
        """
        @summary 挂载connector的应用
        
        @param tmp_req: AttachApplication2ConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachApplication2ConnectorResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.AttachApplication2ConnectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachApplication2Connector',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.AttachApplication2ConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_application_2connector(
        self,
        request: csas_20230120_models.AttachApplication2ConnectorRequest,
    ) -> csas_20230120_models.AttachApplication2ConnectorResponse:
        """
        @summary 挂载connector的应用
        
        @param request: AttachApplication2ConnectorRequest
        @return: AttachApplication2ConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_application_2connector_with_options(request, runtime)

    async def attach_application_2connector_async(
        self,
        request: csas_20230120_models.AttachApplication2ConnectorRequest,
    ) -> csas_20230120_models.AttachApplication2ConnectorResponse:
        """
        @summary 挂载connector的应用
        
        @param request: AttachApplication2ConnectorRequest
        @return: AttachApplication2ConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_application_2connector_with_options_async(request, runtime)

    def create_client_user_with_options(
        self,
        request: csas_20230120_models.CreateClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateClientUserResponse:
        """
        @summary 创建自定义身份源用户
        
        @param request: CreateClientUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClientUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClientUser',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_user_with_options_async(
        self,
        request: csas_20230120_models.CreateClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateClientUserResponse:
        """
        @summary 创建自定义身份源用户
        
        @param request: CreateClientUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClientUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClientUser',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_user(
        self,
        request: csas_20230120_models.CreateClientUserRequest,
    ) -> csas_20230120_models.CreateClientUserResponse:
        """
        @summary 创建自定义身份源用户
        
        @param request: CreateClientUserRequest
        @return: CreateClientUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_client_user_with_options(request, runtime)

    async def create_client_user_async(
        self,
        request: csas_20230120_models.CreateClientUserRequest,
    ) -> csas_20230120_models.CreateClientUserResponse:
        """
        @summary 创建自定义身份源用户
        
        @param request: CreateClientUserRequest
        @return: CreateClientUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_client_user_with_options_async(request, runtime)

    def create_dynamic_route_with_options(
        self,
        request: csas_20230120_models.CreateDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateDynamicRouteResponse:
        """
        @summary 创建动态路由
        
        @param request: CreateDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_hop):
            body['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.CreateDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateDynamicRouteResponse:
        """
        @summary 创建动态路由
        
        @param request: CreateDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_hop):
            body['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dynamic_route(
        self,
        request: csas_20230120_models.CreateDynamicRouteRequest,
    ) -> csas_20230120_models.CreateDynamicRouteResponse:
        """
        @summary 创建动态路由
        
        @param request: CreateDynamicRouteRequest
        @return: CreateDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dynamic_route_with_options(request, runtime)

    async def create_dynamic_route_async(
        self,
        request: csas_20230120_models.CreateDynamicRouteRequest,
    ) -> csas_20230120_models.CreateDynamicRouteResponse:
        """
        @summary 创建动态路由
        
        @param request: CreateDynamicRouteRequest
        @return: CreateDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dynamic_route_with_options_async(request, runtime)

    def create_idp_department_with_options(
        self,
        request: csas_20230120_models.CreateIdpDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateIdpDepartmentResponse:
        """
        @summary 创建自定义身份源部门
        
        @param request: CreateIdpDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIdpDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_name):
            query['DepartmentName'] = request.department_name
        if not UtilClient.is_unset(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIdpDepartment',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateIdpDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_idp_department_with_options_async(
        self,
        request: csas_20230120_models.CreateIdpDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateIdpDepartmentResponse:
        """
        @summary 创建自定义身份源部门
        
        @param request: CreateIdpDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIdpDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_name):
            query['DepartmentName'] = request.department_name
        if not UtilClient.is_unset(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIdpDepartment',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateIdpDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_idp_department(
        self,
        request: csas_20230120_models.CreateIdpDepartmentRequest,
    ) -> csas_20230120_models.CreateIdpDepartmentResponse:
        """
        @summary 创建自定义身份源部门
        
        @param request: CreateIdpDepartmentRequest
        @return: CreateIdpDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_idp_department_with_options(request, runtime)

    async def create_idp_department_async(
        self,
        request: csas_20230120_models.CreateIdpDepartmentRequest,
    ) -> csas_20230120_models.CreateIdpDepartmentResponse:
        """
        @summary 创建自定义身份源部门
        
        @param request: CreateIdpDepartmentRequest
        @return: CreateIdpDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_idp_department_with_options_async(request, runtime)

    def create_private_access_application_with_options(
        self,
        request: csas_20230120_models.CreatePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessApplicationResponse:
        """
        @summary 创建内网访问应用
        
        @param request: CreatePrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.addresses):
            body_flat['Addresses'] = request.addresses
        if not UtilClient.is_unset(request.browser_access_status):
            body['BrowserAccessStatus'] = request.browser_access_status
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.l_7proxy_domain_automatic_prefix):
            body['L7ProxyDomainAutomaticPrefix'] = request.l_7proxy_domain_automatic_prefix
        if not UtilClient.is_unset(request.l_7proxy_domain_custom):
            body['L7ProxyDomainCustom'] = request.l_7proxy_domain_custom
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.port_ranges):
            body_flat['PortRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_access_application_with_options_async(
        self,
        request: csas_20230120_models.CreatePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessApplicationResponse:
        """
        @summary 创建内网访问应用
        
        @param request: CreatePrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.addresses):
            body_flat['Addresses'] = request.addresses
        if not UtilClient.is_unset(request.browser_access_status):
            body['BrowserAccessStatus'] = request.browser_access_status
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.l_7proxy_domain_automatic_prefix):
            body['L7ProxyDomainAutomaticPrefix'] = request.l_7proxy_domain_automatic_prefix
        if not UtilClient.is_unset(request.l_7proxy_domain_custom):
            body['L7ProxyDomainCustom'] = request.l_7proxy_domain_custom
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.port_ranges):
            body_flat['PortRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_access_application(
        self,
        request: csas_20230120_models.CreatePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.CreatePrivateAccessApplicationResponse:
        """
        @summary 创建内网访问应用
        
        @param request: CreatePrivateAccessApplicationRequest
        @return: CreatePrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_private_access_application_with_options(request, runtime)

    async def create_private_access_application_async(
        self,
        request: csas_20230120_models.CreatePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.CreatePrivateAccessApplicationResponse:
        """
        @summary 创建内网访问应用
        
        @param request: CreatePrivateAccessApplicationRequest
        @return: CreatePrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_private_access_application_with_options_async(request, runtime)

    def create_private_access_policy_with_options(
        self,
        request: csas_20230120_models.CreatePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessPolicyResponse:
        """
        @summary 创建内网访问策略
        
        @param request: CreatePrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes):
            body_flat['CustomUserAttributes'] = request.custom_user_attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_attribute_action):
            body['DeviceAttributeAction'] = request.device_attribute_action
        if not UtilClient.is_unset(request.device_attribute_id):
            body['DeviceAttributeId'] = request.device_attribute_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.CreatePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessPolicyResponse:
        """
        @summary 创建内网访问策略
        
        @param request: CreatePrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes):
            body_flat['CustomUserAttributes'] = request.custom_user_attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_attribute_action):
            body['DeviceAttributeAction'] = request.device_attribute_action
        if not UtilClient.is_unset(request.device_attribute_id):
            body['DeviceAttributeId'] = request.device_attribute_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_access_policy(
        self,
        request: csas_20230120_models.CreatePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.CreatePrivateAccessPolicyResponse:
        """
        @summary 创建内网访问策略
        
        @param request: CreatePrivateAccessPolicyRequest
        @return: CreatePrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_private_access_policy_with_options(request, runtime)

    async def create_private_access_policy_async(
        self,
        request: csas_20230120_models.CreatePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.CreatePrivateAccessPolicyResponse:
        """
        @summary 创建内网访问策略
        
        @param request: CreatePrivateAccessPolicyRequest
        @return: CreatePrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_private_access_policy_with_options_async(request, runtime)

    def create_private_access_tag_with_options(
        self,
        request: csas_20230120_models.CreatePrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessTagResponse:
        """
        @summary 创建内网访问标签
        
        @param request: CreatePrivateAccessTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrivateAccessTagResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_private_access_tag_with_options_async(
        self,
        request: csas_20230120_models.CreatePrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreatePrivateAccessTagResponse:
        """
        @summary 创建内网访问标签
        
        @param request: CreatePrivateAccessTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrivateAccessTagResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreatePrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_private_access_tag(
        self,
        request: csas_20230120_models.CreatePrivateAccessTagRequest,
    ) -> csas_20230120_models.CreatePrivateAccessTagResponse:
        """
        @summary 创建内网访问标签
        
        @param request: CreatePrivateAccessTagRequest
        @return: CreatePrivateAccessTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_private_access_tag_with_options(request, runtime)

    async def create_private_access_tag_async(
        self,
        request: csas_20230120_models.CreatePrivateAccessTagRequest,
    ) -> csas_20230120_models.CreatePrivateAccessTagResponse:
        """
        @summary 创建内网访问标签
        
        @param request: CreatePrivateAccessTagRequest
        @return: CreatePrivateAccessTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_private_access_tag_with_options_async(request, runtime)

    def create_registration_policy_with_options(
        self,
        tmp_req: csas_20230120_models.CreateRegistrationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateRegistrationPolicyResponse:
        """
        @summary 创建设备注册策略
        
        @param tmp_req: CreateRegistrationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRegistrationPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreateRegistrationPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.company_limit_count):
            request.company_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.company_limit_count, 'CompanyLimitCount', 'json')
        if not UtilClient.is_unset(tmp_req.personal_limit_count):
            request.personal_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.personal_limit_count, 'PersonalLimitCount', 'json')
        body = {}
        if not UtilClient.is_unset(request.company_limit_count_shrink):
            body['CompanyLimitCount'] = request.company_limit_count_shrink
        if not UtilClient.is_unset(request.company_limit_type):
            body['CompanyLimitType'] = request.company_limit_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.match_mode):
            body['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.personal_limit_count_shrink):
            body['PersonalLimitCount'] = request.personal_limit_count_shrink
        if not UtilClient.is_unset(request.personal_limit_type):
            body['PersonalLimitType'] = request.personal_limit_type
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.whitelist):
            body_flat['Whitelist'] = request.whitelist
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_registration_policy_with_options_async(
        self,
        tmp_req: csas_20230120_models.CreateRegistrationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateRegistrationPolicyResponse:
        """
        @summary 创建设备注册策略
        
        @param tmp_req: CreateRegistrationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRegistrationPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreateRegistrationPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.company_limit_count):
            request.company_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.company_limit_count, 'CompanyLimitCount', 'json')
        if not UtilClient.is_unset(tmp_req.personal_limit_count):
            request.personal_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.personal_limit_count, 'PersonalLimitCount', 'json')
        body = {}
        if not UtilClient.is_unset(request.company_limit_count_shrink):
            body['CompanyLimitCount'] = request.company_limit_count_shrink
        if not UtilClient.is_unset(request.company_limit_type):
            body['CompanyLimitType'] = request.company_limit_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.match_mode):
            body['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.personal_limit_count_shrink):
            body['PersonalLimitCount'] = request.personal_limit_count_shrink
        if not UtilClient.is_unset(request.personal_limit_type):
            body['PersonalLimitType'] = request.personal_limit_type
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.whitelist):
            body_flat['Whitelist'] = request.whitelist
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateRegistrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_registration_policy(
        self,
        request: csas_20230120_models.CreateRegistrationPolicyRequest,
    ) -> csas_20230120_models.CreateRegistrationPolicyResponse:
        """
        @summary 创建设备注册策略
        
        @param request: CreateRegistrationPolicyRequest
        @return: CreateRegistrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_registration_policy_with_options(request, runtime)

    async def create_registration_policy_async(
        self,
        request: csas_20230120_models.CreateRegistrationPolicyRequest,
    ) -> csas_20230120_models.CreateRegistrationPolicyResponse:
        """
        @summary 创建设备注册策略
        
        @param request: CreateRegistrationPolicyRequest
        @return: CreateRegistrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_registration_policy_with_options_async(request, runtime)

    def create_user_group_with_options(
        self,
        request: csas_20230120_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateUserGroupResponse:
        """
        @summary 创建用户组
        
        @param request: CreateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_group_with_options_async(
        self,
        request: csas_20230120_models.CreateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateUserGroupResponse:
        """
        @summary 创建用户组
        
        @param request: CreateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_group(
        self,
        request: csas_20230120_models.CreateUserGroupRequest,
    ) -> csas_20230120_models.CreateUserGroupResponse:
        """
        @summary 创建用户组
        
        @param request: CreateUserGroupRequest
        @return: CreateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    async def create_user_group_async(
        self,
        request: csas_20230120_models.CreateUserGroupRequest,
    ) -> csas_20230120_models.CreateUserGroupResponse:
        """
        @summary 创建用户组
        
        @param request: CreateUserGroupRequest
        @return: CreateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_group_with_options_async(request, runtime)

    def create_wm_base_image_with_options(
        self,
        request: csas_20230120_models.CreateWmBaseImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateWmBaseImageResponse:
        """
        @summary 创建数字水印暗水印透明底图
        
        @param request: CreateWmBaseImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWmBaseImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.opacity):
            body['Opacity'] = request.opacity
        if not UtilClient.is_unset(request.scale):
            body['Scale'] = request.scale
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        if not UtilClient.is_unset(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not UtilClient.is_unset(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not UtilClient.is_unset(request.wm_info_uint):
            body['WmInfoUint'] = request.wm_info_uint
        if not UtilClient.is_unset(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWmBaseImage',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateWmBaseImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wm_base_image_with_options_async(
        self,
        request: csas_20230120_models.CreateWmBaseImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateWmBaseImageResponse:
        """
        @summary 创建数字水印暗水印透明底图
        
        @param request: CreateWmBaseImageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWmBaseImageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.opacity):
            body['Opacity'] = request.opacity
        if not UtilClient.is_unset(request.scale):
            body['Scale'] = request.scale
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        if not UtilClient.is_unset(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not UtilClient.is_unset(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not UtilClient.is_unset(request.wm_info_uint):
            body['WmInfoUint'] = request.wm_info_uint
        if not UtilClient.is_unset(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWmBaseImage',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateWmBaseImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wm_base_image(
        self,
        request: csas_20230120_models.CreateWmBaseImageRequest,
    ) -> csas_20230120_models.CreateWmBaseImageResponse:
        """
        @summary 创建数字水印暗水印透明底图
        
        @param request: CreateWmBaseImageRequest
        @return: CreateWmBaseImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_wm_base_image_with_options(request, runtime)

    async def create_wm_base_image_async(
        self,
        request: csas_20230120_models.CreateWmBaseImageRequest,
    ) -> csas_20230120_models.CreateWmBaseImageResponse:
        """
        @summary 创建数字水印暗水印透明底图
        
        @param request: CreateWmBaseImageRequest
        @return: CreateWmBaseImageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_wm_base_image_with_options_async(request, runtime)

    def create_wm_embed_task_with_options(
        self,
        tmp_req: csas_20230120_models.CreateWmEmbedTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateWmEmbedTaskResponse:
        """
        @summary 创建嵌入水印任务
        
        @param tmp_req: CreateWmEmbedTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWmEmbedTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreateWmEmbedTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.csv_control):
            request.csv_control_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.csv_control, 'CsvControl', 'json')
        if not UtilClient.is_unset(tmp_req.document_control):
            request.document_control_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_control, 'DocumentControl', 'json')
        query = {}
        if not UtilClient.is_unset(request.csv_control_shrink):
            query['CsvControl'] = request.csv_control_shrink
        body = {}
        if not UtilClient.is_unset(request.document_control_shrink):
            body['DocumentControl'] = request.document_control_shrink
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.filename):
            body['Filename'] = request.filename
        if not UtilClient.is_unset(request.image_embed_jpeg_quality):
            body['ImageEmbedJpegQuality'] = request.image_embed_jpeg_quality
        if not UtilClient.is_unset(request.image_embed_level):
            body['ImageEmbedLevel'] = request.image_embed_level
        if not UtilClient.is_unset(request.video_bitrate):
            body['VideoBitrate'] = request.video_bitrate
        if not UtilClient.is_unset(request.video_is_long):
            body['VideoIsLong'] = request.video_is_long
        if not UtilClient.is_unset(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not UtilClient.is_unset(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not UtilClient.is_unset(request.wm_info_uint):
            body['WmInfoUint'] = request.wm_info_uint
        if not UtilClient.is_unset(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWmEmbedTask',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateWmEmbedTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wm_embed_task_with_options_async(
        self,
        tmp_req: csas_20230120_models.CreateWmEmbedTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateWmEmbedTaskResponse:
        """
        @summary 创建嵌入水印任务
        
        @param tmp_req: CreateWmEmbedTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWmEmbedTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreateWmEmbedTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.csv_control):
            request.csv_control_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.csv_control, 'CsvControl', 'json')
        if not UtilClient.is_unset(tmp_req.document_control):
            request.document_control_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.document_control, 'DocumentControl', 'json')
        query = {}
        if not UtilClient.is_unset(request.csv_control_shrink):
            query['CsvControl'] = request.csv_control_shrink
        body = {}
        if not UtilClient.is_unset(request.document_control_shrink):
            body['DocumentControl'] = request.document_control_shrink
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.filename):
            body['Filename'] = request.filename
        if not UtilClient.is_unset(request.image_embed_jpeg_quality):
            body['ImageEmbedJpegQuality'] = request.image_embed_jpeg_quality
        if not UtilClient.is_unset(request.image_embed_level):
            body['ImageEmbedLevel'] = request.image_embed_level
        if not UtilClient.is_unset(request.video_bitrate):
            body['VideoBitrate'] = request.video_bitrate
        if not UtilClient.is_unset(request.video_is_long):
            body['VideoIsLong'] = request.video_is_long
        if not UtilClient.is_unset(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not UtilClient.is_unset(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not UtilClient.is_unset(request.wm_info_uint):
            body['WmInfoUint'] = request.wm_info_uint
        if not UtilClient.is_unset(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWmEmbedTask',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateWmEmbedTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wm_embed_task(
        self,
        request: csas_20230120_models.CreateWmEmbedTaskRequest,
    ) -> csas_20230120_models.CreateWmEmbedTaskResponse:
        """
        @summary 创建嵌入水印任务
        
        @param request: CreateWmEmbedTaskRequest
        @return: CreateWmEmbedTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_wm_embed_task_with_options(request, runtime)

    async def create_wm_embed_task_async(
        self,
        request: csas_20230120_models.CreateWmEmbedTaskRequest,
    ) -> csas_20230120_models.CreateWmEmbedTaskResponse:
        """
        @summary 创建嵌入水印任务
        
        @param request: CreateWmEmbedTaskRequest
        @return: CreateWmEmbedTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_wm_embed_task_with_options_async(request, runtime)

    def create_wm_extract_task_with_options(
        self,
        tmp_req: csas_20230120_models.CreateWmExtractTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateWmExtractTaskResponse:
        """
        @summary 创建文件水印提取任务
        
        @param tmp_req: CreateWmExtractTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWmExtractTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreateWmExtractTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.csv_control):
            request.csv_control_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.csv_control, 'CsvControl', 'json')
        query = {}
        if not UtilClient.is_unset(request.csv_control_shrink):
            query['CsvControl'] = request.csv_control_shrink
        body = {}
        if not UtilClient.is_unset(request.document_is_capture):
            body['DocumentIsCapture'] = request.document_is_capture
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.filename):
            body['Filename'] = request.filename
        if not UtilClient.is_unset(request.video_is_long):
            body['VideoIsLong'] = request.video_is_long
        if not UtilClient.is_unset(request.video_speed):
            body['VideoSpeed'] = request.video_speed
        if not UtilClient.is_unset(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not UtilClient.is_unset(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWmExtractTask',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateWmExtractTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wm_extract_task_with_options_async(
        self,
        tmp_req: csas_20230120_models.CreateWmExtractTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateWmExtractTaskResponse:
        """
        @summary 创建文件水印提取任务
        
        @param tmp_req: CreateWmExtractTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWmExtractTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.CreateWmExtractTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.csv_control):
            request.csv_control_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.csv_control, 'CsvControl', 'json')
        query = {}
        if not UtilClient.is_unset(request.csv_control_shrink):
            query['CsvControl'] = request.csv_control_shrink
        body = {}
        if not UtilClient.is_unset(request.document_is_capture):
            body['DocumentIsCapture'] = request.document_is_capture
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.filename):
            body['Filename'] = request.filename
        if not UtilClient.is_unset(request.video_is_long):
            body['VideoIsLong'] = request.video_is_long
        if not UtilClient.is_unset(request.video_speed):
            body['VideoSpeed'] = request.video_speed
        if not UtilClient.is_unset(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not UtilClient.is_unset(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWmExtractTask',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateWmExtractTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wm_extract_task(
        self,
        request: csas_20230120_models.CreateWmExtractTaskRequest,
    ) -> csas_20230120_models.CreateWmExtractTaskResponse:
        """
        @summary 创建文件水印提取任务
        
        @param request: CreateWmExtractTaskRequest
        @return: CreateWmExtractTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_wm_extract_task_with_options(request, runtime)

    async def create_wm_extract_task_async(
        self,
        request: csas_20230120_models.CreateWmExtractTaskRequest,
    ) -> csas_20230120_models.CreateWmExtractTaskResponse:
        """
        @summary 创建文件水印提取任务
        
        @param request: CreateWmExtractTaskRequest
        @return: CreateWmExtractTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_wm_extract_task_with_options_async(request, runtime)

    def create_wm_info_mapping_with_options(
        self,
        request: csas_20230120_models.CreateWmInfoMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateWmInfoMappingResponse:
        """
        @summary 创建一条字符串水印信息到数字水印信息的映射记录
        
        @param request: CreateWmInfoMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWmInfoMappingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not UtilClient.is_unset(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not UtilClient.is_unset(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWmInfoMapping',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateWmInfoMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wm_info_mapping_with_options_async(
        self,
        request: csas_20230120_models.CreateWmInfoMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.CreateWmInfoMappingResponse:
        """
        @summary 创建一条字符串水印信息到数字水印信息的映射记录
        
        @param request: CreateWmInfoMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWmInfoMappingResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.wm_info_bytes_b64):
            body['WmInfoBytesB64'] = request.wm_info_bytes_b64
        if not UtilClient.is_unset(request.wm_info_size):
            body['WmInfoSize'] = request.wm_info_size
        if not UtilClient.is_unset(request.wm_type):
            body['WmType'] = request.wm_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWmInfoMapping',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.CreateWmInfoMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wm_info_mapping(
        self,
        request: csas_20230120_models.CreateWmInfoMappingRequest,
    ) -> csas_20230120_models.CreateWmInfoMappingResponse:
        """
        @summary 创建一条字符串水印信息到数字水印信息的映射记录
        
        @param request: CreateWmInfoMappingRequest
        @return: CreateWmInfoMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_wm_info_mapping_with_options(request, runtime)

    async def create_wm_info_mapping_async(
        self,
        request: csas_20230120_models.CreateWmInfoMappingRequest,
    ) -> csas_20230120_models.CreateWmInfoMappingResponse:
        """
        @summary 创建一条字符串水印信息到数字水印信息的映射记录
        
        @param request: CreateWmInfoMappingRequest
        @return: CreateWmInfoMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_wm_info_mapping_with_options_async(request, runtime)

    def delete_client_user_with_options(
        self,
        request: csas_20230120_models.DeleteClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteClientUserResponse:
        """
        @summary 删除自定义身份源指定用户
        
        @param request: DeleteClientUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClientUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClientUser',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_user_with_options_async(
        self,
        request: csas_20230120_models.DeleteClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteClientUserResponse:
        """
        @summary 删除自定义身份源指定用户
        
        @param request: DeleteClientUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClientUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClientUser',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client_user(
        self,
        request: csas_20230120_models.DeleteClientUserRequest,
    ) -> csas_20230120_models.DeleteClientUserResponse:
        """
        @summary 删除自定义身份源指定用户
        
        @param request: DeleteClientUserRequest
        @return: DeleteClientUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_client_user_with_options(request, runtime)

    async def delete_client_user_async(
        self,
        request: csas_20230120_models.DeleteClientUserRequest,
    ) -> csas_20230120_models.DeleteClientUserResponse:
        """
        @summary 删除自定义身份源指定用户
        
        @param request: DeleteClientUserRequest
        @return: DeleteClientUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_client_user_with_options_async(request, runtime)

    def delete_dynamic_route_with_options(
        self,
        request: csas_20230120_models.DeleteDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteDynamicRouteResponse:
        """
        @summary 删除动态路由
        
        @param request: DeleteDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_route_id):
            query['DynamicRouteId'] = request.dynamic_route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.DeleteDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteDynamicRouteResponse:
        """
        @summary 删除动态路由
        
        @param request: DeleteDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_route_id):
            query['DynamicRouteId'] = request.dynamic_route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dynamic_route(
        self,
        request: csas_20230120_models.DeleteDynamicRouteRequest,
    ) -> csas_20230120_models.DeleteDynamicRouteResponse:
        """
        @summary 删除动态路由
        
        @param request: DeleteDynamicRouteRequest
        @return: DeleteDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dynamic_route_with_options(request, runtime)

    async def delete_dynamic_route_async(
        self,
        request: csas_20230120_models.DeleteDynamicRouteRequest,
    ) -> csas_20230120_models.DeleteDynamicRouteResponse:
        """
        @summary 删除动态路由
        
        @param request: DeleteDynamicRouteRequest
        @return: DeleteDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dynamic_route_with_options_async(request, runtime)

    def delete_idp_department_with_options(
        self,
        request: csas_20230120_models.DeleteIdpDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteIdpDepartmentResponse:
        """
        @summary 删除指定自定义身份源部门
        
        @param request: DeleteIdpDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIdpDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIdpDepartment',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteIdpDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_idp_department_with_options_async(
        self,
        request: csas_20230120_models.DeleteIdpDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteIdpDepartmentResponse:
        """
        @summary 删除指定自定义身份源部门
        
        @param request: DeleteIdpDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIdpDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIdpDepartment',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteIdpDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_idp_department(
        self,
        request: csas_20230120_models.DeleteIdpDepartmentRequest,
    ) -> csas_20230120_models.DeleteIdpDepartmentResponse:
        """
        @summary 删除指定自定义身份源部门
        
        @param request: DeleteIdpDepartmentRequest
        @return: DeleteIdpDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_idp_department_with_options(request, runtime)

    async def delete_idp_department_async(
        self,
        request: csas_20230120_models.DeleteIdpDepartmentRequest,
    ) -> csas_20230120_models.DeleteIdpDepartmentResponse:
        """
        @summary 删除指定自定义身份源部门
        
        @param request: DeleteIdpDepartmentRequest
        @return: DeleteIdpDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_idp_department_with_options_async(request, runtime)

    def delete_private_access_application_with_options(
        self,
        request: csas_20230120_models.DeletePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessApplicationResponse:
        """
        @summary 删除内网访问应用
        
        @param request: DeletePrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_access_application_with_options_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessApplicationResponse:
        """
        @summary 删除内网访问应用
        
        @param request: DeletePrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_access_application(
        self,
        request: csas_20230120_models.DeletePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.DeletePrivateAccessApplicationResponse:
        """
        @summary 删除内网访问应用
        
        @param request: DeletePrivateAccessApplicationRequest
        @return: DeletePrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_private_access_application_with_options(request, runtime)

    async def delete_private_access_application_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.DeletePrivateAccessApplicationResponse:
        """
        @summary 删除内网访问应用
        
        @param request: DeletePrivateAccessApplicationRequest
        @return: DeletePrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_private_access_application_with_options_async(request, runtime)

    def delete_private_access_policy_with_options(
        self,
        request: csas_20230120_models.DeletePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessPolicyResponse:
        """
        @summary 删除内网访问策略
        
        @param request: DeletePrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessPolicyResponse:
        """
        @summary 删除内网访问策略
        
        @param request: DeletePrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_access_policy(
        self,
        request: csas_20230120_models.DeletePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.DeletePrivateAccessPolicyResponse:
        """
        @summary 删除内网访问策略
        
        @param request: DeletePrivateAccessPolicyRequest
        @return: DeletePrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_private_access_policy_with_options(request, runtime)

    async def delete_private_access_policy_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.DeletePrivateAccessPolicyResponse:
        """
        @summary 删除内网访问策略
        
        @param request: DeletePrivateAccessPolicyRequest
        @return: DeletePrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_private_access_policy_with_options_async(request, runtime)

    def delete_private_access_tag_with_options(
        self,
        request: csas_20230120_models.DeletePrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessTagResponse:
        """
        @summary 删除内网访问标签
        
        @param request: DeletePrivateAccessTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrivateAccessTagResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tag_id):
            body['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_private_access_tag_with_options_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeletePrivateAccessTagResponse:
        """
        @summary 删除内网访问标签
        
        @param request: DeletePrivateAccessTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrivateAccessTagResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tag_id):
            body['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeletePrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_private_access_tag(
        self,
        request: csas_20230120_models.DeletePrivateAccessTagRequest,
    ) -> csas_20230120_models.DeletePrivateAccessTagResponse:
        """
        @summary 删除内网访问标签
        
        @param request: DeletePrivateAccessTagRequest
        @return: DeletePrivateAccessTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_private_access_tag_with_options(request, runtime)

    async def delete_private_access_tag_async(
        self,
        request: csas_20230120_models.DeletePrivateAccessTagRequest,
    ) -> csas_20230120_models.DeletePrivateAccessTagResponse:
        """
        @summary 删除内网访问标签
        
        @param request: DeletePrivateAccessTagRequest
        @return: DeletePrivateAccessTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_private_access_tag_with_options_async(request, runtime)

    def delete_registration_policies_with_options(
        self,
        request: csas_20230120_models.DeleteRegistrationPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteRegistrationPoliciesResponse:
        """
        @summary 删除设备注册策略
        
        @param request: DeleteRegistrationPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRegistrationPoliciesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.policy_ids):
            body_flat['PolicyIds'] = request.policy_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRegistrationPolicies',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteRegistrationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registration_policies_with_options_async(
        self,
        request: csas_20230120_models.DeleteRegistrationPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteRegistrationPoliciesResponse:
        """
        @summary 删除设备注册策略
        
        @param request: DeleteRegistrationPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRegistrationPoliciesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.policy_ids):
            body_flat['PolicyIds'] = request.policy_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRegistrationPolicies',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteRegistrationPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registration_policies(
        self,
        request: csas_20230120_models.DeleteRegistrationPoliciesRequest,
    ) -> csas_20230120_models.DeleteRegistrationPoliciesResponse:
        """
        @summary 删除设备注册策略
        
        @param request: DeleteRegistrationPoliciesRequest
        @return: DeleteRegistrationPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_registration_policies_with_options(request, runtime)

    async def delete_registration_policies_async(
        self,
        request: csas_20230120_models.DeleteRegistrationPoliciesRequest,
    ) -> csas_20230120_models.DeleteRegistrationPoliciesResponse:
        """
        @summary 删除设备注册策略
        
        @param request: DeleteRegistrationPoliciesRequest
        @return: DeleteRegistrationPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_registration_policies_with_options_async(request, runtime)

    def delete_user_devices_with_options(
        self,
        request: csas_20230120_models.DeleteUserDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteUserDevicesResponse:
        """
        @summary 批量删除用户非在线设备
        
        @param request: DeleteUserDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserDevices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteUserDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_devices_with_options_async(
        self,
        request: csas_20230120_models.DeleteUserDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteUserDevicesResponse:
        """
        @summary 批量删除用户非在线设备
        
        @param request: DeleteUserDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserDevices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteUserDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_devices(
        self,
        request: csas_20230120_models.DeleteUserDevicesRequest,
    ) -> csas_20230120_models.DeleteUserDevicesResponse:
        """
        @summary 批量删除用户非在线设备
        
        @param request: DeleteUserDevicesRequest
        @return: DeleteUserDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_devices_with_options(request, runtime)

    async def delete_user_devices_async(
        self,
        request: csas_20230120_models.DeleteUserDevicesRequest,
    ) -> csas_20230120_models.DeleteUserDevicesResponse:
        """
        @summary 批量删除用户非在线设备
        
        @param request: DeleteUserDevicesRequest
        @return: DeleteUserDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_devices_with_options_async(request, runtime)

    def delete_user_group_with_options(
        self,
        request: csas_20230120_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteUserGroupResponse:
        """
        @summary 删除用户组
        
        @param request: DeleteUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_group_with_options_async(
        self,
        request: csas_20230120_models.DeleteUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DeleteUserGroupResponse:
        """
        @summary 删除用户组
        
        @param request: DeleteUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DeleteUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_group(
        self,
        request: csas_20230120_models.DeleteUserGroupRequest,
    ) -> csas_20230120_models.DeleteUserGroupResponse:
        """
        @summary 删除用户组
        
        @param request: DeleteUserGroupRequest
        @return: DeleteUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    async def delete_user_group_async(
        self,
        request: csas_20230120_models.DeleteUserGroupRequest,
    ) -> csas_20230120_models.DeleteUserGroupResponse:
        """
        @summary 删除用户组
        
        @param request: DeleteUserGroupRequest
        @return: DeleteUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_group_with_options_async(request, runtime)

    def detach_application_2connector_with_options(
        self,
        tmp_req: csas_20230120_models.DetachApplication2ConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DetachApplication2ConnectorResponse:
        """
        @summary 卸载connector的应用
        
        @param tmp_req: DetachApplication2ConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachApplication2ConnectorResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.DetachApplication2ConnectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachApplication2Connector',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DetachApplication2ConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_application_2connector_with_options_async(
        self,
        tmp_req: csas_20230120_models.DetachApplication2ConnectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.DetachApplication2ConnectorResponse:
        """
        @summary 卸载connector的应用
        
        @param tmp_req: DetachApplication2ConnectorRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachApplication2ConnectorResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.DetachApplication2ConnectorShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.application_ids):
            request.application_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.application_ids, 'ApplicationIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.application_ids_shrink):
            body['ApplicationIds'] = request.application_ids_shrink
        if not UtilClient.is_unset(request.connector_id):
            body['ConnectorId'] = request.connector_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachApplication2Connector',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.DetachApplication2ConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_application_2connector(
        self,
        request: csas_20230120_models.DetachApplication2ConnectorRequest,
    ) -> csas_20230120_models.DetachApplication2ConnectorResponse:
        """
        @summary 卸载connector的应用
        
        @param request: DetachApplication2ConnectorRequest
        @return: DetachApplication2ConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_application_2connector_with_options(request, runtime)

    async def detach_application_2connector_async(
        self,
        request: csas_20230120_models.DetachApplication2ConnectorRequest,
    ) -> csas_20230120_models.DetachApplication2ConnectorResponse:
        """
        @summary 卸载connector的应用
        
        @param request: DetachApplication2ConnectorRequest
        @return: DetachApplication2ConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_application_2connector_with_options_async(request, runtime)

    def export_user_devices_with_options(
        self,
        request: csas_20230120_models.ExportUserDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ExportUserDevicesResponse:
        """
        @summary 批量查询用户设备列表
        
        @param request: ExportUserDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportUserDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.app_statuses):
            body_flat['AppStatuses'] = request.app_statuses
        if not UtilClient.is_unset(request.department):
            body['Department'] = request.department
        if not UtilClient.is_unset(request.device_belong):
            body['DeviceBelong'] = request.device_belong
        if not UtilClient.is_unset(request.device_statuses):
            body_flat['DeviceStatuses'] = request.device_statuses
        if not UtilClient.is_unset(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        if not UtilClient.is_unset(request.device_types):
            body_flat['DeviceTypes'] = request.device_types
        if not UtilClient.is_unset(request.dlp_statuses):
            body_flat['DlpStatuses'] = request.dlp_statuses
        if not UtilClient.is_unset(request.hostname):
            body['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.ia_statuses):
            body_flat['IaStatuses'] = request.ia_statuses
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.nac_statuses):
            body_flat['NacStatuses'] = request.nac_statuses
        if not UtilClient.is_unset(request.pa_statuses):
            body_flat['PaStatuses'] = request.pa_statuses
        if not UtilClient.is_unset(request.sase_user_id):
            body['SaseUserId'] = request.sase_user_id
        if not UtilClient.is_unset(request.sharing_status):
            body['SharingStatus'] = request.sharing_status
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportUserDevices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ExportUserDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_user_devices_with_options_async(
        self,
        request: csas_20230120_models.ExportUserDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ExportUserDevicesResponse:
        """
        @summary 批量查询用户设备列表
        
        @param request: ExportUserDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportUserDevicesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.app_statuses):
            body_flat['AppStatuses'] = request.app_statuses
        if not UtilClient.is_unset(request.department):
            body['Department'] = request.department
        if not UtilClient.is_unset(request.device_belong):
            body['DeviceBelong'] = request.device_belong
        if not UtilClient.is_unset(request.device_statuses):
            body_flat['DeviceStatuses'] = request.device_statuses
        if not UtilClient.is_unset(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        if not UtilClient.is_unset(request.device_types):
            body_flat['DeviceTypes'] = request.device_types
        if not UtilClient.is_unset(request.dlp_statuses):
            body_flat['DlpStatuses'] = request.dlp_statuses
        if not UtilClient.is_unset(request.hostname):
            body['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.ia_statuses):
            body_flat['IaStatuses'] = request.ia_statuses
        if not UtilClient.is_unset(request.mac):
            body['Mac'] = request.mac
        if not UtilClient.is_unset(request.nac_statuses):
            body_flat['NacStatuses'] = request.nac_statuses
        if not UtilClient.is_unset(request.pa_statuses):
            body_flat['PaStatuses'] = request.pa_statuses
        if not UtilClient.is_unset(request.sase_user_id):
            body['SaseUserId'] = request.sase_user_id
        if not UtilClient.is_unset(request.sharing_status):
            body['SharingStatus'] = request.sharing_status
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportUserDevices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ExportUserDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_user_devices(
        self,
        request: csas_20230120_models.ExportUserDevicesRequest,
    ) -> csas_20230120_models.ExportUserDevicesResponse:
        """
        @summary 批量查询用户设备列表
        
        @param request: ExportUserDevicesRequest
        @return: ExportUserDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_user_devices_with_options(request, runtime)

    async def export_user_devices_async(
        self,
        request: csas_20230120_models.ExportUserDevicesRequest,
    ) -> csas_20230120_models.ExportUserDevicesResponse:
        """
        @summary 批量查询用户设备列表
        
        @param request: ExportUserDevicesRequest
        @return: ExportUserDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_user_devices_with_options_async(request, runtime)

    def get_active_idp_config_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetActiveIdpConfigResponse:
        """
        @summary 查询已启用的身份源配置
        
        @param request: GetActiveIdpConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetActiveIdpConfigResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetActiveIdpConfig',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetActiveIdpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_active_idp_config_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetActiveIdpConfigResponse:
        """
        @summary 查询已启用的身份源配置
        
        @param request: GetActiveIdpConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetActiveIdpConfigResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetActiveIdpConfig',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetActiveIdpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_active_idp_config(self) -> csas_20230120_models.GetActiveIdpConfigResponse:
        """
        @summary 查询已启用的身份源配置
        
        @return: GetActiveIdpConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_active_idp_config_with_options(runtime)

    async def get_active_idp_config_async(self) -> csas_20230120_models.GetActiveIdpConfigResponse:
        """
        @summary 查询已启用的身份源配置
        
        @return: GetActiveIdpConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_active_idp_config_with_options_async(runtime)

    def get_client_user_with_options(
        self,
        request: csas_20230120_models.GetClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetClientUserResponse:
        """
        @summary 查询自定义身份源指定用户
        
        @param request: GetClientUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClientUserResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClientUser',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_client_user_with_options_async(
        self,
        request: csas_20230120_models.GetClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetClientUserResponse:
        """
        @summary 查询自定义身份源指定用户
        
        @param request: GetClientUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClientUserResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClientUser',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_client_user(
        self,
        request: csas_20230120_models.GetClientUserRequest,
    ) -> csas_20230120_models.GetClientUserResponse:
        """
        @summary 查询自定义身份源指定用户
        
        @param request: GetClientUserRequest
        @return: GetClientUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_client_user_with_options(request, runtime)

    async def get_client_user_async(
        self,
        request: csas_20230120_models.GetClientUserRequest,
    ) -> csas_20230120_models.GetClientUserResponse:
        """
        @summary 查询自定义身份源指定用户
        
        @param request: GetClientUserRequest
        @return: GetClientUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_client_user_with_options_async(request, runtime)

    def get_dynamic_route_with_options(
        self,
        request: csas_20230120_models.GetDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetDynamicRouteResponse:
        """
        @summary 查询动态路由详情
        
        @param request: GetDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.GetDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetDynamicRouteResponse:
        """
        @summary 查询动态路由详情
        
        @param request: GetDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dynamic_route(
        self,
        request: csas_20230120_models.GetDynamicRouteRequest,
    ) -> csas_20230120_models.GetDynamicRouteResponse:
        """
        @summary 查询动态路由详情
        
        @param request: GetDynamicRouteRequest
        @return: GetDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dynamic_route_with_options(request, runtime)

    async def get_dynamic_route_async(
        self,
        request: csas_20230120_models.GetDynamicRouteRequest,
    ) -> csas_20230120_models.GetDynamicRouteResponse:
        """
        @summary 查询动态路由详情
        
        @param request: GetDynamicRouteRequest
        @return: GetDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dynamic_route_with_options_async(request, runtime)

    def get_idp_config_with_options(
        self,
        request: csas_20230120_models.GetIdpConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetIdpConfigResponse:
        """
        @summary 查询身份源配置详情
        
        @param request: GetIdpConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIdpConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIdpConfig',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetIdpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_idp_config_with_options_async(
        self,
        request: csas_20230120_models.GetIdpConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetIdpConfigResponse:
        """
        @summary 查询身份源配置详情
        
        @param request: GetIdpConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIdpConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIdpConfig',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetIdpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_idp_config(
        self,
        request: csas_20230120_models.GetIdpConfigRequest,
    ) -> csas_20230120_models.GetIdpConfigResponse:
        """
        @summary 查询身份源配置详情
        
        @param request: GetIdpConfigRequest
        @return: GetIdpConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_idp_config_with_options(request, runtime)

    async def get_idp_config_async(
        self,
        request: csas_20230120_models.GetIdpConfigRequest,
    ) -> csas_20230120_models.GetIdpConfigResponse:
        """
        @summary 查询身份源配置详情
        
        @param request: GetIdpConfigRequest
        @return: GetIdpConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_idp_config_with_options_async(request, runtime)

    def get_private_access_application_with_options(
        self,
        request: csas_20230120_models.GetPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetPrivateAccessApplicationResponse:
        """
        @summary 查询内网访问应用详情
        
        @param request: GetPrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_private_access_application_with_options_async(
        self,
        request: csas_20230120_models.GetPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetPrivateAccessApplicationResponse:
        """
        @summary 查询内网访问应用详情
        
        @param request: GetPrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetPrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_private_access_application(
        self,
        request: csas_20230120_models.GetPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.GetPrivateAccessApplicationResponse:
        """
        @summary 查询内网访问应用详情
        
        @param request: GetPrivateAccessApplicationRequest
        @return: GetPrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_private_access_application_with_options(request, runtime)

    async def get_private_access_application_async(
        self,
        request: csas_20230120_models.GetPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.GetPrivateAccessApplicationResponse:
        """
        @summary 查询内网访问应用详情
        
        @param request: GetPrivateAccessApplicationRequest
        @return: GetPrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_private_access_application_with_options_async(request, runtime)

    def get_private_access_policy_with_options(
        self,
        request: csas_20230120_models.GetPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetPrivateAccessPolicyResponse:
        """
        @summary 查询内网访问策略详情
        
        @param request: GetPrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.GetPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetPrivateAccessPolicyResponse:
        """
        @summary 查询内网访问策略详情
        
        @param request: GetPrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_private_access_policy(
        self,
        request: csas_20230120_models.GetPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.GetPrivateAccessPolicyResponse:
        """
        @summary 查询内网访问策略详情
        
        @param request: GetPrivateAccessPolicyRequest
        @return: GetPrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_private_access_policy_with_options(request, runtime)

    async def get_private_access_policy_async(
        self,
        request: csas_20230120_models.GetPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.GetPrivateAccessPolicyResponse:
        """
        @summary 查询内网访问策略详情
        
        @param request: GetPrivateAccessPolicyRequest
        @return: GetPrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_private_access_policy_with_options_async(request, runtime)

    def get_registration_policy_with_options(
        self,
        request: csas_20230120_models.GetRegistrationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetRegistrationPolicyResponse:
        """
        @summary 查询设备注册策略详情
        
        @param request: GetRegistrationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegistrationPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registration_policy_with_options_async(
        self,
        request: csas_20230120_models.GetRegistrationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetRegistrationPolicyResponse:
        """
        @summary 查询设备注册策略详情
        
        @param request: GetRegistrationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegistrationPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetRegistrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registration_policy(
        self,
        request: csas_20230120_models.GetRegistrationPolicyRequest,
    ) -> csas_20230120_models.GetRegistrationPolicyResponse:
        """
        @summary 查询设备注册策略详情
        
        @param request: GetRegistrationPolicyRequest
        @return: GetRegistrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_registration_policy_with_options(request, runtime)

    async def get_registration_policy_async(
        self,
        request: csas_20230120_models.GetRegistrationPolicyRequest,
    ) -> csas_20230120_models.GetRegistrationPolicyResponse:
        """
        @summary 查询设备注册策略详情
        
        @param request: GetRegistrationPolicyRequest
        @return: GetRegistrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_registration_policy_with_options_async(request, runtime)

    def get_user_device_with_options(
        self,
        request: csas_20230120_models.GetUserDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetUserDeviceResponse:
        """
        @summary 查询用户设备详情
        
        @param request: GetUserDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserDeviceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserDevice',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetUserDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_device_with_options_async(
        self,
        request: csas_20230120_models.GetUserDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetUserDeviceResponse:
        """
        @summary 查询用户设备详情
        
        @param request: GetUserDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserDeviceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserDevice',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetUserDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_device(
        self,
        request: csas_20230120_models.GetUserDeviceRequest,
    ) -> csas_20230120_models.GetUserDeviceResponse:
        """
        @summary 查询用户设备详情
        
        @param request: GetUserDeviceRequest
        @return: GetUserDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_device_with_options(request, runtime)

    async def get_user_device_async(
        self,
        request: csas_20230120_models.GetUserDeviceRequest,
    ) -> csas_20230120_models.GetUserDeviceResponse:
        """
        @summary 查询用户设备详情
        
        @param request: GetUserDeviceRequest
        @return: GetUserDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_device_with_options_async(request, runtime)

    def get_user_group_with_options(
        self,
        request: csas_20230120_models.GetUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetUserGroupResponse:
        """
        @summary 查询用户组详情
        
        @param request: GetUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_group_with_options_async(
        self,
        request: csas_20230120_models.GetUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetUserGroupResponse:
        """
        @summary 查询用户组详情
        
        @param request: GetUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_group(
        self,
        request: csas_20230120_models.GetUserGroupRequest,
    ) -> csas_20230120_models.GetUserGroupResponse:
        """
        @summary 查询用户组详情
        
        @param request: GetUserGroupRequest
        @return: GetUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_group_with_options(request, runtime)

    async def get_user_group_async(
        self,
        request: csas_20230120_models.GetUserGroupRequest,
    ) -> csas_20230120_models.GetUserGroupResponse:
        """
        @summary 查询用户组详情
        
        @param request: GetUserGroupRequest
        @return: GetUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_group_with_options_async(request, runtime)

    def get_wm_embed_task_with_options(
        self,
        request: csas_20230120_models.GetWmEmbedTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetWmEmbedTaskResponse:
        """
        @summary 查询嵌入水印任务
        
        @param request: GetWmEmbedTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWmEmbedTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWmEmbedTask',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetWmEmbedTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_wm_embed_task_with_options_async(
        self,
        request: csas_20230120_models.GetWmEmbedTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetWmEmbedTaskResponse:
        """
        @summary 查询嵌入水印任务
        
        @param request: GetWmEmbedTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWmEmbedTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWmEmbedTask',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetWmEmbedTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_wm_embed_task(
        self,
        request: csas_20230120_models.GetWmEmbedTaskRequest,
    ) -> csas_20230120_models.GetWmEmbedTaskResponse:
        """
        @summary 查询嵌入水印任务
        
        @param request: GetWmEmbedTaskRequest
        @return: GetWmEmbedTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_wm_embed_task_with_options(request, runtime)

    async def get_wm_embed_task_async(
        self,
        request: csas_20230120_models.GetWmEmbedTaskRequest,
    ) -> csas_20230120_models.GetWmEmbedTaskResponse:
        """
        @summary 查询嵌入水印任务
        
        @param request: GetWmEmbedTaskRequest
        @return: GetWmEmbedTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_wm_embed_task_with_options_async(request, runtime)

    def get_wm_extract_task_with_options(
        self,
        request: csas_20230120_models.GetWmExtractTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetWmExtractTaskResponse:
        """
        @summary 查询文件水印提取任务详情
        
        @param request: GetWmExtractTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWmExtractTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWmExtractTask',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetWmExtractTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_wm_extract_task_with_options_async(
        self,
        request: csas_20230120_models.GetWmExtractTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.GetWmExtractTaskResponse:
        """
        @summary 查询文件水印提取任务详情
        
        @param request: GetWmExtractTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWmExtractTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWmExtractTask',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.GetWmExtractTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_wm_extract_task(
        self,
        request: csas_20230120_models.GetWmExtractTaskRequest,
    ) -> csas_20230120_models.GetWmExtractTaskResponse:
        """
        @summary 查询文件水印提取任务详情
        
        @param request: GetWmExtractTaskRequest
        @return: GetWmExtractTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_wm_extract_task_with_options(request, runtime)

    async def get_wm_extract_task_async(
        self,
        request: csas_20230120_models.GetWmExtractTaskRequest,
    ) -> csas_20230120_models.GetWmExtractTaskResponse:
        """
        @summary 查询文件水印提取任务详情
        
        @param request: GetWmExtractTaskRequest
        @return: GetWmExtractTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_wm_extract_task_with_options_async(request, runtime)

    def list_applications_for_private_access_policy_with_options(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的应用
        
        @param request: ListApplicationsForPrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForPrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的应用
        
        @param request: ListApplicationsForPrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForPrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_private_access_policy(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的应用
        
        @param request: ListApplicationsForPrivateAccessPolicyRequest
        @return: ListApplicationsForPrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_private_access_policy_with_options(request, runtime)

    async def list_applications_for_private_access_policy_async(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的应用
        
        @param request: ListApplicationsForPrivateAccessPolicyRequest
        @return: ListApplicationsForPrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_for_private_access_policy_with_options_async(request, runtime)

    def list_applications_for_private_access_tag_with_options(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessTagResponse:
        """
        @summary 批量查询内网访问标签的应用
        
        @param request: ListApplicationsForPrivateAccessTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForPrivateAccessTagResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForPrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListApplicationsForPrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_for_private_access_tag_with_options_async(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessTagResponse:
        """
        @summary 批量查询内网访问标签的应用
        
        @param request: ListApplicationsForPrivateAccessTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsForPrivateAccessTagResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationsForPrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListApplicationsForPrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications_for_private_access_tag(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessTagRequest,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessTagResponse:
        """
        @summary 批量查询内网访问标签的应用
        
        @param request: ListApplicationsForPrivateAccessTagRequest
        @return: ListApplicationsForPrivateAccessTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_for_private_access_tag_with_options(request, runtime)

    async def list_applications_for_private_access_tag_async(
        self,
        request: csas_20230120_models.ListApplicationsForPrivateAccessTagRequest,
    ) -> csas_20230120_models.ListApplicationsForPrivateAccessTagResponse:
        """
        @summary 批量查询内网访问标签的应用
        
        @param request: ListApplicationsForPrivateAccessTagRequest
        @return: ListApplicationsForPrivateAccessTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_for_private_access_tag_with_options_async(request, runtime)

    def list_client_users_with_options(
        self,
        request: csas_20230120_models.ListClientUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListClientUsersResponse:
        """
        @summary 查询自定义身份源用户
        
        @param request: ListClientUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClientUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClientUsers',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListClientUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_client_users_with_options_async(
        self,
        request: csas_20230120_models.ListClientUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListClientUsersResponse:
        """
        @summary 查询自定义身份源用户
        
        @param request: ListClientUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClientUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClientUsers',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListClientUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_client_users(
        self,
        request: csas_20230120_models.ListClientUsersRequest,
    ) -> csas_20230120_models.ListClientUsersResponse:
        """
        @summary 查询自定义身份源用户
        
        @param request: ListClientUsersRequest
        @return: ListClientUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_client_users_with_options(request, runtime)

    async def list_client_users_async(
        self,
        request: csas_20230120_models.ListClientUsersRequest,
    ) -> csas_20230120_models.ListClientUsersResponse:
        """
        @summary 查询自定义身份源用户
        
        @param request: ListClientUsersRequest
        @return: ListClientUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_client_users_with_options_async(request, runtime)

    def list_connectors_with_options(
        self,
        request: csas_20230120_models.ListConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListConnectorsResponse:
        """
        @summary 批量查询connector
        
        @param request: ListConnectorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConnectorsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnectors',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListConnectorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_connectors_with_options_async(
        self,
        request: csas_20230120_models.ListConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListConnectorsResponse:
        """
        @summary 批量查询connector
        
        @param request: ListConnectorsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListConnectorsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConnectors',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListConnectorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_connectors(
        self,
        request: csas_20230120_models.ListConnectorsRequest,
    ) -> csas_20230120_models.ListConnectorsResponse:
        """
        @summary 批量查询connector
        
        @param request: ListConnectorsRequest
        @return: ListConnectorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_connectors_with_options(request, runtime)

    async def list_connectors_async(
        self,
        request: csas_20230120_models.ListConnectorsRequest,
    ) -> csas_20230120_models.ListConnectorsResponse:
        """
        @summary 批量查询connector
        
        @param request: ListConnectorsRequest
        @return: ListConnectorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_connectors_with_options_async(request, runtime)

    def list_dynamic_route_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListDynamicRouteRegionsResponse:
        """
        @summary 批量查询动态路由的地域
        
        @param request: ListDynamicRouteRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDynamicRouteRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDynamicRouteRegions',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListDynamicRouteRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dynamic_route_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListDynamicRouteRegionsResponse:
        """
        @summary 批量查询动态路由的地域
        
        @param request: ListDynamicRouteRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDynamicRouteRegionsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListDynamicRouteRegions',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListDynamicRouteRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dynamic_route_regions(self) -> csas_20230120_models.ListDynamicRouteRegionsResponse:
        """
        @summary 批量查询动态路由的地域
        
        @return: ListDynamicRouteRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_route_regions_with_options(runtime)

    async def list_dynamic_route_regions_async(self) -> csas_20230120_models.ListDynamicRouteRegionsResponse:
        """
        @summary 批量查询动态路由的地域
        
        @return: ListDynamicRouteRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dynamic_route_regions_with_options_async(runtime)

    def list_dynamic_routes_with_options(
        self,
        request: csas_20230120_models.ListDynamicRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListDynamicRoutesResponse:
        """
        @summary 批量查询动态路由
        
        @param request: ListDynamicRoutesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDynamicRoutesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDynamicRoutes',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListDynamicRoutesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dynamic_routes_with_options_async(
        self,
        request: csas_20230120_models.ListDynamicRoutesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListDynamicRoutesResponse:
        """
        @summary 批量查询动态路由
        
        @param request: ListDynamicRoutesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDynamicRoutesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDynamicRoutes',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListDynamicRoutesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dynamic_routes(
        self,
        request: csas_20230120_models.ListDynamicRoutesRequest,
    ) -> csas_20230120_models.ListDynamicRoutesResponse:
        """
        @summary 批量查询动态路由
        
        @param request: ListDynamicRoutesRequest
        @return: ListDynamicRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_routes_with_options(request, runtime)

    async def list_dynamic_routes_async(
        self,
        request: csas_20230120_models.ListDynamicRoutesRequest,
    ) -> csas_20230120_models.ListDynamicRoutesResponse:
        """
        @summary 批量查询动态路由
        
        @param request: ListDynamicRoutesRequest
        @return: ListDynamicRoutesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dynamic_routes_with_options_async(request, runtime)

    def list_excessive_device_registration_applications_with_options(
        self,
        request: csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsResponse:
        """
        @summary 批量查询超额注册申请列表
        
        @param request: ListExcessiveDeviceRegistrationApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExcessiveDeviceRegistrationApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExcessiveDeviceRegistrationApplications',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_excessive_device_registration_applications_with_options_async(
        self,
        request: csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsResponse:
        """
        @summary 批量查询超额注册申请列表
        
        @param request: ListExcessiveDeviceRegistrationApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExcessiveDeviceRegistrationApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExcessiveDeviceRegistrationApplications',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_excessive_device_registration_applications(
        self,
        request: csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsRequest,
    ) -> csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsResponse:
        """
        @summary 批量查询超额注册申请列表
        
        @param request: ListExcessiveDeviceRegistrationApplicationsRequest
        @return: ListExcessiveDeviceRegistrationApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_excessive_device_registration_applications_with_options(request, runtime)

    async def list_excessive_device_registration_applications_async(
        self,
        request: csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsRequest,
    ) -> csas_20230120_models.ListExcessiveDeviceRegistrationApplicationsResponse:
        """
        @summary 批量查询超额注册申请列表
        
        @param request: ListExcessiveDeviceRegistrationApplicationsRequest
        @return: ListExcessiveDeviceRegistrationApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_excessive_device_registration_applications_with_options_async(request, runtime)

    def list_idp_configs_with_options(
        self,
        request: csas_20230120_models.ListIdpConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListIdpConfigsResponse:
        """
        @summary 查询IDP配置
        
        @param request: ListIdpConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdpConfigsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIdpConfigs',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListIdpConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_idp_configs_with_options_async(
        self,
        request: csas_20230120_models.ListIdpConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListIdpConfigsResponse:
        """
        @summary 查询IDP配置
        
        @param request: ListIdpConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdpConfigsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIdpConfigs',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListIdpConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_idp_configs(
        self,
        request: csas_20230120_models.ListIdpConfigsRequest,
    ) -> csas_20230120_models.ListIdpConfigsResponse:
        """
        @summary 查询IDP配置
        
        @param request: ListIdpConfigsRequest
        @return: ListIdpConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_idp_configs_with_options(request, runtime)

    async def list_idp_configs_async(
        self,
        request: csas_20230120_models.ListIdpConfigsRequest,
    ) -> csas_20230120_models.ListIdpConfigsResponse:
        """
        @summary 查询IDP配置
        
        @param request: ListIdpConfigsRequest
        @return: ListIdpConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_idp_configs_with_options_async(request, runtime)

    def list_idp_departments_with_options(
        self,
        request: csas_20230120_models.ListIdpDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListIdpDepartmentsResponse:
        """
        @summary 查询自定义身份源部门
        
        @param request: ListIdpDepartmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdpDepartmentsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIdpDepartments',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListIdpDepartmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_idp_departments_with_options_async(
        self,
        request: csas_20230120_models.ListIdpDepartmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListIdpDepartmentsResponse:
        """
        @summary 查询自定义身份源部门
        
        @param request: ListIdpDepartmentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIdpDepartmentsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIdpDepartments',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListIdpDepartmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_idp_departments(
        self,
        request: csas_20230120_models.ListIdpDepartmentsRequest,
    ) -> csas_20230120_models.ListIdpDepartmentsResponse:
        """
        @summary 查询自定义身份源部门
        
        @param request: ListIdpDepartmentsRequest
        @return: ListIdpDepartmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_idp_departments_with_options(request, runtime)

    async def list_idp_departments_async(
        self,
        request: csas_20230120_models.ListIdpDepartmentsRequest,
    ) -> csas_20230120_models.ListIdpDepartmentsResponse:
        """
        @summary 查询自定义身份源部门
        
        @param request: ListIdpDepartmentsRequest
        @return: ListIdpDepartmentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_idp_departments_with_options_async(request, runtime)

    def list_nac_user_cert_with_options(
        self,
        request: csas_20230120_models.ListNacUserCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListNacUserCertResponse:
        """
        @summary 入网用户列表
        
        @param request: ListNacUserCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNacUserCertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.department):
            query['Department'] = request.department
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNacUserCert',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListNacUserCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nac_user_cert_with_options_async(
        self,
        request: csas_20230120_models.ListNacUserCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListNacUserCertResponse:
        """
        @summary 入网用户列表
        
        @param request: ListNacUserCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNacUserCertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.department):
            query['Department'] = request.department
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNacUserCert',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListNacUserCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nac_user_cert(
        self,
        request: csas_20230120_models.ListNacUserCertRequest,
    ) -> csas_20230120_models.ListNacUserCertResponse:
        """
        @summary 入网用户列表
        
        @param request: ListNacUserCertRequest
        @return: ListNacUserCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nac_user_cert_with_options(request, runtime)

    async def list_nac_user_cert_async(
        self,
        request: csas_20230120_models.ListNacUserCertRequest,
    ) -> csas_20230120_models.ListNacUserCertResponse:
        """
        @summary 入网用户列表
        
        @param request: ListNacUserCertRequest
        @return: ListNacUserCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_nac_user_cert_with_options_async(request, runtime)

    def list_polices_for_private_access_application_with_options(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse:
        """
        @summary 批量查询内网访问应用的策略
        
        @param request: ListPolicesForPrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicesForPrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_polices_for_private_access_application_with_options_async(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse:
        """
        @summary 批量查询内网访问应用的策略
        
        @param request: ListPolicesForPrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicesForPrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_polices_for_private_access_application(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse:
        """
        @summary 批量查询内网访问应用的策略
        
        @param request: ListPolicesForPrivateAccessApplicationRequest
        @return: ListPolicesForPrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_polices_for_private_access_application_with_options(request, runtime)

    async def list_polices_for_private_access_application_async(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessApplicationResponse:
        """
        @summary 批量查询内网访问应用的策略
        
        @param request: ListPolicesForPrivateAccessApplicationRequest
        @return: ListPolicesForPrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_polices_for_private_access_application_with_options_async(request, runtime)

    def list_polices_for_private_access_tag_with_options(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessTagResponse:
        """
        @summary 批量查询内网访问标签的策略
        
        @param request: ListPolicesForPrivateAccessTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicesForPrivateAccessTagResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForPrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForPrivateAccessTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_polices_for_private_access_tag_with_options_async(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessTagResponse:
        """
        @summary 批量查询内网访问标签的策略
        
        @param request: ListPolicesForPrivateAccessTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicesForPrivateAccessTagResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForPrivateAccessTag',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForPrivateAccessTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_polices_for_private_access_tag(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessTagRequest,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessTagResponse:
        """
        @summary 批量查询内网访问标签的策略
        
        @param request: ListPolicesForPrivateAccessTagRequest
        @return: ListPolicesForPrivateAccessTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_polices_for_private_access_tag_with_options(request, runtime)

    async def list_polices_for_private_access_tag_async(
        self,
        request: csas_20230120_models.ListPolicesForPrivateAccessTagRequest,
    ) -> csas_20230120_models.ListPolicesForPrivateAccessTagResponse:
        """
        @summary 批量查询内网访问标签的策略
        
        @param request: ListPolicesForPrivateAccessTagRequest
        @return: ListPolicesForPrivateAccessTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_polices_for_private_access_tag_with_options_async(request, runtime)

    def list_polices_for_user_group_with_options(
        self,
        request: csas_20230120_models.ListPolicesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForUserGroupResponse:
        """
        @summary 批量查询用户组的策略
        
        @param request: ListPolicesForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicesForUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_polices_for_user_group_with_options_async(
        self,
        request: csas_20230120_models.ListPolicesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPolicesForUserGroupResponse:
        """
        @summary 批量查询用户组的策略
        
        @param request: ListPolicesForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicesForUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicesForUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPolicesForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_polices_for_user_group(
        self,
        request: csas_20230120_models.ListPolicesForUserGroupRequest,
    ) -> csas_20230120_models.ListPolicesForUserGroupResponse:
        """
        @summary 批量查询用户组的策略
        
        @param request: ListPolicesForUserGroupRequest
        @return: ListPolicesForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_polices_for_user_group_with_options(request, runtime)

    async def list_polices_for_user_group_async(
        self,
        request: csas_20230120_models.ListPolicesForUserGroupRequest,
    ) -> csas_20230120_models.ListPolicesForUserGroupResponse:
        """
        @summary 批量查询用户组的策略
        
        @param request: ListPolicesForUserGroupRequest
        @return: ListPolicesForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_polices_for_user_group_with_options_async(request, runtime)

    def list_pop_traffic_statistics_with_options(
        self,
        request: csas_20230120_models.ListPopTrafficStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPopTrafficStatisticsResponse:
        """
        @summary pop节点流量统计
        
        @param request: ListPopTrafficStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPopTrafficStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPopTrafficStatistics',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPopTrafficStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pop_traffic_statistics_with_options_async(
        self,
        request: csas_20230120_models.ListPopTrafficStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPopTrafficStatisticsResponse:
        """
        @summary pop节点流量统计
        
        @param request: ListPopTrafficStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPopTrafficStatisticsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPopTrafficStatistics',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPopTrafficStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pop_traffic_statistics(
        self,
        request: csas_20230120_models.ListPopTrafficStatisticsRequest,
    ) -> csas_20230120_models.ListPopTrafficStatisticsResponse:
        """
        @summary pop节点流量统计
        
        @param request: ListPopTrafficStatisticsRequest
        @return: ListPopTrafficStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_pop_traffic_statistics_with_options(request, runtime)

    async def list_pop_traffic_statistics_async(
        self,
        request: csas_20230120_models.ListPopTrafficStatisticsRequest,
    ) -> csas_20230120_models.ListPopTrafficStatisticsResponse:
        """
        @summary pop节点流量统计
        
        @param request: ListPopTrafficStatisticsRequest
        @return: ListPopTrafficStatisticsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_pop_traffic_statistics_with_options_async(request, runtime)

    def list_private_access_applications_with_options(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsResponse:
        """
        @summary 批量查询内网访问应用
        
        @param request: ListPrivateAccessApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateAccessApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessApplications',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_applications_with_options_async(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsResponse:
        """
        @summary 批量查询内网访问应用
        
        @param request: ListPrivateAccessApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateAccessApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessApplications',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_applications(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsRequest,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsResponse:
        """
        @summary 批量查询内网访问应用
        
        @param request: ListPrivateAccessApplicationsRequest
        @return: ListPrivateAccessApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_applications_with_options(request, runtime)

    async def list_private_access_applications_async(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsRequest,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsResponse:
        """
        @summary 批量查询内网访问应用
        
        @param request: ListPrivateAccessApplicationsRequest
        @return: ListPrivateAccessApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_private_access_applications_with_options_async(request, runtime)

    def list_private_access_applications_for_dynamic_route_with_options(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        """
        @summary 批量查询动态路由的内网访问应用
        
        @param request: ListPrivateAccessApplicationsForDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateAccessApplicationsForDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessApplicationsForDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_applications_for_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        """
        @summary 批量查询动态路由的内网访问应用
        
        @param request: ListPrivateAccessApplicationsForDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateAccessApplicationsForDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessApplicationsForDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_applications_for_dynamic_route(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        """
        @summary 批量查询动态路由的内网访问应用
        
        @param request: ListPrivateAccessApplicationsForDynamicRouteRequest
        @return: ListPrivateAccessApplicationsForDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_applications_for_dynamic_route_with_options(request, runtime)

    async def list_private_access_applications_for_dynamic_route_async(
        self,
        request: csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteRequest,
    ) -> csas_20230120_models.ListPrivateAccessApplicationsForDynamicRouteResponse:
        """
        @summary 批量查询动态路由的内网访问应用
        
        @param request: ListPrivateAccessApplicationsForDynamicRouteRequest
        @return: ListPrivateAccessApplicationsForDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_private_access_applications_for_dynamic_route_with_options_async(request, runtime)

    def list_private_access_polices_with_options(
        self,
        request: csas_20230120_models.ListPrivateAccessPolicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessPolicesResponse:
        """
        @summary 批量查询内网访问策略
        
        @param request: ListPrivateAccessPolicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateAccessPolicesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessPolices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessPolicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_polices_with_options_async(
        self,
        request: csas_20230120_models.ListPrivateAccessPolicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessPolicesResponse:
        """
        @summary 批量查询内网访问策略
        
        @param request: ListPrivateAccessPolicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateAccessPolicesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessPolices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessPolicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_polices(
        self,
        request: csas_20230120_models.ListPrivateAccessPolicesRequest,
    ) -> csas_20230120_models.ListPrivateAccessPolicesResponse:
        """
        @summary 批量查询内网访问策略
        
        @param request: ListPrivateAccessPolicesRequest
        @return: ListPrivateAccessPolicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_polices_with_options(request, runtime)

    async def list_private_access_polices_async(
        self,
        request: csas_20230120_models.ListPrivateAccessPolicesRequest,
    ) -> csas_20230120_models.ListPrivateAccessPolicesResponse:
        """
        @summary 批量查询内网访问策略
        
        @param request: ListPrivateAccessPolicesRequest
        @return: ListPrivateAccessPolicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_private_access_polices_with_options_async(request, runtime)

    def list_private_access_tags_with_options(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessTagsResponse:
        """
        @summary Queries the information about all internal access tags within the current Alibaba Cloud account.
        
        @param request: ListPrivateAccessTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateAccessTagsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessTags',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_tags_with_options_async(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessTagsResponse:
        """
        @summary Queries the information about all internal access tags within the current Alibaba Cloud account.
        
        @param request: ListPrivateAccessTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateAccessTagsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessTags',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_tags(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsRequest,
    ) -> csas_20230120_models.ListPrivateAccessTagsResponse:
        """
        @summary Queries the information about all internal access tags within the current Alibaba Cloud account.
        
        @param request: ListPrivateAccessTagsRequest
        @return: ListPrivateAccessTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_tags_with_options(request, runtime)

    async def list_private_access_tags_async(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsRequest,
    ) -> csas_20230120_models.ListPrivateAccessTagsResponse:
        """
        @summary Queries the information about all internal access tags within the current Alibaba Cloud account.
        
        @param request: ListPrivateAccessTagsRequest
        @return: ListPrivateAccessTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_private_access_tags_with_options_async(request, runtime)

    def list_private_access_tags_for_dynamic_route_with_options(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsForDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse:
        """
        @summary 批量查询动态路由的内网访问标签
        
        @param request: ListPrivateAccessTagsForDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateAccessTagsForDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessTagsForDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_private_access_tags_for_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsForDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse:
        """
        @summary 批量查询动态路由的内网访问标签
        
        @param request: ListPrivateAccessTagsForDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrivateAccessTagsForDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrivateAccessTagsForDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_private_access_tags_for_dynamic_route(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsForDynamicRouteRequest,
    ) -> csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse:
        """
        @summary 批量查询动态路由的内网访问标签
        
        @param request: ListPrivateAccessTagsForDynamicRouteRequest
        @return: ListPrivateAccessTagsForDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_private_access_tags_for_dynamic_route_with_options(request, runtime)

    async def list_private_access_tags_for_dynamic_route_async(
        self,
        request: csas_20230120_models.ListPrivateAccessTagsForDynamicRouteRequest,
    ) -> csas_20230120_models.ListPrivateAccessTagsForDynamicRouteResponse:
        """
        @summary 批量查询动态路由的内网访问标签
        
        @param request: ListPrivateAccessTagsForDynamicRouteRequest
        @return: ListPrivateAccessTagsForDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_private_access_tags_for_dynamic_route_with_options_async(request, runtime)

    def list_registration_policies_with_options(
        self,
        request: csas_20230120_models.ListRegistrationPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListRegistrationPoliciesResponse:
        """
        @summary 查询用户设备注册策略列表
        
        @param request: ListRegistrationPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegistrationPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistrationPolicies',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListRegistrationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_registration_policies_with_options_async(
        self,
        request: csas_20230120_models.ListRegistrationPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListRegistrationPoliciesResponse:
        """
        @summary 查询用户设备注册策略列表
        
        @param request: ListRegistrationPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegistrationPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistrationPolicies',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListRegistrationPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_registration_policies(
        self,
        request: csas_20230120_models.ListRegistrationPoliciesRequest,
    ) -> csas_20230120_models.ListRegistrationPoliciesResponse:
        """
        @summary 查询用户设备注册策略列表
        
        @param request: ListRegistrationPoliciesRequest
        @return: ListRegistrationPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_registration_policies_with_options(request, runtime)

    async def list_registration_policies_async(
        self,
        request: csas_20230120_models.ListRegistrationPoliciesRequest,
    ) -> csas_20230120_models.ListRegistrationPoliciesResponse:
        """
        @summary 查询用户设备注册策略列表
        
        @param request: ListRegistrationPoliciesRequest
        @return: ListRegistrationPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_registration_policies_with_options_async(request, runtime)

    def list_registration_policies_for_user_group_with_options(
        self,
        request: csas_20230120_models.ListRegistrationPoliciesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListRegistrationPoliciesForUserGroupResponse:
        """
        @summary 查询用户组相关的设备注册策略
        
        @param request: ListRegistrationPoliciesForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegistrationPoliciesForUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistrationPoliciesForUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListRegistrationPoliciesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_registration_policies_for_user_group_with_options_async(
        self,
        request: csas_20230120_models.ListRegistrationPoliciesForUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListRegistrationPoliciesForUserGroupResponse:
        """
        @summary 查询用户组相关的设备注册策略
        
        @param request: ListRegistrationPoliciesForUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegistrationPoliciesForUserGroupResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistrationPoliciesForUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListRegistrationPoliciesForUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_registration_policies_for_user_group(
        self,
        request: csas_20230120_models.ListRegistrationPoliciesForUserGroupRequest,
    ) -> csas_20230120_models.ListRegistrationPoliciesForUserGroupResponse:
        """
        @summary 查询用户组相关的设备注册策略
        
        @param request: ListRegistrationPoliciesForUserGroupRequest
        @return: ListRegistrationPoliciesForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_registration_policies_for_user_group_with_options(request, runtime)

    async def list_registration_policies_for_user_group_async(
        self,
        request: csas_20230120_models.ListRegistrationPoliciesForUserGroupRequest,
    ) -> csas_20230120_models.ListRegistrationPoliciesForUserGroupResponse:
        """
        @summary 查询用户组相关的设备注册策略
        
        @param request: ListRegistrationPoliciesForUserGroupRequest
        @return: ListRegistrationPoliciesForUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_registration_policies_for_user_group_with_options_async(request, runtime)

    def list_software_for_user_device_with_options(
        self,
        request: csas_20230120_models.ListSoftwareForUserDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListSoftwareForUserDeviceResponse:
        """
        @summary 批量查询终端安装软件列表
        
        @param request: ListSoftwareForUserDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSoftwareForUserDeviceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSoftwareForUserDevice',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListSoftwareForUserDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_software_for_user_device_with_options_async(
        self,
        request: csas_20230120_models.ListSoftwareForUserDeviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListSoftwareForUserDeviceResponse:
        """
        @summary 批量查询终端安装软件列表
        
        @param request: ListSoftwareForUserDeviceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSoftwareForUserDeviceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSoftwareForUserDevice',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListSoftwareForUserDeviceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_software_for_user_device(
        self,
        request: csas_20230120_models.ListSoftwareForUserDeviceRequest,
    ) -> csas_20230120_models.ListSoftwareForUserDeviceResponse:
        """
        @summary 批量查询终端安装软件列表
        
        @param request: ListSoftwareForUserDeviceRequest
        @return: ListSoftwareForUserDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_software_for_user_device_with_options(request, runtime)

    async def list_software_for_user_device_async(
        self,
        request: csas_20230120_models.ListSoftwareForUserDeviceRequest,
    ) -> csas_20230120_models.ListSoftwareForUserDeviceResponse:
        """
        @summary 批量查询终端安装软件列表
        
        @param request: ListSoftwareForUserDeviceRequest
        @return: ListSoftwareForUserDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_software_for_user_device_with_options_async(request, runtime)

    def list_tags_for_private_access_application_with_options(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListTagsForPrivateAccessApplicationResponse:
        """
        @summary 批量查询内网访问应用的标签
        
        @param request: ListTagsForPrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagsForPrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsForPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListTagsForPrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_for_private_access_application_with_options_async(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListTagsForPrivateAccessApplicationResponse:
        """
        @summary 批量查询内网访问应用的标签
        
        @param request: ListTagsForPrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagsForPrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsForPrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListTagsForPrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags_for_private_access_application(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.ListTagsForPrivateAccessApplicationResponse:
        """
        @summary 批量查询内网访问应用的标签
        
        @param request: ListTagsForPrivateAccessApplicationRequest
        @return: ListTagsForPrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tags_for_private_access_application_with_options(request, runtime)

    async def list_tags_for_private_access_application_async(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessApplicationRequest,
    ) -> csas_20230120_models.ListTagsForPrivateAccessApplicationResponse:
        """
        @summary 批量查询内网访问应用的标签
        
        @param request: ListTagsForPrivateAccessApplicationRequest
        @return: ListTagsForPrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_for_private_access_application_with_options_async(request, runtime)

    def list_tags_for_private_access_policy_with_options(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListTagsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的标签
        
        @param request: ListTagsForPrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagsForPrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListTagsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_for_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListTagsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的标签
        
        @param request: ListTagsForPrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagsForPrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListTagsForPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags_for_private_access_policy(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListTagsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的标签
        
        @param request: ListTagsForPrivateAccessPolicyRequest
        @return: ListTagsForPrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tags_for_private_access_policy_with_options(request, runtime)

    async def list_tags_for_private_access_policy_async(
        self,
        request: csas_20230120_models.ListTagsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListTagsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的标签
        
        @param request: ListTagsForPrivateAccessPolicyRequest
        @return: ListTagsForPrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tags_for_private_access_policy_with_options_async(request, runtime)

    def list_user_applications_with_options(
        self,
        request: csas_20230120_models.ListUserApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserApplicationsResponse:
        """
        @summary 列表查询用户应用权限
        
        @param request: ListUserApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserApplications',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_applications_with_options_async(
        self,
        request: csas_20230120_models.ListUserApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserApplicationsResponse:
        """
        @summary 列表查询用户应用权限
        
        @param request: ListUserApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserApplications',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_applications(
        self,
        request: csas_20230120_models.ListUserApplicationsRequest,
    ) -> csas_20230120_models.ListUserApplicationsResponse:
        """
        @summary 列表查询用户应用权限
        
        @param request: ListUserApplicationsRequest
        @return: ListUserApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_applications_with_options(request, runtime)

    async def list_user_applications_async(
        self,
        request: csas_20230120_models.ListUserApplicationsRequest,
    ) -> csas_20230120_models.ListUserApplicationsResponse:
        """
        @summary 列表查询用户应用权限
        
        @param request: ListUserApplicationsRequest
        @return: ListUserApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_applications_with_options_async(request, runtime)

    def list_user_devices_with_options(
        self,
        request: csas_20230120_models.ListUserDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserDevicesResponse:
        """
        @summary 批量查询用户设备列表
        
        @param request: ListUserDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserDevicesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserDevices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_devices_with_options_async(
        self,
        request: csas_20230120_models.ListUserDevicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserDevicesResponse:
        """
        @summary 批量查询用户设备列表
        
        @param request: ListUserDevicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserDevicesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserDevices',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserDevicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_devices(
        self,
        request: csas_20230120_models.ListUserDevicesRequest,
    ) -> csas_20230120_models.ListUserDevicesResponse:
        """
        @summary 批量查询用户设备列表
        
        @param request: ListUserDevicesRequest
        @return: ListUserDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_devices_with_options(request, runtime)

    async def list_user_devices_async(
        self,
        request: csas_20230120_models.ListUserDevicesRequest,
    ) -> csas_20230120_models.ListUserDevicesResponse:
        """
        @summary 批量查询用户设备列表
        
        @param request: ListUserDevicesRequest
        @return: ListUserDevicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_devices_with_options_async(request, runtime)

    def list_user_groups_with_options(
        self,
        request: csas_20230120_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserGroupsResponse:
        """
        @summary 批量查询用户组
        
        @param request: ListUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_with_options_async(
        self,
        request: csas_20230120_models.ListUserGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserGroupsResponse:
        """
        @summary 批量查询用户组
        
        @param request: ListUserGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups(
        self,
        request: csas_20230120_models.ListUserGroupsRequest,
    ) -> csas_20230120_models.ListUserGroupsResponse:
        """
        @summary 批量查询用户组
        
        @param request: ListUserGroupsRequest
        @return: ListUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    async def list_user_groups_async(
        self,
        request: csas_20230120_models.ListUserGroupsRequest,
    ) -> csas_20230120_models.ListUserGroupsResponse:
        """
        @summary 批量查询用户组
        
        @param request: ListUserGroupsRequest
        @return: ListUserGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_with_options_async(request, runtime)

    def list_user_groups_for_private_access_policy_with_options(
        self,
        request: csas_20230120_models.ListUserGroupsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的用户组
        
        @param request: ListUserGroupsForPrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsForPrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_for_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.ListUserGroupsForPrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的用户组
        
        @param request: ListUserGroupsForPrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsForPrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsForPrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups_for_private_access_policy(
        self,
        request: csas_20230120_models.ListUserGroupsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的用户组
        
        @param request: ListUserGroupsForPrivateAccessPolicyRequest
        @return: ListUserGroupsForPrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_for_private_access_policy_with_options(request, runtime)

    async def list_user_groups_for_private_access_policy_async(
        self,
        request: csas_20230120_models.ListUserGroupsForPrivateAccessPolicyRequest,
    ) -> csas_20230120_models.ListUserGroupsForPrivateAccessPolicyResponse:
        """
        @summary 批量查询内网访问策略的用户组
        
        @param request: ListUserGroupsForPrivateAccessPolicyRequest
        @return: ListUserGroupsForPrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_for_private_access_policy_with_options_async(request, runtime)

    def list_user_groups_for_registration_policy_with_options(
        self,
        request: csas_20230120_models.ListUserGroupsForRegistrationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserGroupsForRegistrationPolicyResponse:
        """
        @summary 查询设备注册策略相关用户组
        
        @param request: ListUserGroupsForRegistrationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsForRegistrationPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsForRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsForRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_groups_for_registration_policy_with_options_async(
        self,
        request: csas_20230120_models.ListUserGroupsForRegistrationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserGroupsForRegistrationPolicyResponse:
        """
        @summary 查询设备注册策略相关用户组
        
        @param request: ListUserGroupsForRegistrationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserGroupsForRegistrationPolicyResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroupsForRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserGroupsForRegistrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_groups_for_registration_policy(
        self,
        request: csas_20230120_models.ListUserGroupsForRegistrationPolicyRequest,
    ) -> csas_20230120_models.ListUserGroupsForRegistrationPolicyResponse:
        """
        @summary 查询设备注册策略相关用户组
        
        @param request: ListUserGroupsForRegistrationPolicyRequest
        @return: ListUserGroupsForRegistrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_for_registration_policy_with_options(request, runtime)

    async def list_user_groups_for_registration_policy_async(
        self,
        request: csas_20230120_models.ListUserGroupsForRegistrationPolicyRequest,
    ) -> csas_20230120_models.ListUserGroupsForRegistrationPolicyResponse:
        """
        @summary 查询设备注册策略相关用户组
        
        @param request: ListUserGroupsForRegistrationPolicyRequest
        @return: ListUserGroupsForRegistrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_groups_for_registration_policy_with_options_async(request, runtime)

    def list_user_private_access_policies_with_options(
        self,
        request: csas_20230120_models.ListUserPrivateAccessPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserPrivateAccessPoliciesResponse:
        """
        @summary 列表查询用户零信任策略
        
        @param request: ListUserPrivateAccessPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserPrivateAccessPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserPrivateAccessPolicies',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserPrivateAccessPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_private_access_policies_with_options_async(
        self,
        request: csas_20230120_models.ListUserPrivateAccessPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUserPrivateAccessPoliciesResponse:
        """
        @summary 列表查询用户零信任策略
        
        @param request: ListUserPrivateAccessPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserPrivateAccessPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserPrivateAccessPolicies',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUserPrivateAccessPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_private_access_policies(
        self,
        request: csas_20230120_models.ListUserPrivateAccessPoliciesRequest,
    ) -> csas_20230120_models.ListUserPrivateAccessPoliciesResponse:
        """
        @summary 列表查询用户零信任策略
        
        @param request: ListUserPrivateAccessPoliciesRequest
        @return: ListUserPrivateAccessPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_private_access_policies_with_options(request, runtime)

    async def list_user_private_access_policies_async(
        self,
        request: csas_20230120_models.ListUserPrivateAccessPoliciesRequest,
    ) -> csas_20230120_models.ListUserPrivateAccessPoliciesResponse:
        """
        @summary 列表查询用户零信任策略
        
        @param request: ListUserPrivateAccessPoliciesRequest
        @return: ListUserPrivateAccessPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_private_access_policies_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: csas_20230120_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUsersResponse:
        """
        @summary 列表查询登陆用户
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: csas_20230120_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.ListUsersResponse:
        """
        @summary 列表查询登陆用户
        
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: csas_20230120_models.ListUsersRequest,
    ) -> csas_20230120_models.ListUsersResponse:
        """
        @summary 列表查询登陆用户
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: csas_20230120_models.ListUsersRequest,
    ) -> csas_20230120_models.ListUsersResponse:
        """
        @summary 列表查询登陆用户
        
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def lookup_wm_info_mapping_with_options(
        self,
        request: csas_20230120_models.LookupWmInfoMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.LookupWmInfoMappingResponse:
        """
        @summary 根据数字水印信息查询字符串水印信息
        
        @param request: LookupWmInfoMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LookupWmInfoMappingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LookupWmInfoMapping',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.LookupWmInfoMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def lookup_wm_info_mapping_with_options_async(
        self,
        request: csas_20230120_models.LookupWmInfoMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.LookupWmInfoMappingResponse:
        """
        @summary 根据数字水印信息查询字符串水印信息
        
        @param request: LookupWmInfoMappingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LookupWmInfoMappingResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LookupWmInfoMapping',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.LookupWmInfoMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def lookup_wm_info_mapping(
        self,
        request: csas_20230120_models.LookupWmInfoMappingRequest,
    ) -> csas_20230120_models.LookupWmInfoMappingResponse:
        """
        @summary 根据数字水印信息查询字符串水印信息
        
        @param request: LookupWmInfoMappingRequest
        @return: LookupWmInfoMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lookup_wm_info_mapping_with_options(request, runtime)

    async def lookup_wm_info_mapping_async(
        self,
        request: csas_20230120_models.LookupWmInfoMappingRequest,
    ) -> csas_20230120_models.LookupWmInfoMappingResponse:
        """
        @summary 根据数字水印信息查询字符串水印信息
        
        @param request: LookupWmInfoMappingRequest
        @return: LookupWmInfoMappingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.lookup_wm_info_mapping_with_options_async(request, runtime)

    def revoke_user_session_with_options(
        self,
        request: csas_20230120_models.RevokeUserSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.RevokeUserSessionResponse:
        """
        @summary 吊销用户登录会话
        
        @param request: RevokeUserSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeUserSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_ids):
            query['ExternalIds'] = request.external_ids
        if not UtilClient.is_unset(request.idp_id):
            query['IdpId'] = request.idp_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeUserSession',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.RevokeUserSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_user_session_with_options_async(
        self,
        request: csas_20230120_models.RevokeUserSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.RevokeUserSessionResponse:
        """
        @summary 吊销用户登录会话
        
        @param request: RevokeUserSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeUserSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_ids):
            query['ExternalIds'] = request.external_ids
        if not UtilClient.is_unset(request.idp_id):
            query['IdpId'] = request.idp_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeUserSession',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.RevokeUserSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_user_session(
        self,
        request: csas_20230120_models.RevokeUserSessionRequest,
    ) -> csas_20230120_models.RevokeUserSessionResponse:
        """
        @summary 吊销用户登录会话
        
        @param request: RevokeUserSessionRequest
        @return: RevokeUserSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_user_session_with_options(request, runtime)

    async def revoke_user_session_async(
        self,
        request: csas_20230120_models.RevokeUserSessionRequest,
    ) -> csas_20230120_models.RevokeUserSessionResponse:
        """
        @summary 吊销用户登录会话
        
        @param request: RevokeUserSessionRequest
        @return: RevokeUserSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_user_session_with_options_async(request, runtime)

    def update_client_user_with_options(
        self,
        request: csas_20230120_models.UpdateClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateClientUserResponse:
        """
        @summary 修改自定义身份源指定用户
        
        @param request: UpdateClientUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClientUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClientUser',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateClientUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_client_user_with_options_async(
        self,
        request: csas_20230120_models.UpdateClientUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateClientUserResponse:
        """
        @summary 修改自定义身份源指定用户
        
        @param request: UpdateClientUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClientUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClientUser',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateClientUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_client_user(
        self,
        request: csas_20230120_models.UpdateClientUserRequest,
    ) -> csas_20230120_models.UpdateClientUserResponse:
        """
        @summary 修改自定义身份源指定用户
        
        @param request: UpdateClientUserRequest
        @return: UpdateClientUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_client_user_with_options(request, runtime)

    async def update_client_user_async(
        self,
        request: csas_20230120_models.UpdateClientUserRequest,
    ) -> csas_20230120_models.UpdateClientUserResponse:
        """
        @summary 修改自定义身份源指定用户
        
        @param request: UpdateClientUserRequest
        @return: UpdateClientUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_client_user_with_options_async(request, runtime)

    def update_client_user_password_with_options(
        self,
        request: csas_20230120_models.UpdateClientUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateClientUserPasswordResponse:
        """
        @summary 修改自定义身份源指定用户密码
        
        @param request: UpdateClientUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClientUserPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClientUserPassword',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateClientUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_client_user_password_with_options_async(
        self,
        request: csas_20230120_models.UpdateClientUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateClientUserPasswordResponse:
        """
        @summary 修改自定义身份源指定用户密码
        
        @param request: UpdateClientUserPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClientUserPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClientUserPassword',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateClientUserPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_client_user_password(
        self,
        request: csas_20230120_models.UpdateClientUserPasswordRequest,
    ) -> csas_20230120_models.UpdateClientUserPasswordResponse:
        """
        @summary 修改自定义身份源指定用户密码
        
        @param request: UpdateClientUserPasswordRequest
        @return: UpdateClientUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_client_user_password_with_options(request, runtime)

    async def update_client_user_password_async(
        self,
        request: csas_20230120_models.UpdateClientUserPasswordRequest,
    ) -> csas_20230120_models.UpdateClientUserPasswordResponse:
        """
        @summary 修改自定义身份源指定用户密码
        
        @param request: UpdateClientUserPasswordRequest
        @return: UpdateClientUserPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_client_user_password_with_options_async(request, runtime)

    def update_client_user_status_with_options(
        self,
        request: csas_20230120_models.UpdateClientUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateClientUserStatusResponse:
        """
        @summary 修改自定义身份源指定用户启用状态
        
        @param request: UpdateClientUserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClientUserStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClientUserStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateClientUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_client_user_status_with_options_async(
        self,
        request: csas_20230120_models.UpdateClientUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateClientUserStatusResponse:
        """
        @summary 修改自定义身份源指定用户启用状态
        
        @param request: UpdateClientUserStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateClientUserStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClientUserStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateClientUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_client_user_status(
        self,
        request: csas_20230120_models.UpdateClientUserStatusRequest,
    ) -> csas_20230120_models.UpdateClientUserStatusResponse:
        """
        @summary 修改自定义身份源指定用户启用状态
        
        @param request: UpdateClientUserStatusRequest
        @return: UpdateClientUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_client_user_status_with_options(request, runtime)

    async def update_client_user_status_async(
        self,
        request: csas_20230120_models.UpdateClientUserStatusRequest,
    ) -> csas_20230120_models.UpdateClientUserStatusResponse:
        """
        @summary 修改自定义身份源指定用户启用状态
        
        @param request: UpdateClientUserStatusRequest
        @return: UpdateClientUserStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_client_user_status_with_options_async(request, runtime)

    def update_dynamic_route_with_options(
        self,
        request: csas_20230120_models.UpdateDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateDynamicRouteResponse:
        """
        @summary 修改动态路由
        
        @param request: UpdateDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dynamic_route_id):
            body['DynamicRouteId'] = request.dynamic_route_id
        if not UtilClient.is_unset(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_hop):
            body['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateDynamicRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dynamic_route_with_options_async(
        self,
        request: csas_20230120_models.UpdateDynamicRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateDynamicRouteResponse:
        """
        @summary 修改动态路由
        
        @param request: UpdateDynamicRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDynamicRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.dynamic_route_id):
            body['DynamicRouteId'] = request.dynamic_route_id
        if not UtilClient.is_unset(request.dynamic_route_type):
            body['DynamicRouteType'] = request.dynamic_route_type
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.next_hop):
            body['NextHop'] = request.next_hop
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_ids):
            body_flat['RegionIds'] = request.region_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDynamicRoute',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateDynamicRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dynamic_route(
        self,
        request: csas_20230120_models.UpdateDynamicRouteRequest,
    ) -> csas_20230120_models.UpdateDynamicRouteResponse:
        """
        @summary 修改动态路由
        
        @param request: UpdateDynamicRouteRequest
        @return: UpdateDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dynamic_route_with_options(request, runtime)

    async def update_dynamic_route_async(
        self,
        request: csas_20230120_models.UpdateDynamicRouteRequest,
    ) -> csas_20230120_models.UpdateDynamicRouteResponse:
        """
        @summary 修改动态路由
        
        @param request: UpdateDynamicRouteRequest
        @return: UpdateDynamicRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dynamic_route_with_options_async(request, runtime)

    def update_excessive_device_registration_applications_status_with_options(
        self,
        request: csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse:
        """
        @summary 批量更新超额注册申请状态
        
        @param request: UpdateExcessiveDeviceRegistrationApplicationsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExcessiveDeviceRegistrationApplicationsStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExcessiveDeviceRegistrationApplicationsStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_excessive_device_registration_applications_status_with_options_async(
        self,
        request: csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse:
        """
        @summary 批量更新超额注册申请状态
        
        @param request: UpdateExcessiveDeviceRegistrationApplicationsStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExcessiveDeviceRegistrationApplicationsStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExcessiveDeviceRegistrationApplicationsStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_excessive_device_registration_applications_status(
        self,
        request: csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusRequest,
    ) -> csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse:
        """
        @summary 批量更新超额注册申请状态
        
        @param request: UpdateExcessiveDeviceRegistrationApplicationsStatusRequest
        @return: UpdateExcessiveDeviceRegistrationApplicationsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_excessive_device_registration_applications_status_with_options(request, runtime)

    async def update_excessive_device_registration_applications_status_async(
        self,
        request: csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusRequest,
    ) -> csas_20230120_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponse:
        """
        @summary 批量更新超额注册申请状态
        
        @param request: UpdateExcessiveDeviceRegistrationApplicationsStatusRequest
        @return: UpdateExcessiveDeviceRegistrationApplicationsStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_excessive_device_registration_applications_status_with_options_async(request, runtime)

    def update_idp_department_with_options(
        self,
        request: csas_20230120_models.UpdateIdpDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateIdpDepartmentResponse:
        """
        @summary 修改指定自定义身份源部门
        
        @param request: UpdateIdpDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIdpDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.department_name):
            query['DepartmentName'] = request.department_name
        if not UtilClient.is_unset(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIdpDepartment',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateIdpDepartmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_idp_department_with_options_async(
        self,
        request: csas_20230120_models.UpdateIdpDepartmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateIdpDepartmentResponse:
        """
        @summary 修改指定自定义身份源部门
        
        @param request: UpdateIdpDepartmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateIdpDepartmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.department_id):
            query['DepartmentId'] = request.department_id
        if not UtilClient.is_unset(request.department_name):
            query['DepartmentName'] = request.department_name
        if not UtilClient.is_unset(request.idp_config_id):
            query['IdpConfigId'] = request.idp_config_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIdpDepartment',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateIdpDepartmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_idp_department(
        self,
        request: csas_20230120_models.UpdateIdpDepartmentRequest,
    ) -> csas_20230120_models.UpdateIdpDepartmentResponse:
        """
        @summary 修改指定自定义身份源部门
        
        @param request: UpdateIdpDepartmentRequest
        @return: UpdateIdpDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_idp_department_with_options(request, runtime)

    async def update_idp_department_async(
        self,
        request: csas_20230120_models.UpdateIdpDepartmentRequest,
    ) -> csas_20230120_models.UpdateIdpDepartmentResponse:
        """
        @summary 修改指定自定义身份源部门
        
        @param request: UpdateIdpDepartmentRequest
        @return: UpdateIdpDepartmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_idp_department_with_options_async(request, runtime)

    def update_nac_user_cert_status_with_options(
        self,
        request: csas_20230120_models.UpdateNacUserCertStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateNacUserCertStatusResponse:
        """
        @summary 更新NAC User 状态
        
        @param request: UpdateNacUserCertStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNacUserCertStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.id_list):
            body_flat['IdList'] = request.id_list
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNacUserCertStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateNacUserCertStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nac_user_cert_status_with_options_async(
        self,
        request: csas_20230120_models.UpdateNacUserCertStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateNacUserCertStatusResponse:
        """
        @summary 更新NAC User 状态
        
        @param request: UpdateNacUserCertStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNacUserCertStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.id_list):
            body_flat['IdList'] = request.id_list
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNacUserCertStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateNacUserCertStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nac_user_cert_status(
        self,
        request: csas_20230120_models.UpdateNacUserCertStatusRequest,
    ) -> csas_20230120_models.UpdateNacUserCertStatusResponse:
        """
        @summary 更新NAC User 状态
        
        @param request: UpdateNacUserCertStatusRequest
        @return: UpdateNacUserCertStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_nac_user_cert_status_with_options(request, runtime)

    async def update_nac_user_cert_status_async(
        self,
        request: csas_20230120_models.UpdateNacUserCertStatusRequest,
    ) -> csas_20230120_models.UpdateNacUserCertStatusResponse:
        """
        @summary 更新NAC User 状态
        
        @param request: UpdateNacUserCertStatusRequest
        @return: UpdateNacUserCertStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_nac_user_cert_status_with_options_async(request, runtime)

    def update_private_access_application_with_options(
        self,
        request: csas_20230120_models.UpdatePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdatePrivateAccessApplicationResponse:
        """
        @summary 修改内网访问应用
        
        @param request: UpdatePrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.addresses):
            body_flat['Addresses'] = request.addresses
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.l_7proxy_domain_automatic_prefix):
            body['L7ProxyDomainAutomaticPrefix'] = request.l_7proxy_domain_automatic_prefix
        if not UtilClient.is_unset(request.l_7proxy_domain_custom):
            body['L7ProxyDomainCustom'] = request.l_7proxy_domain_custom
        if not UtilClient.is_unset(request.l_7proxy_domain_private):
            body['L7ProxyDomainPrivate'] = request.l_7proxy_domain_private
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.port_ranges):
            body_flat['PortRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdatePrivateAccessApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_private_access_application_with_options_async(
        self,
        request: csas_20230120_models.UpdatePrivateAccessApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdatePrivateAccessApplicationResponse:
        """
        @summary 修改内网访问应用
        
        @param request: UpdatePrivateAccessApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrivateAccessApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.addresses):
            body_flat['Addresses'] = request.addresses
        if not UtilClient.is_unset(request.application_id):
            body['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.l_7proxy_domain_automatic_prefix):
            body['L7ProxyDomainAutomaticPrefix'] = request.l_7proxy_domain_automatic_prefix
        if not UtilClient.is_unset(request.l_7proxy_domain_custom):
            body['L7ProxyDomainCustom'] = request.l_7proxy_domain_custom
        if not UtilClient.is_unset(request.l_7proxy_domain_private):
            body['L7ProxyDomainPrivate'] = request.l_7proxy_domain_private
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.port_ranges):
            body_flat['PortRanges'] = request.port_ranges
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrivateAccessApplication',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdatePrivateAccessApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_private_access_application(
        self,
        request: csas_20230120_models.UpdatePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.UpdatePrivateAccessApplicationResponse:
        """
        @summary 修改内网访问应用
        
        @param request: UpdatePrivateAccessApplicationRequest
        @return: UpdatePrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_private_access_application_with_options(request, runtime)

    async def update_private_access_application_async(
        self,
        request: csas_20230120_models.UpdatePrivateAccessApplicationRequest,
    ) -> csas_20230120_models.UpdatePrivateAccessApplicationResponse:
        """
        @summary 修改内网访问应用
        
        @param request: UpdatePrivateAccessApplicationRequest
        @return: UpdatePrivateAccessApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_private_access_application_with_options_async(request, runtime)

    def update_private_access_policy_with_options(
        self,
        request: csas_20230120_models.UpdatePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdatePrivateAccessPolicyResponse:
        """
        @summary 修改内网访问策略
        
        @param request: UpdatePrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes):
            body_flat['CustomUserAttributes'] = request.custom_user_attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_attribute_action):
            body['DeviceAttributeAction'] = request.device_attribute_action
        if not UtilClient.is_unset(request.device_attribute_id):
            body['DeviceAttributeId'] = request.device_attribute_id
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdatePrivateAccessPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_private_access_policy_with_options_async(
        self,
        request: csas_20230120_models.UpdatePrivateAccessPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdatePrivateAccessPolicyResponse:
        """
        @summary 修改内网访问策略
        
        @param request: UpdatePrivateAccessPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePrivateAccessPolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.application_ids):
            body_flat['ApplicationIds'] = request.application_ids
        if not UtilClient.is_unset(request.application_type):
            body['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.custom_user_attributes):
            body_flat['CustomUserAttributes'] = request.custom_user_attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_attribute_action):
            body['DeviceAttributeAction'] = request.device_attribute_action
        if not UtilClient.is_unset(request.device_attribute_id):
            body['DeviceAttributeId'] = request.device_attribute_id
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.policy_action):
            body['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.tag_ids):
            body_flat['TagIds'] = request.tag_ids
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.user_group_mode):
            body['UserGroupMode'] = request.user_group_mode
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrivateAccessPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdatePrivateAccessPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_private_access_policy(
        self,
        request: csas_20230120_models.UpdatePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.UpdatePrivateAccessPolicyResponse:
        """
        @summary 修改内网访问策略
        
        @param request: UpdatePrivateAccessPolicyRequest
        @return: UpdatePrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_private_access_policy_with_options(request, runtime)

    async def update_private_access_policy_async(
        self,
        request: csas_20230120_models.UpdatePrivateAccessPolicyRequest,
    ) -> csas_20230120_models.UpdatePrivateAccessPolicyResponse:
        """
        @summary 修改内网访问策略
        
        @param request: UpdatePrivateAccessPolicyRequest
        @return: UpdatePrivateAccessPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_private_access_policy_with_options_async(request, runtime)

    def update_registration_policy_with_options(
        self,
        tmp_req: csas_20230120_models.UpdateRegistrationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateRegistrationPolicyResponse:
        """
        @summary 修改设备注册策略
        
        @param tmp_req: UpdateRegistrationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRegistrationPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.UpdateRegistrationPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.company_limit_count):
            request.company_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.company_limit_count, 'CompanyLimitCount', 'json')
        if not UtilClient.is_unset(tmp_req.personal_limit_count):
            request.personal_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.personal_limit_count, 'PersonalLimitCount', 'json')
        body = {}
        if not UtilClient.is_unset(request.company_limit_count_shrink):
            body['CompanyLimitCount'] = request.company_limit_count_shrink
        if not UtilClient.is_unset(request.company_limit_type):
            body['CompanyLimitType'] = request.company_limit_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.match_mode):
            body['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.personal_limit_count_shrink):
            body['PersonalLimitCount'] = request.personal_limit_count_shrink
        if not UtilClient.is_unset(request.personal_limit_type):
            body['PersonalLimitType'] = request.personal_limit_type
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.whitelist):
            body_flat['Whitelist'] = request.whitelist
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateRegistrationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_registration_policy_with_options_async(
        self,
        tmp_req: csas_20230120_models.UpdateRegistrationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateRegistrationPolicyResponse:
        """
        @summary 修改设备注册策略
        
        @param tmp_req: UpdateRegistrationPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRegistrationPolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = csas_20230120_models.UpdateRegistrationPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.company_limit_count):
            request.company_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.company_limit_count, 'CompanyLimitCount', 'json')
        if not UtilClient.is_unset(tmp_req.personal_limit_count):
            request.personal_limit_count_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.personal_limit_count, 'PersonalLimitCount', 'json')
        body = {}
        if not UtilClient.is_unset(request.company_limit_count_shrink):
            body['CompanyLimitCount'] = request.company_limit_count_shrink
        if not UtilClient.is_unset(request.company_limit_type):
            body['CompanyLimitType'] = request.company_limit_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.match_mode):
            body['MatchMode'] = request.match_mode
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.personal_limit_count_shrink):
            body['PersonalLimitCount'] = request.personal_limit_count_shrink
        if not UtilClient.is_unset(request.personal_limit_type):
            body['PersonalLimitType'] = request.personal_limit_type
        if not UtilClient.is_unset(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        body_flat = {}
        if not UtilClient.is_unset(request.user_group_ids):
            body_flat['UserGroupIds'] = request.user_group_ids
        if not UtilClient.is_unset(request.whitelist):
            body_flat['Whitelist'] = request.whitelist
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRegistrationPolicy',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateRegistrationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_registration_policy(
        self,
        request: csas_20230120_models.UpdateRegistrationPolicyRequest,
    ) -> csas_20230120_models.UpdateRegistrationPolicyResponse:
        """
        @summary 修改设备注册策略
        
        @param request: UpdateRegistrationPolicyRequest
        @return: UpdateRegistrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_registration_policy_with_options(request, runtime)

    async def update_registration_policy_async(
        self,
        request: csas_20230120_models.UpdateRegistrationPolicyRequest,
    ) -> csas_20230120_models.UpdateRegistrationPolicyResponse:
        """
        @summary 修改设备注册策略
        
        @param request: UpdateRegistrationPolicyRequest
        @return: UpdateRegistrationPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_registration_policy_with_options_async(request, runtime)

    def update_user_devices_sharing_status_with_options(
        self,
        request: csas_20230120_models.UpdateUserDevicesSharingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateUserDevicesSharingStatusResponse:
        """
        @summary 批量更新用户设备共享状态
        
        @param request: UpdateUserDevicesSharingStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserDevicesSharingStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        if not UtilClient.is_unset(request.sharing_status):
            body['SharingStatus'] = request.sharing_status
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserDevicesSharingStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserDevicesSharingStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_devices_sharing_status_with_options_async(
        self,
        request: csas_20230120_models.UpdateUserDevicesSharingStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateUserDevicesSharingStatusResponse:
        """
        @summary 批量更新用户设备共享状态
        
        @param request: UpdateUserDevicesSharingStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserDevicesSharingStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        if not UtilClient.is_unset(request.sharing_status):
            body['SharingStatus'] = request.sharing_status
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserDevicesSharingStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserDevicesSharingStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_devices_sharing_status(
        self,
        request: csas_20230120_models.UpdateUserDevicesSharingStatusRequest,
    ) -> csas_20230120_models.UpdateUserDevicesSharingStatusResponse:
        """
        @summary 批量更新用户设备共享状态
        
        @param request: UpdateUserDevicesSharingStatusRequest
        @return: UpdateUserDevicesSharingStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_devices_sharing_status_with_options(request, runtime)

    async def update_user_devices_sharing_status_async(
        self,
        request: csas_20230120_models.UpdateUserDevicesSharingStatusRequest,
    ) -> csas_20230120_models.UpdateUserDevicesSharingStatusResponse:
        """
        @summary 批量更新用户设备共享状态
        
        @param request: UpdateUserDevicesSharingStatusRequest
        @return: UpdateUserDevicesSharingStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_devices_sharing_status_with_options_async(request, runtime)

    def update_user_devices_status_with_options(
        self,
        request: csas_20230120_models.UpdateUserDevicesStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateUserDevicesStatusResponse:
        """
        @summary 批量更新用户设备状态
        
        @param request: UpdateUserDevicesStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserDevicesStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_action):
            body['DeviceAction'] = request.device_action
        body_flat = {}
        if not UtilClient.is_unset(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserDevicesStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserDevicesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_devices_status_with_options_async(
        self,
        request: csas_20230120_models.UpdateUserDevicesStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateUserDevicesStatusResponse:
        """
        @summary 批量更新用户设备状态
        
        @param request: UpdateUserDevicesStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserDevicesStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_action):
            body['DeviceAction'] = request.device_action
        body_flat = {}
        if not UtilClient.is_unset(request.device_tags):
            body_flat['DeviceTags'] = request.device_tags
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserDevicesStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserDevicesStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_devices_status(
        self,
        request: csas_20230120_models.UpdateUserDevicesStatusRequest,
    ) -> csas_20230120_models.UpdateUserDevicesStatusResponse:
        """
        @summary 批量更新用户设备状态
        
        @param request: UpdateUserDevicesStatusRequest
        @return: UpdateUserDevicesStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_devices_status_with_options(request, runtime)

    async def update_user_devices_status_async(
        self,
        request: csas_20230120_models.UpdateUserDevicesStatusRequest,
    ) -> csas_20230120_models.UpdateUserDevicesStatusResponse:
        """
        @summary 批量更新用户设备状态
        
        @param request: UpdateUserDevicesStatusRequest
        @return: UpdateUserDevicesStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_devices_status_with_options_async(request, runtime)

    def update_user_group_with_options(
        self,
        request: csas_20230120_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateUserGroupResponse:
        """
        @summary 修改用户组
        
        @param request: UpdateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_group_with_options_async(
        self,
        request: csas_20230120_models.UpdateUserGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateUserGroupResponse:
        """
        @summary 修改用户组
        
        @param request: UpdateUserGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.attributes):
            body_flat['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.modify_type):
            body['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUserGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_group(
        self,
        request: csas_20230120_models.UpdateUserGroupRequest,
    ) -> csas_20230120_models.UpdateUserGroupResponse:
        """
        @summary 修改用户组
        
        @param request: UpdateUserGroupRequest
        @return: UpdateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    async def update_user_group_async(
        self,
        request: csas_20230120_models.UpdateUserGroupRequest,
    ) -> csas_20230120_models.UpdateUserGroupResponse:
        """
        @summary 修改用户组
        
        @param request: UpdateUserGroupRequest
        @return: UpdateUserGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_group_with_options_async(request, runtime)

    def update_users_status_with_options(
        self,
        request: csas_20230120_models.UpdateUsersStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateUsersStatusResponse:
        """
        @summary 批量修改登陆用户状态
        
        @param request: UpdateUsersStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUsersStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sase_user_ids):
            query['SaseUserIds'] = request.sase_user_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUsersStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUsersStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_users_status_with_options_async(
        self,
        request: csas_20230120_models.UpdateUsersStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> csas_20230120_models.UpdateUsersStatusResponse:
        """
        @summary 批量修改登陆用户状态
        
        @param request: UpdateUsersStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUsersStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.sase_user_ids):
            query['SaseUserIds'] = request.sase_user_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUsersStatus',
            version='2023-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            csas_20230120_models.UpdateUsersStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_users_status(
        self,
        request: csas_20230120_models.UpdateUsersStatusRequest,
    ) -> csas_20230120_models.UpdateUsersStatusResponse:
        """
        @summary 批量修改登陆用户状态
        
        @param request: UpdateUsersStatusRequest
        @return: UpdateUsersStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_users_status_with_options(request, runtime)

    async def update_users_status_async(
        self,
        request: csas_20230120_models.UpdateUsersStatusRequest,
    ) -> csas_20230120_models.UpdateUsersStatusResponse:
        """
        @summary 批量修改登陆用户状态
        
        @param request: UpdateUsersStatusRequest
        @return: UpdateUsersStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_users_status_with_options_async(request, runtime)
