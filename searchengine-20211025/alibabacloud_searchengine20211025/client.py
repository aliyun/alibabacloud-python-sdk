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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/actions/build-index
        
        @param request: BuildIndexRequest
        @return: BuildIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.build_index_with_options_async(instance_id, request, headers, runtime)

    def create_cluster_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateClusterResponse:
        """
        ### Method
        `POST`
        ### URI
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
        ### Method
        `POST`
        ### URI
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
        ### Method
        `POST`
        ### URI
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
        ### Method
        `POST`
        ### URI
        `/openapi/ha3/instances/{instanceId}/clusters`
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cluster_with_options_async(instance_id, request, headers, runtime)

    def create_data_source_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateDataSourceResponse:
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_data_source_with_options(instance_id, request, headers, runtime)

    async def create_data_source_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateDataSourceRequest,
    ) -> searchengine_20211025_models.CreateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_data_source_with_options_async(instance_id, request, headers, runtime)

    def create_index_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.CreateIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.CreateIndexResponse:
        """
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
        `POST`
        ### URI
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
        ### Method
        `POST`
        ### URI
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
        ### Method
        `POST`
        ### URI
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
        ### Method
        `POST`
        ### URI
        `/api/instances?dryRun=false`
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def delete_advance_config_with_options(
        self,
        instance_id: str,
        config_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteAdvanceConfigResponse:
        """
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
        DELETE
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}
        
        @return: DeleteAdvanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_advance_config_with_options_async(instance_id, config_name, headers, runtime)

    def delete_data_source_with_options(
        self,
        instance_id: str,
        data_source_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteDataSourceResponse:
        """
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
        `DELETE`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @return: DeleteDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_data_source_with_options_async(instance_id, data_source_name, headers, runtime)

    def delete_index_with_options(
        self,
        instance_id: str,
        index_name: str,
        request: searchengine_20211025_models.DeleteIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.DeleteIndexResponse:
        """
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
        `DELETE`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, headers, runtime)

    def force_switch_with_options(
        self,
        instance_id: str,
        fsm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ForceSwitchResponse:
        """
        \\### Method
        ```java
        PUT
        ```
        ### URI
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
        \\### Method
        ```java
        PUT
        ```
        ### URI
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
        \\### Method
        ```java
        PUT
        ```
        ### URI
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
        \\### Method
        ```java
        PUT
        ```
        ### URI
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_data_source_deploy_with_options(instance_id, deploy_name, data_source_name, headers, runtime)

    async def get_data_source_deploy_async(
        self,
        instance_id: str,
        deploy_name: str,
        data_source_name: str,
    ) -> searchengine_20211025_models.GetDataSourceDeployResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_data_source_deploy_with_options_async(instance_id, deploy_name, data_source_name, headers, runtime)

    def get_deploy_graph_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetDeployGraphResponse:
        """
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_index_with_options(instance_id, index_name, headers, runtime)

    async def get_index_async(
        self,
        instance_id: str,
        index_name: str,
    ) -> searchengine_20211025_models.GetIndexResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_index_with_options_async(instance_id, index_name, headers, runtime)

    def get_index_version_with_options(
        self,
        instance_id: str,
        cluster_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.GetIndexVersionResponse:
        """
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_config_with_options(instance_id, request, headers, runtime)

    async def get_node_config_async(
        self,
        instance_id: str,
        request: searchengine_20211025_models.GetNodeConfigRequest,
    ) -> searchengine_20211025_models.GetNodeConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_node_config_with_options_async(instance_id, request, headers, runtime)

    def list_advance_config_dir_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ListAdvanceConfigDirRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListAdvanceConfigDirResponse:
        """
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Sample requests
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
        ## Sample requests
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
        ## Sample requests
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
        ## Sample requests
        `GET /openapi/ha3/instances/ose-test1/advanced-configs`
        
        @param request: ListAdvanceConfigsRequest
        @return: ListAdvanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_advance_configs_with_options_async(instance_id, request, headers, runtime)

    def list_cluster_names_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListClusterNamesResponse:
        """
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ### Method
        ```java
        GET
        ```
        ### URI
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
        ### Method
        ```java
        GET
        ```
        ### URI
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
        ### Method
        ```java
        GET
        ```
        ### URI
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
        ### Method
        ```java
        GET
        ```
        ### URI
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
        `GET`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources`
        
        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_sources_with_options_async(instance_id, headers, runtime)

    def list_date_source_generations_with_options(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.ListDateSourceGenerationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListDateSourceGenerationsResponse:
        """
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}/generations?domainName={domainName}`
        
        @param request: ListDateSourceGenerationsRequest
        @return: ListDateSourceGenerationsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_date_source_generations_with_options_async(instance_id, data_source_name, request, headers, runtime)

    def list_indexes_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListIndexesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListIndexesResponse:
        """
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
        `GET`
        ### URI
        `/openapi/[code]/instances`
        
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
        ### Method
        `GET`
        ### URI
        `/openapi/[code]/instances`
        
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
        ### Method
        `GET`
        ### URI
        `/openapi/[code]/instances`
        
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
        ### Method
        `GET`
        ### URI
        `/openapi/[code]/instances`
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_online_configs_with_options(
        self,
        instance_id: str,
        node_name: str,
        request: searchengine_20211025_models.ListOnlineConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListOnlineConfigsResponse:
        """
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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

    def list_query_result_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ListQueryResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ListQueryResultResponse:
        """
        ### Method
        `GET`
        ### URI
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
        ### Method
        `GET`
        ### URI
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
        ### Method
        `GET`
        ### URI
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
        ### Method
        `GET`
        ### URI
        `/openapi/ha3/instances/{instanceId}/query?query=xxxx`
        
        @param request: ListQueryResultRequest
        @return: ListQueryResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_query_result_with_options_async(instance_id, request, headers, runtime)

    def modify_advance_config_file_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.ModifyAdvanceConfigFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyAdvanceConfigFileResponse:
        """
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
        put
        ## URI
        /openapi/ha3/instances/{instanceId}/advanced-configs/{configName}/file?fileName={fileName}
        
        @param request: ModifyAdvanceConfigFileRequest
        @return: ModifyAdvanceConfigFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_advance_config_file_with_options_async(instance_id, config_name, request, headers, runtime)

    def modify_cluster_desc_with_options(
        self,
        instance_id: str,
        cluster_name: str,
        request: searchengine_20211025_models.ModifyClusterDescRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyClusterDescResponse:
        """
        ### Method
        `PUT`
        ### URI
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
        ### Method
        `PUT`
        ### URI
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
        ### Method
        `PUT`
        ### URI
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
        ### Method
        `PUT`
        ### URI
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
        ## Request syntax
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
        ## Request syntax
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
        ## Request syntax
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
        ## Request syntax
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/cluster-online-config`
        
        @param request: ModifyClusterOnlineConfigRequest
        @return: ModifyClusterOnlineConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_cluster_online_config_with_options_async(instance_id, request, headers, runtime)

    def modify_data_source_with_options(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.ModifyDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyDataSourceResponse:
        """
        ## Method
        `PUT`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @param request: ModifyDataSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_source_with_options_async(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.ModifyDataSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyDataSourceResponse:
        """
        ## Method
        `PUT`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @param request: ModifyDataSourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataSourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        body = {}
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDataSource',
            version='2021-10-25',
            protocol='HTTPS',
            pathname=f'/openapi/ha3/instances/{OpenApiUtilClient.get_encode_param(instance_id)}/data-sources/{OpenApiUtilClient.get_encode_param(data_source_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            searchengine_20211025_models.ModifyDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_source(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.ModifyDataSourceRequest,
    ) -> searchengine_20211025_models.ModifyDataSourceResponse:
        """
        ## Method
        `PUT`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @param request: ModifyDataSourceRequest
        @return: ModifyDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_data_source_with_options(instance_id, data_source_name, request, headers, runtime)

    async def modify_data_source_async(
        self,
        instance_id: str,
        data_source_name: str,
        request: searchengine_20211025_models.ModifyDataSourceRequest,
    ) -> searchengine_20211025_models.ModifyDataSourceResponse:
        """
        ## Method
        `PUT`
        ## URI
        `/openapi/ha3/instances/{instanceId}/data-sources/{dataSourceName}`
        
        @param request: ModifyDataSourceRequest
        @return: ModifyDataSourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_data_source_with_options_async(instance_id, data_source_name, request, headers, runtime)

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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
        PUT
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/versions/{versionName}/file?fileName=/root/test.txt
        
        @param request: ModifyFileRequest
        @return: ModifyFileResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_file_with_options_async(instance_id, index_name, version_name, request, headers, runtime)

    def modify_index_partition_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.ModifyIndexPartitionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.ModifyIndexPartitionResponse:
        """
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ## Method
        PUT
        ## URI
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
        ## Method
        PUT
        ## URI
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
        ## Method
        PUT
        ## URI
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
        ## Method
        PUT
        ## URI
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}/password`
        
        @param request: ModifyPasswordRequest
        @return: ModifyPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_password_with_options_async(instance_id, request, headers, runtime)

    def publish_advance_config_with_options(
        self,
        instance_id: str,
        config_name: str,
        request: searchengine_20211025_models.PublishAdvanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.PublishAdvanceConfigResponse:
        """
        ## Method
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
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
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
        ## Method
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
        if not UtilClient.is_unset(request.body):
            body['body'] = request.body
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
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
        ## Method
        POST
        ## URI
        /openapi/ha3/instances/{instanceId}/indexes/{indexName}/actions/publish
        
        @param request: PublishIndexVersionRequest
        @return: PublishIndexVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_index_version_with_options_async(instance_id, index_name, request, headers, runtime)

    def recover_index_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.RecoverIndexRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.RecoverIndexResponse:
        """
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
        `POST`
        ### URI
        `/openapi/ha3/instances/{instanceId}/recover-index`
        
        @param request: RecoverIndexRequest
        @return: RecoverIndexResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recover_index_with_options_async(instance_id, request, headers, runtime)

    def remove_cluster_with_options(
        self,
        instance_id: str,
        cluster_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.RemoveClusterResponse:
        """
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
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

    def stop_task_with_options(
        self,
        instance_id: str,
        fsm_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.StopTaskResponse:
        """
        ### Method
        ```java
        PUT
        ```
        ### URI
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
        ### Method
        ```java
        PUT
        ```
        ### URI
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
        ### Method
        ```java
        PUT
        ```
        ### URI
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
        ### Method
        ```java
        PUT
        ```
        ### URI
        ```java
        /openapi/ha3/instances/{instanceId}/stop-task/{fsmId}
        ```
        
        @return: StopTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_task_with_options_async(instance_id, fsm_id, headers, runtime)

    def update_instance_with_options(
        self,
        instance_id: str,
        request: searchengine_20211025_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> searchengine_20211025_models.UpdateInstanceResponse:
        """
        ### Method
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
        ### Method
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
        ### Method
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
        ### Method
        `PUT`
        ### URI
        `/openapi/ha3/instances/{instanceId}`
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(instance_id, request, headers, runtime)
