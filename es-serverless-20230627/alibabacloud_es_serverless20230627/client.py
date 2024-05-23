# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_es_serverless20230627 import models as es_serverless_20230627_models
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
        self._endpoint = self.get_endpoint('es-serverless', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_app_with_options(
        self,
        request: es_serverless_20230627_models.CreateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CreateAppResponse:
        """
        @summary 创建Serverless应用
        
        @param request: CreateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.authentication):
            body['authentication'] = request.authentication
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.network):
            body['network'] = request.network
        if not UtilClient.is_unset(request.private_network):
            body['privateNetwork'] = request.private_network
        if not UtilClient.is_unset(request.quota_info):
            body['quotaInfo'] = request.quota_info
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: es_serverless_20230627_models.CreateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CreateAppResponse:
        """
        @summary 创建Serverless应用
        
        @param request: CreateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['appName'] = request.app_name
        if not UtilClient.is_unset(request.authentication):
            body['authentication'] = request.authentication
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.network):
            body['network'] = request.network
        if not UtilClient.is_unset(request.private_network):
            body['privateNetwork'] = request.private_network
        if not UtilClient.is_unset(request.quota_info):
            body['quotaInfo'] = request.quota_info
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: es_serverless_20230627_models.CreateAppRequest,
    ) -> es_serverless_20230627_models.CreateAppResponse:
        """
        @summary 创建Serverless应用
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_app_with_options(request, headers, runtime)

    async def create_app_async(
        self,
        request: es_serverless_20230627_models.CreateAppRequest,
    ) -> es_serverless_20230627_models.CreateAppResponse:
        """
        @summary 创建Serverless应用
        
        @param request: CreateAppRequest
        @return: CreateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_app_with_options_async(request, headers, runtime)

    def create_endpoint_with_options(
        self,
        request: es_serverless_20230627_models.CreateEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CreateEndpointResponse:
        """
        @summary 创建端点
        
        @param request: CreateEndpointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.endpoint_zones):
            body['endpointZones'] = request.endpoint_zones
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/endpoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.CreateEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_endpoint_with_options_async(
        self,
        request: es_serverless_20230627_models.CreateEndpointRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.CreateEndpointResponse:
        """
        @summary 创建端点
        
        @param request: CreateEndpointRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.endpoint_zones):
            body['endpointZones'] = request.endpoint_zones
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/endpoints',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.CreateEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_endpoint(
        self,
        request: es_serverless_20230627_models.CreateEndpointRequest,
    ) -> es_serverless_20230627_models.CreateEndpointResponse:
        """
        @summary 创建端点
        
        @param request: CreateEndpointRequest
        @return: CreateEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_endpoint_with_options(request, headers, runtime)

    async def create_endpoint_async(
        self,
        request: es_serverless_20230627_models.CreateEndpointRequest,
    ) -> es_serverless_20230627_models.CreateEndpointResponse:
        """
        @summary 创建端点
        
        @param request: CreateEndpointRequest
        @return: CreateEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_endpoint_with_options_async(request, headers, runtime)

    def delete_app_with_options(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.DeleteAppResponse:
        """
        @summary 删除Serverless应用。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.DeleteAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_with_options_async(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.DeleteAppResponse:
        """
        @summary 删除Serverless应用。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.DeleteAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.DeleteAppResponse:
        """
        @summary 删除Serverless应用。
        
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_app_with_options(app_name, headers, runtime)

    async def delete_app_async(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.DeleteAppResponse:
        """
        @summary 删除Serverless应用。
        
        @return: DeleteAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_app_with_options_async(app_name, headers, runtime)

    def get_app_with_options(
        self,
        app_name: str,
        request: es_serverless_20230627_models.GetAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetAppResponse:
        """
        @summary 获取Serverless应用详情
        
        @param request: GetAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detailed):
            query['detailed'] = request.detailed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.GetAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_with_options_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.GetAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetAppResponse:
        """
        @summary 获取Serverless应用详情
        
        @param request: GetAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.detailed):
            query['detailed'] = request.detailed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.GetAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app(
        self,
        app_name: str,
        request: es_serverless_20230627_models.GetAppRequest,
    ) -> es_serverless_20230627_models.GetAppResponse:
        """
        @summary 获取Serverless应用详情
        
        @param request: GetAppRequest
        @return: GetAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_app_with_options(app_name, request, headers, runtime)

    async def get_app_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.GetAppRequest,
    ) -> es_serverless_20230627_models.GetAppResponse:
        """
        @summary 获取Serverless应用详情
        
        @param request: GetAppRequest
        @return: GetAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_app_with_options_async(app_name, request, headers, runtime)

    def get_app_quota_with_options(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetAppQuotaResponse:
        """
        @summary 获取Serverless应用配额详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppQuotaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppQuota',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.GetAppQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_quota_with_options_async(
        self,
        app_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetAppQuotaResponse:
        """
        @summary 获取Serverless应用配额详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAppQuotaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetAppQuota',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}/quota',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.GetAppQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_quota(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.GetAppQuotaResponse:
        """
        @summary 获取Serverless应用配额详情
        
        @return: GetAppQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_app_quota_with_options(app_name, headers, runtime)

    async def get_app_quota_async(
        self,
        app_name: str,
    ) -> es_serverless_20230627_models.GetAppQuotaResponse:
        """
        @summary 获取Serverless应用配额详情
        
        @return: GetAppQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_app_quota_with_options_async(app_name, headers, runtime)

    def get_monitor_data_with_options(
        self,
        request: es_serverless_20230627_models.GetMonitorDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetMonitorDataResponse:
        """
        @summary 获取监控数据
        
        @param request: GetMonitorDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMonitorDataResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetMonitorData',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/emon/metrics/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.GetMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_monitor_data_with_options_async(
        self,
        request: es_serverless_20230627_models.GetMonitorDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.GetMonitorDataResponse:
        """
        @summary 获取监控数据
        
        @param request: GetMonitorDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMonitorDataResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='GetMonitorData',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/emon/metrics/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.GetMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_monitor_data(
        self,
        request: es_serverless_20230627_models.GetMonitorDataRequest,
    ) -> es_serverless_20230627_models.GetMonitorDataResponse:
        """
        @summary 获取监控数据
        
        @param request: GetMonitorDataRequest
        @return: GetMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_monitor_data_with_options(request, headers, runtime)

    async def get_monitor_data_async(
        self,
        request: es_serverless_20230627_models.GetMonitorDataRequest,
    ) -> es_serverless_20230627_models.GetMonitorDataResponse:
        """
        @summary 获取监控数据
        
        @param request: GetMonitorDataRequest
        @return: GetMonitorDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_monitor_data_with_options_async(request, headers, runtime)

    def list_apps_with_options(
        self,
        request: es_serverless_20230627_models.ListAppsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListAppsResponse:
        """
        @summary 查看Serverless应用列表
        
        @param request: ListAppsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['appName'] = request.app_name
        if not UtilClient.is_unset(request.create_time):
            query['createTime'] = request.create_time
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.order_type):
            query['orderType'] = request.order_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.ListAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apps_with_options_async(
        self,
        request: es_serverless_20230627_models.ListAppsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.ListAppsResponse:
        """
        @summary 查看Serverless应用列表
        
        @param request: ListAppsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['appName'] = request.app_name
        if not UtilClient.is_unset(request.create_time):
            query['createTime'] = request.create_time
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.order_type):
            query['orderType'] = request.order_type
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApps',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.ListAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_apps(
        self,
        request: es_serverless_20230627_models.ListAppsRequest,
    ) -> es_serverless_20230627_models.ListAppsResponse:
        """
        @summary 查看Serverless应用列表
        
        @param request: ListAppsRequest
        @return: ListAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_apps_with_options(request, headers, runtime)

    async def list_apps_async(
        self,
        request: es_serverless_20230627_models.ListAppsRequest,
    ) -> es_serverless_20230627_models.ListAppsResponse:
        """
        @summary 查看Serverless应用列表
        
        @param request: ListAppsRequest
        @return: ListAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_apps_with_options_async(request, headers, runtime)

    def update_app_with_options(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.UpdateAppResponse:
        """
        @summary 编辑Serverless应用
        
        @param request: UpdateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_reason):
            body['applyReason'] = request.apply_reason
        if not UtilClient.is_unset(request.authentication):
            body['authentication'] = request.authentication
        if not UtilClient.is_unset(request.contact_info):
            body['contactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.limiter_info):
            body['limiterInfo'] = request.limiter_info
        if not UtilClient.is_unset(request.network):
            body['network'] = request.network
        if not UtilClient.is_unset(request.private_network):
            body['privateNetwork'] = request.private_network
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_with_options_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateAppRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> es_serverless_20230627_models.UpdateAppResponse:
        """
        @summary 编辑Serverless应用
        
        @param request: UpdateAppRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apply_reason):
            body['applyReason'] = request.apply_reason
        if not UtilClient.is_unset(request.authentication):
            body['authentication'] = request.authentication
        if not UtilClient.is_unset(request.contact_info):
            body['contactInfo'] = request.contact_info
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.limiter_info):
            body['limiterInfo'] = request.limiter_info
        if not UtilClient.is_unset(request.network):
            body['network'] = request.network
        if not UtilClient.is_unset(request.private_network):
            body['privateNetwork'] = request.private_network
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2023-06-27',
            protocol='HTTPS',
            pathname=f'/openapi/es-serverless/instances/{OpenApiUtilClient.get_encode_param(app_name)}',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            es_serverless_20230627_models.UpdateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateAppRequest,
    ) -> es_serverless_20230627_models.UpdateAppResponse:
        """
        @summary 编辑Serverless应用
        
        @param request: UpdateAppRequest
        @return: UpdateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_app_with_options(app_name, request, headers, runtime)

    async def update_app_async(
        self,
        app_name: str,
        request: es_serverless_20230627_models.UpdateAppRequest,
    ) -> es_serverless_20230627_models.UpdateAppResponse:
        """
        @summary 编辑Serverless应用
        
        @param request: UpdateAppRequest
        @return: UpdateAppResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_app_with_options_async(app_name, request, headers, runtime)
