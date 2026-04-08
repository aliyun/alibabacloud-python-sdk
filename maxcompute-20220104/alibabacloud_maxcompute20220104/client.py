# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_maxcompute20220104 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
            'ap-northeast-1': 'maxcompute.aliyuncs.com',
            'ap-northeast-2-pop': 'maxcompute.aliyuncs.com',
            'ap-south-1': 'maxcompute.aliyuncs.com',
            'ap-southeast-1': 'maxcompute.aliyuncs.com',
            'ap-southeast-2': 'maxcompute.aliyuncs.com',
            'ap-southeast-3': 'maxcompute.aliyuncs.com',
            'ap-southeast-5': 'maxcompute.aliyuncs.com',
            'cn-beijing': 'maxcompute.aliyuncs.com',
            'cn-beijing-finance-1': 'maxcompute.aliyuncs.com',
            'cn-beijing-finance-pop': 'maxcompute.aliyuncs.com',
            'cn-beijing-gov-1': 'maxcompute.aliyuncs.com',
            'cn-beijing-nu16-b01': 'maxcompute.aliyuncs.com',
            'cn-chengdu': 'maxcompute.aliyuncs.com',
            'cn-edge-1': 'maxcompute.aliyuncs.com',
            'cn-fujian': 'maxcompute.aliyuncs.com',
            'cn-haidian-cm12-c01': 'maxcompute.aliyuncs.com',
            'cn-hangzhou': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-finance': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'maxcompute.aliyuncs.com',
            'cn-hangzhou-test-306': 'maxcompute.aliyuncs.com',
            'cn-hongkong': 'maxcompute.aliyuncs.com',
            'cn-hongkong-finance-pop': 'maxcompute.aliyuncs.com',
            'cn-huhehaote': 'maxcompute.aliyuncs.com',
            'cn-north-2-gov-1': 'maxcompute.aliyuncs.com',
            'cn-qingdao': 'maxcompute.aliyuncs.com',
            'cn-qingdao-nebula': 'maxcompute.aliyuncs.com',
            'cn-shanghai': 'maxcompute.aliyuncs.com',
            'cn-shanghai-et15-b01': 'maxcompute.aliyuncs.com',
            'cn-shanghai-et2-b01': 'maxcompute.aliyuncs.com',
            'cn-shanghai-finance-1': 'maxcompute.aliyuncs.com',
            'cn-shanghai-inner': 'maxcompute.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'maxcompute.aliyuncs.com',
            'cn-shenzhen': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-finance-1': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-inner': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'maxcompute.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'maxcompute.aliyuncs.com',
            'cn-wuhan': 'maxcompute.aliyuncs.com',
            'cn-yushanfang': 'maxcompute.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'maxcompute.aliyuncs.com',
            'cn-zhangjiakou': 'maxcompute.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'maxcompute.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'maxcompute.aliyuncs.com',
            'eu-central-1': 'maxcompute.aliyuncs.com',
            'eu-west-1': 'maxcompute.aliyuncs.com',
            'eu-west-1-oxs': 'maxcompute.aliyuncs.com',
            'me-east-1': 'maxcompute.aliyuncs.com',
            'rus-west-1-pop': 'maxcompute.aliyuncs.com',
            'us-east-1': 'maxcompute.aliyuncs.com',
            'us-west-1': 'maxcompute.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('maxcompute', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_compute_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyComputeQuotaPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ApplyComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan/{DaraURL.percent_encode(plan_name)}/apply',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ApplyComputeQuotaPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ApplyComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan/{DaraURL.percent_encode(plan_name)}/apply',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_compute_quota_plan(
        self,
        nickname: str,
        plan_name: str,
    ) -> main_models.ApplyComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.apply_compute_quota_plan_with_options(nickname, plan_name, headers, runtime)

    async def apply_compute_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
    ) -> main_models.ApplyComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.apply_compute_quota_plan_with_options_async(nickname, plan_name, headers, runtime)

    def create_compute_quota_plan_with_options(
        self,
        nickname: str,
        request: main_models.CreateComputeQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeQuotaPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        request: main_models.CreateComputeQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComputeQuotaPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compute_quota_plan(
        self,
        nickname: str,
        request: main_models.CreateComputeQuotaPlanRequest,
    ) -> main_models.CreateComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_compute_quota_plan_with_options(nickname, request, headers, runtime)

    async def create_compute_quota_plan_async(
        self,
        nickname: str,
        request: main_models.CreateComputeQuotaPlanRequest,
    ) -> main_models.CreateComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_compute_quota_plan_with_options_async(nickname, request, headers, runtime)

    def create_mms_data_source_with_options(
        self,
        request: main_models.CreateMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMmsDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.networklink):
            body['networklink'] = request.networklink
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMmsDataSource',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMmsDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mms_data_source_with_options_async(
        self,
        request: main_models.CreateMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMmsDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.networklink):
            body['networklink'] = request.networklink
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMmsDataSource',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMmsDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mms_data_source(
        self,
        request: main_models.CreateMmsDataSourceRequest,
    ) -> main_models.CreateMmsDataSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_mms_data_source_with_options(request, headers, runtime)

    async def create_mms_data_source_async(
        self,
        request: main_models.CreateMmsDataSourceRequest,
    ) -> main_models.CreateMmsDataSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_mms_data_source_with_options_async(request, headers, runtime)

    def create_mms_fetch_metadata_job_with_options(
        self,
        source_id: str,
        request: main_models.CreateMmsFetchMetadataJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMmsFetchMetadataJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.db_name):
            body['dbName'] = request.db_name
        if not DaraCore.is_null(request.table_names):
            body['tableNames'] = request.table_names
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMmsFetchMetadataJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/scans',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMmsFetchMetadataJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mms_fetch_metadata_job_with_options_async(
        self,
        source_id: str,
        request: main_models.CreateMmsFetchMetadataJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMmsFetchMetadataJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.db_name):
            body['dbName'] = request.db_name
        if not DaraCore.is_null(request.table_names):
            body['tableNames'] = request.table_names
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMmsFetchMetadataJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/scans',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMmsFetchMetadataJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mms_fetch_metadata_job(
        self,
        source_id: str,
        request: main_models.CreateMmsFetchMetadataJobRequest,
    ) -> main_models.CreateMmsFetchMetadataJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_mms_fetch_metadata_job_with_options(source_id, request, headers, runtime)

    async def create_mms_fetch_metadata_job_async(
        self,
        source_id: str,
        request: main_models.CreateMmsFetchMetadataJobRequest,
    ) -> main_models.CreateMmsFetchMetadataJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_mms_fetch_metadata_job_with_options_async(source_id, request, headers, runtime)

    def create_mms_job_with_options(
        self,
        source_id: str,
        request: main_models.CreateMmsJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMmsJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.column_mapping):
            body['columnMapping'] = request.column_mapping
        if not DaraCore.is_null(request.dst_db_name):
            body['dstDbName'] = request.dst_db_name
        if not DaraCore.is_null(request.dst_schema_name):
            body['dstSchemaName'] = request.dst_schema_name
        if not DaraCore.is_null(request.enable_data_migration):
            body['enableDataMigration'] = request.enable_data_migration
        if not DaraCore.is_null(request.enable_schema_migration):
            body['enableSchemaMigration'] = request.enable_schema_migration
        if not DaraCore.is_null(request.enable_verification):
            body['enableVerification'] = request.enable_verification
        if not DaraCore.is_null(request.eta):
            body['eta'] = request.eta
        if not DaraCore.is_null(request.increment):
            body['increment'] = request.increment
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.others):
            body['others'] = request.others
        if not DaraCore.is_null(request.partition_filters):
            body['partitionFilters'] = request.partition_filters
        if not DaraCore.is_null(request.partitions):
            body['partitions'] = request.partitions
        if not DaraCore.is_null(request.schema_only):
            body['schemaOnly'] = request.schema_only
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        if not DaraCore.is_null(request.source_name):
            body['sourceName'] = request.source_name
        if not DaraCore.is_null(request.src_db_name):
            body['srcDbName'] = request.src_db_name
        if not DaraCore.is_null(request.src_schema_name):
            body['srcSchemaName'] = request.src_schema_name
        if not DaraCore.is_null(request.table_black_list):
            body['tableBlackList'] = request.table_black_list
        if not DaraCore.is_null(request.table_mapping):
            body['tableMapping'] = request.table_mapping
        if not DaraCore.is_null(request.table_white_list):
            body['tableWhiteList'] = request.table_white_list
        if not DaraCore.is_null(request.tables):
            body['tables'] = request.tables
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mms_job_with_options_async(
        self,
        source_id: str,
        request: main_models.CreateMmsJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMmsJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.column_mapping):
            body['columnMapping'] = request.column_mapping
        if not DaraCore.is_null(request.dst_db_name):
            body['dstDbName'] = request.dst_db_name
        if not DaraCore.is_null(request.dst_schema_name):
            body['dstSchemaName'] = request.dst_schema_name
        if not DaraCore.is_null(request.enable_data_migration):
            body['enableDataMigration'] = request.enable_data_migration
        if not DaraCore.is_null(request.enable_schema_migration):
            body['enableSchemaMigration'] = request.enable_schema_migration
        if not DaraCore.is_null(request.enable_verification):
            body['enableVerification'] = request.enable_verification
        if not DaraCore.is_null(request.eta):
            body['eta'] = request.eta
        if not DaraCore.is_null(request.increment):
            body['increment'] = request.increment
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.others):
            body['others'] = request.others
        if not DaraCore.is_null(request.partition_filters):
            body['partitionFilters'] = request.partition_filters
        if not DaraCore.is_null(request.partitions):
            body['partitions'] = request.partitions
        if not DaraCore.is_null(request.schema_only):
            body['schemaOnly'] = request.schema_only
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        if not DaraCore.is_null(request.source_name):
            body['sourceName'] = request.source_name
        if not DaraCore.is_null(request.src_db_name):
            body['srcDbName'] = request.src_db_name
        if not DaraCore.is_null(request.src_schema_name):
            body['srcSchemaName'] = request.src_schema_name
        if not DaraCore.is_null(request.table_black_list):
            body['tableBlackList'] = request.table_black_list
        if not DaraCore.is_null(request.table_mapping):
            body['tableMapping'] = request.table_mapping
        if not DaraCore.is_null(request.table_white_list):
            body['tableWhiteList'] = request.table_white_list
        if not DaraCore.is_null(request.tables):
            body['tables'] = request.tables
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mms_job(
        self,
        source_id: str,
        request: main_models.CreateMmsJobRequest,
    ) -> main_models.CreateMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_mms_job_with_options(source_id, request, headers, runtime)

    async def create_mms_job_async(
        self,
        source_id: str,
        request: main_models.CreateMmsJobRequest,
    ) -> main_models.CreateMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_mms_job_with_options_async(source_id, request, headers, runtime)

    def create_mms_timer_with_options(
        self,
        source_id: str,
        request: main_models.CreateMmsTimerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMmsTimerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.column_mapping):
            body['columnMapping'] = request.column_mapping
        if not DaraCore.is_null(request.enable_data_migration):
            body['enableDataMigration'] = request.enable_data_migration
        if not DaraCore.is_null(request.enable_schema_migration):
            body['enableSchemaMigration'] = request.enable_schema_migration
        if not DaraCore.is_null(request.enable_verification):
            body['enableVerification'] = request.enable_verification
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.others):
            body['others'] = request.others
        if not DaraCore.is_null(request.partition_filters):
            body['partitionFilters'] = request.partition_filters
        if not DaraCore.is_null(request.partitions):
            body['partitions'] = request.partitions
        if not DaraCore.is_null(request.schedule_type):
            body['scheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        if not DaraCore.is_null(request.src_db_name):
            body['srcDbName'] = request.src_db_name
        if not DaraCore.is_null(request.table_black_list):
            body['tableBlackList'] = request.table_black_list
        if not DaraCore.is_null(request.table_mapping):
            body['tableMapping'] = request.table_mapping
        if not DaraCore.is_null(request.table_white_list):
            body['tableWhiteList'] = request.table_white_list
        if not DaraCore.is_null(request.tables):
            body['tables'] = request.tables
        if not DaraCore.is_null(request.value):
            body['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMmsTimer',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/timers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMmsTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mms_timer_with_options_async(
        self,
        source_id: str,
        request: main_models.CreateMmsTimerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMmsTimerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.column_mapping):
            body['columnMapping'] = request.column_mapping
        if not DaraCore.is_null(request.enable_data_migration):
            body['enableDataMigration'] = request.enable_data_migration
        if not DaraCore.is_null(request.enable_schema_migration):
            body['enableSchemaMigration'] = request.enable_schema_migration
        if not DaraCore.is_null(request.enable_verification):
            body['enableVerification'] = request.enable_verification
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.others):
            body['others'] = request.others
        if not DaraCore.is_null(request.partition_filters):
            body['partitionFilters'] = request.partition_filters
        if not DaraCore.is_null(request.partitions):
            body['partitions'] = request.partitions
        if not DaraCore.is_null(request.schedule_type):
            body['scheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.source_id):
            body['sourceId'] = request.source_id
        if not DaraCore.is_null(request.src_db_name):
            body['srcDbName'] = request.src_db_name
        if not DaraCore.is_null(request.table_black_list):
            body['tableBlackList'] = request.table_black_list
        if not DaraCore.is_null(request.table_mapping):
            body['tableMapping'] = request.table_mapping
        if not DaraCore.is_null(request.table_white_list):
            body['tableWhiteList'] = request.table_white_list
        if not DaraCore.is_null(request.tables):
            body['tables'] = request.tables
        if not DaraCore.is_null(request.value):
            body['value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMmsTimer',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/timers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMmsTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mms_timer(
        self,
        source_id: str,
        request: main_models.CreateMmsTimerRequest,
    ) -> main_models.CreateMmsTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_mms_timer_with_options(source_id, request, headers, runtime)

    async def create_mms_timer_async(
        self,
        source_id: str,
        request: main_models.CreateMmsTimerRequest,
    ) -> main_models.CreateMmsTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_mms_timer_with_options_async(source_id, request, headers, runtime)

    def create_package_with_options(
        self,
        project_name: str,
        request: main_models.CreatePackageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_install):
            query['isInstall'] = request.is_install
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreatePackage',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/packages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_package_with_options_async(
        self,
        project_name: str,
        request: main_models.CreatePackageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_install):
            query['isInstall'] = request.is_install
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreatePackage',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/packages',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_package(
        self,
        project_name: str,
        request: main_models.CreatePackageRequest,
    ) -> main_models.CreatePackageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_package_with_options(project_name, request, headers, runtime)

    async def create_package_async(
        self,
        project_name: str,
        request: main_models.CreatePackageRequest,
    ) -> main_models.CreatePackageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_package_with_options_async(project_name, request, headers, runtime)

    def create_project_with_options(
        self,
        request: main_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: main_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_quota_with_options(
        self,
        request: main_models.CreateQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.commodity_code):
            query['commodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.commodity_data):
            query['commodityData'] = request.commodity_data
        if not DaraCore.is_null(request.part_nick_name):
            query['partNickName'] = request.part_nick_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQuota',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_with_options_async(
        self,
        request: main_models.CreateQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.commodity_code):
            query['commodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.commodity_data):
            query['commodityData'] = request.commodity_data
        if not DaraCore.is_null(request.part_nick_name):
            query['partNickName'] = request.part_nick_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQuota',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota(
        self,
        request: main_models.CreateQuotaRequest,
    ) -> main_models.CreateQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_quota_with_options(request, headers, runtime)

    async def create_quota_async(
        self,
        request: main_models.CreateQuotaRequest,
    ) -> main_models.CreateQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_quota_with_options_async(request, headers, runtime)

    def create_quota_plan_with_options(
        self,
        nickname: str,
        request: main_models.CreateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/plans',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quota_plan_with_options_async(
        self,
        nickname: str,
        request: main_models.CreateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateQuotaPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/plans',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quota_plan(
        self,
        nickname: str,
        request: main_models.CreateQuotaPlanRequest,
    ) -> main_models.CreateQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_quota_plan_with_options(nickname, request, headers, runtime)

    async def create_quota_plan_async(
        self,
        nickname: str,
        request: main_models.CreateQuotaPlanRequest,
    ) -> main_models.CreateQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_quota_plan_with_options_async(nickname, request, headers, runtime)

    def create_role_with_options(
        self,
        project_name: str,
        request: main_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        project_name: str,
        request: main_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        project_name: str,
        request: main_models.CreateRoleRequest,
    ) -> main_models.CreateRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_role_with_options(project_name, request, headers, runtime)

    async def create_role_async(
        self,
        project_name: str,
        request: main_models.CreateRoleRequest,
    ) -> main_models.CreateRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_role_with_options_async(project_name, request, headers, runtime)

    def delete_compute_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComputeQuotaPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan/{DaraURL.percent_encode(plan_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComputeQuotaPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan/{DaraURL.percent_encode(plan_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_compute_quota_plan(
        self,
        nickname: str,
        plan_name: str,
    ) -> main_models.DeleteComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_compute_quota_plan_with_options(nickname, plan_name, headers, runtime)

    async def delete_compute_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
    ) -> main_models.DeleteComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_compute_quota_plan_with_options_async(nickname, plan_name, headers, runtime)

    def delete_mms_data_source_with_options(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMmsDataSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMmsDataSource',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMmsDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mms_data_source_with_options_async(
        self,
        source_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMmsDataSourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMmsDataSource',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMmsDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mms_data_source(
        self,
        source_id: str,
    ) -> main_models.DeleteMmsDataSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_mms_data_source_with_options(source_id, headers, runtime)

    async def delete_mms_data_source_async(
        self,
        source_id: str,
    ) -> main_models.DeleteMmsDataSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_mms_data_source_with_options_async(source_id, headers, runtime)

    def delete_mms_job_with_options(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMmsJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mms_job_with_options_async(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMmsJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mms_job(
        self,
        source_id: str,
        job_id: str,
    ) -> main_models.DeleteMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_mms_job_with_options(source_id, job_id, headers, runtime)

    async def delete_mms_job_async(
        self,
        source_id: str,
        job_id: str,
    ) -> main_models.DeleteMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_mms_job_with_options_async(source_id, job_id, headers, runtime)

    def delete_mms_timer_with_options(
        self,
        source_id: str,
        timer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMmsTimerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMmsTimer',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/timers/{DaraURL.percent_encode(timer_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMmsTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mms_timer_with_options_async(
        self,
        source_id: str,
        timer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMmsTimerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMmsTimer',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/timers/{DaraURL.percent_encode(timer_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMmsTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mms_timer(
        self,
        source_id: str,
        timer_id: str,
    ) -> main_models.DeleteMmsTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_mms_timer_with_options(source_id, timer_id, headers, runtime)

    async def delete_mms_timer_async(
        self,
        source_id: str,
        timer_id: str,
    ) -> main_models.DeleteMmsTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_mms_timer_with_options_async(source_id, timer_id, headers, runtime)

    def delete_project_with_options(
        self,
        project_name: str,
        request: main_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_logical):
            query['isLogical'] = request.is_logical
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        project_name: str,
        request: main_models.DeleteProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_logical):
            query['isLogical'] = request.is_logical
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        project_name: str,
        request: main_models.DeleteProjectRequest,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project_name, request, headers, runtime)

    async def delete_project_async(
        self,
        project_name: str,
        request: main_models.DeleteProjectRequest,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(project_name, request, headers, runtime)

    def delete_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.DeleteQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQuotaPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/plans/{DaraURL.percent_encode(plan_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.DeleteQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQuotaPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/plans/{DaraURL.percent_encode(plan_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quota_plan(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.DeleteQuotaPlanRequest,
    ) -> main_models.DeleteQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    async def delete_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.DeleteQuotaPlanRequest,
    ) -> main_models.DeleteQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_quota_plan_with_options_async(nickname, plan_name, request, headers, runtime)

    def get_compute_effective_plan_with_options(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeEffectivePlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetComputeEffectivePlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeEffectivePlan/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeEffectivePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compute_effective_plan_with_options_async(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeEffectivePlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetComputeEffectivePlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeEffectivePlan/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeEffectivePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compute_effective_plan(
        self,
        nickname: str,
    ) -> main_models.GetComputeEffectivePlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_compute_effective_plan_with_options(nickname, headers, runtime)

    async def get_compute_effective_plan_async(
        self,
        nickname: str,
    ) -> main_models.GetComputeEffectivePlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_compute_effective_plan_with_options_async(nickname, headers, runtime)

    def get_compute_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeQuotaPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan/{DaraURL.percent_encode(plan_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeQuotaPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan/{DaraURL.percent_encode(plan_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compute_quota_plan(
        self,
        nickname: str,
        plan_name: str,
    ) -> main_models.GetComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_compute_quota_plan_with_options(nickname, plan_name, headers, runtime)

    async def get_compute_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
    ) -> main_models.GetComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_compute_quota_plan_with_options_async(nickname, plan_name, headers, runtime)

    def get_compute_quota_schedule_with_options(
        self,
        nickname: str,
        request: main_models.GetComputeQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeQuotaScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComputeQuotaSchedule',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaSchedule',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_compute_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: main_models.GetComputeQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetComputeQuotaScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetComputeQuotaSchedule',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaSchedule',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComputeQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_compute_quota_schedule(
        self,
        nickname: str,
        request: main_models.GetComputeQuotaScheduleRequest,
    ) -> main_models.GetComputeQuotaScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_compute_quota_schedule_with_options(nickname, request, headers, runtime)

    async def get_compute_quota_schedule_async(
        self,
        nickname: str,
        request: main_models.GetComputeQuotaScheduleRequest,
    ) -> main_models.GetComputeQuotaScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_compute_quota_schedule_with_options_async(nickname, request, headers, runtime)

    def get_job_info_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetJobInfo',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(instance_id)}/info',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_info_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetJobInfo',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/{DaraURL.percent_encode(instance_id)}/info',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_info(
        self,
        instance_id: str,
    ) -> main_models.GetJobInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_info_with_options(instance_id, headers, runtime)

    async def get_job_info_async(
        self,
        instance_id: str,
    ) -> main_models.GetJobInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_info_with_options_async(instance_id, headers, runtime)

    def get_job_resource_usage_with_options(
        self,
        tmp_req: main_models.GetJobResourceUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResourceUsageResponse:
        tmp_req.validate()
        request = main_models.GetJobResourceUsageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_owner_list):
            request.job_owner_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not DaraCore.is_null(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobResourceUsage',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/resourceUsage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_resource_usage_with_options_async(
        self,
        tmp_req: main_models.GetJobResourceUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResourceUsageResponse:
        tmp_req.validate()
        request = main_models.GetJobResourceUsageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_owner_list):
            request.job_owner_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not DaraCore.is_null(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobResourceUsage',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/resourceUsage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_resource_usage(
        self,
        request: main_models.GetJobResourceUsageRequest,
    ) -> main_models.GetJobResourceUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_resource_usage_with_options(request, headers, runtime)

    async def get_job_resource_usage_async(
        self,
        request: main_models.GetJobResourceUsageRequest,
    ) -> main_models.GetJobResourceUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_resource_usage_with_options_async(request, headers, runtime)

    def get_mms_async_task_with_options(
        self,
        source_id: str,
        async_task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsAsyncTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsAsyncTask',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/asyncTasks/{DaraURL.percent_encode(async_task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsAsyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_async_task_with_options_async(
        self,
        source_id: str,
        async_task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsAsyncTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsAsyncTask',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/asyncTasks/{DaraURL.percent_encode(async_task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsAsyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_async_task(
        self,
        source_id: str,
        async_task_id: str,
    ) -> main_models.GetMmsAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mms_async_task_with_options(source_id, async_task_id, headers, runtime)

    async def get_mms_async_task_async(
        self,
        source_id: str,
        async_task_id: str,
    ) -> main_models.GetMmsAsyncTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mms_async_task_with_options_async(source_id, async_task_id, headers, runtime)

    def get_mms_data_source_with_options(
        self,
        source_id: str,
        request: main_models.GetMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        if not DaraCore.is_null(request.with_config):
            query['withConfig'] = request.with_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMmsDataSource',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_data_source_with_options_async(
        self,
        source_id: str,
        request: main_models.GetMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        if not DaraCore.is_null(request.with_config):
            query['withConfig'] = request.with_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMmsDataSource',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_data_source(
        self,
        source_id: str,
        request: main_models.GetMmsDataSourceRequest,
    ) -> main_models.GetMmsDataSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mms_data_source_with_options(source_id, request, headers, runtime)

    async def get_mms_data_source_async(
        self,
        source_id: str,
        request: main_models.GetMmsDataSourceRequest,
    ) -> main_models.GetMmsDataSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mms_data_source_with_options_async(source_id, request, headers, runtime)

    def get_mms_db_with_options(
        self,
        source_id: str,
        db_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsDbResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsDb',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/dbs/{DaraURL.percent_encode(db_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_db_with_options_async(
        self,
        source_id: str,
        db_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsDbResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsDb',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/dbs/{DaraURL.percent_encode(db_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_db(
        self,
        source_id: str,
        db_id: str,
    ) -> main_models.GetMmsDbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mms_db_with_options(source_id, db_id, headers, runtime)

    async def get_mms_db_async(
        self,
        source_id: str,
        db_id: str,
    ) -> main_models.GetMmsDbResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mms_db_with_options_async(source_id, db_id, headers, runtime)

    def get_mms_fetch_metadata_job_with_options(
        self,
        source_id: str,
        scan_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsFetchMetadataJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsFetchMetadataJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/scans/{DaraURL.percent_encode(scan_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsFetchMetadataJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_fetch_metadata_job_with_options_async(
        self,
        source_id: str,
        scan_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsFetchMetadataJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsFetchMetadataJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/scans/{DaraURL.percent_encode(scan_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsFetchMetadataJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_fetch_metadata_job(
        self,
        source_id: str,
        scan_id: str,
    ) -> main_models.GetMmsFetchMetadataJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mms_fetch_metadata_job_with_options(source_id, scan_id, headers, runtime)

    async def get_mms_fetch_metadata_job_async(
        self,
        source_id: str,
        scan_id: str,
    ) -> main_models.GetMmsFetchMetadataJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mms_fetch_metadata_job_with_options_async(source_id, scan_id, headers, runtime)

    def get_mms_job_with_options(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_job_with_options_async(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_job(
        self,
        source_id: str,
        job_id: str,
    ) -> main_models.GetMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mms_job_with_options(source_id, job_id, headers, runtime)

    async def get_mms_job_async(
        self,
        source_id: str,
        job_id: str,
    ) -> main_models.GetMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mms_job_with_options_async(source_id, job_id, headers, runtime)

    def get_mms_partition_with_options(
        self,
        source_id: str,
        partition_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsPartitionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsPartition',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/partitions/{DaraURL.percent_encode(partition_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsPartitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_partition_with_options_async(
        self,
        source_id: str,
        partition_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsPartitionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsPartition',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/partitions/{DaraURL.percent_encode(partition_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsPartitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_partition(
        self,
        source_id: str,
        partition_id: str,
    ) -> main_models.GetMmsPartitionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mms_partition_with_options(source_id, partition_id, headers, runtime)

    async def get_mms_partition_async(
        self,
        source_id: str,
        partition_id: str,
    ) -> main_models.GetMmsPartitionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mms_partition_with_options_async(source_id, partition_id, headers, runtime)

    def get_mms_table_with_options(
        self,
        source_id: str,
        table_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsTable',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/tables/{DaraURL.percent_encode(table_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_table_with_options_async(
        self,
        source_id: str,
        table_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsTable',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/tables/{DaraURL.percent_encode(table_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_table(
        self,
        source_id: str,
        table_id: str,
    ) -> main_models.GetMmsTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mms_table_with_options(source_id, table_id, headers, runtime)

    async def get_mms_table_async(
        self,
        source_id: str,
        table_id: str,
    ) -> main_models.GetMmsTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mms_table_with_options_async(source_id, table_id, headers, runtime)

    def get_mms_task_with_options(
        self,
        source_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsTask',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_task_with_options_async(
        self,
        source_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsTask',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_task(
        self,
        source_id: str,
        task_id: str,
    ) -> main_models.GetMmsTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mms_task_with_options(source_id, task_id, headers, runtime)

    async def get_mms_task_async(
        self,
        source_id: str,
        task_id: str,
    ) -> main_models.GetMmsTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mms_task_with_options_async(source_id, task_id, headers, runtime)

    def get_mms_timer_with_options(
        self,
        source_id: str,
        timer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsTimerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsTimer',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/timers/{DaraURL.percent_encode(timer_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mms_timer_with_options_async(
        self,
        source_id: str,
        timer_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMmsTimerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMmsTimer',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/timers/{DaraURL.percent_encode(timer_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMmsTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mms_timer(
        self,
        source_id: str,
        timer_id: str,
    ) -> main_models.GetMmsTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_mms_timer_with_options(source_id, timer_id, headers, runtime)

    async def get_mms_timer_async(
        self,
        source_id: str,
        timer_id: str,
    ) -> main_models.GetMmsTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_mms_timer_with_options_async(source_id, timer_id, headers, runtime)

    def get_package_with_options(
        self,
        project_name: str,
        package_name: str,
        request: main_models.GetPackageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.source_project):
            query['sourceProject'] = request.source_project
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPackage',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/packages/{DaraURL.percent_encode(package_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_package_with_options_async(
        self,
        project_name: str,
        package_name: str,
        request: main_models.GetPackageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.source_project):
            query['sourceProject'] = request.source_project
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPackage',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/packages/{DaraURL.percent_encode(package_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_package(
        self,
        project_name: str,
        package_name: str,
        request: main_models.GetPackageRequest,
    ) -> main_models.GetPackageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_package_with_options(project_name, package_name, request, headers, runtime)

    async def get_package_async(
        self,
        project_name: str,
        package_name: str,
        request: main_models.GetPackageRequest,
    ) -> main_models.GetPackageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_package_with_options_async(project_name, package_name, request, headers, runtime)

    def get_project_with_options(
        self,
        project_name: str,
        request: main_models.GetProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['verbose'] = request.verbose
        if not DaraCore.is_null(request.with_quota_product_type):
            query['withQuotaProductType'] = request.with_quota_product_type
        if not DaraCore.is_null(request.with_storage_tier_info):
            query['withStorageTierInfo'] = request.with_storage_tier_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        project_name: str,
        request: main_models.GetProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['verbose'] = request.verbose
        if not DaraCore.is_null(request.with_quota_product_type):
            query['withQuotaProductType'] = request.with_quota_product_type
        if not DaraCore.is_null(request.with_storage_tier_info):
            query['withStorageTierInfo'] = request.with_storage_tier_info
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        project_name: str,
        request: main_models.GetProjectRequest,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project_name, request, headers, runtime)

    async def get_project_async(
        self,
        project_name: str,
        request: main_models.GetProjectRequest,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project_name, request, headers, runtime)

    def get_quota_with_options(
        self,
        nickname: str,
        request: main_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not DaraCore.is_null(request.mock):
            query['mock'] = request.mock
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuota',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_with_options_async(
        self,
        nickname: str,
        request: main_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not DaraCore.is_null(request.mock):
            query['mock'] = request.mock
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuota',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota(
        self,
        nickname: str,
        request: main_models.GetQuotaRequest,
    ) -> main_models.GetQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_quota_with_options(nickname, request, headers, runtime)

    async def get_quota_async(
        self,
        nickname: str,
        request: main_models.GetQuotaRequest,
    ) -> main_models.GetQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_quota_with_options_async(nickname, request, headers, runtime)

    def get_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.GetQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/plans/{DaraURL.percent_encode(plan_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.GetQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/plans/{DaraURL.percent_encode(plan_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_plan(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.GetQuotaPlanRequest,
    ) -> main_models.GetQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    async def get_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.GetQuotaPlanRequest,
    ) -> main_models.GetQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_quota_plan_with_options_async(nickname, plan_name, request, headers, runtime)

    def get_quota_schedule_with_options(
        self,
        nickname: str,
        request: main_models.GetQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaSchedule',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/schedule',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: main_models.GetQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.display_timezone):
            query['displayTimezone'] = request.display_timezone
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaSchedule',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/schedule',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_schedule(
        self,
        nickname: str,
        request: main_models.GetQuotaScheduleRequest,
    ) -> main_models.GetQuotaScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_quota_schedule_with_options(nickname, request, headers, runtime)

    async def get_quota_schedule_async(
        self,
        nickname: str,
        request: main_models.GetQuotaScheduleRequest,
    ) -> main_models.GetQuotaScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_quota_schedule_with_options_async(nickname, request, headers, runtime)

    def get_quota_usage_with_options(
        self,
        nickname: str,
        tmp_req: main_models.GetQuotaUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaUsageResponse:
        tmp_req.validate()
        request = main_models.GetQuotaUsageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.plot_types):
            request.plot_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.plot_types, 'plotTypes', 'simple')
        if not DaraCore.is_null(tmp_req.y_axis_types):
            request.y_axis_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.y_axis_types, 'yAxisTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.agg_method):
            query['aggMethod'] = request.agg_method
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.plot_types_shrink):
            query['plotTypes'] = request.plot_types_shrink
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.sub_quota_nickname):
            query['subQuotaNickname'] = request.sub_quota_nickname
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        if not DaraCore.is_null(request.y_axis_types_shrink):
            query['yAxisTypes'] = request.y_axis_types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaUsage',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/usage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_usage_with_options_async(
        self,
        nickname: str,
        tmp_req: main_models.GetQuotaUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaUsageResponse:
        tmp_req.validate()
        request = main_models.GetQuotaUsageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.plot_types):
            request.plot_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.plot_types, 'plotTypes', 'simple')
        if not DaraCore.is_null(tmp_req.y_axis_types):
            request.y_axis_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.y_axis_types, 'yAxisTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.agg_method):
            query['aggMethod'] = request.agg_method
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.plot_types_shrink):
            query['plotTypes'] = request.plot_types_shrink
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.sub_quota_nickname):
            query['subQuotaNickname'] = request.sub_quota_nickname
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        if not DaraCore.is_null(request.y_axis_types_shrink):
            query['yAxisTypes'] = request.y_axis_types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuotaUsage',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/usage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota_usage(
        self,
        nickname: str,
        request: main_models.GetQuotaUsageRequest,
    ) -> main_models.GetQuotaUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_quota_usage_with_options(nickname, request, headers, runtime)

    async def get_quota_usage_async(
        self,
        nickname: str,
        request: main_models.GetQuotaUsageRequest,
    ) -> main_models.GetQuotaUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_quota_usage_with_options_async(nickname, request, headers, runtime)

    def get_role_acl_with_options(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleAclResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRoleAcl',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles/{DaraURL.percent_encode(role_name)}/roleAcl',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRoleAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_acl_with_options_async(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleAclResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRoleAcl',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles/{DaraURL.percent_encode(role_name)}/roleAcl',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRoleAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role_acl(
        self,
        project_name: str,
        role_name: str,
    ) -> main_models.GetRoleAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_role_acl_with_options(project_name, role_name, headers, runtime)

    async def get_role_acl_async(
        self,
        project_name: str,
        role_name: str,
    ) -> main_models.GetRoleAclResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_role_acl_with_options_async(project_name, role_name, headers, runtime)

    def get_role_acl_on_object_with_options(
        self,
        project_name: str,
        role_name: str,
        request: main_models.GetRoleAclOnObjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleAclOnObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.object_name):
            query['objectName'] = request.object_name
        if not DaraCore.is_null(request.object_type):
            query['objectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRoleAclOnObject',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles/{DaraURL.percent_encode(role_name)}/acl',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRoleAclOnObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_acl_on_object_with_options_async(
        self,
        project_name: str,
        role_name: str,
        request: main_models.GetRoleAclOnObjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleAclOnObjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.object_name):
            query['objectName'] = request.object_name
        if not DaraCore.is_null(request.object_type):
            query['objectType'] = request.object_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRoleAclOnObject',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles/{DaraURL.percent_encode(role_name)}/acl',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRoleAclOnObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role_acl_on_object(
        self,
        project_name: str,
        role_name: str,
        request: main_models.GetRoleAclOnObjectRequest,
    ) -> main_models.GetRoleAclOnObjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_role_acl_on_object_with_options(project_name, role_name, request, headers, runtime)

    async def get_role_acl_on_object_async(
        self,
        project_name: str,
        role_name: str,
        request: main_models.GetRoleAclOnObjectRequest,
    ) -> main_models.GetRoleAclOnObjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_role_acl_on_object_with_options_async(project_name, role_name, request, headers, runtime)

    def get_role_policy_with_options(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRolePolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRolePolicy',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles/{DaraURL.percent_encode(role_name)}/policy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRolePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_policy_with_options_async(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRolePolicyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRolePolicy',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles/{DaraURL.percent_encode(role_name)}/policy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRolePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role_policy(
        self,
        project_name: str,
        role_name: str,
    ) -> main_models.GetRolePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_role_policy_with_options(project_name, role_name, headers, runtime)

    async def get_role_policy_async(
        self,
        project_name: str,
        role_name: str,
    ) -> main_models.GetRolePolicyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_role_policy_with_options_async(project_name, role_name, headers, runtime)

    def get_running_jobs_with_options(
        self,
        tmp_req: main_models.GetRunningJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRunningJobsResponse:
        tmp_req.validate()
        request = main_models.GetRunningJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_owner_list):
            request.job_owner_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not DaraCore.is_null(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRunningJobs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/runningJobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRunningJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_running_jobs_with_options_async(
        self,
        tmp_req: main_models.GetRunningJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRunningJobsResponse:
        tmp_req.validate()
        request = main_models.GetRunningJobsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.job_owner_list):
            request.job_owner_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.job_owner_list, 'jobOwnerList', 'simple')
        if not DaraCore.is_null(tmp_req.quota_nickname_list):
            request.quota_nickname_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.quota_nickname_list, 'quotaNicknameList', 'simple')
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.job_owner_list_shrink):
            query['jobOwnerList'] = request.job_owner_list_shrink
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.quota_nickname_list_shrink):
            query['quotaNicknameList'] = request.quota_nickname_list_shrink
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRunningJobs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/runningJobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRunningJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_running_jobs(
        self,
        request: main_models.GetRunningJobsRequest,
    ) -> main_models.GetRunningJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_running_jobs_with_options(request, headers, runtime)

    async def get_running_jobs_async(
        self,
        request: main_models.GetRunningJobsRequest,
    ) -> main_models.GetRunningJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_running_jobs_with_options_async(request, headers, runtime)

    def get_storage_amount_summary_with_options(
        self,
        request: main_models.GetStorageAmountSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageAmountSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStorageAmountSummary',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/amount',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageAmountSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_amount_summary_with_options_async(
        self,
        request: main_models.GetStorageAmountSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageAmountSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStorageAmountSummary',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/amount',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageAmountSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage_amount_summary(
        self,
        request: main_models.GetStorageAmountSummaryRequest,
    ) -> main_models.GetStorageAmountSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_storage_amount_summary_with_options(request, headers, runtime)

    async def get_storage_amount_summary_async(
        self,
        request: main_models.GetStorageAmountSummaryRequest,
    ) -> main_models.GetStorageAmountSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_storage_amount_summary_with_options_async(request, headers, runtime)

    def get_storage_size_summary_with_options(
        self,
        request: main_models.GetStorageSizeSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageSizeSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStorageSizeSummary',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/size',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageSizeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_size_summary_with_options_async(
        self,
        request: main_models.GetStorageSizeSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageSizeSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStorageSizeSummary',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/size',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageSizeSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage_size_summary(
        self,
        request: main_models.GetStorageSizeSummaryRequest,
    ) -> main_models.GetStorageSizeSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_storage_size_summary_with_options(request, headers, runtime)

    async def get_storage_size_summary_async(
        self,
        request: main_models.GetStorageSizeSummaryRequest,
    ) -> main_models.GetStorageSizeSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_storage_size_summary_with_options_async(request, headers, runtime)

    def get_storage_summary_compared_with_options(
        self,
        type: str,
        tmp_req: main_models.GetStorageSummaryComparedRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageSummaryComparedResponse:
        tmp_req.validate()
        request = main_models.GetStorageSummaryComparedShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.projects):
            request.projects_shrink = Utils.array_to_string_with_specified_style(tmp_req.projects, 'projects', 'simple')
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['beginDate'] = request.begin_date
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.projects_shrink):
            query['projects'] = request.projects_shrink
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStorageSummaryCompared',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/{DaraURL.percent_encode(type)}/compared',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageSummaryComparedResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_summary_compared_with_options_async(
        self,
        type: str,
        tmp_req: main_models.GetStorageSummaryComparedRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageSummaryComparedResponse:
        tmp_req.validate()
        request = main_models.GetStorageSummaryComparedShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.projects):
            request.projects_shrink = Utils.array_to_string_with_specified_style(tmp_req.projects, 'projects', 'simple')
        query = {}
        if not DaraCore.is_null(request.begin_date):
            query['beginDate'] = request.begin_date
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.projects_shrink):
            query['projects'] = request.projects_shrink
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStorageSummaryCompared',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/{DaraURL.percent_encode(type)}/compared',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageSummaryComparedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage_summary_compared(
        self,
        type: str,
        request: main_models.GetStorageSummaryComparedRequest,
    ) -> main_models.GetStorageSummaryComparedResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_storage_summary_compared_with_options(type, request, headers, runtime)

    async def get_storage_summary_compared_async(
        self,
        type: str,
        request: main_models.GetStorageSummaryComparedRequest,
    ) -> main_models.GetStorageSummaryComparedResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_storage_summary_compared_with_options_async(type, request, headers, runtime)

    def get_table_info_with_options(
        self,
        project_name: str,
        table_name: str,
        request: main_models.GetTableInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.schema_name):
            query['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableInfo',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/tables/{DaraURL.percent_encode(table_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_info_with_options_async(
        self,
        project_name: str,
        table_name: str,
        request: main_models.GetTableInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.schema_name):
            query['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableInfo',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/tables/{DaraURL.percent_encode(table_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_info(
        self,
        project_name: str,
        table_name: str,
        request: main_models.GetTableInfoRequest,
    ) -> main_models.GetTableInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_table_info_with_options(project_name, table_name, request, headers, runtime)

    async def get_table_info_async(
        self,
        project_name: str,
        table_name: str,
        request: main_models.GetTableInfoRequest,
    ) -> main_models.GetTableInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_table_info_with_options_async(project_name, table_name, request, headers, runtime)

    def get_trusted_projects_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrustedProjectsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTrustedProjects',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/trustedProjects',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrustedProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trusted_projects_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTrustedProjectsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTrustedProjects',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/trustedProjects',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTrustedProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trusted_projects(
        self,
        project_name: str,
    ) -> main_models.GetTrustedProjectsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_trusted_projects_with_options(project_name, headers, runtime)

    async def get_trusted_projects_async(
        self,
        project_name: str,
    ) -> main_models.GetTrustedProjectsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_trusted_projects_with_options_async(project_name, headers, runtime)

    def kill_jobs_with_options(
        self,
        request: main_models.KillJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.KillJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'KillJobs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/kill',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_jobs_with_options_async(
        self,
        request: main_models.KillJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.KillJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'KillJobs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/kill',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_jobs(
        self,
        request: main_models.KillJobsRequest,
    ) -> main_models.KillJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.kill_jobs_with_options(request, headers, runtime)

    async def kill_jobs_async(
        self,
        request: main_models.KillJobsRequest,
    ) -> main_models.KillJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.kill_jobs_with_options_async(request, headers, runtime)

    def list_compute_metrics_by_instance_with_options(
        self,
        request: main_models.ListComputeMetricsByInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeMetricsByInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_date):
            body['endDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_owner):
            body['jobOwner'] = request.job_owner
        if not DaraCore.is_null(request.page_number):
            body['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_names):
            body['projectNames'] = request.project_names
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.signature):
            body['signature'] = request.signature
        if not DaraCore.is_null(request.spec_codes):
            body['specCodes'] = request.spec_codes
        if not DaraCore.is_null(request.start_date):
            body['startDate'] = request.start_date
        if not DaraCore.is_null(request.types):
            body['types'] = request.types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeMetricsByInstance',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/computeMetrics/listByInstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeMetricsByInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_metrics_by_instance_with_options_async(
        self,
        request: main_models.ListComputeMetricsByInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeMetricsByInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_date):
            body['endDate'] = request.end_date
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_owner):
            body['jobOwner'] = request.job_owner
        if not DaraCore.is_null(request.page_number):
            body['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_names):
            body['projectNames'] = request.project_names
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.signature):
            body['signature'] = request.signature
        if not DaraCore.is_null(request.spec_codes):
            body['specCodes'] = request.spec_codes
        if not DaraCore.is_null(request.start_date):
            body['startDate'] = request.start_date
        if not DaraCore.is_null(request.types):
            body['types'] = request.types
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListComputeMetricsByInstance',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/computeMetrics/listByInstance',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeMetricsByInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_metrics_by_instance(
        self,
        request: main_models.ListComputeMetricsByInstanceRequest,
    ) -> main_models.ListComputeMetricsByInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_compute_metrics_by_instance_with_options(request, headers, runtime)

    async def list_compute_metrics_by_instance_async(
        self,
        request: main_models.ListComputeMetricsByInstanceRequest,
    ) -> main_models.ListComputeMetricsByInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_compute_metrics_by_instance_with_options_async(request, headers, runtime)

    def list_compute_quota_plan_with_options(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeQuotaPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComputeQuotaPlanResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_compute_quota_plan(
        self,
        nickname: str,
    ) -> main_models.ListComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_compute_quota_plan_with_options(nickname, headers, runtime)

    async def list_compute_quota_plan_async(
        self,
        nickname: str,
    ) -> main_models.ListComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_compute_quota_plan_with_options_async(nickname, headers, runtime)

    def list_functions_with_options(
        self,
        project_name: str,
        request: main_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.max_item):
            query['maxItem'] = request.max_item
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.schema_name):
            query['schemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctions',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/functions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_functions_with_options_async(
        self,
        project_name: str,
        request: main_models.ListFunctionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListFunctionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.max_item):
            query['maxItem'] = request.max_item
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.schema_name):
            query['schemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListFunctions',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/functions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFunctionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_functions(
        self,
        project_name: str,
        request: main_models.ListFunctionsRequest,
    ) -> main_models.ListFunctionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_functions_with_options(project_name, request, headers, runtime)

    async def list_functions_async(
        self,
        project_name: str,
        request: main_models.ListFunctionsRequest,
    ) -> main_models.ListFunctionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_functions_with_options_async(project_name, request, headers, runtime)

    def list_job_infos_with_options(
        self,
        request: main_models.ListJobInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.order_column):
            query['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.ext_node_id_list):
            body['extNodeIdList'] = request.ext_node_id_list
        if not DaraCore.is_null(request.ext_node_name_list):
            body['extNodeNameList'] = request.ext_node_name_list
        if not DaraCore.is_null(request.from_):
            body['from'] = request.from_
        if not DaraCore.is_null(request.instance_id_list):
            body['instanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.job_owner_list):
            body['jobOwnerList'] = request.job_owner_list
        if not DaraCore.is_null(request.priority_list):
            body['priorityList'] = request.priority_list
        if not DaraCore.is_null(request.project_list):
            body['projectList'] = request.project_list
        if not DaraCore.is_null(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not DaraCore.is_null(request.scene_tag_list):
            body['sceneTagList'] = request.scene_tag_list
        if not DaraCore.is_null(request.signature_list):
            body['signatureList'] = request.signature_list
        if not DaraCore.is_null(request.sort_by_list):
            body['sortByList'] = request.sort_by_list
        if not DaraCore.is_null(request.sort_order_list):
            body['sortOrderList'] = request.sort_order_list
        if not DaraCore.is_null(request.status_list):
            body['statusList'] = request.status_list
        if not DaraCore.is_null(request.task_name_list):
            body['taskNameList'] = request.task_name_list
        if not DaraCore.is_null(request.to):
            body['to'] = request.to
        if not DaraCore.is_null(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListJobInfos',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_infos_with_options_async(
        self,
        request: main_models.ListJobInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.order_column):
            query['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.ext_node_id_list):
            body['extNodeIdList'] = request.ext_node_id_list
        if not DaraCore.is_null(request.ext_node_name_list):
            body['extNodeNameList'] = request.ext_node_name_list
        if not DaraCore.is_null(request.from_):
            body['from'] = request.from_
        if not DaraCore.is_null(request.instance_id_list):
            body['instanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.job_owner_list):
            body['jobOwnerList'] = request.job_owner_list
        if not DaraCore.is_null(request.priority_list):
            body['priorityList'] = request.priority_list
        if not DaraCore.is_null(request.project_list):
            body['projectList'] = request.project_list
        if not DaraCore.is_null(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not DaraCore.is_null(request.scene_tag_list):
            body['sceneTagList'] = request.scene_tag_list
        if not DaraCore.is_null(request.signature_list):
            body['signatureList'] = request.signature_list
        if not DaraCore.is_null(request.sort_by_list):
            body['sortByList'] = request.sort_by_list
        if not DaraCore.is_null(request.sort_order_list):
            body['sortOrderList'] = request.sort_order_list
        if not DaraCore.is_null(request.status_list):
            body['statusList'] = request.status_list
        if not DaraCore.is_null(request.task_name_list):
            body['taskNameList'] = request.task_name_list
        if not DaraCore.is_null(request.to):
            body['to'] = request.to
        if not DaraCore.is_null(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListJobInfos',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_infos(
        self,
        request: main_models.ListJobInfosRequest,
    ) -> main_models.ListJobInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_job_infos_with_options(request, headers, runtime)

    async def list_job_infos_async(
        self,
        request: main_models.ListJobInfosRequest,
    ) -> main_models.ListJobInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_job_infos_with_options_async(request, headers, runtime)

    def list_job_metric_with_options(
        self,
        request: main_models.ListJobMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not DaraCore.is_null(request.group):
            body['group'] = request.group
        if not DaraCore.is_null(request.metric):
            body['metric'] = request.metric
        if not DaraCore.is_null(request.period):
            body['period'] = request.period
        if not DaraCore.is_null(request.project):
            body['project'] = request.project
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListJobMetric',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/metric',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_metric_with_options_async(
        self,
        request: main_models.ListJobMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not DaraCore.is_null(request.group):
            body['group'] = request.group
        if not DaraCore.is_null(request.metric):
            body['metric'] = request.metric
        if not DaraCore.is_null(request.period):
            body['period'] = request.period
        if not DaraCore.is_null(request.project):
            body['project'] = request.project
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListJobMetric',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/metric',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_metric(
        self,
        request: main_models.ListJobMetricRequest,
    ) -> main_models.ListJobMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_job_metric_with_options(request, headers, runtime)

    async def list_job_metric_async(
        self,
        request: main_models.ListJobMetricRequest,
    ) -> main_models.ListJobMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_job_metric_with_options_async(request, headers, runtime)

    def list_job_snapshot_infos_with_options(
        self,
        request: main_models.ListJobSnapshotInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobSnapshotInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.order_column):
            query['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.ext_node_id_list):
            body['extNodeIdList'] = request.ext_node_id_list
        if not DaraCore.is_null(request.from_):
            body['from'] = request.from_
        if not DaraCore.is_null(request.instance_id_list):
            body['instanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.job_owner_list):
            body['jobOwnerList'] = request.job_owner_list
        if not DaraCore.is_null(request.priority_list):
            body['priorityList'] = request.priority_list
        if not DaraCore.is_null(request.project_list):
            body['projectList'] = request.project_list
        if not DaraCore.is_null(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not DaraCore.is_null(request.signature_list):
            body['signatureList'] = request.signature_list
        if not DaraCore.is_null(request.sort_by_list):
            body['sortByList'] = request.sort_by_list
        if not DaraCore.is_null(request.sort_order_list):
            body['sortOrderList'] = request.sort_order_list
        if not DaraCore.is_null(request.status_list):
            body['statusList'] = request.status_list
        if not DaraCore.is_null(request.to):
            body['to'] = request.to
        if not DaraCore.is_null(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListJobSnapshotInfos',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/snapshot',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobSnapshotInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_snapshot_infos_with_options_async(
        self,
        request: main_models.ListJobSnapshotInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobSnapshotInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.order_column):
            query['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        body = {}
        if not DaraCore.is_null(request.ext_node_id_list):
            body['extNodeIdList'] = request.ext_node_id_list
        if not DaraCore.is_null(request.from_):
            body['from'] = request.from_
        if not DaraCore.is_null(request.instance_id_list):
            body['instanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.job_owner_list):
            body['jobOwnerList'] = request.job_owner_list
        if not DaraCore.is_null(request.priority_list):
            body['priorityList'] = request.priority_list
        if not DaraCore.is_null(request.project_list):
            body['projectList'] = request.project_list
        if not DaraCore.is_null(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not DaraCore.is_null(request.signature_list):
            body['signatureList'] = request.signature_list
        if not DaraCore.is_null(request.sort_by_list):
            body['sortByList'] = request.sort_by_list
        if not DaraCore.is_null(request.sort_order_list):
            body['sortOrderList'] = request.sort_order_list
        if not DaraCore.is_null(request.status_list):
            body['statusList'] = request.status_list
        if not DaraCore.is_null(request.to):
            body['to'] = request.to
        if not DaraCore.is_null(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListJobSnapshotInfos',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobs/snapshot',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobSnapshotInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_snapshot_infos(
        self,
        request: main_models.ListJobSnapshotInfosRequest,
    ) -> main_models.ListJobSnapshotInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_job_snapshot_infos_with_options(request, headers, runtime)

    async def list_job_snapshot_infos_async(
        self,
        request: main_models.ListJobSnapshotInfosRequest,
    ) -> main_models.ListJobSnapshotInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_job_snapshot_infos_with_options_async(request, headers, runtime)

    def list_mms_data_source_config_items_with_options(
        self,
        request: main_models.ListMmsDataSourceConfigItemsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsDataSourceConfigItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsDataSourceConfigItems',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/configItems',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsDataSourceConfigItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_data_source_config_items_with_options_async(
        self,
        request: main_models.ListMmsDataSourceConfigItemsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsDataSourceConfigItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['lang'] = request.lang
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsDataSourceConfigItems',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/configItems',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsDataSourceConfigItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_data_source_config_items(
        self,
        request: main_models.ListMmsDataSourceConfigItemsRequest,
    ) -> main_models.ListMmsDataSourceConfigItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mms_data_source_config_items_with_options(request, headers, runtime)

    async def list_mms_data_source_config_items_async(
        self,
        request: main_models.ListMmsDataSourceConfigItemsRequest,
    ) -> main_models.ListMmsDataSourceConfigItemsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mms_data_source_config_items_with_options_async(request, headers, runtime)

    def list_mms_data_sources_with_options(
        self,
        request: main_models.ListMmsDataSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsDataSources',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_data_sources_with_options_async(
        self,
        request: main_models.ListMmsDataSourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsDataSources',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_data_sources(
        self,
        request: main_models.ListMmsDataSourcesRequest,
    ) -> main_models.ListMmsDataSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mms_data_sources_with_options(request, headers, runtime)

    async def list_mms_data_sources_async(
        self,
        request: main_models.ListMmsDataSourcesRequest,
    ) -> main_models.ListMmsDataSourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mms_data_sources_with_options_async(request, headers, runtime)

    def list_mms_dbs_with_options(
        self,
        source_id: str,
        tmp_req: main_models.ListMmsDbsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsDbsResponse:
        tmp_req.validate()
        request = main_models.ListMmsDbsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sorter):
            request.sorter_shrink = Utils.array_to_string_with_specified_style(tmp_req.sorter, 'sorter', 'json')
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sorter_shrink):
            query['sorter'] = request.sorter_shrink
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsDbs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/dbs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_dbs_with_options_async(
        self,
        source_id: str,
        tmp_req: main_models.ListMmsDbsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsDbsResponse:
        tmp_req.validate()
        request = main_models.ListMmsDbsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sorter):
            request.sorter_shrink = Utils.array_to_string_with_specified_style(tmp_req.sorter, 'sorter', 'json')
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.sorter_shrink):
            query['sorter'] = request.sorter_shrink
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsDbs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/dbs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_dbs(
        self,
        source_id: str,
        request: main_models.ListMmsDbsRequest,
    ) -> main_models.ListMmsDbsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mms_dbs_with_options(source_id, request, headers, runtime)

    async def list_mms_dbs_async(
        self,
        source_id: str,
        request: main_models.ListMmsDbsRequest,
    ) -> main_models.ListMmsDbsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mms_dbs_with_options_async(source_id, request, headers, runtime)

    def list_mms_jobs_with_options(
        self,
        source_id: str,
        request: main_models.ListMmsJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_db_name):
            query['dstDbName'] = request.dst_db_name
        if not DaraCore.is_null(request.dst_table_name):
            query['dstTableName'] = request.dst_table_name
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.src_db_name):
            query['srcDbName'] = request.src_db_name
        if not DaraCore.is_null(request.src_table_name):
            query['srcTableName'] = request.src_table_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.stopped):
            query['stopped'] = request.stopped
        if not DaraCore.is_null(request.timer_id):
            query['timerId'] = request.timer_id
        if not DaraCore.is_null(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsJobs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_jobs_with_options_async(
        self,
        source_id: str,
        request: main_models.ListMmsJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_db_name):
            query['dstDbName'] = request.dst_db_name
        if not DaraCore.is_null(request.dst_table_name):
            query['dstTableName'] = request.dst_table_name
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.src_db_name):
            query['srcDbName'] = request.src_db_name
        if not DaraCore.is_null(request.src_table_name):
            query['srcTableName'] = request.src_table_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.stopped):
            query['stopped'] = request.stopped
        if not DaraCore.is_null(request.timer_id):
            query['timerId'] = request.timer_id
        if not DaraCore.is_null(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsJobs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_jobs(
        self,
        source_id: str,
        request: main_models.ListMmsJobsRequest,
    ) -> main_models.ListMmsJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mms_jobs_with_options(source_id, request, headers, runtime)

    async def list_mms_jobs_async(
        self,
        source_id: str,
        request: main_models.ListMmsJobsRequest,
    ) -> main_models.ListMmsJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mms_jobs_with_options_async(source_id, request, headers, runtime)

    def list_mms_partitions_with_options(
        self,
        source_id: str,
        tmp_req: main_models.ListMmsPartitionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsPartitionsResponse:
        tmp_req.validate()
        request = main_models.ListMmsPartitionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status):
            request.status_shrink = Utils.array_to_string_with_specified_style(tmp_req.status, 'status', 'json')
        query = {}
        if not DaraCore.is_null(request.db_id):
            query['dbId'] = request.db_id
        if not DaraCore.is_null(request.db_name):
            query['dbName'] = request.db_name
        if not DaraCore.is_null(request.last_ddl_time_end):
            query['lastDdlTimeEnd'] = request.last_ddl_time_end
        if not DaraCore.is_null(request.last_ddl_time_start):
            query['lastDdlTimeStart'] = request.last_ddl_time_start
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status_shrink):
            query['status'] = request.status_shrink
        if not DaraCore.is_null(request.table_id):
            query['tableId'] = request.table_id
        if not DaraCore.is_null(request.table_name):
            query['tableName'] = request.table_name
        if not DaraCore.is_null(request.updated):
            query['updated'] = request.updated
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        if not DaraCore.is_null(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsPartitions',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/partitions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsPartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_partitions_with_options_async(
        self,
        source_id: str,
        tmp_req: main_models.ListMmsPartitionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsPartitionsResponse:
        tmp_req.validate()
        request = main_models.ListMmsPartitionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status):
            request.status_shrink = Utils.array_to_string_with_specified_style(tmp_req.status, 'status', 'json')
        query = {}
        if not DaraCore.is_null(request.db_id):
            query['dbId'] = request.db_id
        if not DaraCore.is_null(request.db_name):
            query['dbName'] = request.db_name
        if not DaraCore.is_null(request.last_ddl_time_end):
            query['lastDdlTimeEnd'] = request.last_ddl_time_end
        if not DaraCore.is_null(request.last_ddl_time_start):
            query['lastDdlTimeStart'] = request.last_ddl_time_start
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status_shrink):
            query['status'] = request.status_shrink
        if not DaraCore.is_null(request.table_id):
            query['tableId'] = request.table_id
        if not DaraCore.is_null(request.table_name):
            query['tableName'] = request.table_name
        if not DaraCore.is_null(request.updated):
            query['updated'] = request.updated
        if not DaraCore.is_null(request.value):
            query['value'] = request.value
        if not DaraCore.is_null(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsPartitions',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/partitions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsPartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_partitions(
        self,
        source_id: str,
        request: main_models.ListMmsPartitionsRequest,
    ) -> main_models.ListMmsPartitionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mms_partitions_with_options(source_id, request, headers, runtime)

    async def list_mms_partitions_async(
        self,
        source_id: str,
        request: main_models.ListMmsPartitionsRequest,
    ) -> main_models.ListMmsPartitionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mms_partitions_with_options_async(source_id, request, headers, runtime)

    def list_mms_tables_with_options(
        self,
        source_id: str,
        tmp_req: main_models.ListMmsTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsTablesResponse:
        tmp_req.validate()
        request = main_models.ListMmsTablesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status):
            request.status_shrink = Utils.array_to_string_with_specified_style(tmp_req.status, 'status', 'json')
        query = {}
        if not DaraCore.is_null(request.db_id):
            query['dbId'] = request.db_id
        if not DaraCore.is_null(request.db_name):
            query['dbName'] = request.db_name
        if not DaraCore.is_null(request.dst_name):
            query['dstName'] = request.dst_name
        if not DaraCore.is_null(request.dst_project_name):
            query['dstProjectName'] = request.dst_project_name
        if not DaraCore.is_null(request.dst_schema_name):
            query['dstSchemaName'] = request.dst_schema_name
        if not DaraCore.is_null(request.has_partitions):
            query['hasPartitions'] = request.has_partitions
        if not DaraCore.is_null(request.last_ddl_time_end):
            query['lastDdlTimeEnd'] = request.last_ddl_time_end
        if not DaraCore.is_null(request.last_ddl_time_start):
            query['lastDdlTimeStart'] = request.last_ddl_time_start
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.only_name):
            query['onlyName'] = request.only_name
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status_shrink):
            query['status'] = request.status_shrink
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsTables',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_tables_with_options_async(
        self,
        source_id: str,
        tmp_req: main_models.ListMmsTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsTablesResponse:
        tmp_req.validate()
        request = main_models.ListMmsTablesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status):
            request.status_shrink = Utils.array_to_string_with_specified_style(tmp_req.status, 'status', 'json')
        query = {}
        if not DaraCore.is_null(request.db_id):
            query['dbId'] = request.db_id
        if not DaraCore.is_null(request.db_name):
            query['dbName'] = request.db_name
        if not DaraCore.is_null(request.dst_name):
            query['dstName'] = request.dst_name
        if not DaraCore.is_null(request.dst_project_name):
            query['dstProjectName'] = request.dst_project_name
        if not DaraCore.is_null(request.dst_schema_name):
            query['dstSchemaName'] = request.dst_schema_name
        if not DaraCore.is_null(request.has_partitions):
            query['hasPartitions'] = request.has_partitions
        if not DaraCore.is_null(request.last_ddl_time_end):
            query['lastDdlTimeEnd'] = request.last_ddl_time_end
        if not DaraCore.is_null(request.last_ddl_time_start):
            query['lastDdlTimeStart'] = request.last_ddl_time_start
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.only_name):
            query['onlyName'] = request.only_name
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status_shrink):
            query['status'] = request.status_shrink
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsTables',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_tables(
        self,
        source_id: str,
        request: main_models.ListMmsTablesRequest,
    ) -> main_models.ListMmsTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mms_tables_with_options(source_id, request, headers, runtime)

    async def list_mms_tables_async(
        self,
        source_id: str,
        request: main_models.ListMmsTablesRequest,
    ) -> main_models.ListMmsTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mms_tables_with_options_async(source_id, request, headers, runtime)

    def list_mms_task_logs_with_options(
        self,
        source_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsTaskLogsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListMmsTaskLogs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/tasks/{DaraURL.percent_encode(task_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsTaskLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_task_logs_with_options_async(
        self,
        source_id: str,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsTaskLogsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListMmsTaskLogs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/tasks/{DaraURL.percent_encode(task_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsTaskLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_task_logs(
        self,
        source_id: str,
        task_id: str,
    ) -> main_models.ListMmsTaskLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mms_task_logs_with_options(source_id, task_id, headers, runtime)

    async def list_mms_task_logs_async(
        self,
        source_id: str,
        task_id: str,
    ) -> main_models.ListMmsTaskLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mms_task_logs_with_options_async(source_id, task_id, headers, runtime)

    def list_mms_tasks_with_options(
        self,
        source_id: str,
        request: main_models.ListMmsTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_db_name):
            query['dstDbName'] = request.dst_db_name
        if not DaraCore.is_null(request.dst_table_name):
            query['dstTableName'] = request.dst_table_name
        if not DaraCore.is_null(request.job_id):
            query['jobId'] = request.job_id
        if not DaraCore.is_null(request.job_name):
            query['jobName'] = request.job_name
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.partition):
            query['partition'] = request.partition
        if not DaraCore.is_null(request.src_db_name):
            query['srcDbName'] = request.src_db_name
        if not DaraCore.is_null(request.src_table_name):
            query['srcTableName'] = request.src_table_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsTasks',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_tasks_with_options_async(
        self,
        source_id: str,
        request: main_models.ListMmsTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_db_name):
            query['dstDbName'] = request.dst_db_name
        if not DaraCore.is_null(request.dst_table_name):
            query['dstTableName'] = request.dst_table_name
        if not DaraCore.is_null(request.job_id):
            query['jobId'] = request.job_id
        if not DaraCore.is_null(request.job_name):
            query['jobName'] = request.job_name
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.partition):
            query['partition'] = request.partition
        if not DaraCore.is_null(request.src_db_name):
            query['srcDbName'] = request.src_db_name
        if not DaraCore.is_null(request.src_table_name):
            query['srcTableName'] = request.src_table_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.sorter):
            query['sorter'] = request.sorter
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsTasks',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_tasks(
        self,
        source_id: str,
        request: main_models.ListMmsTasksRequest,
    ) -> main_models.ListMmsTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mms_tasks_with_options(source_id, request, headers, runtime)

    async def list_mms_tasks_async(
        self,
        source_id: str,
        request: main_models.ListMmsTasksRequest,
    ) -> main_models.ListMmsTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mms_tasks_with_options_async(source_id, request, headers, runtime)

    def list_mms_timer_logs_with_options(
        self,
        source_id: str,
        timer_id: str,
        request: main_models.ListMmsTimerLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsTimerLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsTimerLogs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/timers/{DaraURL.percent_encode(timer_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsTimerLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mms_timer_logs_with_options_async(
        self,
        source_id: str,
        timer_id: str,
        request: main_models.ListMmsTimerLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMmsTimerLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['pageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMmsTimerLogs',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/timers/{DaraURL.percent_encode(timer_id)}/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMmsTimerLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mms_timer_logs(
        self,
        source_id: str,
        timer_id: str,
        request: main_models.ListMmsTimerLogsRequest,
    ) -> main_models.ListMmsTimerLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mms_timer_logs_with_options(source_id, timer_id, request, headers, runtime)

    async def list_mms_timer_logs_async(
        self,
        source_id: str,
        timer_id: str,
        request: main_models.ListMmsTimerLogsRequest,
    ) -> main_models.ListMmsTimerLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mms_timer_logs_with_options_async(source_id, timer_id, request, headers, runtime)

    def list_packages_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPackagesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPackages',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/packages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_packages_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPackagesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPackages',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/packages',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_packages(
        self,
        project_name: str,
    ) -> main_models.ListPackagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_packages_with_options(project_name, headers, runtime)

    async def list_packages_async(
        self,
        project_name: str,
    ) -> main_models.ListPackagesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_packages_with_options_async(project_name, headers, runtime)

    def list_project_users_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectUsersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListProjectUsers',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_users_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectUsersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListProjectUsers',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_users(
        self,
        project_name: str,
    ) -> main_models.ListProjectUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_project_users_with_options(project_name, headers, runtime)

    async def list_project_users_async(
        self,
        project_name: str,
    ) -> main_models.ListProjectUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_project_users_with_options_async(project_name, headers, runtime)

    def list_projects_with_options(
        self,
        request: main_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.list_system_catalog):
            query['listSystemCatalog'] = request.list_system_catalog
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.max_item):
            query['maxItem'] = request.max_item
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.quota_name):
            query['quotaName'] = request.quota_name
        if not DaraCore.is_null(request.quota_nick_name):
            query['quotaNickName'] = request.quota_nick_name
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: main_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.list_system_catalog):
            query['listSystemCatalog'] = request.list_system_catalog
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.max_item):
            query['maxItem'] = request.max_item
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.quota_name):
            query['quotaName'] = request.quota_name
        if not DaraCore.is_null(request.quota_nick_name):
            query['quotaNickName'] = request.quota_nick_name
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(request, headers, runtime)

    async def list_projects_async(
        self,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(request, headers, runtime)

    def list_quotas_with_options(
        self,
        request: main_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_type):
            query['billingType'] = request.billing_type
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.max_item):
            query['maxItem'] = request.max_item
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotas',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_with_options_async(
        self,
        request: main_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_type):
            query['billingType'] = request.billing_type
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.max_item):
            query['maxItem'] = request.max_item
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.sale_tags):
            query['saleTags'] = request.sale_tags
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotas',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas(
        self,
        request: main_models.ListQuotasRequest,
    ) -> main_models.ListQuotasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    async def list_quotas_async(
        self,
        request: main_models.ListQuotasRequest,
    ) -> main_models.ListQuotasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_quotas_with_options_async(request, headers, runtime)

    def list_quotas_plans_with_options(
        self,
        nickname: str,
        request: main_models.ListQuotasPlansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotasPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotasPlans',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/plans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotasPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_plans_with_options_async(
        self,
        nickname: str,
        request: main_models.ListQuotasPlansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotasPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotasPlans',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/plans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotasPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas_plans(
        self,
        nickname: str,
        request: main_models.ListQuotasPlansRequest,
    ) -> main_models.ListQuotasPlansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_quotas_plans_with_options(nickname, request, headers, runtime)

    async def list_quotas_plans_async(
        self,
        nickname: str,
        request: main_models.ListQuotasPlansRequest,
    ) -> main_models.ListQuotasPlansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_quotas_plans_with_options_async(nickname, request, headers, runtime)

    def list_resources_with_options(
        self,
        project_name: str,
        request: main_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.max_item):
            query['maxItem'] = request.max_item
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.schema_name):
            query['schemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        project_name: str,
        request: main_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.max_item):
            query['maxItem'] = request.max_item
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.schema_name):
            query['schemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        project_name: str,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(project_name, request, headers, runtime)

    async def list_resources_async(
        self,
        project_name: str,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(project_name, request, headers, runtime)

    def list_roles_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        project_name: str,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_roles_with_options(project_name, headers, runtime)

    async def list_roles_async(
        self,
        project_name: str,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_roles_with_options_async(project_name, headers, runtime)

    def list_storage_partitions_info_with_options(
        self,
        project: str,
        table: str,
        tmp_req: main_models.ListStoragePartitionsInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStoragePartitionsInfoResponse:
        tmp_req.validate()
        request = main_models.ListStoragePartitionsInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'types', 'json')
        query = {}
        if not DaraCore.is_null(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.order_column):
            query['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.partition_prefix):
            query['partitionPrefix'] = request.partition_prefix
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.schema):
            query['schema'] = request.schema
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.types_shrink):
            query['types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStoragePartitionsInfo',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/projects/{DaraURL.percent_encode(project)}/tables/{DaraURL.percent_encode(table)}/partitionsInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStoragePartitionsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_storage_partitions_info_with_options_async(
        self,
        project: str,
        table: str,
        tmp_req: main_models.ListStoragePartitionsInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStoragePartitionsInfoResponse:
        tmp_req.validate()
        request = main_models.ListStoragePartitionsInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'types', 'json')
        query = {}
        if not DaraCore.is_null(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.order_column):
            query['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.partition_prefix):
            query['partitionPrefix'] = request.partition_prefix
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.schema):
            query['schema'] = request.schema
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.types_shrink):
            query['types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStoragePartitionsInfo',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/projects/{DaraURL.percent_encode(project)}/tables/{DaraURL.percent_encode(table)}/partitionsInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStoragePartitionsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_storage_partitions_info(
        self,
        project: str,
        table: str,
        request: main_models.ListStoragePartitionsInfoRequest,
    ) -> main_models.ListStoragePartitionsInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_storage_partitions_info_with_options(project, table, request, headers, runtime)

    async def list_storage_partitions_info_async(
        self,
        project: str,
        table: str,
        request: main_models.ListStoragePartitionsInfoRequest,
    ) -> main_models.ListStoragePartitionsInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_storage_partitions_info_with_options_async(project, table, request, headers, runtime)

    def list_storage_projects_info_with_options(
        self,
        request: main_models.ListStorageProjectsInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStorageProjectsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.order_column):
            query['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_prefix):
            query['projectPrefix'] = request.project_prefix
        if not DaraCore.is_null(request.recent_days):
            query['recentDays'] = request.recent_days
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStorageProjectsInfo',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/projectsInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStorageProjectsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_storage_projects_info_with_options_async(
        self,
        request: main_models.ListStorageProjectsInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStorageProjectsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.order_column):
            query['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_prefix):
            query['projectPrefix'] = request.project_prefix
        if not DaraCore.is_null(request.recent_days):
            query['recentDays'] = request.recent_days
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStorageProjectsInfo',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/projectsInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStorageProjectsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_storage_projects_info(
        self,
        request: main_models.ListStorageProjectsInfoRequest,
    ) -> main_models.ListStorageProjectsInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_storage_projects_info_with_options(request, headers, runtime)

    async def list_storage_projects_info_async(
        self,
        request: main_models.ListStorageProjectsInfoRequest,
    ) -> main_models.ListStorageProjectsInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_storage_projects_info_with_options_async(request, headers, runtime)

    def list_storage_tables_info_with_options(
        self,
        project: str,
        tmp_req: main_models.ListStorageTablesInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStorageTablesInfoResponse:
        tmp_req.validate()
        request = main_models.ListStorageTablesInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'types', 'simple')
        query = {}
        if not DaraCore.is_null(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.order_column):
            query['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.recent_days):
            query['recentDays'] = request.recent_days
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.schema):
            query['schema'] = request.schema
        if not DaraCore.is_null(request.table_prefix):
            query['tablePrefix'] = request.table_prefix
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.types_shrink):
            query['types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStorageTablesInfo',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/projects/{DaraURL.percent_encode(project)}/tablesInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStorageTablesInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_storage_tables_info_with_options_async(
        self,
        project: str,
        tmp_req: main_models.ListStorageTablesInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListStorageTablesInfoResponse:
        tmp_req.validate()
        request = main_models.ListStorageTablesInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'types', 'simple')
        query = {}
        if not DaraCore.is_null(request.asc_order):
            query['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        if not DaraCore.is_null(request.order_column):
            query['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.recent_days):
            query['recentDays'] = request.recent_days
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.schema):
            query['schema'] = request.schema
        if not DaraCore.is_null(request.table_prefix):
            query['tablePrefix'] = request.table_prefix
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.types_shrink):
            query['types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStorageTablesInfo',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/analysis/storage/projects/{DaraURL.percent_encode(project)}/tablesInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStorageTablesInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_storage_tables_info(
        self,
        project: str,
        request: main_models.ListStorageTablesInfoRequest,
    ) -> main_models.ListStorageTablesInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_storage_tables_info_with_options(project, request, headers, runtime)

    async def list_storage_tables_info_async(
        self,
        project: str,
        request: main_models.ListStorageTablesInfoRequest,
    ) -> main_models.ListStorageTablesInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_storage_tables_info_with_options_async(project, request, headers, runtime)

    def list_tables_with_options(
        self,
        project_name: str,
        request: main_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.max_item):
            query['maxItem'] = request.max_item
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.schema_name):
            query['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        project_name: str,
        request: main_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.marker):
            query['marker'] = request.marker
        if not DaraCore.is_null(request.max_item):
            query['maxItem'] = request.max_item
        if not DaraCore.is_null(request.prefix):
            query['prefix'] = request.prefix
        if not DaraCore.is_null(request.schema_name):
            query['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tables(
        self,
        project_name: str,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tables_with_options(project_name, request, headers, runtime)

    async def list_tables_async(
        self,
        project_name: str,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tables_with_options_async(project_name, request, headers, runtime)

    def list_tunnel_quota_timer_with_options(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTunnelQuotaTimerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListTunnelQuotaTimer',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tunnel/{DaraURL.percent_encode(nickname)}/timers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTunnelQuotaTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tunnel_quota_timer_with_options_async(
        self,
        nickname: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTunnelQuotaTimerResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListTunnelQuotaTimer',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tunnel/{DaraURL.percent_encode(nickname)}/timers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTunnelQuotaTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tunnel_quota_timer(
        self,
        nickname: str,
    ) -> main_models.ListTunnelQuotaTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tunnel_quota_timer_with_options(nickname, headers, runtime)

    async def list_tunnel_quota_timer_async(
        self,
        nickname: str,
    ) -> main_models.ListTunnelQuotaTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tunnel_quota_timer_with_options_async(nickname, headers, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_users_with_options(request, headers, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(request, headers, runtime)

    def list_users_by_role_with_options(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersByRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListUsersByRole',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles/{DaraURL.percent_encode(role_name)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersByRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_by_role_with_options_async(
        self,
        project_name: str,
        role_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersByRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListUsersByRole',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles/{DaraURL.percent_encode(role_name)}/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersByRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users_by_role(
        self,
        project_name: str,
        role_name: str,
    ) -> main_models.ListUsersByRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_users_by_role_with_options(project_name, role_name, headers, runtime)

    async def list_users_by_role_async(
        self,
        project_name: str,
        role_name: str,
    ) -> main_models.ListUsersByRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_users_by_role_with_options_async(project_name, role_name, headers, runtime)

    def query_quota_with_options(
        self,
        nickname: str,
        request: main_models.QueryQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not DaraCore.is_null(request.mock):
            query['mock'] = request.mock
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryQuota',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/query',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_quota_with_options_async(
        self,
        nickname: str,
        request: main_models.QueryQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ak_proven):
            query['AkProven'] = request.ak_proven
        if not DaraCore.is_null(request.mock):
            query['mock'] = request.mock
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryQuota',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/query',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_quota(
        self,
        nickname: str,
        request: main_models.QueryQuotaRequest,
    ) -> main_models.QueryQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_quota_with_options(nickname, request, headers, runtime)

    async def query_quota_async(
        self,
        nickname: str,
        request: main_models.QueryQuotaRequest,
    ) -> main_models.QueryQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_quota_with_options_async(nickname, request, headers, runtime)

    def query_quota_metric_with_options(
        self,
        metric: str,
        request: main_models.QueryQuotaMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryQuotaMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.strategy):
            query['strategy'] = request.strategy
        body = {}
        if not DaraCore.is_null(request.interval):
            body['interval'] = request.interval
        if not DaraCore.is_null(request.nickname):
            body['nickname'] = request.nickname
        if not DaraCore.is_null(request.sub_metric):
            body['subMetric'] = request.sub_metric
        if not DaraCore.is_null(request.sub_quota_nickname):
            body['subQuotaNickname'] = request.sub_quota_nickname
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryQuotaMetric',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/quota/{DaraURL.percent_encode(metric)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryQuotaMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_quota_metric_with_options_async(
        self,
        metric: str,
        request: main_models.QueryQuotaMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryQuotaMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.strategy):
            query['strategy'] = request.strategy
        body = {}
        if not DaraCore.is_null(request.interval):
            body['interval'] = request.interval
        if not DaraCore.is_null(request.nickname):
            body['nickname'] = request.nickname
        if not DaraCore.is_null(request.sub_metric):
            body['subMetric'] = request.sub_metric
        if not DaraCore.is_null(request.sub_quota_nickname):
            body['subQuotaNickname'] = request.sub_quota_nickname
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryQuotaMetric',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/quota/{DaraURL.percent_encode(metric)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryQuotaMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_quota_metric(
        self,
        metric: str,
        request: main_models.QueryQuotaMetricRequest,
    ) -> main_models.QueryQuotaMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_quota_metric_with_options(metric, request, headers, runtime)

    async def query_quota_metric_async(
        self,
        metric: str,
        request: main_models.QueryQuotaMetricRequest,
    ) -> main_models.QueryQuotaMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_quota_metric_with_options_async(metric, request, headers, runtime)

    def query_storage_metric_with_options(
        self,
        metric: str,
        request: main_models.QueryStorageMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryStorageMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not DaraCore.is_null(request.project_list):
            body['projectList'] = request.project_list
        if not DaraCore.is_null(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryStorageMetric',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/storage/{DaraURL.percent_encode(metric)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStorageMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_storage_metric_with_options_async(
        self,
        metric: str,
        request: main_models.QueryStorageMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryStorageMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not DaraCore.is_null(request.project_list):
            body['projectList'] = request.project_list
        if not DaraCore.is_null(request.type_list):
            body['typeList'] = request.type_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryStorageMetric',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/storage/{DaraURL.percent_encode(metric)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStorageMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_storage_metric(
        self,
        metric: str,
        request: main_models.QueryStorageMetricRequest,
    ) -> main_models.QueryStorageMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_storage_metric_with_options(metric, request, headers, runtime)

    async def query_storage_metric_async(
        self,
        metric: str,
        request: main_models.QueryStorageMetricRequest,
    ) -> main_models.QueryStorageMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_storage_metric_with_options_async(metric, request, headers, runtime)

    def query_tunnel_metric_with_options(
        self,
        metric: str,
        request: main_models.QueryTunnelMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryTunnelMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.strategy):
            query['strategy'] = request.strategy
        body = {}
        if not DaraCore.is_null(request.code_list):
            body['codeList'] = request.code_list
        if not DaraCore.is_null(request.group_list):
            body['groupList'] = request.group_list
        if not DaraCore.is_null(request.operation_list):
            body['operationList'] = request.operation_list
        if not DaraCore.is_null(request.project):
            body['project'] = request.project
        if not DaraCore.is_null(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not DaraCore.is_null(request.table_list):
            body['tableList'] = request.table_list
        if not DaraCore.is_null(request.top_n):
            body['topN'] = request.top_n
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryTunnelMetric',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/tunnel/{DaraURL.percent_encode(metric)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTunnelMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tunnel_metric_with_options_async(
        self,
        metric: str,
        request: main_models.QueryTunnelMetricRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryTunnelMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.strategy):
            query['strategy'] = request.strategy
        body = {}
        if not DaraCore.is_null(request.code_list):
            body['codeList'] = request.code_list
        if not DaraCore.is_null(request.group_list):
            body['groupList'] = request.group_list
        if not DaraCore.is_null(request.operation_list):
            body['operationList'] = request.operation_list
        if not DaraCore.is_null(request.project):
            body['project'] = request.project
        if not DaraCore.is_null(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not DaraCore.is_null(request.table_list):
            body['tableList'] = request.table_list
        if not DaraCore.is_null(request.top_n):
            body['topN'] = request.top_n
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryTunnelMetric',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/tunnel/{DaraURL.percent_encode(metric)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTunnelMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tunnel_metric(
        self,
        metric: str,
        request: main_models.QueryTunnelMetricRequest,
    ) -> main_models.QueryTunnelMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_tunnel_metric_with_options(metric, request, headers, runtime)

    async def query_tunnel_metric_async(
        self,
        metric: str,
        request: main_models.QueryTunnelMetricRequest,
    ) -> main_models.QueryTunnelMetricResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_tunnel_metric_with_options_async(metric, request, headers, runtime)

    def query_tunnel_metric_detail_with_options(
        self,
        metric: str,
        request: main_models.QueryTunnelMetricDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryTunnelMetricDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not DaraCore.is_null(request.asc_order):
            body['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.group_list):
            body['groupList'] = request.group_list
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.operation_list):
            body['operationList'] = request.operation_list
        if not DaraCore.is_null(request.order_column):
            body['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.project):
            body['project'] = request.project
        if not DaraCore.is_null(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not DaraCore.is_null(request.table_list):
            body['tableList'] = request.table_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryTunnelMetricDetail',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/tunnel/{DaraURL.percent_encode(metric)}/detail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTunnelMetricDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tunnel_metric_detail_with_options_async(
        self,
        metric: str,
        request: main_models.QueryTunnelMetricDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryTunnelMetricDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        body = {}
        if not DaraCore.is_null(request.asc_order):
            body['ascOrder'] = request.asc_order
        if not DaraCore.is_null(request.group_list):
            body['groupList'] = request.group_list
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.operation_list):
            body['operationList'] = request.operation_list
        if not DaraCore.is_null(request.order_column):
            body['orderColumn'] = request.order_column
        if not DaraCore.is_null(request.project):
            body['project'] = request.project
        if not DaraCore.is_null(request.quota_nickname):
            body['quotaNickname'] = request.quota_nickname
        if not DaraCore.is_null(request.table_list):
            body['tableList'] = request.table_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryTunnelMetricDetail',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/observations/tunnel/{DaraURL.percent_encode(metric)}/detail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTunnelMetricDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_tunnel_metric_detail(
        self,
        metric: str,
        request: main_models.QueryTunnelMetricDetailRequest,
    ) -> main_models.QueryTunnelMetricDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_tunnel_metric_detail_with_options(metric, request, headers, runtime)

    async def query_tunnel_metric_detail_async(
        self,
        metric: str,
        request: main_models.QueryTunnelMetricDetailRequest,
    ) -> main_models.QueryTunnelMetricDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_tunnel_metric_detail_with_options_async(metric, request, headers, runtime)

    def retry_mms_job_with_options(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetryMmsJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RetryMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs/{DaraURL.percent_encode(job_id)}/retry',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_mms_job_with_options_async(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RetryMmsJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RetryMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs/{DaraURL.percent_encode(job_id)}/retry',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_mms_job(
        self,
        source_id: str,
        job_id: str,
    ) -> main_models.RetryMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.retry_mms_job_with_options(source_id, job_id, headers, runtime)

    async def retry_mms_job_async(
        self,
        source_id: str,
        job_id: str,
    ) -> main_models.RetryMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.retry_mms_job_with_options_async(source_id, job_id, headers, runtime)

    def start_mms_job_with_options(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartMmsJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs/{DaraURL.percent_encode(job_id)}/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_mms_job_with_options_async(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartMmsJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StartMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs/{DaraURL.percent_encode(job_id)}/start',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_mms_job(
        self,
        source_id: str,
        job_id: str,
    ) -> main_models.StartMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_mms_job_with_options(source_id, job_id, headers, runtime)

    async def start_mms_job_async(
        self,
        source_id: str,
        job_id: str,
    ) -> main_models.StartMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_mms_job_with_options_async(source_id, job_id, headers, runtime)

    def stop_mms_job_with_options(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopMmsJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs/{DaraURL.percent_encode(job_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopMmsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_mms_job_with_options_async(
        self,
        source_id: str,
        job_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopMmsJobResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopMmsJob',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}/jobs/{DaraURL.percent_encode(job_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopMmsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_mms_job(
        self,
        source_id: str,
        job_id: str,
    ) -> main_models.StopMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_mms_job_with_options(source_id, job_id, headers, runtime)

    async def stop_mms_job_async(
        self,
        source_id: str,
        job_id: str,
    ) -> main_models.StopMmsJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_mms_job_with_options_async(source_id, job_id, headers, runtime)

    def sum_storage_metrics_by_date_with_options(
        self,
        request: main_models.SumStorageMetricsByDateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SumStorageMetricsByDateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_date):
            body['endDate'] = request.end_date
        if not DaraCore.is_null(request.project_names):
            body['projectNames'] = request.project_names
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.start_date):
            body['startDate'] = request.start_date
        if not DaraCore.is_null(request.stats_type):
            body['statsType'] = request.stats_type
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SumStorageMetricsByDate',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/storageMetrics/sumByDate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SumStorageMetricsByDateResponse(),
            self.call_api(params, req, runtime)
        )

    async def sum_storage_metrics_by_date_with_options_async(
        self,
        request: main_models.SumStorageMetricsByDateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SumStorageMetricsByDateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_date):
            body['endDate'] = request.end_date
        if not DaraCore.is_null(request.project_names):
            body['projectNames'] = request.project_names
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.start_date):
            body['startDate'] = request.start_date
        if not DaraCore.is_null(request.stats_type):
            body['statsType'] = request.stats_type
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SumStorageMetricsByDate',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/storageMetrics/sumByDate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SumStorageMetricsByDateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sum_storage_metrics_by_date(
        self,
        request: main_models.SumStorageMetricsByDateRequest,
    ) -> main_models.SumStorageMetricsByDateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.sum_storage_metrics_by_date_with_options(request, headers, runtime)

    async def sum_storage_metrics_by_date_async(
        self,
        request: main_models.SumStorageMetricsByDateRequest,
    ) -> main_models.SumStorageMetricsByDateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.sum_storage_metrics_by_date_with_options_async(request, headers, runtime)

    def update_compute_quota_plan_with_options(
        self,
        nickname: str,
        request: main_models.UpdateComputeQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeQuotaPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_quota_plan_with_options_async(
        self,
        nickname: str,
        request: main_models.UpdateComputeQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeQuotaPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaPlan',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_quota_plan(
        self,
        nickname: str,
        request: main_models.UpdateComputeQuotaPlanRequest,
    ) -> main_models.UpdateComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_compute_quota_plan_with_options(nickname, request, headers, runtime)

    async def update_compute_quota_plan_async(
        self,
        nickname: str,
        request: main_models.UpdateComputeQuotaPlanRequest,
    ) -> main_models.UpdateComputeQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_compute_quota_plan_with_options_async(nickname, request, headers, runtime)

    def update_compute_quota_schedule_with_options(
        self,
        nickname: str,
        request: main_models.UpdateComputeQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeQuotaScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.schedule_timezone):
            query['scheduleTimezone'] = request.schedule_timezone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeQuotaSchedule',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaSchedule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: main_models.UpdateComputeQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeQuotaScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.schedule_timezone):
            query['scheduleTimezone'] = request.schedule_timezone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeQuotaSchedule',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeQuotaSchedule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_quota_schedule(
        self,
        nickname: str,
        request: main_models.UpdateComputeQuotaScheduleRequest,
    ) -> main_models.UpdateComputeQuotaScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_compute_quota_schedule_with_options(nickname, request, headers, runtime)

    async def update_compute_quota_schedule_async(
        self,
        nickname: str,
        request: main_models.UpdateComputeQuotaScheduleRequest,
    ) -> main_models.UpdateComputeQuotaScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_compute_quota_schedule_with_options_async(nickname, request, headers, runtime)

    def update_compute_sub_quota_with_options(
        self,
        nickname: str,
        request: main_models.UpdateComputeSubQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeSubQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.sub_quota_info_list):
            body['subQuotaInfoList'] = request.sub_quota_info_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeSubQuota',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeSubQuota',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeSubQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_compute_sub_quota_with_options_async(
        self,
        nickname: str,
        request: main_models.UpdateComputeSubQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComputeSubQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.sub_quota_info_list):
            body['subQuotaInfoList'] = request.sub_quota_info_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComputeSubQuota',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/computeSubQuota',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComputeSubQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_compute_sub_quota(
        self,
        nickname: str,
        request: main_models.UpdateComputeSubQuotaRequest,
    ) -> main_models.UpdateComputeSubQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_compute_sub_quota_with_options(nickname, request, headers, runtime)

    async def update_compute_sub_quota_async(
        self,
        nickname: str,
        request: main_models.UpdateComputeSubQuotaRequest,
    ) -> main_models.UpdateComputeSubQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_compute_sub_quota_with_options_async(nickname, request, headers, runtime)

    def update_mms_data_source_with_options(
        self,
        source_id: str,
        request: main_models.UpdateMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmsDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.test):
            body['test'] = request.test
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmsDataSource',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmsDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_mms_data_source_with_options_async(
        self,
        source_id: str,
        request: main_models.UpdateMmsDataSourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMmsDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.config):
            body['config'] = request.config
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.test):
            body['test'] = request.test
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMmsDataSource',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/mms/datasources/{DaraURL.percent_encode(source_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMmsDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_mms_data_source(
        self,
        source_id: str,
        request: main_models.UpdateMmsDataSourceRequest,
    ) -> main_models.UpdateMmsDataSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_mms_data_source_with_options(source_id, request, headers, runtime)

    async def update_mms_data_source_async(
        self,
        source_id: str,
        request: main_models.UpdateMmsDataSourceRequest,
    ) -> main_models.UpdateMmsDataSourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_mms_data_source_with_options_async(source_id, request, headers, runtime)

    def update_package_with_options(
        self,
        project_name: str,
        package_name: str,
        request: main_models.UpdatePackageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePackageResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdatePackage',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/packages/{DaraURL.percent_encode(package_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_package_with_options_async(
        self,
        project_name: str,
        package_name: str,
        request: main_models.UpdatePackageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePackageResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdatePackage',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/packages/{DaraURL.percent_encode(package_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_package(
        self,
        project_name: str,
        package_name: str,
        request: main_models.UpdatePackageRequest,
    ) -> main_models.UpdatePackageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_package_with_options(project_name, package_name, request, headers, runtime)

    async def update_package_async(
        self,
        project_name: str,
        package_name: str,
        request: main_models.UpdatePackageRequest,
    ) -> main_models.UpdatePackageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_package_with_options_async(project_name, package_name, request, headers, runtime)

    def update_project_basic_meta_with_options(
        self,
        project_name: str,
        request: main_models.UpdateProjectBasicMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectBasicMetaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['comment'] = request.comment
        if not DaraCore.is_null(request.properties):
            body['properties'] = request.properties
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProjectBasicMeta',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/meta',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectBasicMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_basic_meta_with_options_async(
        self,
        project_name: str,
        request: main_models.UpdateProjectBasicMetaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectBasicMetaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['comment'] = request.comment
        if not DaraCore.is_null(request.properties):
            body['properties'] = request.properties
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProjectBasicMeta',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/meta',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectBasicMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_basic_meta(
        self,
        project_name: str,
        request: main_models.UpdateProjectBasicMetaRequest,
    ) -> main_models.UpdateProjectBasicMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_project_basic_meta_with_options(project_name, request, headers, runtime)

    async def update_project_basic_meta_async(
        self,
        project_name: str,
        request: main_models.UpdateProjectBasicMetaRequest,
    ) -> main_models.UpdateProjectBasicMetaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_project_basic_meta_with_options_async(project_name, request, headers, runtime)

    def update_project_default_quota_with_options(
        self,
        project_name: str,
        request: main_models.UpdateProjectDefaultQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectDefaultQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProjectDefaultQuota',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/quota',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectDefaultQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_default_quota_with_options_async(
        self,
        project_name: str,
        request: main_models.UpdateProjectDefaultQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectDefaultQuotaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.quota):
            body['quota'] = request.quota
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProjectDefaultQuota',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/quota',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectDefaultQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_default_quota(
        self,
        project_name: str,
        request: main_models.UpdateProjectDefaultQuotaRequest,
    ) -> main_models.UpdateProjectDefaultQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_project_default_quota_with_options(project_name, request, headers, runtime)

    async def update_project_default_quota_async(
        self,
        project_name: str,
        request: main_models.UpdateProjectDefaultQuotaRequest,
    ) -> main_models.UpdateProjectDefaultQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_project_default_quota_with_options_async(project_name, request, headers, runtime)

    def update_project_ip_white_list_with_options(
        self,
        project_name: str,
        request: main_models.UpdateProjectIpWhiteListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectIpWhiteListResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateProjectIpWhiteList',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/ipWhiteList',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectIpWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_ip_white_list_with_options_async(
        self,
        project_name: str,
        request: main_models.UpdateProjectIpWhiteListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectIpWhiteListResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateProjectIpWhiteList',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/ipWhiteList',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectIpWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_ip_white_list(
        self,
        project_name: str,
        request: main_models.UpdateProjectIpWhiteListRequest,
    ) -> main_models.UpdateProjectIpWhiteListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_project_ip_white_list_with_options(project_name, request, headers, runtime)

    async def update_project_ip_white_list_async(
        self,
        project_name: str,
        request: main_models.UpdateProjectIpWhiteListRequest,
    ) -> main_models.UpdateProjectIpWhiteListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_project_ip_white_list_with_options_async(project_name, request, headers, runtime)

    def update_project_model_tier_with_options(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectModelTierResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UpdateProjectModelTier',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/modelTier',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectModelTierResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_model_tier_with_options_async(
        self,
        project_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectModelTierResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'UpdateProjectModelTier',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/modelTier',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectModelTierResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project_model_tier(
        self,
        project_name: str,
    ) -> main_models.UpdateProjectModelTierResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_project_model_tier_with_options(project_name, headers, runtime)

    async def update_project_model_tier_async(
        self,
        project_name: str,
    ) -> main_models.UpdateProjectModelTierResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_project_model_tier_with_options_async(project_name, headers, runtime)

    def update_quota_plan_with_options(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.UpdateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQuotaPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/plans/{DaraURL.percent_encode(plan_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQuotaPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_plan_with_options_async(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.UpdateQuotaPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQuotaPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateQuotaPlan',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/plans/{DaraURL.percent_encode(plan_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQuotaPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota_plan(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.UpdateQuotaPlanRequest,
    ) -> main_models.UpdateQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_quota_plan_with_options(nickname, plan_name, request, headers, runtime)

    async def update_quota_plan_async(
        self,
        nickname: str,
        plan_name: str,
        request: main_models.UpdateQuotaPlanRequest,
    ) -> main_models.UpdateQuotaPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_quota_plan_with_options_async(nickname, plan_name, request, headers, runtime)

    def update_quota_schedule_with_options(
        self,
        nickname: str,
        request: main_models.UpdateQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQuotaScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateQuotaSchedule',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/schedule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQuotaScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quota_schedule_with_options_async(
        self,
        nickname: str,
        request: main_models.UpdateQuotaScheduleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQuotaScheduleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'UpdateQuotaSchedule',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(nickname)}/schedule',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQuotaScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quota_schedule(
        self,
        nickname: str,
        request: main_models.UpdateQuotaScheduleRequest,
    ) -> main_models.UpdateQuotaScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_quota_schedule_with_options(nickname, request, headers, runtime)

    async def update_quota_schedule_async(
        self,
        nickname: str,
        request: main_models.UpdateQuotaScheduleRequest,
    ) -> main_models.UpdateQuotaScheduleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_quota_schedule_with_options_async(nickname, request, headers, runtime)

    def update_tunnel_quota_timer_with_options(
        self,
        nickname: str,
        request: main_models.UpdateTunnelQuotaTimerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTunnelQuotaTimerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.timezone):
            query['timezone'] = request.timezone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTunnelQuotaTimer',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tunnel/{DaraURL.percent_encode(nickname)}/timers',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTunnelQuotaTimerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tunnel_quota_timer_with_options_async(
        self,
        nickname: str,
        request: main_models.UpdateTunnelQuotaTimerRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTunnelQuotaTimerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.timezone):
            query['timezone'] = request.timezone
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.to_array(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTunnelQuotaTimer',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tunnel/{DaraURL.percent_encode(nickname)}/timers',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTunnelQuotaTimerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tunnel_quota_timer(
        self,
        nickname: str,
        request: main_models.UpdateTunnelQuotaTimerRequest,
    ) -> main_models.UpdateTunnelQuotaTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_tunnel_quota_timer_with_options(nickname, request, headers, runtime)

    async def update_tunnel_quota_timer_async(
        self,
        nickname: str,
        request: main_models.UpdateTunnelQuotaTimerRequest,
    ) -> main_models.UpdateTunnelQuotaTimerResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_tunnel_quota_timer_with_options_async(nickname, request, headers, runtime)

    def update_users_to_role_with_options(
        self,
        project_name: str,
        role_name: str,
        request: main_models.UpdateUsersToRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUsersToRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.add):
            body['add'] = request.add
        if not DaraCore.is_null(request.remove):
            body['remove'] = request.remove
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUsersToRole',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles/{DaraURL.percent_encode(role_name)}/users',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUsersToRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_users_to_role_with_options_async(
        self,
        project_name: str,
        role_name: str,
        request: main_models.UpdateUsersToRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUsersToRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.add):
            body['add'] = request.add
        if not DaraCore.is_null(request.remove):
            body['remove'] = request.remove
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUsersToRole',
            version = '2022-01-04',
            protocol = 'HTTPS',
            pathname = f'/api/v1/projects/{DaraURL.percent_encode(project_name)}/roles/{DaraURL.percent_encode(role_name)}/users',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUsersToRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_users_to_role(
        self,
        project_name: str,
        role_name: str,
        request: main_models.UpdateUsersToRoleRequest,
    ) -> main_models.UpdateUsersToRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_users_to_role_with_options(project_name, role_name, request, headers, runtime)

    async def update_users_to_role_async(
        self,
        project_name: str,
        role_name: str,
        request: main_models.UpdateUsersToRoleRequest,
    ) -> main_models.UpdateUsersToRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_users_to_role_with_options_async(project_name, role_name, request, headers, runtime)
