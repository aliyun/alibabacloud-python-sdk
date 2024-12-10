# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dataanalysisgbi20240823 import models as data_analysis_gbi20240823_models
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
        self._endpoint = self.get_endpoint('dataanalysisgbi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_datasource_authorization_with_options(
        self,
        request: data_analysis_gbi20240823_models.CancelDatasourceAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse:
        """
        @summary 取消关联的数据源授权
        
        @param request: CancelDatasourceAuthorizationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDatasourceAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDatasourceAuthorization',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/cancel/datasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_datasource_authorization_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.CancelDatasourceAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse:
        """
        @summary 取消关联的数据源授权
        
        @param request: CancelDatasourceAuthorizationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDatasourceAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDatasourceAuthorization',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/cancel/datasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_datasource_authorization(
        self,
        request: data_analysis_gbi20240823_models.CancelDatasourceAuthorizationRequest,
    ) -> data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse:
        """
        @summary 取消关联的数据源授权
        
        @param request: CancelDatasourceAuthorizationRequest
        @return: CancelDatasourceAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_datasource_authorization_with_options(request, headers, runtime)

    async def cancel_datasource_authorization_async(
        self,
        request: data_analysis_gbi20240823_models.CancelDatasourceAuthorizationRequest,
    ) -> data_analysis_gbi20240823_models.CancelDatasourceAuthorizationResponse:
        """
        @summary 取消关联的数据源授权
        
        @param request: CancelDatasourceAuthorizationRequest
        @return: CancelDatasourceAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_datasource_authorization_with_options_async(request, headers, runtime)

    def create_datasource_authorization_with_options(
        self,
        request: data_analysis_gbi20240823_models.CreateDatasourceAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse:
        """
        @summary 创建数据库关联授权
        
        @param request: CreateDatasourceAuthorizationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasourceAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        if not UtilClient.is_unset(request.user_name):
            body['userName'] = request.user_name
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasourceAuthorization',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/create/datasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_datasource_authorization_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.CreateDatasourceAuthorizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse:
        """
        @summary 创建数据库关联授权
        
        @param request: CreateDatasourceAuthorizationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasourceAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.url):
            body['url'] = request.url
        if not UtilClient.is_unset(request.user_name):
            body['userName'] = request.user_name
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasourceAuthorization',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/create/datasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_datasource_authorization(
        self,
        request: data_analysis_gbi20240823_models.CreateDatasourceAuthorizationRequest,
    ) -> data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse:
        """
        @summary 创建数据库关联授权
        
        @param request: CreateDatasourceAuthorizationRequest
        @return: CreateDatasourceAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_datasource_authorization_with_options(request, headers, runtime)

    async def create_datasource_authorization_async(
        self,
        request: data_analysis_gbi20240823_models.CreateDatasourceAuthorizationRequest,
    ) -> data_analysis_gbi20240823_models.CreateDatasourceAuthorizationResponse:
        """
        @summary 创建数据库关联授权
        
        @param request: CreateDatasourceAuthorizationRequest
        @return: CreateDatasourceAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_datasource_authorization_with_options_async(request, headers, runtime)

    def create_virtual_datasource_instance_with_options(
        self,
        request: data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse:
        """
        @summary 在指定的业务空间创建虚拟数据源
        
        @param request: CreateVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/createVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virtual_datasource_instance_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse:
        """
        @summary 在指定的业务空间创建虚拟数据源
        
        @param request: CreateVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/createVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_virtual_datasource_instance(
        self,
        request: data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse:
        """
        @summary 在指定的业务空间创建虚拟数据源
        
        @param request: CreateVirtualDatasourceInstanceRequest
        @return: CreateVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_virtual_datasource_instance_with_options(request, headers, runtime)

    async def create_virtual_datasource_instance_async(
        self,
        request: data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.CreateVirtualDatasourceInstanceResponse:
        """
        @summary 在指定的业务空间创建虚拟数据源
        
        @param request: CreateVirtualDatasourceInstanceRequest
        @return: CreateVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_virtual_datasource_instance_with_options_async(request, headers, runtime)

    def delete_virtual_datasource_instance_with_options(
        self,
        request: data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse:
        """
        @summary 删除指定业务空间下面的虚拟数据源实例
        
        @param request: DeleteVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/deleteVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_virtual_datasource_instance_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse:
        """
        @summary 删除指定业务空间下面的虚拟数据源实例
        
        @param request: DeleteVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/deleteVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_virtual_datasource_instance(
        self,
        request: data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse:
        """
        @summary 删除指定业务空间下面的虚拟数据源实例
        
        @param request: DeleteVirtualDatasourceInstanceRequest
        @return: DeleteVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_virtual_datasource_instance_with_options(request, headers, runtime)

    async def delete_virtual_datasource_instance_async(
        self,
        request: data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.DeleteVirtualDatasourceInstanceResponse:
        """
        @summary 删除指定业务空间下面的虚拟数据源实例
        
        @param request: DeleteVirtualDatasourceInstanceRequest
        @return: DeleteVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_virtual_datasource_instance_with_options_async(request, headers, runtime)

    def list_virtual_datasource_instance_with_options(
        self,
        request: data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse:
        """
        @summary 获取当前业务空间下的数据源实例列表
        
        @param request: ListVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/listVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_virtual_datasource_instance_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse:
        """
        @summary 获取当前业务空间下的数据源实例列表
        
        @param request: ListVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/listVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_virtual_datasource_instance(
        self,
        request: data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse:
        """
        @summary 获取当前业务空间下的数据源实例列表
        
        @param request: ListVirtualDatasourceInstanceRequest
        @return: ListVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_virtual_datasource_instance_with_options(request, headers, runtime)

    async def list_virtual_datasource_instance_async(
        self,
        request: data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.ListVirtualDatasourceInstanceResponse:
        """
        @summary 获取当前业务空间下的数据源实例列表
        
        @param request: ListVirtualDatasourceInstanceRequest
        @return: ListVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_virtual_datasource_instance_with_options_async(request, headers, runtime)

    def run_data_analysis_with_options(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDataAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.generate_sql_only):
            body['generateSqlOnly'] = request.generate_sql_only
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.specification_type):
            body['specificationType'] = request.specification_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDataAnalysis',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/gbi/runDataAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.RunDataAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_data_analysis_with_options_async(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunDataAnalysisResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.generate_sql_only):
            body['generateSqlOnly'] = request.generate_sql_only
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            body['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.specification_type):
            body['specificationType'] = request.specification_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunDataAnalysis',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/gbi/runDataAnalysis',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.RunDataAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_data_analysis(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @return: RunDataAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_data_analysis_with_options(workspace_id, request, headers, runtime)

    async def run_data_analysis_async(
        self,
        workspace_id: str,
        request: data_analysis_gbi20240823_models.RunDataAnalysisRequest,
    ) -> data_analysis_gbi20240823_models.RunDataAnalysisResponse:
        """
        @summary 运行数据分析
        
        @param request: RunDataAnalysisRequest
        @return: RunDataAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_data_analysis_with_options_async(workspace_id, request, headers, runtime)

    def save_virtual_datasource_ddl_with_options(
        self,
        request: data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse:
        """
        @summary 向当前指定的业务空间下的指定虚拟数据源实例添加ddl语句
        
        @param request: SaveVirtualDatasourceDdlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveVirtualDatasourceDdlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.ddl):
            body['ddl'] = request.ddl
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveVirtualDatasourceDdl',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/addDdl2VirtualInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_virtual_datasource_ddl_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse:
        """
        @summary 向当前指定的业务空间下的指定虚拟数据源实例添加ddl语句
        
        @param request: SaveVirtualDatasourceDdlRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveVirtualDatasourceDdlResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.ddl):
            body['ddl'] = request.ddl
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveVirtualDatasourceDdl',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/addDdl2VirtualInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_virtual_datasource_ddl(
        self,
        request: data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlRequest,
    ) -> data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse:
        """
        @summary 向当前指定的业务空间下的指定虚拟数据源实例添加ddl语句
        
        @param request: SaveVirtualDatasourceDdlRequest
        @return: SaveVirtualDatasourceDdlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.save_virtual_datasource_ddl_with_options(request, headers, runtime)

    async def save_virtual_datasource_ddl_async(
        self,
        request: data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlRequest,
    ) -> data_analysis_gbi20240823_models.SaveVirtualDatasourceDdlResponse:
        """
        @summary 向当前指定的业务空间下的指定虚拟数据源实例添加ddl语句
        
        @param request: SaveVirtualDatasourceDdlRequest
        @return: SaveVirtualDatasourceDdlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.save_virtual_datasource_ddl_with_options_async(request, headers, runtime)

    def sync_remote_tables_with_options(
        self,
        request: data_analysis_gbi20240823_models.SyncRemoteTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.SyncRemoteTablesResponse:
        """
        @summary 更新当前业务空间所关联的数据表
        
        @param request: SyncRemoteTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncRemoteTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.keep_table_names):
            body['keepTableNames'] = request.keep_table_names
        if not UtilClient.is_unset(request.pull_samples):
            body['pullSamples'] = request.pull_samples
        if not UtilClient.is_unset(request.table_names):
            body['tableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncRemoteTables',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/datasource/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.SyncRemoteTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_remote_tables_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.SyncRemoteTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.SyncRemoteTablesResponse:
        """
        @summary 更新当前业务空间所关联的数据表
        
        @param request: SyncRemoteTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncRemoteTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.keep_table_names):
            body['keepTableNames'] = request.keep_table_names
        if not UtilClient.is_unset(request.pull_samples):
            body['pullSamples'] = request.pull_samples
        if not UtilClient.is_unset(request.table_names):
            body['tableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncRemoteTables',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/update/datasource/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.SyncRemoteTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_remote_tables(
        self,
        request: data_analysis_gbi20240823_models.SyncRemoteTablesRequest,
    ) -> data_analysis_gbi20240823_models.SyncRemoteTablesResponse:
        """
        @summary 更新当前业务空间所关联的数据表
        
        @param request: SyncRemoteTablesRequest
        @return: SyncRemoteTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.sync_remote_tables_with_options(request, headers, runtime)

    async def sync_remote_tables_async(
        self,
        request: data_analysis_gbi20240823_models.SyncRemoteTablesRequest,
    ) -> data_analysis_gbi20240823_models.SyncRemoteTablesResponse:
        """
        @summary 更新当前业务空间所关联的数据表
        
        @param request: SyncRemoteTablesRequest
        @return: SyncRemoteTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.sync_remote_tables_with_options_async(request, headers, runtime)

    def update_virtual_datasource_instance_with_options(
        self,
        request: data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse:
        """
        @summary 修改指定业务空间下所指定的虚拟数据源的信息
        
        @param request: UpdateVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/updateVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_virtual_datasource_instance_with_options_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse:
        """
        @summary 修改指定业务空间下所指定的虚拟数据源的信息
        
        @param request: UpdateVirtualDatasourceInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateVirtualDatasourceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        if not UtilClient.is_unset(request.vdb_id):
            body['vdbId'] = request.vdb_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateVirtualDatasourceInstance',
            version='2024-08-23',
            protocol='HTTPS',
            pathname=f'/gbi/virtualDatasource/updateVirtualDatasourceInstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_virtual_datasource_instance(
        self,
        request: data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse:
        """
        @summary 修改指定业务空间下所指定的虚拟数据源的信息
        
        @param request: UpdateVirtualDatasourceInstanceRequest
        @return: UpdateVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_virtual_datasource_instance_with_options(request, headers, runtime)

    async def update_virtual_datasource_instance_async(
        self,
        request: data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceRequest,
    ) -> data_analysis_gbi20240823_models.UpdateVirtualDatasourceInstanceResponse:
        """
        @summary 修改指定业务空间下所指定的虚拟数据源的信息
        
        @param request: UpdateVirtualDatasourceInstanceRequest
        @return: UpdateVirtualDatasourceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_virtual_datasource_instance_with_options_async(request, headers, runtime)
