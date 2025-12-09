# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dms20250414 import models as dms_20250414_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def batch_create_data_lake_partitions_with_options(
        self,
        tmp_req: dms_20250414_models.BatchCreateDataLakePartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.BatchCreateDataLakePartitionsResponse:
        """
        @summary 批量新建湖仓表分区
        
        @param tmp_req: BatchCreateDataLakePartitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateDataLakePartitionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.BatchCreateDataLakePartitionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_inputs):
            request.partition_inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_inputs, 'PartitionInputs', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.if_not_exists):
            query['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.need_result):
            query['NeedResult'] = request.need_result
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.partition_inputs_shrink):
            body['PartitionInputs'] = request.partition_inputs_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateDataLakePartitions',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.BatchCreateDataLakePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_data_lake_partitions_with_options_async(
        self,
        tmp_req: dms_20250414_models.BatchCreateDataLakePartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.BatchCreateDataLakePartitionsResponse:
        """
        @summary 批量新建湖仓表分区
        
        @param tmp_req: BatchCreateDataLakePartitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateDataLakePartitionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.BatchCreateDataLakePartitionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_inputs):
            request.partition_inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_inputs, 'PartitionInputs', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.if_not_exists):
            query['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.need_result):
            query['NeedResult'] = request.need_result
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.partition_inputs_shrink):
            body['PartitionInputs'] = request.partition_inputs_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateDataLakePartitions',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.BatchCreateDataLakePartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_data_lake_partitions(
        self,
        request: dms_20250414_models.BatchCreateDataLakePartitionsRequest,
    ) -> dms_20250414_models.BatchCreateDataLakePartitionsResponse:
        """
        @summary 批量新建湖仓表分区
        
        @param request: BatchCreateDataLakePartitionsRequest
        @return: BatchCreateDataLakePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_create_data_lake_partitions_with_options(request, runtime)

    async def batch_create_data_lake_partitions_async(
        self,
        request: dms_20250414_models.BatchCreateDataLakePartitionsRequest,
    ) -> dms_20250414_models.BatchCreateDataLakePartitionsResponse:
        """
        @summary 批量新建湖仓表分区
        
        @param request: BatchCreateDataLakePartitionsRequest
        @return: BatchCreateDataLakePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_data_lake_partitions_with_options_async(request, runtime)

    def batch_delete_data_lake_partitions_with_options(
        self,
        request: dms_20250414_models.BatchDeleteDataLakePartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.BatchDeleteDataLakePartitionsResponse:
        """
        @summary 批量删除湖仓表分区
        
        @param request: BatchDeleteDataLakePartitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteDataLakePartitionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.if_exists):
            query['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.partition_values_list):
            query['PartitionValuesList'] = request.partition_values_list
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteDataLakePartitions',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.BatchDeleteDataLakePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_data_lake_partitions_with_options_async(
        self,
        request: dms_20250414_models.BatchDeleteDataLakePartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.BatchDeleteDataLakePartitionsResponse:
        """
        @summary 批量删除湖仓表分区
        
        @param request: BatchDeleteDataLakePartitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteDataLakePartitionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.if_exists):
            query['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.partition_values_list):
            query['PartitionValuesList'] = request.partition_values_list
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteDataLakePartitions',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.BatchDeleteDataLakePartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_data_lake_partitions(
        self,
        request: dms_20250414_models.BatchDeleteDataLakePartitionsRequest,
    ) -> dms_20250414_models.BatchDeleteDataLakePartitionsResponse:
        """
        @summary 批量删除湖仓表分区
        
        @param request: BatchDeleteDataLakePartitionsRequest
        @return: BatchDeleteDataLakePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_data_lake_partitions_with_options(request, runtime)

    async def batch_delete_data_lake_partitions_async(
        self,
        request: dms_20250414_models.BatchDeleteDataLakePartitionsRequest,
    ) -> dms_20250414_models.BatchDeleteDataLakePartitionsResponse:
        """
        @summary 批量删除湖仓表分区
        
        @param request: BatchDeleteDataLakePartitionsRequest
        @return: BatchDeleteDataLakePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_data_lake_partitions_with_options_async(request, runtime)

    def batch_update_data_lake_partitions_with_options(
        self,
        tmp_req: dms_20250414_models.BatchUpdateDataLakePartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.BatchUpdateDataLakePartitionsResponse:
        """
        @summary 批量更新湖仓表分区
        
        @param tmp_req: BatchUpdateDataLakePartitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateDataLakePartitionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.BatchUpdateDataLakePartitionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_inputs):
            request.partition_inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_inputs, 'PartitionInputs', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.partition_inputs_shrink):
            body['PartitionInputs'] = request.partition_inputs_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateDataLakePartitions',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.BatchUpdateDataLakePartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_data_lake_partitions_with_options_async(
        self,
        tmp_req: dms_20250414_models.BatchUpdateDataLakePartitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.BatchUpdateDataLakePartitionsResponse:
        """
        @summary 批量更新湖仓表分区
        
        @param tmp_req: BatchUpdateDataLakePartitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateDataLakePartitionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.BatchUpdateDataLakePartitionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_inputs):
            request.partition_inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_inputs, 'PartitionInputs', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.partition_inputs_shrink):
            body['PartitionInputs'] = request.partition_inputs_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateDataLakePartitions',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.BatchUpdateDataLakePartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_data_lake_partitions(
        self,
        request: dms_20250414_models.BatchUpdateDataLakePartitionsRequest,
    ) -> dms_20250414_models.BatchUpdateDataLakePartitionsResponse:
        """
        @summary 批量更新湖仓表分区
        
        @param request: BatchUpdateDataLakePartitionsRequest
        @return: BatchUpdateDataLakePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_update_data_lake_partitions_with_options(request, runtime)

    async def batch_update_data_lake_partitions_async(
        self,
        request: dms_20250414_models.BatchUpdateDataLakePartitionsRequest,
    ) -> dms_20250414_models.BatchUpdateDataLakePartitionsResponse:
        """
        @summary 批量更新湖仓表分区
        
        @param request: BatchUpdateDataLakePartitionsRequest
        @return: BatchUpdateDataLakePartitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_update_data_lake_partitions_with_options_async(request, runtime)

    def create_airflow_with_options(
        self,
        request: dms_20250414_models.CreateAirflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateAirflowResponse:
        """
        @summary 创建Airflow
        
        @param request: CreateAirflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAirflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_name):
            query['AirflowName'] = request.airflow_name
        if not UtilClient.is_unset(request.app_spec):
            query['AppSpec'] = request.app_spec
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dags_dir):
            query['DagsDir'] = request.dags_dir
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        if not UtilClient.is_unset(request.plugins_dir):
            query['PluginsDir'] = request.plugins_dir
        if not UtilClient.is_unset(request.requirement_file):
            query['RequirementFile'] = request.requirement_file
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.startup_file):
            query['StartupFile'] = request.startup_file
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.worker_serverless_replicas):
            query['WorkerServerlessReplicas'] = request.worker_serverless_replicas
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAirflow',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateAirflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_airflow_with_options_async(
        self,
        request: dms_20250414_models.CreateAirflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateAirflowResponse:
        """
        @summary 创建Airflow
        
        @param request: CreateAirflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAirflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_name):
            query['AirflowName'] = request.airflow_name
        if not UtilClient.is_unset(request.app_spec):
            query['AppSpec'] = request.app_spec
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dags_dir):
            query['DagsDir'] = request.dags_dir
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_path):
            query['OssPath'] = request.oss_path
        if not UtilClient.is_unset(request.plugins_dir):
            query['PluginsDir'] = request.plugins_dir
        if not UtilClient.is_unset(request.requirement_file):
            query['RequirementFile'] = request.requirement_file
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.startup_file):
            query['StartupFile'] = request.startup_file
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.worker_serverless_replicas):
            query['WorkerServerlessReplicas'] = request.worker_serverless_replicas
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAirflow',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateAirflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_airflow(
        self,
        request: dms_20250414_models.CreateAirflowRequest,
    ) -> dms_20250414_models.CreateAirflowResponse:
        """
        @summary 创建Airflow
        
        @param request: CreateAirflowRequest
        @return: CreateAirflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_airflow_with_options(request, runtime)

    async def create_airflow_async(
        self,
        request: dms_20250414_models.CreateAirflowRequest,
    ) -> dms_20250414_models.CreateAirflowResponse:
        """
        @summary 创建Airflow
        
        @param request: CreateAirflowRequest
        @return: CreateAirflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_airflow_with_options_async(request, runtime)

    def create_airflow_login_token_with_options(
        self,
        request: dms_20250414_models.CreateAirflowLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateAirflowLoginTokenResponse:
        """
        @summary Queries the Airflow logon credential. You can use this credential to log on to the DMS-managed Airflow instance.
        
        @param request: CreateAirflowLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAirflowLoginTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAirflowLoginToken',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateAirflowLoginTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_airflow_login_token_with_options_async(
        self,
        request: dms_20250414_models.CreateAirflowLoginTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateAirflowLoginTokenResponse:
        """
        @summary Queries the Airflow logon credential. You can use this credential to log on to the DMS-managed Airflow instance.
        
        @param request: CreateAirflowLoginTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAirflowLoginTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAirflowLoginToken',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateAirflowLoginTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_airflow_login_token(
        self,
        request: dms_20250414_models.CreateAirflowLoginTokenRequest,
    ) -> dms_20250414_models.CreateAirflowLoginTokenResponse:
        """
        @summary Queries the Airflow logon credential. You can use this credential to log on to the DMS-managed Airflow instance.
        
        @param request: CreateAirflowLoginTokenRequest
        @return: CreateAirflowLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_airflow_login_token_with_options(request, runtime)

    async def create_airflow_login_token_async(
        self,
        request: dms_20250414_models.CreateAirflowLoginTokenRequest,
    ) -> dms_20250414_models.CreateAirflowLoginTokenResponse:
        """
        @summary Queries the Airflow logon credential. You can use this credential to log on to the DMS-managed Airflow instance.
        
        @param request: CreateAirflowLoginTokenRequest
        @return: CreateAirflowLoginTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_airflow_login_token_with_options_async(request, runtime)

    def create_data_lake_database_with_options(
        self,
        tmp_req: dms_20250414_models.CreateDataLakeDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateDataLakeDatabaseResponse:
        """
        @summary 新建湖仓数据库
        
        @param tmp_req: CreateDataLakeDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataLakeDatabaseResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.CreateDataLakeDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataLakeDatabase',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateDataLakeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_lake_database_with_options_async(
        self,
        tmp_req: dms_20250414_models.CreateDataLakeDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateDataLakeDatabaseResponse:
        """
        @summary 新建湖仓数据库
        
        @param tmp_req: CreateDataLakeDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataLakeDatabaseResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.CreateDataLakeDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataLakeDatabase',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateDataLakeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_lake_database(
        self,
        request: dms_20250414_models.CreateDataLakeDatabaseRequest,
    ) -> dms_20250414_models.CreateDataLakeDatabaseResponse:
        """
        @summary 新建湖仓数据库
        
        @param request: CreateDataLakeDatabaseRequest
        @return: CreateDataLakeDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_lake_database_with_options(request, runtime)

    async def create_data_lake_database_async(
        self,
        request: dms_20250414_models.CreateDataLakeDatabaseRequest,
    ) -> dms_20250414_models.CreateDataLakeDatabaseResponse:
        """
        @summary 新建湖仓数据库
        
        @param request: CreateDataLakeDatabaseRequest
        @return: CreateDataLakeDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_lake_database_with_options_async(request, runtime)

    def create_data_lake_function_with_options(
        self,
        tmp_req: dms_20250414_models.CreateDataLakeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateDataLakeFunctionResponse:
        """
        @summary 新建湖仓自定义函数
        
        @param tmp_req: CreateDataLakeFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataLakeFunctionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.CreateDataLakeFunctionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.function_input):
            request.function_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.function_input, 'FunctionInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.function_input_shrink):
            body['FunctionInput'] = request.function_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataLakeFunction',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateDataLakeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_lake_function_with_options_async(
        self,
        tmp_req: dms_20250414_models.CreateDataLakeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateDataLakeFunctionResponse:
        """
        @summary 新建湖仓自定义函数
        
        @param tmp_req: CreateDataLakeFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataLakeFunctionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.CreateDataLakeFunctionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.function_input):
            request.function_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.function_input, 'FunctionInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.function_input_shrink):
            body['FunctionInput'] = request.function_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataLakeFunction',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateDataLakeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_lake_function(
        self,
        request: dms_20250414_models.CreateDataLakeFunctionRequest,
    ) -> dms_20250414_models.CreateDataLakeFunctionResponse:
        """
        @summary 新建湖仓自定义函数
        
        @param request: CreateDataLakeFunctionRequest
        @return: CreateDataLakeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_lake_function_with_options(request, runtime)

    async def create_data_lake_function_async(
        self,
        request: dms_20250414_models.CreateDataLakeFunctionRequest,
    ) -> dms_20250414_models.CreateDataLakeFunctionResponse:
        """
        @summary 新建湖仓自定义函数
        
        @param request: CreateDataLakeFunctionRequest
        @return: CreateDataLakeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_lake_function_with_options_async(request, runtime)

    def create_data_lake_partition_with_options(
        self,
        tmp_req: dms_20250414_models.CreateDataLakePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateDataLakePartitionResponse:
        """
        @summary 新建湖仓表分区
        
        @param tmp_req: CreateDataLakePartitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataLakePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.CreateDataLakePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_input):
            request.partition_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_input, 'PartitionInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.if_not_exists):
            query['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.need_result):
            query['NeedResult'] = request.need_result
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.partition_input_shrink):
            body['PartitionInput'] = request.partition_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataLakePartition',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateDataLakePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_lake_partition_with_options_async(
        self,
        tmp_req: dms_20250414_models.CreateDataLakePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateDataLakePartitionResponse:
        """
        @summary 新建湖仓表分区
        
        @param tmp_req: CreateDataLakePartitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataLakePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.CreateDataLakePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_input):
            request.partition_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_input, 'PartitionInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.if_not_exists):
            query['IfNotExists'] = request.if_not_exists
        if not UtilClient.is_unset(request.need_result):
            query['NeedResult'] = request.need_result
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.partition_input_shrink):
            body['PartitionInput'] = request.partition_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataLakePartition',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateDataLakePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_lake_partition(
        self,
        request: dms_20250414_models.CreateDataLakePartitionRequest,
    ) -> dms_20250414_models.CreateDataLakePartitionResponse:
        """
        @summary 新建湖仓表分区
        
        @param request: CreateDataLakePartitionRequest
        @return: CreateDataLakePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_lake_partition_with_options(request, runtime)

    async def create_data_lake_partition_async(
        self,
        request: dms_20250414_models.CreateDataLakePartitionRequest,
    ) -> dms_20250414_models.CreateDataLakePartitionResponse:
        """
        @summary 新建湖仓表分区
        
        @param request: CreateDataLakePartitionRequest
        @return: CreateDataLakePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_lake_partition_with_options_async(request, runtime)

    def create_data_lake_table_with_options(
        self,
        tmp_req: dms_20250414_models.CreateDataLakeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateDataLakeTableResponse:
        """
        @summary 新建湖仓表
        
        @param tmp_req: CreateDataLakeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataLakeTableResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.CreateDataLakeTableShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.table_input):
            request.table_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_input, 'TableInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.table_input_shrink):
            body['TableInput'] = request.table_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataLakeTable',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateDataLakeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_lake_table_with_options_async(
        self,
        tmp_req: dms_20250414_models.CreateDataLakeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.CreateDataLakeTableResponse:
        """
        @summary 新建湖仓表
        
        @param tmp_req: CreateDataLakeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataLakeTableResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.CreateDataLakeTableShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.table_input):
            request.table_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_input, 'TableInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.table_input_shrink):
            body['TableInput'] = request.table_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataLakeTable',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.CreateDataLakeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_lake_table(
        self,
        request: dms_20250414_models.CreateDataLakeTableRequest,
    ) -> dms_20250414_models.CreateDataLakeTableResponse:
        """
        @summary 新建湖仓表
        
        @param request: CreateDataLakeTableRequest
        @return: CreateDataLakeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_lake_table_with_options(request, runtime)

    async def create_data_lake_table_async(
        self,
        request: dms_20250414_models.CreateDataLakeTableRequest,
    ) -> dms_20250414_models.CreateDataLakeTableResponse:
        """
        @summary 新建湖仓表
        
        @param request: CreateDataLakeTableRequest
        @return: CreateDataLakeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_lake_table_with_options_async(request, runtime)

    def delete_airflow_with_options(
        self,
        request: dms_20250414_models.DeleteAirflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.DeleteAirflowResponse:
        """
        @summary 删除Airflow
        
        @param request: DeleteAirflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAirflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAirflow',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.DeleteAirflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_airflow_with_options_async(
        self,
        request: dms_20250414_models.DeleteAirflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.DeleteAirflowResponse:
        """
        @summary 删除Airflow
        
        @param request: DeleteAirflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAirflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAirflow',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.DeleteAirflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_airflow(
        self,
        request: dms_20250414_models.DeleteAirflowRequest,
    ) -> dms_20250414_models.DeleteAirflowResponse:
        """
        @summary 删除Airflow
        
        @param request: DeleteAirflowRequest
        @return: DeleteAirflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_airflow_with_options(request, runtime)

    async def delete_airflow_async(
        self,
        request: dms_20250414_models.DeleteAirflowRequest,
    ) -> dms_20250414_models.DeleteAirflowResponse:
        """
        @summary 删除Airflow
        
        @param request: DeleteAirflowRequest
        @return: DeleteAirflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_airflow_with_options_async(request, runtime)

    def delete_data_lake_database_with_options(
        self,
        request: dms_20250414_models.DeleteDataLakeDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.DeleteDataLakeDatabaseResponse:
        """
        @summary 删除湖仓数据库
        
        @param request: DeleteDataLakeDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLakeDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLakeDatabase',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.DeleteDataLakeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_lake_database_with_options_async(
        self,
        request: dms_20250414_models.DeleteDataLakeDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.DeleteDataLakeDatabaseResponse:
        """
        @summary 删除湖仓数据库
        
        @param request: DeleteDataLakeDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLakeDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLakeDatabase',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.DeleteDataLakeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_lake_database(
        self,
        request: dms_20250414_models.DeleteDataLakeDatabaseRequest,
    ) -> dms_20250414_models.DeleteDataLakeDatabaseResponse:
        """
        @summary 删除湖仓数据库
        
        @param request: DeleteDataLakeDatabaseRequest
        @return: DeleteDataLakeDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_lake_database_with_options(request, runtime)

    async def delete_data_lake_database_async(
        self,
        request: dms_20250414_models.DeleteDataLakeDatabaseRequest,
    ) -> dms_20250414_models.DeleteDataLakeDatabaseResponse:
        """
        @summary 删除湖仓数据库
        
        @param request: DeleteDataLakeDatabaseRequest
        @return: DeleteDataLakeDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_lake_database_with_options_async(request, runtime)

    def delete_data_lake_function_with_options(
        self,
        request: dms_20250414_models.DeleteDataLakeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.DeleteDataLakeFunctionResponse:
        """
        @summary 删除湖仓自定义函数
        
        @param request: DeleteDataLakeFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLakeFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLakeFunction',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.DeleteDataLakeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_lake_function_with_options_async(
        self,
        request: dms_20250414_models.DeleteDataLakeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.DeleteDataLakeFunctionResponse:
        """
        @summary 删除湖仓自定义函数
        
        @param request: DeleteDataLakeFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLakeFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLakeFunction',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.DeleteDataLakeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_lake_function(
        self,
        request: dms_20250414_models.DeleteDataLakeFunctionRequest,
    ) -> dms_20250414_models.DeleteDataLakeFunctionResponse:
        """
        @summary 删除湖仓自定义函数
        
        @param request: DeleteDataLakeFunctionRequest
        @return: DeleteDataLakeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_lake_function_with_options(request, runtime)

    async def delete_data_lake_function_async(
        self,
        request: dms_20250414_models.DeleteDataLakeFunctionRequest,
    ) -> dms_20250414_models.DeleteDataLakeFunctionResponse:
        """
        @summary 删除湖仓自定义函数
        
        @param request: DeleteDataLakeFunctionRequest
        @return: DeleteDataLakeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_lake_function_with_options_async(request, runtime)

    def delete_data_lake_partition_with_options(
        self,
        tmp_req: dms_20250414_models.DeleteDataLakePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.DeleteDataLakePartitionResponse:
        """
        @summary 删除湖仓表分区
        
        @param tmp_req: DeleteDataLakePartitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLakePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.DeleteDataLakePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_values):
            request.partition_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_values, 'PartitionValues', 'simple')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.if_exists):
            query['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.partition_values_shrink):
            query['PartitionValues'] = request.partition_values_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLakePartition',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.DeleteDataLakePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_lake_partition_with_options_async(
        self,
        tmp_req: dms_20250414_models.DeleteDataLakePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.DeleteDataLakePartitionResponse:
        """
        @summary 删除湖仓表分区
        
        @param tmp_req: DeleteDataLakePartitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLakePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.DeleteDataLakePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_values):
            request.partition_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_values, 'PartitionValues', 'simple')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.if_exists):
            query['IfExists'] = request.if_exists
        if not UtilClient.is_unset(request.partition_values_shrink):
            query['PartitionValues'] = request.partition_values_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLakePartition',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.DeleteDataLakePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_lake_partition(
        self,
        request: dms_20250414_models.DeleteDataLakePartitionRequest,
    ) -> dms_20250414_models.DeleteDataLakePartitionResponse:
        """
        @summary 删除湖仓表分区
        
        @param request: DeleteDataLakePartitionRequest
        @return: DeleteDataLakePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_lake_partition_with_options(request, runtime)

    async def delete_data_lake_partition_async(
        self,
        request: dms_20250414_models.DeleteDataLakePartitionRequest,
    ) -> dms_20250414_models.DeleteDataLakePartitionResponse:
        """
        @summary 删除湖仓表分区
        
        @param request: DeleteDataLakePartitionRequest
        @return: DeleteDataLakePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_lake_partition_with_options_async(request, runtime)

    def delete_data_lake_table_with_options(
        self,
        request: dms_20250414_models.DeleteDataLakeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.DeleteDataLakeTableResponse:
        """
        @summary 删除湖仓表
        
        @param request: DeleteDataLakeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLakeTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLakeTable',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.DeleteDataLakeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_lake_table_with_options_async(
        self,
        request: dms_20250414_models.DeleteDataLakeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.DeleteDataLakeTableResponse:
        """
        @summary 删除湖仓表
        
        @param request: DeleteDataLakeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataLakeTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataLakeTable',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.DeleteDataLakeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_lake_table(
        self,
        request: dms_20250414_models.DeleteDataLakeTableRequest,
    ) -> dms_20250414_models.DeleteDataLakeTableResponse:
        """
        @summary 删除湖仓表
        
        @param request: DeleteDataLakeTableRequest
        @return: DeleteDataLakeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_lake_table_with_options(request, runtime)

    async def delete_data_lake_table_async(
        self,
        request: dms_20250414_models.DeleteDataLakeTableRequest,
    ) -> dms_20250414_models.DeleteDataLakeTableResponse:
        """
        @summary 删除湖仓表
        
        @param request: DeleteDataLakeTableRequest
        @return: DeleteDataLakeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_lake_table_with_options_async(request, runtime)

    def get_airflow_with_options(
        self,
        request: dms_20250414_models.GetAirflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetAirflowResponse:
        """
        @summary 查询 Airflow
        
        @param request: GetAirflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAirflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAirflow',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetAirflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_airflow_with_options_async(
        self,
        request: dms_20250414_models.GetAirflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetAirflowResponse:
        """
        @summary 查询 Airflow
        
        @param request: GetAirflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAirflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAirflow',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetAirflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_airflow(
        self,
        request: dms_20250414_models.GetAirflowRequest,
    ) -> dms_20250414_models.GetAirflowResponse:
        """
        @summary 查询 Airflow
        
        @param request: GetAirflowRequest
        @return: GetAirflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_airflow_with_options(request, runtime)

    async def get_airflow_async(
        self,
        request: dms_20250414_models.GetAirflowRequest,
    ) -> dms_20250414_models.GetAirflowResponse:
        """
        @summary 查询 Airflow
        
        @param request: GetAirflowRequest
        @return: GetAirflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_airflow_with_options_async(request, runtime)

    def get_chat_content_with_options(
        self,
        request: dms_20250414_models.GetChatContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetChatContentResponse:
        """
        @summary GetChatContent
        
        @param request: GetChatContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatContent',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetChatContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chat_content_with_options_async(
        self,
        request: dms_20250414_models.GetChatContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetChatContentResponse:
        """
        @summary GetChatContent
        
        @param request: GetChatContentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChatContentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatContent',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetChatContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chat_content(
        self,
        request: dms_20250414_models.GetChatContentRequest,
    ) -> dms_20250414_models.GetChatContentResponse:
        """
        @summary GetChatContent
        
        @param request: GetChatContentRequest
        @return: GetChatContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chat_content_with_options(request, runtime)

    async def get_chat_content_async(
        self,
        request: dms_20250414_models.GetChatContentRequest,
    ) -> dms_20250414_models.GetChatContentResponse:
        """
        @summary GetChatContent
        
        @param request: GetChatContentRequest
        @return: GetChatContentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_chat_content_with_options_async(request, runtime)

    def get_data_lake_catalog_with_options(
        self,
        request: dms_20250414_models.GetDataLakeCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetDataLakeCatalogResponse:
        """
        @summary 获取uc的数据库目录
        
        @param request: GetDataLakeCatalogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataLakeCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataLakeCatalog',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetDataLakeCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_lake_catalog_with_options_async(
        self,
        request: dms_20250414_models.GetDataLakeCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetDataLakeCatalogResponse:
        """
        @summary 获取uc的数据库目录
        
        @param request: GetDataLakeCatalogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataLakeCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataLakeCatalog',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetDataLakeCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_lake_catalog(
        self,
        request: dms_20250414_models.GetDataLakeCatalogRequest,
    ) -> dms_20250414_models.GetDataLakeCatalogResponse:
        """
        @summary 获取uc的数据库目录
        
        @param request: GetDataLakeCatalogRequest
        @return: GetDataLakeCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_lake_catalog_with_options(request, runtime)

    async def get_data_lake_catalog_async(
        self,
        request: dms_20250414_models.GetDataLakeCatalogRequest,
    ) -> dms_20250414_models.GetDataLakeCatalogResponse:
        """
        @summary 获取uc的数据库目录
        
        @param request: GetDataLakeCatalogRequest
        @return: GetDataLakeCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_lake_catalog_with_options_async(request, runtime)

    def get_data_lake_database_with_options(
        self,
        request: dms_20250414_models.GetDataLakeDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetDataLakeDatabaseResponse:
        """
        @summary 获取UC的数据库
        
        @param request: GetDataLakeDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataLakeDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataLakeDatabase',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetDataLakeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_lake_database_with_options_async(
        self,
        request: dms_20250414_models.GetDataLakeDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetDataLakeDatabaseResponse:
        """
        @summary 获取UC的数据库
        
        @param request: GetDataLakeDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataLakeDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataLakeDatabase',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetDataLakeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_lake_database(
        self,
        request: dms_20250414_models.GetDataLakeDatabaseRequest,
    ) -> dms_20250414_models.GetDataLakeDatabaseResponse:
        """
        @summary 获取UC的数据库
        
        @param request: GetDataLakeDatabaseRequest
        @return: GetDataLakeDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_lake_database_with_options(request, runtime)

    async def get_data_lake_database_async(
        self,
        request: dms_20250414_models.GetDataLakeDatabaseRequest,
    ) -> dms_20250414_models.GetDataLakeDatabaseResponse:
        """
        @summary 获取UC的数据库
        
        @param request: GetDataLakeDatabaseRequest
        @return: GetDataLakeDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_lake_database_with_options_async(request, runtime)

    def get_data_lake_function_with_options(
        self,
        request: dms_20250414_models.GetDataLakeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetDataLakeFunctionResponse:
        """
        @summary 获取湖仓自定义函数详细信息
        
        @param request: GetDataLakeFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataLakeFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataLakeFunction',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetDataLakeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_lake_function_with_options_async(
        self,
        request: dms_20250414_models.GetDataLakeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetDataLakeFunctionResponse:
        """
        @summary 获取湖仓自定义函数详细信息
        
        @param request: GetDataLakeFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataLakeFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataLakeFunction',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetDataLakeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_lake_function(
        self,
        request: dms_20250414_models.GetDataLakeFunctionRequest,
    ) -> dms_20250414_models.GetDataLakeFunctionResponse:
        """
        @summary 获取湖仓自定义函数详细信息
        
        @param request: GetDataLakeFunctionRequest
        @return: GetDataLakeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_lake_function_with_options(request, runtime)

    async def get_data_lake_function_async(
        self,
        request: dms_20250414_models.GetDataLakeFunctionRequest,
    ) -> dms_20250414_models.GetDataLakeFunctionResponse:
        """
        @summary 获取湖仓自定义函数详细信息
        
        @param request: GetDataLakeFunctionRequest
        @return: GetDataLakeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_lake_function_with_options_async(request, runtime)

    def get_data_lake_partition_with_options(
        self,
        tmp_req: dms_20250414_models.GetDataLakePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetDataLakePartitionResponse:
        """
        @summary 获取湖仓表分区详情
        
        @param tmp_req: GetDataLakePartitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataLakePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.GetDataLakePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_values):
            request.partition_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_values, 'PartitionValues', 'simple')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.partition_values_shrink):
            query['PartitionValues'] = request.partition_values_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataLakePartition',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetDataLakePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_lake_partition_with_options_async(
        self,
        tmp_req: dms_20250414_models.GetDataLakePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetDataLakePartitionResponse:
        """
        @summary 获取湖仓表分区详情
        
        @param tmp_req: GetDataLakePartitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataLakePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.GetDataLakePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_values):
            request.partition_values_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_values, 'PartitionValues', 'simple')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.partition_values_shrink):
            query['PartitionValues'] = request.partition_values_shrink
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataLakePartition',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetDataLakePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_lake_partition(
        self,
        request: dms_20250414_models.GetDataLakePartitionRequest,
    ) -> dms_20250414_models.GetDataLakePartitionResponse:
        """
        @summary 获取湖仓表分区详情
        
        @param request: GetDataLakePartitionRequest
        @return: GetDataLakePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_lake_partition_with_options(request, runtime)

    async def get_data_lake_partition_async(
        self,
        request: dms_20250414_models.GetDataLakePartitionRequest,
    ) -> dms_20250414_models.GetDataLakePartitionResponse:
        """
        @summary 获取湖仓表分区详情
        
        @param request: GetDataLakePartitionRequest
        @return: GetDataLakePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_lake_partition_with_options_async(request, runtime)

    def get_data_lake_table_with_options(
        self,
        request: dms_20250414_models.GetDataLakeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetDataLakeTableResponse:
        """
        @summary 获取表信息
        
        @param request: GetDataLakeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataLakeTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataLakeTable',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetDataLakeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_lake_table_with_options_async(
        self,
        request: dms_20250414_models.GetDataLakeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetDataLakeTableResponse:
        """
        @summary 获取表信息
        
        @param request: GetDataLakeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDataLakeTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataLakeTable',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetDataLakeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_lake_table(
        self,
        request: dms_20250414_models.GetDataLakeTableRequest,
    ) -> dms_20250414_models.GetDataLakeTableResponse:
        """
        @summary 获取表信息
        
        @param request: GetDataLakeTableRequest
        @return: GetDataLakeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_data_lake_table_with_options(request, runtime)

    async def get_data_lake_table_async(
        self,
        request: dms_20250414_models.GetDataLakeTableRequest,
    ) -> dms_20250414_models.GetDataLakeTableResponse:
        """
        @summary 获取表信息
        
        @param request: GetDataLakeTableRequest
        @return: GetDataLakeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_data_lake_table_with_options_async(request, runtime)

    def get_notebook_and_submit_task_with_options(
        self,
        request: dms_20250414_models.GetNotebookAndSubmitTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetNotebookAndSubmitTaskResponse:
        """
        @summary 调度运行Notebook文件
        
        @param request: GetNotebookAndSubmitTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNotebookAndSubmitTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.retry):
            body['Retry'] = request.retry
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNotebookAndSubmitTask',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetNotebookAndSubmitTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_notebook_and_submit_task_with_options_async(
        self,
        request: dms_20250414_models.GetNotebookAndSubmitTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetNotebookAndSubmitTaskResponse:
        """
        @summary 调度运行Notebook文件
        
        @param request: GetNotebookAndSubmitTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNotebookAndSubmitTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.params):
            body['Params'] = request.params
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        if not UtilClient.is_unset(request.retry):
            body['Retry'] = request.retry
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetNotebookAndSubmitTask',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetNotebookAndSubmitTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_notebook_and_submit_task(
        self,
        request: dms_20250414_models.GetNotebookAndSubmitTaskRequest,
    ) -> dms_20250414_models.GetNotebookAndSubmitTaskResponse:
        """
        @summary 调度运行Notebook文件
        
        @param request: GetNotebookAndSubmitTaskRequest
        @return: GetNotebookAndSubmitTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_notebook_and_submit_task_with_options(request, runtime)

    async def get_notebook_and_submit_task_async(
        self,
        request: dms_20250414_models.GetNotebookAndSubmitTaskRequest,
    ) -> dms_20250414_models.GetNotebookAndSubmitTaskResponse:
        """
        @summary 调度运行Notebook文件
        
        @param request: GetNotebookAndSubmitTaskRequest
        @return: GetNotebookAndSubmitTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_notebook_and_submit_task_with_options_async(request, runtime)

    def get_notebook_task_status_with_options(
        self,
        request: dms_20250414_models.GetNotebookTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetNotebookTaskStatusResponse:
        """
        @summary 查看Notebook任务运行结果
        
        @param request: GetNotebookTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNotebookTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNotebookTaskStatus',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetNotebookTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_notebook_task_status_with_options_async(
        self,
        request: dms_20250414_models.GetNotebookTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.GetNotebookTaskStatusResponse:
        """
        @summary 查看Notebook任务运行结果
        
        @param request: GetNotebookTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNotebookTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNotebookTaskStatus',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.GetNotebookTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_notebook_task_status(
        self,
        request: dms_20250414_models.GetNotebookTaskStatusRequest,
    ) -> dms_20250414_models.GetNotebookTaskStatusResponse:
        """
        @summary 查看Notebook任务运行结果
        
        @param request: GetNotebookTaskStatusRequest
        @return: GetNotebookTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_notebook_task_status_with_options(request, runtime)

    async def get_notebook_task_status_async(
        self,
        request: dms_20250414_models.GetNotebookTaskStatusRequest,
    ) -> dms_20250414_models.GetNotebookTaskStatusResponse:
        """
        @summary 查看Notebook任务运行结果
        
        @param request: GetNotebookTaskStatusRequest
        @return: GetNotebookTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_notebook_task_status_with_options_async(request, runtime)

    def list_airflows_with_options(
        self,
        request: dms_20250414_models.ListAirflowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListAirflowsResponse:
        """
        @summary 列出资源Airflow
        
        @param request: ListAirflowsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAirflowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.skip):
            query['Skip'] = request.skip
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAirflows',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListAirflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_airflows_with_options_async(
        self,
        request: dms_20250414_models.ListAirflowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListAirflowsResponse:
        """
        @summary 列出资源Airflow
        
        @param request: ListAirflowsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAirflowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_index):
            query['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.skip):
            query['Skip'] = request.skip
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAirflows',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListAirflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_airflows(
        self,
        request: dms_20250414_models.ListAirflowsRequest,
    ) -> dms_20250414_models.ListAirflowsResponse:
        """
        @summary 列出资源Airflow
        
        @param request: ListAirflowsRequest
        @return: ListAirflowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_airflows_with_options(request, runtime)

    async def list_airflows_async(
        self,
        request: dms_20250414_models.ListAirflowsRequest,
    ) -> dms_20250414_models.ListAirflowsResponse:
        """
        @summary 列出资源Airflow
        
        @param request: ListAirflowsRequest
        @return: ListAirflowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_airflows_with_options_async(request, runtime)

    def list_data_lake_catalog_with_options(
        self,
        request: dms_20250414_models.ListDataLakeCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeCatalogResponse:
        """
        @summary 获取uc的数据库目录列表
        
        @param request: ListDataLakeCatalogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeCatalog',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_catalog_with_options_async(
        self,
        request: dms_20250414_models.ListDataLakeCatalogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeCatalogResponse:
        """
        @summary 获取uc的数据库目录列表
        
        @param request: ListDataLakeCatalogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeCatalog',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_catalog(
        self,
        request: dms_20250414_models.ListDataLakeCatalogRequest,
    ) -> dms_20250414_models.ListDataLakeCatalogResponse:
        """
        @summary 获取uc的数据库目录列表
        
        @param request: ListDataLakeCatalogRequest
        @return: ListDataLakeCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_lake_catalog_with_options(request, runtime)

    async def list_data_lake_catalog_async(
        self,
        request: dms_20250414_models.ListDataLakeCatalogRequest,
    ) -> dms_20250414_models.ListDataLakeCatalogResponse:
        """
        @summary 获取uc的数据库目录列表
        
        @param request: ListDataLakeCatalogRequest
        @return: ListDataLakeCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_lake_catalog_with_options_async(request, runtime)

    def list_data_lake_database_with_options(
        self,
        request: dms_20250414_models.ListDataLakeDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeDatabaseResponse:
        """
        @summary 获取数据库列表
        
        @param request: ListDataLakeDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeDatabase',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_database_with_options_async(
        self,
        request: dms_20250414_models.ListDataLakeDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeDatabaseResponse:
        """
        @summary 获取数据库列表
        
        @param request: ListDataLakeDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeDatabase',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_database(
        self,
        request: dms_20250414_models.ListDataLakeDatabaseRequest,
    ) -> dms_20250414_models.ListDataLakeDatabaseResponse:
        """
        @summary 获取数据库列表
        
        @param request: ListDataLakeDatabaseRequest
        @return: ListDataLakeDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_lake_database_with_options(request, runtime)

    async def list_data_lake_database_async(
        self,
        request: dms_20250414_models.ListDataLakeDatabaseRequest,
    ) -> dms_20250414_models.ListDataLakeDatabaseResponse:
        """
        @summary 获取数据库列表
        
        @param request: ListDataLakeDatabaseRequest
        @return: ListDataLakeDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_lake_database_with_options_async(request, runtime)

    def list_data_lake_function_with_options(
        self,
        request: dms_20250414_models.ListDataLakeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeFunctionResponse:
        """
        @summary 获取数据湖函数列表
        
        @param request: ListDataLakeFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeFunction',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_function_with_options_async(
        self,
        request: dms_20250414_models.ListDataLakeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeFunctionResponse:
        """
        @summary 获取数据湖函数列表
        
        @param request: ListDataLakeFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeFunctionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeFunction',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_function(
        self,
        request: dms_20250414_models.ListDataLakeFunctionRequest,
    ) -> dms_20250414_models.ListDataLakeFunctionResponse:
        """
        @summary 获取数据湖函数列表
        
        @param request: ListDataLakeFunctionRequest
        @return: ListDataLakeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_lake_function_with_options(request, runtime)

    async def list_data_lake_function_async(
        self,
        request: dms_20250414_models.ListDataLakeFunctionRequest,
    ) -> dms_20250414_models.ListDataLakeFunctionResponse:
        """
        @summary 获取数据湖函数列表
        
        @param request: ListDataLakeFunctionRequest
        @return: ListDataLakeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_lake_function_with_options_async(request, runtime)

    def list_data_lake_function_name_with_options(
        self,
        request: dms_20250414_models.ListDataLakeFunctionNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeFunctionNameResponse:
        """
        @summary 获取数据湖函数名列表
        
        @param request: ListDataLakeFunctionNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeFunctionNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeFunctionName',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeFunctionNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_function_name_with_options_async(
        self,
        request: dms_20250414_models.ListDataLakeFunctionNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeFunctionNameResponse:
        """
        @summary 获取数据湖函数名列表
        
        @param request: ListDataLakeFunctionNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeFunctionNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.function_name_pattern):
            query['FunctionNamePattern'] = request.function_name_pattern
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeFunctionName',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeFunctionNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_function_name(
        self,
        request: dms_20250414_models.ListDataLakeFunctionNameRequest,
    ) -> dms_20250414_models.ListDataLakeFunctionNameResponse:
        """
        @summary 获取数据湖函数名列表
        
        @param request: ListDataLakeFunctionNameRequest
        @return: ListDataLakeFunctionNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_lake_function_name_with_options(request, runtime)

    async def list_data_lake_function_name_async(
        self,
        request: dms_20250414_models.ListDataLakeFunctionNameRequest,
    ) -> dms_20250414_models.ListDataLakeFunctionNameResponse:
        """
        @summary 获取数据湖函数名列表
        
        @param request: ListDataLakeFunctionNameRequest
        @return: ListDataLakeFunctionNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_lake_function_name_with_options_async(request, runtime)

    def list_data_lake_partition_with_options(
        self,
        tmp_req: dms_20250414_models.ListDataLakePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakePartitionResponse:
        """
        @summary 获取数据湖表分区列表
        
        @param tmp_req: ListDataLakePartitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.ListDataLakePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.part_names):
            request.part_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.part_names, 'PartNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.part_names_shrink):
            body['PartNames'] = request.part_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataLakePartition',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_partition_with_options_async(
        self,
        tmp_req: dms_20250414_models.ListDataLakePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakePartitionResponse:
        """
        @summary 获取数据湖表分区列表
        
        @param tmp_req: ListDataLakePartitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.ListDataLakePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.part_names):
            request.part_names_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.part_names, 'PartNames', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.part_names_shrink):
            body['PartNames'] = request.part_names_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataLakePartition',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_partition(
        self,
        request: dms_20250414_models.ListDataLakePartitionRequest,
    ) -> dms_20250414_models.ListDataLakePartitionResponse:
        """
        @summary 获取数据湖表分区列表
        
        @param request: ListDataLakePartitionRequest
        @return: ListDataLakePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_lake_partition_with_options(request, runtime)

    async def list_data_lake_partition_async(
        self,
        request: dms_20250414_models.ListDataLakePartitionRequest,
    ) -> dms_20250414_models.ListDataLakePartitionResponse:
        """
        @summary 获取数据湖表分区列表
        
        @param request: ListDataLakePartitionRequest
        @return: ListDataLakePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_lake_partition_with_options_async(request, runtime)

    def list_data_lake_partition_by_filter_with_options(
        self,
        request: dms_20250414_models.ListDataLakePartitionByFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakePartitionByFilterResponse:
        """
        @summary 根据筛选条件获取数据湖表分区列表
        
        @param request: ListDataLakePartitionByFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakePartitionByFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataLakePartitionByFilter',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakePartitionByFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_partition_by_filter_with_options_async(
        self,
        request: dms_20250414_models.ListDataLakePartitionByFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakePartitionByFilterResponse:
        """
        @summary 根据筛选条件获取数据湖表分区列表
        
        @param request: ListDataLakePartitionByFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakePartitionByFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.filter):
            body['Filter'] = request.filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataLakePartitionByFilter',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakePartitionByFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_partition_by_filter(
        self,
        request: dms_20250414_models.ListDataLakePartitionByFilterRequest,
    ) -> dms_20250414_models.ListDataLakePartitionByFilterResponse:
        """
        @summary 根据筛选条件获取数据湖表分区列表
        
        @param request: ListDataLakePartitionByFilterRequest
        @return: ListDataLakePartitionByFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_lake_partition_by_filter_with_options(request, runtime)

    async def list_data_lake_partition_by_filter_async(
        self,
        request: dms_20250414_models.ListDataLakePartitionByFilterRequest,
    ) -> dms_20250414_models.ListDataLakePartitionByFilterResponse:
        """
        @summary 根据筛选条件获取数据湖表分区列表
        
        @param request: ListDataLakePartitionByFilterRequest
        @return: ListDataLakePartitionByFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_lake_partition_by_filter_with_options_async(request, runtime)

    def list_data_lake_partition_name_with_options(
        self,
        request: dms_20250414_models.ListDataLakePartitionNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakePartitionNameResponse:
        """
        @summary 获取数据湖表分区名列表
        
        @param request: ListDataLakePartitionNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakePartitionNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakePartitionName',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakePartitionNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_partition_name_with_options_async(
        self,
        request: dms_20250414_models.ListDataLakePartitionNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakePartitionNameResponse:
        """
        @summary 获取数据湖表分区名列表
        
        @param request: ListDataLakePartitionNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakePartitionNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakePartitionName',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakePartitionNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_partition_name(
        self,
        request: dms_20250414_models.ListDataLakePartitionNameRequest,
    ) -> dms_20250414_models.ListDataLakePartitionNameResponse:
        """
        @summary 获取数据湖表分区名列表
        
        @param request: ListDataLakePartitionNameRequest
        @return: ListDataLakePartitionNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_lake_partition_name_with_options(request, runtime)

    async def list_data_lake_partition_name_async(
        self,
        request: dms_20250414_models.ListDataLakePartitionNameRequest,
    ) -> dms_20250414_models.ListDataLakePartitionNameResponse:
        """
        @summary 获取数据湖表分区名列表
        
        @param request: ListDataLakePartitionNameRequest
        @return: ListDataLakePartitionNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_lake_partition_name_with_options_async(request, runtime)

    def list_data_lake_table_with_options(
        self,
        request: dms_20250414_models.ListDataLakeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeTableResponse:
        """
        @summary 获取数据湖表列表
        
        @param request: ListDataLakeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeTable',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_table_with_options_async(
        self,
        request: dms_20250414_models.ListDataLakeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeTableResponse:
        """
        @summary 获取数据湖表列表
        
        @param request: ListDataLakeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeTable',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_table(
        self,
        request: dms_20250414_models.ListDataLakeTableRequest,
    ) -> dms_20250414_models.ListDataLakeTableResponse:
        """
        @summary 获取数据湖表列表
        
        @param request: ListDataLakeTableRequest
        @return: ListDataLakeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_lake_table_with_options(request, runtime)

    async def list_data_lake_table_async(
        self,
        request: dms_20250414_models.ListDataLakeTableRequest,
    ) -> dms_20250414_models.ListDataLakeTableResponse:
        """
        @summary 获取数据湖表列表
        
        @param request: ListDataLakeTableRequest
        @return: ListDataLakeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_lake_table_with_options_async(request, runtime)

    def list_data_lake_table_name_with_options(
        self,
        request: dms_20250414_models.ListDataLakeTableNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeTableNameResponse:
        """
        @summary 获取数据湖表名列表
        
        @param request: ListDataLakeTableNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeTableNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeTableName',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeTableNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_table_name_with_options_async(
        self,
        request: dms_20250414_models.ListDataLakeTableNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeTableNameResponse:
        """
        @summary 获取数据湖表名列表
        
        @param request: ListDataLakeTableNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeTableNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.table_name_pattern):
            query['TableNamePattern'] = request.table_name_pattern
        if not UtilClient.is_unset(request.table_type):
            query['TableType'] = request.table_type
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeTableName',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeTableNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_table_name(
        self,
        request: dms_20250414_models.ListDataLakeTableNameRequest,
    ) -> dms_20250414_models.ListDataLakeTableNameResponse:
        """
        @summary 获取数据湖表名列表
        
        @param request: ListDataLakeTableNameRequest
        @return: ListDataLakeTableNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_lake_table_name_with_options(request, runtime)

    async def list_data_lake_table_name_async(
        self,
        request: dms_20250414_models.ListDataLakeTableNameRequest,
    ) -> dms_20250414_models.ListDataLakeTableNameResponse:
        """
        @summary 获取数据湖表名列表
        
        @param request: ListDataLakeTableNameRequest
        @return: ListDataLakeTableNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_lake_table_name_with_options_async(request, runtime)

    def list_data_lake_tablebase_info_with_options(
        self,
        request: dms_20250414_models.ListDataLakeTablebaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeTablebaseInfoResponse:
        """
        @summary 获取表信息
        
        @param request: ListDataLakeTablebaseInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeTablebaseInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.rows):
            query['Rows'] = request.rows
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeTablebaseInfo',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeTablebaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_lake_tablebase_info_with_options_async(
        self,
        request: dms_20250414_models.ListDataLakeTablebaseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.ListDataLakeTablebaseInfoResponse:
        """
        @summary 获取表信息
        
        @param request: ListDataLakeTablebaseInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataLakeTablebaseInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.rows):
            query['Rows'] = request.rows
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataLakeTablebaseInfo',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.ListDataLakeTablebaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_lake_tablebase_info(
        self,
        request: dms_20250414_models.ListDataLakeTablebaseInfoRequest,
    ) -> dms_20250414_models.ListDataLakeTablebaseInfoResponse:
        """
        @summary 获取表信息
        
        @param request: ListDataLakeTablebaseInfoRequest
        @return: ListDataLakeTablebaseInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_lake_tablebase_info_with_options(request, runtime)

    async def list_data_lake_tablebase_info_async(
        self,
        request: dms_20250414_models.ListDataLakeTablebaseInfoRequest,
    ) -> dms_20250414_models.ListDataLakeTablebaseInfoResponse:
        """
        @summary 获取表信息
        
        @param request: ListDataLakeTablebaseInfoRequest
        @return: ListDataLakeTablebaseInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_lake_tablebase_info_with_options_async(request, runtime)

    def send_chat_message_with_options(
        self,
        tmp_req: dms_20250414_models.SendChatMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.SendChatMessageResponse:
        """
        @summary SendChatMessage
        
        @param tmp_req: SendChatMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendChatMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.SendChatMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source):
            request.data_source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source, 'DataSource', 'json')
        if not UtilClient.is_unset(tmp_req.session_config):
            request.session_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.session_config, 'SessionConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not UtilClient.is_unset(request.data_source_shrink):
            query['DataSource'] = request.data_source_shrink
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.question):
            query['Question'] = request.question
        if not UtilClient.is_unset(request.quoted_message):
            query['QuotedMessage'] = request.quoted_message
        if not UtilClient.is_unset(request.reply_to):
            query['ReplyTo'] = request.reply_to
        if not UtilClient.is_unset(request.session_config_shrink):
            query['SessionConfig'] = request.session_config_shrink
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendChatMessage',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.SendChatMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_chat_message_with_options_async(
        self,
        tmp_req: dms_20250414_models.SendChatMessageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.SendChatMessageResponse:
        """
        @summary SendChatMessage
        
        @param tmp_req: SendChatMessageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendChatMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.SendChatMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source):
            request.data_source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source, 'DataSource', 'json')
        if not UtilClient.is_unset(tmp_req.session_config):
            request.session_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.session_config, 'SessionConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_id):
            query['AgentId'] = request.agent_id
        if not UtilClient.is_unset(request.dmsunit):
            query['DMSUnit'] = request.dmsunit
        if not UtilClient.is_unset(request.data_source_shrink):
            query['DataSource'] = request.data_source_shrink
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.question):
            query['Question'] = request.question
        if not UtilClient.is_unset(request.quoted_message):
            query['QuotedMessage'] = request.quoted_message
        if not UtilClient.is_unset(request.reply_to):
            query['ReplyTo'] = request.reply_to
        if not UtilClient.is_unset(request.session_config_shrink):
            query['SessionConfig'] = request.session_config_shrink
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendChatMessage',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.SendChatMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_chat_message(
        self,
        request: dms_20250414_models.SendChatMessageRequest,
    ) -> dms_20250414_models.SendChatMessageResponse:
        """
        @summary SendChatMessage
        
        @param request: SendChatMessageRequest
        @return: SendChatMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_chat_message_with_options(request, runtime)

    async def send_chat_message_async(
        self,
        request: dms_20250414_models.SendChatMessageRequest,
    ) -> dms_20250414_models.SendChatMessageResponse:
        """
        @summary SendChatMessage
        
        @param request: SendChatMessageRequest
        @return: SendChatMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_chat_message_with_options_async(request, runtime)

    def update_airflow_with_options(
        self,
        request: dms_20250414_models.UpdateAirflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.UpdateAirflowResponse:
        """
        @summary 更新UpdateAirflow
        
        @param request: UpdateAirflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAirflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not UtilClient.is_unset(request.airflow_name):
            query['AirflowName'] = request.airflow_name
        if not UtilClient.is_unset(request.app_spec):
            query['AppSpec'] = request.app_spec
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dags_dir):
            query['DagsDir'] = request.dags_dir
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.plugins_dir):
            query['PluginsDir'] = request.plugins_dir
        if not UtilClient.is_unset(request.requirement_file):
            query['RequirementFile'] = request.requirement_file
        if not UtilClient.is_unset(request.startup_file):
            query['StartupFile'] = request.startup_file
        if not UtilClient.is_unset(request.worker_serverless_replicas):
            query['WorkerServerlessReplicas'] = request.worker_serverless_replicas
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAirflow',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.UpdateAirflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_airflow_with_options_async(
        self,
        request: dms_20250414_models.UpdateAirflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.UpdateAirflowResponse:
        """
        @summary 更新UpdateAirflow
        
        @param request: UpdateAirflowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAirflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.airflow_id):
            query['AirflowId'] = request.airflow_id
        if not UtilClient.is_unset(request.airflow_name):
            query['AirflowName'] = request.airflow_name
        if not UtilClient.is_unset(request.app_spec):
            query['AppSpec'] = request.app_spec
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dags_dir):
            query['DagsDir'] = request.dags_dir
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.plugins_dir):
            query['PluginsDir'] = request.plugins_dir
        if not UtilClient.is_unset(request.requirement_file):
            query['RequirementFile'] = request.requirement_file
        if not UtilClient.is_unset(request.startup_file):
            query['StartupFile'] = request.startup_file
        if not UtilClient.is_unset(request.worker_serverless_replicas):
            query['WorkerServerlessReplicas'] = request.worker_serverless_replicas
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAirflow',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.UpdateAirflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_airflow(
        self,
        request: dms_20250414_models.UpdateAirflowRequest,
    ) -> dms_20250414_models.UpdateAirflowResponse:
        """
        @summary 更新UpdateAirflow
        
        @param request: UpdateAirflowRequest
        @return: UpdateAirflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_airflow_with_options(request, runtime)

    async def update_airflow_async(
        self,
        request: dms_20250414_models.UpdateAirflowRequest,
    ) -> dms_20250414_models.UpdateAirflowResponse:
        """
        @summary 更新UpdateAirflow
        
        @param request: UpdateAirflowRequest
        @return: UpdateAirflowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_airflow_with_options_async(request, runtime)

    def update_data_lake_database_with_options(
        self,
        tmp_req: dms_20250414_models.UpdateDataLakeDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.UpdateDataLakeDatabaseResponse:
        """
        @summary 更新湖仓数据库
        
        @param tmp_req: UpdateDataLakeDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataLakeDatabaseResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.UpdateDataLakeDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataLakeDatabase',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.UpdateDataLakeDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_lake_database_with_options_async(
        self,
        tmp_req: dms_20250414_models.UpdateDataLakeDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.UpdateDataLakeDatabaseResponse:
        """
        @summary 更新湖仓数据库
        
        @param tmp_req: UpdateDataLakeDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataLakeDatabaseResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.UpdateDataLakeDatabaseShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataLakeDatabase',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.UpdateDataLakeDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_lake_database(
        self,
        request: dms_20250414_models.UpdateDataLakeDatabaseRequest,
    ) -> dms_20250414_models.UpdateDataLakeDatabaseResponse:
        """
        @summary 更新湖仓数据库
        
        @param request: UpdateDataLakeDatabaseRequest
        @return: UpdateDataLakeDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_lake_database_with_options(request, runtime)

    async def update_data_lake_database_async(
        self,
        request: dms_20250414_models.UpdateDataLakeDatabaseRequest,
    ) -> dms_20250414_models.UpdateDataLakeDatabaseResponse:
        """
        @summary 更新湖仓数据库
        
        @param request: UpdateDataLakeDatabaseRequest
        @return: UpdateDataLakeDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_lake_database_with_options_async(request, runtime)

    def update_data_lake_function_with_options(
        self,
        tmp_req: dms_20250414_models.UpdateDataLakeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.UpdateDataLakeFunctionResponse:
        """
        @summary 更新湖仓自定义函数
        
        @param tmp_req: UpdateDataLakeFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataLakeFunctionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.UpdateDataLakeFunctionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.function_input):
            request.function_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.function_input, 'FunctionInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.function_input_shrink):
            body['FunctionInput'] = request.function_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataLakeFunction',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.UpdateDataLakeFunctionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_lake_function_with_options_async(
        self,
        tmp_req: dms_20250414_models.UpdateDataLakeFunctionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.UpdateDataLakeFunctionResponse:
        """
        @summary 更新湖仓自定义函数
        
        @param tmp_req: UpdateDataLakeFunctionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataLakeFunctionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.UpdateDataLakeFunctionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.function_input):
            request.function_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.function_input, 'FunctionInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.function_input_shrink):
            body['FunctionInput'] = request.function_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataLakeFunction',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.UpdateDataLakeFunctionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_lake_function(
        self,
        request: dms_20250414_models.UpdateDataLakeFunctionRequest,
    ) -> dms_20250414_models.UpdateDataLakeFunctionResponse:
        """
        @summary 更新湖仓自定义函数
        
        @param request: UpdateDataLakeFunctionRequest
        @return: UpdateDataLakeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_lake_function_with_options(request, runtime)

    async def update_data_lake_function_async(
        self,
        request: dms_20250414_models.UpdateDataLakeFunctionRequest,
    ) -> dms_20250414_models.UpdateDataLakeFunctionResponse:
        """
        @summary 更新湖仓自定义函数
        
        @param request: UpdateDataLakeFunctionRequest
        @return: UpdateDataLakeFunctionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_lake_function_with_options_async(request, runtime)

    def update_data_lake_partition_with_options(
        self,
        tmp_req: dms_20250414_models.UpdateDataLakePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.UpdateDataLakePartitionResponse:
        """
        @summary 更新湖仓表分区
        
        @param tmp_req: UpdateDataLakePartitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataLakePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.UpdateDataLakePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_input):
            request.partition_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_input, 'PartitionInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.partition_input_shrink):
            body['PartitionInput'] = request.partition_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataLakePartition',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.UpdateDataLakePartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_lake_partition_with_options_async(
        self,
        tmp_req: dms_20250414_models.UpdateDataLakePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.UpdateDataLakePartitionResponse:
        """
        @summary 更新湖仓表分区
        
        @param tmp_req: UpdateDataLakePartitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataLakePartitionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.UpdateDataLakePartitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.partition_input):
            request.partition_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.partition_input, 'PartitionInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.partition_input_shrink):
            body['PartitionInput'] = request.partition_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataLakePartition',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.UpdateDataLakePartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_lake_partition(
        self,
        request: dms_20250414_models.UpdateDataLakePartitionRequest,
    ) -> dms_20250414_models.UpdateDataLakePartitionResponse:
        """
        @summary 更新湖仓表分区
        
        @param request: UpdateDataLakePartitionRequest
        @return: UpdateDataLakePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_lake_partition_with_options(request, runtime)

    async def update_data_lake_partition_async(
        self,
        request: dms_20250414_models.UpdateDataLakePartitionRequest,
    ) -> dms_20250414_models.UpdateDataLakePartitionResponse:
        """
        @summary 更新湖仓表分区
        
        @param request: UpdateDataLakePartitionRequest
        @return: UpdateDataLakePartitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_lake_partition_with_options_async(request, runtime)

    def update_data_lake_table_with_options(
        self,
        tmp_req: dms_20250414_models.UpdateDataLakeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.UpdateDataLakeTableResponse:
        """
        @summary 更新湖仓表信息
        
        @param tmp_req: UpdateDataLakeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataLakeTableResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.UpdateDataLakeTableShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.table_input):
            request.table_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_input, 'TableInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.table_input_shrink):
            body['TableInput'] = request.table_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataLakeTable',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.UpdateDataLakeTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_lake_table_with_options_async(
        self,
        tmp_req: dms_20250414_models.UpdateDataLakeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dms_20250414_models.UpdateDataLakeTableResponse:
        """
        @summary 更新湖仓表信息
        
        @param tmp_req: UpdateDataLakeTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDataLakeTableResponse
        """
        UtilClient.validate_model(tmp_req)
        request = dms_20250414_models.UpdateDataLakeTableShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.table_input):
            request.table_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_input, 'TableInput', 'json')
        query = {}
        if not UtilClient.is_unset(request.catalog_name):
            query['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        if not UtilClient.is_unset(request.tid):
            query['Tid'] = request.tid
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.table_input_shrink):
            body['TableInput'] = request.table_input_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataLakeTable',
            version='2025-04-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dms_20250414_models.UpdateDataLakeTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_lake_table(
        self,
        request: dms_20250414_models.UpdateDataLakeTableRequest,
    ) -> dms_20250414_models.UpdateDataLakeTableResponse:
        """
        @summary 更新湖仓表信息
        
        @param request: UpdateDataLakeTableRequest
        @return: UpdateDataLakeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_data_lake_table_with_options(request, runtime)

    async def update_data_lake_table_async(
        self,
        request: dms_20250414_models.UpdateDataLakeTableRequest,
    ) -> dms_20250414_models.UpdateDataLakeTableResponse:
        """
        @summary 更新湖仓表信息
        
        @param request: UpdateDataLakeTableRequest
        @return: UpdateDataLakeTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_data_lake_table_with_options_async(request, runtime)
