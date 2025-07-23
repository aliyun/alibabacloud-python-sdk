# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_cms20240330 import models as cms_20240330_models
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
        self._endpoint = self.get_endpoint('cms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateEntityStoreResponse:
        """
        @summary 创建EntityStore相关存储
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateEntityStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_entity_store_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateEntityStoreResponse:
        """
        @summary 创建EntityStore相关存储
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateEntityStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_entity_store(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.CreateEntityStoreResponse:
        """
        @summary 创建EntityStore相关存储
        
        @return: CreateEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_entity_store_with_options(workspace_name, headers, runtime)

    async def create_entity_store_async(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.CreateEntityStoreResponse:
        """
        @summary 创建EntityStore相关存储
        
        @return: CreateEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_entity_store_with_options_async(workspace_name, headers, runtime)

    def create_prometheus_instance_with_options(
        self,
        request: cms_20240330_models.CreatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreatePrometheusInstanceResponse:
        """
        @summary 创建Prometheus监控实例
        
        @param request: CreatePrometheusInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrometheusInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.archive_duration):
            body['archiveDuration'] = request.archive_duration
        if not UtilClient.is_unset(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not UtilClient.is_unset(request.auth_free_write_policy):
            body['authFreeWritePolicy'] = request.auth_free_write_policy
        if not UtilClient.is_unset(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not UtilClient.is_unset(request.enable_auth_free_write):
            body['enableAuthFreeWrite'] = request.enable_auth_free_write
        if not UtilClient.is_unset(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.prometheus_instance_name):
            body['prometheusInstanceName'] = request.prometheus_instance_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.storage_duration):
            body['storageDuration'] = request.storage_duration
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreatePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_instance_with_options_async(
        self,
        request: cms_20240330_models.CreatePrometheusInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreatePrometheusInstanceResponse:
        """
        @summary 创建Prometheus监控实例
        
        @param request: CreatePrometheusInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePrometheusInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.archive_duration):
            body['archiveDuration'] = request.archive_duration
        if not UtilClient.is_unset(request.auth_free_read_policy):
            body['authFreeReadPolicy'] = request.auth_free_read_policy
        if not UtilClient.is_unset(request.auth_free_write_policy):
            body['authFreeWritePolicy'] = request.auth_free_write_policy
        if not UtilClient.is_unset(request.enable_auth_free_read):
            body['enableAuthFreeRead'] = request.enable_auth_free_read
        if not UtilClient.is_unset(request.enable_auth_free_write):
            body['enableAuthFreeWrite'] = request.enable_auth_free_write
        if not UtilClient.is_unset(request.enable_auth_token):
            body['enableAuthToken'] = request.enable_auth_token
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.prometheus_instance_name):
            body['prometheusInstanceName'] = request.prometheus_instance_name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.storage_duration):
            body['storageDuration'] = request.storage_duration
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.workspace):
            body['workspace'] = request.workspace
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusInstance',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/prometheus-instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreatePrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_instance(
        self,
        request: cms_20240330_models.CreatePrometheusInstanceRequest,
    ) -> cms_20240330_models.CreatePrometheusInstanceResponse:
        """
        @summary 创建Prometheus监控实例
        
        @param request: CreatePrometheusInstanceRequest
        @return: CreatePrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_prometheus_instance_with_options(request, headers, runtime)

    async def create_prometheus_instance_async(
        self,
        request: cms_20240330_models.CreatePrometheusInstanceRequest,
    ) -> cms_20240330_models.CreatePrometheusInstanceResponse:
        """
        @summary 创建Prometheus监控实例
        
        @param request: CreatePrometheusInstanceRequest
        @return: CreatePrometheusInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_prometheus_instance_with_options_async(request, headers, runtime)

    def create_umodel_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.CreateUmodelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateUmodelResponse:
        """
        @summary 创建Umodel配置
        
        @param request: CreateUmodelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUmodelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.common_schema_ref):
            body['commonSchemaRef'] = request.common_schema_ref
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_umodel_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.CreateUmodelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.CreateUmodelResponse:
        """
        @summary 创建Umodel配置
        
        @param request: CreateUmodelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUmodelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.common_schema_ref):
            body['commonSchemaRef'] = request.common_schema_ref
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.CreateUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_umodel(
        self,
        workspace: str,
        request: cms_20240330_models.CreateUmodelRequest,
    ) -> cms_20240330_models.CreateUmodelResponse:
        """
        @summary 创建Umodel配置
        
        @param request: CreateUmodelRequest
        @return: CreateUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_umodel_with_options(workspace, request, headers, runtime)

    async def create_umodel_async(
        self,
        workspace: str,
        request: cms_20240330_models.CreateUmodelRequest,
    ) -> cms_20240330_models.CreateUmodelResponse:
        """
        @summary 创建Umodel配置
        
        @param request: CreateUmodelRequest
        @return: CreateUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_umodel_with_options_async(workspace, request, headers, runtime)

    def delete_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteEntityStoreResponse:
        """
        @summary 删除EntityStore相关存储
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteEntityStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_entity_store_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteEntityStoreResponse:
        """
        @summary 删除EntityStore相关存储
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteEntityStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_entity_store(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.DeleteEntityStoreResponse:
        """
        @summary 删除EntityStore相关存储
        
        @return: DeleteEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_entity_store_with_options(workspace_name, headers, runtime)

    async def delete_entity_store_async(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.DeleteEntityStoreResponse:
        """
        @summary 删除EntityStore相关存储
        
        @return: DeleteEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_entity_store_with_options_async(workspace_name, headers, runtime)

    def delete_umodel_with_options(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelResponse:
        """
        @summary 删除Umodel配置信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUmodelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_umodel_with_options_async(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelResponse:
        """
        @summary 删除Umodel配置信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUmodelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_umodel(
        self,
        workspace: str,
    ) -> cms_20240330_models.DeleteUmodelResponse:
        """
        @summary 删除Umodel配置信息
        
        @return: DeleteUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_umodel_with_options(workspace, headers, runtime)

    async def delete_umodel_async(
        self,
        workspace: str,
    ) -> cms_20240330_models.DeleteUmodelResponse:
        """
        @summary 删除Umodel配置信息
        
        @return: DeleteUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_umodel_with_options_async(workspace, headers, runtime)

    def delete_umodel_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelDataResponse:
        """
        @summary 删除 Umodel Elements
        
        @param request: DeleteUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        if not UtilClient.is_unset(request.kind):
            query['kind'] = request.kind
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/data',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteUmodelDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_umodel_data_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteUmodelDataResponse:
        """
        @summary 删除 Umodel Elements
        
        @param request: DeleteUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        if not UtilClient.is_unset(request.kind):
            query['kind'] = request.kind
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/data',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteUmodelDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_umodel_data(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelDataRequest,
    ) -> cms_20240330_models.DeleteUmodelDataResponse:
        """
        @summary 删除 Umodel Elements
        
        @param request: DeleteUmodelDataRequest
        @return: DeleteUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_umodel_data_with_options(workspace, request, headers, runtime)

    async def delete_umodel_data_async(
        self,
        workspace: str,
        request: cms_20240330_models.DeleteUmodelDataRequest,
    ) -> cms_20240330_models.DeleteUmodelDataResponse:
        """
        @summary 删除 Umodel Elements
        
        @param request: DeleteUmodelDataRequest
        @return: DeleteUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_umodel_data_with_options_async(workspace, request, headers, runtime)

    def delete_workspace_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteWorkspaceResponse:
        """
        @summary 删除工作空间
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkspaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.DeleteWorkspaceResponse:
        """
        @summary 删除工作空间
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkspaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.DeleteWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.DeleteWorkspaceResponse:
        """
        @summary 删除工作空间
        
        @return: DeleteWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workspace_with_options(workspace_name, headers, runtime)

    async def delete_workspace_async(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.DeleteWorkspaceResponse:
        """
        @summary 删除工作空间
        
        @return: DeleteWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workspace_with_options_async(workspace_name, headers, runtime)

    def get_entity_store_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetEntityStoreResponse:
        """
        @summary 获取EntityStore相关存储信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetEntityStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_entity_store_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetEntityStoreResponse:
        """
        @summary 获取EntityStore相关存储信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEntityStoreResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetEntityStore',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}/entitystore',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetEntityStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_entity_store(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.GetEntityStoreResponse:
        """
        @summary 获取EntityStore相关存储信息
        
        @return: GetEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_entity_store_with_options(workspace_name, headers, runtime)

    async def get_entity_store_async(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.GetEntityStoreResponse:
        """
        @summary 获取EntityStore相关存储信息
        
        @return: GetEntityStoreResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_entity_store_with_options_async(workspace_name, headers, runtime)

    def get_entity_store_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.GetEntityStoreDataRequest,
        headers: cms_20240330_models.GetEntityStoreDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetEntityStoreDataResponse:
        """
        @summary 查询指定Workspace下的实体和关系数据，返回结果显示某时间区间中的实体数据（返回结果压缩后传输）。
        
        @param request: GetEntityStoreDataRequest
        @param headers: GetEntityStoreDataHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEntityStoreDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['acceptEncoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEntityStoreData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/entitiesAndRelations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetEntityStoreDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_entity_store_data_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.GetEntityStoreDataRequest,
        headers: cms_20240330_models.GetEntityStoreDataHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetEntityStoreDataResponse:
        """
        @summary 查询指定Workspace下的实体和关系数据，返回结果显示某时间区间中的实体数据（返回结果压缩后传输）。
        
        @param request: GetEntityStoreDataRequest
        @param headers: GetEntityStoreDataHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEntityStoreDataResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_):
            body['from'] = request.from_
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        if not UtilClient.is_unset(request.to):
            body['to'] = request.to
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.accept_encoding):
            real_headers['acceptEncoding'] = UtilClient.to_jsonstring(headers.accept_encoding)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEntityStoreData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/entitiesAndRelations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetEntityStoreDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_entity_store_data(
        self,
        workspace: str,
        request: cms_20240330_models.GetEntityStoreDataRequest,
    ) -> cms_20240330_models.GetEntityStoreDataResponse:
        """
        @summary 查询指定Workspace下的实体和关系数据，返回结果显示某时间区间中的实体数据（返回结果压缩后传输）。
        
        @param request: GetEntityStoreDataRequest
        @return: GetEntityStoreDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = cms_20240330_models.GetEntityStoreDataHeaders()
        return self.get_entity_store_data_with_options(workspace, request, headers, runtime)

    async def get_entity_store_data_async(
        self,
        workspace: str,
        request: cms_20240330_models.GetEntityStoreDataRequest,
    ) -> cms_20240330_models.GetEntityStoreDataResponse:
        """
        @summary 查询指定Workspace下的实体和关系数据，返回结果显示某时间区间中的实体数据（返回结果压缩后传输）。
        
        @param request: GetEntityStoreDataRequest
        @return: GetEntityStoreDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = cms_20240330_models.GetEntityStoreDataHeaders()
        return await self.get_entity_store_data_with_options_async(workspace, request, headers, runtime)

    def get_service_observability_with_options(
        self,
        workspace: str,
        type: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetServiceObservabilityResponse:
        """
        @summary 获取应用可观测实例
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceObservabilityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceObservability',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service-observability/{OpenApiUtilClient.get_encode_param(type)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetServiceObservabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_observability_with_options_async(
        self,
        workspace: str,
        type: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetServiceObservabilityResponse:
        """
        @summary 获取应用可观测实例
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceObservabilityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceObservability',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/service-observability/{OpenApiUtilClient.get_encode_param(type)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetServiceObservabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_observability(
        self,
        workspace: str,
        type: str,
    ) -> cms_20240330_models.GetServiceObservabilityResponse:
        """
        @summary 获取应用可观测实例
        
        @return: GetServiceObservabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_observability_with_options(workspace, type, headers, runtime)

    async def get_service_observability_async(
        self,
        workspace: str,
        type: str,
    ) -> cms_20240330_models.GetServiceObservabilityResponse:
        """
        @summary 获取应用可观测实例
        
        @return: GetServiceObservabilityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_observability_with_options_async(workspace, type, headers, runtime)

    def get_umodel_with_options(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelResponse:
        """
        @summary 获取Umodel配置信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUmodelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_umodel_with_options_async(
        self,
        workspace: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelResponse:
        """
        @summary 获取Umodel配置信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUmodelResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_umodel(
        self,
        workspace: str,
    ) -> cms_20240330_models.GetUmodelResponse:
        """
        @summary 获取Umodel配置信息
        
        @return: GetUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_umodel_with_options(workspace, headers, runtime)

    async def get_umodel_async(
        self,
        workspace: str,
    ) -> cms_20240330_models.GetUmodelResponse:
        """
        @summary 获取Umodel配置信息
        
        @return: GetUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_umodel_with_options_async(workspace, headers, runtime)

    def get_umodel_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.GetUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelDataResponse:
        """
        @summary 获取相关联的 Umodel 图数据
        
        @param request: GetUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/graph',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetUmodelDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_umodel_data_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.GetUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetUmodelDataResponse:
        """
        @summary 获取相关联的 Umodel 图数据
        
        @param request: GetUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/graph',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetUmodelDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_umodel_data(
        self,
        workspace: str,
        request: cms_20240330_models.GetUmodelDataRequest,
    ) -> cms_20240330_models.GetUmodelDataResponse:
        """
        @summary 获取相关联的 Umodel 图数据
        
        @param request: GetUmodelDataRequest
        @return: GetUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_umodel_data_with_options(workspace, request, headers, runtime)

    async def get_umodel_data_async(
        self,
        workspace: str,
        request: cms_20240330_models.GetUmodelDataRequest,
    ) -> cms_20240330_models.GetUmodelDataResponse:
        """
        @summary 获取相关联的 Umodel 图数据
        
        @param request: GetUmodelDataRequest
        @return: GetUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_umodel_data_with_options_async(workspace, request, headers, runtime)

    def get_workspace_with_options(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetWorkspaceResponse:
        """
        @summary 获取工作空间
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkspaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        workspace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.GetWorkspaceResponse:
        """
        @summary 获取工作空间
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkspaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.GetWorkspaceResponse:
        """
        @summary 获取工作空间
        
        @return: GetWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_workspace_with_options(workspace_name, headers, runtime)

    async def get_workspace_async(
        self,
        workspace_name: str,
    ) -> cms_20240330_models.GetWorkspaceResponse:
        """
        @summary 获取工作空间
        
        @return: GetWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_workspace_with_options_async(workspace_name, headers, runtime)

    def list_alert_actions_with_options(
        self,
        tmp_req: cms_20240330_models.ListAlertActionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary 查询告警动作
        
        @param tmp_req: ListAlertActionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertActionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListAlertActionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_action_ids):
            request.alert_action_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_action_ids, 'alertActionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_action_ids_shrink):
            query['alertActionIds'] = request.alert_action_ids_shrink
        if not UtilClient.is_unset(request.alert_action_name):
            query['alertActionName'] = request.alert_action_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertActions',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/alertActions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAlertActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_actions_with_options_async(
        self,
        tmp_req: cms_20240330_models.ListAlertActionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary 查询告警动作
        
        @param tmp_req: ListAlertActionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertActionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListAlertActionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_action_ids):
            request.alert_action_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_action_ids, 'alertActionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.alert_action_ids_shrink):
            query['alertActionIds'] = request.alert_action_ids_shrink
        if not UtilClient.is_unset(request.alert_action_name):
            query['alertActionName'] = request.alert_action_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertActions',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/alertActions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListAlertActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_actions(
        self,
        request: cms_20240330_models.ListAlertActionsRequest,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary 查询告警动作
        
        @param request: ListAlertActionsRequest
        @return: ListAlertActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alert_actions_with_options(request, headers, runtime)

    async def list_alert_actions_async(
        self,
        request: cms_20240330_models.ListAlertActionsRequest,
    ) -> cms_20240330_models.ListAlertActionsResponse:
        """
        @summary 查询告警动作
        
        @param request: ListAlertActionsRequest
        @return: ListAlertActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_alert_actions_with_options_async(request, headers, runtime)

    def list_workspaces_with_options(
        self,
        tmp_req: cms_20240330_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListWorkspacesResponse:
        """
        @summary 获取工作空间列表
        
        @param tmp_req: ListWorkspacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workspace_name_list):
            request.workspace_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_name_list, 'workspaceNameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        if not UtilClient.is_unset(request.workspace_name_list_shrink):
            query['workspaceNameList'] = request.workspace_name_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        tmp_req: cms_20240330_models.ListWorkspacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.ListWorkspacesResponse:
        """
        @summary 获取工作空间列表
        
        @param tmp_req: ListWorkspacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkspacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cms_20240330_models.ListWorkspacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.workspace_name_list):
            request.workspace_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.workspace_name_list, 'workspaceNameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region):
            query['region'] = request.region
        if not UtilClient.is_unset(request.workspace_name):
            query['workspaceName'] = request.workspace_name
        if not UtilClient.is_unset(request.workspace_name_list_shrink):
            query['workspaceNameList'] = request.workspace_name_list_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: cms_20240330_models.ListWorkspacesRequest,
    ) -> cms_20240330_models.ListWorkspacesResponse:
        """
        @summary 获取工作空间列表
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workspaces_with_options(request, headers, runtime)

    async def list_workspaces_async(
        self,
        request: cms_20240330_models.ListWorkspacesRequest,
    ) -> cms_20240330_models.ListWorkspacesResponse:
        """
        @summary 获取工作空间列表
        
        @param request: ListWorkspacesRequest
        @return: ListWorkspacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workspaces_with_options_async(request, headers, runtime)

    def put_workspace_with_options(
        self,
        workspace_name: str,
        request: cms_20240330_models.PutWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.PutWorkspaceResponse:
        """
        @summary 创建工作空间
        
        @param request: PutWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutWorkspaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.PutWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_workspace_with_options_async(
        self,
        workspace_name: str,
        request: cms_20240330_models.PutWorkspaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.PutWorkspaceResponse:
        """
        @summary 创建工作空间
        
        @param request: PutWorkspaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutWorkspaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.display_name):
            body['displayName'] = request.display_name
        if not UtilClient.is_unset(request.sls_project):
            body['slsProject'] = request.sls_project
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutWorkspace',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace_name)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.PutWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_workspace(
        self,
        workspace_name: str,
        request: cms_20240330_models.PutWorkspaceRequest,
    ) -> cms_20240330_models.PutWorkspaceResponse:
        """
        @summary 创建工作空间
        
        @param request: PutWorkspaceRequest
        @return: PutWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.put_workspace_with_options(workspace_name, request, headers, runtime)

    async def put_workspace_async(
        self,
        workspace_name: str,
        request: cms_20240330_models.PutWorkspaceRequest,
    ) -> cms_20240330_models.PutWorkspaceResponse:
        """
        @summary 创建工作空间
        
        @param request: PutWorkspaceRequest
        @return: PutWorkspaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.put_workspace_with_options_async(workspace_name, request, headers, runtime)

    def update_umodel_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.UpdateUmodelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateUmodelResponse:
        """
        @summary 更新Umodel配置信息
        
        @param request: UpdateUmodelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUmodelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.common_schema_ref):
            body['commonSchemaRef'] = request.common_schema_ref
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateUmodelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_umodel_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.UpdateUmodelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpdateUmodelResponse:
        """
        @summary 更新Umodel配置信息
        
        @param request: UpdateUmodelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUmodelResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.common_schema_ref):
            body['commonSchemaRef'] = request.common_schema_ref
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUmodel',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpdateUmodelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_umodel(
        self,
        workspace: str,
        request: cms_20240330_models.UpdateUmodelRequest,
    ) -> cms_20240330_models.UpdateUmodelResponse:
        """
        @summary 更新Umodel配置信息
        
        @param request: UpdateUmodelRequest
        @return: UpdateUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_umodel_with_options(workspace, request, headers, runtime)

    async def update_umodel_async(
        self,
        workspace: str,
        request: cms_20240330_models.UpdateUmodelRequest,
    ) -> cms_20240330_models.UpdateUmodelResponse:
        """
        @summary 更新Umodel配置信息
        
        @param request: UpdateUmodelRequest
        @return: UpdateUmodelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_umodel_with_options_async(workspace, request, headers, runtime)

    def upsert_umodel_data_with_options(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpsertUmodelDataResponse:
        """
        @summary 写入 Umodel Elements
        
        @param request: UpsertUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpsertUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        body = {}
        if not UtilClient.is_unset(request.elements):
            body['elements'] = request.elements
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/data',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpsertUmodelDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_umodel_data_with_options_async(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelDataRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cms_20240330_models.UpsertUmodelDataResponse:
        """
        @summary 写入 Umodel Elements
        
        @param request: UpsertUmodelDataRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpsertUmodelDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.method):
            query['method'] = request.method
        body = {}
        if not UtilClient.is_unset(request.elements):
            body['elements'] = request.elements
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpsertUmodelData',
            version='2024-03-30',
            protocol='HTTPS',
            pathname=f'/workspace/{OpenApiUtilClient.get_encode_param(workspace)}/umodel/data',
            method='PATCH',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cms_20240330_models.UpsertUmodelDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_umodel_data(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelDataRequest,
    ) -> cms_20240330_models.UpsertUmodelDataResponse:
        """
        @summary 写入 Umodel Elements
        
        @param request: UpsertUmodelDataRequest
        @return: UpsertUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upsert_umodel_data_with_options(workspace, request, headers, runtime)

    async def upsert_umodel_data_async(
        self,
        workspace: str,
        request: cms_20240330_models.UpsertUmodelDataRequest,
    ) -> cms_20240330_models.UpsertUmodelDataResponse:
        """
        @summary 写入 Umodel Elements
        
        @param request: UpsertUmodelDataRequest
        @return: UpsertUmodelDataResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upsert_umodel_data_with_options_async(workspace, request, headers, runtime)
