# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_appstream_center20210903 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_connection_ticket_with_options(
        self,
        request: main_models.GetConnectionTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectionTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_type):
            body['AccessType'] = request.access_type
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.auto_connect_in_queue):
            body['AutoConnectInQueue'] = request.auto_connect_in_queue
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_type):
            body['ClientType'] = request.client_type
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.connection_properties):
            body['ConnectionProperties'] = request.connection_properties
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.environment_config):
            body['EnvironmentConfig'] = request.environment_config
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.param):
            body['Param'] = request.param
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetConnectionTicket',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectionTicketResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def get_connection_ticket_with_options_async(
        self,
        request: main_models.GetConnectionTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConnectionTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_type):
            body['AccessType'] = request.access_type
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.app_policy_id):
            body['AppPolicyId'] = request.app_policy_id
        if not DaraCore.is_null(request.app_version):
            body['AppVersion'] = request.app_version
        if not DaraCore.is_null(request.auto_connect_in_queue):
            body['AutoConnectInQueue'] = request.auto_connect_in_queue
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_type):
            body['ClientType'] = request.client_type
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.connection_properties):
            body['ConnectionProperties'] = request.connection_properties
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.environment_config):
            body['EnvironmentConfig'] = request.environment_config
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.param):
            body['Param'] = request.param
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetConnectionTicket',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConnectionTicketResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def get_connection_ticket(
        self,
        request: main_models.GetConnectionTicketRequest,
    ) -> main_models.GetConnectionTicketResponse:
        runtime = RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    async def get_connection_ticket_async(
        self,
        request: main_models.GetConnectionTicketRequest,
    ) -> main_models.GetConnectionTicketResponse:
        runtime = RuntimeOptions()
        return await self.get_connection_ticket_with_options_async(request, runtime)

    def list_published_app_info_with_options(
        self,
        request: main_models.ListPublishedAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishedAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_type):
            query['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.order_param):
            query['OrderParam'] = request.order_param
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishedAppInfo',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishedAppInfoResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def list_published_app_info_with_options_async(
        self,
        request: main_models.ListPublishedAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPublishedAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.category_type):
            query['CategoryType'] = request.category_type
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.order_param):
            query['OrderParam'] = request.order_param
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPublishedAppInfo',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPublishedAppInfoResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def list_published_app_info(
        self,
        request: main_models.ListPublishedAppInfoRequest,
    ) -> main_models.ListPublishedAppInfoResponse:
        runtime = RuntimeOptions()
        return self.list_published_app_info_with_options(request, runtime)

    async def list_published_app_info_async(
        self,
        request: main_models.ListPublishedAppInfoRequest,
    ) -> main_models.ListPublishedAppInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_published_app_info_with_options_async(request, runtime)

    def list_running_apps_with_options(
        self,
        request: main_models.ListRunningAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRunningAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRunningApps',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRunningAppsResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def list_running_apps_with_options_async(
        self,
        request: main_models.ListRunningAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRunningAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            query['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            query['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            query['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            query['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.tenant_id):
            query['TenantId'] = request.tenant_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRunningApps',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRunningAppsResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def list_running_apps(
        self,
        request: main_models.ListRunningAppsRequest,
    ) -> main_models.ListRunningAppsResponse:
        runtime = RuntimeOptions()
        return self.list_running_apps_with_options(request, runtime)

    async def list_running_apps_async(
        self,
        request: main_models.ListRunningAppsRequest,
    ) -> main_models.ListRunningAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_running_apps_with_options_async(request, runtime)

    def reset_app_resources_with_options(
        self,
        request: main_models.ResetAppResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAppResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetAppResources',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAppResourcesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def reset_app_resources_with_options_async(
        self,
        request: main_models.ResetAppResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAppResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetAppResources',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAppResourcesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def reset_app_resources(
        self,
        request: main_models.ResetAppResourcesRequest,
    ) -> main_models.ResetAppResourcesResponse:
        runtime = RuntimeOptions()
        return self.reset_app_resources_with_options(request, runtime)

    async def reset_app_resources_async(
        self,
        request: main_models.ResetAppResourcesRequest,
    ) -> main_models.ResetAppResourcesResponse:
        runtime = RuntimeOptions()
        return await self.reset_app_resources_with_options_async(request, runtime)

    def restart_app_resources_with_options(
        self,
        request: main_models.RestartAppResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartAppResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartAppResources',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartAppResourcesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def restart_app_resources_with_options_async(
        self,
        request: main_models.RestartAppResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartAppResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartAppResources',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartAppResourcesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def restart_app_resources(
        self,
        request: main_models.RestartAppResourcesRequest,
    ) -> main_models.RestartAppResourcesResponse:
        runtime = RuntimeOptions()
        return self.restart_app_resources_with_options(request, runtime)

    async def restart_app_resources_async(
        self,
        request: main_models.RestartAppResourcesRequest,
    ) -> main_models.RestartAppResourcesResponse:
        runtime = RuntimeOptions()
        return await self.restart_app_resources_with_options_async(request, runtime)

    def start_app_resources_with_options(
        self,
        request: main_models.StartAppResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAppResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAppResources',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAppResourcesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def start_app_resources_with_options_async(
        self,
        request: main_models.StartAppResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAppResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAppResources',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAppResourcesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def start_app_resources(
        self,
        request: main_models.StartAppResourcesRequest,
    ) -> main_models.StartAppResourcesResponse:
        runtime = RuntimeOptions()
        return self.start_app_resources_with_options(request, runtime)

    async def start_app_resources_async(
        self,
        request: main_models.StartAppResourcesRequest,
    ) -> main_models.StartAppResourcesResponse:
        runtime = RuntimeOptions()
        return await self.start_app_resources_with_options_async(request, runtime)

    def stop_app_with_options(
        self,
        request: main_models.StopAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not DaraCore.is_null(request.api_type):
            body['ApiType'] = request.api_type
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_channel):
            body['ClientChannel'] = request.client_channel
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.force_stop):
            body['ForceStop'] = request.force_stop
        if not DaraCore.is_null(request.idp_id):
            body['IdpId'] = request.idp_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        if not DaraCore.is_null(request.wy_id):
            body['WyId'] = request.wy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopApp',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAppResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def stop_app_with_options_async(
        self,
        request: main_models.StopAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAppResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ali_uid):
            body['AliUid'] = request.ali_uid
        if not DaraCore.is_null(request.api_type):
            body['ApiType'] = request.api_type
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_channel):
            body['ClientChannel'] = request.client_channel
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.force_stop):
            body['ForceStop'] = request.force_stop
        if not DaraCore.is_null(request.idp_id):
            body['IdpId'] = request.idp_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        if not DaraCore.is_null(request.wy_id):
            body['WyId'] = request.wy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopApp',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAppResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def stop_app(
        self,
        request: main_models.StopAppRequest,
    ) -> main_models.StopAppResponse:
        runtime = RuntimeOptions()
        return self.stop_app_with_options(request, runtime)

    async def stop_app_async(
        self,
        request: main_models.StopAppRequest,
    ) -> main_models.StopAppResponse:
        runtime = RuntimeOptions()
        return await self.stop_app_with_options_async(request, runtime)

    def stop_app_resources_with_options(
        self,
        request: main_models.StopAppResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAppResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopAppResources',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAppResourcesResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def stop_app_resources_with_options_async(
        self,
        request: main_models.StopAppResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAppResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.biz_region_id):
            body['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.uuid):
            body['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopAppResources',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAppResourcesResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def stop_app_resources(
        self,
        request: main_models.StopAppResourcesRequest,
    ) -> main_models.StopAppResourcesResponse:
        runtime = RuntimeOptions()
        return self.stop_app_resources_with_options(request, runtime)

    async def stop_app_resources_async(
        self,
        request: main_models.StopAppResourcesRequest,
    ) -> main_models.StopAppResourcesResponse:
        runtime = RuntimeOptions()
        return await self.stop_app_resources_with_options_async(request, runtime)

    def unbind_with_options(
        self,
        request: main_models.UnbindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Unbind',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindResponse(),
            self.do_rpcrequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    async def unbind_with_options_async(
        self,
        request: main_models.UnbindRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnbindResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_instance_group_id):
            body['AppInstanceGroupId'] = request.app_instance_group_id
        if not DaraCore.is_null(request.app_instance_id):
            body['AppInstanceId'] = request.app_instance_id
        if not DaraCore.is_null(request.app_instance_persistent_id):
            body['AppInstancePersistentId'] = request.app_instance_persistent_id
        if not DaraCore.is_null(request.client_id):
            body['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_os):
            body['ClientOS'] = request.client_os
        if not DaraCore.is_null(request.client_version):
            body['ClientVersion'] = request.client_version
        if not DaraCore.is_null(request.end_user_id):
            body['EndUserId'] = request.end_user_id
        if not DaraCore.is_null(request.login_region_id):
            body['LoginRegionId'] = request.login_region_id
        if not DaraCore.is_null(request.login_token):
            body['LoginToken'] = request.login_token
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Unbind',
            version = '2021-09-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnbindResponse(),
            await self.do_rpcrequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.body_type, req, runtime)
        )

    def unbind(
        self,
        request: main_models.UnbindRequest,
    ) -> main_models.UnbindResponse:
        runtime = RuntimeOptions()
        return self.unbind_with_options(request, runtime)

    async def unbind_async(
        self,
        request: main_models.UnbindRequest,
    ) -> main_models.UnbindResponse:
        runtime = RuntimeOptions()
        return await self.unbind_with_options_async(request, runtime)
