# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paifeaturestore20230621 import models as pai_feature_store_20230621_models
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
        self._endpoint = self.get_endpoint('paifeaturestore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_instance_datasource_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CheckInstanceDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CheckInstanceDatasourceResponse:
        """
        @summary 检测资源连接状态。
        
        @param request: CheckInstanceDatasourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckInstanceDatasourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstanceDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/action/checkdatasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CheckInstanceDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_datasource_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CheckInstanceDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CheckInstanceDatasourceResponse:
        """
        @summary 检测资源连接状态。
        
        @param request: CheckInstanceDatasourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckInstanceDatasourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstanceDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/action/checkdatasource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CheckInstanceDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_datasource(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CheckInstanceDatasourceRequest,
    ) -> pai_feature_store_20230621_models.CheckInstanceDatasourceResponse:
        """
        @summary 检测资源连接状态。
        
        @param request: CheckInstanceDatasourceRequest
        @return: CheckInstanceDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_instance_datasource_with_options(instance_id, request, headers, runtime)

    async def check_instance_datasource_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CheckInstanceDatasourceRequest,
    ) -> pai_feature_store_20230621_models.CheckInstanceDatasourceResponse:
        """
        @summary 检测资源连接状态。
        
        @param request: CheckInstanceDatasourceRequest
        @return: CheckInstanceDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_instance_datasource_with_options_async(instance_id, request, headers, runtime)

    def create_datasource_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateDatasourceResponse:
        """
        @summary 创建数据源。
        
        @param request: CreateDatasourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_datasource_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateDatasourceResponse:
        """
        @summary 创建数据源。
        
        @param request: CreateDatasourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_datasource(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateDatasourceRequest,
    ) -> pai_feature_store_20230621_models.CreateDatasourceResponse:
        """
        @summary 创建数据源。
        
        @param request: CreateDatasourceRequest
        @return: CreateDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_datasource_with_options(instance_id, request, headers, runtime)

    async def create_datasource_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateDatasourceRequest,
    ) -> pai_feature_store_20230621_models.CreateDatasourceResponse:
        """
        @summary 创建数据源。
        
        @param request: CreateDatasourceRequest
        @return: CreateDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_datasource_with_options_async(instance_id, request, headers, runtime)

    def create_feature_entity_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureEntityRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateFeatureEntityResponse:
        """
        @summary 创建特征实体
        
        @param request: CreateFeatureEntityRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFeatureEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.join_id):
            body['JoinId'] = request.join_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_entity_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureEntityRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateFeatureEntityResponse:
        """
        @summary 创建特征实体
        
        @param request: CreateFeatureEntityRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFeatureEntityResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.join_id):
            body['JoinId'] = request.join_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature_entity(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureEntityRequest,
    ) -> pai_feature_store_20230621_models.CreateFeatureEntityResponse:
        """
        @summary 创建特征实体
        
        @param request: CreateFeatureEntityRequest
        @return: CreateFeatureEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_entity_with_options(instance_id, request, headers, runtime)

    async def create_feature_entity_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureEntityRequest,
    ) -> pai_feature_store_20230621_models.CreateFeatureEntityResponse:
        """
        @summary 创建特征实体
        
        @param request: CreateFeatureEntityRequest
        @return: CreateFeatureEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_feature_entity_with_options_async(instance_id, request, headers, runtime)

    def create_feature_view_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateFeatureViewResponse:
        """
        @summary 创建特征视图。
        
        @param request: CreateFeatureViewRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFeatureViewResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.feature_entity_id):
            body['FeatureEntityId'] = request.feature_entity_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.register_datasource_id):
            body['RegisterDatasourceId'] = request.register_datasource_id
        if not UtilClient.is_unset(request.register_table):
            body['RegisterTable'] = request.register_table
        if not UtilClient.is_unset(request.sync_online_table):
            body['SyncOnlineTable'] = request.sync_online_table
        if not UtilClient.is_unset(request.ttl):
            body['TTL'] = request.ttl
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.write_method):
            body['WriteMethod'] = request.write_method
        if not UtilClient.is_unset(request.write_to_feature_db):
            body['WriteToFeatureDB'] = request.write_to_feature_db
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_feature_view_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureViewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateFeatureViewResponse:
        """
        @summary 创建特征视图。
        
        @param request: CreateFeatureViewRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFeatureViewResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.feature_entity_id):
            body['FeatureEntityId'] = request.feature_entity_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.register_datasource_id):
            body['RegisterDatasourceId'] = request.register_datasource_id
        if not UtilClient.is_unset(request.register_table):
            body['RegisterTable'] = request.register_table
        if not UtilClient.is_unset(request.sync_online_table):
            body['SyncOnlineTable'] = request.sync_online_table
        if not UtilClient.is_unset(request.ttl):
            body['TTL'] = request.ttl
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.write_method):
            body['WriteMethod'] = request.write_method
        if not UtilClient.is_unset(request.write_to_feature_db):
            body['WriteToFeatureDB'] = request.write_to_feature_db
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateFeatureViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_feature_view(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureViewRequest,
    ) -> pai_feature_store_20230621_models.CreateFeatureViewResponse:
        """
        @summary 创建特征视图。
        
        @param request: CreateFeatureViewRequest
        @return: CreateFeatureViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_feature_view_with_options(instance_id, request, headers, runtime)

    async def create_feature_view_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateFeatureViewRequest,
    ) -> pai_feature_store_20230621_models.CreateFeatureViewResponse:
        """
        @summary 创建特征视图。
        
        @param request: CreateFeatureViewRequest
        @return: CreateFeatureViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_feature_view_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: pai_feature_store_20230621_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateInstanceResponse:
        """
        @summary 创建Feature Store实例。
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: pai_feature_store_20230621_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateInstanceResponse:
        """
        @summary 创建Feature Store实例。
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: pai_feature_store_20230621_models.CreateInstanceRequest,
    ) -> pai_feature_store_20230621_models.CreateInstanceResponse:
        """
        @summary 创建Feature Store实例。
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: pai_feature_store_20230621_models.CreateInstanceRequest,
    ) -> pai_feature_store_20230621_models.CreateInstanceResponse:
        """
        @summary 创建Feature Store实例。
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_label_table_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateLabelTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateLabelTableResponse:
        """
        @summary 创建label表
        
        @param request: CreateLabelTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabelTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_label_table_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateLabelTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateLabelTableResponse:
        """
        @summary 创建label表
        
        @param request: CreateLabelTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLabelTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_label_table(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateLabelTableRequest,
    ) -> pai_feature_store_20230621_models.CreateLabelTableResponse:
        """
        @summary 创建label表
        
        @param request: CreateLabelTableRequest
        @return: CreateLabelTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_label_table_with_options(instance_id, request, headers, runtime)

    async def create_label_table_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateLabelTableRequest,
    ) -> pai_feature_store_20230621_models.CreateLabelTableResponse:
        """
        @summary 创建label表
        
        @param request: CreateLabelTableRequest
        @return: CreateLabelTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_label_table_with_options_async(instance_id, request, headers, runtime)

    def create_model_feature_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateModelFeatureResponse:
        """
        @summary 创建模型特征。
        
        @param request: CreateModelFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.features):
            body['Features'] = request.features
        if not UtilClient.is_unset(request.label_priority_level):
            body['LabelPriorityLevel'] = request.label_priority_level
        if not UtilClient.is_unset(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sequence_feature_view_ids):
            body['SequenceFeatureViewIds'] = request.sequence_feature_view_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_feature_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateModelFeatureResponse:
        """
        @summary 创建模型特征。
        
        @param request: CreateModelFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.features):
            body['Features'] = request.features
        if not UtilClient.is_unset(request.label_priority_level):
            body['LabelPriorityLevel'] = request.label_priority_level
        if not UtilClient.is_unset(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sequence_feature_view_ids):
            body['SequenceFeatureViewIds'] = request.sequence_feature_view_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_feature(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateModelFeatureRequest,
    ) -> pai_feature_store_20230621_models.CreateModelFeatureResponse:
        """
        @summary 创建模型特征。
        
        @param request: CreateModelFeatureRequest
        @return: CreateModelFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_model_feature_with_options(instance_id, request, headers, runtime)

    async def create_model_feature_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateModelFeatureRequest,
    ) -> pai_feature_store_20230621_models.CreateModelFeatureResponse:
        """
        @summary 创建模型特征。
        
        @param request: CreateModelFeatureRequest
        @return: CreateModelFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_model_feature_with_options_async(instance_id, request, headers, runtime)

    def create_project_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateProjectResponse:
        """
        @summary 创建FeatureStore项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.offline_datasource_id):
            body['OfflineDatasourceId'] = request.offline_datasource_id
        if not UtilClient.is_unset(request.offline_life_cycle):
            body['OfflineLifeCycle'] = request.offline_life_cycle
        if not UtilClient.is_unset(request.online_datasource_id):
            body['OnlineDatasourceId'] = request.online_datasource_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateProjectResponse:
        """
        @summary 创建FeatureStore项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.offline_datasource_id):
            body['OfflineDatasourceId'] = request.offline_datasource_id
        if not UtilClient.is_unset(request.offline_life_cycle):
            body['OfflineLifeCycle'] = request.offline_life_cycle
        if not UtilClient.is_unset(request.online_datasource_id):
            body['OnlineDatasourceId'] = request.online_datasource_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateProjectRequest,
    ) -> pai_feature_store_20230621_models.CreateProjectResponse:
        """
        @summary 创建FeatureStore项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(instance_id, request, headers, runtime)

    async def create_project_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.CreateProjectRequest,
    ) -> pai_feature_store_20230621_models.CreateProjectResponse:
        """
        @summary 创建FeatureStore项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(instance_id, request, headers, runtime)

    def create_service_identity_role_with_options(
        self,
        request: pai_feature_store_20230621_models.CreateServiceIdentityRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse:
        """
        @summary 创建feature store服务账户角色
        
        @param request: CreateServiceIdentityRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceIdentityRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceIdentityRole',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/serviceidentityroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_identity_role_with_options_async(
        self,
        request: pai_feature_store_20230621_models.CreateServiceIdentityRoleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse:
        """
        @summary 创建feature store服务账户角色
        
        @param request: CreateServiceIdentityRoleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceIdentityRoleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.role_name):
            body['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceIdentityRole',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/serviceidentityroles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_identity_role(
        self,
        request: pai_feature_store_20230621_models.CreateServiceIdentityRoleRequest,
    ) -> pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse:
        """
        @summary 创建feature store服务账户角色
        
        @param request: CreateServiceIdentityRoleRequest
        @return: CreateServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_identity_role_with_options(request, headers, runtime)

    async def create_service_identity_role_async(
        self,
        request: pai_feature_store_20230621_models.CreateServiceIdentityRoleRequest,
    ) -> pai_feature_store_20230621_models.CreateServiceIdentityRoleResponse:
        """
        @summary 创建feature store服务账户角色
        
        @param request: CreateServiceIdentityRoleRequest
        @return: CreateServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_identity_role_with_options_async(request, headers, runtime)

    def delete_datasource_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteDatasourceResponse:
        """
        @summary 删除指定数据源。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_datasource_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteDatasourceResponse:
        """
        @summary 删除指定数据源。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_datasource(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> pai_feature_store_20230621_models.DeleteDatasourceResponse:
        """
        @summary 删除指定数据源。
        
        @return: DeleteDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_datasource_with_options(instance_id, datasource_id, headers, runtime)

    async def delete_datasource_async(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> pai_feature_store_20230621_models.DeleteDatasourceResponse:
        """
        @summary 删除指定数据源。
        
        @return: DeleteDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_datasource_with_options_async(instance_id, datasource_id, headers, runtime)

    def delete_feature_entity_with_options(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteFeatureEntityResponse:
        """
        @summary 删除指定特征实体
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFeatureEntityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_feature_entity_with_options_async(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteFeatureEntityResponse:
        """
        @summary 删除指定特征实体
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFeatureEntityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_feature_entity(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> pai_feature_store_20230621_models.DeleteFeatureEntityResponse:
        """
        @summary 删除指定特征实体
        
        @return: DeleteFeatureEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_feature_entity_with_options(instance_id, feature_entity_id, headers, runtime)

    async def delete_feature_entity_async(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> pai_feature_store_20230621_models.DeleteFeatureEntityResponse:
        """
        @summary 删除指定特征实体
        
        @return: DeleteFeatureEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_feature_entity_with_options_async(instance_id, feature_entity_id, headers, runtime)

    def delete_feature_view_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteFeatureViewResponse:
        """
        @summary 删除指定特征视图。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFeatureViewResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_feature_view_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteFeatureViewResponse:
        """
        @summary 删除指定特征视图。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFeatureViewResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteFeatureViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_feature_view(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.DeleteFeatureViewResponse:
        """
        @summary 删除指定特征视图。
        
        @return: DeleteFeatureViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_feature_view_with_options(instance_id, feature_view_id, headers, runtime)

    async def delete_feature_view_async(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.DeleteFeatureViewResponse:
        """
        @summary 删除指定特征视图。
        
        @return: DeleteFeatureViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_feature_view_with_options_async(instance_id, feature_view_id, headers, runtime)

    def delete_label_table_with_options(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteLabelTableResponse:
        """
        @summary 删除label表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLabelTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_label_table_with_options_async(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteLabelTableResponse:
        """
        @summary 删除label表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLabelTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_label_table(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> pai_feature_store_20230621_models.DeleteLabelTableResponse:
        """
        @summary 删除label表
        
        @return: DeleteLabelTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_label_table_with_options(instance_id, label_table_id, headers, runtime)

    async def delete_label_table_async(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> pai_feature_store_20230621_models.DeleteLabelTableResponse:
        """
        @summary 删除label表
        
        @return: DeleteLabelTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_label_table_with_options_async(instance_id, label_table_id, headers, runtime)

    def delete_model_feature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteModelFeatureResponse:
        """
        @summary 删除指定模型特征。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelFeatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_feature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteModelFeatureResponse:
        """
        @summary 删除指定模型特征。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelFeatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_feature(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.DeleteModelFeatureResponse:
        """
        @summary 删除指定模型特征。
        
        @return: DeleteModelFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_model_feature_with_options(instance_id, model_feature_id, headers, runtime)

    async def delete_model_feature_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.DeleteModelFeatureResponse:
        """
        @summary 删除指定模型特征。
        
        @return: DeleteModelFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_model_feature_with_options_async(instance_id, model_feature_id, headers, runtime)

    def delete_project_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteProjectResponse:
        """
        @summary 删除指定Feature Store项目。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.DeleteProjectResponse:
        """
        @summary 删除指定Feature Store项目。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.DeleteProjectResponse:
        """
        @summary 删除指定Feature Store项目。
        
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(instance_id, project_id, headers, runtime)

    async def delete_project_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.DeleteProjectResponse:
        """
        @summary 删除指定Feature Store项目。
        
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(instance_id, project_id, headers, runtime)

    def export_model_feature_training_set_table_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse:
        """
        @summary 导出训练集表。
        
        @param request: ExportModelFeatureTrainingSetTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportModelFeatureTrainingSetTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feature_view_config):
            body['FeatureViewConfig'] = request.feature_view_config
        if not UtilClient.is_unset(request.label_input_config):
            body['LabelInputConfig'] = request.label_input_config
        if not UtilClient.is_unset(request.real_time_iterate_interval):
            body['RealTimeIterateInterval'] = request.real_time_iterate_interval
        if not UtilClient.is_unset(request.real_time_partition_count_value):
            body['RealTimePartitionCountValue'] = request.real_time_partition_count_value
        if not UtilClient.is_unset(request.training_set_config):
            body['TrainingSetConfig'] = request.training_set_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportModelFeatureTrainingSetTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/action/exporttrainingsettable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_model_feature_training_set_table_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse:
        """
        @summary 导出训练集表。
        
        @param request: ExportModelFeatureTrainingSetTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportModelFeatureTrainingSetTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feature_view_config):
            body['FeatureViewConfig'] = request.feature_view_config
        if not UtilClient.is_unset(request.label_input_config):
            body['LabelInputConfig'] = request.label_input_config
        if not UtilClient.is_unset(request.real_time_iterate_interval):
            body['RealTimeIterateInterval'] = request.real_time_iterate_interval
        if not UtilClient.is_unset(request.real_time_partition_count_value):
            body['RealTimePartitionCountValue'] = request.real_time_partition_count_value
        if not UtilClient.is_unset(request.training_set_config):
            body['TrainingSetConfig'] = request.training_set_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportModelFeatureTrainingSetTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/action/exporttrainingsettable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_model_feature_training_set_table(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableRequest,
    ) -> pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse:
        """
        @summary 导出训练集表。
        
        @param request: ExportModelFeatureTrainingSetTableRequest
        @return: ExportModelFeatureTrainingSetTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.export_model_feature_training_set_table_with_options(instance_id, model_feature_id, request, headers, runtime)

    async def export_model_feature_training_set_table_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableRequest,
    ) -> pai_feature_store_20230621_models.ExportModelFeatureTrainingSetTableResponse:
        """
        @summary 导出训练集表。
        
        @param request: ExportModelFeatureTrainingSetTableRequest
        @return: ExportModelFeatureTrainingSetTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.export_model_feature_training_set_table_with_options_async(instance_id, model_feature_id, request, headers, runtime)

    def get_datasource_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetDatasourceResponse:
        """
        @summary 获取数据源详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_datasource_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetDatasourceResponse:
        """
        @summary 获取数据源详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_datasource(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> pai_feature_store_20230621_models.GetDatasourceResponse:
        """
        @summary 获取数据源详细信息。
        
        @return: GetDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_datasource_with_options(instance_id, datasource_id, headers, runtime)

    async def get_datasource_async(
        self,
        instance_id: str,
        datasource_id: str,
    ) -> pai_feature_store_20230621_models.GetDatasourceResponse:
        """
        @summary 获取数据源详细信息。
        
        @return: GetDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_datasource_with_options_async(instance_id, datasource_id, headers, runtime)

    def get_datasource_table_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetDatasourceTableResponse:
        """
        @summary 获取数据源下指定表的详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasourceTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasourceTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetDatasourceTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_datasource_table_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetDatasourceTableResponse:
        """
        @summary 获取数据源下指定表的详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasourceTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatasourceTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetDatasourceTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_datasource_table(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
    ) -> pai_feature_store_20230621_models.GetDatasourceTableResponse:
        """
        @summary 获取数据源下指定表的详细信息。
        
        @return: GetDatasourceTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_datasource_table_with_options(instance_id, datasource_id, table_name, headers, runtime)

    async def get_datasource_table_async(
        self,
        instance_id: str,
        datasource_id: str,
        table_name: str,
    ) -> pai_feature_store_20230621_models.GetDatasourceTableResponse:
        """
        @summary 获取数据源下指定表的详细信息。
        
        @return: GetDatasourceTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_datasource_table_with_options_async(instance_id, datasource_id, table_name, headers, runtime)

    def get_feature_entity_with_options(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetFeatureEntityResponse:
        """
        @summary 获取特征实体详细信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureEntityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_entity_with_options_async(
        self,
        instance_id: str,
        feature_entity_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetFeatureEntityResponse:
        """
        @summary 获取特征实体详细信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureEntityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_entity(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> pai_feature_store_20230621_models.GetFeatureEntityResponse:
        """
        @summary 获取特征实体详细信息
        
        @return: GetFeatureEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_entity_with_options(instance_id, feature_entity_id, headers, runtime)

    async def get_feature_entity_async(
        self,
        instance_id: str,
        feature_entity_id: str,
    ) -> pai_feature_store_20230621_models.GetFeatureEntityResponse:
        """
        @summary 获取特征实体详细信息
        
        @return: GetFeatureEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_feature_entity_with_options_async(instance_id, feature_entity_id, headers, runtime)

    def get_feature_view_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetFeatureViewResponse:
        """
        @summary 获取特征视图详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureViewResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetFeatureViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_view_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetFeatureViewResponse:
        """
        @summary 获取特征视图详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureViewResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetFeatureView',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetFeatureViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_view(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.GetFeatureViewResponse:
        """
        @summary 获取特征视图详细信息。
        
        @return: GetFeatureViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_feature_view_with_options(instance_id, feature_view_id, headers, runtime)

    async def get_feature_view_async(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.GetFeatureViewResponse:
        """
        @summary 获取特征视图详细信息。
        
        @return: GetFeatureViewResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_feature_view_with_options_async(instance_id, feature_view_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetInstanceResponse:
        """
        @summary 获取实例详细信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetInstanceResponse:
        """
        @summary 获取实例详细信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> pai_feature_store_20230621_models.GetInstanceResponse:
        """
        @summary 获取实例详细信息
        
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> pai_feature_store_20230621_models.GetInstanceResponse:
        """
        @summary 获取实例详细信息
        
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_label_table_with_options(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetLabelTableResponse:
        """
        @summary 获取Label表详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLabelTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_label_table_with_options_async(
        self,
        instance_id: str,
        label_table_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetLabelTableResponse:
        """
        @summary 获取Label表详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLabelTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_label_table(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> pai_feature_store_20230621_models.GetLabelTableResponse:
        """
        @summary 获取Label表详细信息。
        
        @return: GetLabelTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_label_table_with_options(instance_id, label_table_id, headers, runtime)

    async def get_label_table_async(
        self,
        instance_id: str,
        label_table_id: str,
    ) -> pai_feature_store_20230621_models.GetLabelTableResponse:
        """
        @summary 获取Label表详细信息。
        
        @return: GetLabelTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_label_table_with_options_async(instance_id, label_table_id, headers, runtime)

    def get_model_feature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetModelFeatureResponse:
        """
        @summary 获取模型特征详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelFeatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_feature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetModelFeatureResponse:
        """
        @summary 获取模型特征详情。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelFeatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_feature(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.GetModelFeatureResponse:
        """
        @summary 获取模型特征详情。
        
        @return: GetModelFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_feature_with_options(instance_id, model_feature_id, headers, runtime)

    async def get_model_feature_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.GetModelFeatureResponse:
        """
        @summary 获取模型特征详情。
        
        @return: GetModelFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_feature_with_options_async(instance_id, model_feature_id, headers, runtime)

    def get_model_feature_fgfeature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetModelFeatureFGFeatureResponse:
        """
        @summary 获取模型特征的FG特征配置信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelFeatureFGFeatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeatureFGFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/fgfeature',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureFGFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_feature_fgfeature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetModelFeatureFGFeatureResponse:
        """
        @summary 获取模型特征的FG特征配置信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelFeatureFGFeatureResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeatureFGFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/fgfeature',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureFGFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_feature_fgfeature(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.GetModelFeatureFGFeatureResponse:
        """
        @summary 获取模型特征的FG特征配置信息。
        
        @return: GetModelFeatureFGFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_feature_fgfeature_with_options(instance_id, model_feature_id, headers, runtime)

    async def get_model_feature_fgfeature_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.GetModelFeatureFGFeatureResponse:
        """
        @summary 获取模型特征的FG特征配置信息。
        
        @return: GetModelFeatureFGFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_feature_fgfeature_with_options_async(instance_id, model_feature_id, headers, runtime)

    def get_model_feature_fginfo_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetModelFeatureFGInfoResponse:
        """
        @summary 获取模型特征的fg.json文件配置信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelFeatureFGInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeatureFGInfo',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/fginfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureFGInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_feature_fginfo_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetModelFeatureFGInfoResponse:
        """
        @summary 获取模型特征的fg.json文件配置信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelFeatureFGInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModelFeatureFGInfo',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/fginfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetModelFeatureFGInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_feature_fginfo(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.GetModelFeatureFGInfoResponse:
        """
        @summary 获取模型特征的fg.json文件配置信息。
        
        @return: GetModelFeatureFGInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_model_feature_fginfo_with_options(instance_id, model_feature_id, headers, runtime)

    async def get_model_feature_fginfo_async(
        self,
        instance_id: str,
        model_feature_id: str,
    ) -> pai_feature_store_20230621_models.GetModelFeatureFGInfoResponse:
        """
        @summary 获取模型特征的fg.json文件配置信息。
        
        @return: GetModelFeatureFGInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_model_feature_fginfo_with_options_async(instance_id, model_feature_id, headers, runtime)

    def get_project_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectResponse:
        """
        @summary 获取指定Feature Store项目详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectResponse:
        """
        @summary 获取指定Feature Store项目详细信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.GetProjectResponse:
        """
        @summary 获取指定Feature Store项目详细信息。
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(instance_id, project_id, headers, runtime)

    async def get_project_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.GetProjectResponse:
        """
        @summary 获取指定Feature Store项目详细信息。
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(instance_id, project_id, headers, runtime)

    def get_project_feature_entity_with_options(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityResponse:
        """
        @summary 获取项目下特征实体详细信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectFeatureEntityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_feature_entity_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityResponse:
        """
        @summary 获取项目下特征实体详细信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectFeatureEntityResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProjectFeatureEntity',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureentities/{OpenApiUtilClient.get_encode_param(feature_entity_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetProjectFeatureEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_feature_entity(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityResponse:
        """
        @summary 获取项目下特征实体详细信息
        
        @return: GetProjectFeatureEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_feature_entity_with_options(instance_id, project_id, feature_entity_name, headers, runtime)

    async def get_project_feature_entity_async(
        self,
        instance_id: str,
        project_id: str,
        feature_entity_name: str,
    ) -> pai_feature_store_20230621_models.GetProjectFeatureEntityResponse:
        """
        @summary 获取项目下特征实体详细信息
        
        @return: GetProjectFeatureEntityResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_feature_entity_with_options_async(instance_id, project_id, feature_entity_name, headers, runtime)

    def get_service_identity_role_with_options(
        self,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetServiceIdentityRoleResponse:
        """
        @summary 获取feature store服务账户角色。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceIdentityRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceIdentityRole',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/serviceidentityroles/{OpenApiUtilClient.get_encode_param(role_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetServiceIdentityRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_identity_role_with_options_async(
        self,
        role_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetServiceIdentityRoleResponse:
        """
        @summary 获取feature store服务账户角色。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceIdentityRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetServiceIdentityRole',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/serviceidentityroles/{OpenApiUtilClient.get_encode_param(role_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetServiceIdentityRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_identity_role(
        self,
        role_name: str,
    ) -> pai_feature_store_20230621_models.GetServiceIdentityRoleResponse:
        """
        @summary 获取feature store服务账户角色。
        
        @return: GetServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_identity_role_with_options(role_name, headers, runtime)

    async def get_service_identity_role_async(
        self,
        role_name: str,
    ) -> pai_feature_store_20230621_models.GetServiceIdentityRoleResponse:
        """
        @summary 获取feature store服务账户角色。
        
        @return: GetServiceIdentityRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_identity_role_with_options_async(role_name, headers, runtime)

    def get_task_with_options(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetTaskResponse:
        """
        @summary 获取任务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.GetTaskResponse:
        """
        @summary 获取任务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        instance_id: str,
        task_id: str,
    ) -> pai_feature_store_20230621_models.GetTaskResponse:
        """
        @summary 获取任务详情
        
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(instance_id, task_id, headers, runtime)

    async def get_task_async(
        self,
        instance_id: str,
        task_id: str,
    ) -> pai_feature_store_20230621_models.GetTaskResponse:
        """
        @summary 获取任务详情
        
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(instance_id, task_id, headers, runtime)

    def list_datasource_tables_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.ListDatasourceTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListDatasourceTablesResponse:
        """
        @summary 获取数据源下所有表。
        
        @param request: ListDatasourceTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasourceTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasourceTables',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListDatasourceTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasource_tables_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.ListDatasourceTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListDatasourceTablesResponse:
        """
        @summary 获取数据源下所有表。
        
        @param request: ListDatasourceTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasourceTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasourceTables',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListDatasourceTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasource_tables(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.ListDatasourceTablesRequest,
    ) -> pai_feature_store_20230621_models.ListDatasourceTablesResponse:
        """
        @summary 获取数据源下所有表。
        
        @param request: ListDatasourceTablesRequest
        @return: ListDatasourceTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_datasource_tables_with_options(instance_id, datasource_id, request, headers, runtime)

    async def list_datasource_tables_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.ListDatasourceTablesRequest,
    ) -> pai_feature_store_20230621_models.ListDatasourceTablesResponse:
        """
        @summary 获取数据源下所有表。
        
        @param request: ListDatasourceTablesRequest
        @return: ListDatasourceTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_datasource_tables_with_options_async(instance_id, datasource_id, request, headers, runtime)

    def list_datasources_with_options(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListDatasourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListDatasourcesResponse:
        """
        @summary 获取数据源列表。
        
        @param request: ListDatasourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasources',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListDatasourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasources_with_options_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListDatasourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListDatasourcesResponse:
        """
        @summary 获取数据源列表。
        
        @param request: ListDatasourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasources',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListDatasourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasources(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListDatasourcesRequest,
    ) -> pai_feature_store_20230621_models.ListDatasourcesResponse:
        """
        @summary 获取数据源列表。
        
        @param request: ListDatasourcesRequest
        @return: ListDatasourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_datasources_with_options(instance_id, request, headers, runtime)

    async def list_datasources_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListDatasourcesRequest,
    ) -> pai_feature_store_20230621_models.ListDatasourcesResponse:
        """
        @summary 获取数据源列表。
        
        @param request: ListDatasourcesRequest
        @return: ListDatasourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_datasources_with_options_async(instance_id, request, headers, runtime)

    def list_feature_entities_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListFeatureEntitiesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureEntitiesResponse:
        """
        @summary 创建特征实体列表
        
        @param tmp_req: ListFeatureEntitiesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureEntitiesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureEntitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_entity_ids):
            request.feature_entity_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_entity_ids, 'FeatureEntityIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.feature_entity_ids_shrink):
            query['FeatureEntityIds'] = request.feature_entity_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureEntities',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_entities_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListFeatureEntitiesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureEntitiesResponse:
        """
        @summary 创建特征实体列表
        
        @param tmp_req: ListFeatureEntitiesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureEntitiesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureEntitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_entity_ids):
            request.feature_entity_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_entity_ids, 'FeatureEntityIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.feature_entity_ids_shrink):
            query['FeatureEntityIds'] = request.feature_entity_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureEntities',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureentities',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_entities(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListFeatureEntitiesRequest,
    ) -> pai_feature_store_20230621_models.ListFeatureEntitiesResponse:
        """
        @summary 创建特征实体列表
        
        @param request: ListFeatureEntitiesRequest
        @return: ListFeatureEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_entities_with_options(instance_id, request, headers, runtime)

    async def list_feature_entities_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListFeatureEntitiesRequest,
    ) -> pai_feature_store_20230621_models.ListFeatureEntitiesResponse:
        """
        @summary 创建特征实体列表
        
        @param request: ListFeatureEntitiesRequest
        @return: ListFeatureEntitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_entities_with_options_async(instance_id, request, headers, runtime)

    def list_feature_view_field_relationships_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse:
        """
        @summary 获取特征字段血缘关系。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureViewFieldRelationshipsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFeatureViewFieldRelationships',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/fields/{OpenApiUtilClient.get_encode_param(field_name)}/relationships',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_view_field_relationships_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse:
        """
        @summary 获取特征字段血缘关系。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureViewFieldRelationshipsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFeatureViewFieldRelationships',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/fields/{OpenApiUtilClient.get_encode_param(field_name)}/relationships',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_view_field_relationships(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
    ) -> pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse:
        """
        @summary 获取特征字段血缘关系。
        
        @return: ListFeatureViewFieldRelationshipsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_view_field_relationships_with_options(instance_id, feature_view_id, field_name, headers, runtime)

    async def list_feature_view_field_relationships_async(
        self,
        instance_id: str,
        feature_view_id: str,
        field_name: str,
    ) -> pai_feature_store_20230621_models.ListFeatureViewFieldRelationshipsResponse:
        """
        @summary 获取特征字段血缘关系。
        
        @return: ListFeatureViewFieldRelationshipsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_view_field_relationships_with_options_async(instance_id, feature_view_id, field_name, headers, runtime)

    def list_feature_view_online_features_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        tmp_req: pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesResponse:
        """
        @summary 获取特征视图下的在线特征数据。
        
        @param tmp_req: ListFeatureViewOnlineFeaturesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureViewOnlineFeaturesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.join_ids):
            request.join_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.join_ids, 'JoinIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.join_ids_shrink):
            query['JoinIds'] = request.join_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureViewOnlineFeatures',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/onlinefeatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_view_online_features_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        tmp_req: pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesResponse:
        """
        @summary 获取特征视图下的在线特征数据。
        
        @param tmp_req: ListFeatureViewOnlineFeaturesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureViewOnlineFeaturesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.join_ids):
            request.join_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.join_ids, 'JoinIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.join_ids_shrink):
            query['JoinIds'] = request.join_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureViewOnlineFeatures',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/onlinefeatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_view_online_features(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesRequest,
    ) -> pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesResponse:
        """
        @summary 获取特征视图下的在线特征数据。
        
        @param request: ListFeatureViewOnlineFeaturesRequest
        @return: ListFeatureViewOnlineFeaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_view_online_features_with_options(instance_id, feature_view_id, request, headers, runtime)

    async def list_feature_view_online_features_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesRequest,
    ) -> pai_feature_store_20230621_models.ListFeatureViewOnlineFeaturesResponse:
        """
        @summary 获取特征视图下的在线特征数据。
        
        @param request: ListFeatureViewOnlineFeaturesRequest
        @return: ListFeatureViewOnlineFeaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_view_online_features_with_options_async(instance_id, feature_view_id, request, headers, runtime)

    def list_feature_view_relationships_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse:
        """
        @summary 获取特征视图血缘关系。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureViewRelationshipsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFeatureViewRelationships',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/relationships',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_view_relationships_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse:
        """
        @summary 获取特征视图血缘关系。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureViewRelationshipsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListFeatureViewRelationships',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/relationships',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_view_relationships(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse:
        """
        @summary 获取特征视图血缘关系。
        
        @return: ListFeatureViewRelationshipsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_view_relationships_with_options(instance_id, feature_view_id, headers, runtime)

    async def list_feature_view_relationships_async(
        self,
        instance_id: str,
        feature_view_id: str,
    ) -> pai_feature_store_20230621_models.ListFeatureViewRelationshipsResponse:
        """
        @summary 获取特征视图血缘关系。
        
        @return: ListFeatureViewRelationshipsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_view_relationships_with_options_async(instance_id, feature_view_id, headers, runtime)

    def list_feature_views_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListFeatureViewsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewsResponse:
        """
        @summary 获取特征视图列表。
        
        @param tmp_req: ListFeatureViewsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureViewsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureViewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_view_ids):
            request.feature_view_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_view_ids, 'FeatureViewIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_view_ids_shrink):
            query['FeatureViewIds'] = request.feature_view_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureViews',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_feature_views_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListFeatureViewsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListFeatureViewsResponse:
        """
        @summary 获取特征视图列表。
        
        @param tmp_req: ListFeatureViewsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFeatureViewsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListFeatureViewsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.feature_view_ids):
            request.feature_view_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.feature_view_ids, 'FeatureViewIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_view_ids_shrink):
            query['FeatureViewIds'] = request.feature_view_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFeatureViews',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListFeatureViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_feature_views(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListFeatureViewsRequest,
    ) -> pai_feature_store_20230621_models.ListFeatureViewsResponse:
        """
        @summary 获取特征视图列表。
        
        @param request: ListFeatureViewsRequest
        @return: ListFeatureViewsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_feature_views_with_options(instance_id, request, headers, runtime)

    async def list_feature_views_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListFeatureViewsRequest,
    ) -> pai_feature_store_20230621_models.ListFeatureViewsResponse:
        """
        @summary 获取特征视图列表。
        
        @param request: ListFeatureViewsRequest
        @return: ListFeatureViewsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_feature_views_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        request: pai_feature_store_20230621_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListInstancesResponse:
        """
        @summary 获取Feature Store实例列表。
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: pai_feature_store_20230621_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListInstancesResponse:
        """
        @summary 获取Feature Store实例列表。
        
        @param request: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: pai_feature_store_20230621_models.ListInstancesRequest,
    ) -> pai_feature_store_20230621_models.ListInstancesResponse:
        """
        @summary 获取Feature Store实例列表。
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: pai_feature_store_20230621_models.ListInstancesRequest,
    ) -> pai_feature_store_20230621_models.ListInstancesResponse:
        """
        @summary 获取Feature Store实例列表。
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_label_tables_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListLabelTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListLabelTablesResponse:
        """
        @summary 获取Label表列表。
        
        @param tmp_req: ListLabelTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLabelTablesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListLabelTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_table_ids):
            request.label_table_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_table_ids, 'LabelTableIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_table_ids_shrink):
            query['LabelTableIds'] = request.label_table_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLabelTables',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListLabelTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_label_tables_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListLabelTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListLabelTablesResponse:
        """
        @summary 获取Label表列表。
        
        @param tmp_req: ListLabelTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLabelTablesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListLabelTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.label_table_ids):
            request.label_table_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.label_table_ids, 'LabelTableIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.label_table_ids_shrink):
            query['LabelTableIds'] = request.label_table_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLabelTables',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListLabelTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_label_tables(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListLabelTablesRequest,
    ) -> pai_feature_store_20230621_models.ListLabelTablesResponse:
        """
        @summary 获取Label表列表。
        
        @param request: ListLabelTablesRequest
        @return: ListLabelTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_label_tables_with_options(instance_id, request, headers, runtime)

    async def list_label_tables_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListLabelTablesRequest,
    ) -> pai_feature_store_20230621_models.ListLabelTablesResponse:
        """
        @summary 获取Label表列表。
        
        @param request: ListLabelTablesRequest
        @return: ListLabelTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_label_tables_with_options_async(instance_id, request, headers, runtime)

    def list_model_feature_available_features_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesResponse:
        """
        @summary 获取注册FG特征时模型特征下可选的所有特征。
        
        @param request: ListModelFeatureAvailableFeaturesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelFeatureAvailableFeaturesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelFeatureAvailableFeatures',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/availablefeatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_feature_available_features_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesResponse:
        """
        @summary 获取注册FG特征时模型特征下可选的所有特征。
        
        @param request: ListModelFeatureAvailableFeaturesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelFeatureAvailableFeaturesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelFeatureAvailableFeatures',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/availablefeatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_feature_available_features(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesRequest,
    ) -> pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesResponse:
        """
        @summary 获取注册FG特征时模型特征下可选的所有特征。
        
        @param request: ListModelFeatureAvailableFeaturesRequest
        @return: ListModelFeatureAvailableFeaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_model_feature_available_features_with_options(instance_id, model_feature_id, request, headers, runtime)

    async def list_model_feature_available_features_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesRequest,
    ) -> pai_feature_store_20230621_models.ListModelFeatureAvailableFeaturesResponse:
        """
        @summary 获取注册FG特征时模型特征下可选的所有特征。
        
        @param request: ListModelFeatureAvailableFeaturesRequest
        @return: ListModelFeatureAvailableFeaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_model_feature_available_features_with_options_async(instance_id, model_feature_id, request, headers, runtime)

    def list_model_features_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListModelFeaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListModelFeaturesResponse:
        """
        @summary 获取模型特征列表。
        
        @param tmp_req: ListModelFeaturesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelFeaturesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListModelFeaturesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model_feature_ids):
            request.model_feature_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_feature_ids, 'ModelFeatureIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.model_feature_ids_shrink):
            query['ModelFeatureIds'] = request.model_feature_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelFeatures',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListModelFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_features_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListModelFeaturesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListModelFeaturesResponse:
        """
        @summary 获取模型特征列表。
        
        @param tmp_req: ListModelFeaturesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelFeaturesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListModelFeaturesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model_feature_ids):
            request.model_feature_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_feature_ids, 'ModelFeatureIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.model_feature_ids_shrink):
            query['ModelFeatureIds'] = request.model_feature_ids_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelFeatures',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListModelFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_features(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListModelFeaturesRequest,
    ) -> pai_feature_store_20230621_models.ListModelFeaturesResponse:
        """
        @summary 获取模型特征列表。
        
        @param request: ListModelFeaturesRequest
        @return: ListModelFeaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_model_features_with_options(instance_id, request, headers, runtime)

    async def list_model_features_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListModelFeaturesRequest,
    ) -> pai_feature_store_20230621_models.ListModelFeaturesResponse:
        """
        @summary 获取模型特征列表。
        
        @param request: ListModelFeaturesRequest
        @return: ListModelFeaturesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_model_features_with_options_async(instance_id, request, headers, runtime)

    def list_project_feature_views_with_options(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewsResponse:
        """
        @summary 获取项目下的所有特征视图、特征信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectFeatureViewsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViews',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureviews',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_feature_views_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewsResponse:
        """
        @summary 获取项目下的所有特征视图、特征信息。
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectFeatureViewsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListProjectFeatureViews',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}/featureviews',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectFeatureViewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_feature_views(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewsResponse:
        """
        @summary 获取项目下的所有特征视图、特征信息。
        
        @return: ListProjectFeatureViewsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_feature_views_with_options(instance_id, project_id, headers, runtime)

    async def list_project_feature_views_async(
        self,
        instance_id: str,
        project_id: str,
    ) -> pai_feature_store_20230621_models.ListProjectFeatureViewsResponse:
        """
        @summary 获取项目下的所有特征视图、特征信息。
        
        @return: ListProjectFeatureViewsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_feature_views_with_options_async(instance_id, project_id, headers, runtime)

    def list_projects_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectsResponse:
        """
        @summary 获取Feature Store项目列表。
        
        @param tmp_req: ListProjectsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.project_ids):
            request.project_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.project_ids, 'ProjectIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_ids_shrink):
            query['ProjectIds'] = request.project_ids_shrink
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListProjectsResponse:
        """
        @summary 获取Feature Store项目列表。
        
        @param tmp_req: ListProjectsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.project_ids):
            request.project_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.project_ids, 'ProjectIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_ids_shrink):
            query['ProjectIds'] = request.project_ids_shrink
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListProjectsRequest,
    ) -> pai_feature_store_20230621_models.ListProjectsResponse:
        """
        @summary 获取Feature Store项目列表。
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(instance_id, request, headers, runtime)

    async def list_projects_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListProjectsRequest,
    ) -> pai_feature_store_20230621_models.ListProjectsResponse:
        """
        @summary 获取Feature Store项目列表。
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(instance_id, request, headers, runtime)

    def list_task_logs_with_options(
        self,
        instance_id: str,
        task_id: str,
        request: pai_feature_store_20230621_models.ListTaskLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListTaskLogsResponse:
        """
        @summary 获取任务日志列表
        
        @param request: ListTaskLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskLogs',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListTaskLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_logs_with_options_async(
        self,
        instance_id: str,
        task_id: str,
        request: pai_feature_store_20230621_models.ListTaskLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListTaskLogsResponse:
        """
        @summary 获取任务日志列表
        
        @param request: ListTaskLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskLogs',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListTaskLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_logs(
        self,
        instance_id: str,
        task_id: str,
        request: pai_feature_store_20230621_models.ListTaskLogsRequest,
    ) -> pai_feature_store_20230621_models.ListTaskLogsResponse:
        """
        @summary 获取任务日志列表
        
        @param request: ListTaskLogsRequest
        @return: ListTaskLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_logs_with_options(instance_id, task_id, request, headers, runtime)

    async def list_task_logs_async(
        self,
        instance_id: str,
        task_id: str,
        request: pai_feature_store_20230621_models.ListTaskLogsRequest,
    ) -> pai_feature_store_20230621_models.ListTaskLogsResponse:
        """
        @summary 获取任务日志列表
        
        @param request: ListTaskLogsRequest
        @return: ListTaskLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_task_logs_with_options_async(instance_id, task_id, request, headers, runtime)

    def list_tasks_with_options(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListTasksResponse:
        """
        @summary 获取任务列表
        
        @param tmp_req: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        instance_id: str,
        tmp_req: pai_feature_store_20230621_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.ListTasksResponse:
        """
        @summary 获取任务列表
        
        @param tmp_req: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = pai_feature_store_20230621_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListTasksRequest,
    ) -> pai_feature_store_20230621_models.ListTasksResponse:
        """
        @summary 获取任务列表
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(instance_id, request, headers, runtime)

    async def list_tasks_async(
        self,
        instance_id: str,
        request: pai_feature_store_20230621_models.ListTasksRequest,
    ) -> pai_feature_store_20230621_models.ListTasksResponse:
        """
        @summary 获取任务列表
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(instance_id, request, headers, runtime)

    def publish_feature_view_table_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.PublishFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.PublishFeatureViewTableResponse:
        """
        @summary 将特征视图的离线数据发布/同步到线上。
        
        @param request: PublishFeatureViewTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishFeatureViewTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.event_time):
            body['EventTime'] = request.event_time
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.offline_to_online):
            body['OfflineToOnline'] = request.offline_to_online
        if not UtilClient.is_unset(request.partitions):
            body['Partitions'] = request.partitions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishFeatureViewTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/action/publishtable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.PublishFeatureViewTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_feature_view_table_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.PublishFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.PublishFeatureViewTableResponse:
        """
        @summary 将特征视图的离线数据发布/同步到线上。
        
        @param request: PublishFeatureViewTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishFeatureViewTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.event_time):
            body['EventTime'] = request.event_time
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.offline_to_online):
            body['OfflineToOnline'] = request.offline_to_online
        if not UtilClient.is_unset(request.partitions):
            body['Partitions'] = request.partitions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishFeatureViewTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/action/publishtable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.PublishFeatureViewTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_feature_view_table(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.PublishFeatureViewTableRequest,
    ) -> pai_feature_store_20230621_models.PublishFeatureViewTableResponse:
        """
        @summary 将特征视图的离线数据发布/同步到线上。
        
        @param request: PublishFeatureViewTableRequest
        @return: PublishFeatureViewTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_feature_view_table_with_options(instance_id, feature_view_id, request, headers, runtime)

    async def publish_feature_view_table_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.PublishFeatureViewTableRequest,
    ) -> pai_feature_store_20230621_models.PublishFeatureViewTableResponse:
        """
        @summary 将特征视图的离线数据发布/同步到线上。
        
        @param request: PublishFeatureViewTableRequest
        @return: PublishFeatureViewTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_feature_view_table_with_options_async(instance_id, feature_view_id, request, headers, runtime)

    def update_datasource_with_options(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.UpdateDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateDatasourceResponse:
        """
        @summary 更新数据源信息。
        
        @param request: UpdateDatasourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateDatasourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_datasource_with_options_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.UpdateDatasourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateDatasourceResponse:
        """
        @summary 更新数据源信息。
        
        @param request: UpdateDatasourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasourceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDatasource',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/datasources/{OpenApiUtilClient.get_encode_param(datasource_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateDatasourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_datasource(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.UpdateDatasourceRequest,
    ) -> pai_feature_store_20230621_models.UpdateDatasourceResponse:
        """
        @summary 更新数据源信息。
        
        @param request: UpdateDatasourceRequest
        @return: UpdateDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_datasource_with_options(instance_id, datasource_id, request, headers, runtime)

    async def update_datasource_async(
        self,
        instance_id: str,
        datasource_id: str,
        request: pai_feature_store_20230621_models.UpdateDatasourceRequest,
    ) -> pai_feature_store_20230621_models.UpdateDatasourceResponse:
        """
        @summary 更新数据源信息。
        
        @param request: UpdateDatasourceRequest
        @return: UpdateDatasourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_datasource_with_options_async(instance_id, datasource_id, request, headers, runtime)

    def update_label_table_with_options(
        self,
        instance_id: str,
        label_table_id: str,
        request: pai_feature_store_20230621_models.UpdateLabelTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateLabelTableResponse:
        """
        @summary 更新label表。
        
        @param request: UpdateLabelTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLabelTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateLabelTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_label_table_with_options_async(
        self,
        instance_id: str,
        label_table_id: str,
        request: pai_feature_store_20230621_models.UpdateLabelTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateLabelTableResponse:
        """
        @summary 更新label表。
        
        @param request: UpdateLabelTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLabelTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.datasource_id):
            body['DatasourceId'] = request.datasource_id
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabelTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/labeltables/{OpenApiUtilClient.get_encode_param(label_table_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateLabelTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_label_table(
        self,
        instance_id: str,
        label_table_id: str,
        request: pai_feature_store_20230621_models.UpdateLabelTableRequest,
    ) -> pai_feature_store_20230621_models.UpdateLabelTableResponse:
        """
        @summary 更新label表。
        
        @param request: UpdateLabelTableRequest
        @return: UpdateLabelTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_label_table_with_options(instance_id, label_table_id, request, headers, runtime)

    async def update_label_table_async(
        self,
        instance_id: str,
        label_table_id: str,
        request: pai_feature_store_20230621_models.UpdateLabelTableRequest,
    ) -> pai_feature_store_20230621_models.UpdateLabelTableResponse:
        """
        @summary 更新label表。
        
        @param request: UpdateLabelTableRequest
        @return: UpdateLabelTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_label_table_with_options_async(instance_id, label_table_id, request, headers, runtime)

    def update_model_feature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureResponse:
        """
        @summary 更新模型特征。
        
        @param request: UpdateModelFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.features):
            body['Features'] = request.features
        if not UtilClient.is_unset(request.label_priority_level):
            body['LabelPriorityLevel'] = request.label_priority_level
        if not UtilClient.is_unset(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not UtilClient.is_unset(request.sequence_feature_view_ids):
            body['SequenceFeatureViewIds'] = request.sequence_feature_view_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateModelFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_feature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureResponse:
        """
        @summary 更新模型特征。
        
        @param request: UpdateModelFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.features):
            body['Features'] = request.features
        if not UtilClient.is_unset(request.label_priority_level):
            body['LabelPriorityLevel'] = request.label_priority_level
        if not UtilClient.is_unset(request.label_table_id):
            body['LabelTableId'] = request.label_table_id
        if not UtilClient.is_unset(request.sequence_feature_view_ids):
            body['SequenceFeatureViewIds'] = request.sequence_feature_view_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateModelFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_feature(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureRequest,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureResponse:
        """
        @summary 更新模型特征。
        
        @param request: UpdateModelFeatureRequest
        @return: UpdateModelFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_feature_with_options(instance_id, model_feature_id, request, headers, runtime)

    async def update_model_feature_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureRequest,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureResponse:
        """
        @summary 更新模型特征。
        
        @param request: UpdateModelFeatureRequest
        @return: UpdateModelFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_model_feature_with_options_async(instance_id, model_feature_id, request, headers, runtime)

    def update_model_feature_fgfeature_with_options(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureResponse:
        """
        @summary 更新模型特征的FG特征配置信息。
        
        @param request: UpdateModelFeatureFGFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelFeatureFGFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lookup_features):
            body['LookupFeatures'] = request.lookup_features
        if not UtilClient.is_unset(request.raw_features):
            body['RawFeatures'] = request.raw_features
        if not UtilClient.is_unset(request.reserves):
            body['Reserves'] = request.reserves
        if not UtilClient.is_unset(request.sequence_features):
            body['SequenceFeatures'] = request.sequence_features
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelFeatureFGFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/fgfeature',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_feature_fgfeature_with_options_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureResponse:
        """
        @summary 更新模型特征的FG特征配置信息。
        
        @param request: UpdateModelFeatureFGFeatureRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelFeatureFGFeatureResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.lookup_features):
            body['LookupFeatures'] = request.lookup_features
        if not UtilClient.is_unset(request.raw_features):
            body['RawFeatures'] = request.raw_features
        if not UtilClient.is_unset(request.reserves):
            body['Reserves'] = request.reserves
        if not UtilClient.is_unset(request.sequence_features):
            body['SequenceFeatures'] = request.sequence_features
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelFeatureFGFeature',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/modelfeatures/{OpenApiUtilClient.get_encode_param(model_feature_id)}/fgfeature',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_feature_fgfeature(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureRequest,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureResponse:
        """
        @summary 更新模型特征的FG特征配置信息。
        
        @param request: UpdateModelFeatureFGFeatureRequest
        @return: UpdateModelFeatureFGFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_model_feature_fgfeature_with_options(instance_id, model_feature_id, request, headers, runtime)

    async def update_model_feature_fgfeature_async(
        self,
        instance_id: str,
        model_feature_id: str,
        request: pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureRequest,
    ) -> pai_feature_store_20230621_models.UpdateModelFeatureFGFeatureResponse:
        """
        @summary 更新模型特征的FG特征配置信息。
        
        @param request: UpdateModelFeatureFGFeatureRequest
        @return: UpdateModelFeatureFGFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_model_feature_fgfeature_with_options_async(instance_id, model_feature_id, request, headers, runtime)

    def update_project_with_options(
        self,
        instance_id: str,
        project_id: str,
        request: pai_feature_store_20230621_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateProjectResponse:
        """
        @summary 更新指定Feature Store项目信息。
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        instance_id: str,
        project_id: str,
        request: pai_feature_store_20230621_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.UpdateProjectResponse:
        """
        @summary 更新指定Feature Store项目信息。
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        instance_id: str,
        project_id: str,
        request: pai_feature_store_20230621_models.UpdateProjectRequest,
    ) -> pai_feature_store_20230621_models.UpdateProjectResponse:
        """
        @summary 更新指定Feature Store项目信息。
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(instance_id, project_id, request, headers, runtime)

    async def update_project_async(
        self,
        instance_id: str,
        project_id: str,
        request: pai_feature_store_20230621_models.UpdateProjectRequest,
    ) -> pai_feature_store_20230621_models.UpdateProjectResponse:
        """
        @summary 更新指定Feature Store项目信息。
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(instance_id, project_id, request, headers, runtime)

    def write_feature_view_table_with_options(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.WriteFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.WriteFeatureViewTableResponse:
        """
        @summary 获取特征视图血缘关系。
        
        @param request: WriteFeatureViewTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: WriteFeatureViewTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.partitions):
            body['Partitions'] = request.partitions
        if not UtilClient.is_unset(request.url_datasource):
            body['UrlDatasource'] = request.url_datasource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WriteFeatureViewTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/action/writetable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.WriteFeatureViewTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def write_feature_view_table_with_options_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.WriteFeatureViewTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_feature_store_20230621_models.WriteFeatureViewTableResponse:
        """
        @summary 获取特征视图血缘关系。
        
        @param request: WriteFeatureViewTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: WriteFeatureViewTableResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.partitions):
            body['Partitions'] = request.partitions
        if not UtilClient.is_unset(request.url_datasource):
            body['UrlDatasource'] = request.url_datasource
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='WriteFeatureViewTable',
            version='2023-06-21',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/featureviews/{OpenApiUtilClient.get_encode_param(feature_view_id)}/action/writetable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            pai_feature_store_20230621_models.WriteFeatureViewTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def write_feature_view_table(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.WriteFeatureViewTableRequest,
    ) -> pai_feature_store_20230621_models.WriteFeatureViewTableResponse:
        """
        @summary 获取特征视图血缘关系。
        
        @param request: WriteFeatureViewTableRequest
        @return: WriteFeatureViewTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.write_feature_view_table_with_options(instance_id, feature_view_id, request, headers, runtime)

    async def write_feature_view_table_async(
        self,
        instance_id: str,
        feature_view_id: str,
        request: pai_feature_store_20230621_models.WriteFeatureViewTableRequest,
    ) -> pai_feature_store_20230621_models.WriteFeatureViewTableResponse:
        """
        @summary 获取特征视图血缘关系。
        
        @param request: WriteFeatureViewTableRequest
        @return: WriteFeatureViewTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.write_feature_view_table_with_options_async(instance_id, feature_view_id, request, headers, runtime)
