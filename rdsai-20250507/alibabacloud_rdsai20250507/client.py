# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rdsai20250507 import models as rds_ai_20250507_models
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
        self._endpoint = self.get_endpoint('rdsai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_app_instance_with_options(
        self,
        tmp_req: rds_ai_20250507_models.CreateAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.CreateAppInstanceResponse:
        """
        @summary 创建应用服务实例
        
        @param tmp_req: CreateAppInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.CreateAppInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbinstance_config):
            request.dbinstance_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_config, 'DBInstanceConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_config_shrink):
            query['DBInstanceConfig'] = request.dbinstance_config_shrink
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not UtilClient.is_unset(request.dashboard_username):
            query['DashboardUsername'] = request.dashboard_username
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.public_endpoint_enabled):
            query['PublicEndpointEnabled'] = request.public_endpoint_enabled
        if not UtilClient.is_unset(request.public_network_access_enabled):
            query['PublicNetworkAccessEnabled'] = request.public_network_access_enabled
        if not UtilClient.is_unset(request.ragenabled):
            query['RAGEnabled'] = request.ragenabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.CreateAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_instance_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.CreateAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.CreateAppInstanceResponse:
        """
        @summary 创建应用服务实例
        
        @param tmp_req: CreateAppInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAppInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.CreateAppInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dbinstance_config):
            request.dbinstance_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dbinstance_config, 'DBInstanceConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_config_shrink):
            query['DBInstanceConfig'] = request.dbinstance_config_shrink
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not UtilClient.is_unset(request.dashboard_username):
            query['DashboardUsername'] = request.dashboard_username
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.public_endpoint_enabled):
            query['PublicEndpointEnabled'] = request.public_endpoint_enabled
        if not UtilClient.is_unset(request.public_network_access_enabled):
            query['PublicNetworkAccessEnabled'] = request.public_network_access_enabled
        if not UtilClient.is_unset(request.ragenabled):
            query['RAGEnabled'] = request.ragenabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.CreateAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_instance(
        self,
        request: rds_ai_20250507_models.CreateAppInstanceRequest,
    ) -> rds_ai_20250507_models.CreateAppInstanceResponse:
        """
        @summary 创建应用服务实例
        
        @param request: CreateAppInstanceRequest
        @return: CreateAppInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_app_instance_with_options(request, runtime)

    async def create_app_instance_async(
        self,
        request: rds_ai_20250507_models.CreateAppInstanceRequest,
    ) -> rds_ai_20250507_models.CreateAppInstanceResponse:
        """
        @summary 创建应用服务实例
        
        @param request: CreateAppInstanceRequest
        @return: CreateAppInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_app_instance_with_options_async(request, runtime)

    def delete_app_instance_with_options(
        self,
        request: rds_ai_20250507_models.DeleteAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DeleteAppInstanceResponse:
        """
        @summary 删除应用服务实例
        
        @param request: DeleteAppInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DeleteAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_instance_with_options_async(
        self,
        request: rds_ai_20250507_models.DeleteAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DeleteAppInstanceResponse:
        """
        @summary 删除应用服务实例
        
        @param request: DeleteAppInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAppInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DeleteAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_instance(
        self,
        request: rds_ai_20250507_models.DeleteAppInstanceRequest,
    ) -> rds_ai_20250507_models.DeleteAppInstanceResponse:
        """
        @summary 删除应用服务实例
        
        @param request: DeleteAppInstanceRequest
        @return: DeleteAppInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_app_instance_with_options(request, runtime)

    async def delete_app_instance_async(
        self,
        request: rds_ai_20250507_models.DeleteAppInstanceRequest,
    ) -> rds_ai_20250507_models.DeleteAppInstanceResponse:
        """
        @summary 删除应用服务实例
        
        @param request: DeleteAppInstanceRequest
        @return: DeleteAppInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_instance_with_options_async(request, runtime)

    def describe_app_instance_attribute_with_options(
        self,
        request: rds_ai_20250507_models.DescribeAppInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeAppInstanceAttributeResponse:
        """
        @summary 查询应用服务详情
        
        @param request: DescribeAppInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInstanceAttribute',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeAppInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_instance_attribute_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeAppInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeAppInstanceAttributeResponse:
        """
        @summary 查询应用服务详情
        
        @param request: DescribeAppInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInstanceAttribute',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeAppInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_instance_attribute(
        self,
        request: rds_ai_20250507_models.DescribeAppInstanceAttributeRequest,
    ) -> rds_ai_20250507_models.DescribeAppInstanceAttributeResponse:
        """
        @summary 查询应用服务详情
        
        @param request: DescribeAppInstanceAttributeRequest
        @return: DescribeAppInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_instance_attribute_with_options(request, runtime)

    async def describe_app_instance_attribute_async(
        self,
        request: rds_ai_20250507_models.DescribeAppInstanceAttributeRequest,
    ) -> rds_ai_20250507_models.DescribeAppInstanceAttributeResponse:
        """
        @summary 查询应用服务详情
        
        @param request: DescribeAppInstanceAttributeRequest
        @return: DescribeAppInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_instance_attribute_with_options_async(request, runtime)

    def describe_app_instances_with_options(
        self,
        request: rds_ai_20250507_models.DescribeAppInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeAppInstancesResponse:
        """
        @summary 查询应用服务列表
        
        @param request: DescribeAppInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInstances',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeAppInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_instances_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeAppInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeAppInstancesResponse:
        """
        @summary 查询应用服务列表
        
        @param request: DescribeAppInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAppInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppInstances',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeAppInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_instances(
        self,
        request: rds_ai_20250507_models.DescribeAppInstancesRequest,
    ) -> rds_ai_20250507_models.DescribeAppInstancesResponse:
        """
        @summary 查询应用服务列表
        
        @param request: DescribeAppInstancesRequest
        @return: DescribeAppInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_app_instances_with_options(request, runtime)

    async def describe_app_instances_async(
        self,
        request: rds_ai_20250507_models.DescribeAppInstancesRequest,
    ) -> rds_ai_20250507_models.DescribeAppInstancesResponse:
        """
        @summary 查询应用服务列表
        
        @param request: DescribeAppInstancesRequest
        @return: DescribeAppInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_instances_with_options_async(request, runtime)

    def describe_instance_auth_info_with_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceAuthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceAuthInfoResponse:
        """
        @summary 查看实例认证信息
        
        @param request: DescribeInstanceAuthInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAuthInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAuthInfo',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceAuthInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_auth_info_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceAuthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceAuthInfoResponse:
        """
        @summary 查看实例认证信息
        
        @param request: DescribeInstanceAuthInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAuthInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAuthInfo',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceAuthInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_auth_info(
        self,
        request: rds_ai_20250507_models.DescribeInstanceAuthInfoRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceAuthInfoResponse:
        """
        @summary 查看实例认证信息
        
        @param request: DescribeInstanceAuthInfoRequest
        @return: DescribeInstanceAuthInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auth_info_with_options(request, runtime)

    async def describe_instance_auth_info_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceAuthInfoRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceAuthInfoResponse:
        """
        @summary 查看实例认证信息
        
        @param request: DescribeInstanceAuthInfoRequest
        @return: DescribeInstanceAuthInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auth_info_with_options_async(request, runtime)

    def describe_instance_endpoints_with_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceEndpointsResponse:
        """
        @summary 查看服务连接信息
        
        @param request: DescribeInstanceEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceEndpoints',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_endpoints_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceEndpointsResponse:
        """
        @summary 查看服务连接信息
        
        @param request: DescribeInstanceEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceEndpoints',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_endpoints(
        self,
        request: rds_ai_20250507_models.DescribeInstanceEndpointsRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceEndpointsResponse:
        """
        @summary 查看服务连接信息
        
        @param request: DescribeInstanceEndpointsRequest
        @return: DescribeInstanceEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_endpoints_with_options(request, runtime)

    async def describe_instance_endpoints_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceEndpointsRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceEndpointsResponse:
        """
        @summary 查看服务连接信息
        
        @param request: DescribeInstanceEndpointsRequest
        @return: DescribeInstanceEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_endpoints_with_options_async(request, runtime)

    def describe_instance_ip_whitelist_with_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse:
        """
        @summary 查询服务白名单
        
        @param request: DescribeInstanceIpWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIpWhitelist',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ip_whitelist_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse:
        """
        @summary 查询服务白名单
        
        @param request: DescribeInstanceIpWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceIpWhitelist',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ip_whitelist(
        self,
        request: rds_ai_20250507_models.DescribeInstanceIpWhitelistRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse:
        """
        @summary 查询服务白名单
        
        @param request: DescribeInstanceIpWhitelistRequest
        @return: DescribeInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ip_whitelist_with_options(request, runtime)

    async def describe_instance_ip_whitelist_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceIpWhitelistRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceIpWhitelistResponse:
        """
        @summary 查询服务白名单
        
        @param request: DescribeInstanceIpWhitelistRequest
        @return: DescribeInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_ip_whitelist_with_options_async(request, runtime)

    def describe_instance_ragconfig_with_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceRAGConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceRAGConfigResponse:
        """
        @summary 查看实例RAG配置
        
        @param request: DescribeInstanceRAGConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceRAGConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRAGConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceRAGConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_ragconfig_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceRAGConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceRAGConfigResponse:
        """
        @summary 查看实例RAG配置
        
        @param request: DescribeInstanceRAGConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceRAGConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceRAGConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceRAGConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ragconfig(
        self,
        request: rds_ai_20250507_models.DescribeInstanceRAGConfigRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceRAGConfigResponse:
        """
        @summary 查看实例RAG配置
        
        @param request: DescribeInstanceRAGConfigRequest
        @return: DescribeInstanceRAGConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ragconfig_with_options(request, runtime)

    async def describe_instance_ragconfig_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceRAGConfigRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceRAGConfigResponse:
        """
        @summary 查看实例RAG配置
        
        @param request: DescribeInstanceRAGConfigRequest
        @return: DescribeInstanceRAGConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_ragconfig_with_options_async(request, runtime)

    def describe_instance_sslwith_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceSSLResponse:
        """
        @summary 查看实例SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSSL',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_sslwith_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceSSLResponse:
        """
        @summary 查看实例SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSSL',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_ssl(
        self,
        request: rds_ai_20250507_models.DescribeInstanceSSLRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceSSLResponse:
        """
        @summary 查看实例SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @return: DescribeInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_sslwith_options(request, runtime)

    async def describe_instance_ssl_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceSSLRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceSSLResponse:
        """
        @summary 查看实例SSL配置
        
        @param request: DescribeInstanceSSLRequest
        @return: DescribeInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_sslwith_options_async(request, runtime)

    def describe_instance_storage_config_with_options(
        self,
        request: rds_ai_20250507_models.DescribeInstanceStorageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceStorageConfigResponse:
        """
        @summary 查看实例存储配置
        
        @param request: DescribeInstanceStorageConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStorageConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStorageConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceStorageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_storage_config_with_options_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceStorageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.DescribeInstanceStorageConfigResponse:
        """
        @summary 查看实例存储配置
        
        @param request: DescribeInstanceStorageConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceStorageConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceStorageConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.DescribeInstanceStorageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_storage_config(
        self,
        request: rds_ai_20250507_models.DescribeInstanceStorageConfigRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceStorageConfigResponse:
        """
        @summary 查看实例存储配置
        
        @param request: DescribeInstanceStorageConfigRequest
        @return: DescribeInstanceStorageConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_storage_config_with_options(request, runtime)

    async def describe_instance_storage_config_async(
        self,
        request: rds_ai_20250507_models.DescribeInstanceStorageConfigRequest,
    ) -> rds_ai_20250507_models.DescribeInstanceStorageConfigResponse:
        """
        @summary 查看实例存储配置
        
        @param request: DescribeInstanceStorageConfigRequest
        @return: DescribeInstanceStorageConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_storage_config_with_options_async(request, runtime)

    def modify_instance_auth_config_with_options(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceAuthConfigResponse:
        """
        @summary 修改Supabase Auth相关配置
        
        @param tmp_req: ModifyInstanceAuthConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAuthConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceAuthConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAuthConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceAuthConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_auth_config_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceAuthConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceAuthConfigResponse:
        """
        @summary 修改Supabase Auth相关配置
        
        @param tmp_req: ModifyInstanceAuthConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAuthConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceAuthConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAuthConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceAuthConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_auth_config(
        self,
        request: rds_ai_20250507_models.ModifyInstanceAuthConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceAuthConfigResponse:
        """
        @summary 修改Supabase Auth相关配置
        
        @param request: ModifyInstanceAuthConfigRequest
        @return: ModifyInstanceAuthConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auth_config_with_options(request, runtime)

    async def modify_instance_auth_config_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceAuthConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceAuthConfigResponse:
        """
        @summary 修改Supabase Auth相关配置
        
        @param request: ModifyInstanceAuthConfigRequest
        @return: ModifyInstanceAuthConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auth_config_with_options_async(request, runtime)

    def modify_instance_config_with_options(
        self,
        request: rds_ai_20250507_models.ModifyInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_config_with_options_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_config(
        self,
        request: rds_ai_20250507_models.ModifyInstanceConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceConfigRequest
        @return: ModifyInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_config_with_options(request, runtime)

    async def modify_instance_config_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceConfigRequest
        @return: ModifyInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_config_with_options_async(request, runtime)

    def modify_instance_ip_whitelist_with_options(
        self,
        request: rds_ai_20250507_models.ModifyInstanceIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse:
        """
        @summary 修改服务白名单
        
        @param request: ModifyInstanceIpWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceIpWhitelist',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_ip_whitelist_with_options_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceIpWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse:
        """
        @summary 修改服务白名单
        
        @param request: ModifyInstanceIpWhitelistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceIpWhitelistResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.ip_whitelist):
            query['IpWhitelist'] = request.ip_whitelist
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceIpWhitelist',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ip_whitelist(
        self,
        request: rds_ai_20250507_models.ModifyInstanceIpWhitelistRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse:
        """
        @summary 修改服务白名单
        
        @param request: ModifyInstanceIpWhitelistRequest
        @return: ModifyInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_ip_whitelist_with_options(request, runtime)

    async def modify_instance_ip_whitelist_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceIpWhitelistRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceIpWhitelistResponse:
        """
        @summary 修改服务白名单
        
        @param request: ModifyInstanceIpWhitelistRequest
        @return: ModifyInstanceIpWhitelistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_ip_whitelist_with_options_async(request, runtime)

    def modify_instance_ragconfig_with_options(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceRAGConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceRAGConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param tmp_req: ModifyInstanceRAGConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceRAGConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceRAGConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRAGConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceRAGConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_ragconfig_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceRAGConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceRAGConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param tmp_req: ModifyInstanceRAGConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceRAGConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceRAGConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceRAGConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceRAGConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ragconfig(
        self,
        request: rds_ai_20250507_models.ModifyInstanceRAGConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceRAGConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceRAGConfigRequest
        @return: ModifyInstanceRAGConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_ragconfig_with_options(request, runtime)

    async def modify_instance_ragconfig_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceRAGConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceRAGConfigResponse:
        """
        @summary 修改实例RAG配置
        
        @param request: ModifyInstanceRAGConfigRequest
        @return: ModifyInstanceRAGConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_ragconfig_with_options_async(request, runtime)

    def modify_instance_sslwith_options(
        self,
        request: rds_ai_20250507_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceSSLResponse:
        """
        @summary 修改实例SSL配置
        
        @param request: ModifyInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catype):
            query['CAType'] = request.catype
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not UtilClient.is_unset(request.server_cert):
            query['ServerCert'] = request.server_cert
        if not UtilClient.is_unset(request.server_key):
            query['ServerKey'] = request.server_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSSL',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_sslwith_options_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceSSLResponse:
        """
        @summary 修改实例SSL配置
        
        @param request: ModifyInstanceSSLRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceSSLResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catype):
            query['CAType'] = request.catype
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sslenabled):
            query['SSLEnabled'] = request.sslenabled
        if not UtilClient.is_unset(request.server_cert):
            query['ServerCert'] = request.server_cert
        if not UtilClient.is_unset(request.server_key):
            query['ServerKey'] = request.server_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceSSL',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_ssl(
        self,
        request: rds_ai_20250507_models.ModifyInstanceSSLRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceSSLResponse:
        """
        @summary 修改实例SSL配置
        
        @param request: ModifyInstanceSSLRequest
        @return: ModifyInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_sslwith_options(request, runtime)

    async def modify_instance_ssl_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceSSLRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceSSLResponse:
        """
        @summary 修改实例SSL配置
        
        @param request: ModifyInstanceSSLRequest
        @return: ModifyInstanceSSLResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_sslwith_options_async(request, runtime)

    def modify_instance_storage_config_with_options(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceStorageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceStorageConfigResponse:
        """
        @summary 修改实例存储配置
        
        @param tmp_req: ModifyInstanceStorageConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceStorageConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceStorageConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceStorageConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceStorageConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_storage_config_with_options_async(
        self,
        tmp_req: rds_ai_20250507_models.ModifyInstanceStorageConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ModifyInstanceStorageConfigResponse:
        """
        @summary 修改实例存储配置
        
        @param tmp_req: ModifyInstanceStorageConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceStorageConfigResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rds_ai_20250507_models.ModifyInstanceStorageConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config_list):
            request.config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config_list, 'ConfigList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.config_list_shrink):
            query['ConfigList'] = request.config_list_shrink
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceStorageConfig',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ModifyInstanceStorageConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_storage_config(
        self,
        request: rds_ai_20250507_models.ModifyInstanceStorageConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceStorageConfigResponse:
        """
        @summary 修改实例存储配置
        
        @param request: ModifyInstanceStorageConfigRequest
        @return: ModifyInstanceStorageConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_storage_config_with_options(request, runtime)

    async def modify_instance_storage_config_async(
        self,
        request: rds_ai_20250507_models.ModifyInstanceStorageConfigRequest,
    ) -> rds_ai_20250507_models.ModifyInstanceStorageConfigResponse:
        """
        @summary 修改实例存储配置
        
        @param request: ModifyInstanceStorageConfigRequest
        @return: ModifyInstanceStorageConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_storage_config_with_options_async(request, runtime)

    def reset_instance_password_with_options(
        self,
        request: rds_ai_20250507_models.ResetInstancePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ResetInstancePasswordResponse:
        """
        @summary 重置实例密码
        
        @param request: ResetInstancePasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetInstancePasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetInstancePassword',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ResetInstancePasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_instance_password_with_options_async(
        self,
        request: rds_ai_20250507_models.ResetInstancePasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.ResetInstancePasswordResponse:
        """
        @summary 重置实例密码
        
        @param request: ResetInstancePasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetInstancePasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dashboard_password):
            query['DashboardPassword'] = request.dashboard_password
        if not UtilClient.is_unset(request.database_password):
            query['DatabasePassword'] = request.database_password
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetInstancePassword',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.ResetInstancePasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_instance_password(
        self,
        request: rds_ai_20250507_models.ResetInstancePasswordRequest,
    ) -> rds_ai_20250507_models.ResetInstancePasswordResponse:
        """
        @summary 重置实例密码
        
        @param request: ResetInstancePasswordRequest
        @return: ResetInstancePasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_instance_password_with_options(request, runtime)

    async def reset_instance_password_async(
        self,
        request: rds_ai_20250507_models.ResetInstancePasswordRequest,
    ) -> rds_ai_20250507_models.ResetInstancePasswordResponse:
        """
        @summary 重置实例密码
        
        @param request: ResetInstancePasswordRequest
        @return: ResetInstancePasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_instance_password_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: rds_ai_20250507_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: rds_ai_20250507_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: rds_ai_20250507_models.RestartInstanceRequest,
    ) -> rds_ai_20250507_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartInstanceRequest
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: rds_ai_20250507_models.RestartInstanceRequest,
    ) -> rds_ai_20250507_models.RestartInstanceResponse:
        """
        @summary 重启实例
        
        @param request: RestartInstanceRequest
        @return: RestartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: rds_ai_20250507_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: rds_ai_20250507_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.StartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_instance(
        self,
        request: rds_ai_20250507_models.StartInstanceRequest,
    ) -> rds_ai_20250507_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: rds_ai_20250507_models.StartInstanceRequest,
    ) -> rds_ai_20250507_models.StartInstanceResponse:
        """
        @summary 启动实例
        
        @param request: StartInstanceRequest
        @return: StartInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: rds_ai_20250507_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: rds_ai_20250507_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_ai_20250507_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopInstance',
            version='2025-05-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rds_ai_20250507_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        request: rds_ai_20250507_models.StopInstanceRequest,
    ) -> rds_ai_20250507_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: rds_ai_20250507_models.StopInstanceRequest,
    ) -> rds_ai_20250507_models.StopInstanceResponse:
        """
        @summary 暂停实例
        
        @param request: StopInstanceRequest
        @return: StopInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)
