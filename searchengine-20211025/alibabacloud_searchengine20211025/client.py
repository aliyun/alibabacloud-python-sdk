# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_searchengine20211025 import models as searchengine_20211025_models
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
        self._endpoint = self.get_endpoint('searchengine', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def build_index_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.BuildIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.BuildIndexResponse:
        """
        @summary Triggers reindexing.
        
        @description ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/actions/build-index
        
        @param request: BuildIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BuildIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_mode):
            body['buildMode'] = request.build_mode
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            body['dataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_time_sec):
            body['dataTimeSec'] = request.data_time_sec
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BuildIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/build-index',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.BuildIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def build_index_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.BuildIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.BuildIndexResponse:
        """
        @summary Triggers reindexing.
        
        @description ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/actions/build-index
        
        @param request: BuildIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: BuildIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_mode):
            body['buildMode'] = request.build_mode
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            body['dataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_time_sec):
            body['dataTimeSec'] = request.data_time_sec
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BuildIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/build-index',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.BuildIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def build_index(
        self,
        instance_id: str,
        request: searchengine_20211025_models.BuildIndexRequest,
    ) -> searchengine_20211025_models.BuildIndexResponse:
        """
        @summary Triggers reindexing.
        
        @description ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/actions/build-index
        
        @param request: BuildIndexRequest
        @return: BuildIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.build_index_with_options(instance_id, request, headers, runtime)

    async def build_index_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.BuildIndexRequest,
    ) -> searchengine_20211025_models.BuildIndexResponse:
        """
        @summary Triggers reindexing.
        
        @description ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/actions/build-index
        
        @param request: BuildIndexRequest
        @return: BuildIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.build_index_with_options_async(instance_id, request, headers, runtime)

    def change_resource_group_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ChangeResourceGroupResponse:
        """
        @summary 更换实例资源组
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['newResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/change-resource-group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ChangeResourceGroupResponse:
        """
        @summary 更换实例资源组
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['newResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/actions/change-resource-group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ChangeResourceGroupRequest,
    ) -> searchengine_20211025_models.ChangeResourceGroupResponse:
        """
        @summary 更换实例资源组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(instance_id, request, headers, runtime)

    async def change_resource_group_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ChangeResourceGroupRequest,
    ) -> searchengine_20211025_models.ChangeResourceGroupResponse:
        """
        @summary 更换实例资源组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(instance_id, request, headers, runtime)

    def clone_sql_instance_with_options(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.CloneSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CloneSqlInstanceResponse:
        """
        @param request: CloneSqlInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneSqlInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.target_folder_id):
            body['targetFolderId'] = request.target_folder_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneSqlInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}/actions/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CloneSqlInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_sql_instance_with_options_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.CloneSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CloneSqlInstanceResponse:
        """
        @param request: CloneSqlInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloneSqlInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.target_folder_id):
            body['targetFolderId'] = request.target_folder_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloneSqlInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}/actions/clone',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CloneSqlInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_sql_instance(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.CloneSqlInstanceRequest,
    ) -> searchengine_20211025_models.CloneSqlInstanceResponse:
        """
        @param request: CloneSqlInstanceRequest
        @return: CloneSqlInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.clone_sql_instance_with_options(instance_id, database, sql_instance_id, request, headers, runtime)

    async def clone_sql_instance_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.CloneSqlInstanceRequest,
    ) -> searchengine_20211025_models.CloneSqlInstanceResponse:
        """
        @param request: CloneSqlInstanceRequest
        @return: CloneSqlInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.clone_sql_instance_with_options_async(instance_id, database, sql_instance_id, request, headers, runtime)

    def create_alias_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateAliasResponse:
        """
        @param request: CreateAliasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAliasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_mode):
            query['newMode'] = request.new_mode
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.index):
            body['index'] = request.index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlias',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/aliases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alias_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateAliasResponse:
        """
        @param request: CreateAliasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAliasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_mode):
            query['newMode'] = request.new_mode
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.index):
            body['index'] = request.index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAlias',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/aliases',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alias(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateAliasRequest,
    ) -> searchengine_20211025_models.CreateAliasResponse:
        """
        @param request: CreateAliasRequest
        @return: CreateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_alias_with_options(instance_id, request, headers, runtime)

    async def create_alias_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateAliasRequest,
    ) -> searchengine_20211025_models.CreateAliasResponse:
        """
        @param request: CreateAliasRequest
        @return: CreateAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_alias_with_options_async(instance_id, request, headers, runtime)

    def create_cluster_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateClusterResponse:
        """
        @summary Creates a cluster.
        
        @description ### [](#method)Method
        `POST`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/clusters`
        
        @param request: CreateClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_load):
            body['autoLoad'] = request.auto_load
        if not UtilClient.is_unset(request.data_node):
            body['dataNode'] = request.data_node
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.query_node):
            body['queryNode'] = request.query_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateClusterResponse:
        """
        @summary Creates a cluster.
        
        @description ### [](#method)Method
        `POST`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/clusters`
        
        @param request: CreateClusterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_load):
            body['autoLoad'] = request.auto_load
        if not UtilClient.is_unset(request.data_node):
            body['dataNode'] = request.data_node
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.query_node):
            body['queryNode'] = request.query_node
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateClusterRequest,
    ) -> searchengine_20211025_models.CreateClusterResponse:
        """
        @summary Creates a cluster.
        
        @description ### [](#method)Method
        `POST`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/clusters`
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_with_options(instance_id, request, headers, runtime)

    async def create_cluster_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateClusterRequest,
    ) -> searchengine_20211025_models.CreateClusterResponse:
        """
        @summary Creates a cluster.
        
        @description ### [](#method)Method
        `POST`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/clusters`
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cluster_with_options_async(instance_id, request, headers, runtime)

    def create_config_dir_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.CreateConfigDirRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateConfigDirResponse:
        """
        @param request: CreateConfigDirRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigDirResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dir_name):
            body['dirName'] = request.dir_name
        if not UtilClient.is_unset(request.parent_full_path):
            body['parentFullPath'] = request.parent_full_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigDir',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/dir',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateConfigDirResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_dir_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.CreateConfigDirRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateConfigDirResponse:
        """
        @param request: CreateConfigDirRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigDirResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dir_name):
            body['dirName'] = request.dir_name
        if not UtilClient.is_unset(request.parent_full_path):
            body['parentFullPath'] = request.parent_full_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigDir',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/dir',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateConfigDirResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_dir(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.CreateConfigDirRequest,
    ) -> searchengine_20211025_models.CreateConfigDirResponse:
        """
        @param request: CreateConfigDirRequest
        @return: CreateConfigDirResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_config_dir_with_options(instance_id, config_name, request, headers, runtime)

    async def create_config_dir_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.CreateConfigDirRequest,
    ) -> searchengine_20211025_models.CreateConfigDirResponse:
        """
        @param request: CreateConfigDirRequest
        @return: CreateConfigDirResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_config_dir_with_options_async(instance_id, config_name, request, headers, runtime)

    def create_config_file_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.CreateConfigFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateConfigFileResponse:
        """
        @param request: CreateConfigFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.oss_path):
            body['ossPath'] = request.oss_path
        if not UtilClient.is_unset(request.parent_full_path):
            body['parentFullPath'] = request.parent_full_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/file',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateConfigFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_file_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.CreateConfigFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateConfigFileResponse:
        """
        @param request: CreateConfigFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConfigFileResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.oss_path):
            body['ossPath'] = request.oss_path
        if not UtilClient.is_unset(request.parent_full_path):
            body['parentFullPath'] = request.parent_full_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConfigFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/file',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateConfigFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config_file(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.CreateConfigFileRequest,
    ) -> searchengine_20211025_models.CreateConfigFileResponse:
        """
        @param request: CreateConfigFileRequest
        @return: CreateConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_config_file_with_options(instance_id, config_name, request, headers, runtime)

    async def create_config_file_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.CreateConfigFileRequest,
    ) -> searchengine_20211025_models.CreateConfigFileResponse:
        """
        @param request: CreateConfigFileRequest
        @return: CreateConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_config_file_with_options_async(instance_id, config_name, request, headers, runtime)

    def create_data_source_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateDataSourceResponse:
        """
        @summary Creates data sources.
        
        @param request: CreateDataSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.auto_build_index):
            body['autoBuildIndex'] = request.auto_build_index
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.saro_config):
            body['saroConfig'] = request.saro_config
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateDataSourceResponse:
        """
        @summary Creates data sources.
        
        @param request: CreateDataSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.auto_build_index):
            body['autoBuildIndex'] = request.auto_build_index
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.saro_config):
            body['saroConfig'] = request.saro_config
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_source(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateDataSourceRequest,
    ) -> searchengine_20211025_models.CreateDataSourceResponse:
        """
        @summary Creates data sources.
        
        @param request: CreateDataSourceRequest
        @return: CreateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_source_with_options(instance_id, request, headers, runtime)

    async def create_data_source_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateDataSourceRequest,
    ) -> searchengine_20211025_models.CreateDataSourceResponse:
        """
        @summary Creates data sources.
        
        @param request: CreateDataSourceRequest
        @return: CreateDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_data_source_with_options_async(instance_id, request, headers, runtime)

    def create_folder_with_options(
        self,
        instance_id: str,
        database: str,
        request: searchengine_20211025_models.CreateFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateFolderResponse:
        """
        @param request: CreateFolderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFolderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent):
            body['parent'] = request.parent
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/folders',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_folder_with_options_async(
        self,
        instance_id: str,
        database: str,
        request: searchengine_20211025_models.CreateFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateFolderResponse:
        """
        @param request: CreateFolderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFolderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent):
            body['parent'] = request.parent
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/folders',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_folder(
        self,
        instance_id: str,
        database: str,
        request: searchengine_20211025_models.CreateFolderRequest,
    ) -> searchengine_20211025_models.CreateFolderResponse:
        """
        @param request: CreateFolderRequest
        @return: CreateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_folder_with_options(instance_id, database, request, headers, runtime)

    async def create_folder_async(
        self,
        instance_id: str,
        database: str,
        request: searchengine_20211025_models.CreateFolderRequest,
    ) -> searchengine_20211025_models.CreateFolderResponse:
        """
        @param request: CreateFolderRequest
        @return: CreateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_folder_with_options_async(instance_id, database, request, headers, runtime)

    def create_index_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateIndexResponse:
        """
        @summary Creates an index.
        
        @description ### Method
        ```java
        POST
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/indexes
        ```
        
        @param request: CreateIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.build_parallel_num):
            body['buildParallelNum'] = request.build_parallel_num
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.data_source):
            body['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.data_source_info):
            body['dataSourceInfo'] = request.data_source_info
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.extend):
            body['extend'] = request.extend
        if not UtilClient.is_unset(request.merge_parallel_num):
            body['mergeParallelNum'] = request.merge_parallel_num
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_index_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateIndexResponse:
        """
        @summary Creates an index.
        
        @description ### Method
        ```java
        POST
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/indexes
        ```
        
        @param request: CreateIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.build_parallel_num):
            body['buildParallelNum'] = request.build_parallel_num
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.data_source):
            body['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.data_source_info):
            body['dataSourceInfo'] = request.data_source_info
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.extend):
            body['extend'] = request.extend
        if not UtilClient.is_unset(request.merge_parallel_num):
            body['mergeParallelNum'] = request.merge_parallel_num
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_index(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateIndexRequest,
    ) -> searchengine_20211025_models.CreateIndexResponse:
        """
        @summary Creates an index.
        
        @description ### Method
        ```java
        POST
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/indexes
        ```
        
        @param request: CreateIndexRequest
        @return: CreateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_index_with_options(instance_id, request, headers, runtime)

    async def create_index_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateIndexRequest,
    ) -> searchengine_20211025_models.CreateIndexResponse:
        """
        @summary Creates an index.
        
        @description ### Method
        ```java
        POST
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/indexes
        ```
        
        @param request: CreateIndexRequest
        @return: CreateIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_index_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: searchengine_20211025_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateInstanceResponse:
        """
        @summary Creates a Havenask instance.
        
        @description ### [](#)Method
        `POST`
        ### [](#uri)URI
        `/api/instances?dryRun=false`
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: searchengine_20211025_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateInstanceResponse:
        """
        @summary Creates a Havenask instance.
        
        @description ### [](#)Method
        `POST`
        ### [](#uri)URI
        `/api/instances?dryRun=false`
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.charge_type):
            body['chargeType'] = request.charge_type
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.order):
            body['order'] = request.order
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: searchengine_20211025_models.CreateInstanceRequest,
    ) -> searchengine_20211025_models.CreateInstanceResponse:
        """
        @summary Creates a Havenask instance.
        
        @description ### [](#)Method
        `POST`
        ### [](#uri)URI
        `/api/instances?dryRun=false`
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: searchengine_20211025_models.CreateInstanceRequest,
    ) -> searchengine_20211025_models.CreateInstanceResponse:
        """
        @summary Creates a Havenask instance.
        
        @description ### [](#)Method
        `POST`
        ### [](#uri)URI
        `/api/instances?dryRun=false`
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_public_url_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreatePublicUrlResponse:
        """
        @summary Creates a public endpoint.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePublicUrlResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreatePublicUrl',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/public-url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreatePublicUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_public_url_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreatePublicUrlResponse:
        """
        @summary Creates a public endpoint.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePublicUrlResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreatePublicUrl',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/public-url',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreatePublicUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_public_url(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.CreatePublicUrlResponse:
        """
        @summary Creates a public endpoint.
        
        @return: CreatePublicUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_public_url_with_options(instance_id, headers, runtime)

    async def create_public_url_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.CreatePublicUrlResponse:
        """
        @summary Creates a public endpoint.
        
        @return: CreatePublicUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_public_url_with_options_async(instance_id, headers, runtime)

    def create_sql_instance_with_options(
        self,
        instance_id: str,
        database: str,
        request: searchengine_20211025_models.CreateSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateSqlInstanceResponse:
        """
        @param request: CreateSqlInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSqlInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent):
            body['parent'] = request.parent
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSqlInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateSqlInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sql_instance_with_options_async(
        self,
        instance_id: str,
        database: str,
        request: searchengine_20211025_models.CreateSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateSqlInstanceResponse:
        """
        @param request: CreateSqlInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSqlInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.parent):
            body['parent'] = request.parent
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSqlInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateSqlInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sql_instance(
        self,
        instance_id: str,
        database: str,
        request: searchengine_20211025_models.CreateSqlInstanceRequest,
    ) -> searchengine_20211025_models.CreateSqlInstanceResponse:
        """
        @param request: CreateSqlInstanceRequest
        @return: CreateSqlInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_sql_instance_with_options(instance_id, database, request, headers, runtime)

    async def create_sql_instance_async(
        self,
        instance_id: str,
        database: str,
        request: searchengine_20211025_models.CreateSqlInstanceRequest,
    ) -> searchengine_20211025_models.CreateSqlInstanceResponse:
        """
        @param request: CreateSqlInstanceRequest
        @return: CreateSqlInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_sql_instance_with_options_async(instance_id, database, request, headers, runtime)

    def create_table_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateTableResponse:
        """
        @summary Creates an index table.
        
        @param request: CreateTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.data_process_config):
            body['dataProcessConfig'] = request.data_process_config
        if not UtilClient.is_unset(request.data_processor_count):
            body['dataProcessorCount'] = request.data_processor_count
        if not UtilClient.is_unset(request.data_source):
            body['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.field_schema):
            body['fieldSchema'] = request.field_schema
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.partition_count):
            body['partitionCount'] = request.partition_count
        if not UtilClient.is_unset(request.primary_key):
            body['primaryKey'] = request.primary_key
        if not UtilClient.is_unset(request.raw_schema):
            body['rawSchema'] = request.raw_schema
        if not UtilClient.is_unset(request.vector_index):
            body['vectorIndex'] = request.vector_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTable',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_table_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateTableResponse:
        """
        @summary Creates an index table.
        
        @param request: CreateTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.data_process_config):
            body['dataProcessConfig'] = request.data_process_config
        if not UtilClient.is_unset(request.data_processor_count):
            body['dataProcessorCount'] = request.data_processor_count
        if not UtilClient.is_unset(request.data_source):
            body['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.field_schema):
            body['fieldSchema'] = request.field_schema
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.partition_count):
            body['partitionCount'] = request.partition_count
        if not UtilClient.is_unset(request.primary_key):
            body['primaryKey'] = request.primary_key
        if not UtilClient.is_unset(request.raw_schema):
            body['rawSchema'] = request.raw_schema
        if not UtilClient.is_unset(request.vector_index):
            body['vectorIndex'] = request.vector_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTable',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.CreateTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_table(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateTableRequest,
    ) -> searchengine_20211025_models.CreateTableResponse:
        """
        @summary Creates an index table.
        
        @param request: CreateTableRequest
        @return: CreateTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_table_with_options(instance_id, request, headers, runtime)

    async def create_table_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateTableRequest,
    ) -> searchengine_20211025_models.CreateTableResponse:
        """
        @summary Creates an index table.
        
        @param request: CreateTableRequest
        @return: CreateTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_table_with_options_async(instance_id, request, headers, runtime)

    def delete_advance_config_with_options(
        self,
        instance_id: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteAdvanceConfigResponse:
        """
        @summary Deletes the details about advanced configurations.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAdvanceConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteAdvanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_advance_config_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteAdvanceConfigResponse:
        """
        @summary Deletes the details about advanced configurations.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAdvanceConfigResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteAdvanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_advance_config(
        self,
        instance_id: str,
        config_name: str,
    ) -> searchengine_20211025_models.DeleteAdvanceConfigResponse:
        """
        @summary Deletes the details about advanced configurations.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        
        @return: DeleteAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_advance_config_with_options(instance_id, config_name, headers, runtime)

    async def delete_advance_config_async(
        self,
        instance_id: str,
        config_name: str,
    ) -> searchengine_20211025_models.DeleteAdvanceConfigResponse:
        """
        @summary Deletes the details about advanced configurations.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        
        @return: DeleteAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_advance_config_with_options_async(instance_id, config_name, headers, runtime)

    def delete_alias_with_options(
        self,
        instance_id: str,
        alias: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteAliasResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAliasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlias',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/aliases/{OpenApiUtilClient.get_encode_param(alias)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alias_with_options_async(
        self,
        instance_id: str,
        alias: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteAliasResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAliasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteAlias',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/aliases/{OpenApiUtilClient.get_encode_param(alias)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alias(
        self,
        instance_id: str,
        alias: str,
    ) -> searchengine_20211025_models.DeleteAliasResponse:
        """
        @return: DeleteAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_alias_with_options(instance_id, alias, headers, runtime)

    async def delete_alias_async(
        self,
        instance_id: str,
        alias: str,
    ) -> searchengine_20211025_models.DeleteAliasResponse:
        """
        @return: DeleteAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_alias_with_options_async(instance_id, alias, headers, runtime)

    def delete_config_dir_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.DeleteConfigDirRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteConfigDirResponse:
        """
        @param request: DeleteConfigDirRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigDirResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dir_name):
            query['dirName'] = request.dir_name
        if not UtilClient.is_unset(request.parent_full_path):
            query['parentFullPath'] = request.parent_full_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigDir',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/dir',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteConfigDirResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_dir_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.DeleteConfigDirRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteConfigDirResponse:
        """
        @param request: DeleteConfigDirRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigDirResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dir_name):
            query['dirName'] = request.dir_name
        if not UtilClient.is_unset(request.parent_full_path):
            query['parentFullPath'] = request.parent_full_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigDir',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/dir',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteConfigDirResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_dir(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.DeleteConfigDirRequest,
    ) -> searchengine_20211025_models.DeleteConfigDirResponse:
        """
        @param request: DeleteConfigDirRequest
        @return: DeleteConfigDirResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_dir_with_options(instance_id, config_name, request, headers, runtime)

    async def delete_config_dir_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.DeleteConfigDirRequest,
    ) -> searchengine_20211025_models.DeleteConfigDirResponse:
        """
        @param request: DeleteConfigDirRequest
        @return: DeleteConfigDirResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_config_dir_with_options_async(instance_id, config_name, request, headers, runtime)

    def delete_config_file_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.DeleteConfigFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteConfigFileResponse:
        """
        @param request: DeleteConfigFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.parent_full_path):
            query['parentFullPath'] = request.parent_full_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/file',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteConfigFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_file_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.DeleteConfigFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteConfigFileResponse:
        """
        @param request: DeleteConfigFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteConfigFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.parent_full_path):
            query['parentFullPath'] = request.parent_full_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConfigFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/file',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteConfigFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_file(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.DeleteConfigFileRequest,
    ) -> searchengine_20211025_models.DeleteConfigFileResponse:
        """
        @param request: DeleteConfigFileRequest
        @return: DeleteConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_config_file_with_options(instance_id, config_name, request, headers, runtime)

    async def delete_config_file_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.DeleteConfigFileRequest,
    ) -> searchengine_20211025_models.DeleteConfigFileResponse:
        """
        @param request: DeleteConfigFileRequest
        @return: DeleteConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_config_file_with_options_async(instance_id, config_name, request, headers, runtime)

    def delete_data_source_with_options(
        self,
        instance_id: str,
        data_source_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteDataSourceResponse:
        """
        @summary Deletes a specified data source.
        
        @description ## Method
        `DELETE`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        instance_id: str,
        data_source_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteDataSourceResponse:
        """
        @summary Deletes a specified data source.
        
        @description ## Method
        `DELETE`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        instance_id: str,
        data_source_name: str,
    ) -> searchengine_20211025_models.DeleteDataSourceResponse:
        """
        @summary Deletes a specified data source.
        
        @description ## Method
        `DELETE`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_data_source_with_options(instance_id, data_source_name, headers, runtime)

    async def delete_data_source_async(
        self,
        instance_id: str,
        data_source_name: str,
    ) -> searchengine_20211025_models.DeleteDataSourceResponse:
        """
        @summary Deletes a specified data source.
        
        @description ## Method
        `DELETE`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_data_source_with_options_async(instance_id, data_source_name, headers, runtime)

    def delete_folder_with_options(
        self,
        instance_id: str,
        database: str,
        folder_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteFolderResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFolderResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/folders/{OpenApiUtilClient.get_encode_param(folder_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        instance_id: str,
        database: str,
        folder_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteFolderResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFolderResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/folders/{OpenApiUtilClient.get_encode_param(folder_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_folder(
        self,
        instance_id: str,
        database: str,
        folder_id: str,
    ) -> searchengine_20211025_models.DeleteFolderResponse:
        """
        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_folder_with_options(instance_id, database, folder_id, headers, runtime)

    async def delete_folder_async(
        self,
        instance_id: str,
        database: str,
        folder_id: str,
    ) -> searchengine_20211025_models.DeleteFolderResponse:
        """
        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_folder_with_options_async(instance_id, database, folder_id, headers, runtime)

    def delete_index_with_options(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.DeleteIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteIndexResponse:
        """
        @summary Deletes an index.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}?dataSource=xxx
        
        @param request: DeleteIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source):
            query['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.delete_data_source):
            query['deleteDataSource'] = request.delete_data_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_index_with_options_async(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.DeleteIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteIndexResponse:
        """
        @summary Deletes an index.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}?dataSource=xxx
        
        @param request: DeleteIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source):
            query['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.delete_data_source):
            query['deleteDataSource'] = request.delete_data_source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_index(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.DeleteIndexRequest,
    ) -> searchengine_20211025_models.DeleteIndexResponse:
        """
        @summary Deletes an index.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}?dataSource=xxx
        
        @param request: DeleteIndexRequest
        @return: DeleteIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_with_options(instance_id, index_name, request, headers, runtime)

    async def delete_index_async(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.DeleteIndexRequest,
    ) -> searchengine_20211025_models.DeleteIndexResponse:
        """
        @summary Deletes an index.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}?dataSource=xxx
        
        @param request: DeleteIndexRequest
        @return: DeleteIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_index_with_options_async(instance_id, index_name, request, headers, runtime)

    def delete_index_version_with_options(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteIndexVersionResponse:
        """
        @summary Deletes the version of an index.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndexVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteIndexVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_index_version_with_options_async(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteIndexVersionResponse:
        """
        @summary Deletes the version of an index.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIndexVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteIndexVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_index_version(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
    ) -> searchengine_20211025_models.DeleteIndexVersionResponse:
        """
        @summary Deletes the version of an index.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}
        
        @return: DeleteIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_index_version_with_options(instance_id, index_name, version_name, headers, runtime)

    async def delete_index_version_async(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
    ) -> searchengine_20211025_models.DeleteIndexVersionResponse:
        """
        @summary Deletes the version of an index.
        
        @description ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}
        
        @return: DeleteIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_index_version_with_options_async(instance_id, index_name, version_name, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteInstanceResponse:
        """
        @summary Deletes a specified instance.
        
        @description ### Method
        `DELETE`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteInstanceResponse:
        """
        @summary Deletes a specified instance.
        
        @description ### Method
        `DELETE`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.DeleteInstanceResponse:
        """
        @summary Deletes a specified instance.
        
        @description ### Method
        `DELETE`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.DeleteInstanceResponse:
        """
        @summary Deletes a specified instance.
        
        @description ### Method
        `DELETE`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, headers, runtime)

    def delete_public_url_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeletePublicUrlResponse:
        """
        @summary 删除公网域名
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePublicUrlResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePublicUrl',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/public-url',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeletePublicUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_public_url_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeletePublicUrlResponse:
        """
        @summary 删除公网域名
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePublicUrlResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeletePublicUrl',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/public-url',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeletePublicUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_public_url(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.DeletePublicUrlResponse:
        """
        @summary 删除公网域名
        
        @return: DeletePublicUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_public_url_with_options(instance_id, headers, runtime)

    async def delete_public_url_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.DeletePublicUrlResponse:
        """
        @summary 删除公网域名
        
        @return: DeletePublicUrlResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_public_url_with_options_async(instance_id, headers, runtime)

    def delete_sql_instance_with_options(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteSqlInstanceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSqlInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSqlInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteSqlInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sql_instance_with_options_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteSqlInstanceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSqlInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteSqlInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteSqlInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sql_instance(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
    ) -> searchengine_20211025_models.DeleteSqlInstanceResponse:
        """
        @return: DeleteSqlInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_sql_instance_with_options(instance_id, database, sql_instance_id, headers, runtime)

    async def delete_sql_instance_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
    ) -> searchengine_20211025_models.DeleteSqlInstanceResponse:
        """
        @return: DeleteSqlInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_sql_instance_with_options_async(instance_id, database, sql_instance_id, headers, runtime)

    def delete_table_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteTableResponse:
        """
        @summary Deletes an index table.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTable',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_table_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteTableResponse:
        """
        @summary Deletes an index table.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTable',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DeleteTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_table(
        self,
        instance_id: str,
        table_name: str,
    ) -> searchengine_20211025_models.DeleteTableResponse:
        """
        @summary Deletes an index table.
        
        @return: DeleteTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_table_with_options(instance_id, table_name, headers, runtime)

    async def delete_table_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> searchengine_20211025_models.DeleteTableResponse:
        """
        @summary Deletes an index table.
        
        @return: DeleteTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_table_with_options_async(instance_id, table_name, headers, runtime)

    def describe_regions_with_options(
        self,
        request: searchengine_20211025_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param request: DescribeRegionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: searchengine_20211025_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param request: DescribeRegionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/regions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: searchengine_20211025_models.DescribeRegionsRequest,
    ) -> searchengine_20211025_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: searchengine_20211025_models.DescribeRegionsRequest,
    ) -> searchengine_20211025_models.DescribeRegionsResponse:
        """
        @summary Queries available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def execute_sql_instance_with_options(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.ExecuteSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ExecuteSqlInstanceResponse:
        """
        @param request: ExecuteSqlInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSqlInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.combine_param):
            body['combineParam'] = request.combine_param
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.dynamic_param):
            body['dynamicParam'] = request.dynamic_param
        if not UtilClient.is_unset(request.kvpair):
            body['kvpair'] = request.kvpair
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.static_param):
            body['staticParam'] = request.static_param
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteSqlInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}/actions/execution',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ExecuteSqlInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_sql_instance_with_options_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.ExecuteSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ExecuteSqlInstanceResponse:
        """
        @param request: ExecuteSqlInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteSqlInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.combine_param):
            body['combineParam'] = request.combine_param
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.dynamic_param):
            body['dynamicParam'] = request.dynamic_param
        if not UtilClient.is_unset(request.kvpair):
            body['kvpair'] = request.kvpair
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.static_param):
            body['staticParam'] = request.static_param
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteSqlInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}/actions/execution',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ExecuteSqlInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_sql_instance(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.ExecuteSqlInstanceRequest,
    ) -> searchengine_20211025_models.ExecuteSqlInstanceResponse:
        """
        @param request: ExecuteSqlInstanceRequest
        @return: ExecuteSqlInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_sql_instance_with_options(instance_id, database, sql_instance_id, request, headers, runtime)

    async def execute_sql_instance_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.ExecuteSqlInstanceRequest,
    ) -> searchengine_20211025_models.ExecuteSqlInstanceResponse:
        """
        @param request: ExecuteSqlInstanceRequest
        @return: ExecuteSqlInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_sql_instance_with_options_async(instance_id, database, sql_instance_id, request, headers, runtime)

    def force_switch_with_options(
        self,
        instance_id: str,
        fsm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ForceSwitchResponse:
        """
        @summary Performs a forced switchover.
        
        @description ### [](#)Method
        ```java
        PUT
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/force-switch/{fsmId}
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ForceSwitchResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ForceSwitch',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/force-switch/{OpenApiUtilClient.get_encode_param(fsm_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ForceSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def force_switch_with_options_async(
        self,
        instance_id: str,
        fsm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ForceSwitchResponse:
        """
        @summary Performs a forced switchover.
        
        @description ### [](#)Method
        ```java
        PUT
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/force-switch/{fsmId}
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ForceSwitchResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ForceSwitch',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/force-switch/{OpenApiUtilClient.get_encode_param(fsm_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ForceSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def force_switch(
        self,
        instance_id: str,
        fsm_id: str,
    ) -> searchengine_20211025_models.ForceSwitchResponse:
        """
        @summary Performs a forced switchover.
        
        @description ### [](#)Method
        ```java
        PUT
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/force-switch/{fsmId}
        ```
        
        @return: ForceSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.force_switch_with_options(instance_id, fsm_id, headers, runtime)

    async def force_switch_async(
        self,
        instance_id: str,
        fsm_id: str,
    ) -> searchengine_20211025_models.ForceSwitchResponse:
        """
        @summary Performs a forced switchover.
        
        @description ### [](#)Method
        ```java
        PUT
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/force-switch/{fsmId}
        ```
        
        @return: ForceSwitchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.force_switch_with_options_async(instance_id, fsm_id, headers, runtime)

    def get_advance_config_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.GetAdvanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetAdvanceConfigResponse:
        """
        @summary Queries the information about an advanced configuration.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        
        @param request: GetAdvanceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdvanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetAdvanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_advance_config_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.GetAdvanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetAdvanceConfigResponse:
        """
        @summary Queries the information about an advanced configuration.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        
        @param request: GetAdvanceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdvanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetAdvanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_advance_config(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.GetAdvanceConfigRequest,
    ) -> searchengine_20211025_models.GetAdvanceConfigResponse:
        """
        @summary Queries the information about an advanced configuration.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        
        @param request: GetAdvanceConfigRequest
        @return: GetAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_advance_config_with_options(instance_id, config_name, request, headers, runtime)

    async def get_advance_config_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.GetAdvanceConfigRequest,
    ) -> searchengine_20211025_models.GetAdvanceConfigResponse:
        """
        @summary Queries the information about an advanced configuration.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        
        @param request: GetAdvanceConfigRequest
        @return: GetAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_advance_config_with_options_async(instance_id, config_name, request, headers, runtime)

    def get_advance_config_file_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.GetAdvanceConfigFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetAdvanceConfigFileResponse:
        """
        @summary Queries the information about an advanced configuration file.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        
        @param request: GetAdvanceConfigFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdvanceConfigFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdvanceConfigFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/file',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetAdvanceConfigFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_advance_config_file_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.GetAdvanceConfigFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetAdvanceConfigFileResponse:
        """
        @summary Queries the information about an advanced configuration file.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        
        @param request: GetAdvanceConfigFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAdvanceConfigFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAdvanceConfigFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/file',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetAdvanceConfigFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_advance_config_file(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.GetAdvanceConfigFileRequest,
    ) -> searchengine_20211025_models.GetAdvanceConfigFileResponse:
        """
        @summary Queries the information about an advanced configuration file.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        
        @param request: GetAdvanceConfigFileRequest
        @return: GetAdvanceConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_advance_config_file_with_options(instance_id, config_name, request, headers, runtime)

    async def get_advance_config_file_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.GetAdvanceConfigFileRequest,
    ) -> searchengine_20211025_models.GetAdvanceConfigFileResponse:
        """
        @summary Queries the information about an advanced configuration file.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        
        @param request: GetAdvanceConfigFileRequest
        @return: GetAdvanceConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_advance_config_file_with_options_async(instance_id, config_name, request, headers, runtime)

    def get_cluster_with_options(
        self,
        instance_id: str,
        cluster_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetClusterResponse:
        """
        @summary Queries the details of a cluster.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instance/{instanceId}/clusters/{clusterName}`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters/{OpenApiUtilClient.get_encode_param(cluster_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        instance_id: str,
        cluster_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetClusterResponse:
        """
        @summary Queries the details of a cluster.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instance/{instanceId}/clusters/{clusterName}`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters/{OpenApiUtilClient.get_encode_param(cluster_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        instance_id: str,
        cluster_name: str,
    ) -> searchengine_20211025_models.GetClusterResponse:
        """
        @summary Queries the details of a cluster.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instance/{instanceId}/clusters/{clusterName}`
        
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_with_options(instance_id, cluster_name, headers, runtime)

    async def get_cluster_async(
        self,
        instance_id: str,
        cluster_name: str,
    ) -> searchengine_20211025_models.GetClusterResponse:
        """
        @summary Queries the details of a cluster.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instance/{instanceId}/clusters/{clusterName}`
        
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_with_options_async(instance_id, cluster_name, headers, runtime)

    def get_cluster_run_time_info_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetClusterRunTimeInfoResponse:
        """
        @summary Queries the runtime information about a specified cluster.
        
        @description ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-run-time-info
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterRunTimeInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterRunTimeInfo',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/cluster-run-time-info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetClusterRunTimeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_run_time_info_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetClusterRunTimeInfoResponse:
        """
        @summary Queries the runtime information about a specified cluster.
        
        @description ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-run-time-info
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterRunTimeInfoResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetClusterRunTimeInfo',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/cluster-run-time-info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetClusterRunTimeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_run_time_info(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.GetClusterRunTimeInfoResponse:
        """
        @summary Queries the runtime information about a specified cluster.
        
        @description ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-run-time-info
        
        @return: GetClusterRunTimeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_run_time_info_with_options(instance_id, headers, runtime)

    async def get_cluster_run_time_info_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.GetClusterRunTimeInfoResponse:
        """
        @summary Queries the runtime information about a specified cluster.
        
        @description ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-run-time-info
        
        @return: GetClusterRunTimeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_run_time_info_with_options_async(instance_id, headers, runtime)

    def get_data_source_with_options(
        self,
        instance_id: str,
        data_source_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetDataSourceResponse:
        """
        @summary Obtains a data source.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_with_options_async(
        self,
        instance_id: str,
        data_source_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetDataSourceResponse:
        """
        @summary Obtains a data source.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataSourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source(
        self,
        instance_id: str,
        data_source_name: str,
    ) -> searchengine_20211025_models.GetDataSourceResponse:
        """
        @summary Obtains a data source.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @return: GetDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_source_with_options(instance_id, data_source_name, headers, runtime)

    async def get_data_source_async(
        self,
        instance_id: str,
        data_source_name: str,
    ) -> searchengine_20211025_models.GetDataSourceResponse:
        """
        @summary Obtains a data source.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @return: GetDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_data_source_with_options_async(instance_id, data_source_name, headers, runtime)

    def get_data_source_deploy_with_options(
        self,
        instance_id: str,
        deploy_name: str,
        data_source_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetDataSourceDeployResponse:
        """
        @summary 获取数据源部署信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataSourceDeployResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataSourceDeploy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/deploys/{OpenApiUtilClient.get_encode_param(deploy_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDataSourceDeployResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_source_deploy_with_options_async(
        self,
        instance_id: str,
        deploy_name: str,
        data_source_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetDataSourceDeployResponse:
        """
        @summary 获取数据源部署信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataSourceDeployResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDataSourceDeploy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/deploys/{OpenApiUtilClient.get_encode_param(deploy_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDataSourceDeployResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_source_deploy(
        self,
        instance_id: str,
        deploy_name: str,
        data_source_name: str,
    ) -> searchengine_20211025_models.GetDataSourceDeployResponse:
        """
        @summary 获取数据源部署信息
        
        @return: GetDataSourceDeployResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_source_deploy_with_options(instance_id, deploy_name, data_source_name, headers, runtime)

    async def get_data_source_deploy_async(
        self,
        instance_id: str,
        deploy_name: str,
        data_source_name: str,
    ) -> searchengine_20211025_models.GetDataSourceDeployResponse:
        """
        @summary 获取数据源部署信息
        
        @return: GetDataSourceDeployResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_data_source_deploy_with_options_async(instance_id, deploy_name, data_source_name, headers, runtime)

    def get_database_schema_with_options(
        self,
        instance_id: str,
        database: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetDatabaseSchemaResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabaseSchemaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatabaseSchema',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/schema',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDatabaseSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_schema_with_options_async(
        self,
        instance_id: str,
        database: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetDatabaseSchemaResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatabaseSchemaResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDatabaseSchema',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/schema',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDatabaseSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database_schema(
        self,
        instance_id: str,
        database: str,
        table_name: str,
    ) -> searchengine_20211025_models.GetDatabaseSchemaResponse:
        """
        @return: GetDatabaseSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_database_schema_with_options(instance_id, database, table_name, headers, runtime)

    async def get_database_schema_async(
        self,
        instance_id: str,
        database: str,
        table_name: str,
    ) -> searchengine_20211025_models.GetDatabaseSchemaResponse:
        """
        @return: GetDatabaseSchemaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_database_schema_with_options_async(instance_id, database, table_name, headers, runtime)

    def get_deploy_graph_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetDeployGraphResponse:
        """
        @summary Displays the overview of the deployment.
        
        @description ## Method
        GET
        ## URI
        ```java
        /openapi/ha3/instances/{instanceId}/deploy-graph
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeployGraphResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDeployGraph',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/deploy-graph',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDeployGraphResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deploy_graph_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetDeployGraphResponse:
        """
        @summary Displays the overview of the deployment.
        
        @description ## Method
        GET
        ## URI
        ```java
        /openapi/ha3/instances/{instanceId}/deploy-graph
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeployGraphResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetDeployGraph',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/deploy-graph',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetDeployGraphResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deploy_graph(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.GetDeployGraphResponse:
        """
        @summary Displays the overview of the deployment.
        
        @description ## Method
        GET
        ## URI
        ```java
        /openapi/ha3/instances/{instanceId}/deploy-graph
        ```
        
        @return: GetDeployGraphResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_deploy_graph_with_options(instance_id, headers, runtime)

    async def get_deploy_graph_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.GetDeployGraphResponse:
        """
        @summary Displays the overview of the deployment.
        
        @description ## Method
        GET
        ## URI
        ```java
        /openapi/ha3/instances/{instanceId}/deploy-graph
        ```
        
        @return: GetDeployGraphResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_deploy_graph_with_options_async(instance_id, headers, runtime)

    def get_file_with_options(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
        request: searchengine_20211025_models.GetFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetFileResponse:
        """
        @summary Queries the details of an index table version.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        
        @param request: GetFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/file',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_with_options_async(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
        request: searchengine_20211025_models.GetFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetFileResponse:
        """
        @summary Queries the details of an index table version.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        
        @param request: GetFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/file',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
        request: searchengine_20211025_models.GetFileRequest,
    ) -> searchengine_20211025_models.GetFileResponse:
        """
        @summary Queries the details of an index table version.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        
        @param request: GetFileRequest
        @return: GetFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_file_with_options(instance_id, index_name, version_name, request, headers, runtime)

    async def get_file_async(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
        request: searchengine_20211025_models.GetFileRequest,
    ) -> searchengine_20211025_models.GetFileResponse:
        """
        @summary Queries the details of an index table version.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        
        @param request: GetFileRequest
        @return: GetFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_file_with_options_async(instance_id, index_name, version_name, request, headers, runtime)

    def get_index_with_options(
        self,
        instance_id: str,
        index_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetIndexResponse:
        """
        @summary Queries the information about an index version.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_with_options_async(
        self,
        instance_id: str,
        index_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetIndexResponse:
        """
        @summary Queries the information about an index version.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index(
        self,
        instance_id: str,
        index_name: str,
    ) -> searchengine_20211025_models.GetIndexResponse:
        """
        @summary Queries the information about an index version.
        
        @return: GetIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_with_options(instance_id, index_name, headers, runtime)

    async def get_index_async(
        self,
        instance_id: str,
        index_name: str,
    ) -> searchengine_20211025_models.GetIndexResponse:
        """
        @summary Queries the information about an index version.
        
        @return: GetIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_index_with_options_async(instance_id, index_name, headers, runtime)

    def get_index_online_strategy_with_options(
        self,
        instance_id: str,
        data_source_name: str,
        deploy_name: str,
        index_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetIndexOnlineStrategyResponse:
        """
        @summary Queries the online effective policy of an index.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexOnlineStrategyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndexOnlineStrategy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/deploys/{OpenApiUtilClient.get_encode_param(deploy_name)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/online-strategy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetIndexOnlineStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_online_strategy_with_options_async(
        self,
        instance_id: str,
        data_source_name: str,
        deploy_name: str,
        index_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetIndexOnlineStrategyResponse:
        """
        @summary Queries the online effective policy of an index.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexOnlineStrategyResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndexOnlineStrategy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/deploys/{OpenApiUtilClient.get_encode_param(deploy_name)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/online-strategy',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetIndexOnlineStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index_online_strategy(
        self,
        instance_id: str,
        data_source_name: str,
        deploy_name: str,
        index_name: str,
    ) -> searchengine_20211025_models.GetIndexOnlineStrategyResponse:
        """
        @summary Queries the online effective policy of an index.
        
        @return: GetIndexOnlineStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_online_strategy_with_options(instance_id, data_source_name, deploy_name, index_name, headers, runtime)

    async def get_index_online_strategy_async(
        self,
        instance_id: str,
        data_source_name: str,
        deploy_name: str,
        index_name: str,
    ) -> searchengine_20211025_models.GetIndexOnlineStrategyResponse:
        """
        @summary Queries the online effective policy of an index.
        
        @return: GetIndexOnlineStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_index_online_strategy_with_options_async(instance_id, data_source_name, deploy_name, index_name, headers, runtime)

    def get_index_version_with_options(
        self,
        instance_id: str,
        cluster_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetIndexVersionResponse:
        """
        @summary Queries the information about index versions that the current index version can be rolled back to.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters/{OpenApiUtilClient.get_encode_param(cluster_name)}/index-version',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetIndexVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_index_version_with_options_async(
        self,
        instance_id: str,
        cluster_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetIndexVersionResponse:
        """
        @summary Queries the information about index versions that the current index version can be rolled back to.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIndexVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters/{OpenApiUtilClient.get_encode_param(cluster_name)}/index-version',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetIndexVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_index_version(
        self,
        instance_id: str,
        cluster_name: str,
    ) -> searchengine_20211025_models.GetIndexVersionResponse:
        """
        @summary Queries the information about index versions that the current index version can be rolled back to.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        
        @return: GetIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_version_with_options(instance_id, cluster_name, headers, runtime)

    async def get_index_version_async(
        self,
        instance_id: str,
        cluster_name: str,
    ) -> searchengine_20211025_models.GetIndexVersionResponse:
        """
        @summary Queries the information about index versions that the current index version can be rolled back to.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        
        @return: GetIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_index_version_with_options_async(instance_id, cluster_name, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetInstanceResponse:
        """
        @summary Queries the details of an instance based on the instance ID.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetInstanceResponse:
        """
        @summary Queries the details of an instance based on the instance ID.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.GetInstanceResponse:
        """
        @summary Queries the details of an instance based on the instance ID.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.GetInstanceResponse:
        """
        @summary Queries the details of an instance based on the instance ID.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_node_config_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.GetNodeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetNodeConfigResponse:
        """
        @summary Gets the configuration information of a node.
        
        @param request: GetNodeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['clusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/node-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetNodeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_config_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.GetNodeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetNodeConfigResponse:
        """
        @summary Gets the configuration information of a node.
        
        @param request: GetNodeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['clusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/node-config',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetNodeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_config(
        self,
        instance_id: str,
        request: searchengine_20211025_models.GetNodeConfigRequest,
    ) -> searchengine_20211025_models.GetNodeConfigResponse:
        """
        @summary Gets the configuration information of a node.
        
        @param request: GetNodeConfigRequest
        @return: GetNodeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_config_with_options(instance_id, request, headers, runtime)

    async def get_node_config_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.GetNodeConfigRequest,
    ) -> searchengine_20211025_models.GetNodeConfigResponse:
        """
        @summary Gets the configuration information of a node.
        
        @param request: GetNodeConfigRequest
        @return: GetNodeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_node_config_with_options_async(instance_id, request, headers, runtime)

    def get_sql_instance_with_options(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.GetSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetSqlInstanceResponse:
        """
        @param request: GetSqlInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetSqlInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_instance_with_options_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.GetSqlInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetSqlInstanceResponse:
        """
        @param request: GetSqlInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSqlInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version):
            query['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSqlInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetSqlInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_instance(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.GetSqlInstanceRequest,
    ) -> searchengine_20211025_models.GetSqlInstanceResponse:
        """
        @param request: GetSqlInstanceRequest
        @return: GetSqlInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sql_instance_with_options(instance_id, database, sql_instance_id, request, headers, runtime)

    async def get_sql_instance_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.GetSqlInstanceRequest,
    ) -> searchengine_20211025_models.GetSqlInstanceResponse:
        """
        @param request: GetSqlInstanceRequest
        @return: GetSqlInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sql_instance_with_options_async(instance_id, database, sql_instance_id, request, headers, runtime)

    def get_table_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetTableResponse:
        """
        @summary Queries the information about an index table.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTable',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetTableResponse:
        """
        @summary Queries the information about an index table.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTable',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table(
        self,
        instance_id: str,
        table_name: str,
    ) -> searchengine_20211025_models.GetTableResponse:
        """
        @summary Queries the information about an index table.
        
        @return: GetTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_with_options(instance_id, table_name, headers, runtime)

    async def get_table_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> searchengine_20211025_models.GetTableResponse:
        """
        @summary Queries the information about an index table.
        
        @return: GetTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_with_options_async(instance_id, table_name, headers, runtime)

    def get_table_generation_with_options(
        self,
        instance_id: str,
        table_name: str,
        generation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetTableGenerationResponse:
        """
        @summary Queries the status of an index version based on the ID of the full index version.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableGenerationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTableGeneration',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/index_versions/{OpenApiUtilClient.get_encode_param(generation_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetTableGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_generation_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        generation_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetTableGenerationResponse:
        """
        @summary Queries the status of an index version based on the ID of the full index version.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTableGenerationResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTableGeneration',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/index_versions/{OpenApiUtilClient.get_encode_param(generation_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.GetTableGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_generation(
        self,
        instance_id: str,
        table_name: str,
        generation_id: str,
    ) -> searchengine_20211025_models.GetTableGenerationResponse:
        """
        @summary Queries the status of an index version based on the ID of the full index version.
        
        @return: GetTableGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_table_generation_with_options(instance_id, table_name, generation_id, headers, runtime)

    async def get_table_generation_async(
        self,
        instance_id: str,
        table_name: str,
        generation_id: str,
    ) -> searchengine_20211025_models.GetTableGenerationResponse:
        """
        @summary Queries the status of an index version based on the ID of the full index version.
        
        @return: GetTableGenerationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_table_generation_with_options_async(instance_id, table_name, generation_id, headers, runtime)

    def list_advance_config_dir_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ListAdvanceConfigDirRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListAdvanceConfigDirResponse:
        """
        @summary Queries the files in an advanced configuration directory.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/dir?dirName={dirName}`
        
        @param request: ListAdvanceConfigDirRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAdvanceConfigDirResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dir_name):
            query['dirName'] = request.dir_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdvanceConfigDir',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/dir',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListAdvanceConfigDirResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_advance_config_dir_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ListAdvanceConfigDirRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListAdvanceConfigDirResponse:
        """
        @summary Queries the files in an advanced configuration directory.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/dir?dirName={dirName}`
        
        @param request: ListAdvanceConfigDirRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAdvanceConfigDirResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dir_name):
            query['dirName'] = request.dir_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdvanceConfigDir',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/dir',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListAdvanceConfigDirResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_advance_config_dir(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ListAdvanceConfigDirRequest,
    ) -> searchengine_20211025_models.ListAdvanceConfigDirResponse:
        """
        @summary Queries the files in an advanced configuration directory.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/dir?dirName={dirName}`
        
        @param request: ListAdvanceConfigDirRequest
        @return: ListAdvanceConfigDirResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_advance_config_dir_with_options(instance_id, config_name, request, headers, runtime)

    async def list_advance_config_dir_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ListAdvanceConfigDirRequest,
    ) -> searchengine_20211025_models.ListAdvanceConfigDirResponse:
        """
        @summary Queries the files in an advanced configuration directory.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/dir?dirName={dirName}`
        
        @param request: ListAdvanceConfigDirRequest
        @return: ListAdvanceConfigDirResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_advance_config_dir_with_options_async(instance_id, config_name, request, headers, runtime)

    def list_advance_configs_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListAdvanceConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListAdvanceConfigsResponse:
        """
        @summary Obtains a list of advanced configurations.
        
        @description ## Sample requests
        `GET /openapi/ha3/instances/ose-test1/advanced-configs`
        
        @param request: ListAdvanceConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAdvanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_name):
            query['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.index_name):
            query['indexName'] = request.index_name
        if not UtilClient.is_unset(request.new_mode):
            query['newMode'] = request.new_mode
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdvanceConfigs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListAdvanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_advance_configs_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListAdvanceConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListAdvanceConfigsResponse:
        """
        @summary Obtains a list of advanced configurations.
        
        @description ## Sample requests
        `GET /openapi/ha3/instances/ose-test1/advanced-configs`
        
        @param request: ListAdvanceConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAdvanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_name):
            query['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.index_name):
            query['indexName'] = request.index_name
        if not UtilClient.is_unset(request.new_mode):
            query['newMode'] = request.new_mode
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAdvanceConfigs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListAdvanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_advance_configs(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListAdvanceConfigsRequest,
    ) -> searchengine_20211025_models.ListAdvanceConfigsResponse:
        """
        @summary Obtains a list of advanced configurations.
        
        @description ## Sample requests
        `GET /openapi/ha3/instances/ose-test1/advanced-configs`
        
        @param request: ListAdvanceConfigsRequest
        @return: ListAdvanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_advance_configs_with_options(instance_id, request, headers, runtime)

    async def list_advance_configs_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListAdvanceConfigsRequest,
    ) -> searchengine_20211025_models.ListAdvanceConfigsResponse:
        """
        @summary Obtains a list of advanced configurations.
        
        @description ## Sample requests
        `GET /openapi/ha3/instances/ose-test1/advanced-configs`
        
        @param request: ListAdvanceConfigsRequest
        @return: ListAdvanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_advance_configs_with_options_async(instance_id, request, headers, runtime)

    def list_aliases_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListAliasesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliasesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAliases',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/aliases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aliases_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListAliasesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAliasesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListAliases',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/aliases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListAliasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aliases(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListAliasesResponse:
        """
        @return: ListAliasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_aliases_with_options(instance_id, headers, runtime)

    async def list_aliases_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListAliasesResponse:
        """
        @return: ListAliasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_aliases_with_options_async(instance_id, headers, runtime)

    def list_cluster_names_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListClusterNamesResponse:
        """
        @summary Queries cluster names.
        
        @description ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-names
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterNamesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusterNames',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/cluster-names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListClusterNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_names_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListClusterNamesResponse:
        """
        @summary Queries cluster names.
        
        @description ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-names
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterNamesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusterNames',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/cluster-names',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListClusterNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_names(self) -> searchengine_20211025_models.ListClusterNamesResponse:
        """
        @summary Queries cluster names.
        
        @description ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-names
        
        @return: ListClusterNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_names_with_options(headers, runtime)

    async def list_cluster_names_async(self) -> searchengine_20211025_models.ListClusterNamesResponse:
        """
        @summary Queries cluster names.
        
        @description ### Method
        GET
        ### URI
        /openapi/ha3/instances/{instanceId}/cluster-names
        
        @return: ListClusterNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_names_with_options_async(headers, runtime)

    def list_cluster_tasks_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListClusterTasksResponse:
        """
        @summary Queries cluster tasks.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/cluster-tasks
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterTasksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusterTasks',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/cluster-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListClusterTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_tasks_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListClusterTasksResponse:
        """
        @summary Queries cluster tasks.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/cluster-tasks
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterTasksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusterTasks',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/cluster-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListClusterTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_tasks(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListClusterTasksResponse:
        """
        @summary Queries cluster tasks.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/cluster-tasks
        ```
        
        @return: ListClusterTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_cluster_tasks_with_options(instance_id, headers, runtime)

    async def list_cluster_tasks_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListClusterTasksResponse:
        """
        @summary Queries cluster tasks.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/cluster-tasks
        ```
        
        @return: ListClusterTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_cluster_tasks_with_options_async(instance_id, headers, runtime)

    def list_clusters_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListClustersResponse:
        """
        @summary Queries clusters.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListClustersResponse:
        """
        @summary Queries clusters.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListClustersResponse:
        """
        @summary Queries clusters.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters
        ```
        
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_clusters_with_options(instance_id, headers, runtime)

    async def list_clusters_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListClustersResponse:
        """
        @summary Queries clusters.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters
        ```
        
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_clusters_with_options_async(instance_id, headers, runtime)

    def list_data_source_schemas_with_options(
        self,
        instance_id: str,
        data_source_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDataSourceSchemasResponse:
        """
        @summary Queries the schema information about a data source.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/schemas`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceSchemasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSourceSchemas',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/schemas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDataSourceSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_schemas_with_options_async(
        self,
        instance_id: str,
        data_source_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDataSourceSchemasResponse:
        """
        @summary Queries the schema information about a data source.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/schemas`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceSchemasResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSourceSchemas',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/schemas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDataSourceSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_schemas(
        self,
        instance_id: str,
        data_source_name: str,
    ) -> searchengine_20211025_models.ListDataSourceSchemasResponse:
        """
        @summary Queries the schema information about a data source.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/schemas`
        
        @return: ListDataSourceSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_schemas_with_options(instance_id, data_source_name, headers, runtime)

    async def list_data_source_schemas_async(
        self,
        instance_id: str,
        data_source_name: str,
    ) -> searchengine_20211025_models.ListDataSourceSchemasResponse:
        """
        @summary Queries the schema information about a data source.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/schemas`
        
        @return: ListDataSourceSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_source_schemas_with_options_async(instance_id, data_source_name, headers, runtime)

    def list_data_source_tasks_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDataSourceTasksResponse:
        """
        @summary Displays data source tasks.
        
        @description ### [](#)Method
        ```java
        GET
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/data-source-tasks
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceTasksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSourceTasks',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-source-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDataSourceTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_tasks_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDataSourceTasksResponse:
        """
        @summary Displays data source tasks.
        
        @description ### [](#)Method
        ```java
        GET
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/data-source-tasks
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourceTasksResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSourceTasks',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-source-tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDataSourceTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_tasks(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListDataSourceTasksResponse:
        """
        @summary Displays data source tasks.
        
        @description ### [](#)Method
        ```java
        GET
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/data-source-tasks
        ```
        
        @return: ListDataSourceTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_source_tasks_with_options(instance_id, headers, runtime)

    async def list_data_source_tasks_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListDataSourceTasksResponse:
        """
        @summary Displays data source tasks.
        
        @description ### [](#)Method
        ```java
        GET
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/data-source-tasks
        ```
        
        @return: ListDataSourceTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_source_tasks_with_options_async(instance_id, headers, runtime)

    def list_data_sources_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDataSourcesResponse:
        """
        @summary Obtains the list of data sources.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourcesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDataSourcesResponse:
        """
        @summary Obtains the list of data sources.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources`
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourcesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sources(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListDataSourcesResponse:
        """
        @summary Obtains the list of data sources.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources`
        
        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_sources_with_options(instance_id, headers, runtime)

    async def list_data_sources_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListDataSourcesResponse:
        """
        @summary Obtains the list of data sources.
        
        @description ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources`
        
        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_sources_with_options_async(instance_id, headers, runtime)

    def list_databases_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDatabasesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabasesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDatabases',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDatabasesResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatabasesResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListDatabases',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListDatabasesResponse:
        """
        @return: ListDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_databases_with_options(instance_id, headers, runtime)

    async def list_databases_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListDatabasesResponse:
        """
        @return: ListDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_databases_with_options_async(instance_id, headers, runtime)

    def list_date_source_generations_with_options(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.ListDateSourceGenerationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDateSourceGenerationsResponse:
        """
        @summary Queries the historical index versions of a data source.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/generations?domainName={domainName}`
        
        @param request: ListDateSourceGenerationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDateSourceGenerationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.valid_status):
            query['validStatus'] = request.valid_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDateSourceGenerations',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/generations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDateSourceGenerationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_date_source_generations_with_options_async(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.ListDateSourceGenerationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDateSourceGenerationsResponse:
        """
        @summary Queries the historical index versions of a data source.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/generations?domainName={domainName}`
        
        @param request: ListDateSourceGenerationsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDateSourceGenerationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.valid_status):
            query['validStatus'] = request.valid_status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDateSourceGenerations',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/generations',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListDateSourceGenerationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_date_source_generations(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.ListDateSourceGenerationsRequest,
    ) -> searchengine_20211025_models.ListDateSourceGenerationsResponse:
        """
        @summary Queries the historical index versions of a data source.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/generations?domainName={domainName}`
        
        @param request: ListDateSourceGenerationsRequest
        @return: ListDateSourceGenerationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_date_source_generations_with_options(instance_id, data_source_name, request, headers, runtime)

    async def list_date_source_generations_async(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.ListDateSourceGenerationsRequest,
    ) -> searchengine_20211025_models.ListDateSourceGenerationsResponse:
        """
        @summary Queries the historical index versions of a data source.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/generations?domainName={domainName}`
        
        @param request: ListDateSourceGenerationsRequest
        @return: ListDateSourceGenerationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_date_source_generations_with_options_async(instance_id, data_source_name, request, headers, runtime)

    def list_index_recover_records_with_options(
        self,
        index_name: str,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListIndexRecoverRecordsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndexRecoverRecordsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListIndexRecoverRecords',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/actions/list-recover-records',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListIndexRecoverRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_index_recover_records_with_options_async(
        self,
        index_name: str,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListIndexRecoverRecordsResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndexRecoverRecordsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListIndexRecoverRecords',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/actions/list-recover-records',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListIndexRecoverRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_index_recover_records(
        self,
        index_name: str,
        instance_id: str,
    ) -> searchengine_20211025_models.ListIndexRecoverRecordsResponse:
        """
        @return: ListIndexRecoverRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_index_recover_records_with_options(index_name, instance_id, headers, runtime)

    async def list_index_recover_records_async(
        self,
        index_name: str,
        instance_id: str,
    ) -> searchengine_20211025_models.ListIndexRecoverRecordsResponse:
        """
        @return: ListIndexRecoverRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_index_recover_records_with_options_async(index_name, instance_id, headers, runtime)

    def list_indexes_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListIndexesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListIndexesResponse:
        """
        @summary Obtains the index list.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes
        
        @param request: ListIndexesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndexesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_mode):
            query['newMode'] = request.new_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIndexes',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListIndexesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_indexes_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListIndexesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListIndexesResponse:
        """
        @summary Obtains the index list.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes
        
        @param request: ListIndexesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListIndexesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_mode):
            query['newMode'] = request.new_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIndexes',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListIndexesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_indexes(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListIndexesRequest,
    ) -> searchengine_20211025_models.ListIndexesResponse:
        """
        @summary Obtains the index list.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes
        
        @param request: ListIndexesRequest
        @return: ListIndexesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_indexes_with_options(instance_id, request, headers, runtime)

    async def list_indexes_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListIndexesRequest,
    ) -> searchengine_20211025_models.ListIndexesResponse:
        """
        @summary Obtains the index list.
        
        @description ## Method
        GET
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes
        
        @param request: ListIndexesRequest
        @return: ListIndexesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_indexes_with_options_async(instance_id, request, headers, runtime)

    def list_instance_specs_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListInstanceSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListInstanceSpecsResponse:
        """
        @summary Queries the specifications of an instance.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/specs?type=qrs`
        
        @param request: ListInstanceSpecsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceSpecs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/specs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListInstanceSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_specs_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListInstanceSpecsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListInstanceSpecsResponse:
        """
        @summary Queries the specifications of an instance.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/specs?type=qrs`
        
        @param request: ListInstanceSpecsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceSpecsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceSpecs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/specs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListInstanceSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_specs(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListInstanceSpecsRequest,
    ) -> searchengine_20211025_models.ListInstanceSpecsResponse:
        """
        @summary Queries the specifications of an instance.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/specs?type=qrs`
        
        @param request: ListInstanceSpecsRequest
        @return: ListInstanceSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_specs_with_options(instance_id, request, headers, runtime)

    async def list_instance_specs_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListInstanceSpecsRequest,
    ) -> searchengine_20211025_models.ListInstanceSpecsResponse:
        """
        @summary Queries the specifications of an instance.
        
        @description ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/specs?type=qrs`
        
        @param request: ListInstanceSpecsRequest
        @return: ListInstanceSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_specs_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        tmp_req: searchengine_20211025_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListInstancesResponse:
        """
        @summary Queries a list of instances.
        
        @description ### [](#)Method
        `GET`
        ### [](#uri)URI
        `/openapi/ha3/instances`
        
        @param tmp_req: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = searchengine_20211025_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.edition):
            query['edition'] = request.edition
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        tmp_req: searchengine_20211025_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListInstancesResponse:
        """
        @summary Queries a list of instances.
        
        @description ### [](#)Method
        `GET`
        ### [](#uri)URI
        `/openapi/ha3/instances`
        
        @param tmp_req: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = searchengine_20211025_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.edition):
            query['edition'] = request.edition
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: searchengine_20211025_models.ListInstancesRequest,
    ) -> searchengine_20211025_models.ListInstancesResponse:
        """
        @summary Queries a list of instances.
        
        @description ### [](#)Method
        `GET`
        ### [](#uri)URI
        `/openapi/ha3/instances`
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: searchengine_20211025_models.ListInstancesRequest,
    ) -> searchengine_20211025_models.ListInstancesResponse:
        """
        @summary Queries a list of instances.
        
        @description ### [](#)Method
        `GET`
        ### [](#uri)URI
        `/openapi/ha3/instances`
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_logs_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListLogsResponse:
        """
        @param request: ListLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logs_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListLogsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListLogsResponse:
        """
        @param request: ListLogsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLogs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/logs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logs(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListLogsRequest,
    ) -> searchengine_20211025_models.ListLogsResponse:
        """
        @param request: ListLogsRequest
        @return: ListLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logs_with_options(instance_id, request, headers, runtime)

    async def list_logs_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListLogsRequest,
    ) -> searchengine_20211025_models.ListLogsResponse:
        """
        @param request: ListLogsRequest
        @return: ListLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_logs_with_options_async(instance_id, request, headers, runtime)

    def list_online_configs_with_options(
        self,
        instance_id: str,
        node_name: str,
        request: searchengine_20211025_models.ListOnlineConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListOnlineConfigsResponse:
        """
        @summary Queries the details of an online configuration.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs?domain={domain}
        ```
        
        @param request: ListOnlineConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOnlineConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnlineConfigs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/node/{OpenApiUtilClient.get_encode_param(node_name)}/online-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListOnlineConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_online_configs_with_options_async(
        self,
        instance_id: str,
        node_name: str,
        request: searchengine_20211025_models.ListOnlineConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListOnlineConfigsResponse:
        """
        @summary Queries the details of an online configuration.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs?domain={domain}
        ```
        
        @param request: ListOnlineConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOnlineConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['domain'] = request.domain
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnlineConfigs',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/node/{OpenApiUtilClient.get_encode_param(node_name)}/online-configs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListOnlineConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_online_configs(
        self,
        instance_id: str,
        node_name: str,
        request: searchengine_20211025_models.ListOnlineConfigsRequest,
    ) -> searchengine_20211025_models.ListOnlineConfigsResponse:
        """
        @summary Queries the details of an online configuration.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs?domain={domain}
        ```
        
        @param request: ListOnlineConfigsRequest
        @return: ListOnlineConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_online_configs_with_options(instance_id, node_name, request, headers, runtime)

    async def list_online_configs_async(
        self,
        instance_id: str,
        node_name: str,
        request: searchengine_20211025_models.ListOnlineConfigsRequest,
    ) -> searchengine_20211025_models.ListOnlineConfigsResponse:
        """
        @summary Queries the details of an online configuration.
        
        @description ### Method
        ```java
        GET
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs?domain={domain}
        ```
        
        @param request: ListOnlineConfigsRequest
        @return: ListOnlineConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_online_configs_with_options_async(instance_id, node_name, request, headers, runtime)

    def list_pause_policys_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListPausePolicysResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPausePolicysResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPausePolicys',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/pause-policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListPausePolicysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pause_policys_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListPausePolicysResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPausePolicysResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListPausePolicys',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/pause-policies',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListPausePolicysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pause_policys(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListPausePolicysResponse:
        """
        @return: ListPausePolicysResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_pause_policys_with_options(instance_id, headers, runtime)

    async def list_pause_policys_async(
        self,
        instance_id: str,
    ) -> searchengine_20211025_models.ListPausePolicysResponse:
        """
        @return: ListPausePolicysResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_pause_policys_with_options_async(instance_id, headers, runtime)

    def list_post_query_result_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListPostQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListPostQueryResultResponse:
        """
        @param request: ListPostQueryResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPostQueryResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['address'] = request.address
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPostQueryResult',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListPostQueryResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_post_query_result_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListPostQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListPostQueryResultResponse:
        """
        @param request: ListPostQueryResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPostQueryResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['address'] = request.address
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPostQueryResult',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListPostQueryResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_post_query_result(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListPostQueryResultRequest,
    ) -> searchengine_20211025_models.ListPostQueryResultResponse:
        """
        @param request: ListPostQueryResultRequest
        @return: ListPostQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_post_query_result_with_options(instance_id, request, headers, runtime)

    async def list_post_query_result_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListPostQueryResultRequest,
    ) -> searchengine_20211025_models.ListPostQueryResultResponse:
        """
        @param request: ListPostQueryResultRequest
        @return: ListPostQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_post_query_result_with_options_async(instance_id, request, headers, runtime)

    def list_query_result_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListQueryResultResponse:
        """
        @summary Queries the query result.
        
        @description ### [](#)Method
        `GET`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/query?query=xxxx`
        
        @param request: ListQueryResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueryResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.sql):
            query['sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryResult',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/query',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListQueryResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_query_result_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListQueryResultResponse:
        """
        @summary Queries the query result.
        
        @description ### [](#)Method
        `GET`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/query?query=xxxx`
        
        @param request: ListQueryResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQueryResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.sql):
            query['sql'] = request.sql
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQueryResult',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/query',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListQueryResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_query_result(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListQueryResultRequest,
    ) -> searchengine_20211025_models.ListQueryResultResponse:
        """
        @summary Queries the query result.
        
        @description ### [](#)Method
        `GET`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/query?query=xxxx`
        
        @param request: ListQueryResultRequest
        @return: ListQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_query_result_with_options(instance_id, request, headers, runtime)

    async def list_query_result_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListQueryResultRequest,
    ) -> searchengine_20211025_models.ListQueryResultResponse:
        """
        @summary Queries the query result.
        
        @description ### [](#)Method
        `GET`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/query?query=xxxx`
        
        @param request: ListQueryResultRequest
        @return: ListQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_query_result_with_options_async(instance_id, request, headers, runtime)

    def list_rest_query_result_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListRestQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListRestQueryResultResponse:
        """
        @param request: ListRestQueryResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRestQueryResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['address'] = request.address
        body = {}
        if not UtilClient.is_unset(request.index_name):
            body['indexName'] = request.index_name
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRestQueryResult',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rest-query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListRestQueryResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rest_query_result_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListRestQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListRestQueryResultResponse:
        """
        @param request: ListRestQueryResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRestQueryResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['address'] = request.address
        body = {}
        if not UtilClient.is_unset(request.index_name):
            body['indexName'] = request.index_name
        if not UtilClient.is_unset(request.query):
            body['query'] = request.query
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRestQueryResult',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/rest-query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListRestQueryResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rest_query_result(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListRestQueryResultRequest,
    ) -> searchengine_20211025_models.ListRestQueryResultResponse:
        """
        @param request: ListRestQueryResultRequest
        @return: ListRestQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_rest_query_result_with_options(instance_id, request, headers, runtime)

    async def list_rest_query_result_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListRestQueryResultRequest,
    ) -> searchengine_20211025_models.ListRestQueryResultResponse:
        """
        @param request: ListRestQueryResultRequest
        @return: ListRestQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_rest_query_result_with_options_async(instance_id, request, headers, runtime)

    def list_schemas_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListSchemasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListSchemasResponse:
        """
        @summary 通过数据源配置获取schema信息
        
        @param request: ListSchemasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSchemasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.access_secret):
            query['accessSecret'] = request.access_secret
        if not UtilClient.is_unset(request.endpoint):
            query['endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.partition):
            query['partition'] = request.partition
        if not UtilClient.is_unset(request.project):
            query['project'] = request.project
        if not UtilClient.is_unset(request.table):
            query['table'] = request.table
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemas',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/schemas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_schemas_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListSchemasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListSchemasResponse:
        """
        @summary 通过数据源配置获取schema信息
        
        @param request: ListSchemasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSchemasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_key):
            query['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.access_secret):
            query['accessSecret'] = request.access_secret
        if not UtilClient.is_unset(request.endpoint):
            query['endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.namespace):
            query['namespace'] = request.namespace
        if not UtilClient.is_unset(request.partition):
            query['partition'] = request.partition
        if not UtilClient.is_unset(request.project):
            query['project'] = request.project
        if not UtilClient.is_unset(request.table):
            query['table'] = request.table
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemas',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/schemas',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_schemas(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListSchemasRequest,
    ) -> searchengine_20211025_models.ListSchemasResponse:
        """
        @summary 通过数据源配置获取schema信息
        
        @param request: ListSchemasRequest
        @return: ListSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_schemas_with_options(instance_id, request, headers, runtime)

    async def list_schemas_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListSchemasRequest,
    ) -> searchengine_20211025_models.ListSchemasResponse:
        """
        @summary 通过数据源配置获取schema信息
        
        @param request: ListSchemasRequest
        @return: ListSchemasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_schemas_with_options_async(instance_id, request, headers, runtime)

    def list_table_generations_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListTableGenerationsResponse:
        """
        @summary Queries a list of index versions.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTableGenerationsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTableGenerations',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/index_versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListTableGenerationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_table_generations_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListTableGenerationsResponse:
        """
        @summary Queries a list of index versions.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTableGenerationsResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListTableGenerations',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/index_versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListTableGenerationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_table_generations(
        self,
        instance_id: str,
        table_name: str,
    ) -> searchengine_20211025_models.ListTableGenerationsResponse:
        """
        @summary Queries a list of index versions.
        
        @return: ListTableGenerationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_table_generations_with_options(instance_id, table_name, headers, runtime)

    async def list_table_generations_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> searchengine_20211025_models.ListTableGenerationsResponse:
        """
        @summary Queries a list of index versions.
        
        @return: ListTableGenerationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_table_generations_with_options_async(instance_id, table_name, headers, runtime)

    def list_tables_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListTablesResponse:
        """
        @summary Queries a list of index tables.
        
        @param request: ListTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_mode):
            query['newMode'] = request.new_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListTablesResponse:
        """
        @summary Queries a list of index tables.
        
        @param request: ListTablesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_mode):
            query['newMode'] = request.new_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTables',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tables(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListTablesRequest,
    ) -> searchengine_20211025_models.ListTablesResponse:
        """
        @summary Queries a list of index tables.
        
        @param request: ListTablesRequest
        @return: ListTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tables_with_options(instance_id, request, headers, runtime)

    async def list_tables_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListTablesRequest,
    ) -> searchengine_20211025_models.ListTablesResponse:
        """
        @summary Queries a list of index tables.
        
        @param request: ListTablesRequest
        @return: ListTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tables_with_options_async(instance_id, request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: searchengine_20211025_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListTagResourcesResponse:
        """
        @summary 查标签接口
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = searchengine_20211025_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/resource-tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: searchengine_20211025_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListTagResourcesResponse:
        """
        @summary 查标签接口
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = searchengine_20211025_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/resource-tags',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: searchengine_20211025_models.ListTagResourcesRequest,
    ) -> searchengine_20211025_models.ListTagResourcesResponse:
        """
        @summary 查标签接口
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: searchengine_20211025_models.ListTagResourcesRequest,
    ) -> searchengine_20211025_models.ListTagResourcesResponse:
        """
        @summary 查标签接口
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def list_tasks_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListTasksResponse:
        """
        @summary 获取集群任务列表（数据源+集群）
        
        @param request: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListTasksResponse:
        """
        @summary 获取集群任务列表（数据源+集群）
        
        @param request: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListTasksRequest,
    ) -> searchengine_20211025_models.ListTasksResponse:
        """
        @summary 获取集群任务列表（数据源+集群）
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(instance_id, request, headers, runtime)

    async def list_tasks_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListTasksRequest,
    ) -> searchengine_20211025_models.ListTasksResponse:
        """
        @summary 获取集群任务列表（数据源+集群）
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(instance_id, request, headers, runtime)

    def list_vector_query_result_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListVectorQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListVectorQueryResultResponse:
        """
        @param request: ListVectorQueryResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVectorQueryResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['address'] = request.address
        if not UtilClient.is_unset(request.query_type):
            query['queryType'] = request.query_type
        if not UtilClient.is_unset(request.vector_query_type):
            query['vectorQueryType'] = request.vector_query_type
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVectorQueryResult',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/vector-query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListVectorQueryResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vector_query_result_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListVectorQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListVectorQueryResultResponse:
        """
        @param request: ListVectorQueryResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVectorQueryResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['address'] = request.address
        if not UtilClient.is_unset(request.query_type):
            query['queryType'] = request.query_type
        if not UtilClient.is_unset(request.vector_query_type):
            query['vectorQueryType'] = request.vector_query_type
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVectorQueryResult',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/vector-query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ListVectorQueryResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vector_query_result(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListVectorQueryResultRequest,
    ) -> searchengine_20211025_models.ListVectorQueryResultResponse:
        """
        @param request: ListVectorQueryResultRequest
        @return: ListVectorQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_vector_query_result_with_options(instance_id, request, headers, runtime)

    async def list_vector_query_result_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListVectorQueryResultRequest,
    ) -> searchengine_20211025_models.ListVectorQueryResultResponse:
        """
        @param request: ListVectorQueryResultRequest
        @return: ListVectorQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_vector_query_result_with_options_async(instance_id, request, headers, runtime)

    def modify_advance_config_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ModifyAdvanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyAdvanceConfigResponse:
        """
        @param request: ModifyAdvanceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAdvanceConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            body['contentType'] = request.content_type
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.update_time):
            body['updateTime'] = request.update_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyAdvanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_advance_config_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ModifyAdvanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyAdvanceConfigResponse:
        """
        @param request: ModifyAdvanceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAdvanceConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            body['contentType'] = request.content_type
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.update_time):
            body['updateTime'] = request.update_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyAdvanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_advance_config(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ModifyAdvanceConfigRequest,
    ) -> searchengine_20211025_models.ModifyAdvanceConfigResponse:
        """
        @param request: ModifyAdvanceConfigRequest
        @return: ModifyAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_advance_config_with_options(instance_id, config_name, request, headers, runtime)

    async def modify_advance_config_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ModifyAdvanceConfigRequest,
    ) -> searchengine_20211025_models.ModifyAdvanceConfigResponse:
        """
        @param request: ModifyAdvanceConfigRequest
        @return: ModifyAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_advance_config_with_options_async(instance_id, config_name, request, headers, runtime)

    def modify_advance_config_file_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ModifyAdvanceConfigFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyAdvanceConfigFileResponse:
        """
        @summary Modifies the advanced configurations.
        
        @description ## Method
        put
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        
        @param request: ModifyAdvanceConfigFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAdvanceConfigFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAdvanceConfigFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/file',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyAdvanceConfigFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_advance_config_file_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ModifyAdvanceConfigFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyAdvanceConfigFileResponse:
        """
        @summary Modifies the advanced configurations.
        
        @description ## Method
        put
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        
        @param request: ModifyAdvanceConfigFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAdvanceConfigFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAdvanceConfigFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/file',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyAdvanceConfigFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_advance_config_file(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ModifyAdvanceConfigFileRequest,
    ) -> searchengine_20211025_models.ModifyAdvanceConfigFileResponse:
        """
        @summary Modifies the advanced configurations.
        
        @description ## Method
        put
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        
        @param request: ModifyAdvanceConfigFileRequest
        @return: ModifyAdvanceConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_advance_config_file_with_options(instance_id, config_name, request, headers, runtime)

    async def modify_advance_config_file_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ModifyAdvanceConfigFileRequest,
    ) -> searchengine_20211025_models.ModifyAdvanceConfigFileResponse:
        """
        @summary Modifies the advanced configurations.
        
        @description ## Method
        put
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        
        @param request: ModifyAdvanceConfigFileRequest
        @return: ModifyAdvanceConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_advance_config_file_with_options_async(instance_id, config_name, request, headers, runtime)

    def modify_alias_with_options(
        self,
        instance_id: str,
        alias: str,
        request: searchengine_20211025_models.ModifyAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyAliasResponse:
        """
        @param request: ModifyAliasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAliasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.index):
            body['index'] = request.index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAlias',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/aliases/{OpenApiUtilClient.get_encode_param(alias)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyAliasResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_alias_with_options_async(
        self,
        instance_id: str,
        alias: str,
        request: searchengine_20211025_models.ModifyAliasRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyAliasResponse:
        """
        @param request: ModifyAliasRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAliasResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias):
            body['alias'] = request.alias
        if not UtilClient.is_unset(request.index):
            body['index'] = request.index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyAlias',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/aliases/{OpenApiUtilClient.get_encode_param(alias)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyAliasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_alias(
        self,
        instance_id: str,
        alias: str,
        request: searchengine_20211025_models.ModifyAliasRequest,
    ) -> searchengine_20211025_models.ModifyAliasResponse:
        """
        @param request: ModifyAliasRequest
        @return: ModifyAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_alias_with_options(instance_id, alias, request, headers, runtime)

    async def modify_alias_async(
        self,
        instance_id: str,
        alias: str,
        request: searchengine_20211025_models.ModifyAliasRequest,
    ) -> searchengine_20211025_models.ModifyAliasResponse:
        """
        @param request: ModifyAliasRequest
        @return: ModifyAliasResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_alias_with_options_async(instance_id, alias, request, headers, runtime)

    def modify_cluster_desc_with_options(
        self,
        instance_id: str,
        cluster_name: str,
        request: searchengine_20211025_models.ModifyClusterDescRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyClusterDescResponse:
        """
        @summary Modifies the description of a specified cluster.
        
        @description ### [](#)Method
        `PUT`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/clusters/{clusterName}/desc`
        
        @param request: ModifyClusterDescRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterDescResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterDesc',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters/{OpenApiUtilClient.get_encode_param(cluster_name)}/desc',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyClusterDescResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_desc_with_options_async(
        self,
        instance_id: str,
        cluster_name: str,
        request: searchengine_20211025_models.ModifyClusterDescRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyClusterDescResponse:
        """
        @summary Modifies the description of a specified cluster.
        
        @description ### [](#)Method
        `PUT`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/clusters/{clusterName}/desc`
        
        @param request: ModifyClusterDescRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterDescResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterDesc',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters/{OpenApiUtilClient.get_encode_param(cluster_name)}/desc',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyClusterDescResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_desc(
        self,
        instance_id: str,
        cluster_name: str,
        request: searchengine_20211025_models.ModifyClusterDescRequest,
    ) -> searchengine_20211025_models.ModifyClusterDescResponse:
        """
        @summary Modifies the description of a specified cluster.
        
        @description ### [](#)Method
        `PUT`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/clusters/{clusterName}/desc`
        
        @param request: ModifyClusterDescRequest
        @return: ModifyClusterDescResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_desc_with_options(instance_id, cluster_name, request, headers, runtime)

    async def modify_cluster_desc_async(
        self,
        instance_id: str,
        cluster_name: str,
        request: searchengine_20211025_models.ModifyClusterDescRequest,
    ) -> searchengine_20211025_models.ModifyClusterDescResponse:
        """
        @summary Modifies the description of a specified cluster.
        
        @description ### [](#)Method
        `PUT`
        ### [](#uri)URI
        `/openapi/ha3/instances/{instanceId}/clusters/{clusterName}/desc`
        
        @param request: ModifyClusterDescRequest
        @return: ModifyClusterDescResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cluster_desc_with_options_async(instance_id, cluster_name, request, headers, runtime)

    def modify_cluster_offline_config_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyClusterOfflineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyClusterOfflineConfigResponse:
        """
        @summary Modifies the configuration information of a cluster.
        
        @description ## Request syntax
        PUT /openapi/ha3/instances/{instanceId}/cluster-offline-config
        
        @param request: ModifyClusterOfflineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterOfflineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_mode):
            body['buildMode'] = request.build_mode
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            body['dataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_time_sec):
            body['dataTimeSec'] = request.data_time_sec
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        if not UtilClient.is_unset(request.push_mode):
            body['pushMode'] = request.push_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterOfflineConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/cluster-offline-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyClusterOfflineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_offline_config_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyClusterOfflineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyClusterOfflineConfigResponse:
        """
        @summary Modifies the configuration information of a cluster.
        
        @description ## Request syntax
        PUT /openapi/ha3/instances/{instanceId}/cluster-offline-config
        
        @param request: ModifyClusterOfflineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterOfflineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_mode):
            body['buildMode'] = request.build_mode
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            body['dataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.data_time_sec):
            body['dataTimeSec'] = request.data_time_sec
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        if not UtilClient.is_unset(request.push_mode):
            body['pushMode'] = request.push_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterOfflineConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/cluster-offline-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyClusterOfflineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_offline_config(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyClusterOfflineConfigRequest,
    ) -> searchengine_20211025_models.ModifyClusterOfflineConfigResponse:
        """
        @summary Modifies the configuration information of a cluster.
        
        @description ## Request syntax
        PUT /openapi/ha3/instances/{instanceId}/cluster-offline-config
        
        @param request: ModifyClusterOfflineConfigRequest
        @return: ModifyClusterOfflineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_offline_config_with_options(instance_id, request, headers, runtime)

    async def modify_cluster_offline_config_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyClusterOfflineConfigRequest,
    ) -> searchengine_20211025_models.ModifyClusterOfflineConfigResponse:
        """
        @summary Modifies the configuration information of a cluster.
        
        @description ## Request syntax
        PUT /openapi/ha3/instances/{instanceId}/cluster-offline-config
        
        @param request: ModifyClusterOfflineConfigRequest
        @return: ModifyClusterOfflineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cluster_offline_config_with_options_async(instance_id, request, headers, runtime)

    def modify_cluster_online_config_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyClusterOnlineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyClusterOnlineConfigResponse:
        """
        @summary Modifies the online configuration of a cluster.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/cluster-online-config`
        
        @param request: ModifyClusterOnlineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterOnlineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clusters):
            body['clusters'] = request.clusters
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterOnlineConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/cluster-online-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyClusterOnlineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_online_config_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyClusterOnlineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyClusterOnlineConfigResponse:
        """
        @summary Modifies the online configuration of a cluster.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/cluster-online-config`
        
        @param request: ModifyClusterOnlineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyClusterOnlineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.clusters):
            body['clusters'] = request.clusters
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyClusterOnlineConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/cluster-online-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyClusterOnlineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_online_config(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyClusterOnlineConfigRequest,
    ) -> searchengine_20211025_models.ModifyClusterOnlineConfigResponse:
        """
        @summary Modifies the online configuration of a cluster.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/cluster-online-config`
        
        @param request: ModifyClusterOnlineConfigRequest
        @return: ModifyClusterOnlineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_cluster_online_config_with_options(instance_id, request, headers, runtime)

    async def modify_cluster_online_config_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyClusterOnlineConfigRequest,
    ) -> searchengine_20211025_models.ModifyClusterOnlineConfigResponse:
        """
        @summary Modifies the online configuration of a cluster.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/cluster-online-config`
        
        @param request: ModifyClusterOnlineConfigRequest
        @return: ModifyClusterOnlineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cluster_online_config_with_options_async(instance_id, request, headers, runtime)

    def modify_data_source_deploy_with_options(
        self,
        instance_id: str,
        deploy_name: str,
        data_source_name: str,
        request: searchengine_20211025_models.ModifyDataSourceDeployRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyDataSourceDeployResponse:
        """
        @summary 修改数据源部署信息
        
        @param request: ModifyDataSourceDeployRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataSourceDeployResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.generation_id):
            query['generationId'] = request.generation_id
        body = {}
        if not UtilClient.is_unset(request.auto_build_index):
            body['autoBuildIndex'] = request.auto_build_index
        if not UtilClient.is_unset(request.extend):
            body['extend'] = request.extend
        if not UtilClient.is_unset(request.processor):
            body['processor'] = request.processor
        if not UtilClient.is_unset(request.storage):
            body['storage'] = request.storage
        if not UtilClient.is_unset(request.swift):
            body['swift'] = request.swift
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDataSourceDeploy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/deploys/{OpenApiUtilClient.get_encode_param(deploy_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyDataSourceDeployResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_source_deploy_with_options_async(
        self,
        instance_id: str,
        deploy_name: str,
        data_source_name: str,
        request: searchengine_20211025_models.ModifyDataSourceDeployRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyDataSourceDeployResponse:
        """
        @summary 修改数据源部署信息
        
        @param request: ModifyDataSourceDeployRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataSourceDeployResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.generation_id):
            query['generationId'] = request.generation_id
        body = {}
        if not UtilClient.is_unset(request.auto_build_index):
            body['autoBuildIndex'] = request.auto_build_index
        if not UtilClient.is_unset(request.extend):
            body['extend'] = request.extend
        if not UtilClient.is_unset(request.processor):
            body['processor'] = request.processor
        if not UtilClient.is_unset(request.storage):
            body['storage'] = request.storage
        if not UtilClient.is_unset(request.swift):
            body['swift'] = request.swift
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDataSourceDeploy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/deploys/{OpenApiUtilClient.get_encode_param(deploy_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyDataSourceDeployResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_source_deploy(
        self,
        instance_id: str,
        deploy_name: str,
        data_source_name: str,
        request: searchengine_20211025_models.ModifyDataSourceDeployRequest,
    ) -> searchengine_20211025_models.ModifyDataSourceDeployResponse:
        """
        @summary 修改数据源部署信息
        
        @param request: ModifyDataSourceDeployRequest
        @return: ModifyDataSourceDeployResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_data_source_deploy_with_options(instance_id, deploy_name, data_source_name, request, headers, runtime)

    async def modify_data_source_deploy_async(
        self,
        instance_id: str,
        deploy_name: str,
        data_source_name: str,
        request: searchengine_20211025_models.ModifyDataSourceDeployRequest,
    ) -> searchengine_20211025_models.ModifyDataSourceDeployResponse:
        """
        @summary 修改数据源部署信息
        
        @param request: ModifyDataSourceDeployRequest
        @return: ModifyDataSourceDeployResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_data_source_deploy_with_options_async(instance_id, deploy_name, data_source_name, request, headers, runtime)

    def modify_file_with_options(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
        request: searchengine_20211025_models.ModifyFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyFileResponse:
        """
        @summary Modifies a file.
        
        @description ## Method
        PUT
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        
        @param request: ModifyFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/file',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_file_with_options_async(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
        request: searchengine_20211025_models.ModifyFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyFileResponse:
        """
        @summary Modifies a file.
        
        @description ## Method
        PUT
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        
        @param request: ModifyFileRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyFile',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/versions/{OpenApiUtilClient.get_encode_param(version_name)}/file',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_file(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
        request: searchengine_20211025_models.ModifyFileRequest,
    ) -> searchengine_20211025_models.ModifyFileResponse:
        """
        @summary Modifies a file.
        
        @description ## Method
        PUT
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        
        @param request: ModifyFileRequest
        @return: ModifyFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_file_with_options(instance_id, index_name, version_name, request, headers, runtime)

    async def modify_file_async(
        self,
        instance_id: str,
        index_name: str,
        version_name: str,
        request: searchengine_20211025_models.ModifyFileRequest,
    ) -> searchengine_20211025_models.ModifyFileResponse:
        """
        @summary Modifies a file.
        
        @description ## Method
        PUT
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        
        @param request: ModifyFileRequest
        @return: ModifyFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_file_with_options_async(instance_id, index_name, version_name, request, headers, runtime)

    def modify_index_with_options(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyIndexResponse:
        """
        @param request: ModifyIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.build_parallel_num):
            body['buildParallelNum'] = request.build_parallel_num
        if not UtilClient.is_unset(request.cluster):
            body['cluster'] = request.cluster
        if not UtilClient.is_unset(request.cluster_config_name):
            body['clusterConfigName'] = request.cluster_config_name
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.data_source):
            body['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.data_source_info):
            body['dataSourceInfo'] = request.data_source_info
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.merge_parallel_num):
            body['mergeParallelNum'] = request.merge_parallel_num
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        if not UtilClient.is_unset(request.push_mode):
            body['pushMode'] = request.push_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_index_with_options_async(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyIndexResponse:
        """
        @param request: ModifyIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIndexResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.build_parallel_num):
            body['buildParallelNum'] = request.build_parallel_num
        if not UtilClient.is_unset(request.cluster):
            body['cluster'] = request.cluster
        if not UtilClient.is_unset(request.cluster_config_name):
            body['clusterConfigName'] = request.cluster_config_name
        if not UtilClient.is_unset(request.config):
            body['config'] = request.config
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.data_source):
            body['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.data_source_info):
            body['dataSourceInfo'] = request.data_source_info
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.domain):
            body['domain'] = request.domain
        if not UtilClient.is_unset(request.merge_parallel_num):
            body['mergeParallelNum'] = request.merge_parallel_num
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        if not UtilClient.is_unset(request.push_mode):
            body['pushMode'] = request.push_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_index(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyIndexRequest,
    ) -> searchengine_20211025_models.ModifyIndexResponse:
        """
        @param request: ModifyIndexRequest
        @return: ModifyIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_index_with_options(instance_id, index_name, request, headers, runtime)

    async def modify_index_async(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyIndexRequest,
    ) -> searchengine_20211025_models.ModifyIndexResponse:
        """
        @param request: ModifyIndexRequest
        @return: ModifyIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_index_with_options_async(instance_id, index_name, request, headers, runtime)

    def modify_index_online_strategy_with_options(
        self,
        instance_id: str,
        data_source_name: str,
        deploy_name: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyIndexOnlineStrategyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyIndexOnlineStrategyResponse:
        """
        @summary Modifies the online policy of an index.
        
        @param request: ModifyIndexOnlineStrategyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIndexOnlineStrategyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.change_rate):
            body['changeRate'] = request.change_rate
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyIndexOnlineStrategy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/deploys/{OpenApiUtilClient.get_encode_param(deploy_name)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/online-strategy',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyIndexOnlineStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_index_online_strategy_with_options_async(
        self,
        instance_id: str,
        data_source_name: str,
        deploy_name: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyIndexOnlineStrategyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyIndexOnlineStrategyResponse:
        """
        @summary Modifies the online policy of an index.
        
        @param request: ModifyIndexOnlineStrategyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIndexOnlineStrategyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.change_rate):
            body['changeRate'] = request.change_rate
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyIndexOnlineStrategy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/deploys/{OpenApiUtilClient.get_encode_param(deploy_name)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/online-strategy',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyIndexOnlineStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_index_online_strategy(
        self,
        instance_id: str,
        data_source_name: str,
        deploy_name: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyIndexOnlineStrategyRequest,
    ) -> searchengine_20211025_models.ModifyIndexOnlineStrategyResponse:
        """
        @summary Modifies the online policy of an index.
        
        @param request: ModifyIndexOnlineStrategyRequest
        @return: ModifyIndexOnlineStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_index_online_strategy_with_options(instance_id, data_source_name, deploy_name, index_name, request, headers, runtime)

    async def modify_index_online_strategy_async(
        self,
        instance_id: str,
        data_source_name: str,
        deploy_name: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyIndexOnlineStrategyRequest,
    ) -> searchengine_20211025_models.ModifyIndexOnlineStrategyResponse:
        """
        @summary Modifies the online policy of an index.
        
        @param request: ModifyIndexOnlineStrategyRequest
        @return: ModifyIndexOnlineStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_index_online_strategy_with_options_async(instance_id, data_source_name, deploy_name, index_name, request, headers, runtime)

    def modify_index_partition_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyIndexPartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyIndexPartitionResponse:
        """
        @summary Modifies the information about index partitions.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/index-partition`
        
        @param request: ModifyIndexPartitionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIndexPartitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.domain_name):
            body['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.index_infos):
            body['indexInfos'] = request.index_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyIndexPartition',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/index-partition',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyIndexPartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_index_partition_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyIndexPartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyIndexPartitionResponse:
        """
        @summary Modifies the information about index partitions.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/index-partition`
        
        @param request: ModifyIndexPartitionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIndexPartitionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.domain_name):
            body['domainName'] = request.domain_name
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.index_infos):
            body['indexInfos'] = request.index_infos
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyIndexPartition',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/index-partition',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyIndexPartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_index_partition(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyIndexPartitionRequest,
    ) -> searchengine_20211025_models.ModifyIndexPartitionResponse:
        """
        @summary Modifies the information about index partitions.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/index-partition`
        
        @param request: ModifyIndexPartitionRequest
        @return: ModifyIndexPartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_index_partition_with_options(instance_id, request, headers, runtime)

    async def modify_index_partition_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyIndexPartitionRequest,
    ) -> searchengine_20211025_models.ModifyIndexPartitionResponse:
        """
        @summary Modifies the information about index partitions.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/index-partition`
        
        @param request: ModifyIndexPartitionRequest
        @return: ModifyIndexPartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_index_partition_with_options_async(instance_id, request, headers, runtime)

    def modify_index_version_with_options(
        self,
        instance_id: str,
        cluster_name: str,
        request: searchengine_20211025_models.ModifyIndexVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyIndexVersionResponse:
        """
        @summary Modifies the index version of a cluster (an index version rollback).
        
        @description ## [](#)Method
        PUT
        ## [](#uri)URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        
        @param request: ModifyIndexVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIndexVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='ModifyIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters/{OpenApiUtilClient.get_encode_param(cluster_name)}/index-version',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyIndexVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_index_version_with_options_async(
        self,
        instance_id: str,
        cluster_name: str,
        request: searchengine_20211025_models.ModifyIndexVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyIndexVersionResponse:
        """
        @summary Modifies the index version of a cluster (an index version rollback).
        
        @description ## [](#)Method
        PUT
        ## [](#uri)URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        
        @param request: ModifyIndexVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyIndexVersionResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        params = open_api_models.Params(
            action='ModifyIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters/{OpenApiUtilClient.get_encode_param(cluster_name)}/index-version',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyIndexVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_index_version(
        self,
        instance_id: str,
        cluster_name: str,
        request: searchengine_20211025_models.ModifyIndexVersionRequest,
    ) -> searchengine_20211025_models.ModifyIndexVersionResponse:
        """
        @summary Modifies the index version of a cluster (an index version rollback).
        
        @description ## [](#)Method
        PUT
        ## [](#uri)URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        
        @param request: ModifyIndexVersionRequest
        @return: ModifyIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_index_version_with_options(instance_id, cluster_name, request, headers, runtime)

    async def modify_index_version_async(
        self,
        instance_id: str,
        cluster_name: str,
        request: searchengine_20211025_models.ModifyIndexVersionRequest,
    ) -> searchengine_20211025_models.ModifyIndexVersionResponse:
        """
        @summary Modifies the index version of a cluster (an index version rollback).
        
        @description ## [](#)Method
        PUT
        ## [](#uri)URI
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}/index-version
        
        @param request: ModifyIndexVersionRequest
        @return: ModifyIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_index_version_with_options_async(instance_id, cluster_name, request, headers, runtime)

    def modify_node_config_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyNodeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyNodeConfigResponse:
        """
        @summary Modifies the configurations of a node.
        
        @description ### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node-config?type=qrs&name=test
        ```
        
        @param request: ModifyNodeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['clusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.data_source_name):
            query['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.active):
            body['active'] = request.active
        if not UtilClient.is_unset(request.data_duplicate_number):
            body['dataDuplicateNumber'] = request.data_duplicate_number
        if not UtilClient.is_unset(request.data_fragment_number):
            body['dataFragmentNumber'] = request.data_fragment_number
        if not UtilClient.is_unset(request.flow_ratio):
            body['flowRatio'] = request.flow_ratio
        if not UtilClient.is_unset(request.min_service_percent):
            body['minServicePercent'] = request.min_service_percent
        if not UtilClient.is_unset(request.published):
            body['published'] = request.published
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNodeConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/node-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyNodeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_config_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyNodeConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyNodeConfigResponse:
        """
        @summary Modifies the configurations of a node.
        
        @description ### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node-config?type=qrs&name=test
        ```
        
        @param request: ModifyNodeConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNodeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['clusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.data_source_name):
            query['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.active):
            body['active'] = request.active
        if not UtilClient.is_unset(request.data_duplicate_number):
            body['dataDuplicateNumber'] = request.data_duplicate_number
        if not UtilClient.is_unset(request.data_fragment_number):
            body['dataFragmentNumber'] = request.data_fragment_number
        if not UtilClient.is_unset(request.flow_ratio):
            body['flowRatio'] = request.flow_ratio
        if not UtilClient.is_unset(request.min_service_percent):
            body['minServicePercent'] = request.min_service_percent
        if not UtilClient.is_unset(request.published):
            body['published'] = request.published
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyNodeConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/node-config',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyNodeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_config(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyNodeConfigRequest,
    ) -> searchengine_20211025_models.ModifyNodeConfigResponse:
        """
        @summary Modifies the configurations of a node.
        
        @description ### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node-config?type=qrs&name=test
        ```
        
        @param request: ModifyNodeConfigRequest
        @return: ModifyNodeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_node_config_with_options(instance_id, request, headers, runtime)

    async def modify_node_config_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyNodeConfigRequest,
    ) -> searchengine_20211025_models.ModifyNodeConfigResponse:
        """
        @summary Modifies the configurations of a node.
        
        @description ### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node-config?type=qrs&name=test
        ```
        
        @param request: ModifyNodeConfigRequest
        @return: ModifyNodeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_node_config_with_options_async(instance_id, request, headers, runtime)

    def modify_online_config_with_options(
        self,
        instance_id: str,
        node_name: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyOnlineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyOnlineConfigResponse:
        """
        @summary Modifies online configurations.
        
        @description ### Method
        ```java
        put
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs/{indexName}
        ```
        
        @param request: ModifyOnlineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyOnlineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyOnlineConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/node/{OpenApiUtilClient.get_encode_param(node_name)}/online-configs/{OpenApiUtilClient.get_encode_param(index_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyOnlineConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_online_config_with_options_async(
        self,
        instance_id: str,
        node_name: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyOnlineConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyOnlineConfigResponse:
        """
        @summary Modifies online configurations.
        
        @description ### Method
        ```java
        put
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs/{indexName}
        ```
        
        @param request: ModifyOnlineConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyOnlineConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyOnlineConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/node/{OpenApiUtilClient.get_encode_param(node_name)}/online-configs/{OpenApiUtilClient.get_encode_param(index_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyOnlineConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_online_config(
        self,
        instance_id: str,
        node_name: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyOnlineConfigRequest,
    ) -> searchengine_20211025_models.ModifyOnlineConfigResponse:
        """
        @summary Modifies online configurations.
        
        @description ### Method
        ```java
        put
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs/{indexName}
        ```
        
        @param request: ModifyOnlineConfigRequest
        @return: ModifyOnlineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_online_config_with_options(instance_id, node_name, index_name, request, headers, runtime)

    async def modify_online_config_async(
        self,
        instance_id: str,
        node_name: str,
        index_name: str,
        request: searchengine_20211025_models.ModifyOnlineConfigRequest,
    ) -> searchengine_20211025_models.ModifyOnlineConfigResponse:
        """
        @summary Modifies online configurations.
        
        @description ### Method
        ```java
        put
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/node/{nodeName}/online-configs/{indexName}
        ```
        
        @param request: ModifyOnlineConfigRequest
        @return: ModifyOnlineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_online_config_with_options_async(instance_id, node_name, index_name, request, headers, runtime)

    def modify_password_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPasswordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyPasswordResponse:
        """
        @summary 修改实例的密码
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/password`
        
        @param request: ModifyPasswordRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPasswordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPassword',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/password',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_password_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPasswordRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyPasswordResponse:
        """
        @summary 修改实例的密码
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/password`
        
        @param request: ModifyPasswordRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPasswordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.password):
            body['password'] = request.password
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPassword',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/password',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_password(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPasswordRequest,
    ) -> searchengine_20211025_models.ModifyPasswordResponse:
        """
        @summary 修改实例的密码
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/password`
        
        @param request: ModifyPasswordRequest
        @return: ModifyPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_password_with_options(instance_id, request, headers, runtime)

    async def modify_password_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPasswordRequest,
    ) -> searchengine_20211025_models.ModifyPasswordResponse:
        """
        @summary 修改实例的密码
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/password`
        
        @param request: ModifyPasswordRequest
        @return: ModifyPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_password_with_options_async(instance_id, request, headers, runtime)

    def modify_pause_policy_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPausePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyPausePolicyResponse:
        """
        @param request: ModifyPausePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPausePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPausePolicy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/pause-policies',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyPausePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_pause_policy_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPausePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyPausePolicyResponse:
        """
        @param request: ModifyPausePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPausePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPausePolicy',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/pause-policies',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyPausePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_pause_policy(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPausePolicyRequest,
    ) -> searchengine_20211025_models.ModifyPausePolicyResponse:
        """
        @param request: ModifyPausePolicyRequest
        @return: ModifyPausePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_pause_policy_with_options(instance_id, request, headers, runtime)

    async def modify_pause_policy_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPausePolicyRequest,
    ) -> searchengine_20211025_models.ModifyPausePolicyResponse:
        """
        @param request: ModifyPausePolicyRequest
        @return: ModifyPausePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_pause_policy_with_options_async(instance_id, request, headers, runtime)

    def modify_public_url_ip_list_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPublicUrlIpListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyPublicUrlIpListResponse:
        """
        @summary 修改公网域名访问白名单
        
        @param request: ModifyPublicUrlIpListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPublicUrlIpListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPublicUrlIpList',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/public-url-ip-list',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyPublicUrlIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_public_url_ip_list_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPublicUrlIpListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyPublicUrlIpListResponse:
        """
        @summary 修改公网域名访问白名单
        
        @param request: ModifyPublicUrlIpListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyPublicUrlIpListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPublicUrlIpList',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/public-url-ip-list',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyPublicUrlIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_public_url_ip_list(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPublicUrlIpListRequest,
    ) -> searchengine_20211025_models.ModifyPublicUrlIpListResponse:
        """
        @summary 修改公网域名访问白名单
        
        @param request: ModifyPublicUrlIpListRequest
        @return: ModifyPublicUrlIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_public_url_ip_list_with_options(instance_id, request, headers, runtime)

    async def modify_public_url_ip_list_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyPublicUrlIpListRequest,
    ) -> searchengine_20211025_models.ModifyPublicUrlIpListResponse:
        """
        @summary 修改公网域名访问白名单
        
        @param request: ModifyPublicUrlIpListRequest
        @return: ModifyPublicUrlIpListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_public_url_ip_list_with_options_async(instance_id, request, headers, runtime)

    def modify_table_with_options(
        self,
        instance_id: str,
        table_name: str,
        request: searchengine_20211025_models.ModifyTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyTableResponse:
        """
        @summary Modifies an index table.
        
        @param request: ModifyTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.data_process_config):
            body['dataProcessConfig'] = request.data_process_config
        if not UtilClient.is_unset(request.data_source):
            body['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.field_schema):
            body['fieldSchema'] = request.field_schema
        if not UtilClient.is_unset(request.partition_count):
            body['partitionCount'] = request.partition_count
        if not UtilClient.is_unset(request.primary_key):
            body['primaryKey'] = request.primary_key
        if not UtilClient.is_unset(request.raw_schema):
            body['rawSchema'] = request.raw_schema
        if not UtilClient.is_unset(request.vector_index):
            body['vectorIndex'] = request.vector_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTable',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_table_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        request: searchengine_20211025_models.ModifyTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyTableResponse:
        """
        @summary Modifies an index table.
        
        @param request: ModifyTableRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.data_process_config):
            body['dataProcessConfig'] = request.data_process_config
        if not UtilClient.is_unset(request.data_source):
            body['dataSource'] = request.data_source
        if not UtilClient.is_unset(request.field_schema):
            body['fieldSchema'] = request.field_schema
        if not UtilClient.is_unset(request.partition_count):
            body['partitionCount'] = request.partition_count
        if not UtilClient.is_unset(request.primary_key):
            body['primaryKey'] = request.primary_key
        if not UtilClient.is_unset(request.raw_schema):
            body['rawSchema'] = request.raw_schema
        if not UtilClient.is_unset(request.vector_index):
            body['vectorIndex'] = request.vector_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyTable',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_table(
        self,
        instance_id: str,
        table_name: str,
        request: searchengine_20211025_models.ModifyTableRequest,
    ) -> searchengine_20211025_models.ModifyTableResponse:
        """
        @summary Modifies an index table.
        
        @param request: ModifyTableRequest
        @return: ModifyTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_table_with_options(instance_id, table_name, request, headers, runtime)

    async def modify_table_async(
        self,
        instance_id: str,
        table_name: str,
        request: searchengine_20211025_models.ModifyTableRequest,
    ) -> searchengine_20211025_models.ModifyTableResponse:
        """
        @summary Modifies an index table.
        
        @param request: ModifyTableRequest
        @return: ModifyTableResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_table_with_options_async(instance_id, table_name, request, headers, runtime)

    def publish_advance_config_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.PublishAdvanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.PublishAdvanceConfigResponse:
        """
        @summary Publishes a version of advanced configurations.
        
        @description ## Method
        ~~~
        POST
        ~~~
        ## URI
        ~~~
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/actions/publish
        ~~~
        
        @param request: PublishAdvanceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishAdvanceConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/actions/publish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.PublishAdvanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_advance_config_with_options_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.PublishAdvanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.PublishAdvanceConfigResponse:
        """
        @summary Publishes a version of advanced configurations.
        
        @description ## Method
        ~~~
        POST
        ~~~
        ## URI
        ~~~
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/actions/publish
        ~~~
        
        @param request: PublishAdvanceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishAdvanceConfigResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.desc):
            body['desc'] = request.desc
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishAdvanceConfig',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/advanced-configs/{OpenApiUtilClient.get_encode_param(config_name)}/actions/publish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.PublishAdvanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_advance_config(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.PublishAdvanceConfigRequest,
    ) -> searchengine_20211025_models.PublishAdvanceConfigResponse:
        """
        @summary Publishes a version of advanced configurations.
        
        @description ## Method
        ~~~
        POST
        ~~~
        ## URI
        ~~~
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/actions/publish
        ~~~
        
        @param request: PublishAdvanceConfigRequest
        @return: PublishAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_advance_config_with_options(instance_id, config_name, request, headers, runtime)

    async def publish_advance_config_async(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.PublishAdvanceConfigRequest,
    ) -> searchengine_20211025_models.PublishAdvanceConfigResponse:
        """
        @summary Publishes a version of advanced configurations.
        
        @description ## Method
        ~~~
        POST
        ~~~
        ## URI
        ~~~
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/actions/publish
        ~~~
        
        @param request: PublishAdvanceConfigRequest
        @return: PublishAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_advance_config_with_options_async(instance_id, config_name, request, headers, runtime)

    def publish_index_version_with_options(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.PublishIndexVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.PublishIndexVersionResponse:
        """
        @summary Publishes a specified index version.
        
        @description ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/actions/publish
        
        @param request: PublishIndexVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishIndexVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/actions/publish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.PublishIndexVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_index_version_with_options_async(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.PublishIndexVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.PublishIndexVersionResponse:
        """
        @summary Publishes a specified index version.
        
        @description ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/actions/publish
        
        @param request: PublishIndexVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishIndexVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishIndexVersion',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/actions/publish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.PublishIndexVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_index_version(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.PublishIndexVersionRequest,
    ) -> searchengine_20211025_models.PublishIndexVersionResponse:
        """
        @summary Publishes a specified index version.
        
        @description ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/actions/publish
        
        @param request: PublishIndexVersionRequest
        @return: PublishIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_index_version_with_options(instance_id, index_name, request, headers, runtime)

    async def publish_index_version_async(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.PublishIndexVersionRequest,
    ) -> searchengine_20211025_models.PublishIndexVersionResponse:
        """
        @summary Publishes a specified index version.
        
        @description ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/actions/publish
        
        @param request: PublishIndexVersionRequest
        @return: PublishIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_index_version_with_options_async(instance_id, index_name, request, headers, runtime)

    def push_documents_with_options(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.PushDocumentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.PushDocumentsResponse:
        """
        @param request: PushDocumentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushDocumentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pk_field):
            query['pkField'] = request.pk_field
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='PushDocuments',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.PushDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_documents_with_options_async(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.PushDocumentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.PushDocumentsResponse:
        """
        @param request: PushDocumentsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushDocumentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pk_field):
            query['pkField'] = request.pk_field
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='PushDocuments',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}/actions/bulk',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.PushDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_documents(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.PushDocumentsRequest,
    ) -> searchengine_20211025_models.PushDocumentsResponse:
        """
        @param request: PushDocumentsRequest
        @return: PushDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_documents_with_options(instance_id, data_source_name, request, headers, runtime)

    async def push_documents_async(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.PushDocumentsRequest,
    ) -> searchengine_20211025_models.PushDocumentsResponse:
        """
        @param request: PushDocumentsRequest
        @return: PushDocumentsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_documents_with_options_async(instance_id, data_source_name, request, headers, runtime)

    def recover_index_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.RecoverIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.RecoverIndexResponse:
        """
        @summary Restores data from an index.
        
        @description ### Method
        `POST`
        ### URI
        `/openapi/ha3/instances/{instanceId}/recover-index`
        
        @param request: RecoverIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoverIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_deploy_id):
            body['buildDeployId'] = request.build_deploy_id
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.index_name):
            body['indexName'] = request.index_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecoverIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/recover-index',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.RecoverIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_index_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.RecoverIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.RecoverIndexResponse:
        """
        @summary Restores data from an index.
        
        @description ### Method
        `POST`
        ### URI
        `/openapi/ha3/instances/{instanceId}/recover-index`
        
        @param request: RecoverIndexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecoverIndexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.build_deploy_id):
            body['buildDeployId'] = request.build_deploy_id
        if not UtilClient.is_unset(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.generation):
            body['generation'] = request.generation
        if not UtilClient.is_unset(request.index_name):
            body['indexName'] = request.index_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecoverIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/recover-index',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.RecoverIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_index(
        self,
        instance_id: str,
        request: searchengine_20211025_models.RecoverIndexRequest,
    ) -> searchengine_20211025_models.RecoverIndexResponse:
        """
        @summary Restores data from an index.
        
        @description ### Method
        `POST`
        ### URI
        `/openapi/ha3/instances/{instanceId}/recover-index`
        
        @param request: RecoverIndexRequest
        @return: RecoverIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recover_index_with_options(instance_id, request, headers, runtime)

    async def recover_index_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.RecoverIndexRequest,
    ) -> searchengine_20211025_models.RecoverIndexResponse:
        """
        @summary Restores data from an index.
        
        @description ### Method
        `POST`
        ### URI
        `/openapi/ha3/instances/{instanceId}/recover-index`
        
        @param request: RecoverIndexRequest
        @return: RecoverIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recover_index_with_options_async(instance_id, request, headers, runtime)

    def reindex_with_options(
        self,
        instance_id: str,
        table_name: str,
        request: searchengine_20211025_models.ReindexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ReindexResponse:
        """
        @summary Rebuilds an index.
        
        @param request: ReindexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReindexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_time_sec):
            body['dataTimeSec'] = request.data_time_sec
        if not UtilClient.is_unset(request.oss_data_path):
            body['ossDataPath'] = request.oss_data_path
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Reindex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/reindex',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ReindexResponse(),
            self.call_api(params, req, runtime)
        )

    async def reindex_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        request: searchengine_20211025_models.ReindexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ReindexResponse:
        """
        @summary Rebuilds an index.
        
        @param request: ReindexRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReindexResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_time_sec):
            body['dataTimeSec'] = request.data_time_sec
        if not UtilClient.is_unset(request.oss_data_path):
            body['ossDataPath'] = request.oss_data_path
        if not UtilClient.is_unset(request.partition):
            body['partition'] = request.partition
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Reindex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/tables/{OpenApiUtilClient.get_encode_param(table_name)}/reindex',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ReindexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reindex(
        self,
        instance_id: str,
        table_name: str,
        request: searchengine_20211025_models.ReindexRequest,
    ) -> searchengine_20211025_models.ReindexResponse:
        """
        @summary Rebuilds an index.
        
        @param request: ReindexRequest
        @return: ReindexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reindex_with_options(instance_id, table_name, request, headers, runtime)

    async def reindex_async(
        self,
        instance_id: str,
        table_name: str,
        request: searchengine_20211025_models.ReindexRequest,
    ) -> searchengine_20211025_models.ReindexResponse:
        """
        @summary Rebuilds an index.
        
        @param request: ReindexRequest
        @return: ReindexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reindex_with_options_async(instance_id, table_name, request, headers, runtime)

    def remove_cluster_with_options(
        self,
        instance_id: str,
        cluster_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.RemoveClusterResponse:
        """
        @summary Deletes a cluster.
        
        @description ### Method
        ```java
        DELETE
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveClusterResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveCluster',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters/{OpenApiUtilClient.get_encode_param(cluster_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.RemoveClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cluster_with_options_async(
        self,
        instance_id: str,
        cluster_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.RemoveClusterResponse:
        """
        @summary Deletes a cluster.
        
        @description ### Method
        ```java
        DELETE
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveClusterResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='RemoveCluster',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/clusters/{OpenApiUtilClient.get_encode_param(cluster_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.RemoveClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cluster(
        self,
        instance_id: str,
        cluster_name: str,
    ) -> searchengine_20211025_models.RemoveClusterResponse:
        """
        @summary Deletes a cluster.
        
        @description ### Method
        ```java
        DELETE
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}
        ```
        
        @return: RemoveClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_cluster_with_options(instance_id, cluster_name, headers, runtime)

    async def remove_cluster_async(
        self,
        instance_id: str,
        cluster_name: str,
    ) -> searchengine_20211025_models.RemoveClusterResponse:
        """
        @summary Deletes a cluster.
        
        @description ### Method
        ```java
        DELETE
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/clusters/{clusterName}
        ```
        
        @return: RemoveClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_cluster_with_options_async(instance_id, cluster_name, headers, runtime)

    def rename_folder_with_options(
        self,
        instance_id: str,
        database: str,
        folder_id: str,
        request: searchengine_20211025_models.RenameFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.RenameFolderResponse:
        """
        @param request: RenameFolderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameFolderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameFolder',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/folders/{OpenApiUtilClient.get_encode_param(folder_id)}/name',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.RenameFolderResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_folder_with_options_async(
        self,
        instance_id: str,
        database: str,
        folder_id: str,
        request: searchengine_20211025_models.RenameFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.RenameFolderResponse:
        """
        @param request: RenameFolderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenameFolderResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenameFolder',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/folders/{OpenApiUtilClient.get_encode_param(folder_id)}/name',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.RenameFolderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_folder(
        self,
        instance_id: str,
        database: str,
        folder_id: str,
        request: searchengine_20211025_models.RenameFolderRequest,
    ) -> searchengine_20211025_models.RenameFolderResponse:
        """
        @param request: RenameFolderRequest
        @return: RenameFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.rename_folder_with_options(instance_id, database, folder_id, request, headers, runtime)

    async def rename_folder_async(
        self,
        instance_id: str,
        database: str,
        folder_id: str,
        request: searchengine_20211025_models.RenameFolderRequest,
    ) -> searchengine_20211025_models.RenameFolderResponse:
        """
        @param request: RenameFolderRequest
        @return: RenameFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.rename_folder_with_options_async(instance_id, database, folder_id, request, headers, runtime)

    def start_index_with_options(
        self,
        instance_id: str,
        index_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.StartIndexResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartIndexResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/startIndex',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.StartIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_index_with_options_async(
        self,
        instance_id: str,
        index_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.StartIndexResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartIndexResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StartIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/startIndex',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.StartIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_index(
        self,
        instance_id: str,
        index_name: str,
    ) -> searchengine_20211025_models.StartIndexResponse:
        """
        @return: StartIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.start_index_with_options(instance_id, index_name, headers, runtime)

    async def start_index_async(
        self,
        instance_id: str,
        index_name: str,
    ) -> searchengine_20211025_models.StartIndexResponse:
        """
        @return: StartIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.start_index_with_options_async(instance_id, index_name, headers, runtime)

    def stop_index_with_options(
        self,
        instance_id: str,
        index_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.StopIndexResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopIndexResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/stopIndex',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.StopIndexResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_index_with_options_async(
        self,
        instance_id: str,
        index_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.StopIndexResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopIndexResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopIndex',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/indexes/{OpenApiUtilClient.get_encode_param(index_name)}/stopIndex',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.StopIndexResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_index(
        self,
        instance_id: str,
        index_name: str,
    ) -> searchengine_20211025_models.StopIndexResponse:
        """
        @return: StopIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_index_with_options(instance_id, index_name, headers, runtime)

    async def stop_index_async(
        self,
        instance_id: str,
        index_name: str,
    ) -> searchengine_20211025_models.StopIndexResponse:
        """
        @return: StopIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_index_with_options_async(instance_id, index_name, headers, runtime)

    def stop_task_with_options(
        self,
        instance_id: str,
        fsm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.StopTaskResponse:
        """
        @summary Stops an FSM task.
        
        @description ### [](#)Method
        ```java
        PUT
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/stop-task/{fsmId}
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopTask',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/stop-task/{OpenApiUtilClient.get_encode_param(fsm_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.StopTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_task_with_options_async(
        self,
        instance_id: str,
        fsm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.StopTaskResponse:
        """
        @summary Stops an FSM task.
        
        @description ### [](#)Method
        ```java
        PUT
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/stop-task/{fsmId}
        ```
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='StopTask',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/stop-task/{OpenApiUtilClient.get_encode_param(fsm_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.StopTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_task(
        self,
        instance_id: str,
        fsm_id: str,
    ) -> searchengine_20211025_models.StopTaskResponse:
        """
        @summary Stops an FSM task.
        
        @description ### [](#)Method
        ```java
        PUT
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/stop-task/{fsmId}
        ```
        
        @return: StopTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_task_with_options(instance_id, fsm_id, headers, runtime)

    async def stop_task_async(
        self,
        instance_id: str,
        fsm_id: str,
    ) -> searchengine_20211025_models.StopTaskResponse:
        """
        @summary Stops an FSM task.
        
        @description ### [](#)Method
        ```java
        PUT
        ```
        ### [](#uri)URI
        ```java
        /openapi/ha3/instances/{instanceId}/stop-task/{fsmId}
        ```
        
        @return: StopTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_task_with_options_async(instance_id, fsm_id, headers, runtime)

    def tag_resources_with_options(
        self,
        request: searchengine_20211025_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/resource-tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: searchengine_20211025_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/resource-tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: searchengine_20211025_models.TagResourcesRequest,
    ) -> searchengine_20211025_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: searchengine_20211025_models.TagResourcesRequest,
    ) -> searchengine_20211025_models.TagResourcesResponse:
        """
        @summary 打标签接口
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: searchengine_20211025_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param tmp_req: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = searchengine_20211025_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'tagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['tagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/resource-tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        tmp_req: searchengine_20211025_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param tmp_req: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = searchengine_20211025_models.UntagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'resourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'tagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['all'] = request.all
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['resourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['tagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/resource-tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: searchengine_20211025_models.UntagResourcesRequest,
    ) -> searchengine_20211025_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: searchengine_20211025_models.UntagResourcesRequest,
    ) -> searchengine_20211025_models.UntagResourcesResponse:
        """
        @summary 删标签接口
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UpdateInstanceResponse:
        """
        @summary Modifies the configuration of a specified instance.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @param request: UpdateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.order_type):
            body['orderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UpdateInstanceResponse:
        """
        @summary Modifies the configuration of a specified instance.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @param request: UpdateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.order_type):
            body['orderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        instance_id: str,
        request: searchengine_20211025_models.UpdateInstanceRequest,
    ) -> searchengine_20211025_models.UpdateInstanceResponse:
        """
        @summary Modifies the configuration of a specified instance.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(instance_id, request, headers, runtime)

    async def update_instance_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.UpdateInstanceRequest,
    ) -> searchengine_20211025_models.UpdateInstanceResponse:
        """
        @summary Modifies the configuration of a specified instance.
        
        @description ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)

    def update_sql_instance_content_with_options(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceContentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UpdateSqlInstanceContentResponse:
        """
        @param request: UpdateSqlInstanceContentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSqlInstanceContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSqlInstanceContent',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}/content',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UpdateSqlInstanceContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sql_instance_content_with_options_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceContentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UpdateSqlInstanceContentResponse:
        """
        @param request: UpdateSqlInstanceContentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSqlInstanceContentResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSqlInstanceContent',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}/content',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UpdateSqlInstanceContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sql_instance_content(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceContentRequest,
    ) -> searchengine_20211025_models.UpdateSqlInstanceContentResponse:
        """
        @param request: UpdateSqlInstanceContentRequest
        @return: UpdateSqlInstanceContentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_sql_instance_content_with_options(instance_id, database, sql_instance_id, request, headers, runtime)

    async def update_sql_instance_content_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceContentRequest,
    ) -> searchengine_20211025_models.UpdateSqlInstanceContentResponse:
        """
        @param request: UpdateSqlInstanceContentRequest
        @return: UpdateSqlInstanceContentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_sql_instance_content_with_options_async(instance_id, database, sql_instance_id, request, headers, runtime)

    def update_sql_instance_name_with_options(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UpdateSqlInstanceNameResponse:
        """
        @param request: UpdateSqlInstanceNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSqlInstanceNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSqlInstanceName',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}/name',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UpdateSqlInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sql_instance_name_with_options_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UpdateSqlInstanceNameResponse:
        """
        @param request: UpdateSqlInstanceNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSqlInstanceNameResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSqlInstanceName',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}/name',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UpdateSqlInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sql_instance_name(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceNameRequest,
    ) -> searchengine_20211025_models.UpdateSqlInstanceNameResponse:
        """
        @param request: UpdateSqlInstanceNameRequest
        @return: UpdateSqlInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_sql_instance_name_with_options(instance_id, database, sql_instance_id, request, headers, runtime)

    async def update_sql_instance_name_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceNameRequest,
    ) -> searchengine_20211025_models.UpdateSqlInstanceNameResponse:
        """
        @param request: UpdateSqlInstanceNameRequest
        @return: UpdateSqlInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_sql_instance_name_with_options_async(instance_id, database, sql_instance_id, request, headers, runtime)

    def update_sql_instance_params_with_options(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceParamsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UpdateSqlInstanceParamsResponse:
        """
        @param request: UpdateSqlInstanceParamsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSqlInstanceParamsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.combine_param):
            body['combineParam'] = request.combine_param
        if not UtilClient.is_unset(request.dynamic_param):
            body['dynamicParam'] = request.dynamic_param
        if not UtilClient.is_unset(request.kvpair):
            body['kvpair'] = request.kvpair
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.static_param):
            body['staticParam'] = request.static_param
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSqlInstanceParams',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}/params',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UpdateSqlInstanceParamsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sql_instance_params_with_options_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceParamsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UpdateSqlInstanceParamsResponse:
        """
        @param request: UpdateSqlInstanceParamsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSqlInstanceParamsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.combine_param):
            body['combineParam'] = request.combine_param
        if not UtilClient.is_unset(request.dynamic_param):
            body['dynamicParam'] = request.dynamic_param
        if not UtilClient.is_unset(request.kvpair):
            body['kvpair'] = request.kvpair
        if not UtilClient.is_unset(request.params):
            body['params'] = request.params
        if not UtilClient.is_unset(request.static_param):
            body['staticParam'] = request.static_param
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSqlInstanceParams',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/sql-studio/databases/{OpenApiUtilClient.get_encode_param(database)}/sql-instances/{OpenApiUtilClient.get_encode_param(sql_instance_id)}/params',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.UpdateSqlInstanceParamsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sql_instance_params(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceParamsRequest,
    ) -> searchengine_20211025_models.UpdateSqlInstanceParamsResponse:
        """
        @param request: UpdateSqlInstanceParamsRequest
        @return: UpdateSqlInstanceParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_sql_instance_params_with_options(instance_id, database, sql_instance_id, request, headers, runtime)

    async def update_sql_instance_params_async(
        self,
        instance_id: str,
        database: str,
        sql_instance_id: str,
        request: searchengine_20211025_models.UpdateSqlInstanceParamsRequest,
    ) -> searchengine_20211025_models.UpdateSqlInstanceParamsResponse:
        """
        @param request: UpdateSqlInstanceParamsRequest
        @return: UpdateSqlInstanceParamsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_sql_instance_params_with_options_async(instance_id, database, sql_instance_id, request, headers, runtime)
