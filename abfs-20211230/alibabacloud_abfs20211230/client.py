# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_abfs20211230 import models as abfs_20211230_models
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
        self._endpoint = self.get_endpoint('abfs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_back_flow(
        self,
        table_name: str,
        instance_id: str,
        request: abfs_20211230_models.CreateBackFlowRequest,
    ) -> abfs_20211230_models.CreateBackFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_back_flow_with_options(table_name, instance_id, request, headers, runtime)

    async def create_back_flow_async(
        self,
        table_name: str,
        instance_id: str,
        request: abfs_20211230_models.CreateBackFlowRequest,
    ) -> abfs_20211230_models.CreateBackFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_back_flow_with_options_async(table_name, instance_id, request, headers, runtime)

    def create_back_flow_with_options(
        self,
        table_name: str,
        instance_id: str,
        request: abfs_20211230_models.CreateBackFlowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.CreateBackFlowResponse:
        UtilClient.validate_model(request)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.odps_partition):
            body['odpsPartition'] = request.odps_partition
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBackFlow',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}/backflows',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.CreateBackFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_back_flow_with_options_async(
        self,
        table_name: str,
        instance_id: str,
        request: abfs_20211230_models.CreateBackFlowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.CreateBackFlowResponse:
        UtilClient.validate_model(request)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.odps_partition):
            body['odpsPartition'] = request.odps_partition
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBackFlow',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}/backflows',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.CreateBackFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_table(
        self,
        instance_id: str,
        request: abfs_20211230_models.CreateInstanceTableRequest,
    ) -> abfs_20211230_models.CreateInstanceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_table_with_options(instance_id, request, headers, runtime)

    async def create_instance_table_async(
        self,
        instance_id: str,
        request: abfs_20211230_models.CreateInstanceTableRequest,
    ) -> abfs_20211230_models.CreateInstanceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_table_with_options_async(instance_id, request, headers, runtime)

    def create_instance_table_with_options(
        self,
        instance_id: str,
        request: abfs_20211230_models.CreateInstanceTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.CreateInstanceTableResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.field_map):
            body['fieldMap'] = request.field_map
        if not UtilClient.is_unset(request.full_data_source_config):
            body['fullDataSourceConfig'] = request.full_data_source_config
        if not UtilClient.is_unset(request.inc_data_source_config):
            body['incDataSourceConfig'] = request.inc_data_source_config
        if not UtilClient.is_unset(request.index_type):
            body['indexType'] = request.index_type
        if not UtilClient.is_unset(request.table_name):
            body['tableName'] = request.table_name
        if not UtilClient.is_unset(request.trigger_mode):
            body['triggerMode'] = request.trigger_mode
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceTable',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.CreateInstanceTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_table_with_options_async(
        self,
        instance_id: str,
        request: abfs_20211230_models.CreateInstanceTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.CreateInstanceTableResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.field_map):
            body['fieldMap'] = request.field_map
        if not UtilClient.is_unset(request.full_data_source_config):
            body['fullDataSourceConfig'] = request.full_data_source_config
        if not UtilClient.is_unset(request.inc_data_source_config):
            body['incDataSourceConfig'] = request.inc_data_source_config
        if not UtilClient.is_unset(request.index_type):
            body['indexType'] = request.index_type
        if not UtilClient.is_unset(request.table_name):
            body['tableName'] = request.table_name
        if not UtilClient.is_unset(request.trigger_mode):
            body['triggerMode'] = request.trigger_mode
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstanceTable',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.CreateInstanceTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_table(
        self,
        table_name: str,
        instance_id: str,
    ) -> abfs_20211230_models.DeleteInstanceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_table_with_options(table_name, instance_id, headers, runtime)

    async def delete_instance_table_async(
        self,
        table_name: str,
        instance_id: str,
    ) -> abfs_20211230_models.DeleteInstanceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_table_with_options_async(table_name, instance_id, headers, runtime)

    def delete_instance_table_with_options(
        self,
        table_name: str,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.DeleteInstanceTableResponse:
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceTable',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.DeleteInstanceTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_table_with_options_async(
        self,
        table_name: str,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.DeleteInstanceTableResponse:
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteInstanceTable',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.DeleteInstanceTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_back_flow(
        self,
        table_name: str,
        instance_id: str,
        id: str,
    ) -> abfs_20211230_models.GetBackFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_back_flow_with_options(table_name, instance_id, id, headers, runtime)

    async def get_back_flow_async(
        self,
        table_name: str,
        instance_id: str,
        id: str,
    ) -> abfs_20211230_models.GetBackFlowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_back_flow_with_options_async(table_name, instance_id, id, headers, runtime)

    def get_back_flow_with_options(
        self,
        table_name: str,
        instance_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.GetBackFlowResponse:
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBackFlow',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}/backflows/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.GetBackFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_back_flow_with_options_async(
        self,
        table_name: str,
        instance_id: str,
        id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.GetBackFlowResponse:
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        id = OpenApiUtilClient.get_encode_param(id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetBackFlow',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}/backflows/{id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.GetBackFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_indexes(
        self,
        instance_id: str,
    ) -> abfs_20211230_models.GetIndexesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_indexes_with_options(instance_id, headers, runtime)

    async def get_indexes_async(
        self,
        instance_id: str,
    ) -> abfs_20211230_models.GetIndexesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_indexes_with_options_async(instance_id, headers, runtime)

    def get_indexes_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.GetIndexesResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndexes',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/indexes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.GetIndexesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_indexes_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.GetIndexesResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetIndexes',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/indexes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.GetIndexesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> abfs_20211230_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> abfs_20211230_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.GetInstanceResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.GetInstanceResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_table(
        self,
        instance_id: str,
        table_name: str,
    ) -> abfs_20211230_models.GetInstanceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_table_with_options(instance_id, table_name, headers, runtime)

    async def get_instance_table_async(
        self,
        instance_id: str,
        table_name: str,
    ) -> abfs_20211230_models.GetInstanceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_table_with_options_async(instance_id, table_name, headers, runtime)

    def get_instance_table_with_options(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.GetInstanceTableResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceTable',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.GetInstanceTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_table_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.GetInstanceTableResponse:
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetInstanceTable',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.GetInstanceTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_back_flows(
        self,
        table_name: str,
        instance_id: str,
        request: abfs_20211230_models.ListBackFlowsRequest,
    ) -> abfs_20211230_models.ListBackFlowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_back_flows_with_options(table_name, instance_id, request, headers, runtime)

    async def list_back_flows_async(
        self,
        table_name: str,
        instance_id: str,
        request: abfs_20211230_models.ListBackFlowsRequest,
    ) -> abfs_20211230_models.ListBackFlowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_back_flows_with_options_async(table_name, instance_id, request, headers, runtime)

    def list_back_flows_with_options(
        self,
        table_name: str,
        instance_id: str,
        request: abfs_20211230_models.ListBackFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.ListBackFlowsResponse:
        UtilClient.validate_model(request)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBackFlows',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}/backflows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.ListBackFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_back_flows_with_options_async(
        self,
        table_name: str,
        instance_id: str,
        request: abfs_20211230_models.ListBackFlowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.ListBackFlowsResponse:
        UtilClient.validate_model(request)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.limit):
            query['limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBackFlows',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}/backflows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.ListBackFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_table(
        self,
        instance_id: str,
        request: abfs_20211230_models.ListInstanceTableRequest,
    ) -> abfs_20211230_models.ListInstanceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instance_table_with_options(instance_id, request, headers, runtime)

    async def list_instance_table_async(
        self,
        instance_id: str,
        request: abfs_20211230_models.ListInstanceTableRequest,
    ) -> abfs_20211230_models.ListInstanceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instance_table_with_options_async(instance_id, request, headers, runtime)

    def list_instance_table_with_options(
        self,
        instance_id: str,
        request: abfs_20211230_models.ListInstanceTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.ListInstanceTableResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceTable',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.ListInstanceTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_table_with_options_async(
        self,
        instance_id: str,
        request: abfs_20211230_models.ListInstanceTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.ListInstanceTableResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceTable',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.ListInstanceTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: abfs_20211230_models.ListInstancesRequest,
    ) -> abfs_20211230_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: abfs_20211230_models.ListInstancesRequest,
    ) -> abfs_20211230_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        request: abfs_20211230_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: abfs_20211230_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_table(
        self,
        instance_id: str,
        table_name: str,
        request: abfs_20211230_models.UpdateInstanceTableRequest,
    ) -> abfs_20211230_models.UpdateInstanceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_table_with_options(instance_id, table_name, request, headers, runtime)

    async def update_instance_table_async(
        self,
        instance_id: str,
        table_name: str,
        request: abfs_20211230_models.UpdateInstanceTableRequest,
    ) -> abfs_20211230_models.UpdateInstanceTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_table_with_options_async(instance_id, table_name, request, headers, runtime)

    def update_instance_table_with_options(
        self,
        instance_id: str,
        table_name: str,
        request: abfs_20211230_models.UpdateInstanceTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.UpdateInstanceTableResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.field_map):
            body['fieldMap'] = request.field_map
        if not UtilClient.is_unset(request.full_data_source_config):
            body['fullDataSourceConfig'] = request.full_data_source_config
        if not UtilClient.is_unset(request.inc_data_source_config):
            body['incDataSourceConfig'] = request.inc_data_source_config
        if not UtilClient.is_unset(request.index_type):
            body['indexType'] = request.index_type
        if not UtilClient.is_unset(request.trigger_mode):
            body['triggerMode'] = request.trigger_mode
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceTable',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.UpdateInstanceTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_table_with_options_async(
        self,
        instance_id: str,
        table_name: str,
        request: abfs_20211230_models.UpdateInstanceTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> abfs_20211230_models.UpdateInstanceTableResponse:
        UtilClient.validate_model(request)
        instance_id = OpenApiUtilClient.get_encode_param(instance_id)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.field_map):
            body['fieldMap'] = request.field_map
        if not UtilClient.is_unset(request.full_data_source_config):
            body['fullDataSourceConfig'] = request.full_data_source_config
        if not UtilClient.is_unset(request.inc_data_source_config):
            body['incDataSourceConfig'] = request.inc_data_source_config
        if not UtilClient.is_unset(request.index_type):
            body['indexType'] = request.index_type
        if not UtilClient.is_unset(request.trigger_mode):
            body['triggerMode'] = request.trigger_mode
        if not UtilClient.is_unset(request.ttl):
            body['ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceTable',
            version='2021-12-30',
            protocol='HTTPS',
            pathname=f'/api/v1/instances/{instance_id}/tables/{table_name}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            abfs_20211230_models.UpdateInstanceTableResponse(),
            await self.call_api_async(params, req, runtime)
        )
