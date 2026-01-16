# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sddp20190103 import models as main_models
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
            'cn-hongkong': 'sddp-api.cn-hongkong.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('sddp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_config_with_options(
        self,
        request: main_models.CreateConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfig',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_config_with_options_async(
        self,
        request: main_models.CreateConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateConfig',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_config(
        self,
        request: main_models.CreateConfigRequest,
    ) -> main_models.CreateConfigResponse:
        runtime = RuntimeOptions()
        return self.create_config_with_options(request, runtime)

    async def create_config_async(
        self,
        request: main_models.CreateConfigRequest,
    ) -> main_models.CreateConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_config_with_options_async(request, runtime)

    def create_data_limit_with_options(
        self,
        request: main_models.CreateDataLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.auto_scan):
            query['AutoScan'] = request.auto_scan
        if not DaraCore.is_null(request.certificate_permission):
            query['CertificatePermission'] = request.certificate_permission
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.event_status):
            query['EventStatus'] = request.event_status
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.instantly_scan):
            query['InstantlyScan'] = request.instantly_scan
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.log_store_day):
            query['LogStoreDay'] = request.log_store_day
        if not DaraCore.is_null(request.ocr_status):
            query['OcrStatus'] = request.ocr_status
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sampling_size):
            query['SamplingSize'] = request.sampling_size
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataLimit',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_limit_with_options_async(
        self,
        request: main_models.CreateDataLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.auto_scan):
            query['AutoScan'] = request.auto_scan
        if not DaraCore.is_null(request.certificate_permission):
            query['CertificatePermission'] = request.certificate_permission
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.event_status):
            query['EventStatus'] = request.event_status
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.instantly_scan):
            query['InstantlyScan'] = request.instantly_scan
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.log_store_day):
            query['LogStoreDay'] = request.log_store_day
        if not DaraCore.is_null(request.ocr_status):
            query['OcrStatus'] = request.ocr_status
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sampling_size):
            query['SamplingSize'] = request.sampling_size
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataLimit',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_limit(
        self,
        request: main_models.CreateDataLimitRequest,
    ) -> main_models.CreateDataLimitResponse:
        runtime = RuntimeOptions()
        return self.create_data_limit_with_options(request, runtime)

    async def create_data_limit_async(
        self,
        request: main_models.CreateDataLimitRequest,
    ) -> main_models.CreateDataLimitResponse:
        runtime = RuntimeOptions()
        return await self.create_data_limit_with_options_async(request, runtime)

    def create_rule_with_options(
        self,
        request: main_models.CreateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.content_category):
            query['ContentCategory'] = request.content_category
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.model_rule_ids):
            query['ModelRuleIds'] = request.model_rule_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.stat_express):
            query['StatExpress'] = request.stat_express
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.support_form):
            query['SupportForm'] = request.support_form
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.template_rule_ids):
            query['TemplateRuleIds'] = request.template_rule_ids
        if not DaraCore.is_null(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRule',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: main_models.CreateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.content_category):
            query['ContentCategory'] = request.content_category
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.model_rule_ids):
            query['ModelRuleIds'] = request.model_rule_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.stat_express):
            query['StatExpress'] = request.stat_express
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.support_form):
            query['SupportForm'] = request.support_form
        if not DaraCore.is_null(request.target):
            query['Target'] = request.target
        if not DaraCore.is_null(request.template_rule_ids):
            query['TemplateRuleIds'] = request.template_rule_ids
        if not DaraCore.is_null(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRule',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rule(
        self,
        request: main_models.CreateRuleRequest,
    ) -> main_models.CreateRuleResponse:
        runtime = RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: main_models.CreateRuleRequest,
    ) -> main_models.CreateRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_scan_task_with_options(
        self,
        request: main_models.CreateScanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_limit_id):
            query['DataLimitId'] = request.data_limit_id
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.interval_day):
            query['IntervalDay'] = request.interval_day
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.oss_scan_path):
            query['OssScanPath'] = request.oss_scan_path
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.run_hour):
            query['RunHour'] = request.run_hour
        if not DaraCore.is_null(request.run_minute):
            query['RunMinute'] = request.run_minute
        if not DaraCore.is_null(request.scan_range):
            query['ScanRange'] = request.scan_range
        if not DaraCore.is_null(request.scan_range_content):
            query['ScanRangeContent'] = request.scan_range_content
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_user_name):
            query['TaskUserName'] = request.task_user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScanTask',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scan_task_with_options_async(
        self,
        request: main_models.CreateScanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_limit_id):
            query['DataLimitId'] = request.data_limit_id
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.interval_day):
            query['IntervalDay'] = request.interval_day
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.oss_scan_path):
            query['OssScanPath'] = request.oss_scan_path
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.run_hour):
            query['RunHour'] = request.run_hour
        if not DaraCore.is_null(request.run_minute):
            query['RunMinute'] = request.run_minute
        if not DaraCore.is_null(request.scan_range):
            query['ScanRange'] = request.scan_range
        if not DaraCore.is_null(request.scan_range_content):
            query['ScanRangeContent'] = request.scan_range_content
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_user_name):
            query['TaskUserName'] = request.task_user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScanTask',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scan_task(
        self,
        request: main_models.CreateScanTaskRequest,
    ) -> main_models.CreateScanTaskResponse:
        runtime = RuntimeOptions()
        return self.create_scan_task_with_options(request, runtime)

    async def create_scan_task_async(
        self,
        request: main_models.CreateScanTaskRequest,
    ) -> main_models.CreateScanTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_scan_task_with_options_async(request, runtime)

    def create_slr_role_with_options(
        self,
        request: main_models.CreateSlrRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSlrRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSlrRole',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSlrRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_slr_role_with_options_async(
        self,
        request: main_models.CreateSlrRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSlrRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSlrRole',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSlrRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_slr_role(
        self,
        request: main_models.CreateSlrRoleRequest,
    ) -> main_models.CreateSlrRoleResponse:
        runtime = RuntimeOptions()
        return self.create_slr_role_with_options(request, runtime)

    async def create_slr_role_async(
        self,
        request: main_models.CreateSlrRoleRequest,
    ) -> main_models.CreateSlrRoleResponse:
        runtime = RuntimeOptions()
        return await self.create_slr_role_with_options_async(request, runtime)

    def delete_data_limit_with_options(
        self,
        request: main_models.DeleteDataLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLimit',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_limit_with_options_async(
        self,
        request: main_models.DeleteDataLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataLimit',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_limit(
        self,
        request: main_models.DeleteDataLimitRequest,
    ) -> main_models.DeleteDataLimitResponse:
        runtime = RuntimeOptions()
        return self.delete_data_limit_with_options(request, runtime)

    async def delete_data_limit_async(
        self,
        request: main_models.DeleteDataLimitRequest,
    ) -> main_models.DeleteDataLimitResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_limit_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: main_models.DeleteRuleRequest,
    ) -> main_models.DeleteRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: main_models.DeleteRuleRequest,
    ) -> main_models.DeleteRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def describe_audit_logs_with_options(
        self,
        request: main_models.DescribeAuditLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_request_id):
            query['AsyncRequestId'] = request.async_request_id
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_ua):
            query['ClientUa'] = request.client_ua
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.effect_row_range):
            query['EffectRowRange'] = request.effect_row_range
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_time_range):
            query['ExecuteTimeRange'] = request.execute_time_range
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.ip_type):
            query['IpType'] = request.ip_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.load_white_list):
            query['LoadWhiteList'] = request.load_white_list
        if not DaraCore.is_null(request.log_query_op_json):
            query['LogQueryOpJson'] = request.log_query_op_json
        if not DaraCore.is_null(request.log_source):
            query['LogSource'] = request.log_source
        if not DaraCore.is_null(request.member_account):
            query['MemberAccount'] = request.member_account
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.oss_object_key):
            query['OssObjectKey'] = request.oss_object_key
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.rule_agg_query):
            query['RuleAggQuery'] = request.rule_agg_query
        if not DaraCore.is_null(request.rule_category):
            query['RuleCategory'] = request.rule_category
        if not DaraCore.is_null(request.rule_id):
            query['RuleID'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sql_text):
            query['SqlText'] = request.sql_text
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditLogs',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_logs_with_options_async(
        self,
        request: main_models.DescribeAuditLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.async_request_id):
            query['AsyncRequestId'] = request.async_request_id
        if not DaraCore.is_null(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not DaraCore.is_null(request.client_ua):
            query['ClientUa'] = request.client_ua
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.effect_row_range):
            query['EffectRowRange'] = request.effect_row_range
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_time_range):
            query['ExecuteTimeRange'] = request.execute_time_range
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.ip_type):
            query['IpType'] = request.ip_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.load_white_list):
            query['LoadWhiteList'] = request.load_white_list
        if not DaraCore.is_null(request.log_query_op_json):
            query['LogQueryOpJson'] = request.log_query_op_json
        if not DaraCore.is_null(request.log_source):
            query['LogSource'] = request.log_source
        if not DaraCore.is_null(request.member_account):
            query['MemberAccount'] = request.member_account
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.operate_type):
            query['OperateType'] = request.operate_type
        if not DaraCore.is_null(request.oss_object_key):
            query['OssObjectKey'] = request.oss_object_key
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.rule_agg_query):
            query['RuleAggQuery'] = request.rule_agg_query
        if not DaraCore.is_null(request.rule_category):
            query['RuleCategory'] = request.rule_category
        if not DaraCore.is_null(request.rule_id):
            query['RuleID'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sql_text):
            query['SqlText'] = request.sql_text
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditLogs',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_logs(
        self,
        request: main_models.DescribeAuditLogsRequest,
    ) -> main_models.DescribeAuditLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_audit_logs_with_options(request, runtime)

    async def describe_audit_logs_async(
        self,
        request: main_models.DescribeAuditLogsRequest,
    ) -> main_models.DescribeAuditLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_audit_logs_with_options_async(request, runtime)

    def describe_category_template_list_with_options(
        self,
        request: main_models.DescribeCategoryTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCategoryTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.usage_scenario):
            query['UsageScenario'] = request.usage_scenario
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCategoryTemplateList',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCategoryTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_category_template_list_with_options_async(
        self,
        request: main_models.DescribeCategoryTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCategoryTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.usage_scenario):
            query['UsageScenario'] = request.usage_scenario
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCategoryTemplateList',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCategoryTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_category_template_list(
        self,
        request: main_models.DescribeCategoryTemplateListRequest,
    ) -> main_models.DescribeCategoryTemplateListResponse:
        runtime = RuntimeOptions()
        return self.describe_category_template_list_with_options(request, runtime)

    async def describe_category_template_list_async(
        self,
        request: main_models.DescribeCategoryTemplateListRequest,
    ) -> main_models.DescribeCategoryTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_category_template_list_with_options_async(request, runtime)

    def describe_category_template_rule_list_with_options(
        self,
        request: main_models.DescribeCategoryTemplateRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCategoryTemplateRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCategoryTemplateRuleList',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCategoryTemplateRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_category_template_rule_list_with_options_async(
        self,
        request: main_models.DescribeCategoryTemplateRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCategoryTemplateRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCategoryTemplateRuleList',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCategoryTemplateRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_category_template_rule_list(
        self,
        request: main_models.DescribeCategoryTemplateRuleListRequest,
    ) -> main_models.DescribeCategoryTemplateRuleListResponse:
        runtime = RuntimeOptions()
        return self.describe_category_template_rule_list_with_options(request, runtime)

    async def describe_category_template_rule_list_async(
        self,
        request: main_models.DescribeCategoryTemplateRuleListRequest,
    ) -> main_models.DescribeCategoryTemplateRuleListResponse:
        runtime = RuntimeOptions()
        return await self.describe_category_template_rule_list_with_options_async(request, runtime)

    def describe_columns_with_options(
        self,
        request: main_models.DescribeColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.model_tag_id):
            query['ModelTagId'] = request.model_tag_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sens_level_name):
            query['SensLevelName'] = request.sens_level_name
        if not DaraCore.is_null(request.table_id):
            query['TableId'] = request.table_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_rule_id):
            query['TemplateRuleId'] = request.template_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumns',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columns_with_options_async(
        self,
        request: main_models.DescribeColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.model_tag_id):
            query['ModelTagId'] = request.model_tag_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sens_level_name):
            query['SensLevelName'] = request.sens_level_name
        if not DaraCore.is_null(request.table_id):
            query['TableId'] = request.table_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_rule_id):
            query['TemplateRuleId'] = request.template_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumns',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columns(
        self,
        request: main_models.DescribeColumnsRequest,
    ) -> main_models.DescribeColumnsResponse:
        runtime = RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    async def describe_columns_async(
        self,
        request: main_models.DescribeColumnsRequest,
    ) -> main_models.DescribeColumnsResponse:
        runtime = RuntimeOptions()
        return await self.describe_columns_with_options_async(request, runtime)

    def describe_columns_v2with_options(
        self,
        request: main_models.DescribeColumnsV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnsV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sens_level_name):
            query['SensLevelName'] = request.sens_level_name
        if not DaraCore.is_null(request.table_id):
            query['TableId'] = request.table_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumnsV2',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnsV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_columns_v2with_options_async(
        self,
        request: main_models.DescribeColumnsV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnsV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sens_level_name):
            query['SensLevelName'] = request.sens_level_name
        if not DaraCore.is_null(request.table_id):
            query['TableId'] = request.table_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumnsV2',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnsV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columns_v2(
        self,
        request: main_models.DescribeColumnsV2Request,
    ) -> main_models.DescribeColumnsV2Response:
        runtime = RuntimeOptions()
        return self.describe_columns_v2with_options(request, runtime)

    async def describe_columns_v2_async(
        self,
        request: main_models.DescribeColumnsV2Request,
    ) -> main_models.DescribeColumnsV2Response:
        runtime = RuntimeOptions()
        return await self.describe_columns_v2with_options_async(request, runtime)

    def describe_configs_with_options(
        self,
        request: main_models.DescribeConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigs',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_configs_with_options_async(
        self,
        request: main_models.DescribeConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigs',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_configs(
        self,
        request: main_models.DescribeConfigsRequest,
    ) -> main_models.DescribeConfigsResponse:
        runtime = RuntimeOptions()
        return self.describe_configs_with_options(request, runtime)

    async def describe_configs_async(
        self,
        request: main_models.DescribeConfigsRequest,
    ) -> main_models.DescribeConfigsResponse:
        runtime = RuntimeOptions()
        return await self.describe_configs_with_options_async(request, runtime)

    def describe_data_assets_with_options(
        self,
        request: main_models.DescribeDataAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataAssetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.range_id):
            query['RangeId'] = request.range_id
        if not DaraCore.is_null(request.risk_levels):
            query['RiskLevels'] = request.risk_levels
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataAssets',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_assets_with_options_async(
        self,
        request: main_models.DescribeDataAssetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataAssetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.range_id):
            query['RangeId'] = request.range_id
        if not DaraCore.is_null(request.risk_levels):
            query['RiskLevels'] = request.risk_levels
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataAssets',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_assets(
        self,
        request: main_models.DescribeDataAssetsRequest,
    ) -> main_models.DescribeDataAssetsResponse:
        runtime = RuntimeOptions()
        return self.describe_data_assets_with_options(request, runtime)

    async def describe_data_assets_async(
        self,
        request: main_models.DescribeDataAssetsRequest,
    ) -> main_models.DescribeDataAssetsResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_assets_with_options_async(request, runtime)

    def describe_data_limit_detail_with_options(
        self,
        request: main_models.DescribeDataLimitDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataLimitDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataLimitDetail',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataLimitDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_limit_detail_with_options_async(
        self,
        request: main_models.DescribeDataLimitDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataLimitDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataLimitDetail',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataLimitDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_limit_detail(
        self,
        request: main_models.DescribeDataLimitDetailRequest,
    ) -> main_models.DescribeDataLimitDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_data_limit_detail_with_options(request, runtime)

    async def describe_data_limit_detail_async(
        self,
        request: main_models.DescribeDataLimitDetailRequest,
    ) -> main_models.DescribeDataLimitDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_limit_detail_with_options_async(request, runtime)

    def describe_data_limit_set_with_options(
        self,
        request: main_models.DescribeDataLimitSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataLimitSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.region_type):
            query['RegionType'] = request.region_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataLimitSet',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataLimitSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_limit_set_with_options_async(
        self,
        request: main_models.DescribeDataLimitSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataLimitSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.region_type):
            query['RegionType'] = request.region_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataLimitSet',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataLimitSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_limit_set(
        self,
        request: main_models.DescribeDataLimitSetRequest,
    ) -> main_models.DescribeDataLimitSetResponse:
        runtime = RuntimeOptions()
        return self.describe_data_limit_set_with_options(request, runtime)

    async def describe_data_limit_set_async(
        self,
        request: main_models.DescribeDataLimitSetRequest,
    ) -> main_models.DescribeDataLimitSetResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_limit_set_with_options_async(request, runtime)

    def describe_data_limits_with_options(
        self,
        request: main_models.DescribeDataLimitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataLimitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.check_status):
            query['CheckStatus'] = request.check_status
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.datamask_status):
            query['DatamaskStatus'] = request.datamask_status
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_account):
            query['MemberAccount'] = request.member_account
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataLimits',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataLimitsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_limits_with_options_async(
        self,
        request: main_models.DescribeDataLimitsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataLimitsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.check_status):
            query['CheckStatus'] = request.check_status
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.datamask_status):
            query['DatamaskStatus'] = request.datamask_status
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_account):
            query['MemberAccount'] = request.member_account
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataLimits',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataLimitsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_limits(
        self,
        request: main_models.DescribeDataLimitsRequest,
    ) -> main_models.DescribeDataLimitsResponse:
        runtime = RuntimeOptions()
        return self.describe_data_limits_with_options(request, runtime)

    async def describe_data_limits_async(
        self,
        request: main_models.DescribeDataLimitsRequest,
    ) -> main_models.DescribeDataLimitsResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_limits_with_options_async(request, runtime)

    def describe_data_masking_run_history_with_options(
        self,
        request: main_models.DescribeDataMaskingRunHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataMaskingRunHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_type):
            query['DstType'] = request.dst_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.main_process_id):
            query['MainProcessId'] = request.main_process_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.src_table_name):
            query['SrcTableName'] = request.src_table_name
        if not DaraCore.is_null(request.src_type):
            query['SrcType'] = request.src_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataMaskingRunHistory',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataMaskingRunHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_masking_run_history_with_options_async(
        self,
        request: main_models.DescribeDataMaskingRunHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataMaskingRunHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_type):
            query['DstType'] = request.dst_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.main_process_id):
            query['MainProcessId'] = request.main_process_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.src_table_name):
            query['SrcTableName'] = request.src_table_name
        if not DaraCore.is_null(request.src_type):
            query['SrcType'] = request.src_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataMaskingRunHistory',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataMaskingRunHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_masking_run_history(
        self,
        request: main_models.DescribeDataMaskingRunHistoryRequest,
    ) -> main_models.DescribeDataMaskingRunHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_data_masking_run_history_with_options(request, runtime)

    async def describe_data_masking_run_history_async(
        self,
        request: main_models.DescribeDataMaskingRunHistoryRequest,
    ) -> main_models.DescribeDataMaskingRunHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_masking_run_history_with_options_async(request, runtime)

    def describe_data_masking_tasks_with_options(
        self,
        request: main_models.DescribeDataMaskingTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataMaskingTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_type):
            query['DstType'] = request.dst_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataMaskingTasks',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataMaskingTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_masking_tasks_with_options_async(
        self,
        request: main_models.DescribeDataMaskingTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataMaskingTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dst_type):
            query['DstType'] = request.dst_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataMaskingTasks',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataMaskingTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_masking_tasks(
        self,
        request: main_models.DescribeDataMaskingTasksRequest,
    ) -> main_models.DescribeDataMaskingTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_data_masking_tasks_with_options(request, runtime)

    async def describe_data_masking_tasks_async(
        self,
        request: main_models.DescribeDataMaskingTasksRequest,
    ) -> main_models.DescribeDataMaskingTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_masking_tasks_with_options_async(request, runtime)

    def describe_data_object_column_detail_with_options(
        self,
        request: main_models.DescribeDataObjectColumnDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataObjectColumnDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataObjectColumnDetail',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataObjectColumnDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_object_column_detail_with_options_async(
        self,
        request: main_models.DescribeDataObjectColumnDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataObjectColumnDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataObjectColumnDetail',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataObjectColumnDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_object_column_detail(
        self,
        request: main_models.DescribeDataObjectColumnDetailRequest,
    ) -> main_models.DescribeDataObjectColumnDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_data_object_column_detail_with_options(request, runtime)

    async def describe_data_object_column_detail_async(
        self,
        request: main_models.DescribeDataObjectColumnDetailRequest,
    ) -> main_models.DescribeDataObjectColumnDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_object_column_detail_with_options_async(request, runtime)

    def describe_data_object_column_detail_v2with_options(
        self,
        request: main_models.DescribeDataObjectColumnDetailV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataObjectColumnDetailV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataObjectColumnDetailV2',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataObjectColumnDetailV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_object_column_detail_v2with_options_async(
        self,
        request: main_models.DescribeDataObjectColumnDetailV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataObjectColumnDetailV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataObjectColumnDetailV2',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataObjectColumnDetailV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_object_column_detail_v2(
        self,
        request: main_models.DescribeDataObjectColumnDetailV2Request,
    ) -> main_models.DescribeDataObjectColumnDetailV2Response:
        runtime = RuntimeOptions()
        return self.describe_data_object_column_detail_v2with_options(request, runtime)

    async def describe_data_object_column_detail_v2_async(
        self,
        request: main_models.DescribeDataObjectColumnDetailV2Request,
    ) -> main_models.DescribeDataObjectColumnDetailV2Response:
        runtime = RuntimeOptions()
        return await self.describe_data_object_column_detail_v2with_options_async(request, runtime)

    def describe_data_objects_with_options(
        self,
        request: main_models.DescribeDataObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.file_category_code):
            query['FileCategoryCode'] = request.file_category_code
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_account):
            query['MemberAccount'] = request.member_account
        if not DaraCore.is_null(request.model_ids):
            query['ModelIds'] = request.model_ids
        if not DaraCore.is_null(request.model_tag_ids):
            query['ModelTagIds'] = request.model_tag_ids
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_category_ids):
            query['ParentCategoryIds'] = request.parent_category_ids
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        if not DaraCore.is_null(request.query_name):
            query['QueryName'] = request.query_name
        if not DaraCore.is_null(request.risk_levels):
            query['RiskLevels'] = request.risk_levels
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataObjects',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_objects_with_options_async(
        self,
        request: main_models.DescribeDataObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.domain_id):
            query['DomainId'] = request.domain_id
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.file_category_code):
            query['FileCategoryCode'] = request.file_category_code
        if not DaraCore.is_null(request.file_type):
            query['FileType'] = request.file_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_account):
            query['MemberAccount'] = request.member_account
        if not DaraCore.is_null(request.model_ids):
            query['ModelIds'] = request.model_ids
        if not DaraCore.is_null(request.model_tag_ids):
            query['ModelTagIds'] = request.model_tag_ids
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_category_ids):
            query['ParentCategoryIds'] = request.parent_category_ids
        if not DaraCore.is_null(request.product_ids):
            query['ProductIds'] = request.product_ids
        if not DaraCore.is_null(request.query_name):
            query['QueryName'] = request.query_name
        if not DaraCore.is_null(request.risk_levels):
            query['RiskLevels'] = request.risk_levels
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataObjects',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_objects(
        self,
        request: main_models.DescribeDataObjectsRequest,
    ) -> main_models.DescribeDataObjectsResponse:
        runtime = RuntimeOptions()
        return self.describe_data_objects_with_options(request, runtime)

    async def describe_data_objects_async(
        self,
        request: main_models.DescribeDataObjectsRequest,
    ) -> main_models.DescribeDataObjectsResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_objects_with_options_async(request, runtime)

    def describe_doc_types_with_options(
        self,
        request: main_models.DescribeDocTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocTypes',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_doc_types_with_options_async(
        self,
        request: main_models.DescribeDocTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocTypes',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_doc_types(
        self,
        request: main_models.DescribeDocTypesRequest,
    ) -> main_models.DescribeDocTypesResponse:
        runtime = RuntimeOptions()
        return self.describe_doc_types_with_options(request, runtime)

    async def describe_doc_types_async(
        self,
        request: main_models.DescribeDocTypesRequest,
    ) -> main_models.DescribeDocTypesResponse:
        runtime = RuntimeOptions()
        return await self.describe_doc_types_with_options_async(request, runtime)

    def describe_event_detail_with_options(
        self,
        request: main_models.DescribeEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventDetail',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_detail_with_options_async(
        self,
        request: main_models.DescribeEventDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventDetail',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_detail(
        self,
        request: main_models.DescribeEventDetailRequest,
    ) -> main_models.DescribeEventDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_event_detail_with_options(request, runtime)

    async def describe_event_detail_async(
        self,
        request: main_models.DescribeEventDetailRequest,
    ) -> main_models.DescribeEventDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_detail_with_options_async(request, runtime)

    def describe_event_types_with_options(
        self,
        request: main_models.DescribeEventTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.parent_type_id):
            query['ParentTypeId'] = request.parent_type_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventTypes',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_types_with_options_async(
        self,
        request: main_models.DescribeEventTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.parent_type_id):
            query['ParentTypeId'] = request.parent_type_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventTypes',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_types(
        self,
        request: main_models.DescribeEventTypesRequest,
    ) -> main_models.DescribeEventTypesResponse:
        runtime = RuntimeOptions()
        return self.describe_event_types_with_options(request, runtime)

    async def describe_event_types_async(
        self,
        request: main_models.DescribeEventTypesRequest,
    ) -> main_models.DescribeEventTypesResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_types_with_options_async(request, runtime)

    def describe_events_with_options(
        self,
        request: main_models.DescribeEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.deal_user_id):
            query['DealUserId'] = request.deal_user_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub_type_code):
            query['SubTypeCode'] = request.sub_type_code
        if not DaraCore.is_null(request.target_product_code):
            query['TargetProductCode'] = request.target_product_code
        if not DaraCore.is_null(request.type_code):
            query['TypeCode'] = request.type_code
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEvents',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: main_models.DescribeEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.deal_user_id):
            query['DealUserId'] = request.deal_user_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub_type_code):
            query['SubTypeCode'] = request.sub_type_code
        if not DaraCore.is_null(request.target_product_code):
            query['TargetProductCode'] = request.target_product_code
        if not DaraCore.is_null(request.type_code):
            query['TypeCode'] = request.type_code
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEvents',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events(
        self,
        request: main_models.DescribeEventsRequest,
    ) -> main_models.DescribeEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    async def describe_events_async(
        self,
        request: main_models.DescribeEventsRequest,
    ) -> main_models.DescribeEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_events_with_options_async(request, runtime)

    def describe_identify_task_status_with_options(
        self,
        request: main_models.DescribeIdentifyTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIdentifyTaskStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIdentifyTaskStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIdentifyTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_identify_task_status_with_options_async(
        self,
        request: main_models.DescribeIdentifyTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIdentifyTaskStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIdentifyTaskStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIdentifyTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_identify_task_status(
        self,
        request: main_models.DescribeIdentifyTaskStatusRequest,
    ) -> main_models.DescribeIdentifyTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_identify_task_status_with_options(request, runtime)

    async def describe_identify_task_status_async(
        self,
        request: main_models.DescribeIdentifyTaskStatusRequest,
    ) -> main_models.DescribeIdentifyTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_identify_task_status_with_options_async(request, runtime)

    def describe_instance_sources_with_options(
        self,
        request: main_models.DescribeInstanceSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.auth_status):
            query['AuthStatus'] = request.auth_status
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.search_type):
            query['SearchType'] = request.search_type
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSources',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_sources_with_options_async(
        self,
        request: main_models.DescribeInstanceSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.auth_status):
            query['AuthStatus'] = request.auth_status
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.search_type):
            query['SearchType'] = request.search_type
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceSources',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_sources(
        self,
        request: main_models.DescribeInstanceSourcesRequest,
    ) -> main_models.DescribeInstanceSourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_sources_with_options(request, runtime)

    async def describe_instance_sources_async(
        self,
        request: main_models.DescribeInstanceSourcesRequest,
    ) -> main_models.DescribeInstanceSourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_sources_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_oss_object_detail_with_options(
        self,
        request: main_models.DescribeOssObjectDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssObjectDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssObjectDetail',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssObjectDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_object_detail_with_options_async(
        self,
        request: main_models.DescribeOssObjectDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssObjectDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssObjectDetail',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssObjectDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_object_detail(
        self,
        request: main_models.DescribeOssObjectDetailRequest,
    ) -> main_models.DescribeOssObjectDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_oss_object_detail_with_options(request, runtime)

    async def describe_oss_object_detail_async(
        self,
        request: main_models.DescribeOssObjectDetailRequest,
    ) -> main_models.DescribeOssObjectDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_oss_object_detail_with_options_async(request, runtime)

    def describe_oss_object_detail_v2with_options(
        self,
        request: main_models.DescribeOssObjectDetailV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssObjectDetailV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_key):
            query['ObjectKey'] = request.object_key
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssObjectDetailV2',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssObjectDetailV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_object_detail_v2with_options_async(
        self,
        request: main_models.DescribeOssObjectDetailV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssObjectDetailV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_key):
            query['ObjectKey'] = request.object_key
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssObjectDetailV2',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssObjectDetailV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_object_detail_v2(
        self,
        request: main_models.DescribeOssObjectDetailV2Request,
    ) -> main_models.DescribeOssObjectDetailV2Response:
        runtime = RuntimeOptions()
        return self.describe_oss_object_detail_v2with_options(request, runtime)

    async def describe_oss_object_detail_v2_async(
        self,
        request: main_models.DescribeOssObjectDetailV2Request,
    ) -> main_models.DescribeOssObjectDetailV2Response:
        runtime = RuntimeOptions()
        return await self.describe_oss_object_detail_v2with_options_async(request, runtime)

    def describe_oss_objects_with_options(
        self,
        request: main_models.DescribeOssObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.file_category_code):
            query['FileCategoryCode'] = request.file_category_code
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.last_scan_time_end):
            query['LastScanTimeEnd'] = request.last_scan_time_end
        if not DaraCore.is_null(request.last_scan_time_start):
            query['LastScanTimeStart'] = request.last_scan_time_start
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssObjects',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_oss_objects_with_options_async(
        self,
        request: main_models.DescribeOssObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOssObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.file_category_code):
            query['FileCategoryCode'] = request.file_category_code
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.last_scan_time_end):
            query['LastScanTimeEnd'] = request.last_scan_time_end
        if not DaraCore.is_null(request.last_scan_time_start):
            query['LastScanTimeStart'] = request.last_scan_time_start
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOssObjects',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOssObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_oss_objects(
        self,
        request: main_models.DescribeOssObjectsRequest,
    ) -> main_models.DescribeOssObjectsResponse:
        runtime = RuntimeOptions()
        return self.describe_oss_objects_with_options(request, runtime)

    async def describe_oss_objects_async(
        self,
        request: main_models.DescribeOssObjectsRequest,
    ) -> main_models.DescribeOssObjectsResponse:
        runtime = RuntimeOptions()
        return await self.describe_oss_objects_with_options_async(request, runtime)

    def describe_packages_with_options(
        self,
        request: main_models.DescribePackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePackages',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_packages_with_options_async(
        self,
        request: main_models.DescribePackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePackages',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_packages(
        self,
        request: main_models.DescribePackagesRequest,
    ) -> main_models.DescribePackagesResponse:
        runtime = RuntimeOptions()
        return self.describe_packages_with_options(request, runtime)

    async def describe_packages_async(
        self,
        request: main_models.DescribePackagesRequest,
    ) -> main_models.DescribePackagesResponse:
        runtime = RuntimeOptions()
        return await self.describe_packages_with_options_async(request, runtime)

    def describe_parent_instance_with_options(
        self,
        request: main_models.DescribeParentInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParentInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_status):
            query['AuthStatus'] = request.auth_status
        if not DaraCore.is_null(request.check_status):
            query['CheckStatus'] = request.check_status
        if not DaraCore.is_null(request.cluster_status):
            query['ClusterStatus'] = request.cluster_status
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_account):
            query['MemberAccount'] = request.member_account
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParentInstance',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParentInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parent_instance_with_options_async(
        self,
        request: main_models.DescribeParentInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParentInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_status):
            query['AuthStatus'] = request.auth_status
        if not DaraCore.is_null(request.check_status):
            query['CheckStatus'] = request.check_status
        if not DaraCore.is_null(request.cluster_status):
            query['ClusterStatus'] = request.cluster_status
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.member_account):
            query['MemberAccount'] = request.member_account
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParentInstance',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParentInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parent_instance(
        self,
        request: main_models.DescribeParentInstanceRequest,
    ) -> main_models.DescribeParentInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_parent_instance_with_options(request, runtime)

    async def describe_parent_instance_async(
        self,
        request: main_models.DescribeParentInstanceRequest,
    ) -> main_models.DescribeParentInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_parent_instance_with_options_async(request, runtime)

    def describe_risk_levels_with_options(
        self,
        request: main_models.DescribeRiskLevelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskLevelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskLevels',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskLevelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_risk_levels_with_options_async(
        self,
        request: main_models.DescribeRiskLevelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRiskLevelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRiskLevels',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRiskLevelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_risk_levels(
        self,
        request: main_models.DescribeRiskLevelsRequest,
    ) -> main_models.DescribeRiskLevelsResponse:
        runtime = RuntimeOptions()
        return self.describe_risk_levels_with_options(request, runtime)

    async def describe_risk_levels_async(
        self,
        request: main_models.DescribeRiskLevelsRequest,
    ) -> main_models.DescribeRiskLevelsResponse:
        runtime = RuntimeOptions()
        return await self.describe_risk_levels_with_options_async(request, runtime)

    def describe_rules_with_options(
        self,
        request: main_models.DescribeRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.content_category):
            query['ContentCategory'] = request.content_category
        if not DaraCore.is_null(request.cooperation_channel):
            query['CooperationChannel'] = request.cooperation_channel
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.custom_type):
            query['CustomType'] = request.custom_type
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.keyword_compatible):
            query['KeywordCompatible'] = request.keyword_compatible
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.simplify):
            query['Simplify'] = request.simplify
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.support_form):
            query['SupportForm'] = request.support_form
        if not DaraCore.is_null(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRules',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rules_with_options_async(
        self,
        request: main_models.DescribeRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.content_category):
            query['ContentCategory'] = request.content_category
        if not DaraCore.is_null(request.cooperation_channel):
            query['CooperationChannel'] = request.cooperation_channel
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.custom_type):
            query['CustomType'] = request.custom_type
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.keyword_compatible):
            query['KeywordCompatible'] = request.keyword_compatible
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.simplify):
            query['Simplify'] = request.simplify
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.support_form):
            query['SupportForm'] = request.support_form
        if not DaraCore.is_null(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRules',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rules(
        self,
        request: main_models.DescribeRulesRequest,
    ) -> main_models.DescribeRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_rules_with_options(request, runtime)

    async def describe_rules_async(
        self,
        request: main_models.DescribeRulesRequest,
    ) -> main_models.DescribeRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_rules_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: main_models.DescribeTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.package_id):
            query['PackageId'] = request.package_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTables',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: main_models.DescribeTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.package_id):
            query['PackageId'] = request.package_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTables',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tables(
        self,
        request: main_models.DescribeTablesRequest,
    ) -> main_models.DescribeTablesResponse:
        runtime = RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: main_models.DescribeTablesRequest,
    ) -> main_models.DescribeTablesResponse:
        runtime = RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def describe_template_all_rules_with_options(
        self,
        request: main_models.DescribeTemplateAllRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateAllRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateAllRules',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateAllRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_template_all_rules_with_options_async(
        self,
        request: main_models.DescribeTemplateAllRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTemplateAllRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTemplateAllRules',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTemplateAllRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_template_all_rules(
        self,
        request: main_models.DescribeTemplateAllRulesRequest,
    ) -> main_models.DescribeTemplateAllRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_template_all_rules_with_options(request, runtime)

    async def describe_template_all_rules_async(
        self,
        request: main_models.DescribeTemplateAllRulesRequest,
    ) -> main_models.DescribeTemplateAllRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_template_all_rules_with_options_async(request, runtime)

    def describe_user_status_with_options(
        self,
        request: main_models.DescribeUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_status_with_options_async(
        self,
        request: main_models.DescribeUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_status(
        self,
        request: main_models.DescribeUserStatusRequest,
    ) -> main_models.DescribeUserStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_user_status_with_options(request, runtime)

    async def describe_user_status_async(
        self,
        request: main_models.DescribeUserStatusRequest,
    ) -> main_models.DescribeUserStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_status_with_options_async(request, runtime)

    def disable_user_config_with_options(
        self,
        request: main_models.DisableUserConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableUserConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableUserConfig',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_user_config_with_options_async(
        self,
        request: main_models.DisableUserConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableUserConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.code):
            query['Code'] = request.code
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableUserConfig',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_user_config(
        self,
        request: main_models.DisableUserConfigRequest,
    ) -> main_models.DisableUserConfigResponse:
        runtime = RuntimeOptions()
        return self.disable_user_config_with_options(request, runtime)

    async def disable_user_config_async(
        self,
        request: main_models.DisableUserConfigRequest,
    ) -> main_models.DisableUserConfigResponse:
        runtime = RuntimeOptions()
        return await self.disable_user_config_with_options_async(request, runtime)

    def exec_datamask_with_options(
        self,
        request: main_models.ExecDatamaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecDatamaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecDatamask',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDatamaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_datamask_with_options_async(
        self,
        request: main_models.ExecDatamaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecDatamaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecDatamask',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecDatamaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_datamask(
        self,
        request: main_models.ExecDatamaskRequest,
    ) -> main_models.ExecDatamaskResponse:
        runtime = RuntimeOptions()
        return self.exec_datamask_with_options(request, runtime)

    async def exec_datamask_async(
        self,
        request: main_models.ExecDatamaskRequest,
    ) -> main_models.ExecDatamaskResponse:
        runtime = RuntimeOptions()
        return await self.exec_datamask_with_options_async(request, runtime)

    def manual_trigger_masking_process_with_options(
        self,
        request: main_models.ManualTriggerMaskingProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManualTriggerMaskingProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ManualTriggerMaskingProcess',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManualTriggerMaskingProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def manual_trigger_masking_process_with_options_async(
        self,
        request: main_models.ManualTriggerMaskingProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ManualTriggerMaskingProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ManualTriggerMaskingProcess',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManualTriggerMaskingProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manual_trigger_masking_process(
        self,
        request: main_models.ManualTriggerMaskingProcessRequest,
    ) -> main_models.ManualTriggerMaskingProcessResponse:
        runtime = RuntimeOptions()
        return self.manual_trigger_masking_process_with_options(request, runtime)

    async def manual_trigger_masking_process_async(
        self,
        request: main_models.ManualTriggerMaskingProcessRequest,
    ) -> main_models.ManualTriggerMaskingProcessResponse:
        runtime = RuntimeOptions()
        return await self.manual_trigger_masking_process_with_options_async(request, runtime)

    def mask_oss_image_with_options(
        self,
        request: main_models.MaskOssImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MaskOssImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.is_always_upload):
            query['IsAlwaysUpload'] = request.is_always_upload
        if not DaraCore.is_null(request.is_support_restore):
            query['IsSupportRestore'] = request.is_support_restore
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.mask_rule_id_list):
            query['MaskRuleIdList'] = request.mask_rule_id_list
        if not DaraCore.is_null(request.object_key):
            query['ObjectKey'] = request.object_key
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MaskOssImage',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MaskOssImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def mask_oss_image_with_options_async(
        self,
        request: main_models.MaskOssImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MaskOssImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.is_always_upload):
            query['IsAlwaysUpload'] = request.is_always_upload
        if not DaraCore.is_null(request.is_support_restore):
            query['IsSupportRestore'] = request.is_support_restore
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.mask_rule_id_list):
            query['MaskRuleIdList'] = request.mask_rule_id_list
        if not DaraCore.is_null(request.object_key):
            query['ObjectKey'] = request.object_key
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MaskOssImage',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MaskOssImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def mask_oss_image(
        self,
        request: main_models.MaskOssImageRequest,
    ) -> main_models.MaskOssImageResponse:
        runtime = RuntimeOptions()
        return self.mask_oss_image_with_options(request, runtime)

    async def mask_oss_image_async(
        self,
        request: main_models.MaskOssImageRequest,
    ) -> main_models.MaskOssImageResponse:
        runtime = RuntimeOptions()
        return await self.mask_oss_image_with_options_async(request, runtime)

    def modify_data_limit_with_options(
        self,
        request: main_models.ModifyDataLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.auto_scan):
            query['AutoScan'] = request.auto_scan
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.log_store_day):
            query['LogStoreDay'] = request.log_store_day
        if not DaraCore.is_null(request.modify_password):
            query['ModifyPassword'] = request.modify_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sampling_size):
            query['SamplingSize'] = request.sampling_size
        if not DaraCore.is_null(request.security_group_id_list):
            query['SecurityGroupIdList'] = request.security_group_id_list
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.v_switch_id_list):
            query['VSwitchIdList'] = request.v_switch_id_list
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataLimit',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_limit_with_options_async(
        self,
        request: main_models.ModifyDataLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.auto_scan):
            query['AutoScan'] = request.auto_scan
        if not DaraCore.is_null(request.engine_type):
            query['EngineType'] = request.engine_type
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.log_store_day):
            query['LogStoreDay'] = request.log_store_day
        if not DaraCore.is_null(request.modify_password):
            query['ModifyPassword'] = request.modify_password
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sampling_size):
            query['SamplingSize'] = request.sampling_size
        if not DaraCore.is_null(request.security_group_id_list):
            query['SecurityGroupIdList'] = request.security_group_id_list
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.v_switch_id_list):
            query['VSwitchIdList'] = request.v_switch_id_list
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataLimit',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_limit(
        self,
        request: main_models.ModifyDataLimitRequest,
    ) -> main_models.ModifyDataLimitResponse:
        runtime = RuntimeOptions()
        return self.modify_data_limit_with_options(request, runtime)

    async def modify_data_limit_async(
        self,
        request: main_models.ModifyDataLimitRequest,
    ) -> main_models.ModifyDataLimitResponse:
        runtime = RuntimeOptions()
        return await self.modify_data_limit_with_options_async(request, runtime)

    def modify_default_level_with_options(
        self,
        request: main_models.ModifyDefaultLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefaultLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_id):
            query['DefaultId'] = request.default_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sensitive_ids):
            query['SensitiveIds'] = request.sensitive_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefaultLevel',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefaultLevelResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_default_level_with_options_async(
        self,
        request: main_models.ModifyDefaultLevelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDefaultLevelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_id):
            query['DefaultId'] = request.default_id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sensitive_ids):
            query['SensitiveIds'] = request.sensitive_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDefaultLevel',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDefaultLevelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_default_level(
        self,
        request: main_models.ModifyDefaultLevelRequest,
    ) -> main_models.ModifyDefaultLevelResponse:
        runtime = RuntimeOptions()
        return self.modify_default_level_with_options(request, runtime)

    async def modify_default_level_async(
        self,
        request: main_models.ModifyDefaultLevelRequest,
    ) -> main_models.ModifyDefaultLevelResponse:
        runtime = RuntimeOptions()
        return await self.modify_default_level_with_options_async(request, runtime)

    def modify_event_status_with_options(
        self,
        request: main_models.ModifyEventStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEventStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backed):
            query['Backed'] = request.backed
        if not DaraCore.is_null(request.deal_reason):
            query['DealReason'] = request.deal_reason
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEventStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEventStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_event_status_with_options_async(
        self,
        request: main_models.ModifyEventStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEventStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backed):
            query['Backed'] = request.backed
        if not DaraCore.is_null(request.deal_reason):
            query['DealReason'] = request.deal_reason
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEventStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEventStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_event_status(
        self,
        request: main_models.ModifyEventStatusRequest,
    ) -> main_models.ModifyEventStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_event_status_with_options(request, runtime)

    async def modify_event_status_async(
        self,
        request: main_models.ModifyEventStatusRequest,
    ) -> main_models.ModifyEventStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_event_status_with_options_async(request, runtime)

    def modify_event_type_status_with_options(
        self,
        request: main_models.ModifyEventTypeStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEventTypeStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sub_type_ids):
            query['SubTypeIds'] = request.sub_type_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEventTypeStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEventTypeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_event_type_status_with_options_async(
        self,
        request: main_models.ModifyEventTypeStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEventTypeStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.sub_type_ids):
            query['SubTypeIds'] = request.sub_type_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEventTypeStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEventTypeStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_event_type_status(
        self,
        request: main_models.ModifyEventTypeStatusRequest,
    ) -> main_models.ModifyEventTypeStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_event_type_status_with_options(request, runtime)

    async def modify_event_type_status_async(
        self,
        request: main_models.ModifyEventTypeStatusRequest,
    ) -> main_models.ModifyEventTypeStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_event_type_status_with_options_async(request, runtime)

    def modify_report_task_status_with_options(
        self,
        request: main_models.ModifyReportTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyReportTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.report_task_status):
            query['ReportTaskStatus'] = request.report_task_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyReportTaskStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyReportTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_report_task_status_with_options_async(
        self,
        request: main_models.ModifyReportTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyReportTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature_type):
            query['FeatureType'] = request.feature_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.report_task_status):
            query['ReportTaskStatus'] = request.report_task_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyReportTaskStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyReportTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_report_task_status(
        self,
        request: main_models.ModifyReportTaskStatusRequest,
    ) -> main_models.ModifyReportTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_report_task_status_with_options(request, runtime)

    async def modify_report_task_status_async(
        self,
        request: main_models.ModifyReportTaskStatusRequest,
    ) -> main_models.ModifyReportTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_report_task_status_with_options_async(request, runtime)

    def modify_rule_with_options(
        self,
        request: main_models.ModifyRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.model_rule_ids):
            query['ModelRuleIds'] = request.model_rule_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.support_form):
            query['SupportForm'] = request.support_form
        if not DaraCore.is_null(request.template_rule_ids):
            query['TemplateRuleIds'] = request.template_rule_ids
        if not DaraCore.is_null(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRule',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rule_with_options_async(
        self,
        request: main_models.ModifyRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.model_rule_ids):
            query['ModelRuleIds'] = request.model_rule_ids
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.risk_level_id):
            query['RiskLevelId'] = request.risk_level_id
        if not DaraCore.is_null(request.rule_type):
            query['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.support_form):
            query['SupportForm'] = request.support_form
        if not DaraCore.is_null(request.template_rule_ids):
            query['TemplateRuleIds'] = request.template_rule_ids
        if not DaraCore.is_null(request.warn_level):
            query['WarnLevel'] = request.warn_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRule',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rule(
        self,
        request: main_models.ModifyRuleRequest,
    ) -> main_models.ModifyRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_rule_with_options(request, runtime)

    async def modify_rule_async(
        self,
        request: main_models.ModifyRuleRequest,
    ) -> main_models.ModifyRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_rule_with_options_async(request, runtime)

    def modify_rule_status_with_options(
        self,
        request: main_models.ModifyRuleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRuleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRuleStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rule_status_with_options_async(
        self,
        request: main_models.ModifyRuleStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRuleStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRuleStatus',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rule_status(
        self,
        request: main_models.ModifyRuleStatusRequest,
    ) -> main_models.ModifyRuleStatusResponse:
        runtime = RuntimeOptions()
        return self.modify_rule_status_with_options(request, runtime)

    async def modify_rule_status_async(
        self,
        request: main_models.ModifyRuleStatusRequest,
    ) -> main_models.ModifyRuleStatusResponse:
        runtime = RuntimeOptions()
        return await self.modify_rule_status_with_options_async(request, runtime)

    def restore_oss_image_with_options(
        self,
        request: main_models.RestoreOssImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreOssImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_key):
            query['ObjectKey'] = request.object_key
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.target_object_key):
            query['TargetObjectKey'] = request.target_object_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreOssImage',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreOssImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_oss_image_with_options_async(
        self,
        request: main_models.RestoreOssImageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestoreOssImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_key):
            query['ObjectKey'] = request.object_key
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.target_object_key):
            query['TargetObjectKey'] = request.target_object_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestoreOssImage',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestoreOssImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restore_oss_image(
        self,
        request: main_models.RestoreOssImageRequest,
    ) -> main_models.RestoreOssImageResponse:
        runtime = RuntimeOptions()
        return self.restore_oss_image_with_options(request, runtime)

    async def restore_oss_image_async(
        self,
        request: main_models.RestoreOssImageRequest,
    ) -> main_models.RestoreOssImageResponse:
        runtime = RuntimeOptions()
        return await self.restore_oss_image_with_options_async(request, runtime)

    def scan_oss_object_v1with_options(
        self,
        tmp_req: main_models.ScanOssObjectV1Request,
        runtime: RuntimeOptions,
    ) -> main_models.ScanOssObjectV1Response:
        tmp_req.validate()
        request = main_models.ScanOssObjectV1ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_key_list):
            request.object_key_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_key_list, 'ObjectKeyList', 'json')
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_key_list_shrink):
            query['ObjectKeyList'] = request.object_key_list_shrink
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScanOssObjectV1',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScanOssObjectV1Response(),
            self.call_api(params, req, runtime)
        )

    async def scan_oss_object_v1with_options_async(
        self,
        tmp_req: main_models.ScanOssObjectV1Request,
        runtime: RuntimeOptions,
    ) -> main_models.ScanOssObjectV1Response:
        tmp_req.validate()
        request = main_models.ScanOssObjectV1ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_key_list):
            request.object_key_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_key_list, 'ObjectKeyList', 'json')
        query = {}
        if not DaraCore.is_null(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.object_key_list_shrink):
            query['ObjectKeyList'] = request.object_key_list_shrink
        if not DaraCore.is_null(request.service_region_id):
            query['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ScanOssObjectV1',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScanOssObjectV1Response(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_oss_object_v1(
        self,
        request: main_models.ScanOssObjectV1Request,
    ) -> main_models.ScanOssObjectV1Response:
        runtime = RuntimeOptions()
        return self.scan_oss_object_v1with_options(request, runtime)

    async def scan_oss_object_v1_async(
        self,
        request: main_models.ScanOssObjectV1Request,
    ) -> main_models.ScanOssObjectV1Response:
        runtime = RuntimeOptions()
        return await self.scan_oss_object_v1with_options_async(request, runtime)

    def stop_masking_process_with_options(
        self,
        request: main_models.StopMaskingProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopMaskingProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopMaskingProcess',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopMaskingProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_masking_process_with_options_async(
        self,
        request: main_models.StopMaskingProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopMaskingProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopMaskingProcess',
            version = '2019-01-03',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopMaskingProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_masking_process(
        self,
        request: main_models.StopMaskingProcessRequest,
    ) -> main_models.StopMaskingProcessResponse:
        runtime = RuntimeOptions()
        return self.stop_masking_process_with_options(request, runtime)

    async def stop_masking_process_async(
        self,
        request: main_models.StopMaskingProcessRequest,
    ) -> main_models.StopMaskingProcessResponse:
        runtime = RuntimeOptions()
        return await self.stop_masking_process_with_options_async(request, runtime)
