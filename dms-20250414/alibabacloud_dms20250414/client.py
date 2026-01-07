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
from darabonba.core import DaraCore
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

    def create_airflow_with_options(
        self,
        request: main_models.CreateAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAirflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.airflow_name):
            query['AirflowName'] = request.airflow_name
        if not DaraCore.is_null(request.app_spec):
            query['AppSpec'] = request.app_spec
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dags_dir):
            query['DagsDir'] = request.dags_dir
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
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
        request: main_models.CreateAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAirflowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.airflow_name):
            query['AirflowName'] = request.airflow_name
        if not DaraCore.is_null(request.app_spec):
            query['AppSpec'] = request.app_spec
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dags_dir):
            query['DagsDir'] = request.dags_dir
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
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

    def create_data_agent_workspace_with_options(
        self,
        request: main_models.CreateDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataAgentWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
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
        if not DaraCore.is_null(request.upload_location):
            query['UploadLocation'] = request.upload_location
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
        if not DaraCore.is_null(request.upload_location):
            query['UploadLocation'] = request.upload_location
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
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.GetChatContentResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
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
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.GetChatContentResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
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

    def list_data_agent_workspace_with_options(
        self,
        request: main_models.ListDataAgentWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataAgentWorkspaceResponse:
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
        if not DaraCore.is_null(tmp_req.session_config):
            request.session_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_config, 'SessionConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.data_source_shrink):
            query['DataSource'] = request.data_source_shrink
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
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
        if not DaraCore.is_null(tmp_req.session_config):
            request.session_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.session_config, 'SessionConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['AgentId'] = request.agent_id
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not DaraCore.is_null(request.data_source_shrink):
            query['DataSource'] = request.data_source_shrink
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
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

    def update_airflow_with_options(
        self,
        request: main_models.UpdateAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAirflowResponse:
        request.validate()
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
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
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
        request: main_models.UpdateAirflowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAirflowResponse:
        request.validate()
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
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
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

    def update_data_agent_space_info_with_options(
        self,
        request: main_models.UpdateDataAgentSpaceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataAgentSpaceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
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
