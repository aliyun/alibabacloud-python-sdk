# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_dms20250414 import models as main_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-shenzhen': 'dms.cn-shenzhen.aliyuncs.com',
            'cn-beijing': 'dms.cn-beijing.aliyuncs.com',
            'cn-shanghai': 'dms.cn-shanghai.aliyuncs.com',
            'cn-hongkong': 'dms.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'dms.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou': 'dms.cn-hangzhou.aliyuncs.com',
            'us-west-1': 'dms.us-west-1.aliyuncs.com',
            'us-east-1': 'dms.us-east-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_data_agent_memory_with_options(
        self,
        request: main_models.AddDataAgentMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataAgentMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.from_id):
            query['FromId'] = request.from_id
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.mem_from):
            query['MemFrom'] = request.mem_from
        if not DaraCore.is_null(request.session_uuid):
            query['SessionUuid'] = request.session_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDataAgentMemory',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataAgentMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_agent_memory_with_options_async(
        self,
        request: main_models.AddDataAgentMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddDataAgentMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.from_id):
            query['FromId'] = request.from_id
        if not DaraCore.is_null(request.label):
            query['Label'] = request.label
        if not DaraCore.is_null(request.mem_from):
            query['MemFrom'] = request.mem_from
        if not DaraCore.is_null(request.session_uuid):
            query['SessionUuid'] = request.session_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddDataAgentMemory',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataAgentMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_agent_memory(
        self,
        request: main_models.AddDataAgentMemoryRequest,
    ) -> main_models.AddDataAgentMemoryResponse:
        runtime = RuntimeOptions()
        return self.add_data_agent_memory_with_options(request, runtime)

    async def add_data_agent_memory_async(
        self,
        request: main_models.AddDataAgentMemoryRequest,
    ) -> main_models.AddDataAgentMemoryResponse:
        runtime = RuntimeOptions()
        return await self.add_data_agent_memory_with_options_async(request, runtime)

    def add_user_to_data_agent_workspace_with_options(
        self,
        request: main_models.AddUserToDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToDataAgentWorkspace',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToDataAgentWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_to_data_agent_workspace_with_options_async(
        self,
        request: main_models.AddUserToDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserToDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserToDataAgentWorkspace',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserToDataAgentWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_to_data_agent_workspace(
        self,
        request: main_models.AddUserToDataAgentWorkspaceRequest,
    ) -> main_models.AddUserToDataAgentWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.add_user_to_data_agent_workspace_with_options(request, runtime)

    async def add_user_to_data_agent_workspace_async(
        self,
        request: main_models.AddUserToDataAgentWorkspaceRequest,
    ) -> main_models.AddUserToDataAgentWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.add_user_to_data_agent_workspace_with_options_async(request, runtime)

    def batch_create_data_lake_partitions_with_options(
        self,
        tmp_req: main_models.BatchCreateDataLakePartitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCreateDataLakePartitionsResponse:
        tmp_req.validate()
        request = main_models.BatchCreateDataLakePartitionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_inputs):
            request.partition_inputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_inputs, 'PartitionInputs', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.if_not_exists):
            query['IfNotExists'] = request.if_not_exists
        if not DaraCore.is_null(request.need_result):
            query['NeedResult'] = request.need_result
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.partition_inputs_shrink):
            body['PartitionInputs'] = request.partition_inputs_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchCreateDataLakePartitions',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCreateDataLakePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_data_lake_partitions_with_options_async(
        self,
        tmp_req: main_models.BatchCreateDataLakePartitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCreateDataLakePartitionsResponse:
        tmp_req.validate()
        request = main_models.BatchCreateDataLakePartitionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_inputs):
            request.partition_inputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_inputs, 'PartitionInputs', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.if_not_exists):
            query['IfNotExists'] = request.if_not_exists
        if not DaraCore.is_null(request.need_result):
            query['NeedResult'] = request.need_result
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.partition_inputs_shrink):
            body['PartitionInputs'] = request.partition_inputs_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchCreateDataLakePartitions',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCreateDataLakePartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_data_lake_partitions(
        self,
        request: main_models.BatchCreateDataLakePartitionsRequest,
    ) -> main_models.BatchCreateDataLakePartitionsResponse:
        runtime = RuntimeOptions()
        return self.batch_create_data_lake_partitions_with_options(request, runtime)

    async def batch_create_data_lake_partitions_async(
        self,
        request: main_models.BatchCreateDataLakePartitionsRequest,
    ) -> main_models.BatchCreateDataLakePartitionsResponse:
        runtime = RuntimeOptions()
        return await self.batch_create_data_lake_partitions_with_options_async(request, runtime)

    def batch_delete_data_lake_partitions_with_options(
        self,
        request: main_models.BatchDeleteDataLakePartitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDataLakePartitionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.if_exists):
            query['IfExists'] = request.if_exists
        if not DaraCore.is_null(request.partition_values_list):
            query['PartitionValuesList'] = request.partition_values_list
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDataLakePartitions',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDataLakePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_data_lake_partitions_with_options_async(
        self,
        request: main_models.BatchDeleteDataLakePartitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteDataLakePartitionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.if_exists):
            query['IfExists'] = request.if_exists
        if not DaraCore.is_null(request.partition_values_list):
            query['PartitionValuesList'] = request.partition_values_list
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteDataLakePartitions',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteDataLakePartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_data_lake_partitions(
        self,
        request: main_models.BatchDeleteDataLakePartitionsRequest,
    ) -> main_models.BatchDeleteDataLakePartitionsResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_data_lake_partitions_with_options(request, runtime)

    async def batch_delete_data_lake_partitions_async(
        self,
        request: main_models.BatchDeleteDataLakePartitionsRequest,
    ) -> main_models.BatchDeleteDataLakePartitionsResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_data_lake_partitions_with_options_async(request, runtime)

    def batch_update_data_lake_partitions_with_options(
        self,
        tmp_req: main_models.BatchUpdateDataLakePartitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateDataLakePartitionsResponse:
        tmp_req.validate()
        request = main_models.BatchUpdateDataLakePartitionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_inputs):
            request.partition_inputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_inputs, 'PartitionInputs', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.partition_inputs_shrink):
            body['PartitionInputs'] = request.partition_inputs_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchUpdateDataLakePartitions',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateDataLakePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_data_lake_partitions_with_options_async(
        self,
        tmp_req: main_models.BatchUpdateDataLakePartitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateDataLakePartitionsResponse:
        tmp_req.validate()
        request = main_models.BatchUpdateDataLakePartitionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_inputs):
            request.partition_inputs_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_inputs, 'PartitionInputs', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.partition_inputs_shrink):
            body['PartitionInputs'] = request.partition_inputs_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchUpdateDataLakePartitions',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateDataLakePartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_data_lake_partitions(
        self,
        request: main_models.BatchUpdateDataLakePartitionsRequest,
    ) -> main_models.BatchUpdateDataLakePartitionsResponse:
        runtime = RuntimeOptions()
        return self.batch_update_data_lake_partitions_with_options(request, runtime)

    async def batch_update_data_lake_partitions_async(
        self,
        request: main_models.BatchUpdateDataLakePartitionsRequest,
    ) -> main_models.BatchUpdateDataLakePartitionsResponse:
        runtime = RuntimeOptions()
        return await self.batch_update_data_lake_partitions_with_options_async(request, runtime)

    def check_data_agent_memory_config_with_options(
        self,
        request: main_models.CheckDataAgentMemoryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDataAgentMemoryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDataAgentMemoryConfig',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDataAgentMemoryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_data_agent_memory_config_with_options_async(
        self,
        request: main_models.CheckDataAgentMemoryConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDataAgentMemoryConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDataAgentMemoryConfig',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDataAgentMemoryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_data_agent_memory_config(
        self,
        request: main_models.CheckDataAgentMemoryConfigRequest,
    ) -> main_models.CheckDataAgentMemoryConfigResponse:
        runtime = RuntimeOptions()
        return self.check_data_agent_memory_config_with_options(request, runtime)

    async def check_data_agent_memory_config_async(
        self,
        request: main_models.CheckDataAgentMemoryConfigRequest,
    ) -> main_models.CheckDataAgentMemoryConfigResponse:
        runtime = RuntimeOptions()
        return await self.check_data_agent_memory_config_with_options_async(request, runtime)

    def config_airflow_with_options(
        self,
        tmp_req: main_models.ConfigAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigAirflowResponse:
        tmp_req.validate()
        request = main_models.ConfigAirflowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_airflow_cfg):
            request.custom_airflow_cfg_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_airflow_cfg, 'CustomAirflowCfg', 'simple')
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not DaraCore.is_null(request.custom_airflow_cfg_shrink):
            query['CustomAirflowCfg'] = request.custom_airflow_cfg_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigAirflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_airflow_with_options_async(
        self,
        tmp_req: main_models.ConfigAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigAirflowResponse:
        tmp_req.validate()
        request = main_models.ConfigAirflowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_airflow_cfg):
            request.custom_airflow_cfg_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_airflow_cfg, 'CustomAirflowCfg', 'simple')
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not DaraCore.is_null(request.custom_airflow_cfg_shrink):
            query['CustomAirflowCfg'] = request.custom_airflow_cfg_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigAirflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_airflow(
        self,
        request: main_models.ConfigAirflowRequest,
    ) -> main_models.ConfigAirflowResponse:
        runtime = RuntimeOptions()
        return self.config_airflow_with_options(request, runtime)

    async def config_airflow_async(
        self,
        request: main_models.ConfigAirflowRequest,
    ) -> main_models.ConfigAirflowResponse:
        runtime = RuntimeOptions()
        return await self.config_airflow_with_options_async(request, runtime)

    def config_data_agent_memory_with_options(
        self,
        request: main_models.ConfigDataAgentMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigDataAgentMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.recall_enabled):
            query['RecallEnabled'] = request.recall_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigDataAgentMemory',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigDataAgentMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_data_agent_memory_with_options_async(
        self,
        request: main_models.ConfigDataAgentMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigDataAgentMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.enabled):
            query['Enabled'] = request.enabled
        if not DaraCore.is_null(request.recall_enabled):
            query['RecallEnabled'] = request.recall_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigDataAgentMemory',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigDataAgentMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_data_agent_memory(
        self,
        request: main_models.ConfigDataAgentMemoryRequest,
    ) -> main_models.ConfigDataAgentMemoryResponse:
        runtime = RuntimeOptions()
        return self.config_data_agent_memory_with_options(request, runtime)

    async def config_data_agent_memory_async(
        self,
        request: main_models.ConfigDataAgentMemoryRequest,
    ) -> main_models.ConfigDataAgentMemoryResponse:
        runtime = RuntimeOptions()
        return await self.config_data_agent_memory_with_options_async(request, runtime)

    def create_airflow_with_options(
        self,
        tmp_req: main_models.CreateAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAirflowResponse:
        tmp_req.validate()
        request = main_models.CreateAirflowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_mount_info_list):
            request.data_mount_info_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_mount_info_list, 'DataMountInfoList', 'json')
        query = {}
        if not DaraCore.is_null(request.airflow_name):
            query['AirflowName'] = request.airflow_name
        if not DaraCore.is_null(request.airflow_version):
            query['AirflowVersion'] = request.airflow_version
        if not DaraCore.is_null(request.app_spec):
            query['AppSpec'] = request.app_spec
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dags_dir):
            query['DagsDir'] = request.dags_dir
        if not DaraCore.is_null(request.data_mount_info_list_shrink):
            query['DataMountInfoList'] = request.data_mount_info_list_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_serverless):
            query['EnableServerless'] = request.enable_serverless
        if not DaraCore.is_null(request.graceful_shutdown_timeout):
            query['GracefulShutdownTimeout'] = request.graceful_shutdown_timeout
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_path):
            query['OssPath'] = request.oss_path
        if not DaraCore.is_null(request.plugins_dir):
            query['PluginsDir'] = request.plugins_dir
        if not DaraCore.is_null(request.requirement_file):
            query['RequirementFile'] = request.requirement_file
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.startup_file):
            query['StartupFile'] = request.startup_file
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.worker_serverless_replicas):
            query['WorkerServerlessReplicas'] = request.worker_serverless_replicas
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAirflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_airflow_with_options_async(
        self,
        tmp_req: main_models.CreateAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAirflowResponse:
        tmp_req.validate()
        request = main_models.CreateAirflowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_mount_info_list):
            request.data_mount_info_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_mount_info_list, 'DataMountInfoList', 'json')
        query = {}
        if not DaraCore.is_null(request.airflow_name):
            query['AirflowName'] = request.airflow_name
        if not DaraCore.is_null(request.airflow_version):
            query['AirflowVersion'] = request.airflow_version
        if not DaraCore.is_null(request.app_spec):
            query['AppSpec'] = request.app_spec
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dags_dir):
            query['DagsDir'] = request.dags_dir
        if not DaraCore.is_null(request.data_mount_info_list_shrink):
            query['DataMountInfoList'] = request.data_mount_info_list_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_serverless):
            query['EnableServerless'] = request.enable_serverless
        if not DaraCore.is_null(request.graceful_shutdown_timeout):
            query['GracefulShutdownTimeout'] = request.graceful_shutdown_timeout
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_path):
            query['OssPath'] = request.oss_path
        if not DaraCore.is_null(request.plugins_dir):
            query['PluginsDir'] = request.plugins_dir
        if not DaraCore.is_null(request.requirement_file):
            query['RequirementFile'] = request.requirement_file
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.startup_file):
            query['StartupFile'] = request.startup_file
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.worker_serverless_replicas):
            query['WorkerServerlessReplicas'] = request.worker_serverless_replicas
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAirflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_airflow(
        self,
        request: main_models.CreateAirflowRequest,
    ) -> main_models.CreateAirflowResponse:
        runtime = RuntimeOptions()
        return self.create_airflow_with_options(request, runtime)

    async def create_airflow_async(
        self,
        request: main_models.CreateAirflowRequest,
    ) -> main_models.CreateAirflowResponse:
        runtime = RuntimeOptions()
        return await self.create_airflow_with_options_async(request, runtime)

    def create_airflow_login_token_with_options(
        self,
        request: main_models.CreateAirflowLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAirflowLoginTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAirflowLoginToken',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAirflowLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_airflow_login_token_with_options_async(
        self,
        request: main_models.CreateAirflowLoginTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAirflowLoginTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAirflowLoginToken',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAirflowLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_airflow_login_token(
        self,
        request: main_models.CreateAirflowLoginTokenRequest,
    ) -> main_models.CreateAirflowLoginTokenResponse:
        runtime = RuntimeOptions()
        return self.create_airflow_login_token_with_options(request, runtime)

    async def create_airflow_login_token_async(
        self,
        request: main_models.CreateAirflowLoginTokenRequest,
    ) -> main_models.CreateAirflowLoginTokenResponse:
        runtime = RuntimeOptions()
        return await self.create_airflow_login_token_with_options_async(request, runtime)

    def create_custom_agent_with_options(
        self,
        tmp_req: main_models.CreateCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomAgentResponse:
        tmp_req.validate()
        request = main_models.CreateCustomAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.callback_config):
            request.callback_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.callback_config, 'CallbackConfig', 'json')
        if not DaraCore.is_null(tmp_req.execution_config):
            request.execution_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.execution_config, 'ExecutionConfig', 'json')
        if not DaraCore.is_null(tmp_req.knowledge_config_list):
            request.knowledge_config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_config_list, 'KnowledgeConfigList', 'json')
        if not DaraCore.is_null(tmp_req.knowledge_semantic_config_list):
            request.knowledge_semantic_config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_semantic_config_list, 'KnowledgeSemanticConfigList', 'json')
        if not DaraCore.is_null(tmp_req.schedule_task_config):
            request.schedule_task_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule_task_config, 'ScheduleTaskConfig', 'json')
        if not DaraCore.is_null(tmp_req.user_specified_skill_list):
            request.user_specified_skill_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_specified_skill_list, 'UserSpecifiedSkillList', 'json')
        query = {}
        if not DaraCore.is_null(request.callback_config_shrink):
            query['CallbackConfig'] = request.callback_config_shrink
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.data_json):
            query['DataJson'] = request.data_json
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_config_shrink):
            query['ExecutionConfig'] = request.execution_config_shrink
        if not DaraCore.is_null(request.instruction):
            query['Instruction'] = request.instruction
        if not DaraCore.is_null(request.knowledge):
            query['Knowledge'] = request.knowledge
        if not DaraCore.is_null(request.knowledge_config_list_shrink):
            query['KnowledgeConfigList'] = request.knowledge_config_list_shrink
        if not DaraCore.is_null(request.knowledge_semantic_config_list_shrink):
            query['KnowledgeSemanticConfigList'] = request.knowledge_semantic_config_list_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.related_session_id):
            query['RelatedSessionId'] = request.related_session_id
        if not DaraCore.is_null(request.schedule_task_config_shrink):
            query['ScheduleTaskConfig'] = request.schedule_task_config_shrink
        if not DaraCore.is_null(request.text_report_config):
            query['TextReportConfig'] = request.text_report_config
        if not DaraCore.is_null(request.user_specified_skill_list_shrink):
            query['UserSpecifiedSkillList'] = request.user_specified_skill_list_shrink
        if not DaraCore.is_null(request.web_report_config):
            query['WebReportConfig'] = request.web_report_config
        if not DaraCore.is_null(request.web_report_theme):
            query['WebReportTheme'] = request.web_report_theme
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_agent_with_options_async(
        self,
        tmp_req: main_models.CreateCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomAgentResponse:
        tmp_req.validate()
        request = main_models.CreateCustomAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.callback_config):
            request.callback_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.callback_config, 'CallbackConfig', 'json')
        if not DaraCore.is_null(tmp_req.execution_config):
            request.execution_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.execution_config, 'ExecutionConfig', 'json')
        if not DaraCore.is_null(tmp_req.knowledge_config_list):
            request.knowledge_config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_config_list, 'KnowledgeConfigList', 'json')
        if not DaraCore.is_null(tmp_req.knowledge_semantic_config_list):
            request.knowledge_semantic_config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_semantic_config_list, 'KnowledgeSemanticConfigList', 'json')
        if not DaraCore.is_null(tmp_req.schedule_task_config):
            request.schedule_task_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule_task_config, 'ScheduleTaskConfig', 'json')
        if not DaraCore.is_null(tmp_req.user_specified_skill_list):
            request.user_specified_skill_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_specified_skill_list, 'UserSpecifiedSkillList', 'json')
        query = {}
        if not DaraCore.is_null(request.callback_config_shrink):
            query['CallbackConfig'] = request.callback_config_shrink
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.data_json):
            query['DataJson'] = request.data_json
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_config_shrink):
            query['ExecutionConfig'] = request.execution_config_shrink
        if not DaraCore.is_null(request.instruction):
            query['Instruction'] = request.instruction
        if not DaraCore.is_null(request.knowledge):
            query['Knowledge'] = request.knowledge
        if not DaraCore.is_null(request.knowledge_config_list_shrink):
            query['KnowledgeConfigList'] = request.knowledge_config_list_shrink
        if not DaraCore.is_null(request.knowledge_semantic_config_list_shrink):
            query['KnowledgeSemanticConfigList'] = request.knowledge_semantic_config_list_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.related_session_id):
            query['RelatedSessionId'] = request.related_session_id
        if not DaraCore.is_null(request.schedule_task_config_shrink):
            query['ScheduleTaskConfig'] = request.schedule_task_config_shrink
        if not DaraCore.is_null(request.text_report_config):
            query['TextReportConfig'] = request.text_report_config
        if not DaraCore.is_null(request.user_specified_skill_list_shrink):
            query['UserSpecifiedSkillList'] = request.user_specified_skill_list_shrink
        if not DaraCore.is_null(request.web_report_config):
            query['WebReportConfig'] = request.web_report_config
        if not DaraCore.is_null(request.web_report_theme):
            query['WebReportTheme'] = request.web_report_theme
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_agent(
        self,
        request: main_models.CreateCustomAgentRequest,
    ) -> main_models.CreateCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.create_custom_agent_with_options(request, runtime)

    async def create_custom_agent_async(
        self,
        request: main_models.CreateCustomAgentRequest,
    ) -> main_models.CreateCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_agent_with_options_async(request, runtime)

    def create_data_agent_accuracy_test_with_options(
        self,
        request: main_models.CreateDataAgentAccuracyTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentAccuracyTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.dataset):
            query['Dataset'] = request.dataset
        if not DaraCore.is_null(request.datasource):
            query['Datasource'] = request.datasource
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.evaluation_prompt):
            query['EvaluationPrompt'] = request.evaluation_prompt
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.max_concurrent):
            query['MaxConcurrent'] = request.max_concurrent
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.need_delete):
            query['NeedDelete'] = request.need_delete
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentAccuracyTest',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentAccuracyTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_agent_accuracy_test_with_options_async(
        self,
        request: main_models.CreateDataAgentAccuracyTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentAccuracyTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.dataset):
            query['Dataset'] = request.dataset
        if not DaraCore.is_null(request.datasource):
            query['Datasource'] = request.datasource
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.evaluation_prompt):
            query['EvaluationPrompt'] = request.evaluation_prompt
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.max_concurrent):
            query['MaxConcurrent'] = request.max_concurrent
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.need_delete):
            query['NeedDelete'] = request.need_delete
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentAccuracyTest',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentAccuracyTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_agent_accuracy_test(
        self,
        request: main_models.CreateDataAgentAccuracyTestRequest,
    ) -> main_models.CreateDataAgentAccuracyTestResponse:
        runtime = RuntimeOptions()
        return self.create_data_agent_accuracy_test_with_options(request, runtime)

    async def create_data_agent_accuracy_test_async(
        self,
        request: main_models.CreateDataAgentAccuracyTestRequest,
    ) -> main_models.CreateDataAgentAccuracyTestResponse:
        runtime = RuntimeOptions()
        return await self.create_data_agent_accuracy_test_with_options_async(request, runtime)

    def create_data_agent_feedback_with_options(
        self,
        request: main_models.CreateDataAgentFeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentFeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.feedback_content):
            query['FeedbackContent'] = request.feedback_content
        if not DaraCore.is_null(request.feedback_type):
            query['FeedbackType'] = request.feedback_type
        if not DaraCore.is_null(request.like_value):
            query['LikeValue'] = request.like_value
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentFeedback',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_agent_feedback_with_options_async(
        self,
        request: main_models.CreateDataAgentFeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentFeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.feedback_content):
            query['FeedbackContent'] = request.feedback_content
        if not DaraCore.is_null(request.feedback_type):
            query['FeedbackType'] = request.feedback_type
        if not DaraCore.is_null(request.like_value):
            query['LikeValue'] = request.like_value
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.target_id):
            query['TargetId'] = request.target_id
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentFeedback',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_agent_feedback(
        self,
        request: main_models.CreateDataAgentFeedbackRequest,
    ) -> main_models.CreateDataAgentFeedbackResponse:
        runtime = RuntimeOptions()
        return self.create_data_agent_feedback_with_options(request, runtime)

    async def create_data_agent_feedback_async(
        self,
        request: main_models.CreateDataAgentFeedbackRequest,
    ) -> main_models.CreateDataAgentFeedbackResponse:
        runtime = RuntimeOptions()
        return await self.create_data_agent_feedback_with_options_async(request, runtime)

    def create_data_agent_knowledge_base_with_options(
        self,
        request: main_models.CreateDataAgentKnowledgeBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.from_kb_uuid):
            query['FromKbUuid'] = request.from_kb_uuid
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentKnowledgeBase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_agent_knowledge_base_with_options_async(
        self,
        request: main_models.CreateDataAgentKnowledgeBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.from_kb_uuid):
            query['FromKbUuid'] = request.from_kb_uuid
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentKnowledgeBase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_agent_knowledge_base(
        self,
        request: main_models.CreateDataAgentKnowledgeBaseRequest,
    ) -> main_models.CreateDataAgentKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        return self.create_data_agent_knowledge_base_with_options(request, runtime)

    async def create_data_agent_knowledge_base_async(
        self,
        request: main_models.CreateDataAgentKnowledgeBaseRequest,
    ) -> main_models.CreateDataAgentKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        return await self.create_data_agent_knowledge_base_with_options_async(request, runtime)

    def create_data_agent_session_with_options(
        self,
        tmp_req: main_models.CreateDataAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentSessionResponse:
        tmp_req.validate()
        request = main_models.CreateDataAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.session_config):
            request.session_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_config, 'SessionConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.file):
            query['File'] = request.file
        if not DaraCore.is_null(request.session_config_shrink):
            query['SessionConfig'] = request.session_config_shrink
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentSession',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_agent_session_with_options_async(
        self,
        tmp_req: main_models.CreateDataAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentSessionResponse:
        tmp_req.validate()
        request = main_models.CreateDataAgentSessionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.session_config):
            request.session_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_config, 'SessionConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.file):
            query['File'] = request.file
        if not DaraCore.is_null(request.session_config_shrink):
            query['SessionConfig'] = request.session_config_shrink
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentSession',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_agent_session(
        self,
        request: main_models.CreateDataAgentSessionRequest,
    ) -> main_models.CreateDataAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.create_data_agent_session_with_options(request, runtime)

    async def create_data_agent_session_async(
        self,
        request: main_models.CreateDataAgentSessionRequest,
    ) -> main_models.CreateDataAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.create_data_agent_session_with_options_async(request, runtime)

    def create_data_agent_skill_meta_with_options(
        self,
        request: main_models.CreateDataAgentSkillMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentSkillMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.upload_location):
            query['UploadLocation'] = request.upload_location
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentSkillMeta',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentSkillMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_agent_skill_meta_with_options_async(
        self,
        request: main_models.CreateDataAgentSkillMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentSkillMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.upload_location):
            query['UploadLocation'] = request.upload_location
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentSkillMeta',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentSkillMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_agent_skill_meta(
        self,
        request: main_models.CreateDataAgentSkillMetaRequest,
    ) -> main_models.CreateDataAgentSkillMetaResponse:
        runtime = RuntimeOptions()
        return self.create_data_agent_skill_meta_with_options(request, runtime)

    async def create_data_agent_skill_meta_async(
        self,
        request: main_models.CreateDataAgentSkillMetaRequest,
    ) -> main_models.CreateDataAgentSkillMetaResponse:
        runtime = RuntimeOptions()
        return await self.create_data_agent_skill_meta_with_options_async(request, runtime)

    def create_data_agent_theme_with_options(
        self,
        request: main_models.CreateDataAgentThemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentThemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_from):
            query['FileFrom'] = request.file_from
        if not DaraCore.is_null(request.theme_id):
            query['ThemeId'] = request.theme_id
        if not DaraCore.is_null(request.theme_name):
            query['ThemeName'] = request.theme_name
        if not DaraCore.is_null(request.theme_type):
            query['ThemeType'] = request.theme_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentTheme',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentThemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_agent_theme_with_options_async(
        self,
        request: main_models.CreateDataAgentThemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentThemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_from):
            query['FileFrom'] = request.file_from
        if not DaraCore.is_null(request.theme_id):
            query['ThemeId'] = request.theme_id
        if not DaraCore.is_null(request.theme_name):
            query['ThemeName'] = request.theme_name
        if not DaraCore.is_null(request.theme_type):
            query['ThemeType'] = request.theme_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentTheme',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentThemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_agent_theme(
        self,
        request: main_models.CreateDataAgentThemeRequest,
    ) -> main_models.CreateDataAgentThemeResponse:
        runtime = RuntimeOptions()
        return self.create_data_agent_theme_with_options(request, runtime)

    async def create_data_agent_theme_async(
        self,
        request: main_models.CreateDataAgentThemeRequest,
    ) -> main_models.CreateDataAgentThemeResponse:
        runtime = RuntimeOptions()
        return await self.create_data_agent_theme_with_options_async(request, runtime)

    def create_data_agent_workspace_with_options(
        self,
        request: main_models.CreateDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.is_session_share_enabled):
            query['IsSessionShareEnabled'] = request.is_session_share_enabled
        if not DaraCore.is_null(request.workspace_desc):
            query['WorkspaceDesc'] = request.workspace_desc
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentWorkspace',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_agent_workspace_with_options_async(
        self,
        request: main_models.CreateDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.is_session_share_enabled):
            query['IsSessionShareEnabled'] = request.is_session_share_enabled
        if not DaraCore.is_null(request.workspace_desc):
            query['WorkspaceDesc'] = request.workspace_desc
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataAgentWorkspace',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataAgentWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_agent_workspace(
        self,
        request: main_models.CreateDataAgentWorkspaceRequest,
    ) -> main_models.CreateDataAgentWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.create_data_agent_workspace_with_options(request, runtime)

    async def create_data_agent_workspace_async(
        self,
        request: main_models.CreateDataAgentWorkspaceRequest,
    ) -> main_models.CreateDataAgentWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.create_data_agent_workspace_with_options_async(request, runtime)

    def create_data_lake_database_with_options(
        self,
        tmp_req: main_models.CreateDataLakeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataLakeDatabaseResponse:
        tmp_req.validate()
        request = main_models.CreateDataLakeDatabaseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataLakeDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataLakeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_lake_database_with_options_async(
        self,
        tmp_req: main_models.CreateDataLakeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataLakeDatabaseResponse:
        tmp_req.validate()
        request = main_models.CreateDataLakeDatabaseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataLakeDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataLakeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_lake_database(
        self,
        request: main_models.CreateDataLakeDatabaseRequest,
    ) -> main_models.CreateDataLakeDatabaseResponse:
        runtime = RuntimeOptions()
        return self.create_data_lake_database_with_options(request, runtime)

    async def create_data_lake_database_async(
        self,
        request: main_models.CreateDataLakeDatabaseRequest,
    ) -> main_models.CreateDataLakeDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.create_data_lake_database_with_options_async(request, runtime)

    def create_data_lake_function_with_options(
        self,
        tmp_req: main_models.CreateDataLakeFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataLakeFunctionResponse:
        tmp_req.validate()
        request = main_models.CreateDataLakeFunctionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.function_input):
            request.function_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.function_input, 'FunctionInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.function_input_shrink):
            body['FunctionInput'] = request.function_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataLakeFunction',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataLakeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_lake_function_with_options_async(
        self,
        tmp_req: main_models.CreateDataLakeFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataLakeFunctionResponse:
        tmp_req.validate()
        request = main_models.CreateDataLakeFunctionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.function_input):
            request.function_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.function_input, 'FunctionInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.function_input_shrink):
            body['FunctionInput'] = request.function_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataLakeFunction',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataLakeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_lake_function(
        self,
        request: main_models.CreateDataLakeFunctionRequest,
    ) -> main_models.CreateDataLakeFunctionResponse:
        runtime = RuntimeOptions()
        return self.create_data_lake_function_with_options(request, runtime)

    async def create_data_lake_function_async(
        self,
        request: main_models.CreateDataLakeFunctionRequest,
    ) -> main_models.CreateDataLakeFunctionResponse:
        runtime = RuntimeOptions()
        return await self.create_data_lake_function_with_options_async(request, runtime)

    def create_data_lake_partition_with_options(
        self,
        tmp_req: main_models.CreateDataLakePartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataLakePartitionResponse:
        tmp_req.validate()
        request = main_models.CreateDataLakePartitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_input):
            request.partition_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_input, 'PartitionInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.if_not_exists):
            query['IfNotExists'] = request.if_not_exists
        if not DaraCore.is_null(request.need_result):
            query['NeedResult'] = request.need_result
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.partition_input_shrink):
            body['PartitionInput'] = request.partition_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataLakePartition',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataLakePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_lake_partition_with_options_async(
        self,
        tmp_req: main_models.CreateDataLakePartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataLakePartitionResponse:
        tmp_req.validate()
        request = main_models.CreateDataLakePartitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_input):
            request.partition_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_input, 'PartitionInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.if_not_exists):
            query['IfNotExists'] = request.if_not_exists
        if not DaraCore.is_null(request.need_result):
            query['NeedResult'] = request.need_result
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.partition_input_shrink):
            body['PartitionInput'] = request.partition_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataLakePartition',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataLakePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_lake_partition(
        self,
        request: main_models.CreateDataLakePartitionRequest,
    ) -> main_models.CreateDataLakePartitionResponse:
        runtime = RuntimeOptions()
        return self.create_data_lake_partition_with_options(request, runtime)

    async def create_data_lake_partition_async(
        self,
        request: main_models.CreateDataLakePartitionRequest,
    ) -> main_models.CreateDataLakePartitionResponse:
        runtime = RuntimeOptions()
        return await self.create_data_lake_partition_with_options_async(request, runtime)

    def create_data_lake_table_with_options(
        self,
        tmp_req: main_models.CreateDataLakeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataLakeTableResponse:
        tmp_req.validate()
        request = main_models.CreateDataLakeTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.table_input):
            request.table_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_input, 'TableInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.table_input_shrink):
            body['TableInput'] = request.table_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataLakeTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataLakeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_lake_table_with_options_async(
        self,
        tmp_req: main_models.CreateDataLakeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataLakeTableResponse:
        tmp_req.validate()
        request = main_models.CreateDataLakeTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.table_input):
            request.table_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_input, 'TableInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.table_input_shrink):
            body['TableInput'] = request.table_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataLakeTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataLakeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_lake_table(
        self,
        request: main_models.CreateDataLakeTableRequest,
    ) -> main_models.CreateDataLakeTableResponse:
        runtime = RuntimeOptions()
        return self.create_data_lake_table_with_options(request, runtime)

    async def create_data_lake_table_async(
        self,
        request: main_models.CreateDataLakeTableRequest,
    ) -> main_models.CreateDataLakeTableResponse:
        runtime = RuntimeOptions()
        return await self.create_data_lake_table_with_options_async(request, runtime)

    def create_one_meta_sql_template_with_options(
        self,
        request: main_models.CreateOneMetaSqlTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOneMetaSqlTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expr):
            query['Expr'] = request.expr
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.sql_params):
            query['SqlParams'] = request.sql_params
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOneMetaSqlTemplate',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOneMetaSqlTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_one_meta_sql_template_with_options_async(
        self,
        request: main_models.CreateOneMetaSqlTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOneMetaSqlTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expr):
            query['Expr'] = request.expr
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.sql_params):
            query['SqlParams'] = request.sql_params
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOneMetaSqlTemplate',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOneMetaSqlTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_one_meta_sql_template(
        self,
        request: main_models.CreateOneMetaSqlTemplateRequest,
    ) -> main_models.CreateOneMetaSqlTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_one_meta_sql_template_with_options(request, runtime)

    async def create_one_meta_sql_template_async(
        self,
        request: main_models.CreateOneMetaSqlTemplateRequest,
    ) -> main_models.CreateOneMetaSqlTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_one_meta_sql_template_with_options_async(request, runtime)

    def delete_airflow_with_options(
        self,
        request: main_models.DeleteAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAirflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAirflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_airflow_with_options_async(
        self,
        request: main_models.DeleteAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAirflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAirflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_airflow(
        self,
        request: main_models.DeleteAirflowRequest,
    ) -> main_models.DeleteAirflowResponse:
        runtime = RuntimeOptions()
        return self.delete_airflow_with_options(request, runtime)

    async def delete_airflow_async(
        self,
        request: main_models.DeleteAirflowRequest,
    ) -> main_models.DeleteAirflowResponse:
        runtime = RuntimeOptions()
        return await self.delete_airflow_with_options_async(request, runtime)

    def delete_custom_agent_with_options(
        self,
        request: main_models.DeleteCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_agent_with_options_async(
        self,
        request: main_models.DeleteCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_agent(
        self,
        request: main_models.DeleteCustomAgentRequest,
    ) -> main_models.DeleteCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_agent_with_options(request, runtime)

    async def delete_custom_agent_async(
        self,
        request: main_models.DeleteCustomAgentRequest,
    ) -> main_models.DeleteCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_agent_with_options_async(request, runtime)

    def delete_data_agent_with_options(
        self,
        request: main_models.DeleteDataAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_agent_with_options_async(
        self,
        request: main_models.DeleteDataAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_agent(
        self,
        request: main_models.DeleteDataAgentRequest,
    ) -> main_models.DeleteDataAgentResponse:
        runtime = RuntimeOptions()
        return self.delete_data_agent_with_options(request, runtime)

    async def delete_data_agent_async(
        self,
        request: main_models.DeleteDataAgentRequest,
    ) -> main_models.DeleteDataAgentResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_agent_with_options_async(request, runtime)

    def delete_data_agent_accuracy_test_with_options(
        self,
        request: main_models.DeleteDataAgentAccuracyTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentAccuracyTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentAccuracyTest',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentAccuracyTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_agent_accuracy_test_with_options_async(
        self,
        request: main_models.DeleteDataAgentAccuracyTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentAccuracyTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentAccuracyTest',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentAccuracyTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_agent_accuracy_test(
        self,
        request: main_models.DeleteDataAgentAccuracyTestRequest,
    ) -> main_models.DeleteDataAgentAccuracyTestResponse:
        runtime = RuntimeOptions()
        return self.delete_data_agent_accuracy_test_with_options(request, runtime)

    async def delete_data_agent_accuracy_test_async(
        self,
        request: main_models.DeleteDataAgentAccuracyTestRequest,
    ) -> main_models.DeleteDataAgentAccuracyTestResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_agent_accuracy_test_with_options_async(request, runtime)

    def delete_data_agent_knowledge_base_with_options(
        self,
        request: main_models.DeleteDataAgentKnowledgeBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.kb_uuid):
            query['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentKnowledgeBase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_agent_knowledge_base_with_options_async(
        self,
        request: main_models.DeleteDataAgentKnowledgeBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.kb_uuid):
            query['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentKnowledgeBase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_agent_knowledge_base(
        self,
        request: main_models.DeleteDataAgentKnowledgeBaseRequest,
    ) -> main_models.DeleteDataAgentKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        return self.delete_data_agent_knowledge_base_with_options(request, runtime)

    async def delete_data_agent_knowledge_base_async(
        self,
        request: main_models.DeleteDataAgentKnowledgeBaseRequest,
    ) -> main_models.DeleteDataAgentKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_agent_knowledge_base_with_options_async(request, runtime)

    def delete_data_agent_mcp_with_options(
        self,
        tmp_req: main_models.DeleteDataAgentMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentMcpResponse:
        tmp_req.validate()
        request = main_models.DeleteDataAgentMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.mcp_server_ids):
            request.mcp_server_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.mcp_server_ids, 'McpServerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.mcp_server_ids_shrink):
            query['McpServerIds'] = request.mcp_server_ids_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentMcp',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_agent_mcp_with_options_async(
        self,
        tmp_req: main_models.DeleteDataAgentMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentMcpResponse:
        tmp_req.validate()
        request = main_models.DeleteDataAgentMcpShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.mcp_server_ids):
            request.mcp_server_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.mcp_server_ids, 'McpServerIds', 'json')
        query = {}
        if not DaraCore.is_null(request.mcp_server_ids_shrink):
            query['McpServerIds'] = request.mcp_server_ids_shrink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentMcp',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_agent_mcp(
        self,
        request: main_models.DeleteDataAgentMcpRequest,
    ) -> main_models.DeleteDataAgentMcpResponse:
        runtime = RuntimeOptions()
        return self.delete_data_agent_mcp_with_options(request, runtime)

    async def delete_data_agent_mcp_async(
        self,
        request: main_models.DeleteDataAgentMcpRequest,
    ) -> main_models.DeleteDataAgentMcpResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_agent_mcp_with_options_async(request, runtime)

    def delete_data_agent_memory_with_options(
        self,
        request: main_models.DeleteDataAgentMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentMemory',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_agent_memory_with_options_async(
        self,
        request: main_models.DeleteDataAgentMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentMemory',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_agent_memory(
        self,
        request: main_models.DeleteDataAgentMemoryRequest,
    ) -> main_models.DeleteDataAgentMemoryResponse:
        runtime = RuntimeOptions()
        return self.delete_data_agent_memory_with_options(request, runtime)

    async def delete_data_agent_memory_async(
        self,
        request: main_models.DeleteDataAgentMemoryRequest,
    ) -> main_models.DeleteDataAgentMemoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_agent_memory_with_options_async(request, runtime)

    def delete_data_agent_skill_meta_with_options(
        self,
        request: main_models.DeleteDataAgentSkillMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentSkillMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentSkillMeta',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentSkillMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_agent_skill_meta_with_options_async(
        self,
        request: main_models.DeleteDataAgentSkillMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentSkillMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentSkillMeta',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentSkillMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_agent_skill_meta(
        self,
        request: main_models.DeleteDataAgentSkillMetaRequest,
    ) -> main_models.DeleteDataAgentSkillMetaResponse:
        runtime = RuntimeOptions()
        return self.delete_data_agent_skill_meta_with_options(request, runtime)

    async def delete_data_agent_skill_meta_async(
        self,
        request: main_models.DeleteDataAgentSkillMetaRequest,
    ) -> main_models.DeleteDataAgentSkillMetaResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_agent_skill_meta_with_options_async(request, runtime)

    def delete_data_agent_workspace_with_options(
        self,
        request: main_models.DeleteDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentWorkspace',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_agent_workspace_with_options_async(
        self,
        request: main_models.DeleteDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataAgentWorkspace',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataAgentWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_agent_workspace(
        self,
        request: main_models.DeleteDataAgentWorkspaceRequest,
    ) -> main_models.DeleteDataAgentWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.delete_data_agent_workspace_with_options(request, runtime)

    async def delete_data_agent_workspace_async(
        self,
        request: main_models.DeleteDataAgentWorkspaceRequest,
    ) -> main_models.DeleteDataAgentWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_agent_workspace_with_options_async(request, runtime)

    def delete_data_lake_database_with_options(
        self,
        request: main_models.DeleteDataLakeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLakeDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLakeDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLakeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_lake_database_with_options_async(
        self,
        request: main_models.DeleteDataLakeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLakeDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLakeDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLakeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_lake_database(
        self,
        request: main_models.DeleteDataLakeDatabaseRequest,
    ) -> main_models.DeleteDataLakeDatabaseResponse:
        runtime = RuntimeOptions()
        return self.delete_data_lake_database_with_options(request, runtime)

    async def delete_data_lake_database_async(
        self,
        request: main_models.DeleteDataLakeDatabaseRequest,
    ) -> main_models.DeleteDataLakeDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_lake_database_with_options_async(request, runtime)

    def delete_data_lake_function_with_options(
        self,
        request: main_models.DeleteDataLakeFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLakeFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLakeFunction',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLakeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_lake_function_with_options_async(
        self,
        request: main_models.DeleteDataLakeFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLakeFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLakeFunction',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLakeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_lake_function(
        self,
        request: main_models.DeleteDataLakeFunctionRequest,
    ) -> main_models.DeleteDataLakeFunctionResponse:
        runtime = RuntimeOptions()
        return self.delete_data_lake_function_with_options(request, runtime)

    async def delete_data_lake_function_async(
        self,
        request: main_models.DeleteDataLakeFunctionRequest,
    ) -> main_models.DeleteDataLakeFunctionResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_lake_function_with_options_async(request, runtime)

    def delete_data_lake_partition_with_options(
        self,
        tmp_req: main_models.DeleteDataLakePartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLakePartitionResponse:
        tmp_req.validate()
        request = main_models.DeleteDataLakePartitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_values):
            request.partition_values_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_values, 'PartitionValues', 'simple')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.if_exists):
            query['IfExists'] = request.if_exists
        if not DaraCore.is_null(request.partition_values_shrink):
            query['PartitionValues'] = request.partition_values_shrink
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLakePartition',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLakePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_lake_partition_with_options_async(
        self,
        tmp_req: main_models.DeleteDataLakePartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLakePartitionResponse:
        tmp_req.validate()
        request = main_models.DeleteDataLakePartitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_values):
            request.partition_values_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_values, 'PartitionValues', 'simple')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.if_exists):
            query['IfExists'] = request.if_exists
        if not DaraCore.is_null(request.partition_values_shrink):
            query['PartitionValues'] = request.partition_values_shrink
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLakePartition',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLakePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_lake_partition(
        self,
        request: main_models.DeleteDataLakePartitionRequest,
    ) -> main_models.DeleteDataLakePartitionResponse:
        runtime = RuntimeOptions()
        return self.delete_data_lake_partition_with_options(request, runtime)

    async def delete_data_lake_partition_async(
        self,
        request: main_models.DeleteDataLakePartitionRequest,
    ) -> main_models.DeleteDataLakePartitionResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_lake_partition_with_options_async(request, runtime)

    def delete_data_lake_table_with_options(
        self,
        request: main_models.DeleteDataLakeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLakeTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLakeTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLakeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_lake_table_with_options_async(
        self,
        request: main_models.DeleteDataLakeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLakeTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLakeTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLakeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_lake_table(
        self,
        request: main_models.DeleteDataLakeTableRequest,
    ) -> main_models.DeleteDataLakeTableResponse:
        runtime = RuntimeOptions()
        return self.delete_data_lake_table_with_options(request, runtime)

    async def delete_data_lake_table_async(
        self,
        request: main_models.DeleteDataLakeTableRequest,
    ) -> main_models.DeleteDataLakeTableResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_lake_table_with_options_async(request, runtime)

    def delete_document_with_options(
        self,
        request: main_models.DeleteDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocument',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_with_options_async(
        self,
        request: main_models.DeleteDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocument',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document(
        self,
        request: main_models.DeleteDocumentRequest,
    ) -> main_models.DeleteDocumentResponse:
        runtime = RuntimeOptions()
        return self.delete_document_with_options(request, runtime)

    async def delete_document_async(
        self,
        request: main_models.DeleteDocumentRequest,
    ) -> main_models.DeleteDocumentResponse:
        runtime = RuntimeOptions()
        return await self.delete_document_with_options_async(request, runtime)

    def delete_document_chunks_with_options(
        self,
        tmp_req: main_models.DeleteDocumentChunksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentChunksResponse:
        tmp_req.validate()
        request = main_models.DeleteDocumentChunksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.chunk_ids):
            request.chunk_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.chunk_ids, 'ChunkIds', 'json')
        body = {}
        if not DaraCore.is_null(request.chunk_ids_shrink):
            body['ChunkIds'] = request.chunk_ids_shrink
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocumentChunks',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentChunksResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_document_chunks_with_options_async(
        self,
        tmp_req: main_models.DeleteDocumentChunksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDocumentChunksResponse:
        tmp_req.validate()
        request = main_models.DeleteDocumentChunksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.chunk_ids):
            request.chunk_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.chunk_ids, 'ChunkIds', 'json')
        body = {}
        if not DaraCore.is_null(request.chunk_ids_shrink):
            body['ChunkIds'] = request.chunk_ids_shrink
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDocumentChunks',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDocumentChunksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_document_chunks(
        self,
        request: main_models.DeleteDocumentChunksRequest,
    ) -> main_models.DeleteDocumentChunksResponse:
        runtime = RuntimeOptions()
        return self.delete_document_chunks_with_options(request, runtime)

    async def delete_document_chunks_async(
        self,
        request: main_models.DeleteDocumentChunksRequest,
    ) -> main_models.DeleteDocumentChunksResponse:
        runtime = RuntimeOptions()
        return await self.delete_document_chunks_with_options_async(request, runtime)

    def delete_file_upload_with_options(
        self,
        request: main_models.DeleteFileUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFileUpload',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_upload_with_options_async(
        self,
        request: main_models.DeleteFileUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFileUpload',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file_upload(
        self,
        request: main_models.DeleteFileUploadRequest,
    ) -> main_models.DeleteFileUploadResponse:
        runtime = RuntimeOptions()
        return self.delete_file_upload_with_options(request, runtime)

    async def delete_file_upload_async(
        self,
        request: main_models.DeleteFileUploadRequest,
    ) -> main_models.DeleteFileUploadResponse:
        runtime = RuntimeOptions()
        return await self.delete_file_upload_with_options_async(request, runtime)

    def delete_one_meta_ossie_model_with_options(
        self,
        request: main_models.DeleteOneMetaOssieModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOneMetaOssieModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.knowledge_uuid):
            query['KnowledgeUuid'] = request.knowledge_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOneMetaOssieModel',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOneMetaOssieModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_one_meta_ossie_model_with_options_async(
        self,
        request: main_models.DeleteOneMetaOssieModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOneMetaOssieModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.knowledge_uuid):
            query['KnowledgeUuid'] = request.knowledge_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOneMetaOssieModel',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOneMetaOssieModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_one_meta_ossie_model(
        self,
        request: main_models.DeleteOneMetaOssieModelRequest,
    ) -> main_models.DeleteOneMetaOssieModelResponse:
        runtime = RuntimeOptions()
        return self.delete_one_meta_ossie_model_with_options(request, runtime)

    async def delete_one_meta_ossie_model_async(
        self,
        request: main_models.DeleteOneMetaOssieModelRequest,
    ) -> main_models.DeleteOneMetaOssieModelResponse:
        runtime = RuntimeOptions()
        return await self.delete_one_meta_ossie_model_with_options_async(request, runtime)

    def delete_one_meta_sql_template_with_options(
        self,
        request: main_models.DeleteOneMetaSqlTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOneMetaSqlTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.knowledge_uuid):
            query['KnowledgeUuid'] = request.knowledge_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOneMetaSqlTemplate',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOneMetaSqlTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_one_meta_sql_template_with_options_async(
        self,
        request: main_models.DeleteOneMetaSqlTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOneMetaSqlTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.knowledge_uuid):
            query['KnowledgeUuid'] = request.knowledge_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOneMetaSqlTemplate',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOneMetaSqlTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_one_meta_sql_template(
        self,
        request: main_models.DeleteOneMetaSqlTemplateRequest,
    ) -> main_models.DeleteOneMetaSqlTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_one_meta_sql_template_with_options(request, runtime)

    async def delete_one_meta_sql_template_async(
        self,
        request: main_models.DeleteOneMetaSqlTemplateRequest,
    ) -> main_models.DeleteOneMetaSqlTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_one_meta_sql_template_with_options_async(request, runtime)

    def delete_workspace_code_with_options(
        self,
        request: main_models.DeleteWorkspaceCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.repo):
            query['Repo'] = request.repo
        if not DaraCore.is_null(request.symlink):
            query['Symlink'] = request.symlink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspaceCode',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_code_with_options_async(
        self,
        request: main_models.DeleteWorkspaceCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkspaceCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.repo):
            query['Repo'] = request.repo
        if not DaraCore.is_null(request.symlink):
            query['Symlink'] = request.symlink
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkspaceCode',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkspaceCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace_code(
        self,
        request: main_models.DeleteWorkspaceCodeRequest,
    ) -> main_models.DeleteWorkspaceCodeResponse:
        runtime = RuntimeOptions()
        return self.delete_workspace_code_with_options(request, runtime)

    async def delete_workspace_code_async(
        self,
        request: main_models.DeleteWorkspaceCodeRequest,
    ) -> main_models.DeleteWorkspaceCodeResponse:
        runtime = RuntimeOptions()
        return await self.delete_workspace_code_with_options_async(request, runtime)

    def describe_custom_agent_with_options(
        self,
        request: main_models.DescribeCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_agent_with_options_async(
        self,
        request: main_models.DescribeCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_agent(
        self,
        request: main_models.DescribeCustomAgentRequest,
    ) -> main_models.DescribeCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_agent_with_options(request, runtime)

    async def describe_custom_agent_async(
        self,
        request: main_models.DescribeCustomAgentRequest,
    ) -> main_models.DescribeCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_agent_with_options_async(request, runtime)

    def describe_data_agent_metrics_with_options(
        self,
        request: main_models.DescribeDataAgentMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataAgentMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_names):
            query['MetricNames'] = request.metric_names
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataAgentMetrics',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataAgentMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_agent_metrics_with_options_async(
        self,
        request: main_models.DescribeDataAgentMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataAgentMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.metric_names):
            query['MetricNames'] = request.metric_names
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataAgentMetrics',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataAgentMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_agent_metrics(
        self,
        request: main_models.DescribeDataAgentMetricsRequest,
    ) -> main_models.DescribeDataAgentMetricsResponse:
        runtime = RuntimeOptions()
        return self.describe_data_agent_metrics_with_options(request, runtime)

    async def describe_data_agent_metrics_async(
        self,
        request: main_models.DescribeDataAgentMetricsRequest,
    ) -> main_models.DescribeDataAgentMetricsResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_agent_metrics_with_options_async(request, runtime)

    def describe_data_agent_session_with_options(
        self,
        request: main_models.DescribeDataAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataAgentSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataAgentSession',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_agent_session_with_options_async(
        self,
        request: main_models.DescribeDataAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataAgentSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataAgentSession',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_agent_session(
        self,
        request: main_models.DescribeDataAgentSessionRequest,
    ) -> main_models.DescribeDataAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.describe_data_agent_session_with_options(request, runtime)

    async def describe_data_agent_session_async(
        self,
        request: main_models.DescribeDataAgentSessionRequest,
    ) -> main_models.DescribeDataAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_agent_session_with_options_async(request, runtime)

    def describe_data_agent_theme_with_options(
        self,
        request: main_models.DescribeDataAgentThemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataAgentThemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.theme_id):
            query['ThemeId'] = request.theme_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataAgentTheme',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataAgentThemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_agent_theme_with_options_async(
        self,
        request: main_models.DescribeDataAgentThemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataAgentThemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.theme_id):
            query['ThemeId'] = request.theme_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataAgentTheme',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataAgentThemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_agent_theme(
        self,
        request: main_models.DescribeDataAgentThemeRequest,
    ) -> main_models.DescribeDataAgentThemeResponse:
        runtime = RuntimeOptions()
        return self.describe_data_agent_theme_with_options(request, runtime)

    async def describe_data_agent_theme_async(
        self,
        request: main_models.DescribeDataAgentThemeRequest,
    ) -> main_models.DescribeDataAgentThemeResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_agent_theme_with_options_async(request, runtime)

    def describe_document_with_options(
        self,
        request: main_models.DescribeDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocument',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_document_with_options_async(
        self,
        request: main_models.DescribeDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocument',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_document(
        self,
        request: main_models.DescribeDocumentRequest,
    ) -> main_models.DescribeDocumentResponse:
        runtime = RuntimeOptions()
        return self.describe_document_with_options(request, runtime)

    async def describe_document_async(
        self,
        request: main_models.DescribeDocumentRequest,
    ) -> main_models.DescribeDocumentResponse:
        runtime = RuntimeOptions()
        return await self.describe_document_with_options_async(request, runtime)

    def describe_file_upload_signature_with_options(
        self,
        request: main_models.DescribeFileUploadSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFileUploadSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFileUploadSignature',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFileUploadSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_upload_signature_with_options_async(
        self,
        request: main_models.DescribeFileUploadSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFileUploadSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFileUploadSignature',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFileUploadSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file_upload_signature(
        self,
        request: main_models.DescribeFileUploadSignatureRequest,
    ) -> main_models.DescribeFileUploadSignatureResponse:
        runtime = RuntimeOptions()
        return self.describe_file_upload_signature_with_options(request, runtime)

    async def describe_file_upload_signature_async(
        self,
        request: main_models.DescribeFileUploadSignatureRequest,
    ) -> main_models.DescribeFileUploadSignatureResponse:
        runtime = RuntimeOptions()
        return await self.describe_file_upload_signature_with_options_async(request, runtime)

    def describe_knowledge_base_stats_with_options(
        self,
        request: main_models.DescribeKnowledgeBaseStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKnowledgeBaseStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kb_uuid):
            query['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKnowledgeBaseStats',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKnowledgeBaseStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_knowledge_base_stats_with_options_async(
        self,
        request: main_models.DescribeKnowledgeBaseStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKnowledgeBaseStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kb_uuid):
            query['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKnowledgeBaseStats',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKnowledgeBaseStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_knowledge_base_stats(
        self,
        request: main_models.DescribeKnowledgeBaseStatsRequest,
    ) -> main_models.DescribeKnowledgeBaseStatsResponse:
        runtime = RuntimeOptions()
        return self.describe_knowledge_base_stats_with_options(request, runtime)

    async def describe_knowledge_base_stats_async(
        self,
        request: main_models.DescribeKnowledgeBaseStatsRequest,
    ) -> main_models.DescribeKnowledgeBaseStatsResponse:
        runtime = RuntimeOptions()
        return await self.describe_knowledge_base_stats_with_options_async(request, runtime)

    def describe_knowledge_base_upload_signature_with_options(
        self,
        request: main_models.DescribeKnowledgeBaseUploadSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKnowledgeBaseUploadSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kb_uuid):
            query['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKnowledgeBaseUploadSignature',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKnowledgeBaseUploadSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_knowledge_base_upload_signature_with_options_async(
        self,
        request: main_models.DescribeKnowledgeBaseUploadSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKnowledgeBaseUploadSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kb_uuid):
            query['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeKnowledgeBaseUploadSignature',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKnowledgeBaseUploadSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_knowledge_base_upload_signature(
        self,
        request: main_models.DescribeKnowledgeBaseUploadSignatureRequest,
    ) -> main_models.DescribeKnowledgeBaseUploadSignatureResponse:
        runtime = RuntimeOptions()
        return self.describe_knowledge_base_upload_signature_with_options(request, runtime)

    async def describe_knowledge_base_upload_signature_async(
        self,
        request: main_models.DescribeKnowledgeBaseUploadSignatureRequest,
    ) -> main_models.DescribeKnowledgeBaseUploadSignatureResponse:
        runtime = RuntimeOptions()
        return await self.describe_knowledge_base_upload_signature_with_options_async(request, runtime)

    def describe_skill_file_upload_signature_with_options(
        self,
        request: main_models.DescribeSkillFileUploadSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSkillFileUploadSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSkillFileUploadSignature',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSkillFileUploadSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_skill_file_upload_signature_with_options_async(
        self,
        request: main_models.DescribeSkillFileUploadSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSkillFileUploadSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSkillFileUploadSignature',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSkillFileUploadSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_skill_file_upload_signature(
        self,
        request: main_models.DescribeSkillFileUploadSignatureRequest,
    ) -> main_models.DescribeSkillFileUploadSignatureResponse:
        runtime = RuntimeOptions()
        return self.describe_skill_file_upload_signature_with_options(request, runtime)

    async def describe_skill_file_upload_signature_async(
        self,
        request: main_models.DescribeSkillFileUploadSignatureRequest,
    ) -> main_models.DescribeSkillFileUploadSignatureResponse:
        runtime = RuntimeOptions()
        return await self.describe_skill_file_upload_signature_with_options_async(request, runtime)

    def file_upload_callback_with_options(
        self,
        request: main_models.FileUploadCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FileUploadCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.file_size):
            query['FileSize'] = request.file_size
        if not DaraCore.is_null(request.filename):
            query['Filename'] = request.filename
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.upload_location):
            query['UploadLocation'] = request.upload_location
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FileUploadCallback',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileUploadCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def file_upload_callback_with_options_async(
        self,
        request: main_models.FileUploadCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FileUploadCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.file_size):
            query['FileSize'] = request.file_size
        if not DaraCore.is_null(request.filename):
            query['Filename'] = request.filename
        if not DaraCore.is_null(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not DaraCore.is_null(request.upload_location):
            query['UploadLocation'] = request.upload_location
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FileUploadCallback',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FileUploadCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def file_upload_callback(
        self,
        request: main_models.FileUploadCallbackRequest,
    ) -> main_models.FileUploadCallbackResponse:
        runtime = RuntimeOptions()
        return self.file_upload_callback_with_options(request, runtime)

    async def file_upload_callback_async(
        self,
        request: main_models.FileUploadCallbackRequest,
    ) -> main_models.FileUploadCallbackResponse:
        runtime = RuntimeOptions()
        return await self.file_upload_callback_with_options_async(request, runtime)

    def get_agentic_agent_by_install_token_with_options(
        self,
        request: main_models.GetAgenticAgentByInstallTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgenticAgentByInstallTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.install_token):
            query['InstallToken'] = request.install_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgenticAgentByInstallToken',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgenticAgentByInstallTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agentic_agent_by_install_token_with_options_async(
        self,
        request: main_models.GetAgenticAgentByInstallTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgenticAgentByInstallTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.install_token):
            query['InstallToken'] = request.install_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgenticAgentByInstallToken',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgenticAgentByInstallTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agentic_agent_by_install_token(
        self,
        request: main_models.GetAgenticAgentByInstallTokenRequest,
    ) -> main_models.GetAgenticAgentByInstallTokenResponse:
        runtime = RuntimeOptions()
        return self.get_agentic_agent_by_install_token_with_options(request, runtime)

    async def get_agentic_agent_by_install_token_async(
        self,
        request: main_models.GetAgenticAgentByInstallTokenRequest,
    ) -> main_models.GetAgenticAgentByInstallTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_agentic_agent_by_install_token_with_options_async(request, runtime)

    def get_airflow_with_options(
        self,
        request: main_models.GetAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAirflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAirflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_airflow_with_options_async(
        self,
        request: main_models.GetAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAirflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAirflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_airflow(
        self,
        request: main_models.GetAirflowRequest,
    ) -> main_models.GetAirflowResponse:
        runtime = RuntimeOptions()
        return self.get_airflow_with_options(request, runtime)

    async def get_airflow_async(
        self,
        request: main_models.GetAirflowRequest,
    ) -> main_models.GetAirflowResponse:
        runtime = RuntimeOptions()
        return await self.get_airflow_with_options_async(request, runtime)

    def get_chat_content_with_sse(
        self,
        request: main_models.GetChatContentRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.GetChatContentResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatContent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.GetChatContentResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def get_chat_content_with_sse_async(
        self,
        request: main_models.GetChatContentRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.GetChatContentResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatContent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.GetChatContentResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def get_chat_content_with_options(
        self,
        request: main_models.GetChatContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatContent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_content_with_options_async(
        self,
        request: main_models.GetChatContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChatContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChatContent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChatContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_content(
        self,
        request: main_models.GetChatContentRequest,
    ) -> main_models.GetChatContentResponse:
        runtime = RuntimeOptions()
        return self.get_chat_content_with_options(request, runtime)

    async def get_chat_content_async(
        self,
        request: main_models.GetChatContentRequest,
    ) -> main_models.GetChatContentResponse:
        runtime = RuntimeOptions()
        return await self.get_chat_content_with_options_async(request, runtime)

    def get_data_agent_mcp_with_options(
        self,
        request: main_models.GetDataAgentMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentMcpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mcp_server_id):
            query['McpServerId'] = request.mcp_server_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentMcp',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_agent_mcp_with_options_async(
        self,
        request: main_models.GetDataAgentMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentMcpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mcp_server_id):
            query['McpServerId'] = request.mcp_server_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentMcp',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_agent_mcp(
        self,
        request: main_models.GetDataAgentMcpRequest,
    ) -> main_models.GetDataAgentMcpResponse:
        runtime = RuntimeOptions()
        return self.get_data_agent_mcp_with_options(request, runtime)

    async def get_data_agent_mcp_async(
        self,
        request: main_models.GetDataAgentMcpRequest,
    ) -> main_models.GetDataAgentMcpResponse:
        runtime = RuntimeOptions()
        return await self.get_data_agent_mcp_with_options_async(request, runtime)

    def get_data_agent_sub_account_info_with_options(
        self,
        request: main_models.GetDataAgentSubAccountInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentSubAccountInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.sub_account_id):
            query['SubAccountId'] = request.sub_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentSubAccountInfo',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentSubAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_agent_sub_account_info_with_options_async(
        self,
        request: main_models.GetDataAgentSubAccountInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentSubAccountInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.sub_account_id):
            query['SubAccountId'] = request.sub_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentSubAccountInfo',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentSubAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_agent_sub_account_info(
        self,
        request: main_models.GetDataAgentSubAccountInfoRequest,
    ) -> main_models.GetDataAgentSubAccountInfoResponse:
        runtime = RuntimeOptions()
        return self.get_data_agent_sub_account_info_with_options(request, runtime)

    async def get_data_agent_sub_account_info_async(
        self,
        request: main_models.GetDataAgentSubAccountInfoRequest,
    ) -> main_models.GetDataAgentSubAccountInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_data_agent_sub_account_info_with_options_async(request, runtime)

    def get_data_agent_task_model_usage_with_options(
        self,
        tmp_req: main_models.GetDataAgentTaskModelUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentTaskModelUsageResponse:
        tmp_req.validate()
        request = main_models.GetDataAgentTaskModelUsageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.pay_level):
            query['PayLevel'] = request.pay_level
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentTaskModelUsage',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentTaskModelUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_agent_task_model_usage_with_options_async(
        self,
        tmp_req: main_models.GetDataAgentTaskModelUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentTaskModelUsageResponse:
        tmp_req.validate()
        request = main_models.GetDataAgentTaskModelUsageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.pay_level):
            query['PayLevel'] = request.pay_level
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentTaskModelUsage',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentTaskModelUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_agent_task_model_usage(
        self,
        request: main_models.GetDataAgentTaskModelUsageRequest,
    ) -> main_models.GetDataAgentTaskModelUsageResponse:
        runtime = RuntimeOptions()
        return self.get_data_agent_task_model_usage_with_options(request, runtime)

    async def get_data_agent_task_model_usage_async(
        self,
        request: main_models.GetDataAgentTaskModelUsageRequest,
    ) -> main_models.GetDataAgentTaskModelUsageResponse:
        runtime = RuntimeOptions()
        return await self.get_data_agent_task_model_usage_with_options_async(request, runtime)

    def get_data_agent_task_model_usage_metrics_with_options(
        self,
        tmp_req: main_models.GetDataAgentTaskModelUsageMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentTaskModelUsageMetricsResponse:
        tmp_req.validate()
        request = main_models.GetDataAgentTaskModelUsageMetricsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.pay_level):
            query['PayLevel'] = request.pay_level
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentTaskModelUsageMetrics',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentTaskModelUsageMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_agent_task_model_usage_metrics_with_options_async(
        self,
        tmp_req: main_models.GetDataAgentTaskModelUsageMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentTaskModelUsageMetricsResponse:
        tmp_req.validate()
        request = main_models.GetDataAgentTaskModelUsageMetricsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.pay_level):
            query['PayLevel'] = request.pay_level
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentTaskModelUsageMetrics',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentTaskModelUsageMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_agent_task_model_usage_metrics(
        self,
        request: main_models.GetDataAgentTaskModelUsageMetricsRequest,
    ) -> main_models.GetDataAgentTaskModelUsageMetricsResponse:
        runtime = RuntimeOptions()
        return self.get_data_agent_task_model_usage_metrics_with_options(request, runtime)

    async def get_data_agent_task_model_usage_metrics_async(
        self,
        request: main_models.GetDataAgentTaskModelUsageMetricsRequest,
    ) -> main_models.GetDataAgentTaskModelUsageMetricsResponse:
        runtime = RuntimeOptions()
        return await self.get_data_agent_task_model_usage_metrics_with_options_async(request, runtime)

    def get_data_agent_theme_upload_signature_with_options(
        self,
        request: main_models.GetDataAgentThemeUploadSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentThemeUploadSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.theme_id):
            query['ThemeId'] = request.theme_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentThemeUploadSignature',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentThemeUploadSignatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_agent_theme_upload_signature_with_options_async(
        self,
        request: main_models.GetDataAgentThemeUploadSignatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentThemeUploadSignatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.theme_id):
            query['ThemeId'] = request.theme_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentThemeUploadSignature',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentThemeUploadSignatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_agent_theme_upload_signature(
        self,
        request: main_models.GetDataAgentThemeUploadSignatureRequest,
    ) -> main_models.GetDataAgentThemeUploadSignatureResponse:
        runtime = RuntimeOptions()
        return self.get_data_agent_theme_upload_signature_with_options(request, runtime)

    async def get_data_agent_theme_upload_signature_async(
        self,
        request: main_models.GetDataAgentThemeUploadSignatureRequest,
    ) -> main_models.GetDataAgentThemeUploadSignatureResponse:
        runtime = RuntimeOptions()
        return await self.get_data_agent_theme_upload_signature_with_options_async(request, runtime)

    def get_data_agent_workspace_info_with_options(
        self,
        request: main_models.GetDataAgentWorkspaceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentWorkspaceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentWorkspaceInfo',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentWorkspaceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_agent_workspace_info_with_options_async(
        self,
        request: main_models.GetDataAgentWorkspaceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataAgentWorkspaceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataAgentWorkspaceInfo',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataAgentWorkspaceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_agent_workspace_info(
        self,
        request: main_models.GetDataAgentWorkspaceInfoRequest,
    ) -> main_models.GetDataAgentWorkspaceInfoResponse:
        runtime = RuntimeOptions()
        return self.get_data_agent_workspace_info_with_options(request, runtime)

    async def get_data_agent_workspace_info_async(
        self,
        request: main_models.GetDataAgentWorkspaceInfoRequest,
    ) -> main_models.GetDataAgentWorkspaceInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_data_agent_workspace_info_with_options_async(request, runtime)

    def get_data_lake_catalog_with_options(
        self,
        request: main_models.GetDataLakeCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataLakeCatalogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataLakeCatalog',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataLakeCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_lake_catalog_with_options_async(
        self,
        request: main_models.GetDataLakeCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataLakeCatalogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataLakeCatalog',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataLakeCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_lake_catalog(
        self,
        request: main_models.GetDataLakeCatalogRequest,
    ) -> main_models.GetDataLakeCatalogResponse:
        runtime = RuntimeOptions()
        return self.get_data_lake_catalog_with_options(request, runtime)

    async def get_data_lake_catalog_async(
        self,
        request: main_models.GetDataLakeCatalogRequest,
    ) -> main_models.GetDataLakeCatalogResponse:
        runtime = RuntimeOptions()
        return await self.get_data_lake_catalog_with_options_async(request, runtime)

    def get_data_lake_database_with_options(
        self,
        request: main_models.GetDataLakeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataLakeDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataLakeDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataLakeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_lake_database_with_options_async(
        self,
        request: main_models.GetDataLakeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataLakeDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataLakeDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataLakeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_lake_database(
        self,
        request: main_models.GetDataLakeDatabaseRequest,
    ) -> main_models.GetDataLakeDatabaseResponse:
        runtime = RuntimeOptions()
        return self.get_data_lake_database_with_options(request, runtime)

    async def get_data_lake_database_async(
        self,
        request: main_models.GetDataLakeDatabaseRequest,
    ) -> main_models.GetDataLakeDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.get_data_lake_database_with_options_async(request, runtime)

    def get_data_lake_function_with_options(
        self,
        request: main_models.GetDataLakeFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataLakeFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataLakeFunction',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataLakeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_lake_function_with_options_async(
        self,
        request: main_models.GetDataLakeFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataLakeFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataLakeFunction',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataLakeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_lake_function(
        self,
        request: main_models.GetDataLakeFunctionRequest,
    ) -> main_models.GetDataLakeFunctionResponse:
        runtime = RuntimeOptions()
        return self.get_data_lake_function_with_options(request, runtime)

    async def get_data_lake_function_async(
        self,
        request: main_models.GetDataLakeFunctionRequest,
    ) -> main_models.GetDataLakeFunctionResponse:
        runtime = RuntimeOptions()
        return await self.get_data_lake_function_with_options_async(request, runtime)

    def get_data_lake_partition_with_options(
        self,
        tmp_req: main_models.GetDataLakePartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataLakePartitionResponse:
        tmp_req.validate()
        request = main_models.GetDataLakePartitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_values):
            request.partition_values_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_values, 'PartitionValues', 'simple')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.partition_values_shrink):
            query['PartitionValues'] = request.partition_values_shrink
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataLakePartition',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataLakePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_lake_partition_with_options_async(
        self,
        tmp_req: main_models.GetDataLakePartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataLakePartitionResponse:
        tmp_req.validate()
        request = main_models.GetDataLakePartitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_values):
            request.partition_values_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_values, 'PartitionValues', 'simple')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.partition_values_shrink):
            query['PartitionValues'] = request.partition_values_shrink
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataLakePartition',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataLakePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_lake_partition(
        self,
        request: main_models.GetDataLakePartitionRequest,
    ) -> main_models.GetDataLakePartitionResponse:
        runtime = RuntimeOptions()
        return self.get_data_lake_partition_with_options(request, runtime)

    async def get_data_lake_partition_async(
        self,
        request: main_models.GetDataLakePartitionRequest,
    ) -> main_models.GetDataLakePartitionResponse:
        runtime = RuntimeOptions()
        return await self.get_data_lake_partition_with_options_async(request, runtime)

    def get_data_lake_table_with_options(
        self,
        request: main_models.GetDataLakeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataLakeTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataLakeTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataLakeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_lake_table_with_options_async(
        self,
        request: main_models.GetDataLakeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataLakeTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataLakeTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataLakeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_lake_table(
        self,
        request: main_models.GetDataLakeTableRequest,
    ) -> main_models.GetDataLakeTableResponse:
        runtime = RuntimeOptions()
        return self.get_data_lake_table_with_options(request, runtime)

    async def get_data_lake_table_async(
        self,
        request: main_models.GetDataLakeTableRequest,
    ) -> main_models.GetDataLakeTableResponse:
        runtime = RuntimeOptions()
        return await self.get_data_lake_table_with_options_async(request, runtime)

    def get_list_mcp_server_tools_result_with_options(
        self,
        request: main_models.GetListMcpServerToolsResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetListMcpServerToolsResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.mcp_server_uuid):
            query['McpServerUuid'] = request.mcp_server_uuid
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListMcpServerToolsResult',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetListMcpServerToolsResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_list_mcp_server_tools_result_with_options_async(
        self,
        request: main_models.GetListMcpServerToolsResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetListMcpServerToolsResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.mcp_server_uuid):
            query['McpServerUuid'] = request.mcp_server_uuid
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetListMcpServerToolsResult',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetListMcpServerToolsResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_list_mcp_server_tools_result(
        self,
        request: main_models.GetListMcpServerToolsResultRequest,
    ) -> main_models.GetListMcpServerToolsResultResponse:
        runtime = RuntimeOptions()
        return self.get_list_mcp_server_tools_result_with_options(request, runtime)

    async def get_list_mcp_server_tools_result_async(
        self,
        request: main_models.GetListMcpServerToolsResultRequest,
    ) -> main_models.GetListMcpServerToolsResultResponse:
        runtime = RuntimeOptions()
        return await self.get_list_mcp_server_tools_result_with_options_async(request, runtime)

    def get_notebook_and_submit_task_with_options(
        self,
        request: main_models.GetNotebookAndSubmitTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNotebookAndSubmitTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.retry):
            body['Retry'] = request.retry
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNotebookAndSubmitTask',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNotebookAndSubmitTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_notebook_and_submit_task_with_options_async(
        self,
        request: main_models.GetNotebookAndSubmitTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNotebookAndSubmitTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.params):
            body['Params'] = request.params
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.retry):
            body['Retry'] = request.retry
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNotebookAndSubmitTask',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNotebookAndSubmitTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_notebook_and_submit_task(
        self,
        request: main_models.GetNotebookAndSubmitTaskRequest,
    ) -> main_models.GetNotebookAndSubmitTaskResponse:
        runtime = RuntimeOptions()
        return self.get_notebook_and_submit_task_with_options(request, runtime)

    async def get_notebook_and_submit_task_async(
        self,
        request: main_models.GetNotebookAndSubmitTaskRequest,
    ) -> main_models.GetNotebookAndSubmitTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_notebook_and_submit_task_with_options_async(request, runtime)

    def get_notebook_task_status_with_options(
        self,
        request: main_models.GetNotebookTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNotebookTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNotebookTaskStatus',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNotebookTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_notebook_task_status_with_options_async(
        self,
        request: main_models.GetNotebookTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNotebookTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNotebookTaskStatus',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNotebookTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_notebook_task_status(
        self,
        request: main_models.GetNotebookTaskStatusRequest,
    ) -> main_models.GetNotebookTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.get_notebook_task_status_with_options(request, runtime)

    async def get_notebook_task_status_async(
        self,
        request: main_models.GetNotebookTaskStatusRequest,
    ) -> main_models.GetNotebookTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_notebook_task_status_with_options_async(request, runtime)

    def get_one_meta_ossie_model_with_options(
        self,
        request: main_models.GetOneMetaOssieModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOneMetaOssieModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_format):
            body['DocFormat'] = request.doc_format
        if not DaraCore.is_null(request.knowledge_uuid):
            body['KnowledgeUuid'] = request.knowledge_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOneMetaOssieModel',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOneMetaOssieModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_one_meta_ossie_model_with_options_async(
        self,
        request: main_models.GetOneMetaOssieModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOneMetaOssieModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.doc_format):
            body['DocFormat'] = request.doc_format
        if not DaraCore.is_null(request.knowledge_uuid):
            body['KnowledgeUuid'] = request.knowledge_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOneMetaOssieModel',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOneMetaOssieModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_one_meta_ossie_model(
        self,
        request: main_models.GetOneMetaOssieModelRequest,
    ) -> main_models.GetOneMetaOssieModelResponse:
        runtime = RuntimeOptions()
        return self.get_one_meta_ossie_model_with_options(request, runtime)

    async def get_one_meta_ossie_model_async(
        self,
        request: main_models.GetOneMetaOssieModelRequest,
    ) -> main_models.GetOneMetaOssieModelResponse:
        runtime = RuntimeOptions()
        return await self.get_one_meta_ossie_model_with_options_async(request, runtime)

    def get_sql_console_operation_log_with_options(
        self,
        request: main_models.GetSqlConsoleOperationLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlConsoleOperationLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlConsoleOperationLog',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlConsoleOperationLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_console_operation_log_with_options_async(
        self,
        request: main_models.GetSqlConsoleOperationLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlConsoleOperationLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.schema):
            query['Schema'] = request.schema
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlConsoleOperationLog',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlConsoleOperationLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_console_operation_log(
        self,
        request: main_models.GetSqlConsoleOperationLogRequest,
    ) -> main_models.GetSqlConsoleOperationLogResponse:
        runtime = RuntimeOptions()
        return self.get_sql_console_operation_log_with_options(request, runtime)

    async def get_sql_console_operation_log_async(
        self,
        request: main_models.GetSqlConsoleOperationLogRequest,
    ) -> main_models.GetSqlConsoleOperationLogResponse:
        runtime = RuntimeOptions()
        return await self.get_sql_console_operation_log_with_options_async(request, runtime)

    def get_workspace_code_with_options(
        self,
        request: main_models.GetWorkspaceCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iac):
            query['Iac'] = request.iac
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspaceCode',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_code_with_options_async(
        self,
        request: main_models.GetWorkspaceCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.iac):
            query['Iac'] = request.iac
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspaceCode',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace_code(
        self,
        request: main_models.GetWorkspaceCodeRequest,
    ) -> main_models.GetWorkspaceCodeResponse:
        runtime = RuntimeOptions()
        return self.get_workspace_code_with_options(request, runtime)

    async def get_workspace_code_async(
        self,
        request: main_models.GetWorkspaceCodeRequest,
    ) -> main_models.GetWorkspaceCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_workspace_code_with_options_async(request, runtime)

    def get_workspace_code_publish_setting_with_options(
        self,
        request: main_models.GetWorkspaceCodePublishSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceCodePublishSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspaceCodePublishSetting',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceCodePublishSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_code_publish_setting_with_options_async(
        self,
        request: main_models.GetWorkspaceCodePublishSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceCodePublishSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspaceCodePublishSetting',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceCodePublishSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace_code_publish_setting(
        self,
        request: main_models.GetWorkspaceCodePublishSettingRequest,
    ) -> main_models.GetWorkspaceCodePublishSettingResponse:
        runtime = RuntimeOptions()
        return self.get_workspace_code_publish_setting_with_options(request, runtime)

    async def get_workspace_code_publish_setting_async(
        self,
        request: main_models.GetWorkspaceCodePublishSettingRequest,
    ) -> main_models.GetWorkspaceCodePublishSettingResponse:
        runtime = RuntimeOptions()
        return await self.get_workspace_code_publish_setting_with_options_async(request, runtime)

    def get_workspace_quota_with_options(
        self,
        request: main_models.GetWorkspaceQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspaceQuota',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_quota_with_options_async(
        self,
        request: main_models.GetWorkspaceQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWorkspaceQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWorkspaceQuota',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWorkspaceQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace_quota(
        self,
        request: main_models.GetWorkspaceQuotaRequest,
    ) -> main_models.GetWorkspaceQuotaResponse:
        runtime = RuntimeOptions()
        return self.get_workspace_quota_with_options(request, runtime)

    async def get_workspace_quota_async(
        self,
        request: main_models.GetWorkspaceQuotaRequest,
    ) -> main_models.GetWorkspaceQuotaResponse:
        runtime = RuntimeOptions()
        return await self.get_workspace_quota_with_options_async(request, runtime)

    def import_one_meta_ossie_model_with_options(
        self,
        request: main_models.ImportOneMetaOssieModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportOneMetaOssieModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.doc_format):
            query['DocFormat'] = request.doc_format
        if not DaraCore.is_null(request.document):
            query['Document'] = request.document
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportOneMetaOssieModel',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportOneMetaOssieModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_one_meta_ossie_model_with_options_async(
        self,
        request: main_models.ImportOneMetaOssieModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportOneMetaOssieModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.doc_format):
            query['DocFormat'] = request.doc_format
        if not DaraCore.is_null(request.document):
            query['Document'] = request.document
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportOneMetaOssieModel',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportOneMetaOssieModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_one_meta_ossie_model(
        self,
        request: main_models.ImportOneMetaOssieModelRequest,
    ) -> main_models.ImportOneMetaOssieModelResponse:
        runtime = RuntimeOptions()
        return self.import_one_meta_ossie_model_with_options(request, runtime)

    async def import_one_meta_ossie_model_async(
        self,
        request: main_models.ImportOneMetaOssieModelRequest,
    ) -> main_models.ImportOneMetaOssieModelResponse:
        runtime = RuntimeOptions()
        return await self.import_one_meta_ossie_model_with_options_async(request, runtime)

    def init_workspace_system_mcp_server_with_options(
        self,
        request: main_models.InitWorkspaceSystemMcpServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitWorkspaceSystemMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitWorkspaceSystemMcpServer',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitWorkspaceSystemMcpServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_workspace_system_mcp_server_with_options_async(
        self,
        request: main_models.InitWorkspaceSystemMcpServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitWorkspaceSystemMcpServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitWorkspaceSystemMcpServer',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitWorkspaceSystemMcpServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_workspace_system_mcp_server(
        self,
        request: main_models.InitWorkspaceSystemMcpServerRequest,
    ) -> main_models.InitWorkspaceSystemMcpServerResponse:
        runtime = RuntimeOptions()
        return self.init_workspace_system_mcp_server_with_options(request, runtime)

    async def init_workspace_system_mcp_server_async(
        self,
        request: main_models.InitWorkspaceSystemMcpServerRequest,
    ) -> main_models.InitWorkspaceSystemMcpServerResponse:
        runtime = RuntimeOptions()
        return await self.init_workspace_system_mcp_server_with_options_async(request, runtime)

    def install_data_agent_mcp_with_options(
        self,
        request: main_models.InstallDataAgentMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallDataAgentMcpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.from_json):
            query['FromJson'] = request.from_json
        if not DaraCore.is_null(request.headers):
            query['Headers'] = request.headers
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.need_uid_in_header):
            query['NeedUidInHeader'] = request.need_uid_in_header
        if not DaraCore.is_null(request.net_type):
            query['NetType'] = request.net_type
        if not DaraCore.is_null(request.transport_type):
            query['TransportType'] = request.transport_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vsw_id):
            query['VswId'] = request.vsw_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallDataAgentMcp',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallDataAgentMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_data_agent_mcp_with_options_async(
        self,
        request: main_models.InstallDataAgentMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallDataAgentMcpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.from_json):
            query['FromJson'] = request.from_json
        if not DaraCore.is_null(request.headers):
            query['Headers'] = request.headers
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.need_uid_in_header):
            query['NeedUidInHeader'] = request.need_uid_in_header
        if not DaraCore.is_null(request.net_type):
            query['NetType'] = request.net_type
        if not DaraCore.is_null(request.transport_type):
            query['TransportType'] = request.transport_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vsw_id):
            query['VswId'] = request.vsw_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallDataAgentMcp',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallDataAgentMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_data_agent_mcp(
        self,
        request: main_models.InstallDataAgentMcpRequest,
    ) -> main_models.InstallDataAgentMcpResponse:
        runtime = RuntimeOptions()
        return self.install_data_agent_mcp_with_options(request, runtime)

    async def install_data_agent_mcp_async(
        self,
        request: main_models.InstallDataAgentMcpRequest,
    ) -> main_models.InstallDataAgentMcpResponse:
        runtime = RuntimeOptions()
        return await self.install_data_agent_mcp_with_options_async(request, runtime)

    def list_airflow_versions_with_options(
        self,
        request: main_models.ListAirflowVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAirflowVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAirflowVersions',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAirflowVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_airflow_versions_with_options_async(
        self,
        request: main_models.ListAirflowVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAirflowVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAirflowVersions',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAirflowVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_airflow_versions(
        self,
        request: main_models.ListAirflowVersionsRequest,
    ) -> main_models.ListAirflowVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_airflow_versions_with_options(request, runtime)

    async def list_airflow_versions_async(
        self,
        request: main_models.ListAirflowVersionsRequest,
    ) -> main_models.ListAirflowVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_airflow_versions_with_options_async(request, runtime)

    def list_airflows_with_options(
        self,
        request: main_models.ListAirflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAirflowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAirflows',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAirflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_airflows_with_options_async(
        self,
        request: main_models.ListAirflowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAirflowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAirflows',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAirflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_airflows(
        self,
        request: main_models.ListAirflowsRequest,
    ) -> main_models.ListAirflowsResponse:
        runtime = RuntimeOptions()
        return self.list_airflows_with_options(request, runtime)

    async def list_airflows_async(
        self,
        request: main_models.ListAirflowsRequest,
    ) -> main_models.ListAirflowsResponse:
        runtime = RuntimeOptions()
        return await self.list_airflows_with_options_async(request, runtime)

    def list_custom_agent_with_options(
        self,
        request: main_models.ListCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_all_released):
            query['QueryAllReleased'] = request.query_all_released
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_agent_with_options_async(
        self,
        request: main_models.ListCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_all_released):
            query['QueryAllReleased'] = request.query_all_released
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_agent(
        self,
        request: main_models.ListCustomAgentRequest,
    ) -> main_models.ListCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.list_custom_agent_with_options(request, runtime)

    async def list_custom_agent_async(
        self,
        request: main_models.ListCustomAgentRequest,
    ) -> main_models.ListCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.list_custom_agent_with_options_async(request, runtime)

    def list_data_agent_accuracy_test_instances_with_options(
        self,
        request: main_models.ListDataAgentAccuracyTestInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentAccuracyTestInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentAccuracyTestInstances',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentAccuracyTestInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_agent_accuracy_test_instances_with_options_async(
        self,
        request: main_models.ListDataAgentAccuracyTestInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentAccuracyTestInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentAccuracyTestInstances',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentAccuracyTestInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_agent_accuracy_test_instances(
        self,
        request: main_models.ListDataAgentAccuracyTestInstancesRequest,
    ) -> main_models.ListDataAgentAccuracyTestInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_data_agent_accuracy_test_instances_with_options(request, runtime)

    async def list_data_agent_accuracy_test_instances_async(
        self,
        request: main_models.ListDataAgentAccuracyTestInstancesRequest,
    ) -> main_models.ListDataAgentAccuracyTestInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_agent_accuracy_test_instances_with_options_async(request, runtime)

    def list_data_agent_accuracy_test_results_with_options(
        self,
        request: main_models.ListDataAgentAccuracyTestResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentAccuracyTestResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.accuracy_test_result_id):
            query['AccuracyTestResultId'] = request.accuracy_test_result_id
        if not DaraCore.is_null(request.accuracy_test_subtask_id):
            query['AccuracyTestSubtaskId'] = request.accuracy_test_subtask_id
        if not DaraCore.is_null(request.accuracy_test_task_id):
            query['AccuracyTestTaskId'] = request.accuracy_test_task_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentAccuracyTestResults',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentAccuracyTestResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_agent_accuracy_test_results_with_options_async(
        self,
        request: main_models.ListDataAgentAccuracyTestResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentAccuracyTestResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.accuracy_test_result_id):
            query['AccuracyTestResultId'] = request.accuracy_test_result_id
        if not DaraCore.is_null(request.accuracy_test_subtask_id):
            query['AccuracyTestSubtaskId'] = request.accuracy_test_subtask_id
        if not DaraCore.is_null(request.accuracy_test_task_id):
            query['AccuracyTestTaskId'] = request.accuracy_test_task_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentAccuracyTestResults',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentAccuracyTestResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_agent_accuracy_test_results(
        self,
        request: main_models.ListDataAgentAccuracyTestResultsRequest,
    ) -> main_models.ListDataAgentAccuracyTestResultsResponse:
        runtime = RuntimeOptions()
        return self.list_data_agent_accuracy_test_results_with_options(request, runtime)

    async def list_data_agent_accuracy_test_results_async(
        self,
        request: main_models.ListDataAgentAccuracyTestResultsRequest,
    ) -> main_models.ListDataAgentAccuracyTestResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_agent_accuracy_test_results_with_options_async(request, runtime)

    def list_data_agent_accuracy_test_tasks_with_options(
        self,
        request: main_models.ListDataAgentAccuracyTestTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentAccuracyTestTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.accuracy_test_task_id):
            query['AccuracyTestTaskId'] = request.accuracy_test_task_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentAccuracyTestTasks',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentAccuracyTestTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_agent_accuracy_test_tasks_with_options_async(
        self,
        request: main_models.ListDataAgentAccuracyTestTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentAccuracyTestTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.accuracy_test_task_id):
            query['AccuracyTestTaskId'] = request.accuracy_test_task_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentAccuracyTestTasks',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentAccuracyTestTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_agent_accuracy_test_tasks(
        self,
        request: main_models.ListDataAgentAccuracyTestTasksRequest,
    ) -> main_models.ListDataAgentAccuracyTestTasksResponse:
        runtime = RuntimeOptions()
        return self.list_data_agent_accuracy_test_tasks_with_options(request, runtime)

    async def list_data_agent_accuracy_test_tasks_async(
        self,
        request: main_models.ListDataAgentAccuracyTestTasksRequest,
    ) -> main_models.ListDataAgentAccuracyTestTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_data_agent_accuracy_test_tasks_with_options_async(request, runtime)

    def list_data_agent_mcp_with_options(
        self,
        request: main_models.ListDataAgentMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentMcpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.ready_only):
            query['ReadyOnly'] = request.ready_only
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentMcp',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_agent_mcp_with_options_async(
        self,
        request: main_models.ListDataAgentMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentMcpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.ready_only):
            query['ReadyOnly'] = request.ready_only
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentMcp',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_agent_mcp(
        self,
        request: main_models.ListDataAgentMcpRequest,
    ) -> main_models.ListDataAgentMcpResponse:
        runtime = RuntimeOptions()
        return self.list_data_agent_mcp_with_options(request, runtime)

    async def list_data_agent_mcp_async(
        self,
        request: main_models.ListDataAgentMcpRequest,
    ) -> main_models.ListDataAgentMcpResponse:
        runtime = RuntimeOptions()
        return await self.list_data_agent_mcp_with_options_async(request, runtime)

    def list_data_agent_memory_with_options(
        self,
        request: main_models.ListDataAgentMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content_pattern):
            query['ContentPattern'] = request.content_pattern
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.from_id):
            query['FromId'] = request.from_id
        if not DaraCore.is_null(request.mem_from):
            query['MemFrom'] = request.mem_from
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_all):
            query['QueryAll'] = request.query_all
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentMemory',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_agent_memory_with_options_async(
        self,
        request: main_models.ListDataAgentMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content_pattern):
            query['ContentPattern'] = request.content_pattern
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.from_id):
            query['FromId'] = request.from_id
        if not DaraCore.is_null(request.mem_from):
            query['MemFrom'] = request.mem_from
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_all):
            query['QueryAll'] = request.query_all
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentMemory',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_agent_memory(
        self,
        request: main_models.ListDataAgentMemoryRequest,
    ) -> main_models.ListDataAgentMemoryResponse:
        runtime = RuntimeOptions()
        return self.list_data_agent_memory_with_options(request, runtime)

    async def list_data_agent_memory_async(
        self,
        request: main_models.ListDataAgentMemoryRequest,
    ) -> main_models.ListDataAgentMemoryResponse:
        runtime = RuntimeOptions()
        return await self.list_data_agent_memory_with_options_async(request, runtime)

    def list_data_agent_session_with_options(
        self,
        request: main_models.ListDataAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_end_time):
            query['CreateEndTime'] = request.create_end_time
        if not DaraCore.is_null(request.create_start_time):
            query['CreateStartTime'] = request.create_start_time
        if not DaraCore.is_null(request.creator_id):
            query['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.is_saved):
            query['IsSaved'] = request.is_saved
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentSession',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_agent_session_with_options_async(
        self,
        request: main_models.ListDataAgentSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_end_time):
            query['CreateEndTime'] = request.create_end_time
        if not DaraCore.is_null(request.create_start_time):
            query['CreateStartTime'] = request.create_start_time
        if not DaraCore.is_null(request.creator_id):
            query['CreatorId'] = request.creator_id
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.is_saved):
            query['IsSaved'] = request.is_saved
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentSession',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_agent_session(
        self,
        request: main_models.ListDataAgentSessionRequest,
    ) -> main_models.ListDataAgentSessionResponse:
        runtime = RuntimeOptions()
        return self.list_data_agent_session_with_options(request, runtime)

    async def list_data_agent_session_async(
        self,
        request: main_models.ListDataAgentSessionRequest,
    ) -> main_models.ListDataAgentSessionResponse:
        runtime = RuntimeOptions()
        return await self.list_data_agent_session_with_options_async(request, runtime)

    def list_data_agent_skill_meta_with_options(
        self,
        request: main_models.ListDataAgentSkillMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentSkillMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.skill_from):
            query['SkillFrom'] = request.skill_from
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentSkillMeta',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentSkillMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_agent_skill_meta_with_options_async(
        self,
        request: main_models.ListDataAgentSkillMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentSkillMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.skill_from):
            query['SkillFrom'] = request.skill_from
        if not DaraCore.is_null(request.skill_id):
            query['SkillId'] = request.skill_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentSkillMeta',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentSkillMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_agent_skill_meta(
        self,
        request: main_models.ListDataAgentSkillMetaRequest,
    ) -> main_models.ListDataAgentSkillMetaResponse:
        runtime = RuntimeOptions()
        return self.list_data_agent_skill_meta_with_options(request, runtime)

    async def list_data_agent_skill_meta_async(
        self,
        request: main_models.ListDataAgentSkillMetaRequest,
    ) -> main_models.ListDataAgentSkillMetaResponse:
        runtime = RuntimeOptions()
        return await self.list_data_agent_skill_meta_with_options_async(request, runtime)

    def list_data_agent_theme_with_options(
        self,
        request: main_models.ListDataAgentThemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentThemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.theme_from):
            query['ThemeFrom'] = request.theme_from
        if not DaraCore.is_null(request.theme_type):
            query['ThemeType'] = request.theme_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentTheme',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentThemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_agent_theme_with_options_async(
        self,
        request: main_models.ListDataAgentThemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentThemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.theme_from):
            query['ThemeFrom'] = request.theme_from
        if not DaraCore.is_null(request.theme_type):
            query['ThemeType'] = request.theme_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentTheme',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentThemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_agent_theme(
        self,
        request: main_models.ListDataAgentThemeRequest,
    ) -> main_models.ListDataAgentThemeResponse:
        runtime = RuntimeOptions()
        return self.list_data_agent_theme_with_options(request, runtime)

    async def list_data_agent_theme_async(
        self,
        request: main_models.ListDataAgentThemeRequest,
    ) -> main_models.ListDataAgentThemeResponse:
        runtime = RuntimeOptions()
        return await self.list_data_agent_theme_with_options_async(request, runtime)

    def list_data_agent_workspace_with_options(
        self,
        request: main_models.ListDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        if not DaraCore.is_null(request.workspace_type):
            query['WorkspaceType'] = request.workspace_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentWorkspace',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_agent_workspace_with_options_async(
        self,
        request: main_models.ListDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator):
            query['Creator'] = request.creator
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        if not DaraCore.is_null(request.workspace_type):
            query['WorkspaceType'] = request.workspace_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentWorkspace',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_agent_workspace(
        self,
        request: main_models.ListDataAgentWorkspaceRequest,
    ) -> main_models.ListDataAgentWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.list_data_agent_workspace_with_options(request, runtime)

    async def list_data_agent_workspace_async(
        self,
        request: main_models.ListDataAgentWorkspaceRequest,
    ) -> main_models.ListDataAgentWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.list_data_agent_workspace_with_options_async(request, runtime)

    def list_data_agent_workspace_member_with_options(
        self,
        request: main_models.ListDataAgentWorkspaceMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentWorkspaceMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_member_id):
            query['SearchMemberId'] = request.search_member_id
        if not DaraCore.is_null(request.search_role_name):
            query['SearchRoleName'] = request.search_role_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentWorkspaceMember',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentWorkspaceMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_agent_workspace_member_with_options_async(
        self,
        request: main_models.ListDataAgentWorkspaceMemberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentWorkspaceMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_member_id):
            query['SearchMemberId'] = request.search_member_id
        if not DaraCore.is_null(request.search_role_name):
            query['SearchRoleName'] = request.search_role_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataAgentWorkspaceMember',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataAgentWorkspaceMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_agent_workspace_member(
        self,
        request: main_models.ListDataAgentWorkspaceMemberRequest,
    ) -> main_models.ListDataAgentWorkspaceMemberResponse:
        runtime = RuntimeOptions()
        return self.list_data_agent_workspace_member_with_options(request, runtime)

    async def list_data_agent_workspace_member_async(
        self,
        request: main_models.ListDataAgentWorkspaceMemberRequest,
    ) -> main_models.ListDataAgentWorkspaceMemberResponse:
        runtime = RuntimeOptions()
        return await self.list_data_agent_workspace_member_with_options_async(request, runtime)

    def list_data_center_database_with_options(
        self,
        request: main_models.ListDataCenterDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCenterDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.import_type):
            query['ImportType'] = request.import_type
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCenterDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCenterDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_center_database_with_options_async(
        self,
        request: main_models.ListDataCenterDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCenterDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.import_type):
            query['ImportType'] = request.import_type
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCenterDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCenterDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_center_database(
        self,
        request: main_models.ListDataCenterDatabaseRequest,
    ) -> main_models.ListDataCenterDatabaseResponse:
        runtime = RuntimeOptions()
        return self.list_data_center_database_with_options(request, runtime)

    async def list_data_center_database_async(
        self,
        request: main_models.ListDataCenterDatabaseRequest,
    ) -> main_models.ListDataCenterDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.list_data_center_database_with_options_async(request, runtime)

    def list_data_center_table_with_options(
        self,
        request: main_models.ListDataCenterTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCenterTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.import_type):
            query['ImportType'] = request.import_type
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCenterTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCenterTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_center_table_with_options_async(
        self,
        request: main_models.ListDataCenterTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCenterTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.import_type):
            query['ImportType'] = request.import_type
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCenterTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCenterTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_center_table(
        self,
        request: main_models.ListDataCenterTableRequest,
    ) -> main_models.ListDataCenterTableResponse:
        runtime = RuntimeOptions()
        return self.list_data_center_table_with_options(request, runtime)

    async def list_data_center_table_async(
        self,
        request: main_models.ListDataCenterTableRequest,
    ) -> main_models.ListDataCenterTableResponse:
        runtime = RuntimeOptions()
        return await self.list_data_center_table_with_options_async(request, runtime)

    def list_data_lake_catalog_with_options(
        self,
        request: main_models.ListDataLakeCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeCatalogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeCatalog',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_catalog_with_options_async(
        self,
        request: main_models.ListDataLakeCatalogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeCatalogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeCatalog',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_catalog(
        self,
        request: main_models.ListDataLakeCatalogRequest,
    ) -> main_models.ListDataLakeCatalogResponse:
        runtime = RuntimeOptions()
        return self.list_data_lake_catalog_with_options(request, runtime)

    async def list_data_lake_catalog_async(
        self,
        request: main_models.ListDataLakeCatalogRequest,
    ) -> main_models.ListDataLakeCatalogResponse:
        runtime = RuntimeOptions()
        return await self.list_data_lake_catalog_with_options_async(request, runtime)

    def list_data_lake_database_with_options(
        self,
        request: main_models.ListDataLakeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_database_with_options_async(
        self,
        request: main_models.ListDataLakeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_database(
        self,
        request: main_models.ListDataLakeDatabaseRequest,
    ) -> main_models.ListDataLakeDatabaseResponse:
        runtime = RuntimeOptions()
        return self.list_data_lake_database_with_options(request, runtime)

    async def list_data_lake_database_async(
        self,
        request: main_models.ListDataLakeDatabaseRequest,
    ) -> main_models.ListDataLakeDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.list_data_lake_database_with_options_async(request, runtime)

    def list_data_lake_function_with_options(
        self,
        request: main_models.ListDataLakeFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeFunction',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_function_with_options_async(
        self,
        request: main_models.ListDataLakeFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeFunctionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeFunction',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_function(
        self,
        request: main_models.ListDataLakeFunctionRequest,
    ) -> main_models.ListDataLakeFunctionResponse:
        runtime = RuntimeOptions()
        return self.list_data_lake_function_with_options(request, runtime)

    async def list_data_lake_function_async(
        self,
        request: main_models.ListDataLakeFunctionRequest,
    ) -> main_models.ListDataLakeFunctionResponse:
        runtime = RuntimeOptions()
        return await self.list_data_lake_function_with_options_async(request, runtime)

    def list_data_lake_function_name_with_options(
        self,
        request: main_models.ListDataLakeFunctionNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeFunctionNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeFunctionName',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeFunctionNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_function_name_with_options_async(
        self,
        request: main_models.ListDataLakeFunctionNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeFunctionNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeFunctionName',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeFunctionNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_function_name(
        self,
        request: main_models.ListDataLakeFunctionNameRequest,
    ) -> main_models.ListDataLakeFunctionNameResponse:
        runtime = RuntimeOptions()
        return self.list_data_lake_function_name_with_options(request, runtime)

    async def list_data_lake_function_name_async(
        self,
        request: main_models.ListDataLakeFunctionNameRequest,
    ) -> main_models.ListDataLakeFunctionNameResponse:
        runtime = RuntimeOptions()
        return await self.list_data_lake_function_name_with_options_async(request, runtime)

    def list_data_lake_partition_with_options(
        self,
        tmp_req: main_models.ListDataLakePartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakePartitionResponse:
        tmp_req.validate()
        request = main_models.ListDataLakePartitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.part_names):
            request.part_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.part_names, 'PartNames', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.part_names_shrink):
            body['PartNames'] = request.part_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakePartition',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_partition_with_options_async(
        self,
        tmp_req: main_models.ListDataLakePartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakePartitionResponse:
        tmp_req.validate()
        request = main_models.ListDataLakePartitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.part_names):
            request.part_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.part_names, 'PartNames', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.part_names_shrink):
            body['PartNames'] = request.part_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakePartition',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_partition(
        self,
        request: main_models.ListDataLakePartitionRequest,
    ) -> main_models.ListDataLakePartitionResponse:
        runtime = RuntimeOptions()
        return self.list_data_lake_partition_with_options(request, runtime)

    async def list_data_lake_partition_async(
        self,
        request: main_models.ListDataLakePartitionRequest,
    ) -> main_models.ListDataLakePartitionResponse:
        runtime = RuntimeOptions()
        return await self.list_data_lake_partition_with_options_async(request, runtime)

    def list_data_lake_partition_by_filter_with_options(
        self,
        request: main_models.ListDataLakePartitionByFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakePartitionByFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakePartitionByFilter',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakePartitionByFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_partition_by_filter_with_options_async(
        self,
        request: main_models.ListDataLakePartitionByFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakePartitionByFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakePartitionByFilter',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakePartitionByFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_partition_by_filter(
        self,
        request: main_models.ListDataLakePartitionByFilterRequest,
    ) -> main_models.ListDataLakePartitionByFilterResponse:
        runtime = RuntimeOptions()
        return self.list_data_lake_partition_by_filter_with_options(request, runtime)

    async def list_data_lake_partition_by_filter_async(
        self,
        request: main_models.ListDataLakePartitionByFilterRequest,
    ) -> main_models.ListDataLakePartitionByFilterResponse:
        runtime = RuntimeOptions()
        return await self.list_data_lake_partition_by_filter_with_options_async(request, runtime)

    def list_data_lake_partition_name_with_options(
        self,
        request: main_models.ListDataLakePartitionNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakePartitionNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakePartitionName',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakePartitionNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_partition_name_with_options_async(
        self,
        request: main_models.ListDataLakePartitionNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakePartitionNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakePartitionName',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakePartitionNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_partition_name(
        self,
        request: main_models.ListDataLakePartitionNameRequest,
    ) -> main_models.ListDataLakePartitionNameResponse:
        runtime = RuntimeOptions()
        return self.list_data_lake_partition_name_with_options(request, runtime)

    async def list_data_lake_partition_name_async(
        self,
        request: main_models.ListDataLakePartitionNameRequest,
    ) -> main_models.ListDataLakePartitionNameResponse:
        runtime = RuntimeOptions()
        return await self.list_data_lake_partition_name_with_options_async(request, runtime)

    def list_data_lake_table_with_options(
        self,
        request: main_models.ListDataLakeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_table_with_options_async(
        self,
        request: main_models.ListDataLakeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_table(
        self,
        request: main_models.ListDataLakeTableRequest,
    ) -> main_models.ListDataLakeTableResponse:
        runtime = RuntimeOptions()
        return self.list_data_lake_table_with_options(request, runtime)

    async def list_data_lake_table_async(
        self,
        request: main_models.ListDataLakeTableRequest,
    ) -> main_models.ListDataLakeTableResponse:
        runtime = RuntimeOptions()
        return await self.list_data_lake_table_with_options_async(request, runtime)

    def list_data_lake_table_name_with_options(
        self,
        request: main_models.ListDataLakeTableNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeTableNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeTableName',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeTableNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_table_name_with_options_async(
        self,
        request: main_models.ListDataLakeTableNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeTableNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeTableName',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeTableNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_table_name(
        self,
        request: main_models.ListDataLakeTableNameRequest,
    ) -> main_models.ListDataLakeTableNameResponse:
        runtime = RuntimeOptions()
        return self.list_data_lake_table_name_with_options(request, runtime)

    async def list_data_lake_table_name_async(
        self,
        request: main_models.ListDataLakeTableNameRequest,
    ) -> main_models.ListDataLakeTableNameResponse:
        runtime = RuntimeOptions()
        return await self.list_data_lake_table_name_with_options_async(request, runtime)

    def list_data_lake_tablebase_info_with_options(
        self,
        request: main_models.ListDataLakeTablebaseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeTablebaseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.rows):
            query['Rows'] = request.rows
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeTablebaseInfo',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeTablebaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_tablebase_info_with_options_async(
        self,
        request: main_models.ListDataLakeTablebaseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataLakeTablebaseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.rows):
            query['Rows'] = request.rows
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataLakeTablebaseInfo',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataLakeTablebaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_tablebase_info(
        self,
        request: main_models.ListDataLakeTablebaseInfoRequest,
    ) -> main_models.ListDataLakeTablebaseInfoResponse:
        runtime = RuntimeOptions()
        return self.list_data_lake_tablebase_info_with_options(request, runtime)

    async def list_data_lake_tablebase_info_async(
        self,
        request: main_models.ListDataLakeTablebaseInfoRequest,
    ) -> main_models.ListDataLakeTablebaseInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_data_lake_tablebase_info_with_options_async(request, runtime)

    def list_document_chunks_with_options(
        self,
        request: main_models.ListDocumentChunksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentChunksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunk_title_pattern):
            body['ChunkTitlePattern'] = request.chunk_title_pattern
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sort_field_name):
            body['SortFieldName'] = request.sort_field_name
        if not DaraCore.is_null(request.sort_order):
            body['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDocumentChunks',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentChunksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_document_chunks_with_options_async(
        self,
        request: main_models.ListDocumentChunksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentChunksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunk_title_pattern):
            body['ChunkTitlePattern'] = request.chunk_title_pattern
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sort_field_name):
            body['SortFieldName'] = request.sort_field_name
        if not DaraCore.is_null(request.sort_order):
            body['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDocumentChunks',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentChunksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_document_chunks(
        self,
        request: main_models.ListDocumentChunksRequest,
    ) -> main_models.ListDocumentChunksResponse:
        runtime = RuntimeOptions()
        return self.list_document_chunks_with_options(request, runtime)

    async def list_document_chunks_async(
        self,
        request: main_models.ListDocumentChunksRequest,
    ) -> main_models.ListDocumentChunksResponse:
        runtime = RuntimeOptions()
        return await self.list_document_chunks_with_options_async(request, runtime)

    def list_documents_with_options(
        self,
        request: main_models.ListDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name_pattern):
            body['NamePattern'] = request.name_pattern
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sort_field_name):
            body['SortFieldName'] = request.sort_field_name
        if not DaraCore.is_null(request.sort_order):
            body['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDocuments',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_documents_with_options_async(
        self,
        request: main_models.ListDocumentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDocumentsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name_pattern):
            body['NamePattern'] = request.name_pattern
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sort_field_name):
            body['SortFieldName'] = request.sort_field_name
        if not DaraCore.is_null(request.sort_order):
            body['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDocuments',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDocumentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_documents(
        self,
        request: main_models.ListDocumentsRequest,
    ) -> main_models.ListDocumentsResponse:
        runtime = RuntimeOptions()
        return self.list_documents_with_options(request, runtime)

    async def list_documents_async(
        self,
        request: main_models.ListDocumentsRequest,
    ) -> main_models.ListDocumentsResponse:
        runtime = RuntimeOptions()
        return await self.list_documents_with_options_async(request, runtime)

    def list_file_upload_with_options(
        self,
        request: main_models.ListFileUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFileUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.download_link_expire):
            query['DownloadLinkExpire'] = request.download_link_expire
        if not DaraCore.is_null(request.file_category):
            query['FileCategory'] = request.file_category
        if not DaraCore.is_null(request.file_from):
            query['FileFrom'] = request.file_from
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sort_column):
            query['SortColumn'] = request.sort_column
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFileUpload',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFileUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_file_upload_with_options_async(
        self,
        request: main_models.ListFileUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFileUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.call_from):
            query['CallFrom'] = request.call_from
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.download_link_expire):
            query['DownloadLinkExpire'] = request.download_link_expire
        if not DaraCore.is_null(request.file_category):
            query['FileCategory'] = request.file_category
        if not DaraCore.is_null(request.file_from):
            query['FileFrom'] = request.file_from
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.sort_column):
            query['SortColumn'] = request.sort_column
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFileUpload',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFileUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_file_upload(
        self,
        request: main_models.ListFileUploadRequest,
    ) -> main_models.ListFileUploadResponse:
        runtime = RuntimeOptions()
        return self.list_file_upload_with_options(request, runtime)

    async def list_file_upload_async(
        self,
        request: main_models.ListFileUploadRequest,
    ) -> main_models.ListFileUploadResponse:
        runtime = RuntimeOptions()
        return await self.list_file_upload_with_options_async(request, runtime)

    def list_knowledge_bases_with_options(
        self,
        request: main_models.ListKnowledgeBasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBasesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name_pattern):
            body['NamePattern'] = request.name_pattern
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sort_field_name):
            body['SortFieldName'] = request.sort_field_name
        if not DaraCore.is_null(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBases',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_knowledge_bases_with_options_async(
        self,
        request: main_models.ListKnowledgeBasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBasesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name_pattern):
            body['NamePattern'] = request.name_pattern
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sort_field_name):
            body['SortFieldName'] = request.sort_field_name
        if not DaraCore.is_null(request.sort_order):
            body['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBases',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_knowledge_bases(
        self,
        request: main_models.ListKnowledgeBasesRequest,
    ) -> main_models.ListKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        return self.list_knowledge_bases_with_options(request, runtime)

    async def list_knowledge_bases_async(
        self,
        request: main_models.ListKnowledgeBasesRequest,
    ) -> main_models.ListKnowledgeBasesResponse:
        runtime = RuntimeOptions()
        return await self.list_knowledge_bases_with_options_async(request, runtime)

    def list_one_meta_ossie_models_with_options(
        self,
        request: main_models.ListOneMetaOssieModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOneMetaOssieModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.enable_vector_search):
            query['EnableVectorSearch'] = request.enable_vector_search
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOneMetaOssieModels',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOneMetaOssieModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_one_meta_ossie_models_with_options_async(
        self,
        request: main_models.ListOneMetaOssieModelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOneMetaOssieModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.enable_vector_search):
            query['EnableVectorSearch'] = request.enable_vector_search
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOneMetaOssieModels',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOneMetaOssieModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_one_meta_ossie_models(
        self,
        request: main_models.ListOneMetaOssieModelsRequest,
    ) -> main_models.ListOneMetaOssieModelsResponse:
        runtime = RuntimeOptions()
        return self.list_one_meta_ossie_models_with_options(request, runtime)

    async def list_one_meta_ossie_models_async(
        self,
        request: main_models.ListOneMetaOssieModelsRequest,
    ) -> main_models.ListOneMetaOssieModelsResponse:
        runtime = RuntimeOptions()
        return await self.list_one_meta_ossie_models_with_options_async(request, runtime)

    def list_one_meta_sql_templates_with_options(
        self,
        request: main_models.ListOneMetaSqlTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOneMetaSqlTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.enable_vector_search):
            query['EnableVectorSearch'] = request.enable_vector_search
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOneMetaSqlTemplates',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOneMetaSqlTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_one_meta_sql_templates_with_options_async(
        self,
        request: main_models.ListOneMetaSqlTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOneMetaSqlTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.enable_vector_search):
            query['EnableVectorSearch'] = request.enable_vector_search
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOneMetaSqlTemplates',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOneMetaSqlTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_one_meta_sql_templates(
        self,
        request: main_models.ListOneMetaSqlTemplatesRequest,
    ) -> main_models.ListOneMetaSqlTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_one_meta_sql_templates_with_options(request, runtime)

    async def list_one_meta_sql_templates_async(
        self,
        request: main_models.ListOneMetaSqlTemplatesRequest,
    ) -> main_models.ListOneMetaSqlTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_one_meta_sql_templates_with_options_async(request, runtime)

    def list_workspace_code_with_options(
        self,
        request: main_models.ListWorkspaceCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceCode',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspace_code_with_options_async(
        self,
        request: main_models.ListWorkspaceCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkspaceCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkspaceCode',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkspaceCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspace_code(
        self,
        request: main_models.ListWorkspaceCodeRequest,
    ) -> main_models.ListWorkspaceCodeResponse:
        runtime = RuntimeOptions()
        return self.list_workspace_code_with_options(request, runtime)

    async def list_workspace_code_async(
        self,
        request: main_models.ListWorkspaceCodeRequest,
    ) -> main_models.ListWorkspaceCodeResponse:
        runtime = RuntimeOptions()
        return await self.list_workspace_code_with_options_async(request, runtime)

    def modify_custom_agent_with_options(
        self,
        tmp_req: main_models.ModifyCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomAgentResponse:
        tmp_req.validate()
        request = main_models.ModifyCustomAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.callback_config):
            request.callback_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.callback_config, 'CallbackConfig', 'json')
        if not DaraCore.is_null(tmp_req.execution_config):
            request.execution_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.execution_config, 'ExecutionConfig', 'json')
        if not DaraCore.is_null(tmp_req.knowledge_config_list):
            request.knowledge_config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_config_list, 'KnowledgeConfigList', 'json')
        if not DaraCore.is_null(tmp_req.knowledge_semantic_config_list):
            request.knowledge_semantic_config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_semantic_config_list, 'KnowledgeSemanticConfigList', 'json')
        if not DaraCore.is_null(tmp_req.schedule_task_config):
            request.schedule_task_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule_task_config, 'ScheduleTaskConfig', 'json')
        if not DaraCore.is_null(tmp_req.user_specified_skill_list):
            request.user_specified_skill_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_specified_skill_list, 'UserSpecifiedSkillList', 'json')
        query = {}
        if not DaraCore.is_null(request.callback_config_shrink):
            query['CallbackConfig'] = request.callback_config_shrink
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.data_json):
            query['DataJson'] = request.data_json
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_config_shrink):
            query['ExecutionConfig'] = request.execution_config_shrink
        if not DaraCore.is_null(request.instruction):
            query['Instruction'] = request.instruction
        if not DaraCore.is_null(request.knowledge):
            query['Knowledge'] = request.knowledge
        if not DaraCore.is_null(request.knowledge_config_list_shrink):
            query['KnowledgeConfigList'] = request.knowledge_config_list_shrink
        if not DaraCore.is_null(request.knowledge_semantic_config_list_shrink):
            query['KnowledgeSemanticConfigList'] = request.knowledge_semantic_config_list_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.related_session_id):
            query['RelatedSessionId'] = request.related_session_id
        if not DaraCore.is_null(request.schedule_task_config_shrink):
            query['ScheduleTaskConfig'] = request.schedule_task_config_shrink
        if not DaraCore.is_null(request.text_report_config):
            query['TextReportConfig'] = request.text_report_config
        if not DaraCore.is_null(request.user_specified_skill_list_shrink):
            query['UserSpecifiedSkillList'] = request.user_specified_skill_list_shrink
        if not DaraCore.is_null(request.web_report_config):
            query['WebReportConfig'] = request.web_report_config
        if not DaraCore.is_null(request.web_report_theme):
            query['WebReportTheme'] = request.web_report_theme
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_custom_agent_with_options_async(
        self,
        tmp_req: main_models.ModifyCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomAgentResponse:
        tmp_req.validate()
        request = main_models.ModifyCustomAgentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.callback_config):
            request.callback_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.callback_config, 'CallbackConfig', 'json')
        if not DaraCore.is_null(tmp_req.execution_config):
            request.execution_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.execution_config, 'ExecutionConfig', 'json')
        if not DaraCore.is_null(tmp_req.knowledge_config_list):
            request.knowledge_config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_config_list, 'KnowledgeConfigList', 'json')
        if not DaraCore.is_null(tmp_req.knowledge_semantic_config_list):
            request.knowledge_semantic_config_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.knowledge_semantic_config_list, 'KnowledgeSemanticConfigList', 'json')
        if not DaraCore.is_null(tmp_req.schedule_task_config):
            request.schedule_task_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.schedule_task_config, 'ScheduleTaskConfig', 'json')
        if not DaraCore.is_null(tmp_req.user_specified_skill_list):
            request.user_specified_skill_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_specified_skill_list, 'UserSpecifiedSkillList', 'json')
        query = {}
        if not DaraCore.is_null(request.callback_config_shrink):
            query['CallbackConfig'] = request.callback_config_shrink
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.data_json):
            query['DataJson'] = request.data_json
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_config_shrink):
            query['ExecutionConfig'] = request.execution_config_shrink
        if not DaraCore.is_null(request.instruction):
            query['Instruction'] = request.instruction
        if not DaraCore.is_null(request.knowledge):
            query['Knowledge'] = request.knowledge
        if not DaraCore.is_null(request.knowledge_config_list_shrink):
            query['KnowledgeConfigList'] = request.knowledge_config_list_shrink
        if not DaraCore.is_null(request.knowledge_semantic_config_list_shrink):
            query['KnowledgeSemanticConfigList'] = request.knowledge_semantic_config_list_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.related_session_id):
            query['RelatedSessionId'] = request.related_session_id
        if not DaraCore.is_null(request.schedule_task_config_shrink):
            query['ScheduleTaskConfig'] = request.schedule_task_config_shrink
        if not DaraCore.is_null(request.text_report_config):
            query['TextReportConfig'] = request.text_report_config
        if not DaraCore.is_null(request.user_specified_skill_list_shrink):
            query['UserSpecifiedSkillList'] = request.user_specified_skill_list_shrink
        if not DaraCore.is_null(request.web_report_config):
            query['WebReportConfig'] = request.web_report_config
        if not DaraCore.is_null(request.web_report_theme):
            query['WebReportTheme'] = request.web_report_theme
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_custom_agent(
        self,
        request: main_models.ModifyCustomAgentRequest,
    ) -> main_models.ModifyCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.modify_custom_agent_with_options(request, runtime)

    async def modify_custom_agent_async(
        self,
        request: main_models.ModifyCustomAgentRequest,
    ) -> main_models.ModifyCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.modify_custom_agent_with_options_async(request, runtime)

    def modify_data_agent_mcp_with_options(
        self,
        request: main_models.ModifyDataAgentMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataAgentMcpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.headers):
            query['Headers'] = request.headers
        if not DaraCore.is_null(request.mcp_server_id):
            query['McpServerId'] = request.mcp_server_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.need_uid_in_header):
            query['NeedUidInHeader'] = request.need_uid_in_header
        if not DaraCore.is_null(request.transport_type):
            query['TransportType'] = request.transport_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataAgentMcp',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataAgentMcpResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_agent_mcp_with_options_async(
        self,
        request: main_models.ModifyDataAgentMcpRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataAgentMcpResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.headers):
            query['Headers'] = request.headers
        if not DaraCore.is_null(request.mcp_server_id):
            query['McpServerId'] = request.mcp_server_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.need_uid_in_header):
            query['NeedUidInHeader'] = request.need_uid_in_header
        if not DaraCore.is_null(request.transport_type):
            query['TransportType'] = request.transport_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataAgentMcp',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataAgentMcpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_agent_mcp(
        self,
        request: main_models.ModifyDataAgentMcpRequest,
    ) -> main_models.ModifyDataAgentMcpResponse:
        runtime = RuntimeOptions()
        return self.modify_data_agent_mcp_with_options(request, runtime)

    async def modify_data_agent_mcp_async(
        self,
        request: main_models.ModifyDataAgentMcpRequest,
    ) -> main_models.ModifyDataAgentMcpResponse:
        runtime = RuntimeOptions()
        return await self.modify_data_agent_mcp_with_options_async(request, runtime)

    def modify_data_agent_theme_with_options(
        self,
        request: main_models.ModifyDataAgentThemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataAgentThemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.theme_id):
            query['ThemeId'] = request.theme_id
        if not DaraCore.is_null(request.theme_name):
            query['ThemeName'] = request.theme_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataAgentTheme',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataAgentThemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_agent_theme_with_options_async(
        self,
        request: main_models.ModifyDataAgentThemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataAgentThemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.theme_id):
            query['ThemeId'] = request.theme_id
        if not DaraCore.is_null(request.theme_name):
            query['ThemeName'] = request.theme_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataAgentTheme',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataAgentThemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_agent_theme(
        self,
        request: main_models.ModifyDataAgentThemeRequest,
    ) -> main_models.ModifyDataAgentThemeResponse:
        runtime = RuntimeOptions()
        return self.modify_data_agent_theme_with_options(request, runtime)

    async def modify_data_agent_theme_async(
        self,
        request: main_models.ModifyDataAgentThemeRequest,
    ) -> main_models.ModifyDataAgentThemeResponse:
        runtime = RuntimeOptions()
        return await self.modify_data_agent_theme_with_options_async(request, runtime)

    def operate_custom_agent_with_options(
        self,
        request: main_models.OperateCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateCustomAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_custom_agent_with_options_async(
        self,
        request: main_models.OperateCustomAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OperateCustomAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_agent_id):
            query['CustomAgentId'] = request.custom_agent_id
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateCustomAgent',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateCustomAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_custom_agent(
        self,
        request: main_models.OperateCustomAgentRequest,
    ) -> main_models.OperateCustomAgentResponse:
        runtime = RuntimeOptions()
        return self.operate_custom_agent_with_options(request, runtime)

    async def operate_custom_agent_async(
        self,
        request: main_models.OperateCustomAgentRequest,
    ) -> main_models.OperateCustomAgentResponse:
        runtime = RuntimeOptions()
        return await self.operate_custom_agent_with_options_async(request, runtime)

    def redeploy_airflow_with_options(
        self,
        request: main_models.RedeployAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RedeployAirflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RedeployAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RedeployAirflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def redeploy_airflow_with_options_async(
        self,
        request: main_models.RedeployAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RedeployAirflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RedeployAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RedeployAirflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def redeploy_airflow(
        self,
        request: main_models.RedeployAirflowRequest,
    ) -> main_models.RedeployAirflowResponse:
        runtime = RuntimeOptions()
        return self.redeploy_airflow_with_options(request, runtime)

    async def redeploy_airflow_async(
        self,
        request: main_models.RedeployAirflowRequest,
    ) -> main_models.RedeployAirflowResponse:
        runtime = RuntimeOptions()
        return await self.redeploy_airflow_with_options_async(request, runtime)

    def remove_user_to_data_agent_workspace_with_options(
        self,
        request: main_models.RemoveUserToDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserToDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserToDataAgentWorkspace',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserToDataAgentWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_user_to_data_agent_workspace_with_options_async(
        self,
        request: main_models.RemoveUserToDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveUserToDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveUserToDataAgentWorkspace',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveUserToDataAgentWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_user_to_data_agent_workspace(
        self,
        request: main_models.RemoveUserToDataAgentWorkspaceRequest,
    ) -> main_models.RemoveUserToDataAgentWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.remove_user_to_data_agent_workspace_with_options(request, runtime)

    async def remove_user_to_data_agent_workspace_async(
        self,
        request: main_models.RemoveUserToDataAgentWorkspaceRequest,
    ) -> main_models.RemoveUserToDataAgentWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.remove_user_to_data_agent_workspace_with_options_async(request, runtime)

    def retrieve_knowledge_base_with_options(
        self,
        request: main_models.RetrieveKnowledgeBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveKnowledgeBaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.hybrid_search):
            body['HybridSearch'] = request.hybrid_search
        if not DaraCore.is_null(request.hybrid_search_args):
            body['HybridSearchArgs'] = request.hybrid_search_args
        if not DaraCore.is_null(request.include_metadata_fields):
            body['IncludeMetadataFields'] = request.include_metadata_fields
        if not DaraCore.is_null(request.include_vector):
            body['IncludeVector'] = request.include_vector
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.metrics):
            body['Metrics'] = request.metrics
        if not DaraCore.is_null(request.offset):
            body['Offset'] = request.offset
        if not DaraCore.is_null(request.order_by):
            body['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.recall_window):
            body['RecallWindow'] = request.recall_window
        if not DaraCore.is_null(request.rerank_factor):
            body['RerankFactor'] = request.rerank_factor
        if not DaraCore.is_null(request.top_k):
            body['TopK'] = request.top_k
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetrieveKnowledgeBase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def retrieve_knowledge_base_with_options_async(
        self,
        request: main_models.RetrieveKnowledgeBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetrieveKnowledgeBaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.filter):
            body['Filter'] = request.filter
        if not DaraCore.is_null(request.hybrid_search):
            body['HybridSearch'] = request.hybrid_search
        if not DaraCore.is_null(request.hybrid_search_args):
            body['HybridSearchArgs'] = request.hybrid_search_args
        if not DaraCore.is_null(request.include_metadata_fields):
            body['IncludeMetadataFields'] = request.include_metadata_fields
        if not DaraCore.is_null(request.include_vector):
            body['IncludeVector'] = request.include_vector
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.metrics):
            body['Metrics'] = request.metrics
        if not DaraCore.is_null(request.offset):
            body['Offset'] = request.offset
        if not DaraCore.is_null(request.order_by):
            body['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.recall_window):
            body['RecallWindow'] = request.recall_window
        if not DaraCore.is_null(request.rerank_factor):
            body['RerankFactor'] = request.rerank_factor
        if not DaraCore.is_null(request.top_k):
            body['TopK'] = request.top_k
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RetrieveKnowledgeBase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetrieveKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retrieve_knowledge_base(
        self,
        request: main_models.RetrieveKnowledgeBaseRequest,
    ) -> main_models.RetrieveKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        return self.retrieve_knowledge_base_with_options(request, runtime)

    async def retrieve_knowledge_base_async(
        self,
        request: main_models.RetrieveKnowledgeBaseRequest,
    ) -> main_models.RetrieveKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        return await self.retrieve_knowledge_base_with_options_async(request, runtime)

    def save_workspace_code_with_options(
        self,
        request: main_models.SaveWorkspaceCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveWorkspaceCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.force):
            body['Force'] = request.force
        if not DaraCore.is_null(request.iac):
            body['Iac'] = request.iac
        if not DaraCore.is_null(request.mtime):
            body['Mtime'] = request.mtime
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.repo):
            body['Repo'] = request.repo
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveWorkspaceCode',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveWorkspaceCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_workspace_code_with_options_async(
        self,
        request: main_models.SaveWorkspaceCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveWorkspaceCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.force):
            body['Force'] = request.force
        if not DaraCore.is_null(request.iac):
            body['Iac'] = request.iac
        if not DaraCore.is_null(request.mtime):
            body['Mtime'] = request.mtime
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.repo):
            body['Repo'] = request.repo
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveWorkspaceCode',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveWorkspaceCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_workspace_code(
        self,
        request: main_models.SaveWorkspaceCodeRequest,
    ) -> main_models.SaveWorkspaceCodeResponse:
        runtime = RuntimeOptions()
        return self.save_workspace_code_with_options(request, runtime)

    async def save_workspace_code_async(
        self,
        request: main_models.SaveWorkspaceCodeRequest,
    ) -> main_models.SaveWorkspaceCodeResponse:
        runtime = RuntimeOptions()
        return await self.save_workspace_code_with_options_async(request, runtime)

    def send_chat_message_with_options(
        self,
        tmp_req: main_models.SendChatMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendChatMessageResponse:
        tmp_req.validate()
        request = main_models.SendChatMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source):
            request.data_source_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source, 'DataSource', 'json')
        if not DaraCore.is_null(tmp_req.data_sources):
            request.data_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_sources, 'DataSources', 'json')
        if not DaraCore.is_null(tmp_req.session_config):
            request.session_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_config, 'SessionConfig', 'json')
        if not DaraCore.is_null(tmp_req.task_config):
            request.task_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_config, 'TaskConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.data_source_shrink):
            query['DataSource'] = request.data_source_shrink
        if not DaraCore.is_null(request.data_sources_shrink):
            query['DataSources'] = request.data_sources_shrink
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.parent_session_id):
            query['ParentSessionId'] = request.parent_session_id
        if not DaraCore.is_null(request.question):
            query['Question'] = request.question
        if not DaraCore.is_null(request.quoted_message):
            query['QuotedMessage'] = request.quoted_message
        if not DaraCore.is_null(request.reply_to):
            query['ReplyTo'] = request.reply_to
        if not DaraCore.is_null(request.session_config_shrink):
            query['SessionConfig'] = request.session_config_shrink
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_config_shrink):
            query['TaskConfig'] = request.task_config_shrink
        if not DaraCore.is_null(request.user_oss_bucket):
            query['UserOssBucket'] = request.user_oss_bucket
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendChatMessage',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendChatMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_chat_message_with_options_async(
        self,
        tmp_req: main_models.SendChatMessageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendChatMessageResponse:
        tmp_req.validate()
        request = main_models.SendChatMessageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source):
            request.data_source_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source, 'DataSource', 'json')
        if not DaraCore.is_null(tmp_req.data_sources):
            request.data_sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_sources, 'DataSources', 'json')
        if not DaraCore.is_null(tmp_req.session_config):
            request.session_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_config, 'SessionConfig', 'json')
        if not DaraCore.is_null(tmp_req.task_config):
            request.task_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_config, 'TaskConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.data_source_shrink):
            query['DataSource'] = request.data_source_shrink
        if not DaraCore.is_null(request.data_sources_shrink):
            query['DataSources'] = request.data_sources_shrink
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.parent_session_id):
            query['ParentSessionId'] = request.parent_session_id
        if not DaraCore.is_null(request.question):
            query['Question'] = request.question
        if not DaraCore.is_null(request.quoted_message):
            query['QuotedMessage'] = request.quoted_message
        if not DaraCore.is_null(request.reply_to):
            query['ReplyTo'] = request.reply_to
        if not DaraCore.is_null(request.session_config_shrink):
            query['SessionConfig'] = request.session_config_shrink
        if not DaraCore.is_null(request.session_id):
            query['SessionId'] = request.session_id
        if not DaraCore.is_null(request.task_config_shrink):
            query['TaskConfig'] = request.task_config_shrink
        if not DaraCore.is_null(request.user_oss_bucket):
            query['UserOssBucket'] = request.user_oss_bucket
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendChatMessage',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendChatMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_chat_message(
        self,
        request: main_models.SendChatMessageRequest,
    ) -> main_models.SendChatMessageResponse:
        runtime = RuntimeOptions()
        return self.send_chat_message_with_options(request, runtime)

    async def send_chat_message_async(
        self,
        request: main_models.SendChatMessageRequest,
    ) -> main_models.SendChatMessageResponse:
        runtime = RuntimeOptions()
        return await self.send_chat_message_with_options_async(request, runtime)

    def set_workspace_code_publish_setting_with_options(
        self,
        request: main_models.SetWorkspaceCodePublishSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWorkspaceCodePublishSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetWorkspaceCodePublishSetting',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWorkspaceCodePublishSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_workspace_code_publish_setting_with_options_async(
        self,
        request: main_models.SetWorkspaceCodePublishSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWorkspaceCodePublishSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetWorkspaceCodePublishSetting',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWorkspaceCodePublishSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_workspace_code_publish_setting(
        self,
        request: main_models.SetWorkspaceCodePublishSettingRequest,
    ) -> main_models.SetWorkspaceCodePublishSettingResponse:
        runtime = RuntimeOptions()
        return self.set_workspace_code_publish_setting_with_options(request, runtime)

    async def set_workspace_code_publish_setting_async(
        self,
        request: main_models.SetWorkspaceCodePublishSettingRequest,
    ) -> main_models.SetWorkspaceCodePublishSettingResponse:
        runtime = RuntimeOptions()
        return await self.set_workspace_code_publish_setting_with_options_async(request, runtime)

    def set_workspace_quota_with_options(
        self,
        request: main_models.SetWorkspaceQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWorkspaceQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cu_quota):
            query['CuQuota'] = request.cu_quota
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetWorkspaceQuota',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWorkspaceQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_workspace_quota_with_options_async(
        self,
        request: main_models.SetWorkspaceQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWorkspaceQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cu_quota):
            query['CuQuota'] = request.cu_quota
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetWorkspaceQuota',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWorkspaceQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_workspace_quota(
        self,
        request: main_models.SetWorkspaceQuotaRequest,
    ) -> main_models.SetWorkspaceQuotaResponse:
        runtime = RuntimeOptions()
        return self.set_workspace_quota_with_options(request, runtime)

    async def set_workspace_quota_async(
        self,
        request: main_models.SetWorkspaceQuotaRequest,
    ) -> main_models.SetWorkspaceQuotaResponse:
        runtime = RuntimeOptions()
        return await self.set_workspace_quota_with_options_async(request, runtime)

    def start_data_agent_accuracy_test_task_with_options(
        self,
        request: main_models.StartDataAgentAccuracyTestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDataAgentAccuracyTestTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.csv_file):
            query['CsvFile'] = request.csv_file
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDataAgentAccuracyTestTask',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDataAgentAccuracyTestTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_data_agent_accuracy_test_task_with_options_async(
        self,
        request: main_models.StartDataAgentAccuracyTestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDataAgentAccuracyTestTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.csv_file):
            query['CsvFile'] = request.csv_file
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDataAgentAccuracyTestTask',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDataAgentAccuracyTestTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_data_agent_accuracy_test_task(
        self,
        request: main_models.StartDataAgentAccuracyTestTaskRequest,
    ) -> main_models.StartDataAgentAccuracyTestTaskResponse:
        runtime = RuntimeOptions()
        return self.start_data_agent_accuracy_test_task_with_options(request, runtime)

    async def start_data_agent_accuracy_test_task_async(
        self,
        request: main_models.StartDataAgentAccuracyTestTaskRequest,
    ) -> main_models.StartDataAgentAccuracyTestTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_data_agent_accuracy_test_task_with_options_async(request, runtime)

    def start_list_mcp_server_tools_with_options(
        self,
        request: main_models.StartListMcpServerToolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartListMcpServerToolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.mcp_server_uuid):
            query['McpServerUuid'] = request.mcp_server_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartListMcpServerTools',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartListMcpServerToolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_list_mcp_server_tools_with_options_async(
        self,
        request: main_models.StartListMcpServerToolsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartListMcpServerToolsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.mcp_server_uuid):
            query['McpServerUuid'] = request.mcp_server_uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartListMcpServerTools',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartListMcpServerToolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_list_mcp_server_tools(
        self,
        request: main_models.StartListMcpServerToolsRequest,
    ) -> main_models.StartListMcpServerToolsResponse:
        runtime = RuntimeOptions()
        return self.start_list_mcp_server_tools_with_options(request, runtime)

    async def start_list_mcp_server_tools_async(
        self,
        request: main_models.StartListMcpServerToolsRequest,
    ) -> main_models.StartListMcpServerToolsResponse:
        runtime = RuntimeOptions()
        return await self.start_list_mcp_server_tools_with_options_async(request, runtime)

    def stop_data_agent_accuracy_test_task_with_options(
        self,
        request: main_models.StopDataAgentAccuracyTestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDataAgentAccuracyTestTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_task_id):
            query['AccuracyTestTaskId'] = request.accuracy_test_task_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDataAgentAccuracyTestTask',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDataAgentAccuracyTestTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_data_agent_accuracy_test_task_with_options_async(
        self,
        request: main_models.StopDataAgentAccuracyTestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDataAgentAccuracyTestTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_task_id):
            query['AccuracyTestTaskId'] = request.accuracy_test_task_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDataAgentAccuracyTestTask',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDataAgentAccuracyTestTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_data_agent_accuracy_test_task(
        self,
        request: main_models.StopDataAgentAccuracyTestTaskRequest,
    ) -> main_models.StopDataAgentAccuracyTestTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_data_agent_accuracy_test_task_with_options(request, runtime)

    async def stop_data_agent_accuracy_test_task_async(
        self,
        request: main_models.StopDataAgentAccuracyTestTaskRequest,
    ) -> main_models.StopDataAgentAccuracyTestTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_data_agent_accuracy_test_task_with_options_async(request, runtime)

    def update_airflow_with_options(
        self,
        tmp_req: main_models.UpdateAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAirflowResponse:
        tmp_req.validate()
        request = main_models.UpdateAirflowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_mount_info_list):
            request.data_mount_info_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_mount_info_list, 'DataMountInfoList', 'json')
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not DaraCore.is_null(request.airflow_name):
            query['AirflowName'] = request.airflow_name
        if not DaraCore.is_null(request.app_spec):
            query['AppSpec'] = request.app_spec
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dags_dir):
            query['DagsDir'] = request.dags_dir
        if not DaraCore.is_null(request.data_mount_info_list_shrink):
            query['DataMountInfoList'] = request.data_mount_info_list_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_serverless):
            query['EnableServerless'] = request.enable_serverless
        if not DaraCore.is_null(request.graceful_shutdown_timeout):
            query['GracefulShutdownTimeout'] = request.graceful_shutdown_timeout
        if not DaraCore.is_null(request.plugins_dir):
            query['PluginsDir'] = request.plugins_dir
        if not DaraCore.is_null(request.requirement_file):
            query['RequirementFile'] = request.requirement_file
        if not DaraCore.is_null(request.startup_file):
            query['StartupFile'] = request.startup_file
        if not DaraCore.is_null(request.worker_serverless_replicas):
            query['WorkerServerlessReplicas'] = request.worker_serverless_replicas
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAirflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_airflow_with_options_async(
        self,
        tmp_req: main_models.UpdateAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAirflowResponse:
        tmp_req.validate()
        request = main_models.UpdateAirflowShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_mount_info_list):
            request.data_mount_info_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_mount_info_list, 'DataMountInfoList', 'json')
        query = {}
        if not DaraCore.is_null(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not DaraCore.is_null(request.airflow_name):
            query['AirflowName'] = request.airflow_name
        if not DaraCore.is_null(request.app_spec):
            query['AppSpec'] = request.app_spec
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dags_dir):
            query['DagsDir'] = request.dags_dir
        if not DaraCore.is_null(request.data_mount_info_list_shrink):
            query['DataMountInfoList'] = request.data_mount_info_list_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.enable_serverless):
            query['EnableServerless'] = request.enable_serverless
        if not DaraCore.is_null(request.graceful_shutdown_timeout):
            query['GracefulShutdownTimeout'] = request.graceful_shutdown_timeout
        if not DaraCore.is_null(request.plugins_dir):
            query['PluginsDir'] = request.plugins_dir
        if not DaraCore.is_null(request.requirement_file):
            query['RequirementFile'] = request.requirement_file
        if not DaraCore.is_null(request.startup_file):
            query['StartupFile'] = request.startup_file
        if not DaraCore.is_null(request.worker_serverless_replicas):
            query['WorkerServerlessReplicas'] = request.worker_serverless_replicas
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAirflow',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAirflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_airflow(
        self,
        request: main_models.UpdateAirflowRequest,
    ) -> main_models.UpdateAirflowResponse:
        runtime = RuntimeOptions()
        return self.update_airflow_with_options(request, runtime)

    async def update_airflow_async(
        self,
        request: main_models.UpdateAirflowRequest,
    ) -> main_models.UpdateAirflowResponse:
        runtime = RuntimeOptions()
        return await self.update_airflow_with_options_async(request, runtime)

    def update_data_agent_accuracy_test_with_options(
        self,
        request: main_models.UpdateDataAgentAccuracyTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAgentAccuracyTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.customer_agent_id):
            query['CustomerAgentId'] = request.customer_agent_id
        if not DaraCore.is_null(request.dataset):
            query['Dataset'] = request.dataset
        if not DaraCore.is_null(request.datasource):
            query['Datasource'] = request.datasource
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.evaluation_prompt):
            query['EvaluationPrompt'] = request.evaluation_prompt
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.max_concurrent):
            query['MaxConcurrent'] = request.max_concurrent
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.need_delete):
            query['NeedDelete'] = request.need_delete
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataAgentAccuracyTest',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataAgentAccuracyTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_agent_accuracy_test_with_options_async(
        self,
        request: main_models.UpdateDataAgentAccuracyTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAgentAccuracyTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accuracy_test_ins_id):
            query['AccuracyTestInsId'] = request.accuracy_test_ins_id
        if not DaraCore.is_null(request.customer_agent_id):
            query['CustomerAgentId'] = request.customer_agent_id
        if not DaraCore.is_null(request.dataset):
            query['Dataset'] = request.dataset
        if not DaraCore.is_null(request.datasource):
            query['Datasource'] = request.datasource
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.dms_unit):
            query['DmsUnit'] = request.dms_unit
        if not DaraCore.is_null(request.evaluation_prompt):
            query['EvaluationPrompt'] = request.evaluation_prompt
        if not DaraCore.is_null(request.file_id):
            query['FileId'] = request.file_id
        if not DaraCore.is_null(request.max_concurrent):
            query['MaxConcurrent'] = request.max_concurrent
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.need_delete):
            query['NeedDelete'] = request.need_delete
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataAgentAccuracyTest',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataAgentAccuracyTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_agent_accuracy_test(
        self,
        request: main_models.UpdateDataAgentAccuracyTestRequest,
    ) -> main_models.UpdateDataAgentAccuracyTestResponse:
        runtime = RuntimeOptions()
        return self.update_data_agent_accuracy_test_with_options(request, runtime)

    async def update_data_agent_accuracy_test_async(
        self,
        request: main_models.UpdateDataAgentAccuracyTestRequest,
    ) -> main_models.UpdateDataAgentAccuracyTestResponse:
        runtime = RuntimeOptions()
        return await self.update_data_agent_accuracy_test_with_options_async(request, runtime)

    def update_data_agent_memory_with_options(
        self,
        request: main_models.UpdateDataAgentMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAgentMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.from_id):
            query['FromId'] = request.from_id
        if not DaraCore.is_null(request.mem_from):
            query['MemFrom'] = request.mem_from
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataAgentMemory',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataAgentMemoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_agent_memory_with_options_async(
        self,
        request: main_models.UpdateDataAgentMemoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAgentMemoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.from_id):
            query['FromId'] = request.from_id
        if not DaraCore.is_null(request.mem_from):
            query['MemFrom'] = request.mem_from
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataAgentMemory',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataAgentMemoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_agent_memory(
        self,
        request: main_models.UpdateDataAgentMemoryRequest,
    ) -> main_models.UpdateDataAgentMemoryResponse:
        runtime = RuntimeOptions()
        return self.update_data_agent_memory_with_options(request, runtime)

    async def update_data_agent_memory_async(
        self,
        request: main_models.UpdateDataAgentMemoryRequest,
    ) -> main_models.UpdateDataAgentMemoryResponse:
        runtime = RuntimeOptions()
        return await self.update_data_agent_memory_with_options_async(request, runtime)

    def update_data_agent_space_info_with_options(
        self,
        request: main_models.UpdateDataAgentSpaceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAgentSpaceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.is_session_share_enabled):
            query['IsSessionShareEnabled'] = request.is_session_share_enabled
        if not DaraCore.is_null(request.workspace_desc):
            query['WorkspaceDesc'] = request.workspace_desc
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataAgentSpaceInfo',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataAgentSpaceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_agent_space_info_with_options_async(
        self,
        request: main_models.UpdateDataAgentSpaceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAgentSpaceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.is_session_share_enabled):
            query['IsSessionShareEnabled'] = request.is_session_share_enabled
        if not DaraCore.is_null(request.workspace_desc):
            query['WorkspaceDesc'] = request.workspace_desc
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataAgentSpaceInfo',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataAgentSpaceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_agent_space_info(
        self,
        request: main_models.UpdateDataAgentSpaceInfoRequest,
    ) -> main_models.UpdateDataAgentSpaceInfoResponse:
        runtime = RuntimeOptions()
        return self.update_data_agent_space_info_with_options(request, runtime)

    async def update_data_agent_space_info_async(
        self,
        request: main_models.UpdateDataAgentSpaceInfoRequest,
    ) -> main_models.UpdateDataAgentSpaceInfoResponse:
        runtime = RuntimeOptions()
        return await self.update_data_agent_space_info_with_options_async(request, runtime)

    def update_data_agent_workspace_member_role_with_options(
        self,
        request: main_models.UpdateDataAgentWorkspaceMemberRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAgentWorkspaceMemberRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataAgentWorkspaceMemberRole',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataAgentWorkspaceMemberRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_agent_workspace_member_role_with_options_async(
        self,
        request: main_models.UpdateDataAgentWorkspaceMemberRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAgentWorkspaceMemberRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.member_id):
            query['MemberId'] = request.member_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataAgentWorkspaceMemberRole',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataAgentWorkspaceMemberRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_agent_workspace_member_role(
        self,
        request: main_models.UpdateDataAgentWorkspaceMemberRoleRequest,
    ) -> main_models.UpdateDataAgentWorkspaceMemberRoleResponse:
        runtime = RuntimeOptions()
        return self.update_data_agent_workspace_member_role_with_options(request, runtime)

    async def update_data_agent_workspace_member_role_async(
        self,
        request: main_models.UpdateDataAgentWorkspaceMemberRoleRequest,
    ) -> main_models.UpdateDataAgentWorkspaceMemberRoleResponse:
        runtime = RuntimeOptions()
        return await self.update_data_agent_workspace_member_role_with_options_async(request, runtime)

    def update_data_lake_database_with_options(
        self,
        tmp_req: main_models.UpdateDataLakeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataLakeDatabaseResponse:
        tmp_req.validate()
        request = main_models.UpdateDataLakeDatabaseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataLakeDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataLakeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_lake_database_with_options_async(
        self,
        tmp_req: main_models.UpdateDataLakeDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataLakeDatabaseResponse:
        tmp_req.validate()
        request = main_models.UpdateDataLakeDatabaseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.location):
            query['Location'] = request.location
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataLakeDatabase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataLakeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_lake_database(
        self,
        request: main_models.UpdateDataLakeDatabaseRequest,
    ) -> main_models.UpdateDataLakeDatabaseResponse:
        runtime = RuntimeOptions()
        return self.update_data_lake_database_with_options(request, runtime)

    async def update_data_lake_database_async(
        self,
        request: main_models.UpdateDataLakeDatabaseRequest,
    ) -> main_models.UpdateDataLakeDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.update_data_lake_database_with_options_async(request, runtime)

    def update_data_lake_function_with_options(
        self,
        tmp_req: main_models.UpdateDataLakeFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataLakeFunctionResponse:
        tmp_req.validate()
        request = main_models.UpdateDataLakeFunctionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.function_input):
            request.function_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.function_input, 'FunctionInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.function_input_shrink):
            body['FunctionInput'] = request.function_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataLakeFunction',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataLakeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_lake_function_with_options_async(
        self,
        tmp_req: main_models.UpdateDataLakeFunctionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataLakeFunctionResponse:
        tmp_req.validate()
        request = main_models.UpdateDataLakeFunctionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.function_input):
            request.function_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.function_input, 'FunctionInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.function_name):
            query['FunctionName'] = request.function_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.function_input_shrink):
            body['FunctionInput'] = request.function_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataLakeFunction',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataLakeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_lake_function(
        self,
        request: main_models.UpdateDataLakeFunctionRequest,
    ) -> main_models.UpdateDataLakeFunctionResponse:
        runtime = RuntimeOptions()
        return self.update_data_lake_function_with_options(request, runtime)

    async def update_data_lake_function_async(
        self,
        request: main_models.UpdateDataLakeFunctionRequest,
    ) -> main_models.UpdateDataLakeFunctionResponse:
        runtime = RuntimeOptions()
        return await self.update_data_lake_function_with_options_async(request, runtime)

    def update_data_lake_partition_with_options(
        self,
        tmp_req: main_models.UpdateDataLakePartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataLakePartitionResponse:
        tmp_req.validate()
        request = main_models.UpdateDataLakePartitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_input):
            request.partition_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_input, 'PartitionInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.partition_input_shrink):
            body['PartitionInput'] = request.partition_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataLakePartition',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataLakePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_lake_partition_with_options_async(
        self,
        tmp_req: main_models.UpdateDataLakePartitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataLakePartitionResponse:
        tmp_req.validate()
        request = main_models.UpdateDataLakePartitionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.partition_input):
            request.partition_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.partition_input, 'PartitionInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.partition_input_shrink):
            body['PartitionInput'] = request.partition_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataLakePartition',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataLakePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_lake_partition(
        self,
        request: main_models.UpdateDataLakePartitionRequest,
    ) -> main_models.UpdateDataLakePartitionResponse:
        runtime = RuntimeOptions()
        return self.update_data_lake_partition_with_options(request, runtime)

    async def update_data_lake_partition_async(
        self,
        request: main_models.UpdateDataLakePartitionRequest,
    ) -> main_models.UpdateDataLakePartitionResponse:
        runtime = RuntimeOptions()
        return await self.update_data_lake_partition_with_options_async(request, runtime)

    def update_data_lake_table_with_options(
        self,
        tmp_req: main_models.UpdateDataLakeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataLakeTableResponse:
        tmp_req.validate()
        request = main_models.UpdateDataLakeTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.table_input):
            request.table_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_input, 'TableInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.table_input_shrink):
            body['TableInput'] = request.table_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataLakeTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataLakeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_lake_table_with_options_async(
        self,
        tmp_req: main_models.UpdateDataLakeTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataLakeTableResponse:
        tmp_req.validate()
        request = main_models.UpdateDataLakeTableShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.table_input):
            request.table_input_shrink = Utils.array_to_string_with_specified_style(tmp_req.table_input, 'TableInput', 'json')
        query = {}
        if not DaraCore.is_null(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.tid):
            query['Tid'] = request.tid
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.table_input_shrink):
            body['TableInput'] = request.table_input_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataLakeTable',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataLakeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_lake_table(
        self,
        request: main_models.UpdateDataLakeTableRequest,
    ) -> main_models.UpdateDataLakeTableResponse:
        runtime = RuntimeOptions()
        return self.update_data_lake_table_with_options(request, runtime)

    async def update_data_lake_table_async(
        self,
        request: main_models.UpdateDataLakeTableRequest,
    ) -> main_models.UpdateDataLakeTableResponse:
        runtime = RuntimeOptions()
        return await self.update_data_lake_table_with_options_async(request, runtime)

    def update_document_with_options(
        self,
        request: main_models.UpdateDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.new_description):
            body['NewDescription'] = request.new_description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDocument',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_document_with_options_async(
        self,
        request: main_models.UpdateDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.new_description):
            body['NewDescription'] = request.new_description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDocument',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_document(
        self,
        request: main_models.UpdateDocumentRequest,
    ) -> main_models.UpdateDocumentResponse:
        runtime = RuntimeOptions()
        return self.update_document_with_options(request, runtime)

    async def update_document_async(
        self,
        request: main_models.UpdateDocumentRequest,
    ) -> main_models.UpdateDocumentResponse:
        runtime = RuntimeOptions()
        return await self.update_document_with_options_async(request, runtime)

    def update_knowledge_base_with_options(
        self,
        request: main_models.UpdateKnowledgeBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.kb_uuid):
            query['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_knowledge_base_with_options_async(
        self,
        request: main_models.UpdateKnowledgeBaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.kb_uuid):
            query['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKnowledgeBase',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_knowledge_base(
        self,
        request: main_models.UpdateKnowledgeBaseRequest,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        return self.update_knowledge_base_with_options(request, runtime)

    async def update_knowledge_base_async(
        self,
        request: main_models.UpdateKnowledgeBaseRequest,
    ) -> main_models.UpdateKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        return await self.update_knowledge_base_with_options_async(request, runtime)

    def update_one_meta_ossie_model_with_options(
        self,
        request: main_models.UpdateOneMetaOssieModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOneMetaOssieModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.doc_format):
            query['DocFormat'] = request.doc_format
        if not DaraCore.is_null(request.document):
            query['Document'] = request.document
        if not DaraCore.is_null(request.knowledge_uuid):
            query['KnowledgeUuid'] = request.knowledge_uuid
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOneMetaOssieModel',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOneMetaOssieModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_one_meta_ossie_model_with_options_async(
        self,
        request: main_models.UpdateOneMetaOssieModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOneMetaOssieModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.doc_format):
            query['DocFormat'] = request.doc_format
        if not DaraCore.is_null(request.document):
            query['Document'] = request.document
        if not DaraCore.is_null(request.knowledge_uuid):
            query['KnowledgeUuid'] = request.knowledge_uuid
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOneMetaOssieModel',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOneMetaOssieModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_one_meta_ossie_model(
        self,
        request: main_models.UpdateOneMetaOssieModelRequest,
    ) -> main_models.UpdateOneMetaOssieModelResponse:
        runtime = RuntimeOptions()
        return self.update_one_meta_ossie_model_with_options(request, runtime)

    async def update_one_meta_ossie_model_async(
        self,
        request: main_models.UpdateOneMetaOssieModelRequest,
    ) -> main_models.UpdateOneMetaOssieModelResponse:
        runtime = RuntimeOptions()
        return await self.update_one_meta_ossie_model_with_options_async(request, runtime)

    def update_one_meta_sql_template_with_options(
        self,
        request: main_models.UpdateOneMetaSqlTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOneMetaSqlTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expr):
            query['Expr'] = request.expr
        if not DaraCore.is_null(request.knowledge_uuid):
            query['KnowledgeUuid'] = request.knowledge_uuid
        if not DaraCore.is_null(request.sql_params):
            query['SqlParams'] = request.sql_params
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOneMetaSqlTemplate',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOneMetaSqlTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_one_meta_sql_template_with_options_async(
        self,
        request: main_models.UpdateOneMetaSqlTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOneMetaSqlTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_uuid):
            query['CatalogUuid'] = request.catalog_uuid
        if not DaraCore.is_null(request.database_uuid):
            query['DatabaseUuid'] = request.database_uuid
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expr):
            query['Expr'] = request.expr
        if not DaraCore.is_null(request.knowledge_uuid):
            query['KnowledgeUuid'] = request.knowledge_uuid
        if not DaraCore.is_null(request.sql_params):
            query['SqlParams'] = request.sql_params
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOneMetaSqlTemplate',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOneMetaSqlTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_one_meta_sql_template(
        self,
        request: main_models.UpdateOneMetaSqlTemplateRequest,
    ) -> main_models.UpdateOneMetaSqlTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_one_meta_sql_template_with_options(request, runtime)

    async def update_one_meta_sql_template_async(
        self,
        request: main_models.UpdateOneMetaSqlTemplateRequest,
    ) -> main_models.UpdateOneMetaSqlTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_one_meta_sql_template_with_options_async(request, runtime)

    def upload_document_with_options(
        self,
        tmp_req: main_models.UploadDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocumentResponse:
        tmp_req.validate()
        request = main_models.UploadDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.separators):
            request.separators_shrink = Utils.array_to_string_with_specified_style(tmp_req.separators, 'Separators', 'json')
        body = {}
        if not DaraCore.is_null(request.chunk_overlap):
            body['ChunkOverlap'] = request.chunk_overlap
        if not DaraCore.is_null(request.chunk_size):
            body['ChunkSize'] = request.chunk_size
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.document_loader_name):
            body['DocumentLoaderName'] = request.document_loader_name
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.location):
            body['Location'] = request.location
        if not DaraCore.is_null(request.separators_shrink):
            body['Separators'] = request.separators_shrink
        if not DaraCore.is_null(request.splitter_model):
            body['SplitterModel'] = request.splitter_model
        if not DaraCore.is_null(request.text_splitter_name):
            body['TextSplitterName'] = request.text_splitter_name
        if not DaraCore.is_null(request.vl_enhance):
            body['VlEnhance'] = request.vl_enhance
        if not DaraCore.is_null(request.zh_title_enhance):
            body['ZhTitleEnhance'] = request.zh_title_enhance
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDocument',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_document_with_options_async(
        self,
        tmp_req: main_models.UploadDocumentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDocumentResponse:
        tmp_req.validate()
        request = main_models.UploadDocumentShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.separators):
            request.separators_shrink = Utils.array_to_string_with_specified_style(tmp_req.separators, 'Separators', 'json')
        body = {}
        if not DaraCore.is_null(request.chunk_overlap):
            body['ChunkOverlap'] = request.chunk_overlap
        if not DaraCore.is_null(request.chunk_size):
            body['ChunkSize'] = request.chunk_size
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.document_loader_name):
            body['DocumentLoaderName'] = request.document_loader_name
        if not DaraCore.is_null(request.file_name):
            body['FileName'] = request.file_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        if not DaraCore.is_null(request.location):
            body['Location'] = request.location
        if not DaraCore.is_null(request.separators_shrink):
            body['Separators'] = request.separators_shrink
        if not DaraCore.is_null(request.splitter_model):
            body['SplitterModel'] = request.splitter_model
        if not DaraCore.is_null(request.text_splitter_name):
            body['TextSplitterName'] = request.text_splitter_name
        if not DaraCore.is_null(request.vl_enhance):
            body['VlEnhance'] = request.vl_enhance
        if not DaraCore.is_null(request.zh_title_enhance):
            body['ZhTitleEnhance'] = request.zh_title_enhance
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDocument',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_document(
        self,
        request: main_models.UploadDocumentRequest,
    ) -> main_models.UploadDocumentResponse:
        runtime = RuntimeOptions()
        return self.upload_document_with_options(request, runtime)

    async def upload_document_async(
        self,
        request: main_models.UploadDocumentRequest,
    ) -> main_models.UploadDocumentResponse:
        runtime = RuntimeOptions()
        return await self.upload_document_with_options_async(request, runtime)

    def upsert_document_chunks_with_options(
        self,
        request: main_models.UpsertDocumentChunksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertDocumentChunksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunks):
            body['Chunks'] = request.chunks
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertDocumentChunks',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertDocumentChunksResponse(),
            self.call_api(params, req, runtime)
        )

    async def upsert_document_chunks_with_options_async(
        self,
        request: main_models.UpsertDocumentChunksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpsertDocumentChunksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chunks):
            body['Chunks'] = request.chunks
        if not DaraCore.is_null(request.document_name):
            body['DocumentName'] = request.document_name
        if not DaraCore.is_null(request.kb_uuid):
            body['KbUuid'] = request.kb_uuid
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpsertDocumentChunks',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpsertDocumentChunksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upsert_document_chunks(
        self,
        request: main_models.UpsertDocumentChunksRequest,
    ) -> main_models.UpsertDocumentChunksResponse:
        runtime = RuntimeOptions()
        return self.upsert_document_chunks_with_options(request, runtime)

    async def upsert_document_chunks_async(
        self,
        request: main_models.UpsertDocumentChunksRequest,
    ) -> main_models.UpsertDocumentChunksResponse:
        runtime = RuntimeOptions()
        return await self.upsert_document_chunks_with_options_async(request, runtime)

    def workspace_action_log_with_options(
        self,
        request: main_models.WorkspaceActionLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WorkspaceActionLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WorkspaceActionLog',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WorkspaceActionLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def workspace_action_log_with_options_async(
        self,
        request: main_models.WorkspaceActionLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WorkspaceActionLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WorkspaceActionLog',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WorkspaceActionLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def workspace_action_log(
        self,
        request: main_models.WorkspaceActionLogRequest,
    ) -> main_models.WorkspaceActionLogResponse:
        runtime = RuntimeOptions()
        return self.workspace_action_log_with_options(request, runtime)

    async def workspace_action_log_async(
        self,
        request: main_models.WorkspaceActionLogRequest,
    ) -> main_models.WorkspaceActionLogResponse:
        runtime = RuntimeOptions()
        return await self.workspace_action_log_with_options_async(request, runtime)

    def workspace_action_status_with_options(
        self,
        request: main_models.WorkspaceActionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WorkspaceActionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WorkspaceActionStatus',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WorkspaceActionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def workspace_action_status_with_options_async(
        self,
        request: main_models.WorkspaceActionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WorkspaceActionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WorkspaceActionStatus',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WorkspaceActionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def workspace_action_status(
        self,
        request: main_models.WorkspaceActionStatusRequest,
    ) -> main_models.WorkspaceActionStatusResponse:
        runtime = RuntimeOptions()
        return self.workspace_action_status_with_options(request, runtime)

    async def workspace_action_status_async(
        self,
        request: main_models.WorkspaceActionStatusRequest,
    ) -> main_models.WorkspaceActionStatusResponse:
        runtime = RuntimeOptions()
        return await self.workspace_action_status_with_options_async(request, runtime)

    def workspace_code_publish_with_options(
        self,
        request: main_models.WorkspaceCodePublishRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WorkspaceCodePublishResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'WorkspaceCodePublish',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WorkspaceCodePublishResponse(),
            self.call_api(params, req, runtime)
        )

    async def workspace_code_publish_with_options_async(
        self,
        request: main_models.WorkspaceCodePublishRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WorkspaceCodePublishResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'WorkspaceCodePublish',
            version = '2025-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WorkspaceCodePublishResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def workspace_code_publish(
        self,
        request: main_models.WorkspaceCodePublishRequest,
    ) -> main_models.WorkspaceCodePublishResponse:
        runtime = RuntimeOptions()
        return self.workspace_code_publish_with_options(request, runtime)

    async def workspace_code_publish_async(
        self,
        request: main_models.WorkspaceCodePublishRequest,
    ) -> main_models.WorkspaceCodePublishResponse:
        runtime = RuntimeOptions()
        return await self.workspace_code_publish_with_options_async(request, runtime)
