# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_appstream_center20210903 import models as appstream_center_20210903_models
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
        self._endpoint = self.get_endpoint('appstream-center', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_connection_ticket_with_options(
        self,
        request: appstream_center_20210903_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.GetConnectionTicketResponse:
        """
        @summary 获取连接信息
        
        @param request: GetConnectionTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_type):
            body['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.auto_connect_in_queue):
            body['AutoConnectInQueue'] = request.auto_connect_in_queue
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.connection_properties):
            body['ConnectionProperties'] = request.connection_properties
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.environment_config):
            body['EnvironmentConfig'] = request.environment_config
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.GetConnectionTicketResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def get_connection_ticket_with_options_async(
        self,
        request: appstream_center_20210903_models.GetConnectionTicketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.GetConnectionTicketResponse:
        """
        @summary 获取连接信息
        
        @param request: GetConnectionTicketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetConnectionTicketResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_type):
            body['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.auto_connect_in_queue):
            body['AutoConnectInQueue'] = request.auto_connect_in_queue
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.connection_properties):
            body['ConnectionProperties'] = request.connection_properties
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.environment_config):
            body['EnvironmentConfig'] = request.environment_config
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConnectionTicket',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.GetConnectionTicketResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def get_connection_ticket(
        self,
        request: appstream_center_20210903_models.GetConnectionTicketRequest,
    ) -> appstream_center_20210903_models.GetConnectionTicketResponse:
        """
        @summary 获取连接信息
        
        @param request: GetConnectionTicketRequest
        @return: GetConnectionTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    async def get_connection_ticket_async(
        self,
        request: appstream_center_20210903_models.GetConnectionTicketRequest,
    ) -> appstream_center_20210903_models.GetConnectionTicketResponse:
        """
        @summary 获取连接信息
        
        @param request: GetConnectionTicketRequest
        @return: GetConnectionTicketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_connection_ticket_with_options_async(request, runtime)

    def list_published_app_info_with_options(
        self,
        request: appstream_center_20210903_models.ListPublishedAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.ListPublishedAppInfoResponse:
        """
        @summary 已上架应用列表
        
        @param request: ListPublishedAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishedAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.category_type):
            query['CategoryType'] = request.category_type
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.order_param):
            query['OrderParam'] = request.order_param
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedAppInfo',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.ListPublishedAppInfoResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def list_published_app_info_with_options_async(
        self,
        request: appstream_center_20210903_models.ListPublishedAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.ListPublishedAppInfoResponse:
        """
        @summary 已上架应用列表
        
        @param request: ListPublishedAppInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPublishedAppInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.category_type):
            query['CategoryType'] = request.category_type
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.order_param):
            query['OrderParam'] = request.order_param
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublishedAppInfo',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.ListPublishedAppInfoResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def list_published_app_info(
        self,
        request: appstream_center_20210903_models.ListPublishedAppInfoRequest,
    ) -> appstream_center_20210903_models.ListPublishedAppInfoResponse:
        """
        @summary 已上架应用列表
        
        @param request: ListPublishedAppInfoRequest
        @return: ListPublishedAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_published_app_info_with_options(request, runtime)

    async def list_published_app_info_async(
        self,
        request: appstream_center_20210903_models.ListPublishedAppInfoRequest,
    ) -> appstream_center_20210903_models.ListPublishedAppInfoResponse:
        """
        @summary 已上架应用列表
        
        @param request: ListPublishedAppInfoRequest
        @return: ListPublishedAppInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_published_app_info_with_options_async(request, runtime)

    def list_running_apps_with_options(
        self,
        request: appstream_center_20210903_models.ListRunningAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.ListRunningAppsResponse:
        """
        @summary 运行中应用列表
        
        @param request: ListRunningAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRunningAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRunningApps',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.ListRunningAppsResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def list_running_apps_with_options_async(
        self,
        request: appstream_center_20210903_models.ListRunningAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.ListRunningAppsResponse:
        """
        @summary 运行中应用列表
        
        @param request: ListRunningAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRunningAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            query['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            query['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            query['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRunningApps',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.ListRunningAppsResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def list_running_apps(
        self,
        request: appstream_center_20210903_models.ListRunningAppsRequest,
    ) -> appstream_center_20210903_models.ListRunningAppsResponse:
        """
        @summary 运行中应用列表
        
        @param request: ListRunningAppsRequest
        @return: ListRunningAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_running_apps_with_options(request, runtime)

    async def list_running_apps_async(
        self,
        request: appstream_center_20210903_models.ListRunningAppsRequest,
    ) -> appstream_center_20210903_models.ListRunningAppsResponse:
        """
        @summary 运行中应用列表
        
        @param request: ListRunningAppsRequest
        @return: ListRunningAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_running_apps_with_options_async(request, runtime)

    def reset_app_resources_with_options(
        self,
        request: appstream_center_20210903_models.ResetAppResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.ResetAppResourcesResponse:
        """
        @summary 重置应用资源
        
        @param request: ResetAppResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAppResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAppResources',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.ResetAppResourcesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def reset_app_resources_with_options_async(
        self,
        request: appstream_center_20210903_models.ResetAppResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.ResetAppResourcesResponse:
        """
        @summary 重置应用资源
        
        @param request: ResetAppResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAppResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAppResources',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.ResetAppResourcesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def reset_app_resources(
        self,
        request: appstream_center_20210903_models.ResetAppResourcesRequest,
    ) -> appstream_center_20210903_models.ResetAppResourcesResponse:
        """
        @summary 重置应用资源
        
        @param request: ResetAppResourcesRequest
        @return: ResetAppResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_app_resources_with_options(request, runtime)

    async def reset_app_resources_async(
        self,
        request: appstream_center_20210903_models.ResetAppResourcesRequest,
    ) -> appstream_center_20210903_models.ResetAppResourcesResponse:
        """
        @summary 重置应用资源
        
        @param request: ResetAppResourcesRequest
        @return: ResetAppResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_app_resources_with_options_async(request, runtime)

    def restart_app_resources_with_options(
        self,
        request: appstream_center_20210903_models.RestartAppResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.RestartAppResourcesResponse:
        """
        @summary 重启应用资源
        
        @param request: RestartAppResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartAppResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartAppResources',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.RestartAppResourcesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def restart_app_resources_with_options_async(
        self,
        request: appstream_center_20210903_models.RestartAppResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.RestartAppResourcesResponse:
        """
        @summary 重启应用资源
        
        @param request: RestartAppResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartAppResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartAppResources',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.RestartAppResourcesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def restart_app_resources(
        self,
        request: appstream_center_20210903_models.RestartAppResourcesRequest,
    ) -> appstream_center_20210903_models.RestartAppResourcesResponse:
        """
        @summary 重启应用资源
        
        @param request: RestartAppResourcesRequest
        @return: RestartAppResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_app_resources_with_options(request, runtime)

    async def restart_app_resources_async(
        self,
        request: appstream_center_20210903_models.RestartAppResourcesRequest,
    ) -> appstream_center_20210903_models.RestartAppResourcesResponse:
        """
        @summary 重启应用资源
        
        @param request: RestartAppResourcesRequest
        @return: RestartAppResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_app_resources_with_options_async(request, runtime)

    def start_app_resources_with_options(
        self,
        request: appstream_center_20210903_models.StartAppResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.StartAppResourcesResponse:
        """
        @summary 启动应用资源
        
        @param request: StartAppResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAppResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartAppResources',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.StartAppResourcesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def start_app_resources_with_options_async(
        self,
        request: appstream_center_20210903_models.StartAppResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.StartAppResourcesResponse:
        """
        @summary 启动应用资源
        
        @param request: StartAppResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartAppResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartAppResources',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.StartAppResourcesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def start_app_resources(
        self,
        request: appstream_center_20210903_models.StartAppResourcesRequest,
    ) -> appstream_center_20210903_models.StartAppResourcesResponse:
        """
        @summary 启动应用资源
        
        @param request: StartAppResourcesRequest
        @return: StartAppResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_app_resources_with_options(request, runtime)

    async def start_app_resources_async(
        self,
        request: appstream_center_20210903_models.StartAppResourcesRequest,
    ) -> appstream_center_20210903_models.StartAppResourcesResponse:
        """
        @summary 启动应用资源
        
        @param request: StartAppResourcesRequest
        @return: StartAppResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_app_resources_with_options_async(request, runtime)

    def stop_app_with_options(
        self,
        request: appstream_center_20210903_models.StopAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.StopAppResponse:
        """
        @summary 停止应用
        
        @param request: StopAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_channel):
            body['ClientChannel'] = request.client_channel
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.force_stop):
            body['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.idp_id):
            body['IdpId'] = request.idp_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.wy_id):
            body['WyId'] = request.wy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopApp',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.StopAppResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def stop_app_with_options_async(
        self,
        request: appstream_center_20210903_models.StopAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.StopAppResponse:
        """
        @summary 停止应用
        
        @param request: StopAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_channel):
            body['ClientChannel'] = request.client_channel
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.force_stop):
            body['ForceStop'] = request.force_stop
        if not UtilClient.is_unset(request.idp_id):
            body['IdpId'] = request.idp_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.wy_id):
            body['WyId'] = request.wy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopApp',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.StopAppResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def stop_app(
        self,
        request: appstream_center_20210903_models.StopAppRequest,
    ) -> appstream_center_20210903_models.StopAppResponse:
        """
        @summary 停止应用
        
        @param request: StopAppRequest
        @return: StopAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_app_with_options(request, runtime)

    async def stop_app_async(
        self,
        request: appstream_center_20210903_models.StopAppRequest,
    ) -> appstream_center_20210903_models.StopAppResponse:
        """
        @summary 停止应用
        
        @param request: StopAppRequest
        @return: StopAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_app_with_options_async(request, runtime)

    def stop_app_resources_with_options(
        self,
        request: appstream_center_20210903_models.StopAppResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.StopAppResourcesResponse:
        """
        @summary 关闭应用资源
        
        @param request: StopAppResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAppResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopAppResources',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.StopAppResourcesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def stop_app_resources_with_options_async(
        self,
        request: appstream_center_20210903_models.StopAppResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.StopAppResourcesResponse:
        """
        @summary 关闭应用资源
        
        @param request: StopAppResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopAppResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopAppResources',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.StopAppResourcesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def stop_app_resources(
        self,
        request: appstream_center_20210903_models.StopAppResourcesRequest,
    ) -> appstream_center_20210903_models.StopAppResourcesResponse:
        """
        @summary 关闭应用资源
        
        @param request: StopAppResourcesRequest
        @return: StopAppResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_app_resources_with_options(request, runtime)

    async def stop_app_resources_async(
        self,
        request: appstream_center_20210903_models.StopAppResourcesRequest,
    ) -> appstream_center_20210903_models.StopAppResourcesResponse:
        """
        @summary 关闭应用资源
        
        @param request: StopAppResourcesRequest
        @return: StopAppResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_app_resources_with_options_async(request, runtime)

    def unbind_with_options(
        self,
        request: appstream_center_20210903_models.UnbindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.UnbindResponse:
        """
        @summary 解绑实例
        
        @param request: UnbindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Unbind',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.UnbindResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def unbind_with_options_async(
        self,
        request: appstream_center_20210903_models.UnbindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> appstream_center_20210903_models.UnbindResponse:
        """
        @summary 解绑实例
        
        @param request: UnbindRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnbindResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not UtilClient.is_unset(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.client_id):
            body['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.client_os):
            body['ClientOS'] = request.client_os
        if not UtilClient.is_unset(request.client_version):
            body['ClientVersion'] = request.client_version
        if not UtilClient.is_unset(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not UtilClient.is_unset(request.login_token):
            body['LoginToken'] = request.login_token
        if not UtilClient.is_unset(request.product_type):
            body['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Unbind',
            version='2021-09-03',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            appstream_center_20210903_models.UnbindResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def unbind(
        self,
        request: appstream_center_20210903_models.UnbindRequest,
    ) -> appstream_center_20210903_models.UnbindResponse:
        """
        @summary 解绑实例
        
        @param request: UnbindRequest
        @return: UnbindResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.unbind_with_options(request, runtime)

    async def unbind_async(
        self,
        request: appstream_center_20210903_models.UnbindRequest,
    ) -> appstream_center_20210903_models.UnbindResponse:
        """
        @summary 解绑实例
        
        @param request: UnbindRequest
        @return: UnbindResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.unbind_with_options_async(request, runtime)
