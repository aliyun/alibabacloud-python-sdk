# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cloud_siem20241212 import models as main_models
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
        self._endpoint = self.get_endpoint('cloud-siem', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def check_upgrade_item_with_options(
        self,
        request: main_models.CheckUpgradeItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUpgradeItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.upgrade_item_id):
            body['UpgradeItemId'] = request.upgrade_item_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckUpgradeItem',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUpgradeItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_upgrade_item_with_options_async(
        self,
        request: main_models.CheckUpgradeItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckUpgradeItemResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.upgrade_item_id):
            body['UpgradeItemId'] = request.upgrade_item_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckUpgradeItem',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckUpgradeItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_upgrade_item(
        self,
        request: main_models.CheckUpgradeItemRequest,
    ) -> main_models.CheckUpgradeItemResponse:
        runtime = RuntimeOptions()
        return self.check_upgrade_item_with_options(request, runtime)

    async def check_upgrade_item_async(
        self,
        request: main_models.CheckUpgradeItemRequest,
    ) -> main_models.CheckUpgradeItemResponse:
        runtime = RuntimeOptions()
        return await self.check_upgrade_item_with_options_async(request, runtime)

    def create_data_ingestion_with_options(
        self,
        request: main_models.CreateDataIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.capacity_count):
            body['CapacityCount'] = request.capacity_count
        if not DaraCore.is_null(request.data_ingestion_mode):
            body['DataIngestionMode'] = request.data_ingestion_mode
        if not DaraCore.is_null(request.data_ingestion_state_code):
            body['DataIngestionStateCode'] = request.data_ingestion_state_code
        if not DaraCore.is_null(request.data_ingestion_type):
            body['DataIngestionType'] = request.data_ingestion_type
        if not DaraCore.is_null(request.data_source_editable):
            body['DataSourceEditable'] = request.data_source_editable
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_editable):
            body['NormalizationRuleEditable'] = request.normalization_rule_editable
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.scan_data_source_id):
            body['ScanDataSourceId'] = request.scan_data_source_id
        if not DaraCore.is_null(request.stream_job_id):
            body['StreamJobId'] = request.stream_job_id
        if not DaraCore.is_null(request.update_time):
            body['UpdateTime'] = request.update_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_ingestion_with_options_async(
        self,
        request: main_models.CreateDataIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.capacity_count):
            body['CapacityCount'] = request.capacity_count
        if not DaraCore.is_null(request.data_ingestion_mode):
            body['DataIngestionMode'] = request.data_ingestion_mode
        if not DaraCore.is_null(request.data_ingestion_state_code):
            body['DataIngestionStateCode'] = request.data_ingestion_state_code
        if not DaraCore.is_null(request.data_ingestion_type):
            body['DataIngestionType'] = request.data_ingestion_type
        if not DaraCore.is_null(request.data_source_editable):
            body['DataSourceEditable'] = request.data_source_editable
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_editable):
            body['NormalizationRuleEditable'] = request.normalization_rule_editable
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.scan_data_source_id):
            body['ScanDataSourceId'] = request.scan_data_source_id
        if not DaraCore.is_null(request.stream_job_id):
            body['StreamJobId'] = request.stream_job_id
        if not DaraCore.is_null(request.update_time):
            body['UpdateTime'] = request.update_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_ingestion(
        self,
        request: main_models.CreateDataIngestionRequest,
    ) -> main_models.CreateDataIngestionResponse:
        runtime = RuntimeOptions()
        return self.create_data_ingestion_with_options(request, runtime)

    async def create_data_ingestion_async(
        self,
        request: main_models.CreateDataIngestionRequest,
    ) -> main_models.CreateDataIngestionResponse:
        runtime = RuntimeOptions()
        return await self.create_data_ingestion_with_options_async(request, runtime)

    def create_data_set_with_options(
        self,
        request: main_models.CreateDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_description):
            body['DataSetDescription'] = request.data_set_description
        if not DaraCore.is_null(request.data_set_field_key_name):
            body['DataSetFieldKeyName'] = request.data_set_field_key_name
        if not DaraCore.is_null(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not DaraCore.is_null(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not DaraCore.is_null(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        if not DaraCore.is_null(request.data_set_type):
            body['DataSetType'] = request.data_set_type
        body_flat = {}
        if not DaraCore.is_null(request.ip_whitelist_recognizers):
            body_flat['IpWhitelistRecognizers'] = request.ip_whitelist_recognizers
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSet',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_set_with_options_async(
        self,
        request: main_models.CreateDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_description):
            body['DataSetDescription'] = request.data_set_description
        if not DaraCore.is_null(request.data_set_field_key_name):
            body['DataSetFieldKeyName'] = request.data_set_field_key_name
        if not DaraCore.is_null(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not DaraCore.is_null(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not DaraCore.is_null(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        if not DaraCore.is_null(request.data_set_type):
            body['DataSetType'] = request.data_set_type
        body_flat = {}
        if not DaraCore.is_null(request.ip_whitelist_recognizers):
            body_flat['IpWhitelistRecognizers'] = request.ip_whitelist_recognizers
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSet',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_set(
        self,
        request: main_models.CreateDataSetRequest,
    ) -> main_models.CreateDataSetResponse:
        runtime = RuntimeOptions()
        return self.create_data_set_with_options(request, runtime)

    async def create_data_set_async(
        self,
        request: main_models.CreateDataSetRequest,
    ) -> main_models.CreateDataSetResponse:
        runtime = RuntimeOptions()
        return await self.create_data_set_with_options_async(request, runtime)

    def create_data_source_with_options(
        self,
        tmp_req: main_models.CreateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSourceResponse:
        tmp_req.validate()
        request = main_models.CreateDataSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source_ids):
            request.data_source_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        if not DaraCore.is_null(tmp_req.data_source_references):
            request.data_source_references_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_references, 'DataSourceReferences', 'json')
        body = {}
        if not DaraCore.is_null(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not DaraCore.is_null(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not DaraCore.is_null(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        if not DaraCore.is_null(request.data_source_recognizer):
            body['DataSourceRecognizer'] = request.data_source_recognizer
        if not DaraCore.is_null(request.data_source_references_shrink):
            body['DataSourceReferences'] = request.data_source_references_shrink
        body_flat = {}
        if not DaraCore.is_null(request.data_source_stores):
            body_flat['DataSourceStores'] = request.data_source_stores
        if not DaraCore.is_null(request.data_source_template_id):
            body['DataSourceTemplateId'] = request.data_source_template_id
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSource',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        tmp_req: main_models.CreateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataSourceResponse:
        tmp_req.validate()
        request = main_models.CreateDataSourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source_ids):
            request.data_source_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        if not DaraCore.is_null(tmp_req.data_source_references):
            request.data_source_references_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_references, 'DataSourceReferences', 'json')
        body = {}
        if not DaraCore.is_null(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not DaraCore.is_null(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not DaraCore.is_null(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        if not DaraCore.is_null(request.data_source_recognizer):
            body['DataSourceRecognizer'] = request.data_source_recognizer
        if not DaraCore.is_null(request.data_source_references_shrink):
            body['DataSourceReferences'] = request.data_source_references_shrink
        body_flat = {}
        if not DaraCore.is_null(request.data_source_stores):
            body_flat['DataSourceStores'] = request.data_source_stores
        if not DaraCore.is_null(request.data_source_template_id):
            body['DataSourceTemplateId'] = request.data_source_template_id
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataSource',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_source(
        self,
        request: main_models.CreateDataSourceRequest,
    ) -> main_models.CreateDataSourceResponse:
        runtime = RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    async def create_data_source_async(
        self,
        request: main_models.CreateDataSourceRequest,
    ) -> main_models.CreateDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.create_data_source_with_options_async(request, runtime)

    def create_detection_rule_with_options(
        self,
        request: main_models.CreateDetectionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDetectionRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not DaraCore.is_null(request.alert_description):
            body['AlertDescription'] = request.alert_description
        if not DaraCore.is_null(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_schema_id):
            body['AlertSchemaId'] = request.alert_schema_id
        if not DaraCore.is_null(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not DaraCore.is_null(request.alert_threshold_count):
            body['AlertThresholdCount'] = request.alert_threshold_count
        if not DaraCore.is_null(request.alert_threshold_group):
            body['AlertThresholdGroup'] = request.alert_threshold_group
        if not DaraCore.is_null(request.alert_threshold_period):
            body['AlertThresholdPeriod'] = request.alert_threshold_period
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.detection_expression_content):
            body['DetectionExpressionContent'] = request.detection_expression_content
        if not DaraCore.is_null(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not DaraCore.is_null(request.detection_rule_description):
            body['DetectionRuleDescription'] = request.detection_rule_description
        if not DaraCore.is_null(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not DaraCore.is_null(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not DaraCore.is_null(request.detection_rule_template_id):
            body['DetectionRuleTemplateId'] = request.detection_rule_template_id
        if not DaraCore.is_null(request.detection_rule_template_version):
            body['DetectionRuleTemplateVersion'] = request.detection_rule_template_version
        if not DaraCore.is_null(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not DaraCore.is_null(request.entity_mappings):
            body['EntityMappings'] = request.entity_mappings
        if not DaraCore.is_null(request.incident_aggregation_expression):
            body['IncidentAggregationExpression'] = request.incident_aggregation_expression
        if not DaraCore.is_null(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not DaraCore.is_null(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not DaraCore.is_null(request.playbook_parameters):
            body['PlaybookParameters'] = request.playbook_parameters
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.schedule_begin_time):
            body['ScheduleBeginTime'] = request.schedule_begin_time
        if not DaraCore.is_null(request.schedule_expression):
            body['ScheduleExpression'] = request.schedule_expression
        if not DaraCore.is_null(request.schedule_max_retries):
            body['ScheduleMaxRetries'] = request.schedule_max_retries
        if not DaraCore.is_null(request.schedule_max_timeout):
            body['ScheduleMaxTimeout'] = request.schedule_max_timeout
        if not DaraCore.is_null(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.schedule_window):
            body['ScheduleWindow'] = request.schedule_window
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDetectionRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDetectionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_detection_rule_with_options_async(
        self,
        request: main_models.CreateDetectionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDetectionRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not DaraCore.is_null(request.alert_description):
            body['AlertDescription'] = request.alert_description
        if not DaraCore.is_null(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_schema_id):
            body['AlertSchemaId'] = request.alert_schema_id
        if not DaraCore.is_null(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not DaraCore.is_null(request.alert_threshold_count):
            body['AlertThresholdCount'] = request.alert_threshold_count
        if not DaraCore.is_null(request.alert_threshold_group):
            body['AlertThresholdGroup'] = request.alert_threshold_group
        if not DaraCore.is_null(request.alert_threshold_period):
            body['AlertThresholdPeriod'] = request.alert_threshold_period
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.detection_expression_content):
            body['DetectionExpressionContent'] = request.detection_expression_content
        if not DaraCore.is_null(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not DaraCore.is_null(request.detection_rule_description):
            body['DetectionRuleDescription'] = request.detection_rule_description
        if not DaraCore.is_null(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not DaraCore.is_null(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not DaraCore.is_null(request.detection_rule_template_id):
            body['DetectionRuleTemplateId'] = request.detection_rule_template_id
        if not DaraCore.is_null(request.detection_rule_template_version):
            body['DetectionRuleTemplateVersion'] = request.detection_rule_template_version
        if not DaraCore.is_null(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not DaraCore.is_null(request.entity_mappings):
            body['EntityMappings'] = request.entity_mappings
        if not DaraCore.is_null(request.incident_aggregation_expression):
            body['IncidentAggregationExpression'] = request.incident_aggregation_expression
        if not DaraCore.is_null(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not DaraCore.is_null(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not DaraCore.is_null(request.playbook_parameters):
            body['PlaybookParameters'] = request.playbook_parameters
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.schedule_begin_time):
            body['ScheduleBeginTime'] = request.schedule_begin_time
        if not DaraCore.is_null(request.schedule_expression):
            body['ScheduleExpression'] = request.schedule_expression
        if not DaraCore.is_null(request.schedule_max_retries):
            body['ScheduleMaxRetries'] = request.schedule_max_retries
        if not DaraCore.is_null(request.schedule_max_timeout):
            body['ScheduleMaxTimeout'] = request.schedule_max_timeout
        if not DaraCore.is_null(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.schedule_window):
            body['ScheduleWindow'] = request.schedule_window
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDetectionRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDetectionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_detection_rule(
        self,
        request: main_models.CreateDetectionRuleRequest,
    ) -> main_models.CreateDetectionRuleResponse:
        runtime = RuntimeOptions()
        return self.create_detection_rule_with_options(request, runtime)

    async def create_detection_rule_async(
        self,
        request: main_models.CreateDetectionRuleRequest,
    ) -> main_models.CreateDetectionRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_detection_rule_with_options_async(request, runtime)

    def create_export_task_with_options(
        self,
        request: main_models.CreateExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExportTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.export_task_parameter):
            body['ExportTaskParameter'] = request.export_task_parameter
        if not DaraCore.is_null(request.export_task_type):
            body['ExportTaskType'] = request.export_task_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExportTask',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_export_task_with_options_async(
        self,
        request: main_models.CreateExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExportTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.export_task_parameter):
            body['ExportTaskParameter'] = request.export_task_parameter
        if not DaraCore.is_null(request.export_task_type):
            body['ExportTaskType'] = request.export_task_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateExportTask',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_export_task(
        self,
        request: main_models.CreateExportTaskRequest,
    ) -> main_models.CreateExportTaskResponse:
        runtime = RuntimeOptions()
        return self.create_export_task_with_options(request, runtime)

    async def create_export_task_async(
        self,
        request: main_models.CreateExportTaskRequest,
    ) -> main_models.CreateExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_export_task_with_options_async(request, runtime)

    def create_log_store_with_options(
        self,
        request: main_models.CreateLogStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogStoreResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogStore',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_log_store_with_options_async(
        self,
        request: main_models.CreateLogStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogStoreResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogStore',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_log_store(
        self,
        request: main_models.CreateLogStoreRequest,
    ) -> main_models.CreateLogStoreResponse:
        runtime = RuntimeOptions()
        return self.create_log_store_with_options(request, runtime)

    async def create_log_store_async(
        self,
        request: main_models.CreateLogStoreRequest,
    ) -> main_models.CreateLogStoreResponse:
        runtime = RuntimeOptions()
        return await self.create_log_store_with_options_async(request, runtime)

    def create_normalization_rule_with_options(
        self,
        tmp_req: main_models.CreateNormalizationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNormalizationRuleResponse:
        tmp_req.validate()
        request = main_models.CreateNormalizationRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'json')
        body = {}
        if not DaraCore.is_null(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not DaraCore.is_null(request.extend_field_store_mode):
            body['ExtendFieldStoreMode'] = request.extend_field_store_mode
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_rule_description):
            body['NormalizationRuleDescription'] = request.normalization_rule_description
        if not DaraCore.is_null(request.normalization_rule_expression):
            body['NormalizationRuleExpression'] = request.normalization_rule_expression
        if not DaraCore.is_null(request.normalization_rule_format):
            body['NormalizationRuleFormat'] = request.normalization_rule_format
        if not DaraCore.is_null(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not DaraCore.is_null(request.normalization_rule_mode):
            body['NormalizationRuleMode'] = request.normalization_rule_mode
        if not DaraCore.is_null(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not DaraCore.is_null(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not DaraCore.is_null(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNormalizationRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNormalizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_normalization_rule_with_options_async(
        self,
        tmp_req: main_models.CreateNormalizationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNormalizationRuleResponse:
        tmp_req.validate()
        request = main_models.CreateNormalizationRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'json')
        body = {}
        if not DaraCore.is_null(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not DaraCore.is_null(request.extend_field_store_mode):
            body['ExtendFieldStoreMode'] = request.extend_field_store_mode
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_rule_description):
            body['NormalizationRuleDescription'] = request.normalization_rule_description
        if not DaraCore.is_null(request.normalization_rule_expression):
            body['NormalizationRuleExpression'] = request.normalization_rule_expression
        if not DaraCore.is_null(request.normalization_rule_format):
            body['NormalizationRuleFormat'] = request.normalization_rule_format
        if not DaraCore.is_null(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not DaraCore.is_null(request.normalization_rule_mode):
            body['NormalizationRuleMode'] = request.normalization_rule_mode
        if not DaraCore.is_null(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not DaraCore.is_null(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not DaraCore.is_null(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNormalizationRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNormalizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_normalization_rule(
        self,
        request: main_models.CreateNormalizationRuleRequest,
    ) -> main_models.CreateNormalizationRuleResponse:
        runtime = RuntimeOptions()
        return self.create_normalization_rule_with_options(request, runtime)

    async def create_normalization_rule_async(
        self,
        request: main_models.CreateNormalizationRuleRequest,
    ) -> main_models.CreateNormalizationRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_normalization_rule_with_options_async(request, runtime)

    def create_normalization_schema_with_options(
        self,
        request: main_models.CreateNormalizationSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNormalizationSchemaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_fields):
            body['NormalizationFields'] = request.normalization_fields
        if not DaraCore.is_null(request.normalization_schema_description):
            body['NormalizationSchemaDescription'] = request.normalization_schema_description
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.normalization_schema_name):
            body['NormalizationSchemaName'] = request.normalization_schema_name
        if not DaraCore.is_null(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.target_log_store):
            body['TargetLogStore'] = request.target_log_store
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNormalizationSchema',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNormalizationSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_normalization_schema_with_options_async(
        self,
        request: main_models.CreateNormalizationSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNormalizationSchemaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_fields):
            body['NormalizationFields'] = request.normalization_fields
        if not DaraCore.is_null(request.normalization_schema_description):
            body['NormalizationSchemaDescription'] = request.normalization_schema_description
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.normalization_schema_name):
            body['NormalizationSchemaName'] = request.normalization_schema_name
        if not DaraCore.is_null(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.target_log_store):
            body['TargetLogStore'] = request.target_log_store
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNormalizationSchema',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNormalizationSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_normalization_schema(
        self,
        request: main_models.CreateNormalizationSchemaRequest,
    ) -> main_models.CreateNormalizationSchemaResponse:
        runtime = RuntimeOptions()
        return self.create_normalization_schema_with_options(request, runtime)

    async def create_normalization_schema_async(
        self,
        request: main_models.CreateNormalizationSchemaRequest,
    ) -> main_models.CreateNormalizationSchemaResponse:
        runtime = RuntimeOptions()
        return await self.create_normalization_schema_with_options_async(request, runtime)

    def create_product_with_options(
        self,
        request: main_models.CreateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.product_name):
            body['ProductName'] = request.product_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProduct',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_with_options_async(
        self,
        request: main_models.CreateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.product_name):
            body['ProductName'] = request.product_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProduct',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product(
        self,
        request: main_models.CreateProductRequest,
    ) -> main_models.CreateProductResponse:
        runtime = RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    async def create_product_async(
        self,
        request: main_models.CreateProductRequest,
    ) -> main_models.CreateProductResponse:
        runtime = RuntimeOptions()
        return await self.create_product_with_options_async(request, runtime)

    def create_response_rule_with_options(
        self,
        request: main_models.CreateResponseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResponseRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.response_action_config):
            body['ResponseActionConfig'] = request.response_action_config
        if not DaraCore.is_null(request.response_action_type):
            body['ResponseActionType'] = request.response_action_type
        if not DaraCore.is_null(request.response_execution_condition):
            body['ResponseExecutionCondition'] = request.response_execution_condition
        if not DaraCore.is_null(request.response_rule_name):
            body['ResponseRuleName'] = request.response_rule_name
        if not DaraCore.is_null(request.response_rule_priority):
            body['ResponseRulePriority'] = request.response_rule_priority
        if not DaraCore.is_null(request.response_trigger_type):
            body['ResponseTriggerType'] = request.response_trigger_type
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResponseRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResponseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_response_rule_with_options_async(
        self,
        request: main_models.CreateResponseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResponseRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.response_action_config):
            body['ResponseActionConfig'] = request.response_action_config
        if not DaraCore.is_null(request.response_action_type):
            body['ResponseActionType'] = request.response_action_type
        if not DaraCore.is_null(request.response_execution_condition):
            body['ResponseExecutionCondition'] = request.response_execution_condition
        if not DaraCore.is_null(request.response_rule_name):
            body['ResponseRuleName'] = request.response_rule_name
        if not DaraCore.is_null(request.response_rule_priority):
            body['ResponseRulePriority'] = request.response_rule_priority
        if not DaraCore.is_null(request.response_trigger_type):
            body['ResponseTriggerType'] = request.response_trigger_type
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResponseRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResponseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_response_rule(
        self,
        request: main_models.CreateResponseRuleRequest,
    ) -> main_models.CreateResponseRuleResponse:
        runtime = RuntimeOptions()
        return self.create_response_rule_with_options(request, runtime)

    async def create_response_rule_async(
        self,
        request: main_models.CreateResponseRuleRequest,
    ) -> main_models.CreateResponseRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_response_rule_with_options_async(request, runtime)

    def create_vendor_with_options(
        self,
        request: main_models.CreateVendorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVendorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVendor',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVendorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vendor_with_options_async(
        self,
        request: main_models.CreateVendorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVendorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVendor',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVendorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vendor(
        self,
        request: main_models.CreateVendorRequest,
    ) -> main_models.CreateVendorResponse:
        runtime = RuntimeOptions()
        return self.create_vendor_with_options(request, runtime)

    async def create_vendor_async(
        self,
        request: main_models.CreateVendorRequest,
    ) -> main_models.CreateVendorResponse:
        runtime = RuntimeOptions()
        return await self.create_vendor_with_options_async(request, runtime)

    def delete_data_ingestion_with_options(
        self,
        request: main_models.DeleteDataIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_ingestion_with_options_async(
        self,
        request: main_models.DeleteDataIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_ingestion(
        self,
        request: main_models.DeleteDataIngestionRequest,
    ) -> main_models.DeleteDataIngestionResponse:
        runtime = RuntimeOptions()
        return self.delete_data_ingestion_with_options(request, runtime)

    async def delete_data_ingestion_async(
        self,
        request: main_models.DeleteDataIngestionRequest,
    ) -> main_models.DeleteDataIngestionResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_ingestion_with_options_async(request, runtime)

    def delete_data_set_with_options(
        self,
        request: main_models.DeleteDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSet',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_set_with_options_async(
        self,
        request: main_models.DeleteDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSet',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_set(
        self,
        request: main_models.DeleteDataSetRequest,
    ) -> main_models.DeleteDataSetResponse:
        runtime = RuntimeOptions()
        return self.delete_data_set_with_options(request, runtime)

    async def delete_data_set_async(
        self,
        request: main_models.DeleteDataSetRequest,
    ) -> main_models.DeleteDataSetResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_set_with_options_async(request, runtime)

    def delete_data_set_record_with_options(
        self,
        request: main_models.DeleteDataSetRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSetRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.data_set_record_ids):
            body['DataSetRecordIds'] = request.data_set_record_ids
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSetRecord',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSetRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_set_record_with_options_async(
        self,
        request: main_models.DeleteDataSetRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSetRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.data_set_record_ids):
            body['DataSetRecordIds'] = request.data_set_record_ids
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSetRecord',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSetRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_set_record(
        self,
        request: main_models.DeleteDataSetRecordRequest,
    ) -> main_models.DeleteDataSetRecordResponse:
        runtime = RuntimeOptions()
        return self.delete_data_set_record_with_options(request, runtime)

    async def delete_data_set_record_async(
        self,
        request: main_models.DeleteDataSetRecordRequest,
    ) -> main_models.DeleteDataSetRecordResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_set_record_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: main_models.DeleteDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSource',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        request: main_models.DeleteDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSource',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_source(
        self,
        request: main_models.DeleteDataSourceRequest,
    ) -> main_models.DeleteDataSourceResponse:
        runtime = RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: main_models.DeleteDataSourceRequest,
    ) -> main_models.DeleteDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_detection_rule_with_options(
        self,
        request: main_models.DeleteDetectionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDetectionRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDetectionRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDetectionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_detection_rule_with_options_async(
        self,
        request: main_models.DeleteDetectionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDetectionRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDetectionRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDetectionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_detection_rule(
        self,
        request: main_models.DeleteDetectionRuleRequest,
    ) -> main_models.DeleteDetectionRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_detection_rule_with_options(request, runtime)

    async def delete_detection_rule_async(
        self,
        request: main_models.DeleteDetectionRuleRequest,
    ) -> main_models.DeleteDetectionRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_detection_rule_with_options_async(request, runtime)

    def delete_log_store_with_options(
        self,
        request: main_models.DeleteLogStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogStoreResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogStore',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_store_with_options_async(
        self,
        request: main_models.DeleteLogStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogStoreResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogStore',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_store(
        self,
        request: main_models.DeleteLogStoreRequest,
    ) -> main_models.DeleteLogStoreResponse:
        runtime = RuntimeOptions()
        return self.delete_log_store_with_options(request, runtime)

    async def delete_log_store_async(
        self,
        request: main_models.DeleteLogStoreRequest,
    ) -> main_models.DeleteLogStoreResponse:
        runtime = RuntimeOptions()
        return await self.delete_log_store_with_options_async(request, runtime)

    def delete_normalization_rule_with_options(
        self,
        request: main_models.DeleteNormalizationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNormalizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNormalizationRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNormalizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_normalization_rule_with_options_async(
        self,
        request: main_models.DeleteNormalizationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNormalizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNormalizationRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNormalizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_normalization_rule(
        self,
        request: main_models.DeleteNormalizationRuleRequest,
    ) -> main_models.DeleteNormalizationRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_normalization_rule_with_options(request, runtime)

    async def delete_normalization_rule_async(
        self,
        request: main_models.DeleteNormalizationRuleRequest,
    ) -> main_models.DeleteNormalizationRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_normalization_rule_with_options_async(request, runtime)

    def delete_normalization_rule_version_with_options(
        self,
        request: main_models.DeleteNormalizationRuleVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNormalizationRuleVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNormalizationRuleVersion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNormalizationRuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_normalization_rule_version_with_options_async(
        self,
        request: main_models.DeleteNormalizationRuleVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNormalizationRuleVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNormalizationRuleVersion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNormalizationRuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_normalization_rule_version(
        self,
        request: main_models.DeleteNormalizationRuleVersionRequest,
    ) -> main_models.DeleteNormalizationRuleVersionResponse:
        runtime = RuntimeOptions()
        return self.delete_normalization_rule_version_with_options(request, runtime)

    async def delete_normalization_rule_version_async(
        self,
        request: main_models.DeleteNormalizationRuleVersionRequest,
    ) -> main_models.DeleteNormalizationRuleVersionResponse:
        runtime = RuntimeOptions()
        return await self.delete_normalization_rule_version_with_options_async(request, runtime)

    def delete_product_with_options(
        self,
        request: main_models.DeleteProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProduct',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_with_options_async(
        self,
        request: main_models.DeleteProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProduct',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product(
        self,
        request: main_models.DeleteProductRequest,
    ) -> main_models.DeleteProductResponse:
        runtime = RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    async def delete_product_async(
        self,
        request: main_models.DeleteProductRequest,
    ) -> main_models.DeleteProductResponse:
        runtime = RuntimeOptions()
        return await self.delete_product_with_options_async(request, runtime)

    def delete_response_rule_with_options(
        self,
        request: main_models.DeleteResponseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResponseRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.response_rule_id):
            body['ResponseRuleId'] = request.response_rule_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResponseRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResponseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_response_rule_with_options_async(
        self,
        request: main_models.DeleteResponseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResponseRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.response_rule_id):
            body['ResponseRuleId'] = request.response_rule_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteResponseRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResponseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_response_rule(
        self,
        request: main_models.DeleteResponseRuleRequest,
    ) -> main_models.DeleteResponseRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_response_rule_with_options(request, runtime)

    async def delete_response_rule_async(
        self,
        request: main_models.DeleteResponseRuleRequest,
    ) -> main_models.DeleteResponseRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_response_rule_with_options_async(request, runtime)

    def delete_vendor_with_options(
        self,
        request: main_models.DeleteVendorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVendorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVendor',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVendorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vendor_with_options_async(
        self,
        request: main_models.DeleteVendorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVendorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVendor',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVendorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vendor(
        self,
        request: main_models.DeleteVendorRequest,
    ) -> main_models.DeleteVendorResponse:
        runtime = RuntimeOptions()
        return self.delete_vendor_with_options(request, runtime)

    async def delete_vendor_async(
        self,
        request: main_models.DeleteVendorRequest,
    ) -> main_models.DeleteVendorResponse:
        runtime = RuntimeOptions()
        return await self.delete_vendor_with_options_async(request, runtime)

    def disable_data_ingestion_with_options(
        self,
        request: main_models.DisableDataIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDataIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableDataIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDataIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_data_ingestion_with_options_async(
        self,
        request: main_models.DisableDataIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableDataIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisableDataIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableDataIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_data_ingestion(
        self,
        request: main_models.DisableDataIngestionRequest,
    ) -> main_models.DisableDataIngestionResponse:
        runtime = RuntimeOptions()
        return self.disable_data_ingestion_with_options(request, runtime)

    async def disable_data_ingestion_async(
        self,
        request: main_models.DisableDataIngestionRequest,
    ) -> main_models.DisableDataIngestionResponse:
        runtime = RuntimeOptions()
        return await self.disable_data_ingestion_with_options_async(request, runtime)

    def enable_data_ingestion_with_options(
        self,
        request: main_models.EnableDataIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDataIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableDataIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDataIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_data_ingestion_with_options_async(
        self,
        request: main_models.EnableDataIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableDataIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EnableDataIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableDataIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_data_ingestion(
        self,
        request: main_models.EnableDataIngestionRequest,
    ) -> main_models.EnableDataIngestionResponse:
        runtime = RuntimeOptions()
        return self.enable_data_ingestion_with_options(request, runtime)

    async def enable_data_ingestion_async(
        self,
        request: main_models.EnableDataIngestionRequest,
    ) -> main_models.EnableDataIngestionResponse:
        runtime = RuntimeOptions()
        return await self.enable_data_ingestion_with_options_async(request, runtime)

    def execute_log_query_with_options(
        self,
        request: main_models.ExecuteLogQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteLogQueryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_query):
            body['LogQuery'] = request.log_query
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteLogQuery',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteLogQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_log_query_with_options_async(
        self,
        request: main_models.ExecuteLogQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteLogQueryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_query):
            body['LogQuery'] = request.log_query
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteLogQuery',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteLogQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_log_query(
        self,
        request: main_models.ExecuteLogQueryRequest,
    ) -> main_models.ExecuteLogQueryResponse:
        runtime = RuntimeOptions()
        return self.execute_log_query_with_options(request, runtime)

    async def execute_log_query_async(
        self,
        request: main_models.ExecuteLogQueryRequest,
    ) -> main_models.ExecuteLogQueryResponse:
        runtime = RuntimeOptions()
        return await self.execute_log_query_with_options_async(request, runtime)

    def execute_upgrade_with_options(
        self,
        request: main_models.ExecuteUpgradeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteUpgradeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteUpgrade',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteUpgradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_upgrade_with_options_async(
        self,
        request: main_models.ExecuteUpgradeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteUpgradeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteUpgrade',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteUpgradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_upgrade(
        self,
        request: main_models.ExecuteUpgradeRequest,
    ) -> main_models.ExecuteUpgradeResponse:
        runtime = RuntimeOptions()
        return self.execute_upgrade_with_options(request, runtime)

    async def execute_upgrade_async(
        self,
        request: main_models.ExecuteUpgradeRequest,
    ) -> main_models.ExecuteUpgradeResponse:
        runtime = RuntimeOptions()
        return await self.execute_upgrade_with_options_async(request, runtime)

    def get_data_batch_ingestion_with_options(
        self,
        request: main_models.GetDataBatchIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataBatchIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataBatchIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataBatchIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_batch_ingestion_with_options_async(
        self,
        request: main_models.GetDataBatchIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataBatchIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataBatchIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataBatchIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_batch_ingestion(
        self,
        request: main_models.GetDataBatchIngestionRequest,
    ) -> main_models.GetDataBatchIngestionResponse:
        runtime = RuntimeOptions()
        return self.get_data_batch_ingestion_with_options(request, runtime)

    async def get_data_batch_ingestion_async(
        self,
        request: main_models.GetDataBatchIngestionRequest,
    ) -> main_models.GetDataBatchIngestionResponse:
        runtime = RuntimeOptions()
        return await self.get_data_batch_ingestion_with_options_async(request, runtime)

    def get_data_storage_with_options(
        self,
        request: main_models.GetDataStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataStorage',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_data_storage_with_options_async(
        self,
        request: main_models.GetDataStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDataStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDataStorage',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDataStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_data_storage(
        self,
        request: main_models.GetDataStorageRequest,
    ) -> main_models.GetDataStorageResponse:
        runtime = RuntimeOptions()
        return self.get_data_storage_with_options(request, runtime)

    async def get_data_storage_async(
        self,
        request: main_models.GetDataStorageRequest,
    ) -> main_models.GetDataStorageResponse:
        runtime = RuntimeOptions()
        return await self.get_data_storage_with_options_async(request, runtime)

    def get_detection_statistic_with_options(
        self,
        request: main_models.GetDetectionStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDetectionStatisticResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDetectionStatistic',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDetectionStatisticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detection_statistic_with_options_async(
        self,
        request: main_models.GetDetectionStatisticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDetectionStatisticResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetDetectionStatistic',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDetectionStatisticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detection_statistic(
        self,
        request: main_models.GetDetectionStatisticRequest,
    ) -> main_models.GetDetectionStatisticResponse:
        runtime = RuntimeOptions()
        return self.get_detection_statistic_with_options(request, runtime)

    async def get_detection_statistic_async(
        self,
        request: main_models.GetDetectionStatisticRequest,
    ) -> main_models.GetDetectionStatisticResponse:
        runtime = RuntimeOptions()
        return await self.get_detection_statistic_with_options_async(request, runtime)

    def get_export_task_with_options(
        self,
        request: main_models.GetExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExportTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.export_id):
            body['ExportId'] = request.export_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetExportTask',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_export_task_with_options_async(
        self,
        request: main_models.GetExportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExportTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.export_id):
            body['ExportId'] = request.export_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetExportTask',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_export_task(
        self,
        request: main_models.GetExportTaskRequest,
    ) -> main_models.GetExportTaskResponse:
        runtime = RuntimeOptions()
        return self.get_export_task_with_options(request, runtime)

    async def get_export_task_async(
        self,
        request: main_models.GetExportTaskRequest,
    ) -> main_models.GetExportTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_export_task_with_options_async(request, runtime)

    def get_incident_with_options(
        self,
        request: main_models.GetIncidentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIncidentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIncident',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_incident_with_options_async(
        self,
        request: main_models.GetIncidentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIncidentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.incident_uuid):
            body['IncidentUuid'] = request.incident_uuid
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetIncident',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_incident(
        self,
        request: main_models.GetIncidentRequest,
    ) -> main_models.GetIncidentResponse:
        runtime = RuntimeOptions()
        return self.get_incident_with_options(request, runtime)

    async def get_incident_async(
        self,
        request: main_models.GetIncidentRequest,
    ) -> main_models.GetIncidentResponse:
        runtime = RuntimeOptions()
        return await self.get_incident_with_options_async(request, runtime)

    def get_log_ticket_with_options(
        self,
        request: main_models.GetLogTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLogTicket',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_ticket_with_options_async(
        self,
        request: main_models.GetLogTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetLogTicketResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetLogTicket',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_ticket(
        self,
        request: main_models.GetLogTicketRequest,
    ) -> main_models.GetLogTicketResponse:
        runtime = RuntimeOptions()
        return self.get_log_ticket_with_options(request, runtime)

    async def get_log_ticket_async(
        self,
        request: main_models.GetLogTicketRequest,
    ) -> main_models.GetLogTicketResponse:
        runtime = RuntimeOptions()
        return await self.get_log_ticket_with_options_async(request, runtime)

    def get_normalization_rule_with_options(
        self,
        request: main_models.GetNormalizationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNormalizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNormalizationRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNormalizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_normalization_rule_with_options_async(
        self,
        request: main_models.GetNormalizationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNormalizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNormalizationRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNormalizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_normalization_rule(
        self,
        request: main_models.GetNormalizationRuleRequest,
    ) -> main_models.GetNormalizationRuleResponse:
        runtime = RuntimeOptions()
        return self.get_normalization_rule_with_options(request, runtime)

    async def get_normalization_rule_async(
        self,
        request: main_models.GetNormalizationRuleRequest,
    ) -> main_models.GetNormalizationRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_normalization_rule_with_options_async(request, runtime)

    def get_normalization_rule_version_with_options(
        self,
        request: main_models.GetNormalizationRuleVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNormalizationRuleVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNormalizationRuleVersion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNormalizationRuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_normalization_rule_version_with_options_async(
        self,
        request: main_models.GetNormalizationRuleVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNormalizationRuleVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNormalizationRuleVersion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNormalizationRuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_normalization_rule_version(
        self,
        request: main_models.GetNormalizationRuleVersionRequest,
    ) -> main_models.GetNormalizationRuleVersionResponse:
        runtime = RuntimeOptions()
        return self.get_normalization_rule_version_with_options(request, runtime)

    async def get_normalization_rule_version_async(
        self,
        request: main_models.GetNormalizationRuleVersionRequest,
    ) -> main_models.GetNormalizationRuleVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_normalization_rule_version_with_options_async(request, runtime)

    def get_normalization_schema_with_options(
        self,
        request: main_models.GetNormalizationSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNormalizationSchemaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNormalizationSchema',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNormalizationSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_normalization_schema_with_options_async(
        self,
        request: main_models.GetNormalizationSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNormalizationSchemaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNormalizationSchema',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNormalizationSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_normalization_schema(
        self,
        request: main_models.GetNormalizationSchemaRequest,
    ) -> main_models.GetNormalizationSchemaResponse:
        runtime = RuntimeOptions()
        return self.get_normalization_schema_with_options(request, runtime)

    async def get_normalization_schema_async(
        self,
        request: main_models.GetNormalizationSchemaRequest,
    ) -> main_models.GetNormalizationSchemaResponse:
        runtime = RuntimeOptions()
        return await self.get_normalization_schema_with_options_async(request, runtime)

    def get_user_config_with_options(
        self,
        request: main_models.GetUserConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserConfig',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_config_with_options_async(
        self,
        request: main_models.GetUserConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserConfig',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_config(
        self,
        request: main_models.GetUserConfigRequest,
    ) -> main_models.GetUserConfigResponse:
        runtime = RuntimeOptions()
        return self.get_user_config_with_options(request, runtime)

    async def get_user_config_async(
        self,
        request: main_models.GetUserConfigRequest,
    ) -> main_models.GetUserConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_user_config_with_options_async(request, runtime)

    def list_data_ingestion_templates_with_options(
        self,
        request: main_models.ListDataIngestionTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataIngestionTemplatesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_template_status):
            body['DataIngestionTemplateStatus'] = request.data_ingestion_template_status
        if not DaraCore.is_null(request.data_source_template_ids):
            body['DataSourceTemplateIds'] = request.data_source_template_ids
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataIngestionTemplates',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataIngestionTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_ingestion_templates_with_options_async(
        self,
        request: main_models.ListDataIngestionTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataIngestionTemplatesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_template_status):
            body['DataIngestionTemplateStatus'] = request.data_ingestion_template_status
        if not DaraCore.is_null(request.data_source_template_ids):
            body['DataSourceTemplateIds'] = request.data_source_template_ids
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataIngestionTemplates',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataIngestionTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_ingestion_templates(
        self,
        request: main_models.ListDataIngestionTemplatesRequest,
    ) -> main_models.ListDataIngestionTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_data_ingestion_templates_with_options(request, runtime)

    async def list_data_ingestion_templates_async(
        self,
        request: main_models.ListDataIngestionTemplatesRequest,
    ) -> main_models.ListDataIngestionTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_ingestion_templates_with_options_async(request, runtime)

    def list_data_ingestions_with_options(
        self,
        tmp_req: main_models.ListDataIngestionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataIngestionsResponse:
        tmp_req.validate()
        request = main_models.ListDataIngestionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_ingestion_ids):
            request.data_ingestion_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_ingestion_ids, 'DataIngestionIds', 'simple')
        if not DaraCore.is_null(tmp_req.data_ingestion_template_ids):
            request.data_ingestion_template_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_ingestion_template_ids, 'DataIngestionTemplateIds', 'simple')
        if not DaraCore.is_null(tmp_req.normalization_schema_ids):
            request.normalization_schema_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.normalization_schema_ids, 'NormalizationSchemaIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.data_ingestion_ids_shrink):
            body['DataIngestionIds'] = request.data_ingestion_ids_shrink
        if not DaraCore.is_null(request.data_ingestion_status):
            body['DataIngestionStatus'] = request.data_ingestion_status
        if not DaraCore.is_null(request.data_ingestion_template_ids_shrink):
            body['DataIngestionTemplateIds'] = request.data_ingestion_template_ids_shrink
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_schema_ids_shrink):
            body['NormalizationSchemaIds'] = request.normalization_schema_ids_shrink
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataIngestions',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataIngestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_ingestions_with_options_async(
        self,
        tmp_req: main_models.ListDataIngestionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataIngestionsResponse:
        tmp_req.validate()
        request = main_models.ListDataIngestionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_ingestion_ids):
            request.data_ingestion_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_ingestion_ids, 'DataIngestionIds', 'simple')
        if not DaraCore.is_null(tmp_req.data_ingestion_template_ids):
            request.data_ingestion_template_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_ingestion_template_ids, 'DataIngestionTemplateIds', 'simple')
        if not DaraCore.is_null(tmp_req.normalization_schema_ids):
            request.normalization_schema_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.normalization_schema_ids, 'NormalizationSchemaIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.data_ingestion_ids_shrink):
            body['DataIngestionIds'] = request.data_ingestion_ids_shrink
        if not DaraCore.is_null(request.data_ingestion_status):
            body['DataIngestionStatus'] = request.data_ingestion_status
        if not DaraCore.is_null(request.data_ingestion_template_ids_shrink):
            body['DataIngestionTemplateIds'] = request.data_ingestion_template_ids_shrink
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_schema_ids_shrink):
            body['NormalizationSchemaIds'] = request.normalization_schema_ids_shrink
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataIngestions',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataIngestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_ingestions(
        self,
        request: main_models.ListDataIngestionsRequest,
    ) -> main_models.ListDataIngestionsResponse:
        runtime = RuntimeOptions()
        return self.list_data_ingestions_with_options(request, runtime)

    async def list_data_ingestions_async(
        self,
        request: main_models.ListDataIngestionsRequest,
    ) -> main_models.ListDataIngestionsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_ingestions_with_options_async(request, runtime)

    def list_data_set_records_with_options(
        self,
        request: main_models.ListDataSetRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSetRecordsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSetRecords',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSetRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_set_records_with_options_async(
        self,
        request: main_models.ListDataSetRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSetRecordsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSetRecords',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSetRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_set_records(
        self,
        request: main_models.ListDataSetRecordsRequest,
    ) -> main_models.ListDataSetRecordsResponse:
        runtime = RuntimeOptions()
        return self.list_data_set_records_with_options(request, runtime)

    async def list_data_set_records_async(
        self,
        request: main_models.ListDataSetRecordsRequest,
    ) -> main_models.ListDataSetRecordsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_set_records_with_options_async(request, runtime)

    def list_data_sets_with_options(
        self,
        tmp_req: main_models.ListDataSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSetsResponse:
        tmp_req.validate()
        request = main_models.ListDataSetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_set_ids):
            request.data_set_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_set_ids, 'DataSetIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.data_set_ids_shrink):
            body['DataSetIds'] = request.data_set_ids_shrink
        if not DaraCore.is_null(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not DaraCore.is_null(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        if not DaraCore.is_null(request.data_set_type):
            body['DataSetType'] = request.data_set_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not DaraCore.is_null(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSets',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sets_with_options_async(
        self,
        tmp_req: main_models.ListDataSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSetsResponse:
        tmp_req.validate()
        request = main_models.ListDataSetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_set_ids):
            request.data_set_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_set_ids, 'DataSetIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.data_set_ids_shrink):
            body['DataSetIds'] = request.data_set_ids_shrink
        if not DaraCore.is_null(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not DaraCore.is_null(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        if not DaraCore.is_null(request.data_set_type):
            body['DataSetType'] = request.data_set_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not DaraCore.is_null(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSets',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sets(
        self,
        request: main_models.ListDataSetsRequest,
    ) -> main_models.ListDataSetsResponse:
        runtime = RuntimeOptions()
        return self.list_data_sets_with_options(request, runtime)

    async def list_data_sets_async(
        self,
        request: main_models.ListDataSetsRequest,
    ) -> main_models.ListDataSetsResponse:
        runtime = RuntimeOptions()
        return await self.list_data_sets_with_options_async(request, runtime)

    def list_data_source_templates_with_options(
        self,
        tmp_req: main_models.ListDataSourceTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceTemplatesResponse:
        tmp_req.validate()
        request = main_models.ListDataSourceTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source_template_ids):
            request.data_source_template_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_template_ids, 'DataSourceTemplateIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.data_source_template_ids_shrink):
            body['DataSourceTemplateIds'] = request.data_source_template_ids_shrink
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceTemplates',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_templates_with_options_async(
        self,
        tmp_req: main_models.ListDataSourceTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourceTemplatesResponse:
        tmp_req.validate()
        request = main_models.ListDataSourceTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source_template_ids):
            request.data_source_template_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_template_ids, 'DataSourceTemplateIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.data_source_template_ids_shrink):
            body['DataSourceTemplateIds'] = request.data_source_template_ids_shrink
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSourceTemplates',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourceTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_source_templates(
        self,
        request: main_models.ListDataSourceTemplatesRequest,
    ) -> main_models.ListDataSourceTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_data_source_templates_with_options(request, runtime)

    async def list_data_source_templates_async(
        self,
        request: main_models.ListDataSourceTemplatesRequest,
    ) -> main_models.ListDataSourceTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_source_templates_with_options_async(request, runtime)

    def list_data_sources_with_options(
        self,
        tmp_req: main_models.ListDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourcesResponse:
        tmp_req.validate()
        request = main_models.ListDataSourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source_ids):
            request.data_source_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'simple')
        if not DaraCore.is_null(tmp_req.data_source_template_ids):
            request.data_source_template_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_template_ids, 'DataSourceTemplateIds', 'simple')
        if not DaraCore.is_null(tmp_req.log_user_ids):
            request.log_user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not DaraCore.is_null(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not DaraCore.is_null(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_status):
            body['DataSourceStatus'] = request.data_source_status
        if not DaraCore.is_null(request.data_source_store_status):
            body['DataSourceStoreStatus'] = request.data_source_store_status
        if not DaraCore.is_null(request.data_source_template_ids_shrink):
            body['DataSourceTemplateIds'] = request.data_source_template_ids_shrink
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSources',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        tmp_req: main_models.ListDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSourcesResponse:
        tmp_req.validate()
        request = main_models.ListDataSourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source_ids):
            request.data_source_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'simple')
        if not DaraCore.is_null(tmp_req.data_source_template_ids):
            request.data_source_template_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_template_ids, 'DataSourceTemplateIds', 'simple')
        if not DaraCore.is_null(tmp_req.log_user_ids):
            request.log_user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not DaraCore.is_null(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not DaraCore.is_null(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_status):
            body['DataSourceStatus'] = request.data_source_status
        if not DaraCore.is_null(request.data_source_store_status):
            body['DataSourceStoreStatus'] = request.data_source_store_status
        if not DaraCore.is_null(request.data_source_template_ids_shrink):
            body['DataSourceTemplateIds'] = request.data_source_template_ids_shrink
        if not DaraCore.is_null(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            body['Order'] = request.order
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSources',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sources(
        self,
        request: main_models.ListDataSourcesRequest,
    ) -> main_models.ListDataSourcesResponse:
        runtime = RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    async def list_data_sources_async(
        self,
        request: main_models.ListDataSourcesRequest,
    ) -> main_models.ListDataSourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_data_sources_with_options_async(request, runtime)

    def list_detection_rules_with_options(
        self,
        tmp_req: main_models.ListDetectionRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDetectionRulesResponse:
        tmp_req.validate()
        request = main_models.ListDetectionRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detection_rule_ids):
            request.detection_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.detection_rule_ids, 'DetectionRuleIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not DaraCore.is_null(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not DaraCore.is_null(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not DaraCore.is_null(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not DaraCore.is_null(request.detection_rule_ids_shrink):
            body['DetectionRuleIds'] = request.detection_rule_ids_shrink
        if not DaraCore.is_null(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not DaraCore.is_null(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not DaraCore.is_null(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not DaraCore.is_null(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not DaraCore.is_null(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not DaraCore.is_null(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDetectionRules',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDetectionRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_detection_rules_with_options_async(
        self,
        tmp_req: main_models.ListDetectionRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDetectionRulesResponse:
        tmp_req.validate()
        request = main_models.ListDetectionRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detection_rule_ids):
            request.detection_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.detection_rule_ids, 'DetectionRuleIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not DaraCore.is_null(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not DaraCore.is_null(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not DaraCore.is_null(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not DaraCore.is_null(request.detection_rule_ids_shrink):
            body['DetectionRuleIds'] = request.detection_rule_ids_shrink
        if not DaraCore.is_null(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not DaraCore.is_null(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not DaraCore.is_null(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not DaraCore.is_null(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not DaraCore.is_null(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not DaraCore.is_null(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDetectionRules',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDetectionRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_detection_rules(
        self,
        request: main_models.ListDetectionRulesRequest,
    ) -> main_models.ListDetectionRulesResponse:
        runtime = RuntimeOptions()
        return self.list_detection_rules_with_options(request, runtime)

    async def list_detection_rules_async(
        self,
        request: main_models.ListDetectionRulesRequest,
    ) -> main_models.ListDetectionRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_detection_rules_with_options_async(request, runtime)

    def list_incidents_with_options(
        self,
        tmp_req: main_models.ListIncidentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIncidentsResponse:
        tmp_req.validate()
        request = main_models.ListIncidentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.incident_uuids):
            request.incident_uuids_shrink = Utils.array_to_string_with_specified_style(tmp_req.incident_uuids, 'IncidentUuids', 'simple')
        query = {}
        if not DaraCore.is_null(request.incident_name):
            query['IncidentName'] = request.incident_name
        if not DaraCore.is_null(request.incident_uuids_shrink):
            query['IncidentUuids'] = request.incident_uuids_shrink
        body = {}
        if not DaraCore.is_null(request.alert_uuid):
            body['AlertUuid'] = request.alert_uuid
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.incident_status):
            body['IncidentStatus'] = request.incident_status
        if not DaraCore.is_null(request.incident_tags):
            body['IncidentTags'] = request.incident_tags
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not DaraCore.is_null(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not DaraCore.is_null(request.owners):
            body['Owners'] = request.owners
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.relate_asset_id):
            body['RelateAssetId'] = request.relate_asset_id
        if not DaraCore.is_null(request.relate_entity_id):
            body['RelateEntityId'] = request.relate_entity_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListIncidents',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIncidentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_incidents_with_options_async(
        self,
        tmp_req: main_models.ListIncidentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIncidentsResponse:
        tmp_req.validate()
        request = main_models.ListIncidentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.incident_uuids):
            request.incident_uuids_shrink = Utils.array_to_string_with_specified_style(tmp_req.incident_uuids, 'IncidentUuids', 'simple')
        query = {}
        if not DaraCore.is_null(request.incident_name):
            query['IncidentName'] = request.incident_name
        if not DaraCore.is_null(request.incident_uuids_shrink):
            query['IncidentUuids'] = request.incident_uuids_shrink
        body = {}
        if not DaraCore.is_null(request.alert_uuid):
            body['AlertUuid'] = request.alert_uuid
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.incident_status):
            body['IncidentStatus'] = request.incident_status
        if not DaraCore.is_null(request.incident_tags):
            body['IncidentTags'] = request.incident_tags
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_direction):
            body['OrderDirection'] = request.order_direction
        if not DaraCore.is_null(request.order_field_name):
            body['OrderFieldName'] = request.order_field_name
        if not DaraCore.is_null(request.owners):
            body['Owners'] = request.owners
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.relate_asset_id):
            body['RelateAssetId'] = request.relate_asset_id
        if not DaraCore.is_null(request.relate_entity_id):
            body['RelateEntityId'] = request.relate_entity_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.threat_level):
            body['ThreatLevel'] = request.threat_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListIncidents',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIncidentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_incidents(
        self,
        request: main_models.ListIncidentsRequest,
    ) -> main_models.ListIncidentsResponse:
        runtime = RuntimeOptions()
        return self.list_incidents_with_options(request, runtime)

    async def list_incidents_async(
        self,
        request: main_models.ListIncidentsRequest,
    ) -> main_models.ListIncidentsResponse:
        runtime = RuntimeOptions()
        return await self.list_incidents_with_options_async(request, runtime)

    def list_log_projects_with_options(
        self,
        request: main_models.ListLogProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLogProjectsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLogProjects',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_projects_with_options_async(
        self,
        request: main_models.ListLogProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLogProjectsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLogProjects',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_projects(
        self,
        request: main_models.ListLogProjectsRequest,
    ) -> main_models.ListLogProjectsResponse:
        runtime = RuntimeOptions()
        return self.list_log_projects_with_options(request, runtime)

    async def list_log_projects_async(
        self,
        request: main_models.ListLogProjectsRequest,
    ) -> main_models.ListLogProjectsResponse:
        runtime = RuntimeOptions()
        return await self.list_log_projects_with_options_async(request, runtime)

    def list_log_regions_with_options(
        self,
        request: main_models.ListLogRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLogRegionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLogRegions',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_regions_with_options_async(
        self,
        request: main_models.ListLogRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLogRegionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLogRegions',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_regions(
        self,
        request: main_models.ListLogRegionsRequest,
    ) -> main_models.ListLogRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_log_regions_with_options(request, runtime)

    async def list_log_regions_async(
        self,
        request: main_models.ListLogRegionsRequest,
    ) -> main_models.ListLogRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_log_regions_with_options_async(request, runtime)

    def list_log_stores_with_options(
        self,
        request: main_models.ListLogStoresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLogStoresResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLogStores',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_log_stores_with_options_async(
        self,
        request: main_models.ListLogStoresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLogStoresResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListLogStores',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_log_stores(
        self,
        request: main_models.ListLogStoresRequest,
    ) -> main_models.ListLogStoresResponse:
        runtime = RuntimeOptions()
        return self.list_log_stores_with_options(request, runtime)

    async def list_log_stores_async(
        self,
        request: main_models.ListLogStoresRequest,
    ) -> main_models.ListLogStoresResponse:
        runtime = RuntimeOptions()
        return await self.list_log_stores_with_options_async(request, runtime)

    def list_normalization_categories_with_options(
        self,
        request: main_models.ListNormalizationCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationCategoriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.normalization_category_type):
            body['NormalizationCategoryType'] = request.normalization_category_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationCategories',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_categories_with_options_async(
        self,
        request: main_models.ListNormalizationCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationCategoriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.normalization_category_type):
            body['NormalizationCategoryType'] = request.normalization_category_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationCategories',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_categories(
        self,
        request: main_models.ListNormalizationCategoriesRequest,
    ) -> main_models.ListNormalizationCategoriesResponse:
        runtime = RuntimeOptions()
        return self.list_normalization_categories_with_options(request, runtime)

    async def list_normalization_categories_async(
        self,
        request: main_models.ListNormalizationCategoriesRequest,
    ) -> main_models.ListNormalizationCategoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_normalization_categories_with_options_async(request, runtime)

    def list_normalization_fields_with_options(
        self,
        request: main_models.ListNormalizationFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationFieldsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationFields',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_fields_with_options_async(
        self,
        request: main_models.ListNormalizationFieldsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationFieldsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationFields',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_fields(
        self,
        request: main_models.ListNormalizationFieldsRequest,
    ) -> main_models.ListNormalizationFieldsResponse:
        runtime = RuntimeOptions()
        return self.list_normalization_fields_with_options(request, runtime)

    async def list_normalization_fields_async(
        self,
        request: main_models.ListNormalizationFieldsRequest,
    ) -> main_models.ListNormalizationFieldsResponse:
        runtime = RuntimeOptions()
        return await self.list_normalization_fields_with_options_async(request, runtime)

    def list_normalization_rule_capacities_with_options(
        self,
        tmp_req: main_models.ListNormalizationRuleCapacitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationRuleCapacitiesResponse:
        tmp_req.validate()
        request = main_models.ListNormalizationRuleCapacitiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationRuleCapacities',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationRuleCapacitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_rule_capacities_with_options_async(
        self,
        tmp_req: main_models.ListNormalizationRuleCapacitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationRuleCapacitiesResponse:
        tmp_req.validate()
        request = main_models.ListNormalizationRuleCapacitiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationRuleCapacities',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationRuleCapacitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_rule_capacities(
        self,
        request: main_models.ListNormalizationRuleCapacitiesRequest,
    ) -> main_models.ListNormalizationRuleCapacitiesResponse:
        runtime = RuntimeOptions()
        return self.list_normalization_rule_capacities_with_options(request, runtime)

    async def list_normalization_rule_capacities_async(
        self,
        request: main_models.ListNormalizationRuleCapacitiesRequest,
    ) -> main_models.ListNormalizationRuleCapacitiesResponse:
        runtime = RuntimeOptions()
        return await self.list_normalization_rule_capacities_with_options_async(request, runtime)

    def list_normalization_rule_versions_with_options(
        self,
        request: main_models.ListNormalizationRuleVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationRuleVersionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationRuleVersions',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationRuleVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_rule_versions_with_options_async(
        self,
        request: main_models.ListNormalizationRuleVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationRuleVersionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationRuleVersions',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationRuleVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_rule_versions(
        self,
        request: main_models.ListNormalizationRuleVersionsRequest,
    ) -> main_models.ListNormalizationRuleVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_normalization_rule_versions_with_options(request, runtime)

    async def list_normalization_rule_versions_async(
        self,
        request: main_models.ListNormalizationRuleVersionsRequest,
    ) -> main_models.ListNormalizationRuleVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_normalization_rule_versions_with_options_async(request, runtime)

    def list_normalization_rules_with_options(
        self,
        tmp_req: main_models.ListNormalizationRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationRulesResponse:
        tmp_req.validate()
        request = main_models.ListNormalizationRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not DaraCore.is_null(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not DaraCore.is_null(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.order_type):
            body['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationRules',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_rules_with_options_async(
        self,
        tmp_req: main_models.ListNormalizationRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationRulesResponse:
        tmp_req.validate()
        request = main_models.ListNormalizationRulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not DaraCore.is_null(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not DaraCore.is_null(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.order_type):
            body['OrderType'] = request.order_type
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationRules',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_rules(
        self,
        request: main_models.ListNormalizationRulesRequest,
    ) -> main_models.ListNormalizationRulesResponse:
        runtime = RuntimeOptions()
        return self.list_normalization_rules_with_options(request, runtime)

    async def list_normalization_rules_async(
        self,
        request: main_models.ListNormalizationRulesRequest,
    ) -> main_models.ListNormalizationRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_normalization_rules_with_options_async(request, runtime)

    def list_normalization_schemas_with_options(
        self,
        request: main_models.ListNormalizationSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationSchemasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationSchemas',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_normalization_schemas_with_options_async(
        self,
        request: main_models.ListNormalizationSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNormalizationSchemasResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNormalizationSchemas',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNormalizationSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_normalization_schemas(
        self,
        request: main_models.ListNormalizationSchemasRequest,
    ) -> main_models.ListNormalizationSchemasResponse:
        runtime = RuntimeOptions()
        return self.list_normalization_schemas_with_options(request, runtime)

    async def list_normalization_schemas_async(
        self,
        request: main_models.ListNormalizationSchemasRequest,
    ) -> main_models.ListNormalizationSchemasResponse:
        runtime = RuntimeOptions()
        return await self.list_normalization_schemas_with_options_async(request, runtime)

    def list_products_with_options(
        self,
        tmp_req: main_models.ListProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        tmp_req.validate()
        request = main_models.ListProductsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.product_ids):
            request.product_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.product_ids, 'ProductIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_ids_shrink):
            body['ProductIds'] = request.product_ids_shrink
        if not DaraCore.is_null(request.product_name):
            body['ProductName'] = request.product_name
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        tmp_req: main_models.ListProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        tmp_req.validate()
        request = main_models.ListProductsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.product_ids):
            request.product_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.product_ids, 'ProductIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_ids_shrink):
            body['ProductIds'] = request.product_ids_shrink
        if not DaraCore.is_null(request.product_name):
            body['ProductName'] = request.product_name
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        return self.list_products_with_options(request, runtime)

    async def list_products_async(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        return await self.list_products_with_options_async(request, runtime)

    def list_response_rules_with_options(
        self,
        request: main_models.ListResponseRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResponseRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.response_action_type):
            body['ResponseActionType'] = request.response_action_type
        if not DaraCore.is_null(request.response_rule_name):
            body['ResponseRuleName'] = request.response_rule_name
        if not DaraCore.is_null(request.response_rule_status):
            body['ResponseRuleStatus'] = request.response_rule_status
        if not DaraCore.is_null(request.response_rule_type):
            body['ResponseRuleType'] = request.response_rule_type
        if not DaraCore.is_null(request.response_trigger_type):
            body['ResponseTriggerType'] = request.response_trigger_type
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListResponseRules',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResponseRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_response_rules_with_options_async(
        self,
        request: main_models.ListResponseRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResponseRulesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.response_action_type):
            body['ResponseActionType'] = request.response_action_type
        if not DaraCore.is_null(request.response_rule_name):
            body['ResponseRuleName'] = request.response_rule_name
        if not DaraCore.is_null(request.response_rule_status):
            body['ResponseRuleStatus'] = request.response_rule_status
        if not DaraCore.is_null(request.response_rule_type):
            body['ResponseRuleType'] = request.response_rule_type
        if not DaraCore.is_null(request.response_trigger_type):
            body['ResponseTriggerType'] = request.response_trigger_type
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.role_type):
            body['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListResponseRules',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResponseRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_response_rules(
        self,
        request: main_models.ListResponseRulesRequest,
    ) -> main_models.ListResponseRulesResponse:
        runtime = RuntimeOptions()
        return self.list_response_rules_with_options(request, runtime)

    async def list_response_rules_async(
        self,
        request: main_models.ListResponseRulesRequest,
    ) -> main_models.ListResponseRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_response_rules_with_options_async(request, runtime)

    def list_traffic_statistics_with_options(
        self,
        tmp_req: main_models.ListTrafficStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTrafficStatisticsResponse:
        tmp_req.validate()
        request = main_models.ListTrafficStatisticsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.log_user_ids):
            request.log_user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_tag):
            body['RegionTag'] = request.region_tag
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.traffic_statistic_period):
            body['TrafficStatisticPeriod'] = request.traffic_statistic_period
        if not DaraCore.is_null(request.traffic_statistic_period_type):
            body['TrafficStatisticPeriodType'] = request.traffic_statistic_period_type
        if not DaraCore.is_null(request.traffic_statistic_type):
            body['TrafficStatisticType'] = request.traffic_statistic_type
        if not DaraCore.is_null(request.traffic_type):
            body['TrafficType'] = request.traffic_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTrafficStatistics',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrafficStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_traffic_statistics_with_options_async(
        self,
        tmp_req: main_models.ListTrafficStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTrafficStatisticsResponse:
        tmp_req.validate()
        request = main_models.ListTrafficStatisticsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.log_user_ids):
            request.log_user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_tag):
            body['RegionTag'] = request.region_tag
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.traffic_statistic_period):
            body['TrafficStatisticPeriod'] = request.traffic_statistic_period
        if not DaraCore.is_null(request.traffic_statistic_period_type):
            body['TrafficStatisticPeriodType'] = request.traffic_statistic_period_type
        if not DaraCore.is_null(request.traffic_statistic_type):
            body['TrafficStatisticType'] = request.traffic_statistic_type
        if not DaraCore.is_null(request.traffic_type):
            body['TrafficType'] = request.traffic_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTrafficStatistics',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTrafficStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_traffic_statistics(
        self,
        request: main_models.ListTrafficStatisticsRequest,
    ) -> main_models.ListTrafficStatisticsResponse:
        runtime = RuntimeOptions()
        return self.list_traffic_statistics_with_options(request, runtime)

    async def list_traffic_statistics_async(
        self,
        request: main_models.ListTrafficStatisticsRequest,
    ) -> main_models.ListTrafficStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.list_traffic_statistics_with_options_async(request, runtime)

    def list_upgrade_items_with_options(
        self,
        request: main_models.ListUpgradeItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUpgradeItemsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUpgradeItems',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUpgradeItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_upgrade_items_with_options_async(
        self,
        request: main_models.ListUpgradeItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUpgradeItemsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListUpgradeItems',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUpgradeItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_upgrade_items(
        self,
        request: main_models.ListUpgradeItemsRequest,
    ) -> main_models.ListUpgradeItemsResponse:
        runtime = RuntimeOptions()
        return self.list_upgrade_items_with_options(request, runtime)

    async def list_upgrade_items_async(
        self,
        request: main_models.ListUpgradeItemsRequest,
    ) -> main_models.ListUpgradeItemsResponse:
        runtime = RuntimeOptions()
        return await self.list_upgrade_items_with_options_async(request, runtime)

    def list_vendors_with_options(
        self,
        tmp_req: main_models.ListVendorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVendorsResponse:
        tmp_req.validate()
        request = main_models.ListVendorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vendor_ids):
            request.vendor_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.vendor_ids, 'VendorIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_ids_shrink):
            body['VendorIds'] = request.vendor_ids_shrink
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        if not DaraCore.is_null(request.vendor_type):
            body['VendorType'] = request.vendor_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVendors',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVendorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vendors_with_options_async(
        self,
        tmp_req: main_models.ListVendorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVendorsResponse:
        tmp_req.validate()
        request = main_models.ListVendorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.vendor_ids):
            request.vendor_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.vendor_ids, 'VendorIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_ids_shrink):
            body['VendorIds'] = request.vendor_ids_shrink
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        if not DaraCore.is_null(request.vendor_type):
            body['VendorType'] = request.vendor_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVendors',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVendorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vendors(
        self,
        request: main_models.ListVendorsRequest,
    ) -> main_models.ListVendorsResponse:
        runtime = RuntimeOptions()
        return self.list_vendors_with_options(request, runtime)

    async def list_vendors_async(
        self,
        request: main_models.ListVendorsRequest,
    ) -> main_models.ListVendorsResponse:
        runtime = RuntimeOptions()
        return await self.list_vendors_with_options_async(request, runtime)

    def refresh_data_source_with_options(
        self,
        request: main_models.RefreshDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefreshDataSource',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_data_source_with_options_async(
        self,
        request: main_models.RefreshDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RefreshDataSource',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_data_source(
        self,
        request: main_models.RefreshDataSourceRequest,
    ) -> main_models.RefreshDataSourceResponse:
        runtime = RuntimeOptions()
        return self.refresh_data_source_with_options(request, runtime)

    async def refresh_data_source_async(
        self,
        request: main_models.RefreshDataSourceRequest,
    ) -> main_models.RefreshDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.refresh_data_source_with_options_async(request, runtime)

    def reset_data_storage_with_options(
        self,
        request: main_models.ResetDataStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetDataStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetDataStorage',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetDataStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_data_storage_with_options_async(
        self,
        request: main_models.ResetDataStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetDataStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResetDataStorage',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetDataStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_data_storage(
        self,
        request: main_models.ResetDataStorageRequest,
    ) -> main_models.ResetDataStorageResponse:
        runtime = RuntimeOptions()
        return self.reset_data_storage_with_options(request, runtime)

    async def reset_data_storage_async(
        self,
        request: main_models.ResetDataStorageRequest,
    ) -> main_models.ResetDataStorageResponse:
        runtime = RuntimeOptions()
        return await self.reset_data_storage_with_options_async(request, runtime)

    def set_default_normalization_rule_version_with_options(
        self,
        request: main_models.SetDefaultNormalizationRuleVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultNormalizationRuleVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultNormalizationRuleVersion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultNormalizationRuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_normalization_rule_version_with_options_async(
        self,
        request: main_models.SetDefaultNormalizationRuleVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDefaultNormalizationRuleVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.normalization_rule_version):
            body['NormalizationRuleVersion'] = request.normalization_rule_version
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetDefaultNormalizationRuleVersion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDefaultNormalizationRuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_normalization_rule_version(
        self,
        request: main_models.SetDefaultNormalizationRuleVersionRequest,
    ) -> main_models.SetDefaultNormalizationRuleVersionResponse:
        runtime = RuntimeOptions()
        return self.set_default_normalization_rule_version_with_options(request, runtime)

    async def set_default_normalization_rule_version_async(
        self,
        request: main_models.SetDefaultNormalizationRuleVersionRequest,
    ) -> main_models.SetDefaultNormalizationRuleVersionResponse:
        runtime = RuntimeOptions()
        return await self.set_default_normalization_rule_version_with_options_async(request, runtime)

    def update_data_batch_ingestion_with_options(
        self,
        tmp_req: main_models.UpdateDataBatchIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataBatchIngestionResponse:
        tmp_req.validate()
        request = main_models.UpdateDataBatchIngestionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_ingestion_ids):
            request.data_ingestion_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_ingestion_ids, 'DataIngestionIds', 'simple')
        if not DaraCore.is_null(tmp_req.log_user_ids):
            request.log_user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.auto_scan_new):
            body['AutoScanNew'] = request.auto_scan_new
        if not DaraCore.is_null(request.data_batch_ingestion_mode):
            body['DataBatchIngestionMode'] = request.data_batch_ingestion_mode
        if not DaraCore.is_null(request.data_ingestion_ids_shrink):
            body['DataIngestionIds'] = request.data_ingestion_ids_shrink
        if not DaraCore.is_null(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataBatchIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataBatchIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_batch_ingestion_with_options_async(
        self,
        tmp_req: main_models.UpdateDataBatchIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataBatchIngestionResponse:
        tmp_req.validate()
        request = main_models.UpdateDataBatchIngestionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_ingestion_ids):
            request.data_ingestion_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_ingestion_ids, 'DataIngestionIds', 'simple')
        if not DaraCore.is_null(tmp_req.log_user_ids):
            request.log_user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.auto_scan_new):
            body['AutoScanNew'] = request.auto_scan_new
        if not DaraCore.is_null(request.data_batch_ingestion_mode):
            body['DataBatchIngestionMode'] = request.data_batch_ingestion_mode
        if not DaraCore.is_null(request.data_ingestion_ids_shrink):
            body['DataIngestionIds'] = request.data_ingestion_ids_shrink
        if not DaraCore.is_null(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataBatchIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataBatchIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_batch_ingestion(
        self,
        request: main_models.UpdateDataBatchIngestionRequest,
    ) -> main_models.UpdateDataBatchIngestionResponse:
        runtime = RuntimeOptions()
        return self.update_data_batch_ingestion_with_options(request, runtime)

    async def update_data_batch_ingestion_async(
        self,
        request: main_models.UpdateDataBatchIngestionRequest,
    ) -> main_models.UpdateDataBatchIngestionResponse:
        runtime = RuntimeOptions()
        return await self.update_data_batch_ingestion_with_options_async(request, runtime)

    def update_data_ingestion_with_options(
        self,
        request: main_models.UpdateDataIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not DaraCore.is_null(request.data_ingestion_mode):
            body['DataIngestionMode'] = request.data_ingestion_mode
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataIngestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_ingestion_with_options_async(
        self,
        request: main_models.UpdateDataIngestionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataIngestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_id):
            body['DataIngestionId'] = request.data_ingestion_id
        if not DaraCore.is_null(request.data_ingestion_mode):
            body['DataIngestionMode'] = request.data_ingestion_mode
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataIngestion',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataIngestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_ingestion(
        self,
        request: main_models.UpdateDataIngestionRequest,
    ) -> main_models.UpdateDataIngestionResponse:
        runtime = RuntimeOptions()
        return self.update_data_ingestion_with_options(request, runtime)

    async def update_data_ingestion_async(
        self,
        request: main_models.UpdateDataIngestionRequest,
    ) -> main_models.UpdateDataIngestionResponse:
        runtime = RuntimeOptions()
        return await self.update_data_ingestion_with_options_async(request, runtime)

    def update_data_ingestion_template_with_options(
        self,
        request: main_models.UpdateDataIngestionTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataIngestionTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_status):
            body['DataIngestionStatus'] = request.data_ingestion_status
        if not DaraCore.is_null(request.data_ingestion_template_id):
            body['DataIngestionTemplateId'] = request.data_ingestion_template_id
        if not DaraCore.is_null(request.data_ingestion_template_name):
            body['DataIngestionTemplateName'] = request.data_ingestion_template_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataIngestionTemplate',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataIngestionTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_ingestion_template_with_options_async(
        self,
        request: main_models.UpdateDataIngestionTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataIngestionTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_ingestion_status):
            body['DataIngestionStatus'] = request.data_ingestion_status
        if not DaraCore.is_null(request.data_ingestion_template_id):
            body['DataIngestionTemplateId'] = request.data_ingestion_template_id
        if not DaraCore.is_null(request.data_ingestion_template_name):
            body['DataIngestionTemplateName'] = request.data_ingestion_template_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataIngestionTemplate',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataIngestionTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_ingestion_template(
        self,
        request: main_models.UpdateDataIngestionTemplateRequest,
    ) -> main_models.UpdateDataIngestionTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_data_ingestion_template_with_options(request, runtime)

    async def update_data_ingestion_template_async(
        self,
        request: main_models.UpdateDataIngestionTemplateRequest,
    ) -> main_models.UpdateDataIngestionTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_data_ingestion_template_with_options_async(request, runtime)

    def update_data_set_with_options(
        self,
        request: main_models.UpdateDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_description):
            body['DataSetDescription'] = request.data_set_description
        if not DaraCore.is_null(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not DaraCore.is_null(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        body_flat = {}
        if not DaraCore.is_null(request.ip_whitelist_recognizers):
            body_flat['IpWhitelistRecognizers'] = request.ip_whitelist_recognizers
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSet',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_set_with_options_async(
        self,
        request: main_models.UpdateDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSetResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_description):
            body['DataSetDescription'] = request.data_set_description
        if not DaraCore.is_null(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.data_set_name):
            body['DataSetName'] = request.data_set_name
        if not DaraCore.is_null(request.data_set_status):
            body['DataSetStatus'] = request.data_set_status
        body_flat = {}
        if not DaraCore.is_null(request.ip_whitelist_recognizers):
            body_flat['IpWhitelistRecognizers'] = request.ip_whitelist_recognizers
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSet',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_set(
        self,
        request: main_models.UpdateDataSetRequest,
    ) -> main_models.UpdateDataSetResponse:
        runtime = RuntimeOptions()
        return self.update_data_set_with_options(request, runtime)

    async def update_data_set_async(
        self,
        request: main_models.UpdateDataSetRequest,
    ) -> main_models.UpdateDataSetResponse:
        runtime = RuntimeOptions()
        return await self.update_data_set_with_options_async(request, runtime)

    def update_data_set_record_with_options(
        self,
        request: main_models.UpdateDataSetRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSetRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.data_set_records):
            body['DataSetRecords'] = request.data_set_records
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSetRecord',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSetRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_set_record_with_options_async(
        self,
        request: main_models.UpdateDataSetRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSetRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_set_file_name):
            body['DataSetFileName'] = request.data_set_file_name
        if not DaraCore.is_null(request.data_set_id):
            body['DataSetId'] = request.data_set_id
        if not DaraCore.is_null(request.data_set_records):
            body['DataSetRecords'] = request.data_set_records
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSetRecord',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSetRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_set_record(
        self,
        request: main_models.UpdateDataSetRecordRequest,
    ) -> main_models.UpdateDataSetRecordResponse:
        runtime = RuntimeOptions()
        return self.update_data_set_record_with_options(request, runtime)

    async def update_data_set_record_async(
        self,
        request: main_models.UpdateDataSetRecordRequest,
    ) -> main_models.UpdateDataSetRecordResponse:
        runtime = RuntimeOptions()
        return await self.update_data_set_record_with_options_async(request, runtime)

    def update_data_source_with_options(
        self,
        request: main_models.UpdateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        body_flat = {}
        if not DaraCore.is_null(request.data_source_stores):
            body_flat['DataSourceStores'] = request.data_source_stores
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSource',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_with_options_async(
        self,
        request: main_models.UpdateDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_source_from):
            body['DataSourceFrom'] = request.data_source_from
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not DaraCore.is_null(request.data_source_recognize_enabled):
            body['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        body_flat = {}
        if not DaraCore.is_null(request.data_source_stores):
            body_flat['DataSourceStores'] = request.data_source_stores
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSource',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source(
        self,
        request: main_models.UpdateDataSourceRequest,
    ) -> main_models.UpdateDataSourceResponse:
        runtime = RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    async def update_data_source_async(
        self,
        request: main_models.UpdateDataSourceRequest,
    ) -> main_models.UpdateDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.update_data_source_with_options_async(request, runtime)

    def update_data_source_template_with_options(
        self,
        tmp_req: main_models.UpdateDataSourceTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateDataSourceTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.log_user_ids):
            request.log_user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.data_source_recognize_enabled):
            query['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        body = {}
        if not DaraCore.is_null(request.auto_scan_new):
            body['AutoScanNew'] = request.auto_scan_new
        if not DaraCore.is_null(request.data_source_template_id):
            body['DataSourceTemplateId'] = request.data_source_template_id
        if not DaraCore.is_null(request.data_source_template_name):
            body['DataSourceTemplateName'] = request.data_source_template_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_pattern):
            body['LogProjectPattern'] = request.log_project_pattern
        if not DaraCore.is_null(request.log_region_ids):
            body['LogRegionIds'] = request.log_region_ids
        if not DaraCore.is_null(request.log_store_pattern):
            body['LogStorePattern'] = request.log_store_pattern
        if not DaraCore.is_null(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSourceTemplate',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_template_with_options_async(
        self,
        tmp_req: main_models.UpdateDataSourceTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataSourceTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateDataSourceTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.log_user_ids):
            request.log_user_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.log_user_ids, 'LogUserIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.data_source_recognize_enabled):
            query['DataSourceRecognizeEnabled'] = request.data_source_recognize_enabled
        body = {}
        if not DaraCore.is_null(request.auto_scan_new):
            body['AutoScanNew'] = request.auto_scan_new
        if not DaraCore.is_null(request.data_source_template_id):
            body['DataSourceTemplateId'] = request.data_source_template_id
        if not DaraCore.is_null(request.data_source_template_name):
            body['DataSourceTemplateName'] = request.data_source_template_name
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_pattern):
            body['LogProjectPattern'] = request.log_project_pattern
        if not DaraCore.is_null(request.log_region_ids):
            body['LogRegionIds'] = request.log_region_ids
        if not DaraCore.is_null(request.log_store_pattern):
            body['LogStorePattern'] = request.log_store_pattern
        if not DaraCore.is_null(request.log_user_ids_shrink):
            body['LogUserIds'] = request.log_user_ids_shrink
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataSourceTemplate',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataSourceTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_source_template(
        self,
        request: main_models.UpdateDataSourceTemplateRequest,
    ) -> main_models.UpdateDataSourceTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_data_source_template_with_options(request, runtime)

    async def update_data_source_template_async(
        self,
        request: main_models.UpdateDataSourceTemplateRequest,
    ) -> main_models.UpdateDataSourceTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_data_source_template_with_options_async(request, runtime)

    def update_data_storage_with_options(
        self,
        request: main_models.UpdateDataStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_storage_region_id):
            body['DataStorageRegionId'] = request.data_storage_region_id
        if not DaraCore.is_null(request.delivery_status):
            body['DeliveryStatus'] = request.delivery_status
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataStorage',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_storage_with_options_async(
        self,
        request: main_models.UpdateDataStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataStorageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data_storage_region_id):
            body['DataStorageRegionId'] = request.data_storage_region_id
        if not DaraCore.is_null(request.delivery_status):
            body['DeliveryStatus'] = request.delivery_status
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataStorage',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_storage(
        self,
        request: main_models.UpdateDataStorageRequest,
    ) -> main_models.UpdateDataStorageResponse:
        runtime = RuntimeOptions()
        return self.update_data_storage_with_options(request, runtime)

    async def update_data_storage_async(
        self,
        request: main_models.UpdateDataStorageRequest,
    ) -> main_models.UpdateDataStorageResponse:
        runtime = RuntimeOptions()
        return await self.update_data_storage_with_options_async(request, runtime)

    def update_data_storage_delivery_with_options(
        self,
        request: main_models.UpdateDataStorageDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataStorageDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_code):
            body['LogCode'] = request.log_code
        if not DaraCore.is_null(request.log_delivery_status):
            body['LogDeliveryStatus'] = request.log_delivery_status
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataStorageDelivery',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataStorageDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_storage_delivery_with_options_async(
        self,
        request: main_models.UpdateDataStorageDeliveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataStorageDeliveryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_code):
            body['LogCode'] = request.log_code
        if not DaraCore.is_null(request.log_delivery_status):
            body['LogDeliveryStatus'] = request.log_delivery_status
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataStorageDelivery',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataStorageDeliveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_storage_delivery(
        self,
        request: main_models.UpdateDataStorageDeliveryRequest,
    ) -> main_models.UpdateDataStorageDeliveryResponse:
        runtime = RuntimeOptions()
        return self.update_data_storage_delivery_with_options(request, runtime)

    async def update_data_storage_delivery_async(
        self,
        request: main_models.UpdateDataStorageDeliveryRequest,
    ) -> main_models.UpdateDataStorageDeliveryResponse:
        runtime = RuntimeOptions()
        return await self.update_data_storage_delivery_with_options_async(request, runtime)

    def update_data_storage_ttl_with_options(
        self,
        request: main_models.UpdateDataStorageTtlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataStorageTtlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_store_cold_ttl):
            body['LogStoreColdTtl'] = request.log_store_cold_ttl
        if not DaraCore.is_null(request.log_store_hot_ttl):
            body['LogStoreHotTtl'] = request.log_store_hot_ttl
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_store_ttl):
            body['LogStoreTtl'] = request.log_store_ttl
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataStorageTtl',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataStorageTtlResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_storage_ttl_with_options_async(
        self,
        request: main_models.UpdateDataStorageTtlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDataStorageTtlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_store_cold_ttl):
            body['LogStoreColdTtl'] = request.log_store_cold_ttl
        if not DaraCore.is_null(request.log_store_hot_ttl):
            body['LogStoreHotTtl'] = request.log_store_hot_ttl
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_store_ttl):
            body['LogStoreTtl'] = request.log_store_ttl
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataStorageTtl',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDataStorageTtlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_data_storage_ttl(
        self,
        request: main_models.UpdateDataStorageTtlRequest,
    ) -> main_models.UpdateDataStorageTtlResponse:
        runtime = RuntimeOptions()
        return self.update_data_storage_ttl_with_options(request, runtime)

    async def update_data_storage_ttl_async(
        self,
        request: main_models.UpdateDataStorageTtlRequest,
    ) -> main_models.UpdateDataStorageTtlResponse:
        runtime = RuntimeOptions()
        return await self.update_data_storage_ttl_with_options_async(request, runtime)

    def update_detection_rule_with_options(
        self,
        request: main_models.UpdateDetectionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDetectionRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not DaraCore.is_null(request.alert_description):
            body['AlertDescription'] = request.alert_description
        if not DaraCore.is_null(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_schema_id):
            body['AlertSchemaId'] = request.alert_schema_id
        if not DaraCore.is_null(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not DaraCore.is_null(request.alert_threshold_count):
            body['AlertThresholdCount'] = request.alert_threshold_count
        if not DaraCore.is_null(request.alert_threshold_group):
            body['AlertThresholdGroup'] = request.alert_threshold_group
        if not DaraCore.is_null(request.alert_threshold_period):
            body['AlertThresholdPeriod'] = request.alert_threshold_period
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.detection_expression_content):
            body['DetectionExpressionContent'] = request.detection_expression_content
        if not DaraCore.is_null(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not DaraCore.is_null(request.detection_rule_description):
            body['DetectionRuleDescription'] = request.detection_rule_description
        if not DaraCore.is_null(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not DaraCore.is_null(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not DaraCore.is_null(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not DaraCore.is_null(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not DaraCore.is_null(request.entity_mappings):
            body['EntityMappings'] = request.entity_mappings
        if not DaraCore.is_null(request.incident_aggregation_expression):
            body['IncidentAggregationExpression'] = request.incident_aggregation_expression
        if not DaraCore.is_null(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not DaraCore.is_null(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not DaraCore.is_null(request.playbook_parameters):
            body['PlaybookParameters'] = request.playbook_parameters
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schedule_begin_time):
            body['ScheduleBeginTime'] = request.schedule_begin_time
        if not DaraCore.is_null(request.schedule_expression):
            body['ScheduleExpression'] = request.schedule_expression
        if not DaraCore.is_null(request.schedule_max_retries):
            body['ScheduleMaxRetries'] = request.schedule_max_retries
        if not DaraCore.is_null(request.schedule_max_timeout):
            body['ScheduleMaxTimeout'] = request.schedule_max_timeout
        if not DaraCore.is_null(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.schedule_window):
            body['ScheduleWindow'] = request.schedule_window
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDetectionRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDetectionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_detection_rule_with_options_async(
        self,
        request: main_models.UpdateDetectionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDetectionRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_att_ck):
            body['AlertAttCk'] = request.alert_att_ck
        if not DaraCore.is_null(request.alert_description):
            body['AlertDescription'] = request.alert_description
        if not DaraCore.is_null(request.alert_level):
            body['AlertLevel'] = request.alert_level
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_schema_id):
            body['AlertSchemaId'] = request.alert_schema_id
        if not DaraCore.is_null(request.alert_tactic_id):
            body['AlertTacticId'] = request.alert_tactic_id
        if not DaraCore.is_null(request.alert_threshold_count):
            body['AlertThresholdCount'] = request.alert_threshold_count
        if not DaraCore.is_null(request.alert_threshold_group):
            body['AlertThresholdGroup'] = request.alert_threshold_group
        if not DaraCore.is_null(request.alert_threshold_period):
            body['AlertThresholdPeriod'] = request.alert_threshold_period
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.detection_expression_content):
            body['DetectionExpressionContent'] = request.detection_expression_content
        if not DaraCore.is_null(request.detection_expression_type):
            body['DetectionExpressionType'] = request.detection_expression_type
        if not DaraCore.is_null(request.detection_rule_description):
            body['DetectionRuleDescription'] = request.detection_rule_description
        if not DaraCore.is_null(request.detection_rule_id):
            body['DetectionRuleId'] = request.detection_rule_id
        if not DaraCore.is_null(request.detection_rule_name):
            body['DetectionRuleName'] = request.detection_rule_name
        if not DaraCore.is_null(request.detection_rule_status):
            body['DetectionRuleStatus'] = request.detection_rule_status
        if not DaraCore.is_null(request.detection_rule_type):
            body['DetectionRuleType'] = request.detection_rule_type
        if not DaraCore.is_null(request.entity_mappings):
            body['EntityMappings'] = request.entity_mappings
        if not DaraCore.is_null(request.incident_aggregation_expression):
            body['IncidentAggregationExpression'] = request.incident_aggregation_expression
        if not DaraCore.is_null(request.incident_aggregation_type):
            body['IncidentAggregationType'] = request.incident_aggregation_type
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_category_id):
            body['LogCategoryId'] = request.log_category_id
        if not DaraCore.is_null(request.log_schema_id):
            body['LogSchemaId'] = request.log_schema_id
        if not DaraCore.is_null(request.playbook_parameters):
            body['PlaybookParameters'] = request.playbook_parameters
        if not DaraCore.is_null(request.playbook_uuid):
            body['PlaybookUuid'] = request.playbook_uuid
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schedule_begin_time):
            body['ScheduleBeginTime'] = request.schedule_begin_time
        if not DaraCore.is_null(request.schedule_expression):
            body['ScheduleExpression'] = request.schedule_expression
        if not DaraCore.is_null(request.schedule_max_retries):
            body['ScheduleMaxRetries'] = request.schedule_max_retries
        if not DaraCore.is_null(request.schedule_max_timeout):
            body['ScheduleMaxTimeout'] = request.schedule_max_timeout
        if not DaraCore.is_null(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.schedule_window):
            body['ScheduleWindow'] = request.schedule_window
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDetectionRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDetectionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_detection_rule(
        self,
        request: main_models.UpdateDetectionRuleRequest,
    ) -> main_models.UpdateDetectionRuleResponse:
        runtime = RuntimeOptions()
        return self.update_detection_rule_with_options(request, runtime)

    async def update_detection_rule_async(
        self,
        request: main_models.UpdateDetectionRuleRequest,
    ) -> main_models.UpdateDetectionRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_detection_rule_with_options_async(request, runtime)

    def update_normalization_rule_with_options(
        self,
        tmp_req: main_models.UpdateNormalizationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNormalizationRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateNormalizationRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'json')
        body = {}
        if not DaraCore.is_null(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not DaraCore.is_null(request.extend_field_store_mode):
            body['ExtendFieldStoreMode'] = request.extend_field_store_mode
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_rule_description):
            body['NormalizationRuleDescription'] = request.normalization_rule_description
        if not DaraCore.is_null(request.normalization_rule_expression):
            body['NormalizationRuleExpression'] = request.normalization_rule_expression
        if not DaraCore.is_null(request.normalization_rule_format):
            body['NormalizationRuleFormat'] = request.normalization_rule_format
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not DaraCore.is_null(request.normalization_rule_mode):
            body['NormalizationRuleMode'] = request.normalization_rule_mode
        if not DaraCore.is_null(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not DaraCore.is_null(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNormalizationRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNormalizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_normalization_rule_with_options_async(
        self,
        tmp_req: main_models.UpdateNormalizationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNormalizationRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateNormalizationRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.normalization_rule_ids):
            request.normalization_rule_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.normalization_rule_ids, 'NormalizationRuleIds', 'json')
        body = {}
        if not DaraCore.is_null(request.extend_content_packed):
            body['ExtendContentPacked'] = request.extend_content_packed
        if not DaraCore.is_null(request.extend_field_store_mode):
            body['ExtendFieldStoreMode'] = request.extend_field_store_mode
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_rule_description):
            body['NormalizationRuleDescription'] = request.normalization_rule_description
        if not DaraCore.is_null(request.normalization_rule_expression):
            body['NormalizationRuleExpression'] = request.normalization_rule_expression
        if not DaraCore.is_null(request.normalization_rule_format):
            body['NormalizationRuleFormat'] = request.normalization_rule_format
        if not DaraCore.is_null(request.normalization_rule_id):
            body['NormalizationRuleId'] = request.normalization_rule_id
        if not DaraCore.is_null(request.normalization_rule_ids_shrink):
            body['NormalizationRuleIds'] = request.normalization_rule_ids_shrink
        if not DaraCore.is_null(request.normalization_rule_mode):
            body['NormalizationRuleMode'] = request.normalization_rule_mode
        if not DaraCore.is_null(request.normalization_rule_name):
            body['NormalizationRuleName'] = request.normalization_rule_name
        if not DaraCore.is_null(request.normalization_rule_type):
            body['NormalizationRuleType'] = request.normalization_rule_type
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.order_field):
            body['OrderField'] = request.order_field
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNormalizationRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNormalizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_normalization_rule(
        self,
        request: main_models.UpdateNormalizationRuleRequest,
    ) -> main_models.UpdateNormalizationRuleResponse:
        runtime = RuntimeOptions()
        return self.update_normalization_rule_with_options(request, runtime)

    async def update_normalization_rule_async(
        self,
        request: main_models.UpdateNormalizationRuleRequest,
    ) -> main_models.UpdateNormalizationRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_normalization_rule_with_options_async(request, runtime)

    def update_normalization_schema_with_options(
        self,
        request: main_models.UpdateNormalizationSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNormalizationSchemaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_fields):
            body['NormalizationFields'] = request.normalization_fields
        if not DaraCore.is_null(request.normalization_schema_description):
            body['NormalizationSchemaDescription'] = request.normalization_schema_description
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.normalization_schema_name):
            body['NormalizationSchemaName'] = request.normalization_schema_name
        if not DaraCore.is_null(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNormalizationSchema',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNormalizationSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_normalization_schema_with_options_async(
        self,
        request: main_models.UpdateNormalizationSchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNormalizationSchemaResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.normalization_fields):
            body['NormalizationFields'] = request.normalization_fields
        if not DaraCore.is_null(request.normalization_schema_description):
            body['NormalizationSchemaDescription'] = request.normalization_schema_description
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.normalization_schema_name):
            body['NormalizationSchemaName'] = request.normalization_schema_name
        if not DaraCore.is_null(request.normalization_schema_type):
            body['NormalizationSchemaType'] = request.normalization_schema_type
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNormalizationSchema',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNormalizationSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_normalization_schema(
        self,
        request: main_models.UpdateNormalizationSchemaRequest,
    ) -> main_models.UpdateNormalizationSchemaResponse:
        runtime = RuntimeOptions()
        return self.update_normalization_schema_with_options(request, runtime)

    async def update_normalization_schema_async(
        self,
        request: main_models.UpdateNormalizationSchemaRequest,
    ) -> main_models.UpdateNormalizationSchemaResponse:
        runtime = RuntimeOptions()
        return await self.update_normalization_schema_with_options_async(request, runtime)

    def update_product_with_options(
        self,
        request: main_models.UpdateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_name):
            body['ProductName'] = request.product_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProduct',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_with_options_async(
        self,
        request: main_models.UpdateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_name):
            body['ProductName'] = request.product_name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProduct',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product(
        self,
        request: main_models.UpdateProductRequest,
    ) -> main_models.UpdateProductResponse:
        runtime = RuntimeOptions()
        return self.update_product_with_options(request, runtime)

    async def update_product_async(
        self,
        request: main_models.UpdateProductRequest,
    ) -> main_models.UpdateProductResponse:
        runtime = RuntimeOptions()
        return await self.update_product_with_options_async(request, runtime)

    def update_response_rule_with_options(
        self,
        request: main_models.UpdateResponseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResponseRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.response_action_config):
            body['ResponseActionConfig'] = request.response_action_config
        if not DaraCore.is_null(request.response_action_type):
            body['ResponseActionType'] = request.response_action_type
        if not DaraCore.is_null(request.response_execution_condition):
            body['ResponseExecutionCondition'] = request.response_execution_condition
        if not DaraCore.is_null(request.response_rule_id):
            body['ResponseRuleId'] = request.response_rule_id
        if not DaraCore.is_null(request.response_rule_name):
            body['ResponseRuleName'] = request.response_rule_name
        if not DaraCore.is_null(request.response_rule_priority):
            body['ResponseRulePriority'] = request.response_rule_priority
        if not DaraCore.is_null(request.response_rule_status):
            body['ResponseRuleStatus'] = request.response_rule_status
        if not DaraCore.is_null(request.response_trigger_type):
            body['ResponseTriggerType'] = request.response_trigger_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResponseRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResponseRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_response_rule_with_options_async(
        self,
        request: main_models.UpdateResponseRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResponseRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.response_action_config):
            body['ResponseActionConfig'] = request.response_action_config
        if not DaraCore.is_null(request.response_action_type):
            body['ResponseActionType'] = request.response_action_type
        if not DaraCore.is_null(request.response_execution_condition):
            body['ResponseExecutionCondition'] = request.response_execution_condition
        if not DaraCore.is_null(request.response_rule_id):
            body['ResponseRuleId'] = request.response_rule_id
        if not DaraCore.is_null(request.response_rule_name):
            body['ResponseRuleName'] = request.response_rule_name
        if not DaraCore.is_null(request.response_rule_priority):
            body['ResponseRulePriority'] = request.response_rule_priority
        if not DaraCore.is_null(request.response_rule_status):
            body['ResponseRuleStatus'] = request.response_rule_status
        if not DaraCore.is_null(request.response_trigger_type):
            body['ResponseTriggerType'] = request.response_trigger_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResponseRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResponseRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_response_rule(
        self,
        request: main_models.UpdateResponseRuleRequest,
    ) -> main_models.UpdateResponseRuleResponse:
        runtime = RuntimeOptions()
        return self.update_response_rule_with_options(request, runtime)

    async def update_response_rule_async(
        self,
        request: main_models.UpdateResponseRuleRequest,
    ) -> main_models.UpdateResponseRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_response_rule_with_options_async(request, runtime)

    def update_vendor_with_options(
        self,
        request: main_models.UpdateVendorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVendorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVendor',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVendorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vendor_with_options_async(
        self,
        request: main_models.UpdateVendorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVendorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        if not DaraCore.is_null(request.vendor_name):
            body['VendorName'] = request.vendor_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVendor',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVendorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vendor(
        self,
        request: main_models.UpdateVendorRequest,
    ) -> main_models.UpdateVendorResponse:
        runtime = RuntimeOptions()
        return self.update_vendor_with_options(request, runtime)

    async def update_vendor_async(
        self,
        request: main_models.UpdateVendorRequest,
    ) -> main_models.UpdateVendorResponse:
        runtime = RuntimeOptions()
        return await self.update_vendor_with_options_async(request, runtime)

    def validate_log_store_with_options(
        self,
        request: main_models.ValidateLogStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateLogStoreResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateLogStore',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateLogStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_log_store_with_options_async(
        self,
        request: main_models.ValidateLogStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateLogStoreResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_project_name):
            body['LogProjectName'] = request.log_project_name
        if not DaraCore.is_null(request.log_region_id):
            body['LogRegionId'] = request.log_region_id
        if not DaraCore.is_null(request.log_store_name):
            body['LogStoreName'] = request.log_store_name
        if not DaraCore.is_null(request.log_user_id):
            body['LogUserId'] = request.log_user_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateLogStore',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateLogStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_log_store(
        self,
        request: main_models.ValidateLogStoreRequest,
    ) -> main_models.ValidateLogStoreResponse:
        runtime = RuntimeOptions()
        return self.validate_log_store_with_options(request, runtime)

    async def validate_log_store_async(
        self,
        request: main_models.ValidateLogStoreRequest,
    ) -> main_models.ValidateLogStoreResponse:
        runtime = RuntimeOptions()
        return await self.validate_log_store_with_options_async(request, runtime)

    def validate_normalization_rule_with_options(
        self,
        request: main_models.ValidateNormalizationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateNormalizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.extend_field_store_mode):
            body['ExtendFieldStoreMode'] = request.extend_field_store_mode
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_sample):
            body['LogSample'] = request.log_sample
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_rule_expression):
            body['NormalizationRuleExpression'] = request.normalization_rule_expression
        if not DaraCore.is_null(request.normalization_rule_mode):
            body['NormalizationRuleMode'] = request.normalization_rule_mode
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateNormalizationRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateNormalizationRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_normalization_rule_with_options_async(
        self,
        request: main_models.ValidateNormalizationRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateNormalizationRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.extend_field_store_mode):
            body['ExtendFieldStoreMode'] = request.extend_field_store_mode
        if not DaraCore.is_null(request.lang):
            body['Lang'] = request.lang
        if not DaraCore.is_null(request.log_sample):
            body['LogSample'] = request.log_sample
        if not DaraCore.is_null(request.normalization_category_id):
            body['NormalizationCategoryId'] = request.normalization_category_id
        if not DaraCore.is_null(request.normalization_rule_expression):
            body['NormalizationRuleExpression'] = request.normalization_rule_expression
        if not DaraCore.is_null(request.normalization_rule_mode):
            body['NormalizationRuleMode'] = request.normalization_rule_mode
        if not DaraCore.is_null(request.normalization_schema_id):
            body['NormalizationSchemaId'] = request.normalization_schema_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_for):
            body['RoleFor'] = request.role_for
        if not DaraCore.is_null(request.vendor_id):
            body['VendorId'] = request.vendor_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateNormalizationRule',
            version = '2024-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateNormalizationRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_normalization_rule(
        self,
        request: main_models.ValidateNormalizationRuleRequest,
    ) -> main_models.ValidateNormalizationRuleResponse:
        runtime = RuntimeOptions()
        return self.validate_normalization_rule_with_options(request, runtime)

    async def validate_normalization_rule_async(
        self,
        request: main_models.ValidateNormalizationRuleRequest,
    ) -> main_models.ValidateNormalizationRuleResponse:
        runtime = RuntimeOptions()
        return await self.validate_normalization_rule_with_options_async(request, runtime)
