# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_lhm20250116 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('lhm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_data_check_config_with_options(
        self,
        request: main_models.AddDataCheckConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDataCheckConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_full_table_count):
            body['isFullTableCount'] = request.is_full_table_count
        if not DaraCore.is_null(request.source_columns):
            body['sourceColumns'] = request.source_columns
        if not DaraCore.is_null(request.source_group_clause):
            body['sourceGroupClause'] = request.source_group_clause
        if not DaraCore.is_null(request.source_hint):
            body['sourceHint'] = request.source_hint
        if not DaraCore.is_null(request.source_partition):
            body['sourcePartition'] = request.source_partition
        if not DaraCore.is_null(request.source_table):
            body['sourceTable'] = request.source_table
        if not DaraCore.is_null(request.source_where_clause):
            body['sourceWhereClause'] = request.source_where_clause
        if not DaraCore.is_null(request.target_columns):
            body['targetColumns'] = request.target_columns
        if not DaraCore.is_null(request.target_group_clause):
            body['targetGroupClause'] = request.target_group_clause
        if not DaraCore.is_null(request.target_hint):
            body['targetHint'] = request.target_hint
        if not DaraCore.is_null(request.target_partition):
            body['targetPartition'] = request.target_partition
        if not DaraCore.is_null(request.target_table):
            body['targetTable'] = request.target_table
        if not DaraCore.is_null(request.target_where_clause):
            body['targetWhereClause'] = request.target_where_clause
        if not DaraCore.is_null(request.task_config_info):
            body['taskConfigInfo'] = request.task_config_info
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.total_count_threshold):
            body['totalCountThreshold'] = request.total_count_threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataCheckConfig',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/config/v3/saveConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataCheckConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_check_config_with_options_async(
        self,
        request: main_models.AddDataCheckConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDataCheckConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_full_table_count):
            body['isFullTableCount'] = request.is_full_table_count
        if not DaraCore.is_null(request.source_columns):
            body['sourceColumns'] = request.source_columns
        if not DaraCore.is_null(request.source_group_clause):
            body['sourceGroupClause'] = request.source_group_clause
        if not DaraCore.is_null(request.source_hint):
            body['sourceHint'] = request.source_hint
        if not DaraCore.is_null(request.source_partition):
            body['sourcePartition'] = request.source_partition
        if not DaraCore.is_null(request.source_table):
            body['sourceTable'] = request.source_table
        if not DaraCore.is_null(request.source_where_clause):
            body['sourceWhereClause'] = request.source_where_clause
        if not DaraCore.is_null(request.target_columns):
            body['targetColumns'] = request.target_columns
        if not DaraCore.is_null(request.target_group_clause):
            body['targetGroupClause'] = request.target_group_clause
        if not DaraCore.is_null(request.target_hint):
            body['targetHint'] = request.target_hint
        if not DaraCore.is_null(request.target_partition):
            body['targetPartition'] = request.target_partition
        if not DaraCore.is_null(request.target_table):
            body['targetTable'] = request.target_table
        if not DaraCore.is_null(request.target_where_clause):
            body['targetWhereClause'] = request.target_where_clause
        if not DaraCore.is_null(request.task_config_info):
            body['taskConfigInfo'] = request.task_config_info
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.total_count_threshold):
            body['totalCountThreshold'] = request.total_count_threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataCheckConfig',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/config/v3/saveConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataCheckConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_check_config(
        self,
        request: main_models.AddDataCheckConfigRequest,
    ) -> main_models.AddDataCheckConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_data_check_config_with_options(request, headers, runtime)

    async def add_data_check_config_async(
        self,
        request: main_models.AddDataCheckConfigRequest,
    ) -> main_models.AddDataCheckConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_data_check_config_with_options_async(request, headers, runtime)

    def add_data_check_task_with_options(
        self,
        request: main_models.AddDataCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDataCheckTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_template_id):
            body['checkTemplateId'] = request.check_template_id
        if not DaraCore.is_null(request.check_type):
            body['checkType'] = request.check_type
        if not DaraCore.is_null(request.dst_ds_id):
            body['dstDsId'] = request.dst_ds_id
        if not DaraCore.is_null(request.dst_ds_name):
            body['dstDsName'] = request.dst_ds_name
        if not DaraCore.is_null(request.dst_ds_type):
            body['dstDsType'] = request.dst_ds_type
        if not DaraCore.is_null(request.src_ds_id):
            body['srcDsId'] = request.src_ds_id
        if not DaraCore.is_null(request.src_ds_name):
            body['srcDsName'] = request.src_ds_name
        if not DaraCore.is_null(request.src_ds_type):
            body['srcDsType'] = request.src_ds_type
        if not DaraCore.is_null(request.task_mode):
            body['taskMode'] = request.task_mode
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataCheckTask',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/add',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_check_task_with_options_async(
        self,
        request: main_models.AddDataCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDataCheckTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_template_id):
            body['checkTemplateId'] = request.check_template_id
        if not DaraCore.is_null(request.check_type):
            body['checkType'] = request.check_type
        if not DaraCore.is_null(request.dst_ds_id):
            body['dstDsId'] = request.dst_ds_id
        if not DaraCore.is_null(request.dst_ds_name):
            body['dstDsName'] = request.dst_ds_name
        if not DaraCore.is_null(request.dst_ds_type):
            body['dstDsType'] = request.dst_ds_type
        if not DaraCore.is_null(request.src_ds_id):
            body['srcDsId'] = request.src_ds_id
        if not DaraCore.is_null(request.src_ds_name):
            body['srcDsName'] = request.src_ds_name
        if not DaraCore.is_null(request.src_ds_type):
            body['srcDsType'] = request.src_ds_type
        if not DaraCore.is_null(request.task_mode):
            body['taskMode'] = request.task_mode
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataCheckTask',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/add',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_check_task(
        self,
        request: main_models.AddDataCheckTaskRequest,
    ) -> main_models.AddDataCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_data_check_task_with_options(request, headers, runtime)

    async def add_data_check_task_async(
        self,
        request: main_models.AddDataCheckTaskRequest,
    ) -> main_models.AddDataCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_data_check_task_with_options_async(request, headers, runtime)

    def add_data_check_template_with_options(
        self,
        request: main_models.AddDataCheckTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDataCheckTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.basic_metric_rules):
            body['basicMetricRules'] = request.basic_metric_rules
        if not DaraCore.is_null(request.check_type):
            body['checkType'] = request.check_type
        if not DaraCore.is_null(request.complex_metric_rules):
            body['complexMetricRules'] = request.complex_metric_rules
        if not DaraCore.is_null(request.ds_engine_rels):
            body['dsEngineRels'] = request.ds_engine_rels
        if not DaraCore.is_null(request.fulltext_rule):
            body['fulltextRule'] = request.fulltext_rule
        if not DaraCore.is_null(request.metric_rules):
            body['metricRules'] = request.metric_rules
        if not DaraCore.is_null(request.null_rules):
            body['nullRules'] = request.null_rules
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.template_desc):
            body['templateDesc'] = request.template_desc
        if not DaraCore.is_null(request.template_name):
            body['templateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.weak_content_rule):
            body['weakContentRule'] = request.weak_content_rule
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataCheckTemplate',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/template/v3/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataCheckTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_data_check_template_with_options_async(
        self,
        request: main_models.AddDataCheckTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddDataCheckTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.basic_metric_rules):
            body['basicMetricRules'] = request.basic_metric_rules
        if not DaraCore.is_null(request.check_type):
            body['checkType'] = request.check_type
        if not DaraCore.is_null(request.complex_metric_rules):
            body['complexMetricRules'] = request.complex_metric_rules
        if not DaraCore.is_null(request.ds_engine_rels):
            body['dsEngineRels'] = request.ds_engine_rels
        if not DaraCore.is_null(request.fulltext_rule):
            body['fulltextRule'] = request.fulltext_rule
        if not DaraCore.is_null(request.metric_rules):
            body['metricRules'] = request.metric_rules
        if not DaraCore.is_null(request.null_rules):
            body['nullRules'] = request.null_rules
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.template_desc):
            body['templateDesc'] = request.template_desc
        if not DaraCore.is_null(request.template_name):
            body['templateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            body['tenantId'] = request.tenant_id
        if not DaraCore.is_null(request.weak_content_rule):
            body['weakContentRule'] = request.weak_content_rule
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddDataCheckTemplate',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/template/v3/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddDataCheckTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_data_check_template(
        self,
        request: main_models.AddDataCheckTemplateRequest,
    ) -> main_models.AddDataCheckTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_data_check_template_with_options(request, headers, runtime)

    async def add_data_check_template_async(
        self,
        request: main_models.AddDataCheckTemplateRequest,
    ) -> main_models.AddDataCheckTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_data_check_template_with_options_async(request, headers, runtime)

    def add_meta_data_component_with_options(
        self,
        request: main_models.AddMetaDataComponentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddMetaDataComponentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_type):
            body['categoryType'] = request.category_type
        if not DaraCore.is_null(request.component_type):
            body['componentType'] = request.component_type
        if not DaraCore.is_null(request.ds_config):
            body['dsConfig'] = request.ds_config
        if not DaraCore.is_null(request.ds_desc):
            body['dsDesc'] = request.ds_desc
        if not DaraCore.is_null(request.ds_id):
            body['dsId'] = request.ds_id
        if not DaraCore.is_null(request.ds_name):
            body['dsName'] = request.ds_name
        if not DaraCore.is_null(request.ds_status):
            body['dsStatus'] = request.ds_status
        if not DaraCore.is_null(request.ds_type):
            body['dsType'] = request.ds_type
        if not DaraCore.is_null(request.ds_version):
            body['dsVersion'] = request.ds_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddMetaDataComponent',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/v2/meta/data-component',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMetaDataComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_meta_data_component_with_options_async(
        self,
        request: main_models.AddMetaDataComponentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddMetaDataComponentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_type):
            body['categoryType'] = request.category_type
        if not DaraCore.is_null(request.component_type):
            body['componentType'] = request.component_type
        if not DaraCore.is_null(request.ds_config):
            body['dsConfig'] = request.ds_config
        if not DaraCore.is_null(request.ds_desc):
            body['dsDesc'] = request.ds_desc
        if not DaraCore.is_null(request.ds_id):
            body['dsId'] = request.ds_id
        if not DaraCore.is_null(request.ds_name):
            body['dsName'] = request.ds_name
        if not DaraCore.is_null(request.ds_status):
            body['dsStatus'] = request.ds_status
        if not DaraCore.is_null(request.ds_type):
            body['dsType'] = request.ds_type
        if not DaraCore.is_null(request.ds_version):
            body['dsVersion'] = request.ds_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddMetaDataComponent',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/v2/meta/data-component',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddMetaDataComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_meta_data_component(
        self,
        request: main_models.AddMetaDataComponentRequest,
    ) -> main_models.AddMetaDataComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_meta_data_component_with_options(request, headers, runtime)

    async def add_meta_data_component_async(
        self,
        request: main_models.AddMetaDataComponentRequest,
    ) -> main_models.AddMetaDataComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_meta_data_component_with_options_async(request, headers, runtime)

    def create_execute_sql_conversion_with_options(
        self,
        request: main_models.CreateExecuteSqlConversionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExecuteSqlConversionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.source_dialect):
            body['sourceDialect'] = request.source_dialect
        if not DaraCore.is_null(request.source_sql_script):
            body['sourceSqlScript'] = request.source_sql_script
        if not DaraCore.is_null(request.target_dialect):
            body['targetDialect'] = request.target_dialect
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExecuteSqlConversion',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/jobMigrate/sqlTranslator/task/api/createExecute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExecuteSqlConversionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_execute_sql_conversion_with_options_async(
        self,
        request: main_models.CreateExecuteSqlConversionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateExecuteSqlConversionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.source_dialect):
            body['sourceDialect'] = request.source_dialect
        if not DaraCore.is_null(request.source_sql_script):
            body['sourceSqlScript'] = request.source_sql_script
        if not DaraCore.is_null(request.target_dialect):
            body['targetDialect'] = request.target_dialect
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExecuteSqlConversion',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/jobMigrate/sqlTranslator/task/api/createExecute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExecuteSqlConversionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_execute_sql_conversion(
        self,
        request: main_models.CreateExecuteSqlConversionRequest,
    ) -> main_models.CreateExecuteSqlConversionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_execute_sql_conversion_with_options(request, headers, runtime)

    async def create_execute_sql_conversion_async(
        self,
        request: main_models.CreateExecuteSqlConversionRequest,
    ) -> main_models.CreateExecuteSqlConversionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_execute_sql_conversion_with_options_async(request, headers, runtime)

    def create_sql_exec_job_with_options(
        self,
        request: main_models.CreateSqlExecJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSqlExecJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.concurrency):
            body['concurrency'] = request.concurrency
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSqlExecJob',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/execute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSqlExecJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sql_exec_job_with_options_async(
        self,
        request: main_models.CreateSqlExecJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSqlExecJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.concurrency):
            body['concurrency'] = request.concurrency
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSqlExecJob',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/execute',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSqlExecJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sql_exec_job(
        self,
        request: main_models.CreateSqlExecJobRequest,
    ) -> main_models.CreateSqlExecJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_sql_exec_job_with_options(request, headers, runtime)

    async def create_sql_exec_job_async(
        self,
        request: main_models.CreateSqlExecJobRequest,
    ) -> main_models.CreateSqlExecJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_sql_exec_job_with_options_async(request, headers, runtime)

    def delete_data_check_config_with_options(
        self,
        request: main_models.DeleteDataCheckConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataCheckConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataCheckConfig',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/config/v3/deleteConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataCheckConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_check_config_with_options_async(
        self,
        request: main_models.DeleteDataCheckConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataCheckConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataCheckConfig',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/config/v3/deleteConfig',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataCheckConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_check_config(
        self,
        request: main_models.DeleteDataCheckConfigRequest,
    ) -> main_models.DeleteDataCheckConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_data_check_config_with_options(request, headers, runtime)

    async def delete_data_check_config_async(
        self,
        request: main_models.DeleteDataCheckConfigRequest,
    ) -> main_models.DeleteDataCheckConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_data_check_config_with_options_async(request, headers, runtime)

    def delete_data_check_task_with_options(
        self,
        request: main_models.DeleteDataCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataCheckTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_ids):
            body['taskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataCheckTask',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_check_task_with_options_async(
        self,
        request: main_models.DeleteDataCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataCheckTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_ids):
            body['taskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataCheckTask',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_check_task(
        self,
        request: main_models.DeleteDataCheckTaskRequest,
    ) -> main_models.DeleteDataCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_data_check_task_with_options(request, headers, runtime)

    async def delete_data_check_task_async(
        self,
        request: main_models.DeleteDataCheckTaskRequest,
    ) -> main_models.DeleteDataCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_data_check_task_with_options_async(request, headers, runtime)

    def delete_data_check_template_with_options(
        self,
        request: main_models.DeleteDataCheckTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataCheckTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataCheckTemplate',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/template/v3/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataCheckTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_check_template_with_options_async(
        self,
        request: main_models.DeleteDataCheckTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataCheckTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.template_ids):
            body['templateIds'] = request.template_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataCheckTemplate',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/template/v3/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataCheckTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_check_template(
        self,
        request: main_models.DeleteDataCheckTemplateRequest,
    ) -> main_models.DeleteDataCheckTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_data_check_template_with_options(request, headers, runtime)

    async def delete_data_check_template_async(
        self,
        request: main_models.DeleteDataCheckTemplateRequest,
    ) -> main_models.DeleteDataCheckTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_data_check_template_with_options_async(request, headers, runtime)

    def edit_task_pop_with_options(
        self,
        request: main_models.EditTaskPopRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EditTaskPopResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.concurrency):
            body['concurrency'] = request.concurrency
        if not DaraCore.is_null(request.dql_test_datasource_name):
            body['dqlTestDatasourceName'] = request.dql_test_datasource_name
        if not DaraCore.is_null(request.source_dialect):
            body['sourceDialect'] = request.source_dialect
        if not DaraCore.is_null(request.target_dialect):
            body['targetDialect'] = request.target_dialect
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditTaskPop',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/editPop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditTaskPopResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_task_pop_with_options_async(
        self,
        request: main_models.EditTaskPopRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EditTaskPopResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.concurrency):
            body['concurrency'] = request.concurrency
        if not DaraCore.is_null(request.dql_test_datasource_name):
            body['dqlTestDatasourceName'] = request.dql_test_datasource_name
        if not DaraCore.is_null(request.source_dialect):
            body['sourceDialect'] = request.source_dialect
        if not DaraCore.is_null(request.target_dialect):
            body['targetDialect'] = request.target_dialect
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EditTaskPop',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/editPop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditTaskPopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_task_pop(
        self,
        request: main_models.EditTaskPopRequest,
    ) -> main_models.EditTaskPopResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.edit_task_pop_with_options(request, headers, runtime)

    async def edit_task_pop_async(
        self,
        request: main_models.EditTaskPopRequest,
    ) -> main_models.EditTaskPopResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.edit_task_pop_with_options_async(request, headers, runtime)

    def exec_data_check_download_report_with_options(
        self,
        request: main_models.ExecDataCheckDownloadReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckDownloadReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckDownloadReport',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/download',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckDownloadReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_data_check_download_report_with_options_async(
        self,
        request: main_models.ExecDataCheckDownloadReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckDownloadReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckDownloadReport',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/download',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckDownloadReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_data_check_download_report(
        self,
        request: main_models.ExecDataCheckDownloadReportRequest,
    ) -> main_models.ExecDataCheckDownloadReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_data_check_download_report_with_options(request, headers, runtime)

    async def exec_data_check_download_report_async(
        self,
        request: main_models.ExecDataCheckDownloadReportRequest,
    ) -> main_models.ExecDataCheckDownloadReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_data_check_download_report_with_options_async(request, headers, runtime)

    def exec_data_check_generate_report_with_options(
        self,
        request: main_models.ExecDataCheckGenerateReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckGenerateReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckGenerateReport',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/generateReport',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckGenerateReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_data_check_generate_report_with_options_async(
        self,
        request: main_models.ExecDataCheckGenerateReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckGenerateReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckGenerateReport',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/generateReport',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckGenerateReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_data_check_generate_report(
        self,
        request: main_models.ExecDataCheckGenerateReportRequest,
    ) -> main_models.ExecDataCheckGenerateReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_data_check_generate_report_with_options(request, headers, runtime)

    async def exec_data_check_generate_report_async(
        self,
        request: main_models.ExecDataCheckGenerateReportRequest,
    ) -> main_models.ExecDataCheckGenerateReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_data_check_generate_report_with_options_async(request, headers, runtime)

    def exec_data_check_re_run_with_options(
        self,
        request: main_models.ExecDataCheckReRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckReRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckReRun',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/rerun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckReRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_data_check_re_run_with_options_async(
        self,
        request: main_models.ExecDataCheckReRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckReRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckReRun',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/rerun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckReRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_data_check_re_run(
        self,
        request: main_models.ExecDataCheckReRunRequest,
    ) -> main_models.ExecDataCheckReRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_data_check_re_run_with_options(request, headers, runtime)

    async def exec_data_check_re_run_async(
        self,
        request: main_models.ExecDataCheckReRunRequest,
    ) -> main_models.ExecDataCheckReRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_data_check_re_run_with_options_async(request, headers, runtime)

    def exec_data_check_run_with_options(
        self,
        request: main_models.ExecDataCheckRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckRun',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_data_check_run_with_options_async(
        self,
        request: main_models.ExecDataCheckRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckRun',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/run',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_data_check_run(
        self,
        request: main_models.ExecDataCheckRunRequest,
    ) -> main_models.ExecDataCheckRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_data_check_run_with_options(request, headers, runtime)

    async def exec_data_check_run_async(
        self,
        request: main_models.ExecDataCheckRunRequest,
    ) -> main_models.ExecDataCheckRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_data_check_run_with_options_async(request, headers, runtime)

    def exec_data_check_run_failed_with_options(
        self,
        request: main_models.ExecDataCheckRunFailedRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckRunFailedResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckRunFailed',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/runFailed',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckRunFailedResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_data_check_run_failed_with_options_async(
        self,
        request: main_models.ExecDataCheckRunFailedRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckRunFailedResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckRunFailed',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/runFailed',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckRunFailedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_data_check_run_failed(
        self,
        request: main_models.ExecDataCheckRunFailedRequest,
    ) -> main_models.ExecDataCheckRunFailedResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_data_check_run_failed_with_options(request, headers, runtime)

    async def exec_data_check_run_failed_async(
        self,
        request: main_models.ExecDataCheckRunFailedRequest,
    ) -> main_models.ExecDataCheckRunFailedResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_data_check_run_failed_with_options_async(request, headers, runtime)

    def exec_data_check_save_task_with_options(
        self,
        request: main_models.ExecDataCheckSaveTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckSaveTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_global_params):
            body['checkGlobalParams'] = request.check_global_params
        if not DaraCore.is_null(request.full_table_count):
            body['fullTableCount'] = request.full_table_count
        if not DaraCore.is_null(request.source_global_params):
            body['sourceGlobalParams'] = request.source_global_params
        if not DaraCore.is_null(request.start_immediately):
            body['startImmediately'] = request.start_immediately
        if not DaraCore.is_null(request.target_global_params):
            body['targetGlobalParams'] = request.target_global_params
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.total_count_threshold):
            body['totalCountThreshold'] = request.total_count_threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckSaveTask',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/save',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckSaveTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_data_check_save_task_with_options_async(
        self,
        request: main_models.ExecDataCheckSaveTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckSaveTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_global_params):
            body['checkGlobalParams'] = request.check_global_params
        if not DaraCore.is_null(request.full_table_count):
            body['fullTableCount'] = request.full_table_count
        if not DaraCore.is_null(request.source_global_params):
            body['sourceGlobalParams'] = request.source_global_params
        if not DaraCore.is_null(request.start_immediately):
            body['startImmediately'] = request.start_immediately
        if not DaraCore.is_null(request.target_global_params):
            body['targetGlobalParams'] = request.target_global_params
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.total_count_threshold):
            body['totalCountThreshold'] = request.total_count_threshold
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckSaveTask',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/save',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckSaveTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_data_check_save_task(
        self,
        request: main_models.ExecDataCheckSaveTaskRequest,
    ) -> main_models.ExecDataCheckSaveTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_data_check_save_task_with_options(request, headers, runtime)

    async def exec_data_check_save_task_async(
        self,
        request: main_models.ExecDataCheckSaveTaskRequest,
    ) -> main_models.ExecDataCheckSaveTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_data_check_save_task_with_options_async(request, headers, runtime)

    def exec_data_check_sql_preview_with_options(
        self,
        request: main_models.ExecDataCheckSqlPreviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckSqlPreviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_column):
            body['checkColumn'] = request.check_column
        if not DaraCore.is_null(request.data_source_id):
            body['dataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.engine_id):
            body['engineId'] = request.engine_id
        if not DaraCore.is_null(request.full_table_name):
            body['fullTableName'] = request.full_table_name
        if not DaraCore.is_null(request.partition_condition):
            body['partitionCondition'] = request.partition_condition
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.where_clause):
            body['whereClause'] = request.where_clause
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckSqlPreview',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/config/v3/sql/preview',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckSqlPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_data_check_sql_preview_with_options_async(
        self,
        request: main_models.ExecDataCheckSqlPreviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckSqlPreviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_column):
            body['checkColumn'] = request.check_column
        if not DaraCore.is_null(request.data_source_id):
            body['dataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.engine_id):
            body['engineId'] = request.engine_id
        if not DaraCore.is_null(request.full_table_name):
            body['fullTableName'] = request.full_table_name
        if not DaraCore.is_null(request.partition_condition):
            body['partitionCondition'] = request.partition_condition
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.where_clause):
            body['whereClause'] = request.where_clause
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckSqlPreview',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/config/v3/sql/preview',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckSqlPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_data_check_sql_preview(
        self,
        request: main_models.ExecDataCheckSqlPreviewRequest,
    ) -> main_models.ExecDataCheckSqlPreviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_data_check_sql_preview_with_options(request, headers, runtime)

    async def exec_data_check_sql_preview_async(
        self,
        request: main_models.ExecDataCheckSqlPreviewRequest,
    ) -> main_models.ExecDataCheckSqlPreviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_data_check_sql_preview_with_options_async(request, headers, runtime)

    def exec_data_check_stop_with_options(
        self,
        request: main_models.ExecDataCheckStopRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckStopResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckStop',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckStopResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_data_check_stop_with_options_async(
        self,
        request: main_models.ExecDataCheckStopRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckStopResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckStop',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckStopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_data_check_stop(
        self,
        request: main_models.ExecDataCheckStopRequest,
    ) -> main_models.ExecDataCheckStopResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_data_check_stop_with_options(request, headers, runtime)

    async def exec_data_check_stop_async(
        self,
        request: main_models.ExecDataCheckStopRequest,
    ) -> main_models.ExecDataCheckStopResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_data_check_stop_with_options_async(request, headers, runtime)

    def exec_data_check_toggle_with_options(
        self,
        request: main_models.ExecDataCheckToggleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckToggleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckToggle',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/toggle',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckToggleResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_data_check_toggle_with_options_async(
        self,
        request: main_models.ExecDataCheckToggleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecDataCheckToggleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.params):
            body['params'] = request.params
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecDataCheckToggle',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/toggle',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDataCheckToggleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_data_check_toggle(
        self,
        request: main_models.ExecDataCheckToggleRequest,
    ) -> main_models.ExecDataCheckToggleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_data_check_toggle_with_options(request, headers, runtime)

    async def exec_data_check_toggle_async(
        self,
        request: main_models.ExecDataCheckToggleRequest,
    ) -> main_models.ExecDataCheckToggleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_data_check_toggle_with_options_async(request, headers, runtime)

    def exec_meta_data_component_name_with_options(
        self,
        request: main_models.ExecMetaDataComponentNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecMetaDataComponentNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ds_name):
            query['dsName'] = request.ds_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecMetaDataComponentName',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/v2/meta/data-component/check-name',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecMetaDataComponentNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_meta_data_component_name_with_options_async(
        self,
        request: main_models.ExecMetaDataComponentNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecMetaDataComponentNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ds_name):
            query['dsName'] = request.ds_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecMetaDataComponentName',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/v2/meta/data-component/check-name',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecMetaDataComponentNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_meta_data_component_name(
        self,
        request: main_models.ExecMetaDataComponentNameRequest,
    ) -> main_models.ExecMetaDataComponentNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_meta_data_component_name_with_options(request, headers, runtime)

    async def exec_meta_data_component_name_async(
        self,
        request: main_models.ExecMetaDataComponentNameRequest,
    ) -> main_models.ExecMetaDataComponentNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_meta_data_component_name_with_options_async(request, headers, runtime)

    def exec_sql_trans_single_script_translate_with_options(
        self,
        request: main_models.ExecSqlTransSingleScriptTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecSqlTransSingleScriptTranslateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.source_dialect):
            body['sourceDialect'] = request.source_dialect
        if not DaraCore.is_null(request.source_sql_script):
            body['sourceSqlScript'] = request.source_sql_script
        if not DaraCore.is_null(request.table_mapping):
            body['tableMapping'] = request.table_mapping
        if not DaraCore.is_null(request.target_dialect):
            body['targetDialect'] = request.target_dialect
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecSqlTransSingleScriptTranslate',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/open/single/translate-sync',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecSqlTransSingleScriptTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_sql_trans_single_script_translate_with_options_async(
        self,
        request: main_models.ExecSqlTransSingleScriptTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecSqlTransSingleScriptTranslateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.source_dialect):
            body['sourceDialect'] = request.source_dialect
        if not DaraCore.is_null(request.source_sql_script):
            body['sourceSqlScript'] = request.source_sql_script
        if not DaraCore.is_null(request.table_mapping):
            body['tableMapping'] = request.table_mapping
        if not DaraCore.is_null(request.target_dialect):
            body['targetDialect'] = request.target_dialect
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecSqlTransSingleScriptTranslate',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/open/single/translate-sync',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecSqlTransSingleScriptTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_sql_trans_single_script_translate(
        self,
        request: main_models.ExecSqlTransSingleScriptTranslateRequest,
    ) -> main_models.ExecSqlTransSingleScriptTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_sql_trans_single_script_translate_with_options(request, headers, runtime)

    async def exec_sql_trans_single_script_translate_async(
        self,
        request: main_models.ExecSqlTransSingleScriptTranslateRequest,
    ) -> main_models.ExecSqlTransSingleScriptTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_sql_trans_single_script_translate_with_options_async(request, headers, runtime)

    def exec_workflow_connectivity_with_options(
        self,
        request: main_models.ExecWorkflowConnectivityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecWorkflowConnectivityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ds_config):
            body['dsConfig'] = request.ds_config
        if not DaraCore.is_null(request.ds_name):
            body['dsName'] = request.ds_name
        if not DaraCore.is_null(request.ds_type):
            body['dsType'] = request.ds_type
        if not DaraCore.is_null(request.ds_version):
            body['dsVersion'] = request.ds_version
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.is_modified):
            body['isModified'] = request.is_modified
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecWorkflowConnectivity',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/v2/meta/data-component/workflow/connectivity',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecWorkflowConnectivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_workflow_connectivity_with_options_async(
        self,
        request: main_models.ExecWorkflowConnectivityRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecWorkflowConnectivityResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ds_config):
            body['dsConfig'] = request.ds_config
        if not DaraCore.is_null(request.ds_name):
            body['dsName'] = request.ds_name
        if not DaraCore.is_null(request.ds_type):
            body['dsType'] = request.ds_type
        if not DaraCore.is_null(request.ds_version):
            body['dsVersion'] = request.ds_version
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.is_modified):
            body['isModified'] = request.is_modified
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecWorkflowConnectivity',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/v2/meta/data-component/workflow/connectivity',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecWorkflowConnectivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_workflow_connectivity(
        self,
        request: main_models.ExecWorkflowConnectivityRequest,
    ) -> main_models.ExecWorkflowConnectivityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.exec_workflow_connectivity_with_options(request, headers, runtime)

    async def exec_workflow_connectivity_async(
        self,
        request: main_models.ExecWorkflowConnectivityRequest,
    ) -> main_models.ExecWorkflowConnectivityResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.exec_workflow_connectivity_with_options_async(request, headers, runtime)

    def get_bwm_migration_submit_instance_list_with_options(
        self,
        request: main_models.GetBwmMigrationSubmitInstanceListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBwmMigrationSubmitInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBwmMigrationSubmitInstanceList',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bwm/task/migration/submit/instances/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBwmMigrationSubmitInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bwm_migration_submit_instance_list_with_options_async(
        self,
        request: main_models.GetBwmMigrationSubmitInstanceListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBwmMigrationSubmitInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBwmMigrationSubmitInstanceList',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bwm/task/migration/submit/instances/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBwmMigrationSubmitInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bwm_migration_submit_instance_list(
        self,
        request: main_models.GetBwmMigrationSubmitInstanceListRequest,
    ) -> main_models.GetBwmMigrationSubmitInstanceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_bwm_migration_submit_instance_list_with_options(request, headers, runtime)

    async def get_bwm_migration_submit_instance_list_async(
        self,
        request: main_models.GetBwmMigrationSubmitInstanceListRequest,
    ) -> main_models.GetBwmMigrationSubmitInstanceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_bwm_migration_submit_instance_list_with_options_async(request, headers, runtime)

    def get_bwm_migration_task_writer_result_package_with_options(
        self,
        request: main_models.GetBwmMigrationTaskWriterResultPackageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBwmMigrationTaskWriterResultPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBwmMigrationTaskWriterResultPackage',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bwm/task/migration/write/result/export/package',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBwmMigrationTaskWriterResultPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bwm_migration_task_writer_result_package_with_options_async(
        self,
        request: main_models.GetBwmMigrationTaskWriterResultPackageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBwmMigrationTaskWriterResultPackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBwmMigrationTaskWriterResultPackage',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bwm/task/migration/write/result/export/package',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBwmMigrationTaskWriterResultPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bwm_migration_task_writer_result_package(
        self,
        request: main_models.GetBwmMigrationTaskWriterResultPackageRequest,
    ) -> main_models.GetBwmMigrationTaskWriterResultPackageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_bwm_migration_task_writer_result_package_with_options(request, headers, runtime)

    async def get_bwm_migration_task_writer_result_package_async(
        self,
        request: main_models.GetBwmMigrationTaskWriterResultPackageRequest,
    ) -> main_models.GetBwmMigrationTaskWriterResultPackageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_bwm_migration_task_writer_result_package_with_options_async(request, headers, runtime)

    def get_bwm_migration_task_writer_workflow_list_with_options(
        self,
        request: main_models.GetBwmMigrationTaskWriterWorkflowListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBwmMigrationTaskWriterWorkflowListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.workflow_name):
            query['workflowName'] = request.workflow_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBwmMigrationTaskWriterWorkflowList',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bwm/task/migration/write/result/workflow/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBwmMigrationTaskWriterWorkflowListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bwm_migration_task_writer_workflow_list_with_options_async(
        self,
        request: main_models.GetBwmMigrationTaskWriterWorkflowListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBwmMigrationTaskWriterWorkflowListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.workflow_name):
            query['workflowName'] = request.workflow_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBwmMigrationTaskWriterWorkflowList',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bwm/task/migration/write/result/workflow/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBwmMigrationTaskWriterWorkflowListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bwm_migration_task_writer_workflow_list(
        self,
        request: main_models.GetBwmMigrationTaskWriterWorkflowListRequest,
    ) -> main_models.GetBwmMigrationTaskWriterWorkflowListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_bwm_migration_task_writer_workflow_list_with_options(request, headers, runtime)

    async def get_bwm_migration_task_writer_workflow_list_async(
        self,
        request: main_models.GetBwmMigrationTaskWriterWorkflowListRequest,
    ) -> main_models.GetBwmMigrationTaskWriterWorkflowListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_bwm_migration_task_writer_workflow_list_with_options_async(request, headers, runtime)

    def get_bwm_migration_workflow_submit_start_with_options(
        self,
        request: main_models.GetBwmMigrationWorkflowSubmitStartRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBwmMigrationWorkflowSubmitStartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBwmMigrationWorkflowSubmitStart',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bwm/task/migration/submit/start',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBwmMigrationWorkflowSubmitStartResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bwm_migration_workflow_submit_start_with_options_async(
        self,
        request: main_models.GetBwmMigrationWorkflowSubmitStartRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBwmMigrationWorkflowSubmitStartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBwmMigrationWorkflowSubmitStart',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bwm/task/migration/submit/start',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBwmMigrationWorkflowSubmitStartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bwm_migration_workflow_submit_start(
        self,
        request: main_models.GetBwmMigrationWorkflowSubmitStartRequest,
    ) -> main_models.GetBwmMigrationWorkflowSubmitStartResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_bwm_migration_workflow_submit_start_with_options(request, headers, runtime)

    async def get_bwm_migration_workflow_submit_start_async(
        self,
        request: main_models.GetBwmMigrationWorkflowSubmitStartRequest,
    ) -> main_models.GetBwmMigrationWorkflowSubmitStartResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_bwm_migration_workflow_submit_start_with_options_async(request, headers, runtime)

    def get_cron_exec_time_with_options(
        self,
        request: main_models.GetCronExecTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCronExecTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cron_rule):
            query['cronRule'] = request.cron_rule
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCronExecTime',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/cron/exeTime',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCronExecTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cron_exec_time_with_options_async(
        self,
        request: main_models.GetCronExecTimeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCronExecTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cron_rule):
            query['cronRule'] = request.cron_rule
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCronExecTime',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/cron/exeTime',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCronExecTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cron_exec_time(
        self,
        request: main_models.GetCronExecTimeRequest,
    ) -> main_models.GetCronExecTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_cron_exec_time_with_options(request, headers, runtime)

    async def get_cron_exec_time_async(
        self,
        request: main_models.GetCronExecTimeRequest,
    ) -> main_models.GetCronExecTimeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_cron_exec_time_with_options_async(request, headers, runtime)

    def get_data_check_config_with_options(
        self,
        request: main_models.GetDataCheckConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckConfig',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/config/v3/getConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_check_config_with_options_async(
        self,
        request: main_models.GetDataCheckConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckConfig',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/config/v3/getConfig',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_check_config(
        self,
        request: main_models.GetDataCheckConfigRequest,
    ) -> main_models.GetDataCheckConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_data_check_config_with_options(request, headers, runtime)

    async def get_data_check_config_async(
        self,
        request: main_models.GetDataCheckConfigRequest,
    ) -> main_models.GetDataCheckConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_data_check_config_with_options_async(request, headers, runtime)

    def get_data_check_report_overview_with_options(
        self,
        request: main_models.GetDataCheckReportOverviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckReportOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckReportOverview',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/overview',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckReportOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_check_report_overview_with_options_async(
        self,
        request: main_models.GetDataCheckReportOverviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckReportOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckReportOverview',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/overview',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckReportOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_check_report_overview(
        self,
        request: main_models.GetDataCheckReportOverviewRequest,
    ) -> main_models.GetDataCheckReportOverviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_data_check_report_overview_with_options(request, headers, runtime)

    async def get_data_check_report_overview_async(
        self,
        request: main_models.GetDataCheckReportOverviewRequest,
    ) -> main_models.GetDataCheckReportOverviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_data_check_report_overview_with_options_async(request, headers, runtime)

    def get_data_check_report_status_with_options(
        self,
        request: main_models.GetDataCheckReportStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckReportStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckReportStatus',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/getReportStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckReportStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_check_report_status_with_options_async(
        self,
        request: main_models.GetDataCheckReportStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckReportStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['batchId'] = request.batch_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckReportStatus',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/getReportStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckReportStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_check_report_status(
        self,
        request: main_models.GetDataCheckReportStatusRequest,
    ) -> main_models.GetDataCheckReportStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_data_check_report_status_with_options(request, headers, runtime)

    async def get_data_check_report_status_async(
        self,
        request: main_models.GetDataCheckReportStatusRequest,
    ) -> main_models.GetDataCheckReportStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_data_check_report_status_with_options_async(request, headers, runtime)

    def get_data_check_task_config_with_options(
        self,
        request: main_models.GetDataCheckTaskConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckTaskConfig',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_check_task_config_with_options_async(
        self,
        request: main_models.GetDataCheckTaskConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckTaskConfig',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_check_task_config(
        self,
        request: main_models.GetDataCheckTaskConfigRequest,
    ) -> main_models.GetDataCheckTaskConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_data_check_task_config_with_options(request, headers, runtime)

    async def get_data_check_task_config_async(
        self,
        request: main_models.GetDataCheckTaskConfigRequest,
    ) -> main_models.GetDataCheckTaskConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_data_check_task_config_with_options_async(request, headers, runtime)

    def get_data_check_task_list_with_options(
        self,
        request: main_models.GetDataCheckTaskListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckTaskListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_result):
            body['checkResult'] = request.check_result
        if not DaraCore.is_null(request.check_type):
            body['checkType'] = request.check_type
        if not DaraCore.is_null(request.create_end_time):
            body['createEndTime'] = request.create_end_time
        if not DaraCore.is_null(request.create_start_time):
            body['createStartTime'] = request.create_start_time
        if not DaraCore.is_null(request.exec_status):
            body['execStatus'] = request.exec_status
        if not DaraCore.is_null(request.is_scheduled):
            body['isScheduled'] = request.is_scheduled
        if not DaraCore.is_null(request.page_index):
            body['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        if not DaraCore.is_null(request.template_name):
            body['templateName'] = request.template_name
        if not DaraCore.is_null(request.update_end_time):
            body['updateEndTime'] = request.update_end_time
        if not DaraCore.is_null(request.update_start_time):
            body['updateStartTime'] = request.update_start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckTaskList',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/find',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_check_task_list_with_options_async(
        self,
        request: main_models.GetDataCheckTaskListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckTaskListResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_result):
            body['checkResult'] = request.check_result
        if not DaraCore.is_null(request.check_type):
            body['checkType'] = request.check_type
        if not DaraCore.is_null(request.create_end_time):
            body['createEndTime'] = request.create_end_time
        if not DaraCore.is_null(request.create_start_time):
            body['createStartTime'] = request.create_start_time
        if not DaraCore.is_null(request.exec_status):
            body['execStatus'] = request.exec_status
        if not DaraCore.is_null(request.is_scheduled):
            body['isScheduled'] = request.is_scheduled
        if not DaraCore.is_null(request.page_index):
            body['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        if not DaraCore.is_null(request.template_name):
            body['templateName'] = request.template_name
        if not DaraCore.is_null(request.update_end_time):
            body['updateEndTime'] = request.update_end_time
        if not DaraCore.is_null(request.update_start_time):
            body['updateStartTime'] = request.update_start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckTaskList',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/find',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_check_task_list(
        self,
        request: main_models.GetDataCheckTaskListRequest,
    ) -> main_models.GetDataCheckTaskListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_data_check_task_list_with_options(request, headers, runtime)

    async def get_data_check_task_list_async(
        self,
        request: main_models.GetDataCheckTaskListRequest,
    ) -> main_models.GetDataCheckTaskListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_data_check_task_list_with_options_async(request, headers, runtime)

    def get_data_check_template_with_options(
        self,
        request: main_models.GetDataCheckTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckTemplate',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/template/v3/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_check_template_with_options_async(
        self,
        request: main_models.GetDataCheckTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckTemplate',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/template/v3/get',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_check_template(
        self,
        request: main_models.GetDataCheckTemplateRequest,
    ) -> main_models.GetDataCheckTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_data_check_template_with_options(request, headers, runtime)

    async def get_data_check_template_async(
        self,
        request: main_models.GetDataCheckTemplateRequest,
    ) -> main_models.GetDataCheckTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_data_check_template_with_options_async(request, headers, runtime)

    def get_data_check_template_list_with_options(
        self,
        tmp_req: main_models.GetDataCheckTemplateListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckTemplateListResponse:
        tmp_req.validate()
        request = main_models.GetDataCheckTemplateListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.id_list):
            request.id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.id_list, 'idList', 'json')
        query = {}
        if not DaraCore.is_null(request.check_type):
            query['checkType'] = request.check_type
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.id_list_shrink):
            query['idList'] = request.id_list_shrink
        if not DaraCore.is_null(request.is_admin):
            query['isAdmin'] = request.is_admin
        if not DaraCore.is_null(request.is_builtin):
            query['isBuiltin'] = request.is_builtin
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.request_id):
            query['requestId'] = request.request_id
        if not DaraCore.is_null(request.template_name):
            query['templateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckTemplateList',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/template/v3/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_check_template_list_with_options_async(
        self,
        tmp_req: main_models.GetDataCheckTemplateListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDataCheckTemplateListResponse:
        tmp_req.validate()
        request = main_models.GetDataCheckTemplateListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.id_list):
            request.id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.id_list, 'idList', 'json')
        query = {}
        if not DaraCore.is_null(request.check_type):
            query['checkType'] = request.check_type
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.id_list_shrink):
            query['idList'] = request.id_list_shrink
        if not DaraCore.is_null(request.is_admin):
            query['isAdmin'] = request.is_admin
        if not DaraCore.is_null(request.is_builtin):
            query['isBuiltin'] = request.is_builtin
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.request_id):
            query['requestId'] = request.request_id
        if not DaraCore.is_null(request.template_name):
            query['templateName'] = request.template_name
        if not DaraCore.is_null(request.tenant_id):
            query['tenantId'] = request.tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataCheckTemplateList',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/template/v3/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataCheckTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_check_template_list(
        self,
        request: main_models.GetDataCheckTemplateListRequest,
    ) -> main_models.GetDataCheckTemplateListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_data_check_template_list_with_options(request, headers, runtime)

    async def get_data_check_template_list_async(
        self,
        request: main_models.GetDataCheckTemplateListRequest,
    ) -> main_models.GetDataCheckTemplateListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_data_check_template_list_with_options_async(request, headers, runtime)

    def get_inner_convert_async_result_with_options(
        self,
        request: main_models.GetInnerConvertAsyncResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInnerConvertAsyncResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInnerConvertAsyncResult',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/skill/inner/v1/convert/async-result',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInnerConvertAsyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inner_convert_async_result_with_options_async(
        self,
        request: main_models.GetInnerConvertAsyncResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInnerConvertAsyncResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInnerConvertAsyncResult',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/skill/inner/v1/convert/async-result',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInnerConvertAsyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inner_convert_async_result(
        self,
        request: main_models.GetInnerConvertAsyncResultRequest,
    ) -> main_models.GetInnerConvertAsyncResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_inner_convert_async_result_with_options(request, headers, runtime)

    async def get_inner_convert_async_result_async(
        self,
        request: main_models.GetInnerConvertAsyncResultRequest,
    ) -> main_models.GetInnerConvertAsyncResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_inner_convert_async_result_with_options_async(request, headers, runtime)

    def get_inner_read_async_result_with_options(
        self,
        request: main_models.GetInnerReadAsyncResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInnerReadAsyncResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInnerReadAsyncResult',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/skill/inner/v1/read/async-result',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInnerReadAsyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inner_read_async_result_with_options_async(
        self,
        request: main_models.GetInnerReadAsyncResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInnerReadAsyncResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetInnerReadAsyncResult',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/skill/inner/v1/read/async-result',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInnerReadAsyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inner_read_async_result(
        self,
        request: main_models.GetInnerReadAsyncResultRequest,
    ) -> main_models.GetInnerReadAsyncResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_inner_read_async_result_with_options(request, headers, runtime)

    async def get_inner_read_async_result_async(
        self,
        request: main_models.GetInnerReadAsyncResultRequest,
    ) -> main_models.GetInnerReadAsyncResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_inner_read_async_result_with_options_async(request, headers, runtime)

    def get_lhm_agent_status_with_options(
        self,
        request: main_models.GetLhmAgentStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLhmAgentStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['agentType'] = request.agent_type
        if not DaraCore.is_null(request.skill_name):
            query['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLhmAgentStatus',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/lhm/agent/getAgentStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLhmAgentStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lhm_agent_status_with_options_async(
        self,
        request: main_models.GetLhmAgentStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLhmAgentStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['agentType'] = request.agent_type
        if not DaraCore.is_null(request.skill_name):
            query['skillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLhmAgentStatus',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/lhm/agent/getAgentStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLhmAgentStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lhm_agent_status(
        self,
        request: main_models.GetLhmAgentStatusRequest,
    ) -> main_models.GetLhmAgentStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_lhm_agent_status_with_options(request, headers, runtime)

    async def get_lhm_agent_status_async(
        self,
        request: main_models.GetLhmAgentStatusRequest,
    ) -> main_models.GetLhmAgentStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_lhm_agent_status_with_options_async(request, headers, runtime)

    def get_lhm_dwresource_group_status_with_options(
        self,
        request: main_models.GetLhmDWResourceGroupStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLhmDWResourceGroupStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLhmDWResourceGroupStatus',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/lhm/resource/getDWResourceGroupStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLhmDWResourceGroupStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lhm_dwresource_group_status_with_options_async(
        self,
        request: main_models.GetLhmDWResourceGroupStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLhmDWResourceGroupStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLhmDWResourceGroupStatus',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/lhm/resource/getDWResourceGroupStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLhmDWResourceGroupStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lhm_dwresource_group_status(
        self,
        request: main_models.GetLhmDWResourceGroupStatusRequest,
    ) -> main_models.GetLhmDWResourceGroupStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_lhm_dwresource_group_status_with_options(request, headers, runtime)

    async def get_lhm_dwresource_group_status_async(
        self,
        request: main_models.GetLhmDWResourceGroupStatusRequest,
    ) -> main_models.GetLhmDWResourceGroupStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_lhm_dwresource_group_status_with_options_async(request, headers, runtime)

    def get_meta_oss_temp_key_with_options(
        self,
        request: main_models.GetMetaOssTempKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMetaOssTempKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMetaOssTempKey',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/v2/meta/data-component/okss-services/file-job/sts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetaOssTempKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_meta_oss_temp_key_with_options_async(
        self,
        request: main_models.GetMetaOssTempKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMetaOssTempKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMetaOssTempKey',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/v2/meta/data-component/okss-services/file-job/sts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMetaOssTempKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_meta_oss_temp_key(
        self,
        request: main_models.GetMetaOssTempKeyRequest,
    ) -> main_models.GetMetaOssTempKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_meta_oss_temp_key_with_options(request, headers, runtime)

    async def get_meta_oss_temp_key_async(
        self,
        request: main_models.GetMetaOssTempKeyRequest,
    ) -> main_models.GetMetaOssTempKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_meta_oss_temp_key_with_options_async(request, headers, runtime)

    def get_sql_conversion_progress_with_options(
        self,
        request: main_models.GetSqlConversionProgressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlConversionProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlConversionProgress',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/jobMigrate/sqlTranslator/task/api/progress',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlConversionProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_conversion_progress_with_options_async(
        self,
        request: main_models.GetSqlConversionProgressRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlConversionProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlConversionProgress',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/jobMigrate/sqlTranslator/task/api/progress',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlConversionProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_conversion_progress(
        self,
        request: main_models.GetSqlConversionProgressRequest,
    ) -> main_models.GetSqlConversionProgressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sql_conversion_progress_with_options(request, headers, runtime)

    async def get_sql_conversion_progress_async(
        self,
        request: main_models.GetSqlConversionProgressRequest,
    ) -> main_models.GetSqlConversionProgressResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sql_conversion_progress_with_options_async(request, headers, runtime)

    def get_sql_conversion_result_with_options(
        self,
        request: main_models.GetSqlConversionResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlConversionResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.size):
            body['size'] = request.size
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlConversionResult',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/jobMigrate/sqlTranslator/task/api/result',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlConversionResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_conversion_result_with_options_async(
        self,
        request: main_models.GetSqlConversionResultRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlConversionResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.size):
            body['size'] = request.size
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlConversionResult',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/jobMigrate/sqlTranslator/task/api/result',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlConversionResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_conversion_result(
        self,
        request: main_models.GetSqlConversionResultRequest,
    ) -> main_models.GetSqlConversionResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sql_conversion_result_with_options(request, headers, runtime)

    async def get_sql_conversion_result_async(
        self,
        request: main_models.GetSqlConversionResultRequest,
    ) -> main_models.GetSqlConversionResultResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sql_conversion_result_with_options_async(request, headers, runtime)

    def get_sql_table_lineage_with_options(
        self,
        request: main_models.GetSqlTableLineageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlTableLineageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default_schema):
            body['defaultSchema'] = request.default_schema
        if not DaraCore.is_null(request.dialect):
            body['dialect'] = request.dialect
        if not DaraCore.is_null(request.source_sql_script_base_64):
            body['sourceSqlScriptBase64'] = request.source_sql_script_base_64
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlTableLineage',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/open/single/getTableLineage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlTableLineageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_table_lineage_with_options_async(
        self,
        request: main_models.GetSqlTableLineageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlTableLineageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.default_schema):
            body['defaultSchema'] = request.default_schema
        if not DaraCore.is_null(request.dialect):
            body['dialect'] = request.dialect
        if not DaraCore.is_null(request.source_sql_script_base_64):
            body['sourceSqlScriptBase64'] = request.source_sql_script_base_64
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlTableLineage',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/open/single/getTableLineage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlTableLineageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_table_lineage(
        self,
        request: main_models.GetSqlTableLineageRequest,
    ) -> main_models.GetSqlTableLineageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sql_table_lineage_with_options(request, headers, runtime)

    async def get_sql_table_lineage_async(
        self,
        request: main_models.GetSqlTableLineageRequest,
    ) -> main_models.GetSqlTableLineageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sql_table_lineage_with_options_async(request, headers, runtime)

    def get_sql_trans_table_meta_info_with_options(
        self,
        request: main_models.GetSqlTransTableMetaInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlTransTableMetaInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.source_dialect):
            body['sourceDialect'] = request.source_dialect
        if not DaraCore.is_null(request.source_sql_script):
            body['sourceSqlScript'] = request.source_sql_script
        if not DaraCore.is_null(request.target_dialect):
            body['targetDialect'] = request.target_dialect
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlTransTableMetaInfo',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/open/single/get-table-info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlTransTableMetaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sql_trans_table_meta_info_with_options_async(
        self,
        request: main_models.GetSqlTransTableMetaInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSqlTransTableMetaInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.source_dialect):
            body['sourceDialect'] = request.source_dialect
        if not DaraCore.is_null(request.source_sql_script):
            body['sourceSqlScript'] = request.source_sql_script
        if not DaraCore.is_null(request.target_dialect):
            body['targetDialect'] = request.target_dialect
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetSqlTransTableMetaInfo',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/open/single/get-table-info',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSqlTransTableMetaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sql_trans_table_meta_info(
        self,
        request: main_models.GetSqlTransTableMetaInfoRequest,
    ) -> main_models.GetSqlTransTableMetaInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_sql_trans_table_meta_info_with_options(request, headers, runtime)

    async def get_sql_trans_table_meta_info_async(
        self,
        request: main_models.GetSqlTransTableMetaInfoRequest,
    ) -> main_models.GetSqlTransTableMetaInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_sql_trans_table_meta_info_with_options_async(request, headers, runtime)

    def get_step_result_overview_with_options(
        self,
        request: main_models.GetStepResultOverviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStepResultOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.result_id):
            query['resultId'] = request.result_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStepResultOverview',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/result/overview',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStepResultOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_step_result_overview_with_options_async(
        self,
        request: main_models.GetStepResultOverviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStepResultOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.result_id):
            query['resultId'] = request.result_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStepResultOverview',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/result/overview',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStepResultOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_step_result_overview(
        self,
        request: main_models.GetStepResultOverviewRequest,
    ) -> main_models.GetStepResultOverviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_step_result_overview_with_options(request, headers, runtime)

    async def get_step_result_overview_async(
        self,
        request: main_models.GetStepResultOverviewRequest,
    ) -> main_models.GetStepResultOverviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_step_result_overview_with_options_async(request, headers, runtime)

    def list_data_check_column_results_with_options(
        self,
        request: main_models.ListDataCheckColumnResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckColumnResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.result_id):
            query['resultId'] = request.result_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckColumnResults',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/column/page',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckColumnResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_check_column_results_with_options_async(
        self,
        request: main_models.ListDataCheckColumnResultsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckColumnResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.result_id):
            query['resultId'] = request.result_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckColumnResults',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/column/page',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckColumnResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_check_column_results(
        self,
        request: main_models.ListDataCheckColumnResultsRequest,
    ) -> main_models.ListDataCheckColumnResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_check_column_results_with_options(request, headers, runtime)

    async def list_data_check_column_results_async(
        self,
        request: main_models.ListDataCheckColumnResultsRequest,
    ) -> main_models.ListDataCheckColumnResultsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_check_column_results_with_options_async(request, headers, runtime)

    def list_data_check_config_with_options(
        self,
        request: main_models.ListDataCheckConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.src_table):
            query['srcTable'] = request.src_table
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckConfig',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/config/v3/listConfig/page',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_check_config_with_options_async(
        self,
        request: main_models.ListDataCheckConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.src_table):
            query['srcTable'] = request.src_table
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckConfig',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/config/v3/listConfig/page',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_check_config(
        self,
        request: main_models.ListDataCheckConfigRequest,
    ) -> main_models.ListDataCheckConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_check_config_with_options(request, headers, runtime)

    async def list_data_check_config_async(
        self,
        request: main_models.ListDataCheckConfigRequest,
    ) -> main_models.ListDataCheckConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_check_config_with_options_async(request, headers, runtime)

    def list_data_check_report_with_options(
        self,
        request: main_models.ListDataCheckReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        if not DaraCore.is_null(request.check_result):
            body['checkResult'] = request.check_result
        if not DaraCore.is_null(request.job_status):
            body['jobStatus'] = request.job_status
        if not DaraCore.is_null(request.page_index):
            body['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.table_name):
            body['tableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckReport',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/page',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_check_report_with_options_async(
        self,
        request: main_models.ListDataCheckReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckReportResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.batch_id):
            body['batchId'] = request.batch_id
        if not DaraCore.is_null(request.check_result):
            body['checkResult'] = request.check_result
        if not DaraCore.is_null(request.job_status):
            body['jobStatus'] = request.job_status
        if not DaraCore.is_null(request.page_index):
            body['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.table_name):
            body['tableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckReport',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/page',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_check_report(
        self,
        request: main_models.ListDataCheckReportRequest,
    ) -> main_models.ListDataCheckReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_check_report_with_options(request, headers, runtime)

    async def list_data_check_report_async(
        self,
        request: main_models.ListDataCheckReportRequest,
    ) -> main_models.ListDataCheckReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_check_report_with_options_async(request, headers, runtime)

    def list_data_check_report_instance_with_options(
        self,
        request: main_models.ListDataCheckReportInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckReportInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckReportInstance',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckReportInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_check_report_instance_with_options_async(
        self,
        request: main_models.ListDataCheckReportInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckReportInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckReportInstance',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckReportInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_check_report_instance(
        self,
        request: main_models.ListDataCheckReportInstanceRequest,
    ) -> main_models.ListDataCheckReportInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_check_report_instance_with_options(request, headers, runtime)

    async def list_data_check_report_instance_async(
        self,
        request: main_models.ListDataCheckReportInstanceRequest,
    ) -> main_models.ListDataCheckReportInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_check_report_instance_with_options_async(request, headers, runtime)

    def list_data_check_report_step_with_options(
        self,
        request: main_models.ListDataCheckReportStepRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckReportStepResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_result):
            query['checkResult'] = request.check_result
        if not DaraCore.is_null(request.job_id):
            query['jobId'] = request.job_id
        if not DaraCore.is_null(request.job_status):
            query['jobStatus'] = request.job_status
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckReportStep',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/step/page',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckReportStepResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_check_report_step_with_options_async(
        self,
        request: main_models.ListDataCheckReportStepRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckReportStepResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_result):
            query['checkResult'] = request.check_result
        if not DaraCore.is_null(request.job_id):
            query['jobId'] = request.job_id
        if not DaraCore.is_null(request.job_status):
            query['jobStatus'] = request.job_status
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckReportStep',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/step/page',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckReportStepResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_check_report_step(
        self,
        request: main_models.ListDataCheckReportStepRequest,
    ) -> main_models.ListDataCheckReportStepResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_check_report_step_with_options(request, headers, runtime)

    async def list_data_check_report_step_async(
        self,
        request: main_models.ListDataCheckReportStepRequest,
    ) -> main_models.ListDataCheckReportStepResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_check_report_step_with_options_async(request, headers, runtime)

    def list_data_check_report_step_by_job_id_with_options(
        self,
        request: main_models.ListDataCheckReportStepByJobIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckReportStepByJobIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['jobId'] = request.job_id
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckReportStepByJobId',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/step/pageByJobId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckReportStepByJobIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_check_report_step_by_job_id_with_options_async(
        self,
        request: main_models.ListDataCheckReportStepByJobIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckReportStepByJobIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['jobId'] = request.job_id
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckReportStepByJobId',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/report/v3/step/pageByJobId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckReportStepByJobIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_check_report_step_by_job_id(
        self,
        request: main_models.ListDataCheckReportStepByJobIdRequest,
    ) -> main_models.ListDataCheckReportStepByJobIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_check_report_step_by_job_id_with_options(request, headers, runtime)

    async def list_data_check_report_step_by_job_id_async(
        self,
        request: main_models.ListDataCheckReportStepByJobIdRequest,
    ) -> main_models.ListDataCheckReportStepByJobIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_check_report_step_by_job_id_with_options_async(request, headers, runtime)

    def list_data_check_task_history_with_options(
        self,
        request: main_models.ListDataCheckTaskHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckTaskHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['batchId'] = request.batch_id
        if not DaraCore.is_null(request.check_result):
            query['checkResult'] = request.check_result
        if not DaraCore.is_null(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not DaraCore.is_null(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not DaraCore.is_null(request.exec_end_time):
            query['execEndTime'] = request.exec_end_time
        if not DaraCore.is_null(request.exec_start_time):
            query['execStartTime'] = request.exec_start_time
        if not DaraCore.is_null(request.exec_status):
            query['execStatus'] = request.exec_status
        if not DaraCore.is_null(request.finish_end_time):
            query['finishEndTime'] = request.finish_end_time
        if not DaraCore.is_null(request.finish_start_time):
            query['finishStartTime'] = request.finish_start_time
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckTaskHistory',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckTaskHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_check_task_history_with_options_async(
        self,
        request: main_models.ListDataCheckTaskHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCheckTaskHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_id):
            query['batchId'] = request.batch_id
        if not DaraCore.is_null(request.check_result):
            query['checkResult'] = request.check_result
        if not DaraCore.is_null(request.create_end_time):
            query['createEndTime'] = request.create_end_time
        if not DaraCore.is_null(request.create_start_time):
            query['createStartTime'] = request.create_start_time
        if not DaraCore.is_null(request.exec_end_time):
            query['execEndTime'] = request.exec_end_time
        if not DaraCore.is_null(request.exec_start_time):
            query['execStartTime'] = request.exec_start_time
        if not DaraCore.is_null(request.exec_status):
            query['execStatus'] = request.exec_status
        if not DaraCore.is_null(request.finish_end_time):
            query['finishEndTime'] = request.finish_end_time
        if not DaraCore.is_null(request.finish_start_time):
            query['finishStartTime'] = request.finish_start_time
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCheckTaskHistory',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCheckTaskHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_check_task_history(
        self,
        request: main_models.ListDataCheckTaskHistoryRequest,
    ) -> main_models.ListDataCheckTaskHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_check_task_history_with_options(request, headers, runtime)

    async def list_data_check_task_history_async(
        self,
        request: main_models.ListDataCheckTaskHistoryRequest,
    ) -> main_models.ListDataCheckTaskHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_check_task_history_with_options_async(request, headers, runtime)

    def list_meta_data_component_page_with_options(
        self,
        request: main_models.ListMetaDataComponentPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMetaDataComponentPageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_type):
            body['categoryType'] = request.category_type
        if not DaraCore.is_null(request.component_type):
            body['componentType'] = request.component_type
        if not DaraCore.is_null(request.ds_name):
            body['dsName'] = request.ds_name
        if not DaraCore.is_null(request.ds_status):
            body['dsStatus'] = request.ds_status
        if not DaraCore.is_null(request.ds_type):
            body['dsType'] = request.ds_type
        if not DaraCore.is_null(request.ds_type_list):
            body['dsTypeList'] = request.ds_type_list
        if not DaraCore.is_null(request.group_by):
            body['groupBy'] = request.group_by
        if not DaraCore.is_null(request.need_total_count):
            body['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.order_by):
            body['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            body['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            body['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.src_component_id):
            body['srcComponentId'] = request.src_component_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMetaDataComponentPage',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/v2/meta/data-component/page',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMetaDataComponentPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_meta_data_component_page_with_options_async(
        self,
        request: main_models.ListMetaDataComponentPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMetaDataComponentPageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.category_type):
            body['categoryType'] = request.category_type
        if not DaraCore.is_null(request.component_type):
            body['componentType'] = request.component_type
        if not DaraCore.is_null(request.ds_name):
            body['dsName'] = request.ds_name
        if not DaraCore.is_null(request.ds_status):
            body['dsStatus'] = request.ds_status
        if not DaraCore.is_null(request.ds_type):
            body['dsType'] = request.ds_type
        if not DaraCore.is_null(request.ds_type_list):
            body['dsTypeList'] = request.ds_type_list
        if not DaraCore.is_null(request.group_by):
            body['groupBy'] = request.group_by
        if not DaraCore.is_null(request.need_total_count):
            body['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.order_by):
            body['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            body['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            body['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.src_component_id):
            body['srcComponentId'] = request.src_component_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMetaDataComponentPage',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/v2/meta/data-component/page',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMetaDataComponentPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_meta_data_component_page(
        self,
        request: main_models.ListMetaDataComponentPageRequest,
    ) -> main_models.ListMetaDataComponentPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_meta_data_component_page_with_options(request, headers, runtime)

    async def list_meta_data_component_page_async(
        self,
        request: main_models.ListMetaDataComponentPageRequest,
    ) -> main_models.ListMetaDataComponentPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_meta_data_component_page_with_options_async(request, headers, runtime)

    def post_inner_convert_with_options(
        self,
        request: main_models.PostInnerConvertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PostInnerConvertResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.sql_convert_map):
            body['sqlConvertMap'] = request.sql_convert_map
        if not DaraCore.is_null(request.src_data_source_name):
            body['srcDataSourceName'] = request.src_data_source_name
        if not DaraCore.is_null(request.tgt_data_source_name):
            body['tgtDataSourceName'] = request.tgt_data_source_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostInnerConvert',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/skill/inner/v1/convert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostInnerConvertResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_inner_convert_with_options_async(
        self,
        request: main_models.PostInnerConvertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PostInnerConvertResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.sql_convert_map):
            body['sqlConvertMap'] = request.sql_convert_map
        if not DaraCore.is_null(request.src_data_source_name):
            body['srcDataSourceName'] = request.src_data_source_name
        if not DaraCore.is_null(request.tgt_data_source_name):
            body['tgtDataSourceName'] = request.tgt_data_source_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostInnerConvert',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/skill/inner/v1/convert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostInnerConvertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_inner_convert(
        self,
        request: main_models.PostInnerConvertRequest,
    ) -> main_models.PostInnerConvertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.post_inner_convert_with_options(request, headers, runtime)

    async def post_inner_convert_async(
        self,
        request: main_models.PostInnerConvertRequest,
    ) -> main_models.PostInnerConvertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.post_inner_convert_with_options_async(request, headers, runtime)

    def post_inner_reader_with_options(
        self,
        request: main_models.PostInnerReaderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PostInnerReaderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source_descriptor):
            body['dataSourceDescriptor'] = request.data_source_descriptor
        if not DaraCore.is_null(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostInnerReader',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/skill/inner/v1/read',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostInnerReaderResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_inner_reader_with_options_async(
        self,
        request: main_models.PostInnerReaderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PostInnerReaderResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source_descriptor):
            body['dataSourceDescriptor'] = request.data_source_descriptor
        if not DaraCore.is_null(request.data_source_name):
            body['dataSourceName'] = request.data_source_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostInnerReader',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/skill/inner/v1/read',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostInnerReaderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_inner_reader(
        self,
        request: main_models.PostInnerReaderRequest,
    ) -> main_models.PostInnerReaderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.post_inner_reader_with_options(request, headers, runtime)

    async def post_inner_reader_async(
        self,
        request: main_models.PostInnerReaderRequest,
    ) -> main_models.PostInnerReaderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.post_inner_reader_with_options_async(request, headers, runtime)

    def post_inner_upload_convert_package_with_options(
        self,
        request: main_models.PostInnerUploadConvertPackageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PostInnerUploadConvertPackageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_content_base_64):
            body['fileContentBase64'] = request.file_content_base_64
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostInnerUploadConvertPackage',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/skill/inner/v1/convert/upload-package',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostInnerUploadConvertPackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def post_inner_upload_convert_package_with_options_async(
        self,
        request: main_models.PostInnerUploadConvertPackageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PostInnerUploadConvertPackageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_content_base_64):
            body['fileContentBase64'] = request.file_content_base_64
        if not DaraCore.is_null(request.file_name):
            body['fileName'] = request.file_name
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PostInnerUploadConvertPackage',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/skill/inner/v1/convert/upload-package',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PostInnerUploadConvertPackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def post_inner_upload_convert_package(
        self,
        request: main_models.PostInnerUploadConvertPackageRequest,
    ) -> main_models.PostInnerUploadConvertPackageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.post_inner_upload_convert_package_with_options(request, headers, runtime)

    async def post_inner_upload_convert_package_async(
        self,
        request: main_models.PostInnerUploadConvertPackageRequest,
    ) -> main_models.PostInnerUploadConvertPackageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.post_inner_upload_convert_package_with_options_async(request, headers, runtime)

    def single_sql_dry_run_with_options(
        self,
        request: main_models.SingleSqlDryRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SingleSqlDryRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.datasource_name):
            body['datasourceName'] = request.datasource_name
        if not DaraCore.is_null(request.sql):
            body['sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SingleSqlDryRun',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/dryRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SingleSqlDryRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def single_sql_dry_run_with_options_async(
        self,
        request: main_models.SingleSqlDryRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SingleSqlDryRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.datasource_name):
            body['datasourceName'] = request.datasource_name
        if not DaraCore.is_null(request.sql):
            body['sql'] = request.sql
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SingleSqlDryRun',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/sql-translator/dryRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SingleSqlDryRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def single_sql_dry_run(
        self,
        request: main_models.SingleSqlDryRunRequest,
    ) -> main_models.SingleSqlDryRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.single_sql_dry_run_with_options(request, headers, runtime)

    async def single_sql_dry_run_async(
        self,
        request: main_models.SingleSqlDryRunRequest,
    ) -> main_models.SingleSqlDryRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.single_sql_dry_run_with_options_async(request, headers, runtime)

    def syntax_check_and_transform_sql_conversion_task_with_options(
        self,
        request: main_models.SyntaxCheckAndTransformSqlConversionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyntaxCheckAndTransformSqlConversionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyntaxCheckAndTransformSqlConversionTask',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/jobMigrate/sqlTranslator/task/api/syntaxCheckAndTransformTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyntaxCheckAndTransformSqlConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def syntax_check_and_transform_sql_conversion_task_with_options_async(
        self,
        request: main_models.SyntaxCheckAndTransformSqlConversionTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyntaxCheckAndTransformSqlConversionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyntaxCheckAndTransformSqlConversionTask',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/api/bigdata/jobMigrate/sqlTranslator/task/api/syntaxCheckAndTransformTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyntaxCheckAndTransformSqlConversionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def syntax_check_and_transform_sql_conversion_task(
        self,
        request: main_models.SyntaxCheckAndTransformSqlConversionTaskRequest,
    ) -> main_models.SyntaxCheckAndTransformSqlConversionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.syntax_check_and_transform_sql_conversion_task_with_options(request, headers, runtime)

    async def syntax_check_and_transform_sql_conversion_task_async(
        self,
        request: main_models.SyntaxCheckAndTransformSqlConversionTaskRequest,
    ) -> main_models.SyntaxCheckAndTransformSqlConversionTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.syntax_check_and_transform_sql_conversion_task_with_options_async(request, headers, runtime)

    def update_data_check_task_with_options(
        self,
        request: main_models.UpdateDataCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataCheckTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_template_id):
            body['checkTemplateId'] = request.check_template_id
        if not DaraCore.is_null(request.dst_ds_id):
            body['dstDsId'] = request.dst_ds_id
        if not DaraCore.is_null(request.dst_ds_name):
            body['dstDsName'] = request.dst_ds_name
        if not DaraCore.is_null(request.dst_ds_type):
            body['dstDsType'] = request.dst_ds_type
        if not DaraCore.is_null(request.dst_engine_id):
            body['dstEngineId'] = request.dst_engine_id
        if not DaraCore.is_null(request.dst_engine_name):
            body['dstEngineName'] = request.dst_engine_name
        if not DaraCore.is_null(request.dst_engine_type):
            body['dstEngineType'] = request.dst_engine_type
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.src_ds_id):
            body['srcDsId'] = request.src_ds_id
        if not DaraCore.is_null(request.src_ds_name):
            body['srcDsName'] = request.src_ds_name
        if not DaraCore.is_null(request.src_ds_type):
            body['srcDsType'] = request.src_ds_type
        if not DaraCore.is_null(request.src_engine_id):
            body['srcEngineId'] = request.src_engine_id
        if not DaraCore.is_null(request.src_engine_name):
            body['srcEngineName'] = request.src_engine_name
        if not DaraCore.is_null(request.src_engine_type):
            body['srcEngineType'] = request.src_engine_type
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataCheckTask',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_check_task_with_options_async(
        self,
        request: main_models.UpdateDataCheckTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataCheckTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.check_template_id):
            body['checkTemplateId'] = request.check_template_id
        if not DaraCore.is_null(request.dst_ds_id):
            body['dstDsId'] = request.dst_ds_id
        if not DaraCore.is_null(request.dst_ds_name):
            body['dstDsName'] = request.dst_ds_name
        if not DaraCore.is_null(request.dst_ds_type):
            body['dstDsType'] = request.dst_ds_type
        if not DaraCore.is_null(request.dst_engine_id):
            body['dstEngineId'] = request.dst_engine_id
        if not DaraCore.is_null(request.dst_engine_name):
            body['dstEngineName'] = request.dst_engine_name
        if not DaraCore.is_null(request.dst_engine_type):
            body['dstEngineType'] = request.dst_engine_type
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.src_ds_id):
            body['srcDsId'] = request.src_ds_id
        if not DaraCore.is_null(request.src_ds_name):
            body['srcDsName'] = request.src_ds_name
        if not DaraCore.is_null(request.src_ds_type):
            body['srcDsType'] = request.src_ds_type
        if not DaraCore.is_null(request.src_engine_id):
            body['srcEngineId'] = request.src_engine_id
        if not DaraCore.is_null(request.src_engine_name):
            body['srcEngineName'] = request.src_engine_name
        if not DaraCore.is_null(request.src_engine_type):
            body['srcEngineType'] = request.src_engine_type
        if not DaraCore.is_null(request.task_description):
            body['taskDescription'] = request.task_description
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataCheckTask',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/task/v3/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_check_task(
        self,
        request: main_models.UpdateDataCheckTaskRequest,
    ) -> main_models.UpdateDataCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_data_check_task_with_options(request, headers, runtime)

    async def update_data_check_task_async(
        self,
        request: main_models.UpdateDataCheckTaskRequest,
    ) -> main_models.UpdateDataCheckTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_data_check_task_with_options_async(request, headers, runtime)

    def update_data_check_template_with_options(
        self,
        request: main_models.UpdateDataCheckTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataCheckTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.basic_metric_rules):
            body['basicMetricRules'] = request.basic_metric_rules
        if not DaraCore.is_null(request.check_type):
            body['checkType'] = request.check_type
        if not DaraCore.is_null(request.complex_metric_rules):
            body['complexMetricRules'] = request.complex_metric_rules
        if not DaraCore.is_null(request.ds_engine_rels):
            body['dsEngineRels'] = request.ds_engine_rels
        if not DaraCore.is_null(request.fulltext_rule):
            body['fulltextRule'] = request.fulltext_rule
        if not DaraCore.is_null(request.metric_rules):
            body['metricRules'] = request.metric_rules
        if not DaraCore.is_null(request.null_rules):
            body['nullRules'] = request.null_rules
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.template_desc):
            body['templateDesc'] = request.template_desc
        if not DaraCore.is_null(request.template_id):
            body['templateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            body['templateName'] = request.template_name
        if not DaraCore.is_null(request.weak_content_rule):
            body['weakContentRule'] = request.weak_content_rule
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataCheckTemplate',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/template/v3/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataCheckTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_check_template_with_options_async(
        self,
        request: main_models.UpdateDataCheckTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataCheckTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.basic_metric_rules):
            body['basicMetricRules'] = request.basic_metric_rules
        if not DaraCore.is_null(request.check_type):
            body['checkType'] = request.check_type
        if not DaraCore.is_null(request.complex_metric_rules):
            body['complexMetricRules'] = request.complex_metric_rules
        if not DaraCore.is_null(request.ds_engine_rels):
            body['dsEngineRels'] = request.ds_engine_rels
        if not DaraCore.is_null(request.fulltext_rule):
            body['fulltextRule'] = request.fulltext_rule
        if not DaraCore.is_null(request.metric_rules):
            body['metricRules'] = request.metric_rules
        if not DaraCore.is_null(request.null_rules):
            body['nullRules'] = request.null_rules
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.template_desc):
            body['templateDesc'] = request.template_desc
        if not DaraCore.is_null(request.template_id):
            body['templateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            body['templateName'] = request.template_name
        if not DaraCore.is_null(request.weak_content_rule):
            body['weakContentRule'] = request.weak_content_rule
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataCheckTemplate',
            version = '2025-01-16',
            protocol = 'HTTPS',
            pathname = f'/dataCheck/template/v3/update',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataCheckTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_check_template(
        self,
        request: main_models.UpdateDataCheckTemplateRequest,
    ) -> main_models.UpdateDataCheckTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_data_check_template_with_options(request, headers, runtime)

    async def update_data_check_template_async(
        self,
        request: main_models.UpdateDataCheckTemplateRequest,
    ) -> main_models.UpdateDataCheckTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_data_check_template_with_options_async(request, headers, runtime)
